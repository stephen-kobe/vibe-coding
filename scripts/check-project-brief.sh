#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
brief="$root_dir/docs/ai/PROJECT_BRIEF.md"

if [ ! -f "$brief" ]; then
  echo "Cahier des charges introuvable : $brief" >&2
  exit 1
fi

if grep -Fq '> Statut : BROUILLON' "$brief"; then
  echo "Le cahier des charges est encore au statut BROUILLON : complétez-le avant de valider le projet." >&2
  exit 1
fi

for heading in \
  '# Cahier des charges projet' \
  '## 1. Identité' \
  '## 2. Problème et résultat attendu' \
  '## 3. Périmètre' \
  '## 4. Utilisateurs et cas d’usage' \
  '## 5. Exigences fonctionnelles' \
  '## 6. Exigences non fonctionnelles' \
  '## 7. Critères d’acceptation' \
  '## 8. Validation et commandes' \
  '## 9. Risques, hypothèses et décisions en attente'
do
  if ! grep -Fqx "$heading" "$brief"; then
    echo "Section obligatoire absente du cahier des charges : $heading" >&2
    exit 1
  fi
done

echo "Structure du cahier des charges valide."
