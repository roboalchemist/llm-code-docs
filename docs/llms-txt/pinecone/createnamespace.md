# Source: https://docs.pinecone.io/reference/api/2025-10/data-plane/createnamespace.md

# Create a namespace

> Create a namespace in a serverless index.

For guidance and examples, see [Manage namespaces](https://docs.pinecone.io/guides/manage-data/manage-namespaces).

**Note:** This operation is not supported for pod-based indexes.

## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/db_data_2025-10.oas.yaml post /namespaces
paths:
  path: /namespaces
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
      header:
        X-Pinecone-Api-Version:
          schema:
            - type: string
              required: true
              description: Required date-based version header
              default: 2025-10
          style: simple
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - example: example-namespace
                    description: The name of the namespace.
                    type: string
              schema:
                allOf:
                  - example:
                      fields:
                        description:
                          filterable: true
                        genre:
                          filterable: true
                        year:
                          filterable: true
                    description: >-
                      Schema for the behavior of Pinecone's internal metadata
                      index. By default, all metadata is indexed; when `schema`
                      is present, only fields which are present in the `fields`
                      object with a `filterable: true` are indexed. Note that
                      `filterable: false` is not currently supported.
                    type: object
                    properties:
                      fields:
                        description: >-
                          A map of metadata field names to their configuration.
                          The field name must be a valid metadata field name.
                          The field name must be unique.
                        type: object
                        additionalProperties:
                          type: object
                          properties:
                            filterable:
                              description: >-
                                Whether the field is filterable. If true, the
                                field is indexed and can be used in filters.
                                Only true values are allowed.
                              type: boolean
                    required:
                      - fields
            required: true
            description: >-
              A request for creating a namespace with the specified namespace
              name.
            refIdentifier: '#/components/schemas/CreateNamespaceRequest'
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: example-namespace
              schema:
                fields:
                  description:
                    filterable: true
                  genre:
                    filterable: true
                  year:
                    filterable: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - example: example-namespace
                    description: The name of the namespace.
                    type: string
              record_count:
                allOf:
                  - example: 20000
                    description: The total amount of records within the namespace.
                    type: integer
                    format: int64
              schema:
                allOf:
                  - example:
                      fields:
                        description:
                          filterable: true
                        genre:
                          filterable: true
                        year:
                          filterable: true
                    description: >-
                      Schema for the behavior of Pinecone's internal metadata
                      index. By default, all metadata is indexed; when `schema`
                      is present, only fields which are present in the `fields`
                      object with a `filterable: true` are indexed. Note that
                      `filterable: false` is not currently supported.
                    type: object
                    properties:
                      fields:
                        description: >-
                          A map of metadata field names to their configuration.
                          The field name must be a valid metadata field name.
                          The field name must be unique.
                        type: object
                        additionalProperties:
                          type: object
                          properties:
                            filterable:
                              description: >-
                                Whether the field is filterable. If true, the
                                field is indexed and can be used in filters.
                                Only true values are allowed.
                              type: boolean
                    required:
                      - fields
              indexed_fields:
                allOf:
                  - description: A list of all indexed metatadata fields in the namespace
                    type: object
                    properties:
                      fields:
                        type: array
                        items:
                          type: string
                        example:
                          - genre
                          - year
                          - author
            description: A description of a namespace, including the name and record count.
            refIdentifier: '#/components/schemas/NamespaceDescription'
        examples:
          example:
            value:
              name: example-namespace
              record_count: 20000
              schema:
                fields:
                  description:
                    filterable: true
                  genre:
                    filterable: true
                  year:
                    filterable: true
              indexed_fields:
                fields:
                  - genre
                  - year
                  - author
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
    '409':
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
        description: Namespace of the given name already exists on the index.
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