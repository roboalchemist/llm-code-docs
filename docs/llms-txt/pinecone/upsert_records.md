# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/upsert_records.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Upsert text

> Upsert text into a namespace. Pinecone converts the text to vectors automatically using the hosted embedding model associated with the index.

Upserting text is supported only for [indexes with integrated embedding](https://docs.pinecone.io/reference/api/2025-01/control-plane/create_for_model).

For guidance, examples, and limits, see [Upsert data](https://docs.pinecone.io/guides/index-data/upsert-data).

<RequestExample>
  ```shell curl theme={null}
  # To get the unique host for an index,
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  INDEX_HOST="INDEX_HOST"
  NAMESPACE="YOUR_NAMESPACE"
  PINECONE_API_KEY="YOUR_API_KEY"

  # Upsert records into a namespace
  # `chunk_text` fields are converted to dense vectors
  # `category` fields are stored as metadata
  curl "https://$INDEX_HOST/records/namespaces/$NAMESPACE/upsert" \
    -H "Content-Type: application/x-ndjson" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10" \
    -d '{"_id": "rec1", "chunk_text": "Apples are a great source of dietary fiber, which supports digestion and helps maintain a healthy gut.", "category": "digestive system"}
        {"_id": "rec2", "chunk_text": "Apples originated in Central Asia and have been cultivated for thousands of years, with over 7,500 varieties available today.", "category": "cultivation"}
        {"_id": "rec3", "chunk_text": "Rich in vitamin C and other antioxidants, apples contribute to immune health and may reduce the risk of chronic diseases.", "category": "immune system"}
        {"_id": "rec4", "chunk_text": "The high fiber content in apples can also help regulate blood sugar levels, making them a favorable snack for people with diabetes.", "category": "endocrine system"}'
  ```
</RequestExample>

<ResponseExample />


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /records/namespaces/{namespace}/upsert
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
  /records/namespaces/{namespace}/upsert:
    post:
      tags:
        - Vector Operations
      summary: Upsert text
      description: >-
        Upsert text into a namespace. Pinecone converts the text to vectors
        automatically using the hosted embedding model associated with the
        index.


        Upserting text is supported only for [indexes with integrated
        embedding](https://docs.pinecone.io/reference/api/2025-01/control-plane/create_for_model).


        For guidance, examples, and limits, see [Upsert
        data](https://docs.pinecone.io/guides/index-data/upsert-data).
      operationId: upsertRecordsNamespace
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
          description: The namespace to upsert records into.
          required: true
          schema:
            type: string
          style: simple
      requestBody:
        description: >
          Each record in the request body must include an `_id` field and a
          field that matches your index's `field_map` configuration (such as
          `chunk_text` or `data`). All other fields are stored as metadata.
        content:
          application/x-ndjson:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/UpsertRecord'
        required: true
      responses:
        '201':
          description: A successful response.
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
    UpsertRecord:
      example:
        _id: example-record-1
      description: The request for the `upsert` operation.
      type: object
      properties:
        _id:
          description: >-
            The unique ID of the record to upsert. Note that `id` can be used as
            an alias for `_id`.
          type: string
      required:
        - _id
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