# Kit d’amorçage pour l’équipe

Les archives sont générées dans `outputs/` par :

```sh
python3 scripts/build-starter-kit.py
```

Distribuer `vibe-coding-starter-kit-1.0.0.zip` sur macOS, Windows ou Linux. Le seul prérequis de l’initialisation est Python 3 ; elle n’utilise aucune dépendance externe.

## Initialiser un projet PHP et Python

Après extraction de l’archive :

```sh
python3 init-project.py \
  --name "Mon produit" \
  --destination ../mon-produit \
  --owner "Mon équipe" \
  --stacks php,python \
  --php-version "<VERSION_PHP_EXACTE>" \
  --python-version "<VERSION_PYTHON_EXACTE>" \
  --github-repository owner/mon-produit
```

Remplacer les deux valeurs entre chevrons par les versions décidées par l’équipe, au format `X.Y.Z`. L’initialiseur refuse une destination existante, prépare les squelettes sélectionnés et initialise Git sur `main`. Il n’écrase jamais un projet local.

## Finalisation obligatoire

1. Compléter le cahier des charges créé dans `docs/ai/PROJECT_BRIEF.md`.
2. Décider les commandes de formatage, test et build.
3. Pour PHP, produire et committer `composer.lock` via `composer install`.
4. Pour Python, compléter `requirements.lock.txt` avec des versions et hashes exacts.
5. Exécuter `make verify`, committer, puis pousser sur le dépôt GitHub.

Le cahier des charges est volontairement créé au statut `BROUILLON`, donc `make verify` échoue tant que l’équipe n’a pas renseigné le produit. Cela évite de démarrer du code sur une spécification vide.
