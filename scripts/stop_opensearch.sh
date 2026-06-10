#!/bin/bash
# Stop OpenSearch containers gracefully

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.opensearch.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Stopping OpenSearch containers...${NC}"

# Check if compose file exists
if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo -e "${RED}Error: docker-compose.opensearch.yml not found at $COMPOSE_FILE${NC}"
    exit 1
fi

# Check if containers are running
if ! docker compose -f "$COMPOSE_FILE" ps --quiet 2>/dev/null | grep -q .; then
    echo -e "${YELLOW}No OpenSearch containers are currently running${NC}"
    exit 0
fi

# Stop containers gracefully
docker compose -f "$COMPOSE_FILE" down

echo -e "${GREEN}OpenSearch containers stopped successfully${NC}"

# Optional: show remaining volumes
echo ""
echo -e "${YELLOW}Note: Data volume 'opensearch-data' is preserved.${NC}"
echo "To remove all data, run: docker compose -f $COMPOSE_FILE down -v"
