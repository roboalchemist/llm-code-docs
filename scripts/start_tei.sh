#!/bin/bash
# Start TEI (Text Embeddings Inference) servers on RTX 3090s
# Model: Qwen/Qwen3-Embedding-0.6B (1024 dimensions)
# Throughput: ~475 texts/sec on 2x RTX 3090

set -e

echo "Starting TEI embedding servers..."

# Stop existing containers if running
sudo docker rm -f tei-gpu3 tei-gpu5 2>/dev/null || true

# Start TEI on GPU 3 (RTX 3090)
sudo docker run -d --name tei-gpu3 \
  --gpus '"device=3"' \
  -p 10001:80 \
  -v ~/.cache/huggingface:/data \
  --restart unless-stopped \
  ghcr.io/huggingface/text-embeddings-inference:1.8 \
  --model-id Qwen/Qwen3-Embedding-0.6B \
  --auto-truncate \
  --max-batch-tokens 65536

# Start TEI on GPU 5 (RTX 3090)
sudo docker run -d --name tei-gpu5 \
  --gpus '"device=5"' \
  -p 10002:80 \
  -v ~/.cache/huggingface:/data \
  --restart unless-stopped \
  ghcr.io/huggingface/text-embeddings-inference:1.8 \
  --model-id Qwen/Qwen3-Embedding-0.6B \
  --auto-truncate \
  --max-batch-tokens 65536

echo "Waiting for servers to start..."
sleep 15

# Check health
for port in 10001 10002; do
  status=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:$port/health)
  if [ "$status" = "200" ]; then
    echo "  Port $port: healthy"
  else
    echo "  Port $port: NOT READY (status: $status)"
  fi
done

echo ""
echo "TEI servers started."
echo "Usage: USE_GPU_CLUSTER=true python -m search.cli index --rebuild"
