<!-- GENERATED from docs/ai/AI_CONTRACT.md; run make sync-ai-instructions -->

# Contrat IA du dépôt

## 1. Hiérarchie des sources de vérité

En cas de conflit, appliquer la première règle applicable dans cet ordre :

1. Les instructions système, la loi applicable et les contraintes de sécurité de la plateforme.
2. Les règles non négociables de ce dépôt, dont la confidentialité, la sécurité et la reproductibilité.
3. Le cahier des charges du projet : [`PROJECT_BRIEF.md`](PROJECT_BRIEF.md).
4. Les décisions d’architecture : [`ARCHITECTURE_DECISIONS.md`](ARCHITECTURE_DECISIONS.md).
5. Les règles les plus proches du code modifié, si elles existent et ne contredisent pas les niveaux précédents.
6. La demande courante, si elle ne contredit pas les niveaux précédents.

Ne jamais deviner une exigence produit, un secret, une dépendance, une autorisation de déploiement ou une décision d’architecture. Documenter l’incertitude, puis demander la précision indispensable avant de poursuivre.

## 2. Procédure obligatoire avant toute modification

1. Lire ce contrat, `PROJECT_BRIEF.md` et `ARCHITECTURE_DECISIONS.md`.
2. Vérifier que le besoin, les critères d’acceptation et la commande de vérification sont complets et non contradictoires.
3. Énoncer les hypothèses vérifiables ; interrompre le travail lorsqu’une information indispensable manque.
4. Limiter le changement au besoin demandé. Ne pas mélanger refactoring opportuniste et évolution produit.
5. Mettre à jour la documentation et les tests affectés dans la même modification.

## 3. Règles de développement

1. Écrire du code déterministe : pas de date, d’aléa, de réseau ou d’état global implicite dans les tests ou la génération de fichiers.
2. Ajouter ou mettre à jour un test automatisé pour chaque comportement modifié, sauf exemption écrite dans le cahier des charges.
3. Échouer explicitement face aux entrées invalides ; ne pas masquer une erreur par une valeur par défaut non documentée.
4. Ne jamais ajouter de secret, jeton, clé privée, mot de passe ou données personnelles au dépôt, aux journaux ou aux tests.
5. Fixer les versions des outils et dépendances dans les fichiers de verrouillage du langage choisi. Ne pas modifier un verrouillage sans justifier le changement.
6. Utiliser des fichiers texte UTF-8, des fins de ligne LF et une ligne vide finale.
7. Conserver des fonctions et modules petits, nommés selon le domaine et sans dépendance circulaire.

## 4. Règles GitHub et qualité

1. Toute modification passe par Git, une branche dédiée, une revue et une intégration sur GitHub ; ne jamais contourner la vérification CI.
2. La CI doit exécuter les mêmes commandes que le poste local et bloquer une intégration si elles échouent.
3. Accorder le minimum de permissions aux workflows. Référencer les GitHub Actions externes par SHA complet vérifié ou par un fichier de verrouillage des actions.
4. Examiner le diff avant le commit et ne commiter que les fichiers relevant du changement.
5. Utiliser un message de commit conventionnel : `type(scope): résumé à l’impératif`.

## 5. Contrat de sortie d’un agent

Avant de considérer une tâche terminée, l’agent doit fournir :

1. Les fichiers modifiés et la raison fonctionnelle.
2. Les commandes exécutées et leur résultat.
3. Les limites, hypothèses ou vérifications non réalisées.
4. Une mise à jour du cahier des charges ou des décisions d’architecture si elles ont changé.

## 6. Limite explicite

Ce contrat uniformise les instructions disponibles dans le dépôt. Il ne peut pas garantir qu’un modèle, une extension ou un outil tiers les charge ni les respecte. La conformité est donc contrôlée par les fichiers versionnés, la revue humaine et la CI, et non par une promesse sur le comportement d’un modèle.
