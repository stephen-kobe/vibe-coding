#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_file="$root_dir/docs/ai/AI_CONTRACT.md"

if [ ! -f "$source_file" ]; then
  echo "Contrat canonique introuvable : $source_file" >&2
  exit 1
fi

mkdir -p "$root_dir/.github"

for target in AGENTS.md CLAUDE.md .github/copilot-instructions.md; do
  {
    printf '%s\n\n' '<!-- GENERATED from docs/ai/AI_CONTRACT.md; run make sync-ai-instructions -->'
    cat "$source_file"
  } > "$root_dir/$target"
done
