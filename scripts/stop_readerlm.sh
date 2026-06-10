#!/bin/bash
# Stop ReaderLM-v2 server

CONTAINER_NAME="readerlm-v2"

echo "Stopping ReaderLM-v2 server..."

if sudo docker ps -q -f name=${CONTAINER_NAME} | grep -q .; then
  sudo docker stop ${CONTAINER_NAME}
  sudo docker rm ${CONTAINER_NAME}
  echo "ReaderLM-v2 server stopped."
else
  echo "ReaderLM-v2 server is not running."
  # Clean up stopped container if exists
  sudo docker rm ${CONTAINER_NAME} 2>/dev/null || true
fi
