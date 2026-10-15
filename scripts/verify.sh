#!/bin/sh
set -eu

root_dir=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)

"$root_dir/scripts/check-ai-contract.sh"
"$root_dir/scripts/check-project-brief.sh"

echo "Vérification réussie."
