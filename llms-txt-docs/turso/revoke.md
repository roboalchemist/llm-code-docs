# Source: https://docs.turso.tech/cli/auth/api-tokens/revoke.md

# Source: https://docs.turso.tech/api-reference/tokens/revoke.md

# Revoke API Token

> Revokes the provided API token belonging to a user.

## OpenAPI

````yaml DELETE /v1/auth/api-tokens/{tokenName}
paths:
  path: /v1/auth/api-tokens/{tokenName}
  method: delete
  servers:
    - url: https://api.turso.tech
      description: Turso's Platform API
  request:
    security: []
    parameters:
      path:
        tokenName:
          schema:
            - type: string
              required: true
              description: The name of the api token.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              token:
                allOf:
                  - type: string
                    description: The revoked token name.
                    example: ...
        examples:
          example:
            value:
              token: ...
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````