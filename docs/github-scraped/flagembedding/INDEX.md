# BGE Embedding Models Documentation

This directory contains the BAAI General Embedding (BGE) documentation extracted from the FlagEmbedding repository.

## Overview

BGE (BAAI General Embedding) is a series of open-source embedding models developed by the Beijing Academy of Artificial Intelligence (BAAI). The models are optimized for production-grade retrieval and semantic search tasks.

## Key Features

- **Top MTEB Performance**: Ranking among the highest performing models on the Massive Text Embedding Benchmark
- **Multilingual Support**: BGE-M3 supports 100+ languages
- **Dense Retrieval**: Optimized for semantic search and document embedding
- **Hybrid Retrieval**: Support for combining dense embeddings with sparse retrievers
- **Instruction-Tuned Variants**: Special prompts to align embeddings with specific tasks

## Model Variants

- **BGE-Base-EN / BGE-Large-EN**: English-specific models
- **BGE-Large-EN-v1.5**: Enhanced large English model with 1024-dim vectors
- **BGE-M3**: Multilingual model supporting 100+ languages with 8192 token context
- **BGE-Reranker**: Cross-encoder models for re-ranking search results
- **BGE-VL**: Multimodal models supporting visual search

## Quick Links

- **Official Website**: https://bge-model.com
- **GitHub**: https://github.com/FlagOpen/FlagEmbedding
- **Hugging Face**: https://huggingface.co/BAAI
- **Paper**: https://arxiv.org/abs/2309.07597

## Documentation Structure

- `docs/source/`: Main documentation in Sphinx/RST format
  - `Introduction/`: Introduction and getting started guides
  - `tutorial/`: Comprehensive tutorials
  - `API/`: API reference documentation
  - `FAQ/`: Frequently asked questions
  - `bge/`: BGE-specific documentation
  - `community/`: Community resources
  
- `examples/`: Usage examples for embedder and reranker
- `research/`: Research projects and implementations

## Installation

```bash
pip install -U FlagEmbedding
```

## Basic Usage

### Using FlagEmbedding Library

```python
from FlagEmbedding import FlagModel

model = FlagModel('BAAI/bge-base-en-v1.5',
                  query_instruction_for_retrieval="Represent this sentence for searching relevant passages:",
                  use_fp16=True)

sentences_1 = ["What is BGE?", "How to use BGE?"]
sentences_2 = ["BGE is an embedding model", "You can use BGE by loading the model"]

embeddings_1 = model.encode(sentences_1)
embeddings_2 = model.encode(sentences_2)

scores = embeddings_1 @ embeddings_2.T
print(scores)
```

### Using Sentence Transformers

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('BAAI/bge-base-en-v1.5')
embeddings = model.encode(["This is a sample sentence", "Each sentence is converted to a vector"])
```

### Using Transformers Library

```python
from transformers import AutoTokenizer, AutoModel
import torch

tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-base-en-v1.5')
model = AutoModel.from_pretrained('BAAI/bge-base-en-v1.5')
```

## Integration with Vector Databases

BGE embeddings can be integrated with various vector databases:

- **Milvus**: For scalable vector search
- **Pinecone**: For serverless vector database
- **Chroma**: For lightweight vector storage
- **Weaviate**: For vector search with semantic understanding
- **Qdrant**: For vector similarity search

## RAG Pipeline Integration

Use BGE with RAG frameworks:

- **LangChain**: Full integration support
- **LlamaIndex**: Direct embedding model support
- **Haystack**: Compatible embeddings
- **OpenAI Cookbook**: RAG examples using BGE

## Multilingual Support

BGE-M3 supports retrieval in 100+ languages:

```python
from FlagEmbedding import FlagModel

model = FlagModel('BAAI/bge-m3', use_fp16=True)

# Dense embedding
dense_embeddings = model.encode(documents, batch_size=256)

# Sparse embedding (BM25-like)
sparse_embeddings = model.encode_multi(documents, batch_size=256)

# Colbert embedding
colbert_embeddings = model.encode_multi(documents, batch_size=256)
```

## Performance Benchmarks

- **MTEB Benchmark**: Top-ranked among open-source models
- **C-MTEB**: Leading performance on Chinese text embeddings
- **MIRACL**: Best multilingual cross-lingual retrieval

## Community and Support

- **GitHub Issues**: https://github.com/FlagOpen/FlagEmbedding/issues
- **WeChat Group**: Scan QR code in README
- **Discussions**: https://github.com/FlagOpen/FlagEmbedding/discussions

## Citation

If you use BGE in your research, please cite:

```bibtex
@article{bge,
  title={C-Pack: Packaged Resources To Advance General and Chinese Text Embeddings},
  author={Wang, Shitao and Xie, Jing and Zhu, Wentao and others},
  journal={arXiv preprint arXiv:2309.07597},
  year={2023}
}
```

## License

MIT License - See LICENSE file for details

## Source

This documentation is extracted from the [FlagEmbedding](https://github.com/FlagOpen/FlagEmbedding) repository.

Last updated: January 1, 2026
