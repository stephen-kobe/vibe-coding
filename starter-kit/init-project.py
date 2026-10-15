#!/usr/bin/env python3
"""Initialise un projet à partir du kit Vibe Coding, sans dépendance externe."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path


def parse_stacks(raw_value: str) -> list[str]:
    stacks = [item.strip().lower() for item in raw_value.split(",") if item.strip()]
    if not stacks or any(item not in {"php", "python"} for item in stacks):
        raise ValueError("--stacks doit contenir php, python, ou php,python.")
    if len(stacks) != len(set(stacks)):
        raise ValueError("Chaque pile ne peut être déclarée qu’une fois.")
    return stacks


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        raise ValueError("Le nom doit contenir au moins une lettre ou un chiffre ASCII.")
    return slug


def replace_tokens(path: Path, values: dict[str, str]) -> None:
    content = path.read_text(encoding="utf-8")
    for token, value in values.items():
        content = content.replace(f"[{token}]", value)
    path.write_text(content, encoding="utf-8", newline="\n")


def write_project_readme(destination: Path, project_name: str, stacks: list[str]) -> None:
    stack_label = " et ".join(stack.upper() if stack == "php" else "Python" for stack in stacks)
    destination.joinpath("README.md").write_text(
        f"# {project_name}\n\n"
        f"Projet initialisé avec le socle Vibe Coding pour {stack_label}.\n\n"
        "## Avant le premier développement\n\n"
        "1. Compléter `docs/ai/PROJECT_BRIEF.md`.\n"
        "2. Décider des commandes de formatage, test et build.\n"
        "3. Verrouiller les dépendances de chaque composant.\n"
        "4. Exécuter `make verify`. La commande échoue volontairement tant que le cahier des charges est au statut BROUILLON.\n",
        encoding="utf-8",
        newline="\n",
    )


def create_php_component(destination: Path, project_slug: str, owner_slug: str, php_version: str) -> None:
    component = destination / "apps" / "php"
    component.mkdir(parents=True)
    composer = {
        "name": f"{owner_slug}/{project_slug}-php",
        "description": "PHP component initialized by vibe-coding-starter-kit",
        "type": "project",
        "require": {"php": php_version},
        "config": {"platform": {"php": php_version}, "sort-packages": True},
        "scripts": {"test": "@php -v"},
    }
    component.joinpath("composer.json").write_text(
        json.dumps(composer, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    component.joinpath("README.md").write_text(
        "# Composant PHP\n\n"
        f"Runtime requis : PHP {php_version}.\n\n"
        "Avant le premier commit applicatif, exécuter `composer install --no-interaction --prefer-dist --no-progress` "
        "puis versionner le `composer.lock` produit.\n",
        encoding="utf-8",
        newline="\n",
    )


def create_python_component(destination: Path, project_slug: str, python_version: str) -> None:
    component = destination / "apps" / "python"
    component.mkdir(parents=True)
    module_name = project_slug.replace("-", "_")
    pyproject = (
        "[project]\n"
        f'name = "{project_slug}-python"\n'
        'version = "0.1.0"\n'
        'description = "Python component initialized by vibe-coding-starter-kit"\n'
        'readme = "README.md"\n'
        f'requires-python = "=={python_version}"\n'
        'dependencies = []\n'
    )
    component.joinpath("pyproject.toml").write_text(pyproject, encoding="utf-8", newline="\n")
    component.joinpath("requirements.lock.txt").write_text(
        "# Lock file for pip. Add only exact versions with --hash=sha256:… values.\n"
        "# Installation: python -m pip install --require-hashes --no-deps -r requirements.lock.txt\n",
        encoding="utf-8",
        newline="\n",
    )
    source_dir = component / "src" / module_name
    source_dir.mkdir(parents=True)
    source_dir.joinpath("__init__.py").write_text("", encoding="utf-8")
    component.joinpath("README.md").write_text(
        "# Composant Python\n\n"
        f"Runtime requis : Python {python_version}.\n\n"
        "Ajouter les dépendances dans `pyproject.toml`, puis régénérer `requirements.lock.txt` avec des hashes "
        "avant de les installer dans la CI.\n",
        encoding="utf-8",
        newline="\n",
    )


def initialize_git(destination: Path, github_repository: str | None) -> None:
    if shutil.which("git") is None:
        print("Git est absent : initialisation Git ignorée.", file=sys.stderr)
        return
    subprocess.run(["git", "init", "-b", "main"], cwd=destination, check=True)
    if github_repository:
        subprocess.run(
            ["git", "remote", "add", "origin", f"https://github.com/{github_repository}.git"],
            cwd=destination,
            check=True,
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialise un projet Vibe Coding reproductible.")
    parser.add_argument("--name", required=True, help="Nom lisible du projet.")
    parser.add_argument("--destination", required=True, help="Répertoire à créer ; il ne doit pas exister.")
    parser.add_argument("--owner", required=True, help="Équipe ou propriétaire du projet.")
    parser.add_argument("--stacks", required=True, help="php, python, ou php,python.")
    parser.add_argument("--php-version", help="Version PHP exacte, requise si php est sélectionné.")
    parser.add_argument("--python-version", help="Version Python exacte, requise si python est sélectionné.")
    parser.add_argument("--github-repository", help="Dépôt GitHub existant au format owner/name.")
    parser.add_argument("--no-git", action="store_true", help="Ne pas initialiser Git.")
    args = parser.parse_args()

    try:
        stacks = parse_stacks(args.stacks)
        project_slug = slugify(args.name)
        owner_slug = slugify(args.owner)
    except ValueError as error:
        parser.error(str(error))

    if "php" in stacks and not args.php_version:
        parser.error("--php-version est requis lorsque php est sélectionné.")
    if "python" in stacks and not args.python_version:
        parser.error("--python-version est requis lorsque python est sélectionné.")
    if args.github_repository and not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", args.github_repository):
        parser.error("--github-repository doit être au format owner/name.")

    package_root = Path(__file__).resolve().parent
    template = package_root / "template"
    destination = Path(args.destination).expanduser().resolve()
    if not template.is_dir():
        parser.error("Le dossier template est absent du kit.")
    if destination.exists():
        parser.error(f"Le répertoire de destination existe déjà : {destination}")

    shutil.copytree(template, destination)
    brief = destination / "docs" / "ai" / "PROJECT_BRIEF.md"
    shutil.copy2(destination / "docs" / "ai" / "PROJECT_BRIEF.template.md", brief)
    replace_tokens(
        brief,
        {
            "NOM_PROJET": args.name,
            "NOM_OU_EQUIPE": args.owner,
            "URL_GITHUB": f"https://github.com/{args.github_repository}" if args.github_repository else "À créer",
            "SEMVER": "0.1.0",
        },
    )
    write_project_readme(destination, args.name, stacks)
    if "php" in stacks:
        create_php_component(destination, project_slug, owner_slug, args.php_version)
    if "python" in stacks:
        create_python_component(destination, project_slug, args.python_version)
    if not args.no_git:
        initialize_git(destination, args.github_repository)

    print(f"Projet créé : {destination}")
    print("Complétez docs/ai/PROJECT_BRIEF.md, puis exécutez make verify.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
