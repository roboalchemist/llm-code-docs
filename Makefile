.PHONY: install install-dev uninstall clean test help

help:
	@echo "llm-code-docs - Documentation Search Assistant"
	@echo ""
	@echo "Available targets:"
	@echo "  install       Install llm-code-docs CLI and API"
	@echo "  install-dev   Install in development mode with dev dependencies"
	@echo "  uninstall     Uninstall llm-code-docs"
	@echo "  clean         Remove build artifacts"
	@echo "  test          Run tests"
	@echo "  services      Start all services (OpenSearch, TEI, API, watcher)"
	@echo "  stop-services Stop all services"
	@echo ""
	@echo "Usage:"
	@echo "  make install             # Install via uv"
	@echo "  llm-code-docs health     # Check API status"
	@echo "  llm-code-docs search QUERY"

install:
	@echo "Installing llm-code-docs..."
	uv pip install .
	@echo ""
	@echo "✓ Installed! Try: llm-code-docs health"

install-dev:
	@echo "Installing llm-code-docs in development mode..."
	uv pip install -e ".[dev]"
	@echo ""
	@echo "✓ Installed in dev mode!"

uninstall:
	uv pip uninstall llm-code-docs

clean:
	rm -rf build/ dist/ *.egg-info .pytest_cache __pycache__
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

test:
	pytest tests/ -v

# Service management
services:
	@echo "Starting llm-code-docs services..."
	./scripts/start_opensearch.sh
	./scripts/start_tei.sh
	./scripts/start_watcher.sh
	systemctl --user start llm-code-docs-api.service
	@echo "✓ All services started"

stop-services:
	@echo "Stopping llm-code-docs services..."
	./scripts/stop_opensearch.sh || true
	./scripts/stop_tei.sh || true
	systemctl --user stop llm-code-docs-watcher.service || true
	systemctl --user stop llm-code-docs-api.service || true
	@echo "✓ All services stopped"

# Index management
index-docs:
	USE_GPU_CLUSTER=true python -m search.cli index --rebuild

index-folders:
	USE_GPU_CLUSTER=true python -m search.cli index --folders

# API shortcuts
api-start:
	systemctl --user start llm-code-docs-api.service

api-stop:
	systemctl --user stop llm-code-docs-api.service

api-status:
	systemctl --user status llm-code-docs-api.service --no-pager

api-logs:
	tail -f .api.log
