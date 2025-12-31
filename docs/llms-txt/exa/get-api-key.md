# Source: https://docs.exa.ai/reference/team-management/get-api-key.md

# Get API Key

> Retrieve details of a specific API key by its ID.

## OpenAPI

````yaml get /api-keys/{id}
paths:
  path: /api-keys/{id}
  method: get
  servers:
    - url: https://admin-api.exa.ai/team-management
  request:
    security:
      - title: apikey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
              description: Service API key for team authentication
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the API key
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Get a specific API key
        lang: bash
        source: |
          curl -X GET 'https://admin-api.exa.ai/team-management/api-keys/{id}' \
            -H 'x-api-key: YOUR-SERVICE-KEY'
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              apiKey:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                        format: uuid
                      name:
                        type: string
                      rateLimit:
                        type: integer
                        nullable: true
                      teamId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
        examples:
          example:
            value:
              apiKey:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                rateLimit: 123
                teamId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
        description: API key retrieved successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Invalid API key ID format. Must be a valid UUID.
        examples:
          example:
            value:
              error: Invalid API key ID format. Must be a valid UUID.
        description: Bad request - invalid API key ID format
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Unauthorized
        examples:
          example:
            value:
              error: Unauthorized
        description: Unauthorized - Invalid or missing service key
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: API key not found
        examples:
          example:
            value:
              error: API key not found
        description: Not found - API key does not exist
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt