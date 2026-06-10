#!/bin/bash
# Start ReaderLM-v2 (jinaai/ReaderLM-v2) on GPU 3 (RTX 3090)
# Model: 1.54B params, bfloat16, 512K context
# Purpose: Local HTML-to-Markdown conversion without rate limits

set -e

CONTAINER_NAME="readerlm-v2"
GPU_ID="3"
PORT="10010"
MODEL="jinaai/ReaderLM-v2"

echo "Starting ReaderLM-v2 server on GPU ${GPU_ID}..."

# Stop existing container if running
sudo docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

# Start vLLM with OpenAI-compatible API
# NOTE: Using GPU 3 (RTX 3090) - 24GB VRAM
# Model uses ~4GB VRAM with bfloat16
sudo docker run -d --name ${CONTAINER_NAME} \
  --gpus '"device='${GPU_ID}'"' \
  -p ${PORT}:8000 \
  -v ~/.cache/huggingface:/root/.cache/huggingface \
  --restart unless-stopped \
  --ipc=host \
  vllm/vllm-openai:latest \
  --model ${MODEL} \
  --dtype bfloat16 \
  --max-model-len 16384 \
  --trust-remote-code \
  --gpu-memory-utilization 0.7 \
  --max-num-seqs 128

echo "Waiting for server to start (downloading model if needed)..."
echo "This may take a few minutes on first run..."

# Wait up to 10 minutes for model download and startup
MAX_WAIT=600
ELAPSED=0
INTERVAL=10

while [ $ELAPSED -lt $MAX_WAIT ]; do
  # Check if container is still running
  if ! sudo docker ps -q -f name=${CONTAINER_NAME} | grep -q .; then
    echo "ERROR: Container stopped unexpectedly. Checking logs..."
    sudo docker logs ${CONTAINER_NAME} 2>&1 | tail -50
    exit 1
  fi

  # Try health check
  status=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 http://localhost:${PORT}/health 2>/dev/null || echo "000")
  if [ "$status" = "200" ]; then
    echo ""
    echo "ReaderLM-v2 server is ready!"
    echo ""
    echo "API Endpoint: http://localhost:${PORT}/v1"
    echo "Model: ${MODEL}"
    echo "GPU: ${GPU_ID} (RTX 3090)"
    echo ""
    echo "Test with:"
    echo "  curl http://localhost:${PORT}/v1/chat/completions \\"
    echo "    -H 'Content-Type: application/json' \\"
    echo "    -d '{\"model\": \"jinaai/ReaderLM-v2\", \"messages\": [{\"role\": \"user\", \"content\": \"Convert to markdown:\\n\\\`\\\`\\\`html\\n<h1>Hello</h1>\\n\\\`\\\`\\\`\"}]}'"
    exit 0
  fi

  printf "."
  sleep $INTERVAL
  ELAPSED=$((ELAPSED + INTERVAL))
done

echo ""
echo "ERROR: Server did not become ready within ${MAX_WAIT} seconds"
echo "Checking container logs..."
sudo docker logs ${CONTAINER_NAME} 2>&1 | tail -50
exit 1
