# Reproductibilité

## Ce qui peut être garanti

À partir du même commit Git, `make sync-ai-instructions` produit les mêmes trois fichiers d’instructions octet pour octet. `make verify` vérifie cette propriété et la structure du cahier des charges.

Pour une application métier, la garantie de reconstruction doit être définie comme : même commit + même environnement + mêmes outils + mêmes dépendances verrouillées + mêmes paramètres de build = mêmes sources générées et, lorsque la pile le permet, mêmes artefacts binaires.

## Ce qui ne peut pas être garanti par les règles seules

Un modèle IA n’est pas un compilateur déterministe. Deux modèles — et parfois deux exécutions du même modèle — peuvent proposer un code différent. Les règles diminuent cette variabilité, mais ne la suppriment pas. Le résultat de référence est donc le commit revu et validé, pas une nouvelle génération libre par l’IA.

## Exigences de chaque projet produit

Avant le premier build, compléter le cahier des charges avec :

1. version exacte du langage et du gestionnaire de dépendances ;
2. fichier de verrouillage commité ;
3. image de développement ou dev container figé par digest si des conteneurs sont employés ;
4. commandes sans interaction de formatage, vérification, test et build ;
5. variables d’environnement non secrètes, avec valeurs par défaut documentées ;
6. variable `SOURCE_DATE_EPOCH` ou mécanisme équivalent lorsque la pile génère des artefacts horodatés ;
7. manifeste des artefacts avec hashes SHA-256, si l’artefact distribué doit être identique octet pour octet.

Un dev container n’est volontairement pas fourni ici : son image, ses extensions et ses dépendances dépendent de la pile technique qui n’a pas été choisie. Ajouter un conteneur générique non figé donnerait une fausse garantie de reproductibilité.

## Vérification de reconstruction à adopter dans un projet produit

1. Partir de deux répertoires propres au même commit.
2. Installer uniquement depuis les fichiers de verrouillage, en mode immuable ou équivalent.
3. Exécuter les mêmes commandes de build avec le même environnement.
4. Comparer les hashes des artefacts ou les arbres de sources générés.
5. Faire échouer la CI si les comparaisons diffèrent.
