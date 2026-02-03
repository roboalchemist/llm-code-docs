# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/describeindexstats.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get index stats

> Return statistics about the contents of an index, including the vector count per namespace, the number of dimensions, and the index fullness.

Serverless indexes scale automatically as needed, so index fullness is relevant only for pod-based indexes.

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="YOUR_INDEX_HOST"

  curl -X POST "https://$INDEX_HOST/describe_index_stats" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  // EXAMPLE RESPONSE 1: Serverless index (on-demand)
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 10000
      }
    },
    "indexFullness": 0,
    "totalVectorCount": 10000,
    "dimension": 1024,
    "metric": "cosine",
    "vectorType": "dense"
  }

  // EXAMPLE RESPONSE 2: Serverless index (dedicated)
  {
    "namespaces": {
      "example-namespace": {
        "vectorCount": 10000
      }
    },
    "indexFullness": 0.000309539,
    "totalVectorCount": 10000,
    "dimension": 1536,
    "metric": "cosine",
    "vectorType": "dense"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /describe_index_stats
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
  /describe_index_stats:
    post:
      tags:
        - Vector Operations
      summary: Get index stats
      description: >-
        Return statistics about the contents of an index, including the vector
        count per namespace, the number of dimensions, and the index fullness.


        Serverless indexes scale automatically as needed, so index fullness is
        relevant only for pod-based indexes.
      operationId: describeIndexStats
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
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DescribeIndexStatsRequest'
        required: true
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IndexDescription'
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
    DescribeIndexStatsRequest:
      description: The request for the `describe_index_stats` operation.
      type: object
      properties:
        filter:
          description: >-
            If this parameter is present, the operation only returns statistics
            for vectors that satisfy the filter. See [Understanding
            metadata](https://docs.pinecone.io/guides/index-data/indexing-overview#metadata).


            Serverless indexes do not support filtering `describe_index_stats`
            by metadata.
          type: object
    IndexDescription:
      example:
        dimension: 1024
        index_fullness: 0.4
        namespaces:
          '':
            vectorCount: 50000
          example-namespace-2:
            vectorCount: 30000
        totalVectorCount: 80000
      description: The response for the `describe_index_stats` operation.
      type: object
      properties:
        namespaces:
          description: >-
            A mapping for each namespace in the index from the namespace name to
            a summary of its contents. If a metadata filter expression is
            present, the summary will reflect only vectors matching that
            expression.
          type: object
          additionalProperties:
            $ref: '#/components/schemas/NamespaceSummary'
        dimension:
          example: 1024
          description: >-
            The dimension of the indexed vectors. Not specified if `sparse`
            index.
          type: integer
          format: int64
        indexFullness:
          example: 0.4
          description: >-
            The fullness of the index, regardless of whether a metadata filter
            expression was passed. The granularity of this metric is 10%.


            Serverless indexes scale automatically as needed, so index fullness 
            is relevant only for pod-based indexes.


            The index fullness result may be inaccurate during pod resizing; to
            get the status of a pod resizing process, use
            [`describe_index`](https://docs.pinecone.io/reference/api/2024-10/control-plane/describe_index).
          type: number
          format: float
        totalVectorCount:
          example: 80000
          description: >-
            The total number of vectors in the index, regardless of whether a
            metadata filter expression was passed
          type: integer
          format: int64
        metric:
          example: cosine
          description: The metric used to measure similarity.
          type: string
        vectorType:
          example: dense
          description: The type of vectors stored in the index.
          type: string
        memory_fullness:
          description: The amount of memory used by a dedicated index
          type: number
          format: float
        storage_fullness:
          description: The amount of storage used by a dedicated index
          type: number
          format: float
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
    NamespaceSummary:
      description: A summary of the contents of a namespace.
      type: object
      properties:
        vectorCount:
          example: 50000
          description: >-
            The number of vectors stored in this namespace. Note that updates to
            this field may lag behind updates to the underlying index and
            corresponding query results, etc.
          type: integer
          format: int64
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: >-
        An API Key is required to call Pinecone APIs. Get yours from the
        [console](https://app.pinecone.io/).

````