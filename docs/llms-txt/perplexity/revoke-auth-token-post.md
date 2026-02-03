# Source: https://docs.perplexity.ai/api-reference/revoke-auth-token-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke Auth Token

> Revokes an existing authentication token.



## OpenAPI

````yaml post /revoke_auth_token
openapi: 3.1.0
info:
  description: Perplexity AI API - Authentication Management
  title: Perplexity AI API - Authentication
  version: 1.0.0
servers:
  - url: https://api.perplexity.ai
    description: Perplexity AI API
security: []
paths:
  /revoke_auth_token:
    post:
      summary: Revoke Auth Token
      description: Revokes an existing authentication token.
      operationId: revoke_auth_token
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/RevokeAuthTokenRequest'
      responses:
        '200':
          description: Successfully revoked authentication token.
      security:
        - BearerAuth: []
components:
  schemas:
    RevokeAuthTokenRequest:
      type: object
      required:
        - auth_token
      properties:
        auth_token:
          type: string
          description: The authentication token to revoke.
          example: pplx-1234567890abcdef
  securitySchemes:
    BearerAuth:
      scheme: bearer
      type: http

````