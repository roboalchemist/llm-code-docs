# RAG Documentation Tickets Created

**Date:** January 1, 2026
**Project:** DOCS (llm-code-docs)
**Label:** docs-add
**Status:** todo
**Priority:** medium

## Summary

Successfully created **86 new tickets** for missing RAG-related documentation in the llm-code-docs repository.

- **Total RAG tools in list:** 88
- **Already had documentation:** 2 (Hugging Face Transformers, NLP Cloud)
- **New tickets created:** 86

## Analysis

### RAG Tools Already Documented
1. **Hugging Face Transformers** - docs/llms-txt/huggingface-transformers/
2. **NLP Cloud** - docs/llms-txt/cloud/

### Missing RAG Tools (New Tickets Created)

#### Vector Databases & Search Engines (17 items)
- Annoy - Approximate Nearest Neighbors library for similarity search and vector indexing
- Azure Cosmos DB - Globally distributed NoSQL database with vector search capabilities
- ClickHouse - Columnar database optimized for analytical queries and vector operations
- Deep Lake - Vector database for building and managing RAG data pipelines
- Elasticsearch - Distributed search engine with vector search and RAG capabilities
- HNSW - Hierarchical Navigable Small World algorithm for approximate nearest neighbor search
- Hnswlib - C++ implementation of HNSW algorithm for efficient vector similarity search
- KDB.AI - Vector database built on KDB+ for high-performance similarity search
- Marqo - Tensor search engine for building RAG systems with multimodal search
- Milvus - Vector database optimized for similarity search in RAG applications
- MongoDB Atlas Vector Search - Vector search capability in MongoDB for RAG and semantic search
- Nmslib - Non-metric space library for approximate nearest neighbor search
- Oracle Database 23ai - Enterprise database with AI-powered vector and semantic search features
- ScaNN - Scalable nearest neighbors library by Google for efficient vector search
- Vald - Distributed fast similarity search engine for vector data
- Weaviate - Vector database and search engine designed for RAG applications
- YugabyteDB - Distributed SQL database with vector search for RAG workloads

#### RAG Frameworks & Platforms (11 items)
- FlashRAG - Fast and efficient framework for building RAG systems
- GraphRAG - Framework for building RAG systems with knowledge graph foundations
- Haystack - Framework for building RAG and search applications with large language models
- LightRAG - Lightweight framework for building Retrieval-Augmented Generation applications
- LLMWare - Modular framework for building RAG applications with enterprise features
- Pathway - Real-time data processing framework for building RAG pipelines
- R2R - Open-source framework for building production-ready RAG systems
- RAGFlow - End-to-end workflow platform for building and deploying RAG applications
- RAGatouille - Python library for deploying and managing ColBERT for efficient RAG
- Vectara - Generative search and RAG platform with built-in semantic understanding
- Verba - Open-source RAG framework with semantic search capabilities
- txtai - Semantic search engine and RAG framework built for simplicity

#### Embedding Models (10 items)
- all-MiniLM - Lightweight sentence embedding model optimized for semantic similarity
- BAAI BGE - Open-source BERT-based embedding model for semantic text representation
- BERT - Bidirectional Encoder Representations from Transformers for NLP tasks
- ColBERT - Contextualized Late Interaction BERT model for efficient semantic search
- E5 Embeddings - E5 multilingual embedding model for semantic search and RAG
- EmbeddingGemma - Google's Gemma embedding model for semantic text representation
- Nomic Embed - Open-source embedding model optimized for semantic search in RAG
- Stella Embeddings - High-performance embedding model for semantic similarity tasks
- Voyage Embeddings - Commercial embedding API for semantic search in RAG applications
- sentence-transformers - Framework for computing sentence embeddings and semantic similarity

#### Document Processing & Parsing (6 items)
- Docling - Document layout analysis and conversion tool for RAG data preparation
- LlamaParse - Parser for extracting structured content from documents for RAG systems
- MinerU - Lightweight PDF parsing library for extracting content for RAG applications
- PDFLoader - Tool for loading and parsing PDF documents in RAG pipelines
- PDFPlumber - PDF parsing library for extracting text and tables from documents
- PyPDF - Python library for reading and manipulating PDF documents

#### Evaluation & Monitoring (7 items)
- Arize - ML observability platform for monitoring RAG system performance
- Braintrust - Platform for testing and evaluating RAG and AI applications
- DeepEval - Evaluation framework for assessing LLM and RAG system quality
- Honeycomb - Observability platform for monitoring distributed systems and RAG applications
- LangSmith - Platform for developing, testing, and monitoring LLM applications
- RAGAS - Evaluation framework for assessing retrieval-augmented generation system quality
- WhyLabs - ML monitoring and observability platform for RAG system health

#### Inference & Model Services (15 items)
- Anyscale - Platform for running distributed Python and Ray applications
- DeepInfra - Inference API platform for running embeddings and language models
- DeepSeek - Open-source language model for RAG and semantic understanding
- Eden AI - Unified API for accessing multiple AI services and models
- Elastic Enterprise Search - Enterprise search platform with vector and semantic capabilities
- LocalAI - Local inference server for running embedding and language models privately
- Novita AI - AI platform and API for accessing various models and inference services
- Nuclia - Intelligent search and RAG platform with knowledge graph capabilities
- Ragie - Document processing platform optimized for RAG data extraction
- Replicate - Platform for running and sharing machine learning models
- Together AI - AI platform for deploying open-source models and building applications
- Voyage AI - Commercial embedding and retrieval API service for RAG applications
- vLLM - High-throughput inference engine for running language models in RAG
- xAI - AI research company with language models for semantic understanding

#### Search & Data APIs (5 items)
- Brave Search - Privacy-focused search API for RAG applications
- Bright Data - Web data collection platform for RAG training and evaluation data
- Latenode - Integration platform for connecting RAG systems to enterprise tools
- Linkup - Integration and orchestration platform for AI workflows
- Serper - Google search API for integrating web search into RAG applications

#### Workflow & Data Orchestration (8 items)
- Apache Airflow - Workflow orchestration platform for managing RAG data pipelines
- Dagster - Data orchestration platform for building complex RAG data pipelines
- Flyte - Kubernetes-native workflow orchestration for ML and data pipelines
- Kestra - Workflow orchestration platform for building data and ML pipelines
- Mage - Data orchestration platform for building RAG data preparation pipelines
- N8N - Low-code workflow automation platform for integrating RAG systems
- OpenTelemetry - Observability framework for monitoring RAG and AI applications
- Prefect - Modern workflow orchestration for building and monitoring data pipelines

#### Fine-Tuning & Optimization (5 items)
- Ailog - Logging framework for monitoring and debugging AI applications
- LoRA - Parameter-efficient fine-tuning technique for adapting models in RAG
- QLoRA - Quantized LoRA technique for efficient fine-tuning in resource-constrained RAG
- Semantic Router - Routing library for directing queries in RAG systems based on semantics

#### Auxiliary Tools (2 items)
- AutoGen - Framework for building multi-agent AI systems with RAG capabilities
- Shaped - Feature engineering and management platform for ML applications

## Ticket Coverage

All 86 tickets have been created with:
- **Title Format:** "Add {tool-name} documentation"
- **Project:** DOCS (project ID: 0e5104bf-8740-4115-9d70-5036b76186b3)
- **Status:** todo
- **Labels:** docs-add
- **Priority:** medium
- **Descriptions:** One-sentence descriptions customized per tool

## Next Steps

Documentation contributors can now:

1. Select a ticket from the DOCS project with the "docs-add" label
2. Research if the tool has:
   - llms.txt documentation (preferred - check via `/scripts/find-llms-txt.sh example.com`)
   - GitHub repository documentation
   - Web-scrapable documentation
3. Add documentation to the appropriate directory:
   - `docs/llms-txt/{tool-name}/` for llms.txt sites
   - `docs/github-scraped/{tool-name}/` for Git repositories
   - `docs/web-scraped/{tool-name}/` for web-scraped docs
4. Update the relevant configuration files (`scripts/llms-sites.yaml` or `scripts/repo_config.yaml`)
5. Commit and push changes following the standard workflow

## Priority Items

Based on RAG importance, these tools should be prioritized:

**High Priority (Core RAG Infrastructure):**
- Haystack, Weaviate, Milvus, Elasticsearch, RAGAS, RAGFlow, Langchain (already exists)
- LLM frameworks: Verba, R2R, Vectara

**Medium Priority (Key Components):**
- Embedding models: sentence-transformers, BAAI BGE, all-MiniLM
- Vector DBs: Pinecone (already exists), Deep Lake, Marqo
- Document processing: PDFPlumber, Docling, LlamaParse
- Orchestration: Apache Airflow, Dagster

**Integration Priority:**
- Search APIs: Serper, Brave Search
- Inference: DeepInfra, vLLM, LocalAI
- Evaluation: DeepEval, Braintrust, LangSmith

## Related Files

- `ERP_TICKETS_CREATED.md` - Similar process for ERP documentation (93 tickets created)

---

**Task Completion:** ✓ All 86 RAG documentation tickets successfully created in DOCS project
