# Livraison GitHub

## Règle de dépôt

Le code source, le cahier des charges, les décisions, les fichiers de verrouillage et la CI sont versionnés dans Git puis publiés dans un dépôt GitHub. Les secrets restent dans le gestionnaire de secrets GitHub ou un coffre externe ; ils ne sont jamais committés.

## Création contrôlée du dépôt distant

Le dépôt cible est `stephen-kobe/vibe-coding`. Sa visibilité n’est pas encore définie. Après décision, créer le dépôt vide sans README, licence ni `.gitignore` distants, puis publier ce dépôt local. GitHub documente la création et l’envoi d’un dépôt local avec `gh repo create --source=. --private|--public --push`.

Avant le premier merge, activer au minimum :

1. protection de `main` avec pull request et vérification CI obligatoire ;
2. revue requise selon la politique de l’équipe ;
3. permissions GitHub Actions en lecture seule par défaut ;
4. alertes et mises à jour de dépendances adaptées à la politique de l’organisation ;
5. règles de gestion des secrets et des collaborateurs.

## CI fournie

`.github/workflows/verify.yml` exécute `make verify` sur push et pull request, avec `contents: read`. L’action de récupération est épinglée sur un SHA complet. Les futurs workflows doivent appliquer la même règle ou être protégés par un fichier de verrouillage des dépendances Actions.
