# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/delete.md

# Source: https://docs.pinecone.io/reference/api/2025-04/data-plane/delete.md

# Delete vectors

> Delete vectors by id from a single namespace.

For guidance and examples, see [Delete data](https://docs.pinecone.io/guides/manage-data/delete-data).

## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-04/db_data_2025-04.oas.yaml post /vectors/delete
paths:
  path: /vectors/delete
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
              ids:
                allOf:
                  - example:
                      - id-0
                      - id-1
                    description: Vectors to delete.
                    type: array
                    items:
                      type: string
                    minLength: 1
                    maxLength: 1000
              deleteAll:
                allOf:
                  - example: false
                    description: >-
                      This indicates that all vectors in the index namespace
                      should be deleted.
                    default: 'false'
                    type: boolean
              namespace:
                allOf:
                  - example: example-namespace
                    description: The namespace to delete vectors from, if applicable.
                    type: string
              filter:
                allOf:
                  - description: >-
                      If specified, the metadata filter here will be used to
                      select the vectors to delete. This is mutually exclusive
                      with specifying ids to delete in the ids param or using
                      delete_all=True. See [Delete
                      data](https://docs.pinecone.io/guides/manage-data/delete-data#delete-records-by-metadata).
                    type: object
            required: true
            description: The request for the `delete` operation.
            refIdentifier: '#/components/schemas/DeleteRequest'
        examples:
          example:
            value:
              ids:
                - id-0
                - id-1
              deleteAll: false
              namespace: example-namespace
              filter: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            description: The response for the `delete` operation.
            refIdentifier: '#/components/schemas/DeleteResponse'
        examples:
          example:
            value: {}
        description: A successful response.
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
    protobufAny:
      type: object
      properties:
        typeUrl:
          type: string
        value:
          type: string
          format: byte

````