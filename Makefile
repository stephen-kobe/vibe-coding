.DEFAULT_GOAL := verify

.PHONY: verify sync-ai-instructions

verify:
	./scripts/verify.sh

sync-ai-instructions:
	./scripts/sync-ai-instructions.sh
