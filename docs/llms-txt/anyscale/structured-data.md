# Source: https://docs.anyscale.com/rag/structured-data.md

# Integrating RAG with structured data

[View Markdown](/rag/structured-data.md)

# Integrating RAG with structured data

This page provides strategies for integrating RAG with structured data sources such as databases, CSVs, and spreadsheets.

note

This page focuses on natively structured data sources. For strategies on handling semi-structured data extracted from raw documents using OCR (such as tables, forms, and key-value pairs embedded in PDFs or images), see [Poor OCR or challenging layouts](/rag/quality-improvement/data-ingestion-strategies.md#ocr-layouts).

## Understanding the challenge[​](#challenge "Direct link to Understanding the challenge")

While RAG excels with unstructured text, it traditionally struggles with structured data. Embedding models are designed for semantic similarity, not for the numeric precision and relational logic that structured data relies on. A naive RAG pipeline that embeds table rows as text will fail at any query requiring calculation, exact numeric matching, or an understanding of relational table structures.

## Enhancing retrieval for simple lookups[​](#structured-retrieval "Direct link to Enhancing retrieval for simple lookups")

For simpler "look-up" style queries, you can improve the retrieval step to be more "structure-aware" without needing complex agents.

**Strategies:**

* **Hybrid retrieval**: As discussed in the retrieval section, combining semantic (vector) search with keyword-based search is highly effective. For structured data, this is critical for ensuring exact matches for IDs, product codes, or specific dates that vector search might otherwise miss.
* **Data-to-text conversion**: Convert structured data into natural language before embedding it. Instead of indexing a raw CSV row, you "serialize" it into a human-readable sentence. For example, a row `[12345, 'Alice', '2023-09-01', 250.00, 'Shipped']` becomes "Order 12345, placed by Alice on 2023-09-01, totaled $250.00 and is currently 'Shipped'." This text can be embedded and retrieved by a standard RAG pipeline. For greater precision, you can store numeric or categorical fields (such as dates or IDs) as metadata, allowing a query to filter by metadata first and then use semantic search on the remaining text.

## Direct integration with agents and tool use[​](#agents-tool-use "Direct link to Direct integration with agents and tool use")

The most powerful approach is to compute or query for answers live instead of retrieving pre-written answers. This involves using the LLM as a reasoning engine to generate code that interacts with data sources.

**Strategies:**

* **Text-to-SQL**: Instead of embedding a database, provide the LLM with the database schema (table names, columns, data types). When a user asks a question such as "What were our total electronics sales in Q3 2023?", the LLM generates and executes a SQL query to get a precise, up-to-date answer directly from the database.
* **DataFrame agents**: This is a similar concept for local files such as CSVs or spreadsheets. The LLM is given access to a Python environment and the structure of a DataFrame (for example, using the pandas library). If a user asks "Which city has the highest population?", the LLM generates and executes Python code (such as `df['city'][df['population'].idxmax()]`) to find the answer.
* **Programmatic agents (tool use)**: Both Text-to-SQL and DataFrame agents are examples of a broader concept: tool use. A programmatic agent is an LLM given access to a suite of tools (such as a `query_db` tool, a `run_python_code` tool, or a calculator). Using a paradigm such as ReAct (Reason+Act), the LLM "thinks" about what it needs to do and then "acts" by calling the appropriate tool. A key challenge is security; executing LLM-generated code must be done in a sandboxed, controlled environment.

## Mitigating numerical errors[​](#numerical-errors "Direct link to Mitigating numerical errors")

Even when data is retrieved correctly, you must have strategies to ensure the LLM's final reasoning is numerically sound. For additional strategies on handling numerical reasoning errors in RAG generation, see [Numerical reasoning and aggregation errors](/rag/quality-improvement/generation-strategies.md#numerical-errors).
