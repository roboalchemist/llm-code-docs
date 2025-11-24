# Source: https://docs.argil.ai/api-reference/endpoint/subtitles.list.md

# List subtitle styles

> Returns a paginated array of subtitle styles available for the user

## OpenAPI

````yaml get /subtitles
paths:
  path: /subtitles
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
      query:
        page:
          schema:
            - type: integer
              required: false
              description: Page number of the subtitle styles list
              minimum: 1
              default: 1
        pageSize:
          schema:
            - type: integer
              required: false
              description: Number of subtitle styles per page
              maximum: 100
              minimum: 1
              default: 10
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              items:
                allOf:
                  - type: array
                    items:
                      $ref: '#/components/schemas/SubtitleStyle'
              totalItems:
                allOf:
                  - type: integer
                    description: Total number of subtitle styles available
              totalPages:
                allOf:
                  - type: integer
                    description: Total number of pages
              currentPage:
                allOf:
                  - type: integer
                    description: Current page number
              itemsPerPage:
                allOf:
                  - type: integer
                    description: Number of items per page
        examples:
          example:
            value:
              items:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
              totalItems: 123
              totalPages: 123
              currentPage: 123
              itemsPerPage: 123
        description: A paginated list of subtitle styles
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
    SubtitleStyle:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier of the subtitle style
        name:
          type: string
          description: Name of the subtitle style

````