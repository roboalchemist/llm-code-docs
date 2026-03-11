# Source: https://docs.anyscale.com/rag/quality-improvement/generation-strategies.md

# Generation strategies: Ensuring accurate synthesis

[View Markdown](/rag/quality-improvement/generation-strategies.md)

# Generation strategies: Ensuring accurate synthesis

This page provides strategies for ensuring your LLM correctly uses retrieved context in RAG systems. It covers solutions for common generation failures: context overload, extraction format issues, hallucinations, and numerical reasoning errors.

For an overview of common RAG challenges, see [Common RAG challenges](/rag/quality-improvement.md#common-challenges).

## "Lost in the middle" and context overload[​](#lost-in-middle "Direct link to \"Lost in the middle\" and context overload")

LLMs have a finite context window and don't pay equal attention to all parts of it. Research shows many models have a U-shaped attention curve: they pay close attention to the beginning and end of the context, but often ignore information in the middle.

**Strategies:**

* **Context filtering and reordering**: Use the filtering or reranking strategies mentioned in [Low precision or recall (missed retrieval)](/rag/quality-improvement/retrieval-strategies.md#precision-recall). After reranking, strategically reorder the context you send to the LLM. Place the most relevant documents at the beginning.
* **Context compression**: Instead of passing full document chunks, use an LLM call to "compress" or "summarize" the retrieved content first. This can involve extracting only the most relevant sentences from each chunk or generating a concise summary of each. This filters out noise and fits more signal into the limited context window.

## "Missing the big picture"[​](#missing-big-picture "Direct link to \"Missing the big picture\"")

Retrieved chunks from semantic matching can be partial and miss important context. For example, financial information in text chunks might mention quarter names, but the year information appears only in the document title or header on the first page.

**Strategies:**

* **Include document metadata**: Add metadata such as document headers and section headers extracted during OCR processing. This preserves important context that might not appear in individual chunks. See [Poor OCR or challenging layouts](/rag/quality-improvement/data-ingestion-strategies.md#ocr-layouts) for strategies on preserving structure during OCR.
* **Leverage document and section summaries**: Use document summaries or section summaries to provide broader context alongside retrieved chunks. This helps the LLM understand the overall document structure and key themes.
* **Include schema information for semi-structured data**: For semi-structured data such as tables or key-value pairs extracted from OCR text, include schema information and headers with each chunk. This ensures the LLM understands the structure and relationships in the data. See [Poor OCR or challenging layouts](/rag/quality-improvement/data-ingestion-strategies.md#ocr-layouts) for strategies on preserving headers during OCR extraction. For natively structured data sources such as databases and CSVs, see [Integrating RAG with structured data](/rag/structured-data.md) for integration approaches.

## Hallucination and contradiction[​](#hallucination "Direct link to Hallucination and contradiction")

The system produces a response that's factually incorrect or illogical. This can happen when the context is weak, ambiguous, or contains conflicting information.

**Strategies:**

* **Grounding prompts**: Be strict in your instructions. Explicitly tell the LLM to only use the provided context and to state "I don't have enough information to answer" if the answer isn't present. Setting the generation temperature to a low value (such as 0) also reduces randomness.

* **Source verification and citations**: Design your system to cite its sources, linking each part of the answer back to the specific source chunk it came from. See the [Improve RAG with Prompt Engineering](https://console.anyscale.com/template-preview/e2e-rag-deepdive?file=%252Ffiles%252Fnotebooks%252F05_Improve_RAG_with_Prompt_Engineering.ipynb) notebook for how to do the citations.

* **Verification pipelines**: For high-stakes applications, add a second "verification agent." One LLM generates an answer, and a second, independent LLM agent checks that answer against the sources to ensure it's factually supported.

* **Contradiction handling**: When retrieved documents conflict, your system needs a clear strategy:

  <!-- -->

  1. **Acknowledge**: Have the LLM state the conflict to the user (for example, "Source A says X, but Source B says Y").
  2. **Prioritize**: Use metadata (such as recency or source authority) to automatically resolve the conflict.
  3. **Clarify**: In an interactive chat, ask the user a clarifying question to resolve the ambiguity.

## Numerical reasoning and aggregation errors[​](#numerical-errors "Direct link to Numerical reasoning and aggregation errors")

LLMs aren't calculators. They struggle with precise arithmetic, counting, aggregations (such as sums and averages), and multi-step numerical reasoning. When your RAG system retrieves tables or numerical data—whether from semi-structured data extracted via OCR or from natively structured data sources—expecting the LLM to compute totals, compare values, or perform statistical analysis often leads to incorrect results.

**Strategies:**

* **Delegate computation to external tools**: Instead of asking the LLM to compute results, use function calling or tool use to delegate numerical operations to Python code, SQL queries, or specialized APIs. The LLM's role becomes parsing the user's intent, generating the appropriate code or query, executing it in a sandbox, and presenting the result. This eliminates arithmetic errors entirely. For natively structured data sources, see [Integrating RAG with structured data](/rag/structured-data.md) for text-to-SQL and DataFrame agent approaches.
* **Structured output with computed fields**: When retrieving structured or semi-structured data, pre-compute aggregations and statistics at index time or query time. Store summary fields (such as total\_revenue, average\_rating, row\_count) as metadata. Retrieve these computed values instead of raw data, so the LLM only needs to read and present the result, not calculate it.
* **Generate and execute Python/SQL code**: For complex analytical questions (such as "What's the average order value for customers in California?"), use the LLM to generate Python code (with pandas) or SQL queries. Execute this code in a secure sandbox environment (such as Ray Data or a containerized Python runtime) against the retrieved data. Return the computed result to the LLM for final formatting and presentation. This combines the LLM's natural language understanding with the precision of programmatic computation. For detailed integration strategies, see [Integrating RAG with structured data](/rag/structured-data.md).
* **Break down multi-step reasoning**: For questions requiring multiple calculations, decompose the task into smaller steps. Have the LLM generate a plan (such as "Step 1: Filter by region. Step 2: Sum revenues. Step 3: Compare to threshold"). Execute each step as code, pass intermediate results to the next step, and let the LLM synthesize the final answer from verified computed values.
* **Use specialized models for math**: Consider using LLMs specifically fine-tuned for mathematical reasoning, or augment your general-purpose LLM with a math-specialized model for numerical questions. Route math-heavy queries to the specialized model.
* **Validate numerical outputs**: After generation, implement sanity checks on numerical results. For example, if the LLM claims "total revenue is $1.5M from 10,000 orders", verify that 1,500,000 / 10,000 equals the stated average. Flag or reject answers that fail basic consistency checks.

## Wrong format in final response[​](#wrong-format "Direct link to Wrong format in final response")

The answer is in the context, but the LLM fails to pull it out or returns it in an unusable format (such as a text paragraph when you need JSON).

**Strategies:**

* **Advanced prompt engineering**: Design prompts that define the assistant's scope and identity (for example, "You are an expert in \[domain], specializing in \[specific topics]"). Include explicit instructions to refuse off-topic requests and to cite sources when answering. Use Chain-of-Thought prompting by instructing the model to "explain your reasoning step-by-step." Request structured output with markdown formatting. For hands-on examples, see the [Improve RAG with Prompt Engineering](https://console.anyscale.com/template-preview/e2e-rag-deepdive?file=%252Ffiles%252Fnotebooks%252F05_Improve_RAG_with_Prompt_Engineering.ipynb) notebook.
* **Few-shot prompting**: Provide two to three high-quality examples of (input, desired\_output) pairs directly in the prompt. This is one of the most effective ways to guide the model to produce the exact tone, style, and structure you need.
* **Structured output (JSON mode)**: For machine-readable applications, use your LLM API's "tool calling," "function calling," or "JSON mode" feature. This forces the model's output to conform to a specified Pydantic class or JSON schema, completely eliminating formatting errors and fragile parsing logic. See [Configure structured output for LLMs](/llm/serving/structured-output.md).
