# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-api-key.md

# Source: https://docs.fireworks.ai/api-reference/delete-api-key.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-api-key.md

# Source: https://docs.fireworks.ai/api-reference/delete-api-key.md

# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-api-key.md

# Source: https://docs.fireworks.ai/api-reference/delete-api-key.md

# Delete API Key

## OpenAPI

````yaml post /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete
paths:
  path: /v1/accounts/{account_id}/users/{user_id}/apiKeys:delete
  method: post
  servers:
    - url: https://api.fireworks.ai
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        account_id:
          schema:
            - type: string
              required: true
              description: The Account Id
        user_id:
          schema:
            - type: string
              required: true
              description: The User Id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              keyId:
                allOf:
                  - type: string
                    description: The key ID for the API key.
            required: true
            refIdentifier: '#/components/schemas/GatewayDeleteApiKeyBody'
            requiredProperties:
              - keyId
        examples:
          example:
            value:
              keyId: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
        examples:
          example:
            value: {}
        description: A successful response.
  deprecated: false
  type: path
components:
  schemas: {}

````