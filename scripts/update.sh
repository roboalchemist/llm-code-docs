#!/bin/bash
#
# Master Documentation Update Script
# Runs all documentation generation scripts in the scripts folder
#

set -e  # Exit on any error

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."  # Change to repository root

echo "🚀 Starting documentation update process..."
echo "Repository: $(pwd)"
echo "Update scripts directory: $SCRIPT_DIR"
echo

# Track success/failure
declare -a successful_scripts=()
declare -a failed_scripts=()

# Function to run a script and track results
run_script() {
    local script_name="$1"
    local script_path="$2"
    
    echo "═══════════════════════════════════════════════════════════════"
    echo "▶ Running: $script_name"
    echo "═══════════════════════════════════════════════════════════════"
    
    if [[ "$script_path" == *.py ]]; then
        if python3 "$script_path"; then
            successful_scripts+=("$script_name")
            echo
            echo "✅ $script_name completed successfully"
        else
            failed_scripts+=("$script_name")
            echo
            echo "❌ $script_name failed"
        fi
    elif [[ "$script_path" == *.sh ]] && [[ "$script_name" != "update.sh" ]]; then
        if bash "$script_path"; then
            successful_scripts+=("$script_name")
            echo
            echo "✅ $script_name completed successfully"
        else
            failed_scripts+=("$script_name")
            echo
            echo "❌ $script_name failed"
        fi
    else
        echo "⏭️  Skipping $script_name (not executable or is update.sh)"
        return 0
    fi
    
    echo
}

# Find and run all executable scripts in scripts directory
echo "🔍 Scanning for documentation update scripts..."

# Count total scripts
total_scripts=0
for script in "$SCRIPT_DIR"/*.py "$SCRIPT_DIR"/*.sh; do
    if [[ -f "$script" ]]; then
        script_name=$(basename "$script")
        if [[ "$script_name" != "update.sh" ]]; then
            ((total_scripts++))
        fi
    fi
done

echo "Found $total_scripts documentation generation script(s)"
echo

# Run CircuitPython documentation extraction (using our existing tool)
if [[ -f "$SCRIPT_DIR/extract_docs.py" ]]; then
    run_script "CircuitPython Documentation Extractor" "$SCRIPT_DIR/extract_docs.py"
fi

# Run Claude Code SDK documentation download
if [[ -f "$SCRIPT_DIR/claude-code-sdk-docs.py" ]]; then
    run_script "Claude Code SDK Documentation Downloader" "$SCRIPT_DIR/claude-code-sdk-docs.py"
fi

# Run llms.txt sites documentation download (Graphite, Claude, Augment, etc.)
if [[ -f "$SCRIPT_DIR/llms-txt-scraper.py" ]]; then
    run_script "llms.txt Documentation Scraper" "$SCRIPT_DIR/llms-txt-scraper.py"
fi

# Run any other Python or shell scripts
for script in "$SCRIPT_DIR"/*.py "$SCRIPT_DIR"/*.sh; do
    if [[ -f "$script" ]]; then
        script_name=$(basename "$script")
        # Skip scripts we've already run and update.sh itself
        if [[ "$script_name" != "extract_docs.py" ]] && \
           [[ "$script_name" != "claude-code-sdk-docs.py" ]] && \
           [[ "$script_name" != "llms-txt-scraper.py" ]] && \
           [[ "$script_name" != "update.sh" ]]; then
            run_script "$script_name" "$script"
        fi
    fi
done

# Final summary
echo "═══════════════════════════════════════════════════════════════"
echo "📊 Documentation Update Summary"
echo "═══════════════════════════════════════════════════════════════"

echo
echo "📈 Results:"
echo "  Total scripts found: $total_scripts"
echo "  Successful: ${#successful_scripts[@]}"
echo "  Failed: ${#failed_scripts[@]}"

if [[ ${#successful_scripts[@]} -gt 0 ]]; then
    echo
    echo "✅ Successful scripts:"
    for script in "${successful_scripts[@]}"; do
        echo "    • $script"
    done
fi

if [[ ${#failed_scripts[@]} -gt 0 ]]; then
    echo
    echo "❌ Failed scripts:"
    for script in "${failed_scripts[@]}"; do
        echo "    • $script"
    done
fi

echo
echo "📁 Generated documentation directories:"

# Standard documentation (non-llms.txt)
for dir in textual circuitpython claude-code-sdk; do
    if [[ -d "$dir" ]]; then
        file_count=$(find "$dir" -name "*.md" -o -name "*.rst" -o -name "*.py" | wc -l)
        dir_size=$(du -sh "$dir" 2>/dev/null | cut -f1 || echo "unknown")
        echo "    • $dir/ ($file_count files, $dir_size)"
    fi
done

# llms.txt-compliant documentation
if [[ -d "docs/llms-txt" ]]; then
    echo "    • docs/llms-txt/ (llms.txt standard sites):"
    for subdir in docs/llms-txt/*; do
        if [[ -d "$subdir" ]]; then
            subdir_name=$(basename "$subdir")
            file_count=$(find "$subdir" -name "*.md" | wc -l)
            dir_size=$(du -sh "$subdir" 2>/dev/null | cut -f1 || echo "unknown")
            echo "        - $subdir_name/ ($file_count files, $dir_size)"
        fi
    done
fi

echo
if [[ ${#failed_scripts[@]} -eq 0 ]]; then
    echo "🎉 All documentation updates completed successfully!"
    echo "📚 Your local documentation is now up to date."
    exit 0
else
    echo "⚠️  Some documentation updates failed. Check the logs above for details."
    exit 1
fi