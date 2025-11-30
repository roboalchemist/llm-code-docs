# Source: https://docs.exa.ai/reference/team-management/delete-api-key.md

# Delete API Key

> Permanently delete an API key from your team.

## OpenAPI

````yaml delete /api-keys/{id}
paths:
  path: /api-keys/{id}
  method: delete
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
              description: The unique identifier of the API key to delete
              format: uuid
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - label: Delete an API key
        lang: bash
        source: >
          curl -X DELETE
          'https://admin-api.exa.ai/team-management/api-keys/{id}' \
            -H 'x-api-key: YOUR-SERVICE-KEY'
      - label: Delete an API key
        lang: python
        source: |
          import requests

          headers = {
              'x-api-key': 'YOUR-SERVICE-KEY',
              'Content-Type': 'application/json'
          }

          response = requests.delete(
              'https://admin-api.exa.ai/team-management/api-keys/{id}',
              headers=headers
          )

          print(response.json())
      - label: Delete an API key
        lang: javascript
        source: >
          const response = await
          fetch('https://admin-api.exa.ai/team-management/api-keys/{id}', {
            method: 'DELETE',
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
              success:
                allOf:
                  - type: boolean
                    example: true
        examples:
          example:
            value:
              success: true
        description: API key deleted successfully
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