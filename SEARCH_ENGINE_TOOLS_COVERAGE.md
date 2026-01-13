# Search Engine Tools Documentation Coverage Report

**Date:** January 1, 2026
**Total Tools:** 102
**Documentation Coverage:** 13 tools (12.7%)

---

## HAVE Documentation (13 items)

### llms-txt Directories (9 tools)
- **Jina** - Cloud-native neural search framework for multimodal search
- **LanceDB** - Vector database for AI applications with serverless architecture
- **Meilisearch** - Lightweight full-text search engine with typo tolerance
- **Mintlify** - Modern documentation platform with AI-powered search
- **pgvector** - PostgreSQL extension for vector similarity search
- **Pinecone** - Cloud-native vector database for similarity search at scale
- **Qdrant** - Vector database for similarity search and semantic search applications
- **Sourcegraph** - Code search and intelligence platform
- **Vespa** - Big data serving engine with machine learning and search capabilities

### github-scraped Directories (4 tools)
- **Chroma** - Open-source embedding database for AI applications
- **Docusaurus** - Documentation site generator with built-in search
- **FAISS** - Facebook AI library for efficient similarity search and clustering
- **OpenSearch** - Open-source fork of Elasticsearch for search and analytics

---

## MISSING Documentation (89 items)

### A-C
- Algolia
- Amazon OpenSearch Service
- Annoy
- Apache Pinot
- Arc Search
- Atlassian Search API
- Azure Cognitive Search
- Baidu Search
- Bing Search API
- Bleve
- Brave Search API
- ChatGPT Search
- Cludo
- Coveo

### D-G
- Document360
- DuckDB FTS
- DuckDuckGo API
- ELK Stack
- ElasticPress
- Elasticsearch
- Elasticsearch-py
- Exa API
- Facet
- FacetWP
- FlexSearch
- GitHub Code Search
- Google AI Mode
- Google Custom Search
- Google Custom Search API
- Graylog
- Gumshoe

### H-M
- Haystack
- Humio
- IndexNow
- Ivory Search
- Jetpack Search
- Loki
- Lunr.js
- Manticore
- MediaStack API
- MetaGer
- Microsoft Copilot
- Milvus
- MiniSearch
- MongoDB Atlas Search
- MySQL FTS

### N-R
- NewsAPI
- Nuclino
- Perplexity AI
- Perplexity API
- Phind
- PostgreSQL FTS
- Quickwit
- Read the Docs
- Relevanssi
- Relixir
- Rockset

### S-T
- SearchWP
- Searchcode
- Searx
- SearXNG
- Semrush
- SerpAPI
- Serper
- SharePoint Search REST API
- Silver Searcher
- Sinequa
- Solr
- Sonic
- Sphinx
- Sphinx Search
- Splunk
- SQLite FTS
- Swiftype
- Tantivy
- Tavily API
- Typesense

### V-Z
- Vald
- Weaviate
- Whoosh
- Wolfram Alpha API
- WPSOLR
- Xapian
- You.com
- Zinc
- ZincSearch
- Zoho Search

### Command-line Tools
- ack
- ripgrep

---

## Analysis & Recommendations

### High-Priority Additions
These tools appear frequently in modern AI/development workflows and are candidates for documentation addition:

1. **Elasticsearch** - Foundational search technology used across enterprises
2. **Exa API** - Semantic search API optimized for AI applications
3. **Tavily API** - Search API specifically designed for LLM agents
4. **SerpAPI/Serper** - Search engine API integrations
5. **Haystack** - End-to-end RAG framework
6. **Weaviate** - Open-source vector database with ML modules
7. **Milvus** - Widely-used vector database for AI

### Coverage Gaps by Category

**Vector/Embedding Databases:** 3 of ~8 covered (Pinecone, LanceDB, Qdrant, pgvector)
- Missing: Weaviate, Milvus, Vald, Chroma (we have Chroma but for different reasons)

**API-Based Search:** 0 of ~10 covered
- Missing: Exa, SerpAPI, Serper, Tavily, DuckDuckGo, Brave, Bing

**Enterprise Search:** 2 of ~15 covered (OpenSearch, Sourcegraph)
- Missing: Elasticsearch, Solr, Splunk, Azure Cognitive Search, Algolia, Coveo

**Documentation Platforms:** 2 of ~5 covered (Docusaurus, Mintlify)
- Missing: Read the Docs, Document360, Sphinx

**Full-Text Search Engines:** 1 of ~15 covered (Meilisearch)
- Missing: Manticore, Solr, Sonic, Tantivy, Typesense, Whoosh

**Command-Line Tools:** 0 of ~4 covered
- Missing: ack, ripgrep, Silver Searcher, Xapian

---

## Notes

1. **Perplexity** - We have the main "perplexity" directory in llms-txt covering both AI and API aspects
2. **Normalization Method** - Tools checked using case-insensitive, space/punctuation-normalized comparison against actual directory names
3. **Coverage Target** - Current coverage is 12.7%; aim should be ~30-40% for comprehensive search engine tools coverage
