# Source: https://docs.exa.ai/reference/team-management/update-api-key.md

# Update API Key

> Update the name and rate limit of an existing API key.

## OpenAPI

````yaml put /api-keys/{id}
paths:
  path: /api-keys/{id}
  method: put
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
              description: The unique identifier of the API key to update
              format: uuid
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
                    description: Optional new name for the API key
                    example: Updated Production Key
              rateLimit:
                allOf:
                  - type: integer
                    description: Optional new rate limit for the API key
                    example: 2000
            required: true
            additionalProperties: false
        examples:
          example:
            value:
              name: Updated Production Key
              rateLimit: 2000
    codeSamples:
      - label: Update API key name and rate limit
        lang: bash
        source: |
          curl -X PUT 'https://admin-api.exa.ai/team-management/api-keys/{id}' \
            -H 'x-api-key: YOUR-SERVICE-KEY' \
            -H 'Content-Type: application/json' \
            -d '{
              "name": "Updated Production Key",
              "rateLimit": 2000
            }'
      - label: Update API key name and rate limit
        lang: python
        source: |
          import requests

          headers = {
              'x-api-key': 'YOUR-SERVICE-KEY',
              'Content-Type': 'application/json'
          }

          data = {
              'name': 'Updated Production Key',
              'rateLimit': 2000
          }

          response = requests.put(
              'https://admin-api.exa.ai/team-management/api-keys/{id}',
              headers=headers,
              json=data
          )

          print(response.json())
      - label: Update API key name and rate limit
        lang: javascript
        source: >
          const response = await
          fetch('https://admin-api.exa.ai/team-management/api-keys/{id}', {
            method: 'PUT',
            headers: {
              'x-api-key': 'YOUR-SERVICE-KEY',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              name: 'Updated Production Key',
              rateLimit: 2000
            })
          });


          const result = await response.json();

          console.log(result);
      - label: Update only the name
        lang: bash
        source: |
          curl -X PUT 'https://admin-api.exa.ai/team-management/api-keys/{id}' \
            -H 'x-api-key: YOUR-SERVICE-KEY' \
            -H 'Content-Type: application/json' \
            -d '{
              "name": "New Name Only"
            }'
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
                      userId:
                        type: string
                        format: uuid
                      createdAt:
                        type: string
                        format: date-time
                      updatedAt:
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
                userId: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                createdAt: '2023-11-07T05:31:56Z'
                updatedAt: '2023-11-07T05:31:56Z'
        description: API key updated successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    examples:
                      - api_key_id is required
                      - Invalid API key ID format. Must be a valid UUID.
        examples:
          example:
            value:
              error: api_key_id is required
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
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    example: You do not have permission to access this API key
        examples:
          example:
            value:
              error: You do not have permission to access this API key
        description: Forbidden - API key belongs to a different team
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
        description: Not Found - API key does not exist
  deprecated: false
  type: path
components:
  schemas: {}

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.exa.ai/llms.txt