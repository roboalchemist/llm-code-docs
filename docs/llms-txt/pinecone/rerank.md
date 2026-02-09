# Source: https://docs.pinecone.io/reference/api/2025-10/inference/rerank.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Rerank results

> Rerank results according to their relevance to a query.

For guidance and examples, see [Rerank results](https://docs.pinecone.io/guides/search/rerank-results).

<RequestExample>
  ```shell curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"

  curl https://api.pinecone.io/rerank \
    -H "Content-Type: application/json" \
    -H "Accept: application/json" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -H "Api-Key: $PINECONE_API_KEY" \
  -d '{
    "model": "bge-reranker-v2-m3",
    "query": "The tech company Apple is known for its innovative products like the iPhone.",
    "return_documents": true,
    "top_n": 4,
    "documents": [
      {"id": "vec1", "text": "Apple is a popular fruit known for its sweetness and crisp texture."},
      {"id": "vec2", "text": "Many people enjoy eating apples as a healthy snack."},
      {"id": "vec3", "text": "Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."},
      {"id": "vec4", "text": "An apple a day keeps the doctor away, as the saying goes."}
    ],
    "parameters": {
      "truncate": "END"
    }
  }'
  ```
</RequestExample>

<ResponseExample>
  ```JSON curl theme={null}
  {
    "data":[
      {
        "index":2,
        "document":{
          "id":"vec3",
          "text":"Apple Inc. has revolutionized the tech industry with its sleek designs and user-friendly interfaces."
        },
        "score":0.47654688
      },
      {
        "index":0,
        "document":{
          "id":"vec1",
          "text":"Apple is a popular fruit known for its sweetness and crisp texture."
        },
        "score":0.047963805
      },
      {
        "index":3,
        "document":{
          "id":"vec4",
          "text":"An apple a day keeps the doctor away, as the saying goes."
        },
        "score":0.007587992
      },
      {
        "index":1,
        "document":{
          "id":"vec2",
          "text":"Many people enjoy eating apples as a healthy snack."
        },
        "score":0.0006491712
      }
    ],
    "usage":{
      "rerank_units":1
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/inference_2025-10.oas.yaml post /rerank
openapi: 3.0.3
info:
  title: Pinecone Inference API
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
  - url: https://api.pinecone.io
    description: Production API endpoints
security:
  - ApiKeyAuth: []
tags:
  - name: Inference
    description: Model inference
externalDocs:
  description: More Pinecone.io API docs
  url: https://docs.pinecone.io/introduction
paths:
  /rerank:
    post:
      tags:
        - Inference
      summary: Rerank results
      description: >-
        Rerank results according to their relevance to a query.


        For guidance and examples, see [Rerank
        results](https://docs.pinecone.io/guides/search/rerank-results).
      operationId: rerank
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
      requestBody:
        description: Rerank documents for the given query
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RerankRequest'
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RerankResult'
        '400':
          description: Bad request. The request body included invalid request parameters.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                index-metric-validation-error:
                  summary: Validation error
                  value:
                    error:
                      code: INVALID_ARGUMENT
                      message: >-
                        Bad request. The request body included invalid request
                        parameters.
                    status: 400
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    RerankRequest:
      type: object
      properties:
        model:
          example: bge-reranker-v2-m3
          description: >-
            The
            [model](https://docs.pinecone.io/guides/search/rerank-results#reranking-models)
            to use for reranking.
          type: string
        query:
          example: What is the capital of France?
          description: The query to rerank documents against.
          type: string
        top_n:
          example: 5
          description: >-
            The number of results to return sorted by relevance. Defaults to the
            number of inputs.
          type: integer
        return_documents:
          example: true
          description: Whether to return the documents in the response.
          default: true
          type: boolean
        rank_fields:
          description: >
            The field(s) to consider for reranking. If not provided, the default
            is `["text"]`.


            The number of fields supported is
            [model-specific](https://docs.pinecone.io/guides/search/rerank-results#reranking-models).
          default:
            - text
          type: array
          items:
            type: string
        documents:
          description: The documents to rerank.
          type: array
          items:
            $ref: '#/components/schemas/Document'
        parameters:
          example:
            truncate: END
          description: >-
            Additional model-specific parameters. Refer to the [model
            guide](https://docs.pinecone.io/guides/search/rerank-results#reranking-models)
            for available model parameters.
          type: object
          additionalProperties: true
      required:
        - model
        - documents
        - query
    RerankResult:
      description: The result of a reranking request.
      type: object
      properties:
        model:
          example: bge-reranker-v2-m3
          description: The model used to rerank documents.
          type: string
        data:
          description: The reranked documents.
          type: array
          items:
            $ref: '#/components/schemas/RankedDocument'
        usage:
          description: Usage statistics for the model inference.
          type: object
          properties:
            rerank_units:
              example: 1
              description: The number of rerank units consumed by this operation.
              type: integer
              format: int32
              minimum: 0
      required:
        - model
        - data
        - usage
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: >-
              Index name must contain only lowercase alphanumeric characters or
              hyphens, and must not begin or end with a hyphen.
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              description: >-
                The error code.

                Possible values: `OK`, `UNKNOWN`, `INVALID_ARGUMENT`,
                `DEADLINE_EXCEEDED`, `QUOTA_EXCEEDED`, `NOT_FOUND`,
                `ALREADY_EXISTS`, `PERMISSION_DENIED`, `UNAUTHENTICATED`,
                `RESOURCE_EXHAUSTED`, `FAILED_PRECONDITION`, `ABORTED`,
                `OUT_OF_RANGE`, `UNIMPLEMENTED`, `INTERNAL`, `UNAVAILABLE`,
                `DATA_LOSS`, or `FORBIDDEN`.
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              description: A human-readable error message describing the error.
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
    Document:
      example:
        id: '1'
        text: Paris is the capital of France.
        title: France
        url: https://example.com
      description: Document for reranking
      type: object
      additionalProperties: true
    RankedDocument:
      description: A ranked document with a relevance score and an index position.
      type: object
      properties:
        index:
          description: The index position of the document from the original request.
          type: integer
        score:
          example: 0.5
          description: >-
            The relevance of the document to the query, normalized between 0 and
            1, with scores closer to 1 indicating higher relevance.
          type: number
        document:
          $ref: '#/components/schemas/Document'
      required:
        - index
        - score
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````