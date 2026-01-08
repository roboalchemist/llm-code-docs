# Getting Started with Embedding Models & Vector Search

Quick start guides for different use cases and skill levels.

---

## Quick Start Scenarios

### Scenario 1: "I want to try embeddings locally in 5 minutes"

**Best Tool**: Ollama + Python

```bash
# 1. Install Ollama (macOS, Linux, Windows, Docker)
# https://ollama.ai

# 2. Download BGE-M3 (best open-source model, 92.5% accuracy)
ollama pull bge-m3

# 3. Run in Python
pip install ollama requests

# 4. Quick test
from ollama import Client
client = Client()
response = client.embeddings(
    model="bge-m3",
    prompt="Hello, world!"
)
print(response['embedding'])  # 1024-dim vector
```

**Why**: Simplest setup, no dependencies, runs on CPU, cross-platform.

---

### Scenario 2: "I need embeddings in my Python project"

**Best Tool**: Sentence-Transformers

```bash
# 1. Install
pip install sentence-transformers torch

# 2. Use in Python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # 384-dim, fast
sentences = ["How many people live in Berlin?", "Berlin has a population of 3.5 million"]

embeddings = model.encode(sentences)
print(embeddings.shape)  # (2, 384)

# 3. Compute similarity
from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
print(f"Similarity: {similarity:.4f}")
```

**Why**: Simple API, zero configuration, works with GPU if available, wide model support.

**Model Options**:
- `all-MiniLM-L6-v2` (384-dim): Fastest, light
- `all-mpnet-base-v2` (768-dim): Good quality/speed balance
- `e5-large-v2` (1024-dim): High quality, slower

---

### Scenario 3: "I need fast vector search on 10M+ vectors"

**Best Tool**: FAISS

```bash
# 1. Install
pip install faiss-cpu  # or faiss-gpu for GPU version

# 2. Create index and add vectors
import faiss
import numpy as np

# Generate sample vectors (768-dimensional)
d = 768  # vector dimension
nb = 1000000  # number of vectors
np.random.seed(0)
xb = np.random.random((nb, d)).astype('float32')

# Create index
index = faiss.IndexFlatL2(d)  # L2 distance
index.add(xb)

# Search
k = 5  # return top 5
xq = np.random.random((10, d)).astype('float32')  # 10 queries
distances, indices = index.search(xq, k)

print(f"Top 5 results for query 0: {indices[0]}")
```

**Why**: Fastest for large-scale, supports GPU, versatile indexing options.

**Index Types**:
- `IndexFlatL2`: Exact search (baseline)
- `IndexIVFFlat`: Approximate, faster
- `IndexHNSW`: Approximate, fast
- `IndexPQ`: Compressed, memory-efficient

---

### Scenario 4: "I need a vector database for my RAG application"

**Option A: Self-Hosted & Lightweight** → Chroma

```bash
# 1. Install
pip install chromadb

# 2. Create collection and add documents
import chromadb

client = chromadb.Client()
collection = client.create_collection(name="my_collection")

# Add documents with embeddings
collection.add(
    ids=["id1", "id2"],
    documents=["Document 1", "Document 2"],
    metadatas=[{"source": "web"}, {"source": "file"}]
)

# Query
results = collection.query(
    query_texts=["similarity search"],
    n_results=2
)
print(results['documents'])
```

**Why**: Simplest to set up, perfect for RAG, beginner-friendly.

---

**Option B: Production & Scalable** → Qdrant

```bash
# 1. Install (or use Docker)
pip install qdrant-client

# 2. Create client and collection
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams

client = QdrantClient(":memory:")  # or URL for remote

client.create_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE),
)

# 3. Add vectors
from qdrant_client.models import PointStruct

points = [
    PointStruct(
        id=1,
        vector=[0.1] * 384,  # 384-dimensional vector
        payload={"text": "Example document"}
    )
]
client.upsert(collection_name="my_collection", points=points)

# 4. Search
search_result = client.search(
    collection_name="my_collection",
    query_vector=[0.1] * 384,
    limit=5
)
```

**Why**: Production-ready, distributed, rich filtering, Rust-based performance.

---

**Option C: Fully Managed** → Pinecone

```bash
# 1. Get API key from https://www.pinecone.io/
# 2. Install
pip install pinecone-client

# 3. Initialize
from pinecone import Pinecone

pc = Pinecone(api_key="YOUR_API_KEY")
index = pc.Index("my-index")

# 4. Upsert vectors
index.upsert(vectors=[
    {"id": "1", "values": [0.1] * 1536, "metadata": {"text": "Document 1"}},
    {"id": "2", "values": [0.2] * 1536, "metadata": {"text": "Document 2"}},
])

# 5. Query
results = index.query(
    vector=[0.1] * 1536,
    top_k=5,
    include_metadata=True
)
```

**Why**: Zero ops, <50ms latency, enterprise-ready, automatic scaling.

---

### Scenario 5: "I want to build a semantic search engine"

**Complete Stack**:

```python
# 1. Generate embeddings from documents
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-mpnet-base-v2')

documents = [
    "Python is a programming language",
    "Java is also a programming language",
    "Dogs are pets",
]

embeddings = model.encode(documents)

# 2. Create FAISS index
d = embeddings.shape[1]  # 768
index = faiss.IndexFlatL2(d)
index.add(np.array(embeddings).astype('float32'))

# 3. Search
query = "What is Python?"
query_embedding = model.encode([query])[0]
distances, indices = index.search(np.array([query_embedding]).astype('float32'), k=3)

# 4. Display results
for idx in indices[0]:
    print(f"- {documents[idx]}")
```

**Upgrade Path**:
- Start: Sentence-Transformers + FAISS (above)
- Scale: Add Qdrant/Weaviate for persistence
- Production: Use Pinecone or managed cloud vector DB

---

## Decision Trees

### "What embedding model should I use?"

```
Start
├─ Cost is critical?
│  ├─ Yes → Use free open-source (BGE-M3, E5-small via Ollama)
│  └─ No  → Continue
├─ Need multilingual?
│  ├─ Yes → OpenAI text-embedding-3 or Voyage-Multilingual-2
│  └─ No  → Continue
├─ Speed is critical?
│  ├─ Yes → Cohere Embed v3 (fast API) or E5-small (local)
│  └─ No  → OpenAI text-embedding-3 or Jina embeddings
└─ Self-hosted only?
   ├─ Yes → BGE-M3 (best quality) or E5-small (best speed)
   └─ No  → OpenAI text-embedding-3 (industry standard)
```

### "What vector search library should I use?"

```
Start
├─ Data size < 10M vectors?
│  ├─ Yes, CPU only → hnswlib (fastest CPU)
│  └─ Yes, have GPU → FAISS (GPU acceleration)
├─ Data size 10M - 100M?
│  ├─ Memory critical → ScaNN (10x compression)
│  └─ Normal → FAISS with IVF-PQ
├─ Data size > 100M?
│  ├─ Fits in RAM → Milvus + hnswlib
│  └─ Doesn't fit → DiskANN or vector database
├─ Need persistence?
│  └─ Yes → Use vector database instead
└─ Real-time low latency (<5ms)?
   └─ Yes → Annoy
```

### "What vector database should I use?"

```
Start
├─ Just prototyping/learning?
│  └─ Yes → Chroma (simplest)
├─ Need managed service?
│  ├─ Yes → Pinecone (fastest, $$$)
│  └─ No  → Continue
├─ Need hybrid search (text + vectors)?
│  ├─ Yes → Elasticsearch or Vespa
│  └─ No  → Continue
├─ Scale requirements?
│  ├─ < 1B vectors → Qdrant or Weaviate
│  ├─ > 1B vectors → Milvus
│  └─ Cloud-native → Pinecone or MongoDB Atlas
└─ Special requirements?
   ├─ PostgreSQL user? → pgvector
   ├─ Filtering/ACID? → Qdrant (advanced filtering, ACID)
   ├─ GraphQL API? → Weaviate
   └─ Distributed? → Milvus
```

---

## Common Patterns

### Pattern 1: RAG with Embeddings

```python
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Setup
model = SentenceTransformer('all-mpnet-base-v2')
client = chromadb.Client()
collection = client.create_collection(name="documents")

# 2. Index documents
documents = ["Document 1", "Document 2", "Document 3"]
embeddings = model.encode(documents)

collection.add(
    ids=[str(i) for i in range(len(documents))],
    embeddings=embeddings.tolist(),
    documents=documents
)

# 3. Retrieve on query
query = "Search query"
query_embedding = model.encode([query])[0]

results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)

# 4. Pass to LLM
context = "\n".join(results['documents'][0])
# Use context with LLM for generation
```

### Pattern 2: Real-Time Recommendations

```python
import annoy

# Build index
f = 128  # feature dimension
t = annoy.AnnoyIndex(f, metric='angular')

# Add items
for i, vector in enumerate(user_vectors):
    t.add_item(i, vector)

t.build(10)  # 10 trees

# Get recommendations for user
user_id = 0
similar_users = t.get_nns_by_item(user_id, 5)  # Top 5 similar
print(f"Similar users: {similar_users}")
```

### Pattern 3: Semantic Deduplication

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-mpnet-base-v2')

# Get embeddings
documents = ["Doc A", "Doc B", "Doc C"]
embeddings = model.encode(documents)

# Compute similarity matrix
similarity = cosine_similarity(embeddings)

# Find duplicates (threshold > 0.95)
threshold = 0.95
duplicates = []
for i in range(len(documents)):
    for j in range(i+1, len(documents)):
        if similarity[i][j] > threshold:
            duplicates.append((i, j, similarity[i][j]))

for i, j, sim in duplicates:
    print(f"Document {i} and {j} are similar: {sim:.4f}")
```

---

## Performance Benchmarks

### Embedding Model Speed (1000 sentences)

| Model | Speed (CPU) | Speed (GPU) | Dimension |
|-------|-----------|-----------|-----------|
| all-MiniLM-L6-v2 | ~8s | ~1s | 384 |
| all-mpnet-base-v2 | ~15s | ~2s | 768 |
| e5-large-v2 | ~25s | ~3s | 1024 |
| BGE-M3 | ~30s | ~4s | 1024 |

### Vector Search Speed (1M vectors, 768-dim, 100 queries)

| Library | Speed | Recall | Memory |
|---------|-------|--------|--------|
| FAISS-IVF | ~50ms | 95% | ~800MB |
| hnswlib | ~100ms | 98% | ~2.5GB |
| Annoy | ~5ms | 85% | ~500MB |
| ScaNN | ~30ms | 96% | ~300MB |

### Vector Database Latency (p99)

| Database | Insert | Query | Scale |
|----------|--------|-------|-------|
| Pinecone | ~100ms | <50ms | 100B+ |
| Qdrant | ~50ms | <200ms | 10B+ |
| Weaviate | ~100ms | <300ms | 10B+ |
| Chroma | ~10ms | ~50ms | 100M+ |
| Milvus | ~100ms | ~200ms | Massive |

---

## Troubleshooting

### "My embeddings are all similar (similarity ~1.0)"

**Problem**: Model might be returning unnormalized vectors or there's a bug.

**Solution**:
```python
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-mpnet-base-v2')
embeddings = model.encode(["text1", "text2"], normalize_embeddings=True)

# Check if normalized
norm = np.linalg.norm(embeddings[0])
print(f"Vector norm: {norm}")  # Should be close to 1.0 if normalized
```

### "FAISS index is using too much memory"

**Problem**: Using exact search (IndexFlatL2) or uncompressed index.

**Solution**: Use compressed index
```python
import faiss

# Instead of:
# index = faiss.IndexFlatL2(d)

# Use compressed:
quantizer = faiss.IndexFlatL2(d)
index = faiss.IndexIVFPQ(quantizer, d, 100, 8)  # 100 clusters, 8-bit quantization
index.train(training_vectors)
```

### "Vector database insert is slow"

**Problem**: Inserting vectors one at a time instead of batch.

**Solution**: Batch inserts
```python
# Slow
for vector in vectors:
    collection.add(ids=[id], vectors=[vector])

# Fast
collection.add(
    ids=ids,
    vectors=vectors  # Batch all at once
)
```

### "Search results are bad quality"

**Problem**: Possibly wrong embedding model or poor semantic match.

**Solution**:
1. Try stronger embedding model (e.g., upgrade from all-MiniLM to BGE-M3)
2. Check if documents need preprocessing
3. Verify embedding dimension matches indexing
4. Use reranking (semantic, learned, or keyword-based)

---

## Next Steps

1. **Start Small**: Pick one scenario above and try the code
2. **Benchmark**: Test on your actual data
3. **Scale**: Move to vector database when needed
4. **Optimize**: Use the comparison tables to choose better tools
5. **Monitor**: Track latency, recall, and memory usage

---

## Additional Resources

- **Official Docs**: See EMBEDDING_VECTOR_RESEARCH.md for complete links
- **Benchmarks**: https://ann-benchmarks.com
- **MTEB Leaderboard**: https://huggingface.co/spaces/mteb/leaderboard
- **Hugging Face Hub**: https://huggingface.co/models (search "embedding")
- **Papers**: arXiv papers on vector search and dense embeddings

---

**Last Updated**: December 31, 2025
**For Questions**: See EMBEDDING_VECTOR_RESEARCH.md for detailed analysis
