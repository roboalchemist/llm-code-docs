#!/bin/bash
set -e

echo "Starting full index rebuild..."
echo "This will take approximately 30-60 minutes"
echo ""

# Auto-confirm with yes
echo y | docker run --rm -i \
  -v ~/github/llm-code-docs:/llm-code-docs:ro \
  -v $(pwd)/lancedb:/app/lancedb \
  llm-docs-search \
  python search.py index --rebuild

echo ""
echo "✓ Rebuild complete!"
