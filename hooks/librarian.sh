#!/usr/bin/env bash
#
# librarian.sh - Claude Code UserPromptSubmit hook
#
# Provides automatic documentation suggestions from the librarian API.
# Called on each user prompt submission to inject relevant documentation context.
#
# Requirements:
# - librarian API running at LIBRARIAN_URL (default: http://localhost:8080)
# - curl with timeout support
# - jq for JSON parsing
#
# Configuration:
#   LIBRARIAN_URL - Base URL of the librarian API (default: http://localhost:8080)
#   LIBRARIAN_TIMEOUT_MS - Timeout in milliseconds (default: 50)
#   LIBRARIAN_LIMIT - Maximum number of suggestions (default: 3)
#   LIBRARIAN_ENABLED - Set to "false" to disable (default: true)
#
# Exit codes:
#   0 - Success (always, to not block Claude Code)

set -euo pipefail

# Configuration with sensible defaults
LIBRARIAN_URL="${LIBRARIAN_URL:-http://localhost:8080}"
LIBRARIAN_TIMEOUT_MS="${LIBRARIAN_TIMEOUT_MS:-50}"
LIBRARIAN_LIMIT="${LIBRARIAN_LIMIT:-3}"
LIBRARIAN_ENABLED="${LIBRARIAN_ENABLED:-true}"

# Convert ms to seconds for curl using awk (more portable than bc)
# Default 50ms = 0.05s
TIMEOUT_SECS=$(awk "BEGIN {printf \"%.3f\", $LIBRARIAN_TIMEOUT_MS / 1000}")

# Early exit if disabled
if [[ "$LIBRARIAN_ENABLED" == "false" ]]; then
    exit 0
fi

# Read hook input from stdin
INPUT=$(cat)

# Extract the user prompt from the hook input
# The hook receives JSON with structure: {"user_prompt": "...", ...}
USER_PROMPT=$(echo "$INPUT" | jq -r '.user_prompt // empty' 2>/dev/null) || exit 0

# Skip if no prompt or prompt is too short
if [[ -z "$USER_PROMPT" ]] || [[ ${#USER_PROMPT} -lt 3 ]]; then
    exit 0
fi

# URL-encode the query using Python (handles special characters properly)
ENCODED_QUERY=$(python3 -c "import urllib.parse, sys; print(urllib.parse.quote(sys.stdin.read().strip()))" <<< "$USER_PROMPT" 2>/dev/null) || exit 0

if [[ -z "$ENCODED_QUERY" ]]; then
    exit 0
fi

# Call the /suggest endpoint with strict timeout
# curl exits non-zero on timeout or connection error, which we catch with || exit 0
RESPONSE=$(curl -s --max-time "$TIMEOUT_SECS" \
    "${LIBRARIAN_URL}/suggest?q=${ENCODED_QUERY}&limit=${LIBRARIAN_LIMIT}" 2>/dev/null) || exit 0

# Parse response and check if we have suggestions
SUGGESTION_COUNT=$(echo "$RESPONSE" | jq -r '.returned // 0' 2>/dev/null) || exit 0

if [[ "$SUGGESTION_COUNT" == "0" ]] || [[ -z "$SUGGESTION_COUNT" ]] || [[ "$SUGGESTION_COUNT" == "null" ]]; then
    exit 0
fi

# Build markdown-formatted context using jq to format the output
FORMATTED_SUGGESTIONS=$(echo "$RESPONSE" | jq -r '
    .suggestions[]? |
    "- **\(.framework_name)** (\(.category)): \(.description // "No description")\n  Path: `\(.path)`"
' 2>/dev/null) || exit 0

if [[ -z "$FORMATTED_SUGGESTIONS" ]]; then
    exit 0
fi

# Build the complete context message
CONTEXT="<user-prompt-submit-hook>
## Relevant Documentation Available

The following documentation may be helpful for this query:

${FORMATTED_SUGGESTIONS}

Use the Read tool to access these docs if needed.
</user-prompt-submit-hook>"

# Output the formatted context as JSON
# Claude Code expects JSON output with optional systemMessage field for context injection
jq -n --arg msg "$CONTEXT" '{"systemMessage": $msg}'

exit 0
