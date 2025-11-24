# Source: https://docs.perplexity.ai/api-reference/generate-auth-token-post.md

# Generate Auth Token

> Generates a new authentication token for API access.

## OpenAPI

````yaml post /generate_auth_token
paths:
  path: /generate_auth_token
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
              token_name:
                allOf:
                  - title: Token Name
                    type: string
                    description: >-
                      Optional name for the authentication token to help
                      identify its purpose.
                    example: Production API Key
            required: false
            title: GenerateAuthTokenRequest
            refIdentifier: '#/components/schemas/GenerateAuthTokenRequest'
        examples:
          example:
            value:
              token_name: Production API Key
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              auth_token:
                allOf:
                  - title: Auth Token
                    type: string
                    description: >-
                      The newly generated authentication token. Store this
                      securely as it cannot be retrieved again.
                    example: pplx-1234567890abcdef
              created_at_epoch_seconds:
                allOf:
                  - title: Created At Epoch Seconds
                    type: number
                    description: Unix timestamp (in seconds) of when the token was created.
                    example: 1735689600
              token_name:
                allOf:
                  - title: Token Name
                    type: string
                    description: The name associated with this token, if provided.
                    example: Production API Key
            title: GenerateAuthTokenResponse
            refIdentifier: '#/components/schemas/GenerateAuthTokenResponse'
            requiredProperties:
              - auth_token
              - created_at_epoch_seconds
        examples:
          example:
            value:
              auth_token: pplx-1234567890abcdef
              created_at_epoch_seconds: 1735689600
              token_name: Production API Key
        description: Successfully generated authentication token.
  deprecated: false
  type: path
components:
  schemas: {}

````