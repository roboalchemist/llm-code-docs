# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/search_records.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Search with text

> Search a namespace with a query text, query vector, or record ID and return the most similar records, along with their similarity scores. Optionally, rerank the initial results based on their relevance to the query. 

Searching with text is supported only for indexes with [integrated embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding). Searching with a query vector or record ID is supported for all indexes. 

For guidance and examples, see [Search](https://docs.pinecone.io/guides/search/search-overview).

<RequestExample>
  ```shell curl theme={null}
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Search with a query text and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "query": {
              "inputs": {"text": "Disease prevention"},
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a query vector and rerank the results
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "query": {
              "vector": {
                  "values": [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
              },
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"] # Specified field must also be included in 'fields'
          }
       }'

  # Search with a record ID and rerank the results
  # Supported only for indexes with integrated embedding
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/search" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{
          "query": {
              "id": "rec1",
              "top_k": 4,
          },
          "fields": ["category", "chunk_text"]
          "rerank": {
              "query": "Disease prevention",
              "model": "bge-reranker-v2-m3",
              "top_n": 2,
              "rank_fields": ["chunk_text"]
          }
       }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
      "result": {
          "hits": [
              {
                  "_id": "rec3",
                  "_score": 0.004433765076100826,
                  "fields": {
                      "category": "immune system",
                      "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases."
                  }
              },
              {
                  "_id": "rec4",
                  "_score": 0.0029121784027665854,
                  "fields": {
                      "category": "endocrine system",
                      "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes."
                  }
              }
          ]
      },
      "usage": {
          "embed_total_tokens": 8,
          "read_units": 6,
          "rerank_units": 1
      }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /records/namespaces/{namespace}/search
openapi: 3.0.3
info:
  title: Pinecone Data Plane API
  description: >-
    Pinecone is a vector database that makes it easy to search and retrieve
    billions of high-dimensional vectors.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://{index_host}
    variables:
      index_host:
        default: unknown
        description: host of the index
security:
  - ApiKeyAuth: []
tags:
  - name: Vector Operations
  - name: Bulk Operations
  - name: Namespace Operations
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /records/namespaces/{namespace}/search:
    post:
      tags:
        - Vector Operations
      summary: Search with text
      description: >-
        Search a namespace with a query text, query vector, or record ID and
        return the most similar records, along with their similarity scores.
        Optionally, rerank the initial results based on their relevance to the
        query. 


        Searching with text is supported only for indexes with [integrated
        embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding).
        Searching with a query vector or record ID is supported for all
        indexes. 


        For guidance and examples, see
        [Search](https://docs.pinecone.io/guides/search/search-overview).
      operationId: searchRecordsNamespace
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: namespace
          description: The namespace to search.
          required: true
          schema:
            type: string
          style: simple
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SearchRecordsRequest'
        required: true
      responses:
        '200':
          description: A successful search namespace response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SearchRecordsResponse'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        4XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
        5XX:
          description: An unexpected error response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/rpcStatus'
components:
  schemas:
    SearchRecordsRequest:
      example:
        fields:
          - chunk_text
        query:
          inputs:
            text: your query text
          top_k: 10
      description: A search request for records in a specific namespace.
      type: object
      properties:
        query:
          description: .
          type: object
          properties:
            top_k:
              example: 10
              description: The number of similar records to return.
              type: integer
              format: int32
            filter:
              description: >-
                The filter to apply. You can use vector metadata to limit your
                search. See [Understanding
                metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).
              type: object
            inputs:
              $ref: '#/components/schemas/EmbedInputs'
            vector:
              $ref: '#/components/schemas/SearchRecordsVector'
            id:
              example: example-vector-1
              description: The unique ID of the vector to be used as a query vector.
              type: string
              maxLength: 512
            match_terms:
              $ref: '#/components/schemas/SearchMatchTerms'
          required:
            - top_k
        fields:
          example:
            - chunk_text
          description: >-
            The fields to return in the search results. If not specified, the
            response will include all fields.
          type: array
          items:
            type: string
          maxLength: 100
        rerank:
          description: Parameters for reranking the initial search results.
          type: object
          properties:
            model:
              example: bge-reranker-v2-m3
              description: >-
                The name of the [reranking
                model](https://docs.pinecone.io/guides/search/rerank-results#reranking-models)
                to use.
              type: string
            rank_fields:
              example:
                - chunk_text
                - title
              description: >
                The field(s) to consider for reranking. If not provided, the
                default is `["text"]`.


                The number of fields supported is
                [model-specific](https://docs.pinecone.io/guides/search/rerank-results#reranking-models).
              type: array
              items:
                type: string
            top_n:
              example: 5
              description: >-
                The number of top results to return after reranking. Defaults to
                top_k.
              type: integer
              format: int32
            parameters:
              example:
                truncate: END
              description: >-
                Additional model-specific parameters. Refer to the [model
                guide](https://docs.pinecone.io/guides/search/rerank-results#reranking-models)
                for available model parameters.
              type: object
              additionalProperties: true
            query:
              example: What is the capital of France?
              description: >-
                The query to rerank documents against. If a specific rerank
                query is specified,  it overwrites the query input that was
                provided at the top level.
              type: string
          required:
            - model
            - rank_fields
      required:
        - query
    SearchRecordsResponse:
      example:
        result:
          hits:
            - _id: example-record-1
              _score: 0.9281134605407715
              fields:
                data: your example text
        usage:
          embed_total_tokens: 10
          read_units: 5
      description: The records search response.
      type: object
      properties:
        result:
          type: object
          properties:
            hits:
              description: The hits for the search document request.
              type: array
              items:
                $ref: '#/components/schemas/Hit'
          required:
            - hits
        usage:
          $ref: '#/components/schemas/SearchUsage'
      required:
        - usage
        - result
    rpcStatus:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/protobufAny'
    EmbedInputs:
      example:
        text: chunk_text
      type: object
    SearchRecordsVector:
      type: object
      properties:
        values:
          $ref: '#/components/schemas/VectorValues'
        sparse_values:
          example:
            - 0.1
            - 0.2
            - 0.3
          description: The sparse embedding values.
          type: array
          items:
            type: number
            format: float
        sparse_indices:
          example:
            - 10
            - 3
            - 156
          description: The sparse embedding indices.
          type: array
          items:
            type: integer
            format: int32
            minimum: 0
    SearchMatchTerms:
      example:
        strategy: all
        terms:
          - animal
          - CHARACTER
          - donald Duck
      description: >-
        Specifies which terms must be present in the text of each search hit
        based on the specified strategy. The match is performed

        against the text field specified in the integrated index `field_map`
        configuration.


        Terms are normalized and tokenized into single tokens before matching,
        and order does not matter.


        Example:

          `"match_terms": {"terms": ["animal", "CHARACTER", "donald Duck"], "strategy": "all"}` will tokenize
          to `["animal", "character", "donald", "duck"]`, and would match
          `"Donald F. Duck is a funny animal character"` but would not match `"A duck is a funny animal"`.

        Match terms filtering is supported only for sparse indexes with
        [integrated
        embedding](https://docs.pinecone.io/guides/index-data/indexing-overview#vector-embedding)

        configured to use the
        [pinecone-sparse-english-v0](https://docs.pinecone.io/models/pinecone-sparse-english-v0)
        model.
      type: object
      properties:
        strategy:
          description: >-
            The strategy for matching terms in the text. Currently, only `all`
            is supported, which means all specified terms must be present.
          x-enum:
            - all
          type: string
        terms:
          description: >-
            A list of terms that must be present in the text of each search hit
            based on the specified strategy.
          type: array
          items:
            type: string
    Hit:
      example:
        _id: example-record-1
        _score: 0.9281134605407715
        fields:
          data: your example text
          more_data:
            text: your example text
      description: A record whose vector values are similar to the provided search query.
      type: object
      properties:
        _id:
          description: The record id of the search hit.
          type: string
        _score:
          description: The similarity score of the returned record.
          type: number
          format: float
        fields:
          description: The selected record fields associated with the search hit.
          type: object
      required:
        - _id
        - _score
        - fields
    SearchUsage:
      type: object
      properties:
        read_units:
          example: 5
          description: The number of read units consumed by this operation.
          type: integer
          format: int32
          minimum: 0
        embed_total_tokens:
          example: 2
          description: The number of embedding tokens consumed by this operation.
          type: integer
          format: int32
          minimum: 0
        rerank_units:
          example: 1
          description: The number of rerank units consumed by this operation.
          type: integer
          format: int32
          minimum: 0
      required:
        - read_units
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte
    VectorValues:
      description: This is the vector data included in the request.
      type: array
      items:
        type: number
        format: float
      minLength: 1
      maxLength: 20000
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````