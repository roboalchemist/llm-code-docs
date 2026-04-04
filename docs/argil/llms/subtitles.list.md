# Source: https://docs.argil.ai/api-reference/endpoint/subtitles.list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List subtitle styles

> Returns a paginated array of subtitle styles available for the user



## OpenAPI

````yaml get /subtitles
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /subtitles:
    get:
      summary: List subtitle styles
      description: Returns a paginated array of subtitle styles available for the user
      parameters:
        - name: page
          in: query
          description: Page number of the subtitle styles list
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
        - name: pageSize
          in: query
          description: Number of subtitle styles per page
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
      responses:
        '200':
          description: A paginated list of subtitle styles
          content:
            application/json:
              schema:
                type: object
                properties:
                  items:
                    type: array
                    items:
                      $ref: '#/components/schemas/SubtitleStyle'
                  totalItems:
                    type: integer
                    description: Total number of subtitle styles available
                  totalPages:
                    type: integer
                    description: Total number of pages
                  currentPage:
                    type: integer
                    description: Current page number
                  itemsPerPage:
                    type: integer
                    description: Number of items per page
        '400':
          description: Unexpected error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
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
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````