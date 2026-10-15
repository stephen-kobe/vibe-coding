#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
expected_file=$(mktemp "${TMPDIR:-/tmp}/ai-contract.XXXXXX")
trap 'rm -f "$expected_file"' EXIT HUP INT TERM

{
  printf '%s\n\n' '<!-- GENERATED from docs/ai/AI_CONTRACT.md; run make sync-ai-instructions -->'
  cat "$root_dir/docs/ai/AI_CONTRACT.md"
} > "$expected_file"

for target in AGENTS.md CLAUDE.md .github/copilot-instructions.md; do
  if ! cmp -s "$expected_file" "$root_dir/$target"; then
    echo "Adaptateur IA non synchronisé : $target. Exécutez : make sync-ai-instructions" >&2
    exit 1
  fi
done

echo "Adaptateurs IA synchronisés."
