# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/start_import.md

# Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/start_import.md

# Start import

> Start an asynchronous import of vectors from object storage into an index.

For guidance and examples, see [Import data](https://docs.pinecone.io/guides/index-data/import-data).

## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /bulk/imports
paths:
  path: /bulk/imports
  method: post
  servers:
    - url: https://{index_host}
      variables:
        index_host:
          type: string
          description: host of the index
          default: unknown
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Api-Key:
              type: apiKey
              description: >-
                An API Key is required to call Pinecone APIs. Get yours from the
                [console](https://app.pinecone.io/).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              integrationId:
                allOf:
                  - description: >-
                      The id of the [storage
                      integration](https://docs.pinecone.io/guides/operations/integrations/manage-storage-integrations)
                      that should be used to access the data.
                    type: string
                    maxLength: 1000
              uri:
                allOf:
                  - description: >-
                      The URI of the bucket (or container) and import directory
                      containing the namespaces and Parquet files you want to
                      import. For example, `s3://BUCKET_NAME/IMPORT_DIR` for
                      Amazon S3, `gs://BUCKET_NAME/IMPORT_DIR` for Google Cloud
                      Storage, or
                      `https://STORAGE_ACCOUNT.blob.core.windows.net/CONTAINER_NAME/IMPORT_DIR`
                      for Azure Blob Storage. For more information, see [Import
                      records](https://docs.pinecone.io/guides/index-data/import-data#prepare-your-data).
                    type: string
                    minLength: 1
                    maxLength: 1500
              errorMode:
                allOf:
                  - $ref: '#/components/schemas/ImportErrorMode'
            required: true
            description: The request for the `start_import` operation.
            refIdentifier: '#/components/schemas/StartImportRequest'
            requiredProperties:
              - uri
        examples:
          example:
            value:
              integrationId: <string>
              uri: <string>
              errorMode:
                onError: abort
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - example: '101'
                    description: Unique identifier for the import operation.
                    type: string
                    minLength: 1
                    maxLength: 1000
            description: The response for the `start_import` operation.
            refIdentifier: '#/components/schemas/StartImportResponse'
        examples:
          example:
            value:
              id: '101'
        description: Successful import operation
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
              message:
                allOf:
                  - &ref_1
                    type: string
              details:
                allOf:
                  - &ref_2
                    type: array
                    items:
                      $ref: '#/components/schemas/protobufAny'
            refIdentifier: '#/components/schemas/rpcStatus'
        examples:
          example:
            value:
              code: 123
              message: <string>
              details:
                - typeUrl: <string>
                  value: aSDinaTvuI8gbWludGxpZnk=
        description: Bad request. The request body included invalid request parameters.
    4XX:
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
              details:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/rpcStatus'
        examples:
          example:
            value:
              code: 123
              message: <string>
              details:
                - typeUrl: <string>
                  value: aSDinaTvuI8gbWludGxpZnk=
        description: An unexpected error response.
    5XX:
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
              details:
                allOf:
                  - *ref_2
            refIdentifier: '#/components/schemas/rpcStatus'
        examples:
          example:
            value:
              code: 123
              message: <string>
              details:
                - typeUrl: <string>
                  value: aSDinaTvuI8gbWludGxpZnk=
        description: An unexpected error response.
  deprecated: false
  type: path
components:
  schemas:
    ImportErrorMode:
      description: Indicates how to respond to errors during the import process.
      type: object
      properties:
        onError:
          description: Indicates how to respond to errors during the import process.
          type: string
          enum:
            - abort
            - continue
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte

````