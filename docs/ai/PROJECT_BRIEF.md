# Cahier des charges projet

> Statut : ACTIF — Ce dépôt met en place le socle de vibe coding reproductible. Copier `PROJECT_BRIEF.template.md` et remplacer intégralement ce fichier au démarrage d’un produit.

## 1. Identité

- Nom : Socle de vibe coding VS Code
- Propriétaire produit : À désigner avant le premier projet produit
- Dépôt GitHub : https://github.com/stephen-kobe/vibe-coding
- Version de la spécification : 1.1.0

## 2. Problème et résultat attendu

Fournir un cadre versionné pour que plusieurs assistants IA configurés dans Visual Studio Code appliquent les mêmes règles de développement et lisent le même cahier des charges.

## 3. Périmètre

Inclus : contrat IA, standards d’architecture et de développement, modèle de cahier des charges, ADR, réglages VS Code, contrôle GitHub, documentation de reproductibilité et politiques PHP/Python.

Exclus : une application métier, le choix des versions de runtime, la création du dépôt GitHub distant et le déploiement en production.

## 4. Utilisateurs et cas d’usage

- Développeur : ouvre le dépôt dans VS Code, choisit son assistant, lit le même contexte versionné et lance la vérification locale.
- Relecteur : contrôle le même contrat, le cahier des charges, le diff et la CI avant intégration.

## 5. Exigences fonctionnelles

1. Les adaptateurs d’instructions pour Copilot, Claude et Codex doivent être identiques au contrat canonique.
2. Un cahier des charges au format identique doit être disponible pour chaque nouveau projet.
3. Une commande locale doit détecter tout écart entre les adaptateurs et le contrat canonique.
4. Une CI GitHub doit exécuter cette commande à chaque push et pull request.
5. Les standards d’architecture, qualité, API/données, sécurité, tests et exploitation doivent être versionnés et référencés par le contrat IA.

## 6. Exigences non fonctionnelles

- Les scripts doivent utiliser uniquement l’interpréteur POSIX `sh`, `cmp`, `grep` et `mkdir` disponibles dans l’environnement de développement défini par le projet.
- Le dépôt ne doit contenir aucun secret.
- Les fichiers générés par la synchronisation doivent être byte-à-byte identiques à partir du même commit.
- Les projets PHP doivent versionner `composer.json` et `composer.lock`. Les projets Python doivent versionner `pyproject.toml` et un verrouillage avec hashes.

## 7. Critères d’acceptation

1. `make verify` réussit sur une copie propre du dépôt.
2. Modifier un des trois adaptateurs d’instructions fait échouer `make verify`.
3. `make sync-ai-instructions` restaure les trois adaptateurs exactement.
4. La CI exécute `make verify` avec des permissions en lecture seule du contenu.
5. Retirer un repère de structure obligatoire des standards, du contrat ou des ADR fait échouer `make verify`.

## 8. Validation et commandes

- Commande de vérification : `make verify`
- Commande de régénération : `make sync-ai-instructions`
- Revue humaine : le propriétaire produit confirme le périmètre et les critères avant tout projet métier.

## 9. Risques, hypothèses et décisions en attente

- Risque : les assistants ne partagent pas un protocole universel de lecture des instructions.
- Hypothèse : les environnements de développement du projet disposeront des utilitaires POSIX listés ci-dessus.
- Décision en attente : visibilité du dépôt GitHub, versions exactes de PHP/Python et règles de protection GitHub.

## 10. Plan de livraison et retour arrière

1. Centraliser les règles détaillées dans un standard versionné puis synchroniser les trois adaptateurs IA depuis le contrat.
2. Vérifier automatiquement les adaptateurs, le cahier des charges et les repères de gouvernance ; la CI exécute les mêmes contrôles.
3. En cas de régression, annuler le commit de la branche ou restaurer la dernière version revue ; aucun changement de données ou API publique n’est réalisé par ce socle.
