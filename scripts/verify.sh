#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

"$root_dir/scripts/check-ai-contract.sh"
"$root_dir/scripts/check-project-brief.sh"
sh "$root_dir/scripts/check-governance-docs.sh"
sh "$root_dir/scripts/check-rules-catalog.sh"

echo "Vérification réussie."
