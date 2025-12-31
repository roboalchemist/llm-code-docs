# Source: https://docs.squared.ai/api-reference/catalogs/create_catalog.md

# Create Catalog

## OpenAPI

````yaml POST /api/v1/catalogs
paths:
  path: /api/v1/catalogs
  method: post
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
      path: {}
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
                          key: value
            required: true
        examples:
          example:
            value:
              connector_id: 6
              catalog:
                json_schema:
                  key: value
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: integer
                    example: 123
              connector_id:
                allOf:
                  - type: integer
                    example: 6
              workspace_id:
                allOf:
                  - type: integer
                    example: 2
              catalog:
                allOf:
                  - type: object
                    properties:
                      json_schema:
                        type: object
                        example:
                          key: value
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    example: '2023-08-20T15:28:00Z'
              updated_at:
                allOf:
                  - type: string
                    format: date-time
                    example: '2023-08-20T15:28:00Z'
        examples:
          example:
            value:
              id: 123
              connector_id: 6
              workspace_id: 2
              catalog:
                json_schema:
                  key: value
              created_at: '2023-08-20T15:28:00Z'
              updated_at: '2023-08-20T15:28:00Z'
        description: Successful response
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