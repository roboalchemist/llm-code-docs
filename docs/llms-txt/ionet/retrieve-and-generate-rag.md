# Source: https://io.net/docs/reference/rag/retrieval/retrieve-and-generate-rag.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# RAG Query

> The R2R RAG Query endpoint performs Retrieval-Augmented Generation by combining semantic search, graph-enhanced context, and LLM generation. It supports streaming, source citation, and multiple model providers for contextually accurate AI responses.

The **RAG Query endpoint** executes a **Retrieval-Augmented Generation (RAG)** workflow by combining semantic search, optional knowledge graph integration, and large language model (LLM) generation.

It returns **contextually grounded, source-cited responses** derived from your document corpus and external web content (if enabled).

This endpoint is ideal for applications that require **explainable AI answers**, **document-grounded responses**, and **real-time contextual reasoning**.

### Key Features

* **Combined retrieval and generation**: Merges vector search, optional graph traversal, and LLM output generation in one request.
* **Automatic source citation**: Each referenced document includes a unique citation identifier.
* **Streaming and non-streaming modes**: Supports token-level updates or full-response delivery.
* **Provider flexibility**: Compatible with OpenAI, Anthropic, Ollama, and other LiteLLM-supported models.
* **Web search integration**: Optionally augments internal context with real-time external data.

### Model Support

| **Provider**  | **Description**                                                               |
| :------------ | :---------------------------------------------------------------------------- |
| **OpenAI**    | Default provider supporting GPT-based models (`gpt-4o`, `gpt-4o-mini`, etc.). |
| **Anthropic** | Supports Claude models (requires `ANTHROPIC_API_KEY`).                        |
| **Ollama**    | Enables local model execution via Ollama runtime.                             |
| **LiteLLM**   | Provides access to additional supported model providers.                      |

### Request Body

The request body combines **search configuration** (for retrieval) and **generation configuration** (for LLM behavior).\
All search parameters available in the `/search` endpoint can be reused here, including **filters**, **hybrid search**, and **graph-enhanced retrieval**.

### **Generation Configuration**

Control model behavior using the `rag_generation_config` object.

**Example:**

```json  theme={null}
{
    "model": "openai/gpt-4o-mini",
    "temperature": 0.7,
    "max_tokens": 1500,
    "stream": true
}
```

**Parameters:**

* `model`: Specifies the model used for generation.
* `temperature`: Controls output randomness (0 for deterministic, 1 for creative).
* `max_tokens`: Sets maximum output length.
* `stream`: Enables or disables token streaming for real-time responses.

### Streaming Responses

When `stream: true` is enabled, the API emits **Server-Sent Events (SSE)** during processing.\
Each event type corresponds to a distinct phase of the retrieval and generation workflow.

| **Event Type**   | **Description**                                                      |
| :--------------- | :------------------------------------------------------------------- |
| `search_results` | Contains the initial search results from your documents.             |
| `message`        | Streams partial tokens as the model generates them.                  |
| `citation`       | Emits citation metadata when a source is referenced.                 |
| `final_answer`   | Contains the complete, generated response with structured citations. |

**Example Response:**

```json  theme={null}
{
	"generated_answer": "DeepSeek-R1 is a model that demonstrates impressive performance...[1]",
	"search_results": { ... },
	"citations": [
    	{
        	"id": "cit.123456",
        	"object": "citation",
        	"payload": { ... }
    }
]
}
```


## OpenAPI

````yaml openapi/rag-retrieval/retrieve-and-generate-rag.json post /api/r2r/v3/retrieval/rag
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/retrieval/rag:
    post:
      summary: RAG Query
      description: Execute a RAG (Retrieval-Augmented Generation) query.
      operationId: retrieve-and-generate-rag
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: The user's question
                search_mode:
                  type: string
                  description: >-
                    Default value of custom allows full control over search
                    settings.  Pre-configured search modes: basic: A simple
                    semantic-based search. advanced: A more powerful hybrid
                    search combining semantic and full-text. custom: Full
                    control via search_settings.  If filters or limit are
                    provided alongside basic or advanced, they will override the
                    default settings for that mode.
                  default: custom
                  enum:
                    - basic
                    - advanced
                    - custom
                search_settings:
                  type: object
                  description: >-
                    The search configuration object. If search_mode is custom,
                    these settings are used as-is. For basic or advanced, these
                    settings will override the default mode configuration. 
                    Common overrides include filters to narrow results and limit
                    to control how many results are returned.
                  properties:
                    use_hybrid_search:
                      type: boolean
                      description: >-
                        Whether to perform a hybrid search. This is equivalent
                        to setting use_semantic_search=True and
                        use_fulltext_search=True, e.g. combining vector and
                        keyword search.
                      default: false
                    use_semantic_search:
                      type: boolean
                      description: Whether to use semantic search
                      default: true
                    use_fulltext_search:
                      type: boolean
                      description: Whether to use full-text search
                      default: false
                    filters:
                      type: string
                      description: >-
                        Filters to apply to the search. Allowed operators
                        include eq, neq, gt, gte, lt, lte, like, ilike, in, and
                        nin.  Commonly seen filters include operations include
                        the following:  {"document_id": {"$eq":
                        "9fbe403b-..."}}  {"document_id": {"$in":
                        ["9fbe403b-...", "3e157b3a-..."]}}  {"collection_ids":
                        {"$overlap": ["122fdf6a-...", "..."]}}  {"$and":
                        {"$document_id": ..., "collection_ids": ...}}
                    limit:
                      type: integer
                      description: Maximum number of results to return. >=1 <=1000
                      default: 10
                      format: int32
                    offset:
                      type: string
                      description: Offset to paginate search results
                      default: '0'
                    include_metadatas:
                      type: boolean
                      description: >-
                        Whether to include element metadata in the search
                        results
                      default: true
                    include_scores:
                      type: boolean
                      description: >-
                        Whether to include search score values in the search
                        results
                      default: true
                    search_strategy:
                      type: string
                      description: >-
                        Search strategy to use (e.g., ‘vanilla’, ‘query_fusion’,
                        ‘hyde’)
                      default: vanilla
                    hybrid_settings:
                      type: object
                      description: >-
                        Settings for hybrid search (only used if
                        use_semantic_search and use_fulltext_search are both
                        true)
                      properties:
                        full_text_weight:
                          type: number
                          description: Weight to apply to full text search
                          default: 1
                          format: double
                        semantic_weight:
                          type: number
                          description: Weight to apply to semantic search
                          default: 5
                          format: double
                        full_text_limit:
                          type: integer
                          description: >-
                            Maximum number of results to return from full text
                            search
                          default: 200
                          format: int32
                        rrf_k:
                          type: integer
                          description: K-value for RRF (Rank Reciprocal Fusion)
                          default: 50
                          format: int32
                    chunk_settings:
                      type: object
                      description: Settings specific to chunk/vector search
                      properties:
                        index_measure:
                          type: string
                          description: The distance measure to use for indexing
                          enum:
                            - l2_distance
                            - max_inner_product
                            - cosine_distance
                            - l1_distance
                            - hamming_distance
                            - jaccard_distance
                        probes:
                          type: integer
                          description: >-
                            Number of ivfflat index lists to query. Higher
                            increases accuracy but decreases speed.
                          default: 10
                          format: int32
                        ef_search:
                          type: integer
                          description: >-
                            Size of the dynamic candidate list for HNSW index
                            search. Higher increases accuracy but decreases
                            speed.
                          default: 40
                          format: int32
                        enabled:
                          type: boolean
                          description: Whether to enable chunk search
                          default: true
                    graph_settings:
                      type: object
                      description: Settings specific to knowledge graph search
                      properties:
                        limits:
                          type: array
                        enabled:
                          type: boolean
                          description: Whether to enable graph search
                          default: true
                    num_sub_queries:
                      type: integer
                      description: >-
                        Number of sub-queries/hypothetical docs to generate when
                        using hyde or rag_fusion search strategies.
                      default: 5
                      format: int32
                rag_generation_config:
                  type: object
                  description: Configuration for RAG generation
                  properties:
                    model:
                      type: string
                    temperature:
                      type: number
                      format: double
                    top_p:
                      type: number
                      format: double
                    max_tokens_to_sample:
                      type: integer
                      format: int32
                    stream:
                      type: boolean
                    functions:
                      type: array
                    tools:
                      type: array
                    add_generation_kwargs:
                      type: array
                    api_base:
                      type: string
                    response_format:
                      type: array
                      items:
                        properties:
                          Base Model:
                            type: object
                        type: object
                    extended_thinking:
                      type: boolean
                      description: >-
                        Flag to enable extended thinking mode (for Anthropic
                        providers)
                      default: false
                    thinking_budget:
                      type: integer
                      description: >-
                        Token budget for internal reasoning when extended
                        thinking mode is enabled. Must be less than
                        max_tokens_to_sample.
                      format: int32
                    reasoning_effort:
                      type: string
                      description: >-
                        Effort level for internal reasoning when extended
                        thinking mode is enabled, low, medium, or high.Only
                        applicable to OpenAI providers.
                task_prompt:
                  type: string
                  description: Optional custom prompt to override default
                include_title_if_available:
                  type: boolean
                  description: Include document titles in responses when available
                  default: false
                include_web_search:
                  type: boolean
                  description: Include web search results provided to the LLM.
                  default: false
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    key: value
              schema:
                type: object
                properties:
                  key:
                    type: string
                    example: value
        '404':
          description: '404'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
        '422':
          description: '422'
          content:
            text/plain:
              examples:
                Result:
                  value: ''
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````