# Source: https://io.net/docs/reference/rag/prompts/list-all-prompts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List all prompts

> List all available prompts. This endpoint retrieves a list of all prompts in the system. Only superusers can access this endpoint.



## OpenAPI

````yaml openapi/rag-prompts/list-all-prompts.json post /api/r2r/v3/prompts
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/r2r/v3/prompts:
    post:
      summary: List all prompts
      description: >-
        List all available prompts. This endpoint retrieves a list of all
        prompts in the system. Only superusers can access this endpoint.
      operationId: list-all-prompts
      responses:
        '200':
          description: '200'
          content:
            application/json:
              examples:
                Result:
                  value:
                    results:
                      - id: id
                        name: name
                        template: template
                        created_at: '2024-01-15T09:30:00Z'
                        updated_at: '2024-01-15T09:30:00Z'
                        input_types:
                          key: value
                    total_entries: 1
              schema:
                type: object
                properties:
                  results:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          example: id
                        name:
                          type: string
                          example: name
                        template:
                          type: string
                          example: template
                        created_at:
                          type: string
                          example: '2024-01-15T09:30:00Z'
                        updated_at:
                          type: string
                          example: '2024-01-15T09:30:00Z'
                        input_types:
                          type: object
                          properties:
                            key:
                              type: string
                              example: value
                  total_entries:
                    type: integer
                    example: 1
                    default: 0
        '400':
          description: '400'
          content:
            application/json:
              examples:
                Result:
                  value: {}
              schema:
                type: object
                properties: {}
      deprecated: false
components:
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````