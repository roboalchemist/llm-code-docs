# Source: https://docs.anyscale.com/rag/quality-improvement/data-ingestion-strategies.md

# Data ingestion strategies: building a quality foundation

[View Markdown](/rag/quality-improvement/data-ingestion-strategies.md)

# Data ingestion strategies: building a quality foundation

This page provides strategies to improve RAG data ingestion quality. It covers five common data ingestion challenges: missing or inaccurate content, OCR and layout issues, suboptimal chunking, semantic mismatch between queries and documents, and schema drift in structured data sources.

For an overview of common RAG challenges, see [Common RAG challenges](/rag/quality-improvement.md#common-challenges).

## Missing, inaccurate, or stale content[​](#missing-content "Direct link to Missing, inaccurate, or stale content")

The best retrieval system can't find information that's missing or is wrong.

**Strategies:**

* **Comprehensive data curation**: Actively curate your knowledge sources. Use domain experts to identify and validate the most relevant, high-quality documents.
* **Rigorous quality control**: Implement automated scripts to clean data (such as fixing formatting or removing errors) before you index it.
* **Human-in-the-loop (HITL) validation**: Integrate human experts into your pipeline to spot subtle inaccuracies and knowledge gaps that automated systems miss.
* **Automated update pipelines**: Build robust data pipelines to regularly refresh and re-index content, especially for time-sensitive domains.

## Poor OCR or challenging layouts[​](#ocr-layouts "Direct link to Poor OCR or challenging layouts")

Scanned PDFs, multi-column layouts, tables, and complex formatting can corrupt text extraction. OCR often produces semi-structured data (such as tables, forms, and key-value pairs) embedded within unstructured text. If your ingestion step produces garbled, out-of-order, or incomplete text, retrieval quality collapses regardless of downstream techniques.

note

This section focuses on semi-structured data extracted from raw documents using OCR. For strategies on integrating natively structured data sources such as databases, CSVs, and spreadsheets with RAG, see [Integrating RAG with structured data](/rag/structured-data.md).

**Strategies:**

* **Use native text extraction**: Use PDF/text parsers to read embedded text when available, and fall back to OCR only for scanned pages.
* **Preprocess images for OCR**: Improve OCR fidelity with deskewing, denoising, deblurring, binarization, and contrast enhancement.
* **Use layout-aware and reading-order-aware OCR**: Use advanced open-source OCR models such as PaddleOCR-VL or DeepSeek-OCR, or cloud provider solutions such as Azure AI Document Intelligence, Amazon Textract, or Google Enterprise OCR for scanned documents. Preserve blocks, columns, headings, lists, footnotes, and reading order. Export structured formats (such as Markdown) rather than a single flat text blob.
* **Extract tables and forms structurally**: Detect tables and forms, recover headers, rows, and columns, and serialize to CSV or Markdown tables. This creates semi-structured data from unstructured documents. Store key fields (such as IDs, dates, and totals) as metadata for precise filtering.
* **Preserve structure in the index**: Keep both a flattened text field for embedding and a rendered/structured field for display. Attach metadata such as page number, section heading, and table cell coordinates. When chunking, keep the metadata along with the rows. For example, append the table header to each table chunk that contains 10 rows. This ensures semi-structured data from OCR retains its context.
* **Chunk on structure boundaries**: Create chunks at paragraph, section, and table boundaries instead of page boundaries, because some tables span multiple pages.
* **Quality checks and sampling**: Sample pages per document type to audit OCR output. Track simple quality signals (such as OCR confidence or character error rate) and route low-quality pages for correction or re-scan.
* **Filter low-confidence content**: Exclude pages with very low OCR confidence from the index to avoid adding noise.

## Suboptimal chunking[​](#chunking "Direct link to Suboptimal chunking")

Arbitrarily splitting documents (such as "every 300-500 tokens") is a primary source of RAG failure. Arbitrary splits can sever semantic context, making chunks meaningless, or create chunks with too much noise, diluting their vector representation.

**Strategies:**

* **Recursive character splitting**: This method splits text on logical separators in a prioritized order (such as paragraphs, then sentences, then words).
* **Semantic chunking**: This technique splits a document based on semantic meaning. It segments the text where the topic shifts, creating thematically cohesive chunks. This leads to more precise embeddings and better retrieval.
* **Parent-child retrieval**: This strategy provides both retrieval precision and generation context. You index small, granular "child" chunks (such as single sentences) for search, but you also store the larger "parent" chunk they came from (such as the full paragraph or section). You search over the child chunks, but retrieve the corresponding parent chunks to give the LLM full context.

## Semantic mismatch[​](#semantic-mismatch "Direct link to Semantic mismatch")

Your embedding model must understand your domain's unique language. A generic model trained on the internet won't know that, in your company, "Project Titan" and "the Q4 initiative" refer to the same thing.

**Strategies:**

* **Embedding model selection**: Start by choosing a top-performing base embedding model from a public benchmark (such as the MTEB leaderboard).
* **Fine-tune the embedding model**: Fine-tune a pre-trained embedding model on your own domain-specific data. This teaches the model what "similarity" means in your specific context, dramatically improving retrieval relevance. If you lack a labeled (query, document) dataset, use a capable open-source LLM to synthetically generate relevant, high-quality questions for each of your document chunks. This creates the (query, positive\_document) pairs needed for training. If you're consistently getting low precision or recall despite trying other techniques, fine-tuning can significantly improve performance. Train the model on your actual user queries and their relevant documents using contrastive learning objectives such as MultipleNegativesRankingLoss. This helps the model distinguish between truly relevant and superficially similar documents in your specific domain.
* **Use alternative retrieval techniques**: If you can't change the embedding model, use retrieval strategies such as query rewriting, hybrid search, and reranking to compensate for semantic mismatch. See [Retrieval strategies: Finding the right information](/rag/quality-improvement/retrieval-strategies.md) for details.

## Schema drift and poor serialization[​](#schema-drift "Direct link to Schema drift and poor serialization")

Schema drift and poor serialization also affect semi-structured data extracted with OCR, such as tables, forms, and key-value pairs. Headers can shift, columns get merged or split, multi-line cells are truncated, and structural cues (such as row/column indices or cell coordinates) are lost. These issues produce ambiguous text and degrade retrieval quality. For techniques to integrate natively structured sources (such as databases and CSVs), see [Integrating RAG with structured data](/rag/structured-data.md).

**Strategies:**

* **Validate and normalize layouts**: Before ingestion, validate detected tables and forms. Check for required headers, consistent column counts per row, expected value types, and allowed ranges. Trigger alerts and human review when the extracted structure violates these rules.
* **Preserve headers and keys during serialization**: When converting OCR output to text, for key-value pairs, include the header with each row and keep key names with values. Instead of "John, Engineer, 2020", serialize as "Name: John, Role: Engineer, Start year: 2020". This prevents ambiguity and helps the LLM interpret each value. For tables, include the header row with every chunk that contains table rows.
* **Store structured metadata alongside text**: Keep structural metadata in your index, such as `page`, `table_id`, `row_index`, `col_index`, and bounding boxes (`x1,y1,x2,y2`). Also store queryable fields (such as IDs, dates, and totals) to enable precise metadata filtering with hybrid search.
* **Use consistent delimiters and formatting**: When flattening semi-structured data, use consistent, unambiguous delimiters (such as " | " between columns and " :: " between key-value pairs), and escape delimiters that appear in values. Prefer stable serializations such as CSV or Markdown tables and standardize these formats across your knowledge base.
