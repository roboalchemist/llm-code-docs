# Source: https://docs.exa.ai/reference/team-management/list-api-keys.md

# List API Keys

> Retrieve all API keys belonging to your team with their metadata.

## OpenAPI

````yaml get /api-keys
paths:
  path: /api-keys
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
      path: {}
      query:
        api_key_id:
          schema:
            - type: string
              required: false
              description: Optional API key ID to retrieve a specific key
              format: uuid
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: List all API keys
        lang: bash
        source: |
          curl -X GET 'https://admin-api.exa.ai/team-management/api-keys' \
            -H 'x-api-key: YOUR-SERVICE-KEY'
      - label: List all API keys
        lang: python
        source: |
          import requests

          headers = {
              'x-api-key': 'YOUR-SERVICE-KEY'
          }

          response = requests.get(
              'https://admin-api.exa.ai/team-management/api-keys',
              headers=headers
          )

          print(response.json())
      - label: List all API keys
        lang: javascript
        source: >
          const response = await
          fetch('https://admin-api.exa.ai/team-management/api-keys', {
            method: 'GET',
            headers: {
              'x-api-key': 'YOUR-SERVICE-KEY'
            }
          });


          const result = await response.json();

          console.log(result);
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              apiKeys:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                          format: uuid
                        name:
                          type: string
                        rateLimit:
                          type: integer
                          nullable: true
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
              apiKeys:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  rateLimit: 123
        description: List of API keys retrieved successfully
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: Insufficient permissions to access this API key
        examples:
          example:
            value:
              error: Insufficient permissions to access this API key
        description: Forbidden - insufficient permissions to access this API key
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    examples:
                      - API key not found
                      - Team not found
        examples:
          example:
            value:
              error: API key not found
        description: Not found - API key or team not found
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt