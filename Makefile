.DEFAULT_GOAL := verify

.PHONY: verify sync-ai-instructions check-governance

verify:
	./scripts/verify.sh

sync-ai-instructions:
	./scripts/sync-ai-instructions.sh

check-governance:
	sh ./scripts/check-governance-docs.sh
