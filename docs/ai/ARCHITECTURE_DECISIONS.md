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

## ADR-004 — Standards centralisés et contrôle structurel

- Statut : accepté
- Contexte : le contrat IA devait porter des règles concrètes d’architecture, qualité, API/données, sécurité, tests et exploitation sans créer une architecture imposée.
- Décision : `docs/ai/DEVELOPMENT_STANDARDS.md` devient la référence détaillée, liée par le contrat IA. Le cahier des charges comporte un plan de livraison et retour arrière. `make verify` contrôle la présence et les points d’ancrage de cette gouvernance.
- Conséquences : les assistants disposent d’un référentiel court et versionné ; les changements structurants doivent citer un ADR, et le contrôle automatique détecte une suppression accidentelle des repères de gouvernance sans prétendre analyser sémantiquement le code.

## ADR-005 — Catalogue exhaustif et traçabilité des règles

- Statut : accepté
- Contexte : les standards synthétiques n'explicitaient pas les 91 règles identifiées, leurs priorités et leur vérification.
- Décision : `docs/ai/RULES_CATALOG.md` devient le référentiel exhaustif de 91 règles ARC, DEV, DATA, SEC, QA, PRJ, OPS et AI ; le contrat canonique le référence, `docs/ai/AGENT_PLAYBOOK.md` décrit leur application et `make verify` en contrôle l'intégrité structurelle.
- Conséquences : les changements peuvent citer chaque ID ; l'automatisation n'atteste pas de la qualité sémantique du code produit et la revue humaine conserve sa place.
