# Source: https://io.net/docs/reference/rag/retrieval/agent-based-query-resolution.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# RAG-Powered Conversational Agent

> The R2R Agent endpoint provides a conversational RAG interface for retrieval, reasoning, and research. It supports multi-turn context, tool integration, streaming output, and both RAG and Research modes for dynamic AI-driven analysis.

The **RAG-powered Conversational Agent** enables interactive, multi-turn communication with an intelligent agent built on R2R’s Retrieval-Augmented Generation (RAG) system.

This endpoint allows users to engage in real-time dialogue with an AI capable of retrieving information from internal and external sources, reasoning through complex problems, executing computations, and maintaining context across multiple conversation turns.

It operates in two distinct modes: **RAG Mode** for knowledge-based responses and **Research Mode** for deep analytical reasoning.

## Operating Modes

### **RAG Mode (Default)**

Provides fast, grounded answers by combining retrieval and generation.

Features include:

* Semantic and hybrid search across documents and chunks
* Optional web search integration for live context
* Document-level and chunk-level content retrieval
* Source citation and evidence-based responses

## **Research Mode**

Extends RAG functionality with advanced reasoning and computational abilities.

Features include:

* Dedicated reasoning system for multi-step problem-solving
* Automated critique generation to identify biases or logical fallacies
* Python execution for quantitative analysis and code-based reasoning
* Deep exploration capabilities across multiple sources

## **Available Tools**

### **RAG Tools:**

* `search_file_knowledge` — Perform semantic or hybrid search across ingested documents.
* `search_file_descriptions` — Search file-level metadata and descriptions.
* `content` — Retrieve full documents or chunk structures.
* `web_search` — Query external search engines for up-to-date information.
* `web_scrape` — Extract content directly from specified web pages.

**Research Tools:**

* `rag` — Invoke the underlying RAG agent for information retrieval.
* `reasoning` — Use a dedicated reasoning model for deep analysis and logical inference.
* `critique` — Analyze the conversation for potential biases or reasoning flaws.
* `python_executor` — Execute Python code for computation, simulation, or data processing.

## **Streaming Output**

When streaming is enabled (`"stream": true`), the API emits **Server-Sent Events (SSE)** to deliver updates in real time.

Each event corresponds to a stage in the agent’s reasoning and response generation process.

| **Event Type** | **Description**                                                                          |
| :------------- | :--------------------------------------------------------------------------------------- |
| `thinking`     | Displays the model’s intermediate reasoning steps (enabled by `extended_thinking=true`). |
| `tool_call`    | Indicates when the agent invokes a tool.                                                 |
| `tool_result`  | Contains the output from an executed tool.                                               |
| `citation`     | Signals that a citation has been added to the response.                                  |
| `message`      | Streams partial tokens of the generated message.                                         |
| `final_answer` | Provides the complete generated response with structured citations.                      |

## **Conversations**

The agent maintains persistent conversational context using the `conversation_id` field.

**How it works:**

1. On the initial request, the system creates a new conversation and returns a `conversation_id`.
2. Include this ID in subsequent requests to continue the same thread.
3. If no conversation name exists, R2R automatically assigns one.

This design allows for **multi-turn, context-aware discussions**, where the agent can recall prior messages, reasoning, and results.


## OpenAPI

````yaml openapi/rag-retrieval/agent-based-query-resolution.json post /api/r2r/v3/retrieval/agent
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/retrieval/agent:
    post:
      summary: RAG-powered Conversational Agent
      description: >-
        Engage with an intelligent agent for information retrieval, analysis,
        and research.
      operationId: agent-based-query-resolution
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                Params:
                  type: object
                  description: Current message to process
                  required:
                    - role
                  properties:
                    role:
                      type: string
                      description: Or allowed string *
                      enum:
                        - system
                        - user
                        - assistant
                        - function
                        - tool
                    content:
                      type: string
                    name:
                      type: string
                    function_call:
                      type: array
                    tool_calls:
                      type: array
                    tool_call_id:
                      type: string
                    metadata:
                      type: array
                    structured_content:
                      type: array
                    image_url:
                      type: string
                    image_data:
                      type: array
                search_mode:
                  type: string
                  description: 'Pre-configured search modes: basic, advanced, or custom.'
                  enum:
                    - basic
                    - advanced
                    - custom
                search_settings:
                  type: object
                  description: The search configuration object for retrieving context.
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
                  description: Configuration for RAG generation in 'rag' mode
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
                research_generation_config:
                  type: object
                  description: >-
                    Configuration for generation in ‘research’ mode. If not
                    provided but mode=‘research’, rag_generation_config will be
                    used with appropriate model overrides.
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
                rag_tools:
                  type: string
                  description: >-
                    List of tools to enable for RAG mode. Available tools:
                    search_file_knowledge, get_file_content, web_search,
                    web_scrape, search_file_descriptions
                  enum:
                    - web_search
                    - web_scrape
                    - search_file_descriptions
                    - search_file_knowledge
                    - get_file_content
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      messages:
                        - role: assistant
                          content: |-
                            Aristotle (384–322 BC) was an Ancient
                                                    Greek philosopher and polymath whose contributions
                                                    have had a profound impact on various fields of
                                                    knowledge.
                                                    Here are some key points about his life and work:
                                                    

                            1. **Early Life**: Aristotle was born in 384 BC in
                                                    Stagira, Chalcidice, which is near modern-day
                                                    Thessaloniki, Greece. His father, Nicomachus, was the
                                                    personal physician to King Amyntas of Macedon, which
                                                    exposed Aristotle to medical and biological knowledge
                                                    from a young age [C].

                            2. **Education and Career**:
                                                    After the death of his parents, Aristotle was sent to
                                                    Athens to study at Plato's Academy, where he remained
                                                    for about 20 years. After Plato's death, Aristotle
                                                    left Athens and eventually became the tutor of
                                                    Alexander the Great [C].
                                                    

                            3. **Philosophical Contributions**: Aristotle
                                                    founded the Lyceum in Athens, where he established the
                                                    Peripatetic school of philosophy. His works cover a
                                                    wide range of subjects, including metaphysics, ethics,
                                                    politics, logic, biology, and aesthetics. His writings
                                                    laid the groundwork for many modern scientific and
                                                    philosophical inquiries [A].

                            4. **Legacy**:
                                                    Aristotle's influence extends beyond philosophy to the
                                                      natural sciences, linguistics, economics, and
                                                      psychology. His method of systematic observation and
                                                      analysis has been foundational to the development of
                                                      modern science [A].

                            Aristotle's comprehensive
                                                      approach to knowledge and his systematic methodology
                                                      have earned him a lasting legacy as one of the
                                                      greatest philosophers of all time.

                            Sources:
                                                      
                            - [A] Aristotle's broad range of writings and
                                                      influence on modern science.
                            - [C] Details about
                                                      Aristotle's early life and education.
                          metadata:
                            aggregated_search_results:
                              chunk_search_results:
                                - document_id: 3e157b3a-8469-51db-90d9-52e7d896b49b
                                  id: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                  metadata:
                                    associated_query: What is the capital of France?
                                    title: example_document.pdf
                                  owner_id: 2acb499e-8428-543b-bd85-0d9098718220
                                  score: 0.23943702876567796
                                  text: Example text from the document
                              document_search_results:
                                - document:
                                    chunks:
                                      - Chunk 1
                                      - Chunk 2
                                    id: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                    metadata: {}
                                    title: Document Title
                              graph_search_results:
                                - chunk_ids:
                                    - c68dc72e-fc23-5452-8f49-d7bd46088a96
                                  content:
                                    description: Entity Description
                                    id: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                    metadata: {}
                                    name: Entity Name
                                  metadata:
                                    associated_query: What is the capital of France?
                                  result_type: entity
                              web_search_results:
                                - date: '2021-01-01'
                                  link: https://example.com/page
                                  position: 1
                                  sitelinks:
                                    - link: https://example.com/sitelink
                                      title: Sitelink Title
                                  snippet: Page snippet
                                  title: Page Title
                            citations:
                              - collection_ids:
                                  - 122fdf6a-e116-546b-a8f6-e4cb2e2c0a09
                                document_id: |2-

                                                                      e43864f5-a36f-548e-aacd-6f8d48b30c7f
                                                                      
                                endIndex: 396
                                id: e760bb76-1c6e-52eb-910d-0ce5b567011b
                                index: 1
                                metadata:
                                  chunk_order: 68
                                  document_type: pdf
                                  license: CC-BY-4.0
                                  title: DeepSeek_R1.pdf
                                owner_id: |2-

                                                                      2acb499e-8428-543b-bd85-0d9098718220
                                                                      
                                rawIndex: 9
                                score: 0.64
                                snippetEndIndex: 418
                                snippetStartIndex: 320
                                sourceType: chunk
                                startIndex: 393
                                text: |2-

                                                                      Document Title: DeepSeek_R1.pdf
                                                                      

                                  Text: could achieve an accuracy of ...
                                                                      
                      conversation_id: a32b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      messages:
                        type: array
                        items:
                          type: object
                          properties:
                            role:
                              type: string
                              example: assistant
                            content:
                              type: string
                              example: >-
                                Aristotle (384–322 BC) was an Ancient
                                                        Greek philosopher and polymath whose contributions
                                                        have had a profound impact on various fields of
                                                        knowledge.
                                                        Here are some key points about his life and work:
                                                        

                                1. **Early Life**: Aristotle was born in 384 BC
                                in
                                                        Stagira, Chalcidice, which is near modern-day
                                                        Thessaloniki, Greece. His father, Nicomachus, was the
                                                        personal physician to King Amyntas of Macedon, which
                                                        exposed Aristotle to medical and biological knowledge
                                                        from a young age [C].

                                2. **Education and Career**:
                                                        After the death of his parents, Aristotle was sent to
                                                        Athens to study at Plato's Academy, where he remained
                                                        for about 20 years. After Plato's death, Aristotle
                                                        left Athens and eventually became the tutor of
                                                        Alexander the Great [C].
                                                        

                                3. **Philosophical Contributions**: Aristotle
                                                        founded the Lyceum in Athens, where he established the
                                                        Peripatetic school of philosophy. His works cover a
                                                        wide range of subjects, including metaphysics, ethics,
                                                        politics, logic, biology, and aesthetics. His writings
                                                        laid the groundwork for many modern scientific and
                                                        philosophical inquiries [A].

                                4. **Legacy**:
                                                        Aristotle's influence extends beyond philosophy to the
                                                          natural sciences, linguistics, economics, and
                                                          psychology. His method of systematic observation and
                                                          analysis has been foundational to the development of
                                                          modern science [A].

                                Aristotle's comprehensive
                                                          approach to knowledge and his systematic methodology
                                                          have earned him a lasting legacy as one of the
                                                          greatest philosophers of all time.

                                Sources:
                                                          
                                - [A] Aristotle's broad range of writings and
                                                          influence on modern science.
                                - [C] Details about
                                                          Aristotle's early life and education.
                            metadata:
                              type: object
                              properties:
                                aggregated_search_results:
                                  type: object
                                  properties:
                                    chunk_search_results:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          document_id:
                                            type: string
                                            example: 3e157b3a-8469-51db-90d9-52e7d896b49b
                                          id:
                                            type: string
                                            example: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                          metadata:
                                            type: object
                                            properties:
                                              associated_query:
                                                type: string
                                                example: What is the capital of France?
                                              title:
                                                type: string
                                                example: example_document.pdf
                                          owner_id:
                                            type: string
                                            example: 2acb499e-8428-543b-bd85-0d9098718220
                                          score:
                                            type: number
                                            example: 0.23943702876567796
                                            default: 0
                                          text:
                                            type: string
                                            example: Example text from the document
                                    document_search_results:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          document:
                                            type: object
                                            properties:
                                              chunks:
                                                type: array
                                                items:
                                                  type: string
                                                  example: Chunk 1
                                              id:
                                                type: string
                                                example: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                              metadata:
                                                type: object
                                                properties: {}
                                              title:
                                                type: string
                                                example: Document Title
                                    graph_search_results:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          chunk_ids:
                                            type: array
                                            items:
                                              type: string
                                              example: c68dc72e-fc23-5452-8f49-d7bd46088a96
                                          content:
                                            type: object
                                            properties:
                                              description:
                                                type: string
                                                example: Entity Description
                                              id:
                                                type: string
                                                example: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                              metadata:
                                                type: object
                                                properties: {}
                                              name:
                                                type: string
                                                example: Entity Name
                                          metadata:
                                            type: object
                                            properties:
                                              associated_query:
                                                type: string
                                                example: What is the capital of France?
                                          result_type:
                                            type: string
                                            example: entity
                                    web_search_results:
                                      type: array
                                      items:
                                        type: object
                                        properties:
                                          date:
                                            type: string
                                            example: '2021-01-01'
                                          link:
                                            type: string
                                            example: https://example.com/page
                                          position:
                                            type: integer
                                            example: 1
                                            default: 0
                                          sitelinks:
                                            type: array
                                            items:
                                              type: object
                                              properties:
                                                link:
                                                  type: string
                                                  example: https://example.com/sitelink
                                                title:
                                                  type: string
                                                  example: Sitelink Title
                                          snippet:
                                            type: string
                                            example: Page snippet
                                          title:
                                            type: string
                                            example: Page Title
                                citations:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      collection_ids:
                                        type: array
                                        items:
                                          type: string
                                          example: 122fdf6a-e116-546b-a8f6-e4cb2e2c0a09
                                      document_id:
                                        type: string
                                        example: |2-

                                                                              e43864f5-a36f-548e-aacd-6f8d48b30c7f
                                                                              
                                      endIndex:
                                        type: integer
                                        example: 396
                                        default: 0
                                      id:
                                        type: string
                                        example: e760bb76-1c6e-52eb-910d-0ce5b567011b
                                      index:
                                        type: integer
                                        example: 1
                                        default: 0
                                      metadata:
                                        type: object
                                        properties:
                                          chunk_order:
                                            type: integer
                                            example: 68
                                            default: 0
                                          document_type:
                                            type: string
                                            example: pdf
                                          license:
                                            type: string
                                            example: CC-BY-4.0
                                          title:
                                            type: string
                                            example: DeepSeek_R1.pdf
                                      owner_id:
                                        type: string
                                        example: |2-

                                                                              2acb499e-8428-543b-bd85-0d9098718220
                                                                              
                                      rawIndex:
                                        type: integer
                                        example: 9
                                        default: 0
                                      score:
                                        type: number
                                        example: 0.64
                                        default: 0
                                      snippetEndIndex:
                                        type: integer
                                        example: 418
                                        default: 0
                                      snippetStartIndex:
                                        type: integer
                                        example: 320
                                        default: 0
                                      sourceType:
                                        type: string
                                        example: chunk
                                      startIndex:
                                        type: integer
                                        example: 393
                                        default: 0
                                      text:
                                        type: string
                                        example: |2-

                                                                              Document Title: DeepSeek_R1.pdf
                                                                              

                                          Text: could achieve an accuracy of ...
                                                                              
                      conversation_id:
                        type: string
                        example: a32b4c5d-6e7f-8a9b-0c1d-2e3f4a5b6c7d
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
                  value: {}
              schema:
                type: object
                properties: {}
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````