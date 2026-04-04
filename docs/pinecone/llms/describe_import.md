# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/describe_import.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Describe an import

> Return details of a specific import operation.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

<Note>
  This feature is in [public preview](/release-notes/feature-availability) and available only on [Standard and Enterprise plans](https://www.pinecone.io/pricing/).
</Note>

<RequestExample>
  ```bash curl theme={null}
  # To get the unique host for an index, 
  # see https://docs.pinecone.io/guides/manage-data/target-an-index
  PINECONE_API_KEY="YOUR_API_KEY"
  INDEX_HOST="INDEX_HOST"

  curl -X GET "https://$INDEX_HOST/bulk/imports/101" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-Api-Version: 2025-10'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "id": "101",
    "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
    "status": "Pending",
    "created_at": "2024-08-19T20:49:00.754Z",
    "finished_at": "2024-08-19T20:49:00.754Z",
    "percent_complete": 42.2,
    "records_imported": 1000000
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml get /bulk/imports/{id}
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
  /bulk/imports/{id}:
    get:
      tags:
        - Bulk Operations
      summary: Describe an import
      description: >-
        Return details of a specific import operation.


        For guidance and examples, see [Import
        data](https://docs.pinecone.io/guides/index-data/import-data).
      operationId: describeBulkImport
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
          name: id
          description: Unique identifier for the import operation.
          required: true
          schema:
            type: string
            minLength: 1
            maxLength: 1000
          example: '101'
          style: simple
      responses:
        '200':
          description: Details of the import operation.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImportModel'
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
    ImportModel:
      description: The model for an import operation.
      type: object
      properties:
        id:
          example: '101'
          description: Unique identifier for the import operation.
          type: string
          minLength: 1
          maxLength: 1000
        uri:
          description: The URI from where the data is imported.
          type: string
        status:
          example: Pending
          description: >-
            The status of the operation.

            Possible values: `Pending`, `InProgress`, `Failed`, `Completed`, or
            `Cancelled`.
          x-enum:
            - Pending
            - InProgress
            - Failed
            - Completed
            - Cancelled
          type: string
        createdAt:
          description: The start time of the import operation.
          type: string
          format: date-time
        finishedAt:
          description: The end time of the import operation.
          type: string
          format: date-time
        percentComplete:
          example: 42.2
          description: The progress made by the operation, as a percentage.
          type: number
          format: float
          minimum: 0
          maximum: 100
        recordsImported:
          example: 1000000
          description: The number of records successfully imported.
          type: integer
          format: int64
        error:
          description: The error message if the import process failed.
          type: string
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