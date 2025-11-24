# Source: https://docs.squared.ai/api-reference/catalogs/update_catalog.md

# Update Catalog

## OpenAPI

````yaml PUT /api/v1/catalogs/{id}
paths:
  path: /api/v1/catalogs/{id}
  method: put
  servers:
    - url: https://api.squared.ai
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: integer
              required: true
              description: The ID of the catalog to update
              example: 34
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              connector_id:
                allOf:
                  - type: integer
                    example: 6
              catalog:
                allOf:
                  - type: object
                    properties:
                      json_schema:
                        type: object
                        example:
                          field: test_field
            required: true
        examples:
          example:
            value:
              connector_id: 6
              catalog:
                json_schema:
                  field: test_field
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        example: '34'
                      type:
                        type: string
                        example: catalogs
                      attributes:
                        type: object
                        properties:
                          connector_id:
                            type: integer
                            example: 6
                          workspace_id:
                            type: integer
                            example: 2
                          catalog:
                            type: object
                            properties:
                              streams:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    name:
                                      type: string
                                      example: test_name
                                    url:
                                      type: string
                                      example: test_url
                                    json_schema:
                                      type: object
                                      example:
                                        field: test field
                                    batch_support:
                                      type: boolean
                                      example: false
                                    batch_size:
                                      type: integer
                                      example: 0
                                    request_method:
                                      type: string
                                      example: POST
                              request_rate_concurrency:
                                type: integer
                                example: 10
                              request_rate_limit:
                                type: integer
                                example: 600
                              request_rate_limit_unit:
                                type: string
                                example: minute
                          catalog_hash:
                            type: string
                            example: 0755b5f0d3432bc3b0064227d2b6178d402327b9
        examples:
          example:
            value:
              data:
                id: '34'
                type: catalogs
                attributes:
                  connector_id: 6
                  workspace_id: 2
                  catalog:
                    streams:
                      - name: test_name
                        url: test_url
                        json_schema:
                          field: test field
                        batch_support: false
                        batch_size: 0
                        request_method: POST
                    request_rate_concurrency: 10
                    request_rate_limit: 600
                    request_rate_limit_unit: minute
                  catalog_hash: 0755b5f0d3432bc3b0064227d2b6178d402327b9
        description: Catalog updated successfully
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Bad Request
        examples: {}
        description: Bad Request
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized
        examples: {}
        description: Unauthorized
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Catalog not found
        examples: {}
        description: Catalog not found
    '500':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Internal Server Error
        examples: {}
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````