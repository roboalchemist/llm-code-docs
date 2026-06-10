# Indexing Reliability Improvements

## Critical Issues to Fix

### 1. Silent Failures → Loud Failures
**Current**: Returns zero vectors when server unavailable
**Fix**: Raise exception immediately, don't continue

```python
# generator.py - Remove silent fallback
except Exception as e:
    print(f"\nError generating batch embeddings: {e}")
    # DELETE THIS: for _ in batch_texts: all_embeddings.append([0.0] * config.EMBEDDING_DIMENSION)
    # ADD THIS:
    raise RuntimeError(f"Embedding generation failed: {e}. Server may be down.") from e
```

### 2. Resume Capability
**Current**: Starts from scratch every time (wastes 3+ minutes)
**Fix**: Save checkpoints and resume

```python
# builder.py - Add checkpoint system
def _index_documents_with_resume(self, documents: List[DocumentInfo]):
    checkpoint_file = config.LANCEDB_DIR / ".rebuild_checkpoint.json"

    # Load checkpoint if exists
    if checkpoint_file.exists():
        checkpoint = json.load(open(checkpoint_file))
        processed_paths = set(checkpoint.get("processed_paths", []))
        print(f"Resuming from checkpoint: {len(processed_paths)} documents already processed")
    else:
        processed_paths = set()

    # Process only unprocessed documents
    remaining_docs = [d for d in documents if str(d.path) not in processed_paths]

    # ... process and save checkpoint every 1000 documents ...

    # Delete checkpoint when complete
    checkpoint_file.unlink(missing_ok=True)
```

### 3. Server Health Monitoring
**Current**: Only checks health at startup
**Fix**: Monitor during processing

```python
# generator.py - Add health checks
def _check_server_health(self):
    try:
        response = requests.get(f"{self.api_url}/health", timeout=5)
        response.raise_for_status()
        return True
    except Exception as e:
        raise RuntimeError(f"Server health check failed: {e}")

def generate(self, texts, batch_size=None, show_progress=True):
    # Check health before starting
    self._check_server_health()

    # Check every 50 batches during processing
    for i in iterator:
        if i > 0 and i % 50 == 0:
            self._check_server_health()

        # ... process batch ...
```

### 4. Better Error Messages
**Current**: Generic "Connection refused"
**Fix**: Specific actionable errors

```python
# generator.py - Improved error handling
try:
    response = requests.post(...)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    raise RuntimeError(
        f"Cannot connect to embedding server at {self.api_url}. "
        f"Please ensure the server is running:\n"
        f"  cd /tmp/qwen3-embeddings-mlx\n"
        f"  PORT=10001 python server.py"
    )
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 404:
        raise RuntimeError(
            f"Endpoint {e.request.url} not found. "
            f"Server may be running wrong application."
        )
    raise
```

### 5. Progress Persistence
**Current**: Lost on crash
**Fix**: Save to database incrementally

```python
# builder.py - Incremental inserts
def _index_documents(self, documents, is_update=False):
    # Process in batches of 1000 documents
    for doc_batch in chunks(documents, 1000):
        records, texts = self._prepare_batch(doc_batch)
        embeddings = self.generator.generate(texts)

        # Insert immediately (don't wait for all docs)
        self.db.documents_table.add(records)

        # Update checkpoint
        self._save_checkpoint(doc_batch)

    # Create index only at the end
    self._create_indices()
```

## Implementation Priority

1. **Immediate (5 min)**: Remove silent zero-vector fallback
2. **High (20 min)**: Add checkpoint/resume system
3. **Medium (10 min)**: Add server health monitoring
4. **Low (5 min)**: Improve error messages

## Testing

```bash
# Test failure scenarios
1. Stop server mid-process → should fail loudly, save checkpoint
2. Resume after stopping → should continue from checkpoint
3. Wrong port configured → should give clear error message
4. Server returns 404 → should explain endpoint issue
```

## Benefits

- **Save time**: Resume instead of restarting (~3 min saved per failure)
- **Clear errors**: Know exactly what's wrong and how to fix it
- **Reliability**: Detect server crashes immediately
- **Data safety**: Incremental saves prevent total loss
