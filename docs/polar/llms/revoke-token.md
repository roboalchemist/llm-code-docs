# Source: https://polar.sh/docs/api-reference/oauth2/connect/revoke-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Revoke Token

> Revoke an access token or a refresh token.



## OpenAPI

````yaml post /v1/oauth2/revoke
openapi: 3.1.0
info:
  title: Polar API
  summary: Polar HTTP and Webhooks API
  description: Read the docs at https://polar.sh/docs/api-reference
  version: 0.1.0
servers:
  - url: https://api.polar.sh
    description: Production environment
    x-speakeasy-server-id: production
  - url: https://sandbox-api.polar.sh
    description: Sandbox environment
    x-speakeasy-server-id: sandbox
security:
  - access_token: []
tags:
  - name: public
    description: >-
      Endpoints shown and documented in the Polar API documentation and
      available in our SDKs.
  - name: private
    description: >-
      Endpoints that should appear in the schema only in development to generate
      our internal JS SDK.
  - name: mcp
    description: Endpoints enabled in the MCP server.
paths:
  /v1/oauth2/revoke:
    post:
      tags:
        - oauth2
        - public
      summary: Revoke Token
      description: Revoke an access token or a refresh token.
      operationId: oauth2:revoke_token
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/RevokeTokenRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RevokeTokenResponse'
      security:
        - {}
components:
  schemas:
    RevokeTokenRequest:
      properties:
        token:
          type: string
          title: Token
        token_type_hint:
          anyOf:
            - enum:
                - access_token
                - refresh_token
              type: string
            - type: 'null'
          default: null
          title: Token Type Hint
        client_id:
          type: string
          title: Client Id
        client_secret:
          type: string
          title: Client Secret
      required:
        - token
        - client_id
        - client_secret
      title: RevokeTokenRequest
      type: object
    RevokeTokenResponse:
      properties: {}
      type: object
      title: RevokeTokenResponse
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.

````