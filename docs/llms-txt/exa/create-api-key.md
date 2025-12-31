# Source: https://docs.exa.ai/reference/team-management/create-api-key.md

# Create API Key

> Create a new API key for your team with optional name and rate limit configuration.

## OpenAPI

````yaml post /api-keys
paths:
  path: /api-keys
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: Optional name for the API key
                    example: Production API Key
              rateLimit:
                allOf:
                  - type: integer
                    description: Optional rate limit for the API key (requests per minute)
                    example: 1000
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: Production API Key
              rateLimit: 1000
    codeSamples:
      - label: Create API key with name and rate limit
        lang: bash
        source: |
          curl -X POST 'https://admin-api.exa.ai/team-management/api-keys' \
            -H 'x-api-key: YOUR-SERVICE-KEY' \
            -H 'Content-Type: application/json' \
            -d '{
              "name": "Production API Key",
              "rateLimit": 1000
            }'
      - label: Create API key with name and rate limit
        lang: python
        source: |
          import requests

          headers = {
              'x-api-key': 'YOUR-SERVICE-KEY',
              'Content-Type': 'application/json'
          }

          data = {
              'name': 'Production API Key',
              'rateLimit': 1000
          }

          response = requests.post(
              'https://admin-api.exa.ai/team-management/api-keys',
              headers=headers,
              json=data
          )

          print(response.json())
      - label: Create API key with name and rate limit
        lang: javascript
        source: >
          const response = await
          fetch('https://admin-api.exa.ai/team-management/api-keys', {
            method: 'POST',
            headers: {
              'x-api-key': 'YOUR-SERVICE-KEY',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              name: 'Production API Key',
              rateLimit: 1000
            })
          });


          const result = await response.json();

          console.log(result);
      - label: Create API key without optional parameters
        lang: bash
        source: |
          curl -X POST 'https://admin-api.exa.ai/team-management/api-keys' \
            -H 'x-api-key: YOUR-SERVICE-KEY' \
            -H 'Content-Type: application/json' \
            -d '{}'
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
                        description: Unique identifier for the API key
                      name:
                        type: string
                        description: Name of the API key
                      rateLimit:
                        type: integer
                        nullable: true
                        description: Rate limit in requests per minute
                      teamId:
                        type: string
                        format: uuid
                        description: Team ID this key belongs to
                      userId:
                        type: string
                        format: uuid
                        description: User ID who created this key
                      createdAt:
                        type: string
                        format: date-time
                        description: When the key was created
        examples:
          example:
            value:
              apiKey:
                id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                name: <string>
                rateLimit: 123
                teamId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
        description: API key created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    examples:
                      - No user found for team
                      - Rate limit cannot exceed team's limit of 500 QPS
                      - >-
                        Unexpected parameters: invalidParam. Allowed: name,
                        rateLimit.
        examples:
          example:
            value:
              error: No user found for team
        description: Bad Request - Invalid parameters
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
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt