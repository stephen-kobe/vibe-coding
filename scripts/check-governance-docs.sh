#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
standards="$root_dir/docs/ai/DEVELOPMENT_STANDARDS.md"
contract="$root_dir/docs/ai/AI_CONTRACT.md"
decisions="$root_dir/docs/ai/ARCHITECTURE_DECISIONS.md"

for file in "$standards" "$contract" "$decisions"; do
  if [ ! -f "$file" ]; then
    echo "Document de gouvernance introuvable : $file" >&2
    exit 1
  fi
done

for heading in \
  '# Standards de développement' \
  '## 1. Architecture' \
  '## 2. Qualité et conception' \
  '## 3. API et données' \
  '## 4. Sécurité' \
  '## 5. Tests et vérification' \
  '## 6. Exploitation et livraison' \
  '## 7. Décisions nécessitant une validation humaine' \
  '## 8. Checklist de revue'
do
  if ! grep -Fqx "$heading" "$standards"; then
    echo "Section obligatoire absente des standards : $heading" >&2
    exit 1
  fi
done

if ! grep -Fq '[`DEVELOPMENT_STANDARDS.md`](DEVELOPMENT_STANDARDS.md)' "$contract"; then
  echo "Le contrat IA ne référence pas les standards de développement." >&2
  exit 1
fi

if ! grep -Fqx '## ADR-004 — Standards centralisés et contrôle structurel' "$decisions"; then
  echo "ADR-004 absent des décisions d’architecture." >&2
  exit 1
fi

echo "Gouvernance de développement valide."
