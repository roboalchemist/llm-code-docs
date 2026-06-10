#!/bin/bash
# Start OpenSearch with ML Commons
# Sets required system settings and performs health check

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
COMPOSE_FILE="$PROJECT_DIR/docker-compose.opensearch.yml"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Starting OpenSearch with ML Commons...${NC}"

# Check if compose file exists
if [[ ! -f "$COMPOSE_FILE" ]]; then
    echo -e "${RED}Error: docker-compose.opensearch.yml not found at $COMPOSE_FILE${NC}"
    exit 1
fi

# Set vm.max_map_count (required for OpenSearch)
CURRENT_MAP_COUNT=$(cat /proc/sys/vm/max_map_count 2>/dev/null || echo "0")
REQUIRED_MAP_COUNT=262144

if [[ "$CURRENT_MAP_COUNT" -lt "$REQUIRED_MAP_COUNT" ]]; then
    echo -e "${YELLOW}Setting vm.max_map_count to $REQUIRED_MAP_COUNT (current: $CURRENT_MAP_COUNT)${NC}"
    if sudo sysctl -w vm.max_map_count=$REQUIRED_MAP_COUNT > /dev/null 2>&1; then
        echo -e "${GREEN}vm.max_map_count set successfully${NC}"
    else
        echo -e "${RED}Warning: Could not set vm.max_map_count. You may need to run:${NC}"
        echo -e "${RED}  sudo sysctl -w vm.max_map_count=$REQUIRED_MAP_COUNT${NC}"
        echo -e "${RED}Or add to /etc/sysctl.conf for persistence${NC}"
    fi
else
    echo -e "${GREEN}vm.max_map_count already set to $CURRENT_MAP_COUNT (>= $REQUIRED_MAP_COUNT)${NC}"
fi

# Start containers
echo -e "${YELLOW}Starting Docker containers...${NC}"
docker compose -f "$COMPOSE_FILE" up -d

# Wait for OpenSearch to be healthy
echo -e "${YELLOW}Waiting for OpenSearch to be healthy...${NC}"
MAX_ATTEMPTS=60
ATTEMPT=1

while [[ $ATTEMPT -le $MAX_ATTEMPTS ]]; do
    if curl -s --max-time 5 http://localhost:9200/_cluster/health 2>/dev/null | grep -qE '"status":"(green|yellow)"'; then
        echo -e "${GREEN}OpenSearch is healthy!${NC}"
        break
    fi

    if [[ $ATTEMPT -eq $MAX_ATTEMPTS ]]; then
        echo -e "${RED}Error: OpenSearch failed to become healthy after $MAX_ATTEMPTS attempts${NC}"
        echo "Checking container logs..."
        docker compose -f "$COMPOSE_FILE" logs --tail=50 opensearch
        exit 1
    fi

    echo "  Attempt $ATTEMPT/$MAX_ATTEMPTS - waiting 5 seconds..."
    sleep 5
    ((ATTEMPT++))
done

# Verify ML Commons is available
echo -e "${YELLOW}Verifying ML Commons plugin...${NC}"
ML_RESPONSE=$(curl -s --max-time 10 http://localhost:9200/_plugins/_ml/stats 2>/dev/null)

if echo "$ML_RESPONSE" | grep -q '"ml_node_count"'; then
    echo -e "${GREEN}ML Commons plugin is available!${NC}"
else
    echo -e "${YELLOW}Warning: ML Commons stats check returned unexpected response${NC}"
    echo "Response: $ML_RESPONSE"
fi

# Print status summary
echo ""
echo -e "${GREEN}=== OpenSearch Status ===${NC}"
echo ""
echo "Cluster Health:"
curl -s http://localhost:9200/_cluster/health?pretty | head -15
echo ""
echo -e "${GREEN}OpenSearch:${NC} http://localhost:9200"
echo -e "${GREEN}Dashboards:${NC} http://localhost:5601 (may take a minute to start)"
echo -e "${GREEN}ML Stats:${NC}   curl http://localhost:9200/_plugins/_ml/stats"
echo ""
echo -e "${GREEN}OpenSearch is ready!${NC}"
