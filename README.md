# Socle de vibe coding pour VS Code

Ce dépôt fournit une base commune pour utiliser plusieurs assistants IA dans Visual Studio Code avec des règles, un cahier des charges et des contrôles versionnés.

Projet d’AI vibe coding.

## Démarrage

```sh
make verify
```

Pour ouvrir un nouveau projet produit :

1. copier `docs/ai/PROJECT_BRIEF.template.md` vers `docs/ai/PROJECT_BRIEF.md` ;
2. compléter chaque section avant de générer du code ;
3. choisir et verrouiller la pile technique, les dépendances et les commandes de build ;
4. exécuter `make verify`, puis publier le dépôt sur GitHub.

## Points d’entrée

- [Configuration VS Code](docs/VSCODE_SETUP.md)
- [Contrat IA](docs/ai/AI_CONTRACT.md)
- [Cahier des charges](docs/ai/PROJECT_BRIEF.md)
- [Reproductibilité](docs/REPRODUCIBILITY.md)
- [Politique PHP et Python](docs/STACK_POLICY.md)
- [Kit d’amorçage équipe](docs/STARTER_KIT.md)
- [Livraison GitHub](docs/GITHUB_DELIVERY.md)
- [Sources](docs/SOURCES.md)

## Garantie réaliste

Le dépôt garantit que les adaptateurs d’instructions sont reconstruits à l’identique depuis le contrat versionné. Il ne prétend pas qu’un modèle IA, par nature non déterministe et doté de son propre mécanisme de découverte des instructions, générera spontanément le même code qu’un autre modèle. La référence est le commit Git revu, testé et verrouillé.
