# Jina AI Integrations

This directory contains documentation for Jina AI integrations with popular frameworks and libraries.

## Integration Categories

### LangChain Integration

Jina AI provides embeddings and reranking capabilities through LangChain:

- **JinaEmbeddings** - Text embedding model integration for Python and JavaScript
  - Supports multilingual text embedding with Jina's embedding models
  - Available in LangChain Python and LangChain JS

- **JinaReranker** - Document reranking for improving search results
  - Integrates with LangChain's document compression framework
  - Improves relevance of RAG (Retrieval Augmented Generation) results

## Supported Models

- `jina-embeddings-v3` - 570M parameter multilingual text embedding model
- `jina-embeddings-v4` - 3.8B parameter multimodal embedding model
- `jina-clip-v2` - Multimodal embedding for text-image retrieval
- `jina-reranker-v3` - Multilingual document reranking model
- `jina-reranker-m0` - Multimodal reranking supporting text and images

## Installation

### LangChain Python

```bash
pip install langchain-community langchain jina
```

### LangChain JavaScript

```bash
npm install @langchain/community @langchain/core
```

## Usage Examples

### Python - JinaEmbeddings

```python
from langchain_community.embeddings.jina import JinaEmbeddings

embeddings = JinaEmbeddings(
    model="jina-embeddings-v3",
    api_key="your-jina-api-key"
)

# Embed text

text = "Hello, world!"
embedding = embeddings.embed_query(text)
```

### Python - JinaReranker

```python
from langchain_community.document_compressors.jina_rerank import JinaRerank

reranker = JinaRerank(
    model="jina-reranker-v3",
    api_key="your-jina-api-key"
)

# Rerank documents

reranked_docs = reranker.compress_documents(docs, query)
```

## Documentation Links

- [Jina Official Documentation](https://docs.jina.ai/)
- [LangChain Jina Integration Docs](https://python.langchain.com/docs/integrations/providers/jina/)
- [LangChain Community GitHub](https://github.com/langchain-ai/langchain)

## API Key Setup

Get your Jina API key for free at: https://jina.ai/?sui=apikey

Set the environment variable:

```bash
export JINA_API_KEY="your-api-key"
```

## Features

- **Multilingual Support**: Embedding models support 100+ languages
- **Multimodal Capabilities**: Some models support both text and images
- **High Performance**: Optimized for production use with low latency
- **Flexible Dimensions**: Truncate embeddings to desired dimensions
- **Task-Specific Optimization**: Different embedding modes for different tasks

## Support

For issues and questions:
- GitHub: https://github.com/jina-ai/jina
- Documentation: https://docs.jina.ai/
- Community Forum: https://github.com/jina-ai/jina/discussions
