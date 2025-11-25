# Source: https://docs.fireworks.ai/tools-sdks/firectl/commands/delete-secret.md

# Source: https://docs.fireworks.ai/api-reference/delete-secret.md

# null

## OpenAPI

````yaml delete /v1/accounts/{account_id}/secrets/{secret_id}
paths:
  path: /v1/accounts/{account_id}/secrets/{secret_id}
  method: delete
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
        secret_id:
          schema:
            - type: string
              required: true
              description: The Secret Id
      query: {}
      header: {}
      cookie: {}
    body: {}
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