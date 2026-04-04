# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/list_imports.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List imports

> List all recent and ongoing import operations.

By default, `list_imports` returns up to 100 imports per page. If the `limit` parameter is set, `list` returns up to that number of imports instead. Whenever there are additional IDs to return, the response also includes a `pagination_token` that you can use to get the next batch of imports. When the response does not include a `pagination_token`, there are no more imports to return.

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

  curl -X GET "https://$INDEX_HOST/bulk/imports?paginationToken==Tm90aGluZyB0byBzZWUgaGVyZQo" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'X-Pinecone-Api-Version: 2025-10'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
    "data": [
      {
        "id": "1",
        "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
        "status": "Pending",
        "started_at": "2024-08-19T20:49:00.754Z",
        "finished_at": "2024-08-19T20:49:00.754Z",
        "percent_complete": 42.2,
        "records_imported": 1000000
      }
    ],
    "pagination": {
      "next": "Tm90aGluZyB0byBzZWUgaGVyZQo="
    }
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml get /bulk/imports
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
  /bulk/imports:
    get:
      tags:
        - Bulk Operations
      summary: List imports
      description: >-
        List all recent and ongoing import operations.


        By default, `list_imports` returns up to 100 imports per page. If the
        `limit` parameter is set, `list` returns up to that number of imports
        instead. Whenever there are additional IDs to return, the response also
        includes a `pagination_token` that you can use to get the next batch of
        imports. When the response does not include a `pagination_token`, there
        are no more imports to return.


        For guidance and examples, see [Import
        data](https://docs.pinecone.io/guides/index-data/import-data).
      operationId: listBulkImports
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: query
          name: limit
          description: Max number of operations to return per page.
          schema:
            default: 100
            type: integer
            format: int32
            minimum: 1
            maximum: 100
          example: 10
          style: form
        - in: query
          name: paginationToken
          description: Pagination token to continue a previous listing operation.
          schema:
            type: string
          style: form
      responses:
        '200':
          description: A list of import operations
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListImportsResponse'
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
    ListImportsResponse:
      description: The response for the `list_imports` operation.
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/ImportModel'
        pagination:
          $ref: '#/components/schemas/Pagination'
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
    Pagination:
      type: object
      properties:
        next:
          example: Tm90aGluZyB0byBzZWUgaGVyZQo=
          type: string
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