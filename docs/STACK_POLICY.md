# Politique de piles : PHP et Python

## 1. Règle de séparation

Un composant possède une pile principale : PHP **ou** Python. Si les deux sont nécessaires, les isoler dans des répertoires explicites et leur attribuer leurs propres tests, dépendances et commandes. Une organisation possible est :

```text
apps/
  php-api/
  python-worker/
packages/
  php-*/
  python-*/
```

Cette arborescence est un modèle, pas une contrainte à créer avant qu’un cahier des charges le justifie.

## 2. Composants PHP

Chaque composant PHP doit contenir et versionner :

1. `composer.json`, décrivant les dépendances directes et les scripts ;
2. `composer.lock`, résultat validé de la résolution ;
3. la version exacte de PHP dans le cahier des charges et l’environnement de développement ;
4. les commandes non interactives de qualité, test et build.

En intégration continue, installer avec `composer install --no-interaction --prefer-dist --no-progress` à partir de `composer.lock`. Utiliser `composer update` seulement dans une pull request dédiée de mise à jour des dépendances, puis committer le nouveau verrouillage.

## 3. Composants Python

Chaque composant Python doit contenir et versionner :

1. `pyproject.toml`, décrivant le projet et ses contraintes ;
2. un fichier de verrouillage dédié, par exemple `requirements.lock.txt`, contenant les versions exactes et hashes ;
3. la version exacte de Python dans le cahier des charges et l’environnement de développement ;
4. les commandes non interactives de qualité, test et build.

En intégration continue, installer le verrouillage avec `python -m pip install --require-hashes --no-deps -r requirements.lock.txt`. Générer ce fichier dans une pull request dédiée et conserver l’outil de génération, sa version et la commande utilisés.

## 4. Runtimes et conteneurs

Les versions de PHP et Python ne sont pas encore fournies. Ne pas écrire `latest`, une image flottante ou une plage de versions pour satisfaire artificiellement la reproductibilité. Après décision, figer :

- la version de runtime ;
- l’image de base par digest si un conteneur est utilisé ;
- les extensions VS Code nécessaires avec leurs versions lorsqu’elles influencent le build ;
- les fichiers de verrouillage et les commandes CI correspondantes.

## 5. Vérification par composant

La section 8 du cahier des charges doit déclarer les commandes précises de chaque composant. La CI exécute ces mêmes commandes, sans installation globale cachée ni téléchargement non verrouillé.
