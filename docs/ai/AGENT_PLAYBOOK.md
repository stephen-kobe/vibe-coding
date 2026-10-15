# Guide opérationnel des agents IA

Ce guide complète le [contrat canonique](AI_CONTRACT.md), le [catalogue numéroté de 91 règles](RULES_CATALOG.md), les [standards de développement](DEVELOPMENT_STANDARDS.md) et les [décisions d'architecture](ARCHITECTURE_DECISIONS.md). Les agents Codex, Claude et Copilot s'alignent sur le même contrat généré. Les règles de sécurité et les droits réels restent appliqués par la plateforme, GitHub et la CI : une instruction Markdown ne constitue pas une permission technique.

## Quatre niveaux de gouvernance

| Niveau | Dispositif | Finalité |
| --- | --- | --- |
| Gouvernance de l’agent | `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md` générés depuis `AI_CONTRACT.md` | Encadrer méthode de travail, autonomie, revue et transparence. |
| Gouvernance architecturale | `RULES_CATALOG.md`, `DEVELOPMENT_STANDARDS.md`, ADR et cahier des charges | Préserver modules, contrats et décisions techniques. |
| Gouvernance de la qualité | Linters, tests, analyses statiques, sécurité et CI propres au projet | Vérifier par des outils les contraintes déterministes. |
| Gouvernance humaine | Revues, décisions, permissions et protections de branches | Valider les décisions risquées ; ne pas laisser l’agent redéfinir seul le cadre. |

## Les 15 règles prioritaires

| Ordre | ID(s) indicatifs | Objectif |
| --- | --- | --- |
| 1 | ARC-01 | Respecter l’architecture existante et prévenir les dérives. |
| 2 | AI-02 | Comprendre le besoin avant de coder. |
| 3 | DEV-01, DEV-03 | Appliquer KISS et YAGNI. |
| 4 | ARC-03, ARC-04 | Respecter les frontières des modules. |
| 5 | DEV-10 | Réutiliser les composants existants. |
| 6 | PRJ-02, AI-04 | Ne pas modifier le code hors périmètre. |
| 7 | ARC-10, DATA-02 | Préserver contrats et rétrocompatibilité. |
| 8 | SEC-01 à SEC-10 | Appliquer les règles de sécurité. |
| 9 | QA-01 à QA-05 | Générer les tests pertinents. |
| 10 | QA-06, QA-07, QA-10 | Exécuter les contrôles qualité. |
| 11 | AI-13 | Ne jamais masquer un échec. |
| 12 | ARC-12, AI-14 | Documenter les décisions structurantes. |
| 13 | AI-12 | Demander validation pour les décisions critiques. |
| 14 | AI-11, PRJ-08 | Présenter les modifications et impacts. |
| 15 | AI-15 | Ne déclarer la tâche terminée qu’après vérification. |

## Autonomie de l’agent : matrice de décision

| Action | Autonomie attendue |
| --- | --- |
| Ajouter une fonction dans un service existant, corriger un bug localisé, ajouter des tests | Autonome dans le périmètre et les permissions accordées. |
| Refactoriser une fonction dans le périmètre demandé | Autonome si les contrats et le comportement sont préservés. |
| Ajouter une dépendance ou un nouveau module | Vérifier licences, alternatives, contraintes et demander validation si l’architecture change. |
| Rompre un contrat d’API, changer la pile ou l’architecture | Validation humaine préalable et ADR. |
| Migration destructive, suppression de données, changement d’autorisation, déploiement en production | Validation humaine explicite et procédure autorisée ; aucune auto-autorisation. |

## Méthode standard : avant, pendant et après

1. **Avant** : identifier contexte, objectif métier, périmètre, contraintes, comportements attendus, critères d’acceptation, validations et restrictions. Examiner le code existant et lire les règles `ARC-..`, `DEV-..`, `DATA-..`, `SEC-..`, `QA-..`, `PRJ-..`, `OPS-..`, `AI-..` pertinentes ; ne pas inventer de spécification.
2. **Planifier si nécessaire** : pour une évolution structurante, proposer étapes, impacts, risques et ADR. Pour une correction simple, intervenir directement dans le cadre convenu.
3. **Pendant** : privilégier une solution simple, le réemploi et les changements atomiques ; tester progressivement. Ne jamais exécuter d’opération destructive sans autorisation.
4. **Après** : relire le diff, exécuter les vérifications adaptées au risque, mettre à jour les documents touchés, présenter fichiers modifiés, règles concernées, preuves, exceptions et limites.

## Exemple de prompt à Codex

> **Contexte** : le service utilisateur existant gère la création des comptes.
>
> **Objectif** : permettre la désactivation sans suppression de données.
>
> **Périmètre et contraintes** : réutiliser les composants actuels, préserver les API et l’authentification, ne pas ajouter de dépendance.
>
> **Comportement attendu** : un compte désactivé ne s’authentifie plus ; seuls les administrateurs autorisés peuvent le désactiver ; l’opération est tracée ; les données restent conservées.
>
> **Critères d’acceptation et validation** : permissions respectées, tests unitaires/intégration pertinents, absence de régression.
>
> **Méthode** : lire `AGENTS.md`, `RULES_CATALOG.md` et les documents applicables ; analyser puis planifier si le changement est structurant ; développer, vérifier et rendre compte.

## Contrôles possibles et preuve réelle

| Objectif | Moyen technique à configurer pour chaque projet |
| --- | --- |
| Nommage, format, typage | Linter, formateur et analyseur de types propres au langage. |
| Frontières architecturales et cycles | Règles d’import et tests d’architecture. |
| Secrets, dépendances et vulnérabilités | Détecteur de secrets, analyse de dépendances et SAST. |
| Non-régression et API | Tests unitaires, intégration et tests de contrat. |
| Revue et droits | Protection GitHub, contrôles CI requis et validation humaine. |
| Intégrité des règles et synchronisation des assistants | `make verify`, `scripts/check-rules-catalog.sh`, `scripts/check-ai-contract.sh`. |

La CI de ce dépôt est **un contrôle documentaire et structurel**, pas un certificat de conformité du code métier. Les règles à revue humaine ne peuvent pas être certifiées par simple lecture de leur présence dans un fichier.

## Convention de gestion des règles

Chaque identifiant désigne une règle stable : préserver l’ID lors de toute reformulation ; modifier la description ou priorité par PR revue et vérifier les impacts. Ajouter ou retirer une règle implique de décider explicitement de la version du catalogue et d’adapter le script de contrôle, la documentation, le cahier des charges et les adaptateurs régénérés.

## Livraison

Une PR doit mentionner les IDs applicables, l’impact architecture/API/données/sécurité/tests/exploitation, les commandes réellement exécutées, les approbations nécessaires et la stratégie de retour arrière. Les décisions structurantes utilisent les ADR ; le plan de livraison est dans le cahier des charges. Ne pas fusionner un changement qui échoue à la CI, et ne pas présumer que « contrôlé structurellement » signifie « conforme sémantiquement ».
