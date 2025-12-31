# Source: https://docs.perplexity.ai/api-reference/revoke-auth-token-post.md

# Revoke Auth Token

> Revokes an existing authentication token.

## OpenAPI

````yaml post /revoke_auth_token
paths:
  path: /revoke_auth_token
  method: post
  servers:
    - url: https://api.perplexity.ai
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
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
              auth_token:
                allOf:
                  - title: Auth Token
                    type: string
                    description: The authentication token to revoke.
                    example: pplx-1234567890abcdef
            required: true
            title: RevokeAuthTokenRequest
            refIdentifier: '#/components/schemas/RevokeAuthTokenRequest'
            requiredProperties:
              - auth_token
        examples:
          example:
            value:
              auth_token: pplx-1234567890abcdef
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Successfully revoked authentication token.
        examples: {}
        description: Successfully revoked authentication token.
  deprecated: false
  type: path
components:
  schemas: {}

````