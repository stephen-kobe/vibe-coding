# Décisions d’architecture

## ADR-001 — Contrat canonique et adaptateurs par moteur

- Statut : accepté
- Contexte : les moteurs IA de VS Code ne documentent pas tous le même nom ni le même emplacement de fichier d’instructions.
- Décision : `docs/ai/AI_CONTRACT.md` est la source canonique. `AGENTS.md`, `CLAUDE.md` et `.github/copilot-instructions.md` sont des adaptateurs générés, volontairement identiques, contrôlés par `scripts/check-ai-contract.sh`.
- Conséquences : un modèle compatible avec son adaptateur voit le même contenu. Un moteur qui ne lit aucun de ces formats doit être configuré explicitement ou écarté ; il n’existe pas de mécanisme portable pour le forcer.

## ADR-002 — Reproductibilité par entrée figée et vérification

- Statut : accepté
- Contexte : deux modèles ne produisent pas nécessairement le même code à partir d’une même demande, même avec les mêmes consignes.
- Décision : la reproductibilité porte sur les entrées versionnées, les dépendances verrouillées, les outils fixés et les sorties générées déterministes. Le code IA n’est accepté qu’après tests, revue et commit Git immuable.
- Conséquences : un futur projet doit déclarer sa version de langage, son gestionnaire de dépendances, son fichier de verrouillage et ses commandes de build dans son cahier des charges avant le premier code métier.

## ADR-003 — Double pile PHP et Python

- Statut : accepté
- Contexte : le dépôt vise principalement des applications et outils PHP et Python, avec des gestionnaires de dépendances différents.
- Décision : chaque composant choisit une seule pile principale, documente son chemin, son runtime exact et ses commandes dans le cahier des charges. PHP utilise Composer avec `composer.lock` ; Python utilise `pip` avec un fichier de verrouillage incluant les hashes. Les politiques détaillées sont dans `docs/STACK_POLICY.md`.
- Conséquences : les versions de PHP et Python doivent être décidées avant d’ajouter un dev container ou une CI de build. Aucun `composer update` ni installation Python non verrouillée n’est admis dans une CI reproductible.
