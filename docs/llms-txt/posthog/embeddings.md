# Source: https://posthog.com/docs/llm-analytics/embeddings.md

# Embeddings - Docs

Embeddings are calls to embedding models that convert text into vector representations for semantic search, RAG (retrieval-augmented generation) pipelines, and similarity matching.

While [generations](/docs/llm-analytics/generations.md) track LLM conversations and [spans](/docs/llm-analytics/spans.md) track operations, embeddings specifically monitor vector generation:

-   **Search queries** - Converting user input for semantic search
-   **Document indexing** - Embedding content for retrieval
-   **RAG pipelines** - Query and document vectorization
-   **Batch processing** - Multiple embeddings in one call

For technical implementation details, see [manual capture](/docs/llm-analytics/installation/manual-capture.md).

## Event properties

An embedding is a single call to an embedding model to convert text into a vector representation.

**Event name**: `$ai_embedding`

### Core properties

| Property | Description |
| --- | --- |
| $ai_trace_id | The trace ID (a UUID to group related AI events together). Must contain only letters, numbers, and special characters: -, _, ~, ., @, (, ), !, ', :, \|Example: d9222e05-8708-41b8-98ea-d4a21849e761 |
| $ai_session_id | (Optional) Groups related traces together. Use this to organize traces by whatever grouping makes sense for your application (user sessions, workflows, conversations, or other logical boundaries).Example: session-abc-123, conv-user-456 |
| $ai_span_id | (Optional) Unique identifier for this embedding operation |
| $ai_span_name | (Optional) Name given to this embedding operationExample: embed_user_query, index_document |
| $ai_parent_id | (Optional) Parent span ID for tree-view grouping |
| $ai_model | The embedding model usedExample: text-embedding-3-small, text-embedding-ada-002 |
| $ai_provider | The LLM providerExample: openai, cohere, voyage |
| $ai_input | The text to embedExample: "Tell me a fun fact about hedgehogs" or array of strings for batch embeddings |
| $ai_input_tokens | The number of tokens in the input |
| $ai_latency | (Optional) The latency of the embedding call in seconds |
| $ai_http_status | (Optional) The HTTP status code of the response |
| $ai_base_url | (Optional) The base URL of the LLM providerExample: https://api.openai.com/v1 |
| $ai_request_url | (Optional) The full URL of the request made to the embedding APIExample: https://api.openai.com/v1/embeddings |
| $ai_is_error | (Optional) Boolean to indicate if the request was an error |
| $ai_error | (Optional) The error message or object if the embedding failed |

### Cost properties

Cost properties are optional as we can automatically calculate them from model and token counts. If you want, you can provide your own cost property instead.

| Property | Description |
| --- | --- |
| $ai_input_cost_usd | (Optional) Cost in USD for input tokens |
| $ai_output_cost_usd | (Optional) Cost in USD for output tokens (usually 0 for embeddings) |
| $ai_total_cost_usd | (Optional) Total cost in USD |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better