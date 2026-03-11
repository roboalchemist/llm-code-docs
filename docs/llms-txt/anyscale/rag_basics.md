# Source: https://docs.anyscale.com/rag/rag_basics.md

# RAG basics

[View Markdown](/rag/rag_basics.md)

# RAG basics

This page provides an overview of Retrieval-Augmented Generation (RAG) architecture, explains why Anyscale is effective for building RAG systems, and offers practical guidance for implementation.

## Why use RAG[​](#why-use-rag "Direct link to Why use RAG")

RAG provides the following benefits:

* **Reduced hallucinations**: RAG grounds answers in verifiable, up-to-date data, including proprietary internal documents that can't be shared for model training due to privacy or regulatory constraints.
* **Transparent sourcing**: Well-designed RAG systems provide citations, allowing you to verify exactly where information came from.
* **Graceful fallbacks**: A properly implemented RAG system informs you when it can't find relevant sources, effectively flagging potential hallucinations.
* **No retraining needed**: Add new documents to your RAG system through data ingestion, and your system can immediately answer questions about this new information.

## RAG architecture[​](#architecture "Direct link to RAG architecture")

Retrieval-augmented generation (RAG) combines an information retriever with a language model to answer questions using both pre-trained knowledge and external data. A RAG pipeline takes a user request, retrieves relevant content from a knowledge base, and feeds it to a language model to produce a grounded response.

### Data ingestion pipeline[​](#data-ingestion "Direct link to Data ingestion pipeline")

The data ingestion pipeline includes the following steps:

1. Load various document formats (PDF, DOCX, PPTX, HTML, TXT).
2. Apply a text chunking strategy (fixed and recursive) to break down the text for further processing.
3. Embed the text chunks using an embedding model.
4. Store the embeddings in a vector database for document retrieval capabilities.

![RAG data ingestion pipeline showing document loading, chunking, embedding, and vector database storage](https://anyscale-public-materials.s3.us-west-2.amazonaws.com/llm-and-agent-docs/01-rag-data-ingestion.drawio.png)

High-quality preprocessing is critical; retrieval can't recover information that was never extracted or chunked poorly.

**Extraction and cleaning**: Convert PDFs, Word documents, HTML, and other formats to clean text. Use OCR models (for example, Tesseract, PaddleOCR-VL, or DeepSeek-OCR) for scanned documents, and preserve page numbers where helpful for citation. If possible, preserve essential layout structure (such as headings, lists, tables, and code blocks), as this helps improve the quality of a standard RAG pipeline.

**Structuring and metadata**: Parse titles, headings, paragraph boundaries, figure/table captions, and anchors. Attach metadata (title, section path, page, URL, timestamps, access tags). Good metadata improves retrieval and makes citations and audits trivial.

**Chunking**: Split documents into manageable pieces sized to your model and queries. Typical ranges are 300–500 tokens with 10–20% overlap. Prefer semantic/structural chunking (by section/paragraph/table) to avoid splitting concepts mid-thought. Consider adaptive chunking for long spanning elements such as tables, for example, keeping the table header with a small window of rows together in the chunk.

**Embedding models**: Check the [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) to find embedding models that provide strong retrieval quality; larger models with bigger embedding dimensions could improve quality at higher latency and price.

**Indexing and vector stores**: Store embeddings in systems that support approximate nearest-neighbor (ANN) search (for example, Pinecone, Weaviate, ChromaDB, FAISS, Milvus, pgvector/Postgres, Elasticsearch/OpenSearch k-NN). Store each chunk's vector alongside metadata such as document title, section, page, table ID, created/updated time, and access controls. Rich metadata enables filtering, ranking, and auditability.

### Retrieval and generation pipeline[​](#retrieval-generation "Direct link to Retrieval and generation pipeline")

The retrieval and generation pipeline showcases embedding generation, vector search, context-aware prompting, and LLM streaming response delivery—all in a single executable pipeline.

![RAG retrieval and generation pipeline showing query embedding, vector search, context assembly, and LLM generation](https://anyscale-public-materials.s3.us-west-2.amazonaws.com/llm-and-agent-docs/04-rag-user-query-pipeline.drawio.png)

**User request**: The system receives a natural-language question (optionally with filters such as time range or source).

**Embedding and search**: An embedding model encodes the user request into a dense vector. The system compares this vector against pre-computed document embeddings in a vector store. Many systems combine dense retrieval with lexical signals such as BM25 (hybrid search) to improve recall. Advanced techniques include reranking candidates with LLMs or specialized models to improve precision, and applying metadata filtering to support exact-match lookups such as dates, IDs, or categories.

**Context assembly**: A bounded set of top-ranked chunks plus helpful metadata (title, section headers, source URL, page numbers) are composed into context. Deduplicate near-duplicates, enforce domain/recency filters, and budget tokens so the most on-topic evidence is included.

**Generation**: An LLM receives the original user request and the assembled context and produces an answer that cites or otherwise references the retrieved information (for example, document name with page number or URL). Carefully select the LLM and tune the prompt for the best performance.

## Next steps[​](#next-steps "Direct link to Next steps")

* Get started with RAG on Anyscale. See [RAG quickstart on Anyscale](/rag/quickstart.md).
* Improve RAG quality. See [RAG quality improvement strategies](/rag/quality-improvement.md).
* Improve production scalability. See [Scale RAG for production](/rag/production-scalability.md).
* Evaluate RAG performance. See [RAG evaluation](/rag/evaluation.md).
