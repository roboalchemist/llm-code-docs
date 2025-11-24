# Source: https://docs.argil.ai/api-reference/endpoint/assets.list.md

# List Assets

> Get a list of available assets from your library

## OpenAPI

````yaml get /assets
paths:
  path: /assets
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Asset'
        examples:
          example:
            value:
              - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                type: AUDIO
                fileUrl: <string>
        description: An array of audio assets
    '400':
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
        description: Unexpected error
  deprecated: false
  type: path
components:
  schemas:
    Asset:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        type:
          type: string
          enum:
            - AUDIO
        fileUrl:
          type: string
          description: URL to access the asset

````