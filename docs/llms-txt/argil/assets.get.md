# Source: https://docs.argil.ai/api-reference/endpoint/assets.get.md

# Get an Asset by id

> Returns a single Asset identified by its id

## OpenAPI

````yaml get /assets/{id}
paths:
  path: /assets/{id}
  method: get
  servers:
    - url: https://api.argil.ai/v1
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: API key to be included in the x-api-key header
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The id of the Asset to retrieve
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
              name:
                allOf:
                  - type: string
              type:
                allOf:
                  - type: string
                    enum:
                      - AUDIO
              fileUrl:
                allOf:
                  - type: string
                    description: URL to access the asset
            refIdentifier: '#/components/schemas/Asset'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              name: <string>
              type: AUDIO
              fileUrl: <string>
        description: Detailed information about the Asset
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              code:
                allOf:
                  - type: integer
                    format: int32
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              code: 123
              message: <string>
        description: Asset not found
  deprecated: false
  type: path
components:
  schemas: {}

````