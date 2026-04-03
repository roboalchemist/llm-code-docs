#!/bin/bash
# Fetch Fast.AI documentation from GitHub

set -e

OUTPUT_DIR="/Users/joseph.schlesinger/github/llm-code-docs/docs/github-scraped/fastai"
REPO="https://raw.githubusercontent.com/fastai/fastai/main"

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Fetch README
echo "Fetching README..."
curl -s "$REPO/README.md" > "$OUTPUT_DIR/README.md"

# Fetch CONTRIBUTING
echo "Fetching CONTRIBUTING..."
curl -s "$REPO/CONTRIBUTING.md" > "$OUTPUT_DIR/CONTRIBUTING.md"

# Fetch CHANGELOG
echo "Fetching CHANGELOG..."
curl -s "$REPO/CHANGELOG.md" > "$OUTPUT_DIR/CHANGELOG.md"

# Combine into single file
OUTPUT_FILE="$OUTPUT_DIR/fastai-full.md"
cat > "$OUTPUT_FILE" << 'EOF'
# Fast.AI Documentation

Source: https://github.com/fastai/fastai

This documentation is extracted from the Fast.AI repository. Fast.AI is a deep learning library built on top of PyTorch that aims to simplify training fast and accurate neural networks using modern best practices.

---

## Repository

- **Repository**: https://github.com/fastai/fastai
- **Documentation**: https://docs.fast.ai
- **Website**: https://fast.ai

---

EOF

# Append extracted files
for file in "$OUTPUT_DIR"/*.md; do
    if [[ "$(basename "$file")" != "fastai-full.md" ]]; then
        echo "## $(basename "$file" | sed 's/.md$//')" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        cat "$file" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
        echo "---" >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    fi
done

echo "Documentation saved to $OUTPUT_FILE"
echo "File size: $(du -h "$OUTPUT_FILE" | cut -f1)"
