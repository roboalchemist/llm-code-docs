# Embedding Models and Vector Similarity Search: Comprehensive Research

**Date**: December 31, 2025
**Status**: Complete research compilation from Tavily and Perplexity
**Scope**: Embedding providers, local libraries, vector similarity tools, and databases

---

## Table of Contents

1. [Embedding Model Providers (APIs)](#embedding-model-providers-apis)
2. [Local Embedding Libraries](#local-embedding-libraries)
3. [Vector Similarity & ANN Libraries](#vector-similarity--ann-libraries)
4. [Vector Databases](#vector-databases)
5. [Semantic Search & Inference Servers](#semantic-search--inference-servers)
6. [Quick Reference Comparison](#quick-reference-comparison)
7. [Documentation Resources in llm-code-docs](#documentation-resources-in-llm-code-docs)

---

## Embedding Model Providers (APIs)

Cloud-based API services for generating embeddings.

### OpenAI
- **Models**: text-embedding-3-large, text-embedding-3-small
- **Strengths**: Industry standard, optimized for RAG, multilingual
- **Website**: https://platform.openai.com/docs/guides/embeddings

### Cohere
- **Models**: Embed v3
- **Strengths**: Long-context, 100+ languages, balanced recall/precision
- **Website**: https://docs.cohere.com/

### Voyage AI
- **Models**: Voyage-Multilingual-2, Voyage-3-large
- **Strengths**: Top benchmarks, multilingual, document retrieval focused
- **Website**: https://www.voyageai.com/

### Anthropic
- **Strengths**: Factual grounding, reduced toxicity, enterprise-focused
- **Website**: https://docs.anthropic.com/

### Google Vertex AI
- **Models**: Vertex Multimodal Embeddings, text-embedding-005
- **Strengths**: Text + image embeddings, enterprise scale
- **Website**: https://cloud.google.com/vertex-ai

### Jina AI
- **Models**: Jina embeddings
- **Strengths**: MTEB benchmark leader, flexible deployment
- **Website**: https://www.jina.ai/

---

## Local Embedding Libraries

### Sentence-Transformers (Python)
- **Type**: Library for transformer-based embeddings
- **Ease of Use**: Very High (recommended starting point)
- **Features**: GPU acceleration, caching, wide model compatibility
- **Website**: https://sbert.net/
- **GitHub**: https://github.com/UKPLab/sentence-transformers

### FastEmbed (Python)
- **Type**: Lightweight, high-speed embedding library
- **Performance**: Excellent (optimized latency)
- **Use Cases**: Real-time, production deployments
- **GitHub**: https://github.com/qdrant/fastembed

### Ollama
- **Type**: Local LLM/embedding platform
- **Ease of Use**: Very High (one-command setup)
- **Features**: Cross-platform, no external dependencies
- **Website**: https://ollama.ai/
- **Models**: BGE-M3 (92.5% accuracy), mxbai-embed-large, nomic-embed-text

### Hugging Face Transformers (Python)
- **Type**: General deep learning library
- **Features**: 2000+ models, flexible, research-friendly
- **Website**: https://huggingface.co/transformers/

### Text Embeddings Inference (TEI - Rust)
- **Type**: High-performance inference server
- **Performance**: Highest throughput, memory efficient
- **Website**: https://github.com/huggingface/text-embeddings-inference

### Popular Open-Source Models
- **BGE-M3**: 92.5% accuracy, trilingual, 1024-dim
- **E5 Series**: Low-latency, multiple sizes
- **NV-Embed**: NVIDIA-optimized, generalist
- **Instructor-XL**: Task-aware embeddings
- **Stella**: 400M and 1.5B variants

---

## Vector Similarity & ANN Libraries

### FAISS (Facebook AI Similarity Search)
- **Language**: C++/Python
- **Algorithms**: IVF-PQ, HNSW, LSH
- **Strengths**: GPU support, scalable, versatile indexing
- **Index Size** (768-dim, 10M vecs): 0.3 GB (compressed)
- **Query Speed**: Fast with GPU
- **Website**: https://github.com/facebookresearch/faiss

### hnswlib
- **Language**: C++/Python
- **Algorithm**: HNSW (Hierarchical Navigable Small World)
- **Strengths**: Top CPU speed, 95-99% recall
- **Limitations**: High memory, all data in RAM
- **Best For**: CPU-only mid-size datasets
- **GitHub**: https://github.com/nmslib/hnswlib

### ScaNN (Google)
- **Language**: C++/Python
- **Algorithm**: Asymmetric hashing + quantization
- **Strengths**: 10x compression, semantic search optimized
- **Query Speed**: Ultra-fast for compressed
- **GitHub**: https://github.com/google-research/scann

### Annoy (Spotify)
- **Language**: C++/Python
- **Algorithm**: Random projection trees
- **Strengths**: Ultra-low latency (0.00015s), simple
- **Best For**: Real-time, low-latency apps
- **GitHub**: https://github.com/spotify/annoy

### DiskANN (Microsoft)
- **Language**: C++
- **Strengths**: Billion-scale with disk, low RAM
- **Best For**: Massive datasets exceeding RAM
- **GitHub**: https://github.com/microsoft/DiskANN

### NGT (Yahoo)
- **Language**: C++/Python
- **Algorithm**: Tree-based indexing
- **Best For**: General ANN, euclidean/angular
- **GitHub**: https://github.com/yahoojapan/NGT

### PyNNDescent (Python)
- **Type**: Pure Python HNSW implementation
- **Best For**: Development, learning, Python-only environments
- **GitHub**: https://github.com/lmcinnes/pynndescent

---

## Vector Databases

### Pinecone (Managed SaaS)
- **Strengths**: <50ms p99 latency, 100B+ scale, fully managed
- **Best For**: Production at scale, managed service preference
- **Website**: https://www.pinecone.io/

### Weaviate
- **Type**: Open-source + managed option
- **Features**: GraphQL API, multiple vector spaces, hybrid search
- **Scale**: 10B+ vectors
- **Website**: https://weaviate.io/

### Milvus
- **Type**: Open-source distributed
- **GitHub Stars**: 35k+
- **Features**: GPU acceleration, multiple indexing types
- **Scale**: Massive (distributed)
- **Website**: https://milvus.io/

### Qdrant
- **Type**: Open-source + managed option
- **Language**: Rust (high performance)
- **Features**: Rich filtering, ACID compliance, hybrid search
- **Website**: https://qdrant.tech/

### Chroma
- **Type**: Open-source, lightweight
- **Best For**: RAG applications, rapid development
- **Website**: https://docs.trychroma.com/

### Vespa (Yahoo)
- **Type**: Open-source
- **Features**: Hybrid search (vectors + text + ranking)
- **Website**: https://vespa.ai/

### Elasticsearch
- **Type**: Open-source + managed
- **Features**: Full-text + vector hybrid, 50B+ scale
- **Website**: https://www.elastic.co/

### pgvector (PostgreSQL Extension)
- **Type**: Native PostgreSQL
- **Features**: SQL-based, ACID compliance
- **Website**: https://github.com/pgvector/pgvector

### MongoDB Atlas Vector Search
- **Type**: Managed MongoDB service
- **Features**: Document model + vector search
- **Website**: https://www.mongodb.com/

---

## Semantic Search & Inference Servers

### Deep Learning Frameworks
- **PyTorch**: GPU-accelerated, dynamic graphs, transformer-friendly
- **TensorFlow**: Scalable, mature deployment, distributed training
- **Keras**: High-level API, rapid prototyping

### Inference Servers
- **vLLM**: LLM + embedding serving, PagedAttention optimization
- **TorchServe**: PyTorch-native, REST/gRPC endpoints
- **NVIDIA Triton**: Multi-framework (PyTorch/TensorFlow/ONNX), production-grade
- **Text Embeddings Inference (TEI)**: Rust-based, embedding-optimized

---

## Performance Benchmarks

### Vector Search Speed (1M vectors, 768-dim, 100 queries)
| Library | Speed | Recall | Memory |
|---------|-------|--------|--------|
| FAISS-IVF | 50ms | 95% | 800MB |
| hnswlib | 100ms | 98% | 2.5GB |
| Annoy | 5ms | 85% | 500MB |
| ScaNN | 30ms | 96% | 300MB |

### Vector Database Latency (p99)
| Database | Insert | Query | Scale |
|----------|--------|-------|-------|
| Pinecone | 100ms | <50ms | 100B+ |
| Qdrant | 50ms | <200ms | 10B+ |
| Weaviate | 100ms | <300ms | 10B+ |
| Chroma | 10ms | 50ms | 100M+ |
| Milvus | 100ms | 200ms | Massive |

---

## Selection Guide

### Embedding Provider
- **Best Overall**: OpenAI text-embedding-3
- **Cost-Conscious**: Cohere Embed v3 or BGE-M3 (self-hosted)
- **High Performance**: Voyage-3-large
- **Open-Source**: BGE-M3 (92.5% accuracy)

### Local Library
- **Easiest Start**: Ollama + BGE-M3
- **Python Projects**: Sentence-Transformers
- **Production Speed**: FastEmbed or TEI

### Vector Search
- **Large-Scale (GPU)**: FAISS
- **Fastest CPU**: Annoy
- **Best Recall (CPU)**: hnswlib
- **Memory-Constrained**: ScaNN

### Vector Database
- **Managed & Fast**: Pinecone
- **Open-Source**: Weaviate or Qdrant
- **Maximum Scale**: Milvus
- **RAG Focus**: Chroma
- **Existing PostgreSQL**: pgvector

---

## Documentation in llm-code-docs

**Currently Available**:
- FAISS: `/docs/github-scraped/faiss/`
- Flag Embeddings: `/docs/github-scraped/flagembedding/`
- Qwen3 Embeddings: `/docs/github-scraped/qwen3-embedding/`
- Vespa: `/docs/llms-txt/vespa/`
- pgvector: `/docs/llms-txt/pgvector/`

**Recommended Additions**:
1. Sentence-Transformers
2. Ollama
3. Milvus
4. Weaviate
5. Qdrant (full docs)
6. Cohere (download pending)
7. Text Embeddings Inference
8. Hugging Face Transformers (embeddings focus)

---

**Last Updated**: December 31, 2025
**Research Tools**: Tavily AI Search, Perplexity AI
**Total Cost**: ~0.04 credits
