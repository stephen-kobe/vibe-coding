#!/bin/sh
set -eu
root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
catalog="$root_dir/docs/ai/RULES_CATALOG.md"
[ -f "$catalog" ] || { echo "Catalogue absent" >&2; exit 1; }
tmp=$(mktemp)
trap 'rm -f "$tmp"' EXIT HUP INT TERM
# Ancrage unique et strict : seuls les identifiants dans la première colonne des tableaux de définitions comptent.
sed -n 's/^| \(\(ARC\|DEV\|DATA\|SEC\|QA\|PRJ\|OPS\|AI\)-[0-9][0-9]\) |.*/\1/p' "$catalog" > "$tmp"
for spec in 'ARC 12' 'DEV 16' 'DATA 10' 'SEC 10' 'QA 10' 'PRJ 10' 'OPS 8' 'AI 15'; do
  set -- $spec
  prefix=$1
  max=$2
  i=1
  while [ "$i" -le "$max" ]; do
    identifier=$(printf '%s-%02d' "$prefix" "$i")
    count=$(grep -Fxc "$identifier" "$tmp" || true)
    if [ "$count" -ne 1 ]; then
      echo "Définition manquante ou dupliquée : $identifier (trouvée $count fois)" >&2
      exit 1
    fi
    i=$((i + 1))
  done
  count=$(grep -c "^$prefix-" "$tmp" || true)
  if [ "$count" -ne "$max" ]; then
    echo "Nombre inattendu pour $prefix : $count au lieu de $max" >&2
    exit 1
  fi
  count=$(grep -c "^## $prefix — " "$catalog" || true)
  if [ "$count" -ne 1 ]; then
    echo "Section de catégorie absente ou dupliquée : $prefix" >&2
    exit 1
  fi
done
count=$(wc -l < "$tmp" | tr -d ' ')
[ "$count" -eq 91 ] || { echo "Nombre de définitions inattendu : $count" >&2; exit 1; }
for file in "$root_dir/docs/ai/AI_CONTRACT.md" "$root_dir/docs/ai/DEVELOPMENT_STANDARDS.md" "$root_dir/README.md"; do
  grep -Fq RULES_CATALOG.md "$file" || { echo "Lien de catalogue absent : $file" >&2; exit 1; }
done
echo "Catalogue valide : 91 règles, 8 catégories, aucun doublon ni trou."
