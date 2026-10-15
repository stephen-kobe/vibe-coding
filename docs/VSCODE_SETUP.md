# Configuration de Visual Studio Code

## Mise en route

1. Installer une version stable prise en charge par l’organisation, puis ouvrir **la racine** du dépôt dans VS Code.
2. Installer les extensions recommandées par `.vscode/extensions.json` si elles sont utiles au projet. Elles sont des recommandations, pas une garantie de reproductibilité.
3. Lancer la tâche VS Code **Verify AI contract** ou exécuter `make verify` dans le terminal intégré.
4. Utiliser l’assistant IA choisi uniquement après avoir ouvert le dépôt à sa racine : les fichiers d’instructions sont alors découvrables par le moteur qui les prend en charge.

## Compatibilité des assistants

| Assistant / moteur | Fichier projet prévu | Rôle dans ce dépôt |
| --- | --- | --- |
| GitHub Copilot | `.github/copilot-instructions.md` | Adaptateur contrôlé du contrat canonique |
| Anthropic Claude | `CLAUDE.md` | Adaptateur contrôlé du contrat canonique |
| OpenAI Codex | `AGENTS.md` | Adaptateur contrôlé du contrat canonique |

VS Code documente ces emplacements séparément. Un fichier pris en charge par un moteur n’est pas automatiquement pris en charge par tous les autres. Vérifier l’indicateur d’instructions du moteur choisi sur une tâche représentative avant de l’adopter pour l’équipe.

## Paramètres versionnés

`.vscode/settings.json` impose seulement des conventions de texte partageables et active, pour Copilot, l’usage des instructions de dépôt. Les identifiants, modèles, jetons et préférences personnelles ne doivent pas être versionnés.

## Procédure quotidienne

1. Créer une branche depuis `main`.
2. Vérifier ou mettre à jour `docs/ai/PROJECT_BRIEF.md` avant de demander une modification à l’IA.
3. Demander un petit changement traçable, vérifier le diff, puis exécuter les commandes de la section 8 du cahier des charges.
4. Ouvrir une pull request, attendre la CI et effectuer une revue humaine.
