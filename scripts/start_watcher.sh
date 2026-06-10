#!/bin/bash
# Start the file watcher daemon for llm-code-docs
# Monitors markdown files and triggers incremental OpenSearch indexing
#
# Usage:
#   ./scripts/start_watcher.sh              # Start with defaults
#   ./scripts/start_watcher.sh --background # Start in background (writes PID file)
#   ./scripts/start_watcher.sh --stop       # Stop background daemon
#   ./scripts/start_watcher.sh --status     # Check daemon status

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
PID_FILE="$PROJECT_DIR/.watcher.pid"
LOG_FILE="$PROJECT_DIR/.watcher.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default settings
DEBOUNCE=5
POLL_INTERVAL=1
LOG_LEVEL="INFO"

usage() {
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Start the file watcher daemon for llm-code-docs."
    echo ""
    echo "Options:"
    echo "  --background     Run in background (detached)"
    echo "  --stop           Stop the background daemon"
    echo "  --status         Check if daemon is running"
    echo "  --debounce SEC   Debounce seconds (default: $DEBOUNCE)"
    echo "  --poll SEC       Poll interval seconds (default: $POLL_INTERVAL)"
    echo "  --log-level LVL  Logging level: DEBUG|INFO|WARNING|ERROR (default: $LOG_LEVEL)"
    echo "  --help           Show this help message"
}

is_running() {
    if [[ -f "$PID_FILE" ]]; then
        local pid
        pid=$(cat "$PID_FILE")
        if kill -0 "$pid" 2>/dev/null; then
            return 0
        else
            # Stale PID file
            rm -f "$PID_FILE"
        fi
    fi
    return 1
}

do_status() {
    if is_running; then
        local pid
        pid=$(cat "$PID_FILE")
        echo -e "${GREEN}Watcher is running (PID: $pid)${NC}"
        echo "Log file: $LOG_FILE"
        return 0
    else
        echo -e "${YELLOW}Watcher is not running${NC}"
        return 1
    fi
}

do_stop() {
    if is_running; then
        local pid
        pid=$(cat "$PID_FILE")
        echo -e "${YELLOW}Stopping watcher (PID: $pid)...${NC}"
        kill "$pid" 2>/dev/null || true
        # Wait for process to exit
        local count=0
        while kill -0 "$pid" 2>/dev/null && [[ $count -lt 10 ]]; do
            sleep 1
            ((count++))
        done
        if kill -0 "$pid" 2>/dev/null; then
            echo -e "${YELLOW}Process didn't stop gracefully, sending SIGKILL...${NC}"
            kill -9 "$pid" 2>/dev/null || true
        fi
        rm -f "$PID_FILE"
        echo -e "${GREEN}Watcher stopped${NC}"
    else
        echo -e "${YELLOW}Watcher is not running${NC}"
    fi
}

do_start_foreground() {
    echo -e "${GREEN}Starting file watcher daemon (foreground)${NC}"
    echo -e "  Docs root:  ${config.DOCS_ROOT:-~/github/llm-code-docs/docs}"
    echo -e "  Debounce:   ${DEBOUNCE}s"
    echo -e "  Log level:  ${LOG_LEVEL}"
    echo ""
    echo -e "${YELLOW}Press Ctrl+C to stop${NC}"
    echo ""

    cd "$PROJECT_DIR"
    exec python -m search.watcher.daemon \
        --debounce "$DEBOUNCE" \
        --poll-interval "$POLL_INTERVAL" \
        --log-level "$LOG_LEVEL"
}

do_start_background() {
    if is_running; then
        local pid
        pid=$(cat "$PID_FILE")
        echo -e "${YELLOW}Watcher is already running (PID: $pid)${NC}"
        return 1
    fi

    echo -e "${GREEN}Starting file watcher daemon (background)${NC}"

    cd "$PROJECT_DIR"
    nohup python -m search.watcher.daemon \
        --debounce "$DEBOUNCE" \
        --poll-interval "$POLL_INTERVAL" \
        --log-level "$LOG_LEVEL" \
        > "$LOG_FILE" 2>&1 &

    local pid=$!
    echo "$pid" > "$PID_FILE"

    # Verify it started
    sleep 1
    if kill -0 "$pid" 2>/dev/null; then
        echo -e "${GREEN}Watcher started (PID: $pid)${NC}"
        echo "Log file: $LOG_FILE"
    else
        echo -e "${RED}Watcher failed to start. Check log:${NC}"
        echo "  tail -20 $LOG_FILE"
        rm -f "$PID_FILE"
        return 1
    fi
}

# Parse arguments
BACKGROUND=false
ACTION=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --background)
            BACKGROUND=true
            shift
            ;;
        --stop)
            ACTION="stop"
            shift
            ;;
        --status)
            ACTION="status"
            shift
            ;;
        --debounce)
            DEBOUNCE="$2"
            shift 2
            ;;
        --poll)
            POLL_INTERVAL="$2"
            shift 2
            ;;
        --log-level)
            LOG_LEVEL="$2"
            shift 2
            ;;
        --help)
            usage
            exit 0
            ;;
        *)
            echo -e "${RED}Unknown option: $1${NC}"
            usage
            exit 1
            ;;
    esac
done

# Check OpenSearch connectivity (non-blocking warning)
if ! curl -s --max-time 2 http://localhost:9200/_cluster/health >/dev/null 2>&1; then
    echo -e "${YELLOW}Warning: OpenSearch is not reachable at localhost:9200${NC}"
    echo -e "${YELLOW}The watcher will queue events but indexing will fail until OpenSearch is available.${NC}"
    echo ""
fi

# Execute action
case "$ACTION" in
    stop)
        do_stop
        ;;
    status)
        do_status
        ;;
    *)
        if [[ "$BACKGROUND" == "true" ]]; then
            do_start_background
        else
            do_start_foreground
        fi
        ;;
esac
