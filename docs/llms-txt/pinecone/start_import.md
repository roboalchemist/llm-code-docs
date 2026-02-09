# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/start_import.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Start import

> Start an asynchronous import of vectors from object storage into an index.

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

  curl "https://$INDEX_HOST/bulk/imports" \
    -H 'Api-Key: $PINECONE_API_KEY' \
    -H 'Content-Type: application/json' \
    -H 'X-Pinecone-Api-Version: 2025-10' \
    -d '{
          "integrationId": "a12b3d4c-47d2-492c-a97a-dd98c8dbefde",
          "uri": "s3://BUCKET_NAME/PATH/TO/DIR",
          "errorMode": {
              "onError": "continue"
              }
          }'
  ```
</RequestExample>

<ResponseExample>
  ```json curl theme={null}
  {
     "id": "101"
  }
  ```
</ResponseExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /bulk/imports
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
    post:
      tags:
        - Bulk Operations
      summary: Start import
      description: >-
        Start an asynchronous import of vectors from object storage into an
        index.


        For guidance and examples, see [Import
        data](https://docs.pinecone.io/guides/index-data/import-data).
      operationId: startBulkImport
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
              $ref: '#/components/schemas/StartImportRequest'
        required: true
      responses:
        '200':
          description: Successful import operation
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartImportResponse'
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
    StartImportRequest:
      description: The request for the `start_import` operation.
      type: object
      properties:
        integrationId:
          description: >-
            The id of the [storage
            integration](https://docs.pinecone.io/guides/operations/integrations/manage-storage-integrations)
            that should be used to access the data.
          type: string
          maxLength: 1000
        uri:
          description: >-
            The URI of the bucket (or container) and import directory containing
            the namespaces and Parquet files you want to import. For example,
            `s3://BUCKET_NAME/IMPORT_DIR` for Amazon S3,
            `gs://BUCKET_NAME/IMPORT_DIR` for Google Cloud Storage, or
            `https://STORAGE_ACCOUNT.blob.core.windows.net/CONTAINER_NAME/IMPORT_DIR`
            for Azure Blob Storage. For more information, see [Import
            records](https://docs.pinecone.io/guides/index-data/import-data#prepare-your-data).
          type: string
          minLength: 1
          maxLength: 1500
        errorMode:
          $ref: '#/components/schemas/ImportErrorMode'
      required:
        - uri
    StartImportResponse:
      description: The response for the `start_import` operation.
      type: object
      properties:
        id:
          example: '101'
          description: Unique identifier for the import operation.
          type: string
          minLength: 1
          maxLength: 1000
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
    ImportErrorMode:
      description: Indicates how to respond to errors during the import process.
      type: object
      properties:
        onError:
          description: |-
            Indicates how to respond to errors during the import process.
            Possible values: `abort` or `continue`.
          x-enum:
            - abort
            - continue
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