# Source: https://io.net/docs/reference/rag/retrieval/semantic-search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Search R2R

> The R2R Search Endpoint provides semantic, hybrid, and graph-enhanced retrieval across documents and chunks. It supports advanced filters, hybrid ranking, and knowledge graph traversal to deliver contextually relevant and explainable results.

The **Search** endpoint provides advanced retrieval capabilities across documents, chunks, and knowledge graphs within R2R.

It supports multiple **search modes**, **hybrid vector and keyword retrieval**, **graph-enhanced search**, and **metadata-based filtering**, enabling powerful and flexible information discovery for semantic, contextual, and RAG-driven applications.

This endpoint is designed for both simple semantic lookups and complex, structured search workflows that combine multiple retrieval strategies.

### **Search Modes**

The `search_mode` field determines the level of control and type of retrieval performed.

| **Mode**   | **Description**                                                                                                     |
| :--------- | :------------------------------------------------------------------------------------------------------------------ |
| `basic`    | Performs a standard **semantic search** using vector embeddings. Ideal for quick and simple retrievals.             |
| `advanced` | Combines **semantic search** with **full-text search** for broader and more comprehensive results.                  |
| `custom`   | Grants full control via a `SearchSettings` object, allowing fine-tuned configurations for specialized applications. |

### **Filters**

Filters can be used to restrict search results by document attributes or metadata. Apply filters directly inside `search_settings.filters.`

**Supported operators:**

`$eq`, `$neq`, `$gt`, `$gte`, `$lt`, `$lte`, `$like`, `$ilike`, `$in`, `$nin`.

**Example:**

```json  theme={null}
{
	"filters": {
		"document_id": {"$eq": "e43864f5-a36f-548e-aacd-6f8d48b30c7f"}
	}
}
```

**Complex Filters Example:**

```json  theme={null}
{
  "filters": {
    "$and": [
      {"document_type": {"$eq": "report"}},
      {"metadata.topic": {"$ilike": "finance"}}
    ]
  }
}
```

### **Hybrid Search**

Hybrid search combines **semantic similarity** with **keyword-based retrieval**, improving result relevance by leveraging both vector embeddings and traditional text search.

Enable hybrid search by setting `use_hybrid_search`: `true` in `search_settings `and configure with `hybrid_settings` .

**Configuration Example:**

```json  theme={null}
{
	"use_hybrid_search": true,
	"hybrid_settings": {
    	"full_text_weight": 1.0,
    	"semantic_weight": 5.0,
    	"full_text_limit": 200,
    	"rrf_k": 50
	}
}
```

**Parameters:**

* `full_text_weight`: Adjusts the influence of keyword search.
* `semantic_weight`: Adjusts the influence of semantic similarity.
* `full_text_limit`: Limits keyword results before fusion.
* `rrf_k`: Rank fusion parameter controlling hybrid blending strength.

### **Graph-Enhanced Search**

The Search API supports **knowledge graph integration**, enabling entity- and relationship-aware retrieval.

This allows search results to include contextually related information based on graph traversal.

Knowledge graph integration is enabled by default. Configure it with `graph_search_settings` .

**Configuration Example:**

```json  theme={null}
{
	"graph_search_settings": {
    	"use_graph_search": true,
    	"kg_search_type": "local"
	}
}
```

**Parameters:**

* `use_graph_search`: Enables or disables graph integration.
* `kg_search_type`: Defines scope — `"local"` (collection-level) or `"global"` (across all graphs).


## OpenAPI

````yaml openapi/rag-retrieval/semantic-search.json post /api/r2r/v3/retrieval/search
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/retrieval/search:
    post:
      summary: Search R2R
      description: Perform a search query against vector and/or graph-based databases.
      operationId: semantic-search
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                query:
                  type: string
                  description: The search query text
                search_mode:
                  type: string
                  description: >-
                    Default value of custom allows full control over search
                    settings.  Pre-configured search modes: basic: A simple
                    semantic-based search. advanced: A more powerful hybrid
                    search combining semantic and full-text. custom: Full
                    control via search_settings.  If filters or limit are
                    provided alongside basic or advanced, they will override the
                    default settings for that mode.ID of the collection to
                    search in
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
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      chunk_search_results:
                        - id: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                          document_id: 3e157b3a-8469-51db-90d9-52e7d896b49b
                          collection_ids:
                            - collection_ids
                          text: Example text from the document
                          metadata:
                            associated_query: What is the capital of France?
                            title: example_document.pdf
                          owner_id: 2acb499e-8428-543b-bd85-0d9098718220
                          score: 0.23943702876567796
                      graph_search_results:
                        - content:
                            id: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                            name: Entity Name
                            description: Entity Description
                            metadata:
                              key: value
                          id: id
                          result_type: entity
                          chunk_ids:
                            - c68dc72e-fc23-5452-8f49-d7bd46088a96
                          metadata:
                            associated_query: What is the capital of France?
                      web_search_results:
                        - position: 1
                          id: id
                          title: Page Title
                          link: https://example.com/page
                          snippet: Page snippet
                          date: '2021-01-01'
                          sitelinks:
                            - link: https://example.com/sitelink
                              title: Sitelink Title
                      document_search_results:
                        - id: id
                          collection_ids:
                            - collection_ids
                          owner_id: owner_id
                          document_type: mp3
                          metadata:
                            key: value
                          version: version
              schema:
                type: object
                properties:
                  results:
                    type: object
                    properties:
                      chunk_search_results:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                              example: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                            document_id:
                              type: string
                              example: 3e157b3a-8469-51db-90d9-52e7d896b49b
                            collection_ids:
                              type: array
                              items:
                                type: string
                                example: collection_ids
                            text:
                              type: string
                              example: Example text from the document
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
                      graph_search_results:
                        type: array
                        items:
                          type: object
                          properties:
                            content:
                              type: object
                              properties:
                                id:
                                  type: string
                                  example: 3f3d47f3-8baf-58eb-8bc2-0171fb1c6e09
                                name:
                                  type: string
                                  example: Entity Name
                                description:
                                  type: string
                                  example: Entity Description
                                metadata:
                                  type: object
                                  properties:
                                    key:
                                      type: string
                                      example: value
                            id:
                              type: string
                              example: id
                            result_type:
                              type: string
                              example: entity
                            chunk_ids:
                              type: array
                              items:
                                type: string
                                example: c68dc72e-fc23-5452-8f49-d7bd46088a96
                            metadata:
                              type: object
                              properties:
                                associated_query:
                                  type: string
                                  example: What is the capital of France?
                      web_search_results:
                        type: array
                        items:
                          type: object
                          properties:
                            position:
                              type: integer
                              example: 1
                              default: 0
                            id:
                              type: string
                              example: id
                            title:
                              type: string
                              example: Page Title
                            link:
                              type: string
                              example: https://example.com/page
                            snippet:
                              type: string
                              example: Page snippet
                            date:
                              type: string
                              example: '2021-01-01'
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
                      document_search_results:
                        type: array
                        items:
                          type: object
                          properties:
                            id:
                              type: string
                              example: id
                            collection_ids:
                              type: array
                              items:
                                type: string
                                example: collection_ids
                            owner_id:
                              type: string
                              example: owner_id
                            document_type:
                              type: string
                              example: mp3
                            metadata:
                              type: object
                              properties:
                                key:
                                  type: string
                                  example: value
                            version:
                              type: string
                              example: version
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