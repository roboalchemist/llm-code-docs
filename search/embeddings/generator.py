"""Embedding generation using qwen3-embeddings-mlx server."""

from typing import List
import time
import requests
from tqdm import tqdm
from search import config
from search.utils.server_manager import get_server_manager
import logging

logger = logging.getLogger(__name__)

# Import GPU load balancer if using GPU cluster
if config.USE_GPU_CLUSTER:
    from search.embeddings.gpu_load_balancer import MultiGPUEmbeddingClient


class EmbeddingGenerator:
    """Generates embeddings using qwen3-embeddings-mlx server."""

    def __init__(self, model_name: str = None, api_url: str = None):
        """
        Initialize the embedding generator.

        Args:
            model_name: Name of the model (small/medium/large).
                       Defaults from config.EMBEDDING_MODEL.
            api_url: URL of the qwen3-embeddings-mlx server (ignored if USE_GPU_CLUSTER=True).
        """
        self.model_name = model_name or config.EMBEDDING_MODEL
        self.use_gpu_cluster = config.USE_GPU_CLUSTER

        if self.use_gpu_cluster:
            # Use multi-GPU load balancer
            self.gpu_client = MultiGPUEmbeddingClient(config.GPU_SERVERS)
            health = self.gpu_client.health_check()
            healthy_count = sum(1 for v in health.values() if v.get("status") == "healthy")
            logger.info(f"GPU cluster: {healthy_count}/{len(config.GPU_SERVERS)} servers healthy")
            if healthy_count == 0:
                raise RuntimeError(f"No GPU servers available: {health}")
        else:
            # Use single server (TEI)
            self.api_url = api_url or config.EMBEDDING_API_URL
            try:
                response = requests.get(f"{self.api_url}/health", timeout=5)
                if response.status_code != 200:
                    raise RuntimeError(f"TEI server health check failed with status {response.status_code}")
            except Exception as e:
                raise RuntimeError(f"TEI embedding server is not available at {self.api_url}: {e}")

    def generate(
        self,
        texts: List[str],
        batch_size: int = None,
        show_progress: bool = True,
    ) -> List[List[float]]:
        """
        Generate embeddings for a list of texts.

        Args:
            texts: List of text strings to embed.
            batch_size: Batch size for encoding. Defaults to config.EMBEDDING_BATCH_SIZE.
            show_progress: Whether to show progress bar.

        Returns:
            List of embedding vectors (each is a list of floats).
        """
        if not texts:
            return []

        # Use GPU cluster for large batches (handles distribution internally)
        if self.use_gpu_cluster:
            if show_progress:
                logger.info(f"Generating embeddings for {len(texts)} texts using GPU cluster...")
            return self.gpu_client.embed_batch(texts, model=self.model_name)

        # Single server path
        batch_size = batch_size or config.EMBEDDING_BATCH_SIZE
        all_embeddings = []

        # Process in batches with progress bar
        num_batches = (len(texts) + batch_size - 1) // batch_size
        iterator = range(num_batches)

        if show_progress:
            iterator = tqdm(iterator, desc="Generating embeddings")

        for i in iterator:
            start_idx = i * batch_size
            end_idx = min((i + 1) * batch_size, len(texts))
            batch_texts = texts[start_idx:end_idx]

            # Retry with exponential backoff on failure
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    response = requests.post(
                        f"{self.api_url}/embed",
                        json={"inputs": batch_texts},
                        timeout=300,  # 5 minute timeout for large batches
                    )
                    response.raise_for_status()
                    result = response.json()
                    all_embeddings.extend(result)  # TEI returns embeddings directly
                    break  # Success!

                except requests.exceptions.ConnectionError as e:
                    if attempt < max_retries - 1:
                        logger.warning(f"Server connection failed (attempt {attempt+1}/{max_retries}), attempting restart...")
                        # Try to restart server
                        server_mgr = get_server_manager()
                        if server_mgr.ensure_server_running():
                            wait_time = 2 ** attempt  # Exponential backoff
                            logger.info(f"Server restarted, waiting {wait_time}s before retry...")
                            time.sleep(wait_time)
                            continue

                    # All retries failed
                    raise RuntimeError(
                        f"\n\n{'='*60}\n"
                        f"EMBEDDING SERVER CONNECTION FAILED\n"
                        f"{'='*60}\n"
                        f"Cannot connect to server at {self.api_url}\n"
                        f"Tried {max_retries} times with auto-restart\n\n"
                        f"Error: {e}\n"
                        f"{'='*60}\n"
                    ) from e

                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 404:
                        raise RuntimeError(
                            f"\n\n{'='*60}\n"
                            f"WRONG ENDPOINT OR SERVER\n"
                            f"{'='*60}\n"
                            f"Endpoint {e.request.url} returned 404\n\n"
                            f"This usually means:\n"
                            f"  1. Wrong server is running on port 10001\n"
                            f"  2. Embedding server version mismatch\n\n"
                            f"Expected endpoint: POST /embed_batch\n"
                            f"{'='*60}\n"
                        ) from e
                    raise RuntimeError(f"HTTP error from embedding server: {e}") from e

                except Exception as e:
                    if attempt < max_retries - 1:
                        wait_time = 2 ** attempt
                        logger.warning(f"Error generating embeddings (attempt {attempt+1}/{max_retries}): {e}")
                        time.sleep(wait_time)
                        continue
                    raise RuntimeError(f"Failed after {max_retries} attempts: {e}") from e

        return all_embeddings

    def generate_single(self, text: str) -> List[float]:
        """
        Generate embedding for a single text.

        Args:
            text: Text string to embed.

        Returns:
            Embedding vector as a list of floats.
        """
        if self.use_gpu_cluster:
            return self.gpu_client.embed_single(text)

        try:
            response = requests.post(
                f"{self.api_url}/embed",
                json={"inputs": text},
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()
            # TEI returns [[...]] for single text, extract first embedding
            return result[0] if isinstance(result, list) else result
        except Exception as e:
            raise RuntimeError(f"Failed to generate single embedding: {e}") from e


# Global generator instance
_generator = None


def get_generator() -> EmbeddingGenerator:
    """Get global embedding generator instance."""
    global _generator
    if _generator is None:
        _generator = EmbeddingGenerator()
    return _generator
