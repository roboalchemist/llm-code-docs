#!/usr/bin/env python3
"""Load-balancing client for multi-GPU embedding servers."""

import requests
from typing import List
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging

logger = logging.getLogger(__name__)

# Maximum texts per GPU per batch to avoid OOM
MAX_CHUNK_SIZE = 20  # Very conservative for real document chunks with memory fragmentation

class MultiGPUEmbeddingClient:
    """Client that distributes requests across multiple GPU servers."""
    
    def __init__(self, servers: List[str]):
        """
        Initialize with list of server URLs.
        
        Args:
            servers: List of server URLs (e.g., ["http://chungus2:10002", ...])
        """
        self.servers = servers
        self.num_servers = len(servers)
        logger.info(f"Initialized with {self.num_servers} GPU servers")
    
    def embed_batch(self, texts: List[str], model: str = "small", timeout: int = 300, chunk_size: int = None) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts, distributed across servers.

        Args:
            texts: List of text strings to embed
            model: Model name (for API compatibility)
            timeout: Request timeout in seconds
            chunk_size: Override default chunk size (for retry with smaller batches)

        Returns:
            List of embedding vectors
        """
        if not texts:
            return []

        # For small batches, use single server
        if len(texts) < self.num_servers * 4:
            try:
                response = requests.post(
                    self.servers[0],  # TEI root endpoint
                    json={"inputs": texts},  # TEI format
                    timeout=timeout
                )
                response.raise_for_status()
                return response.json()  # TEI returns embeddings directly
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 500 and "out of memory" in str(e.response.text).lower():
                    # Retry with smaller batch
                    logger.warning(f"OOM on small batch ({len(texts)} texts), splitting in half")
                    mid = len(texts) // 2
                    emb1 = self.embed_batch(texts[:mid], model, timeout)
                    emb2 = self.embed_batch(texts[mid:], model, timeout)
                    return emb1 + emb2
                raise

        # Determine chunk size (respect MAX_CHUNK_SIZE)
        if chunk_size is None:
            chunk_size = min(MAX_CHUNK_SIZE, (len(texts) + self.num_servers - 1) // self.num_servers)

        # If chunk size is too large, process in multiple rounds
        if chunk_size > MAX_CHUNK_SIZE:
            chunk_size = MAX_CHUNK_SIZE
            logger.info(f"Processing {len(texts)} texts in rounds of {chunk_size * self.num_servers}")

        all_embeddings = [None] * len(texts)  # Preserve order

        def process_chunk(server_idx, server, start_idx, end_idx, retry_count=0):
            chunk = texts[start_idx:end_idx]
            try:
                response = requests.post(
                    server,  # TEI root endpoint
                    json={"inputs": chunk},  # TEI format
                    timeout=timeout
                )
                response.raise_for_status()
                return server_idx, start_idx, response.json()  # TEI returns embeddings directly
            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 500 and retry_count < 2:
                    # Check if OOM error
                    error_text = str(e.response.text).lower()
                    if "out of memory" in error_text or "cuda" in error_text:
                        # Retry with half the chunk size
                        new_chunk_size = (end_idx - start_idx) // 2
                        if new_chunk_size < 10:
                            raise RuntimeError(f"GPU OOM even with tiny batch ({end_idx - start_idx} texts)") from e
                        logger.warning(f"OOM on server {server_idx}, retrying with {new_chunk_size} texts (was {end_idx - start_idx})")
                        # Process in two smaller chunks
                        mid = start_idx + new_chunk_size
                        _, _, emb1 = process_chunk(server_idx, server, start_idx, mid, retry_count + 1)
                        _, _, emb2 = process_chunk(server_idx, server, mid, end_idx, retry_count + 1)
                        return server_idx, start_idx, emb1 + emb2
                raise

        # Process all texts in rounds of (chunk_size * num_servers)
        round_size = chunk_size * self.num_servers
        for round_start in range(0, len(texts), round_size):
            round_end = min(round_start + round_size, len(texts))

            with ThreadPoolExecutor(max_workers=self.num_servers) as executor:
                futures = []
                for i, server in enumerate(self.servers):
                    start_idx = round_start + i * chunk_size
                    end_idx = min(start_idx + chunk_size, round_end)
                    if start_idx >= round_end:
                        break
                    futures.append(executor.submit(process_chunk, i, server, start_idx, end_idx))

                for future in as_completed(futures):
                    server_idx, start_idx, embeddings = future.result()
                    for j, emb in enumerate(embeddings):
                        all_embeddings[start_idx + j] = emb

        return all_embeddings
    
    def embed_single(self, text: str, model: str = "small", timeout: int = 30) -> List[float]:
        """Generate embedding for a single text (uses first server)."""
        response = requests.post(
            self.servers[0],  # TEI root endpoint
            json={"inputs": text},  # TEI format (single string)
            timeout=timeout
        )
        response.raise_for_status()
        result = response.json()
        # TEI returns array of arrays for batch, single array for single text
        return result[0] if isinstance(result[0], list) else result
    
    def health_check(self) -> dict:
        """Check health of all servers."""
        results = {}
        for i, server in enumerate(self.servers):
            try:
                response = requests.get(f"{server}/health", timeout=5)
                response.raise_for_status()
                # TEI returns empty body with 200 OK
                results[f"gpu_{i+1}"] = {"status": "healthy"}
            except Exception as e:
                results[f"gpu_{i+1}"] = {"status": "error", "error": str(e)}
        return results
