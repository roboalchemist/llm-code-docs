# Source: https://docs.tavus.io/api-reference/guardrails/get-guardrails-list.md

# Get Guardrails (All Sets)

> This endpoint returns a list of all sets of guardrails.


## OpenAPI

````yaml get /v2/guardrails
paths:
  path: /v2/guardrails
  method: get
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path: {}
      query:
        limit:
          schema:
            - type: integer
              description: The number of guardrails to return per page. Default is 10.
        page:
          schema:
            - type: integer
              description: The page number to return. Default is 1.
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        guardrails_id:
                          type: string
                          description: Unique identifier for the guardrails
                          example: g12345
                        created_at:
                          type: string
                          description: >-
                            ISO 8601 timestamp of when the guardrails were
                            created
                          example: '2024-01-15T10:30:00Z'
                        updated_at:
                          type: string
                          description: >-
                            ISO 8601 timestamp of when the guardrails were last
                            updated
                          example: '2024-01-15T10:30:00Z'
              total_count:
                allOf:
                  - type: integer
                    description: The total number of guardrails
                    example: 15
        examples:
          example:
            value:
              data:
                - guardrails_id: g12345
                  created_at: '2024-01-15T10:30:00Z'
                  updated_at: '2024-01-15T10:30:00Z'
              total_count: 15
        description: Successfully retrieved guardrails
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
  deprecated: false
  type: path
components:
  schemas: {}

````