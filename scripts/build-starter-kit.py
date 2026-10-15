#!/usr/bin/env python3
"""Construit les archives portables du kit d’amorçage depuis le dépôt courant."""

from __future__ import annotations

import shutil
import subprocess
import tarfile
import tempfile
import zipfile
from datetime import datetime, timezone
from gzip import GzipFile
from os import environ
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "vibe-coding-starter-kit-1.0.0"
EXCLUDED_TOP_LEVEL = {".git", "outputs", "work", "starter-kit"}
EXCLUDED_FILES = {Path("scripts/build-starter-kit.py")}


def should_copy(path: Path) -> bool:
    relative = path.relative_to(REPOSITORY_ROOT)
    return relative.parts[0] not in EXCLUDED_TOP_LEVEL and relative not in EXCLUDED_FILES


def copy_template(destination: Path) -> None:
    for source in REPOSITORY_ROOT.rglob("*"):
        if not should_copy(source):
            continue
        relative = source.relative_to(REPOSITORY_ROOT)
        target = destination / relative
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
        elif source.is_file():
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)


def source_date_epoch() -> int:
    configured = environ.get("SOURCE_DATE_EPOCH")
    if configured and configured.isdigit():
        return int(configured)
    return int(
        subprocess.check_output(
            ["git", "show", "-s", "--format=%ct", "HEAD"], cwd=REPOSITORY_ROOT, text=True
        ).strip()
    )


def create_archives(package_directory: Path, output_directory: Path, epoch: int) -> None:
    zip_path = output_directory / f"{PACKAGE_NAME}.zip"
    tar_path = output_directory / f"{PACKAGE_NAME}.tar.gz"
    timestamp = datetime.fromtimestamp(epoch, tz=timezone.utc).timetuple()[:6]
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in sorted(package_directory.rglob("*")):
            if file_path.is_file():
                entry = zipfile.ZipInfo(str(file_path.relative_to(package_directory.parent)), timestamp)
                entry.compress_type = zipfile.ZIP_DEFLATED
                entry.external_attr = 0o100644 << 16
                archive.writestr(entry, file_path.read_bytes())
    with tar_path.open("wb") as raw_file:
        with GzipFile(filename="", mode="wb", fileobj=raw_file, mtime=epoch) as compressed_file:
            with tarfile.open(fileobj=compressed_file, mode="w") as archive:
                for file_path in sorted(package_directory.rglob("*")):
                    relative = file_path.relative_to(package_directory.parent)
                    info = archive.gettarinfo(str(file_path), arcname=str(relative))
                    info.mtime = epoch
                    info.uid = 0
                    info.gid = 0
                    info.uname = ""
                    info.gname = ""
                    if file_path.is_file():
                        with file_path.open("rb") as file_handle:
                            archive.addfile(info, file_handle)
                    else:
                        archive.addfile(info)


def main() -> int:
    subprocess.run(["make", "verify"], cwd=REPOSITORY_ROOT, check=True)
    output_directory = REPOSITORY_ROOT / "outputs"
    output_directory.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="vibe-coding-starter-") as temporary:
        temporary_root = Path(temporary)
        package_directory = temporary_root / PACKAGE_NAME
        package_directory.mkdir()
        shutil.copy2(REPOSITORY_ROOT / "starter-kit" / "init-project.py", package_directory / "init-project.py")
        shutil.copy2(REPOSITORY_ROOT / "starter-kit" / "README.md", package_directory / "README.md")
        copy_template(package_directory / "template")
        create_archives(package_directory, output_directory, source_date_epoch())
    print(f"Archives créées dans {output_directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
