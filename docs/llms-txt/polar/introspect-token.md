# Source: https://polar.sh/docs/api-reference/oauth2/connect/introspect-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introspect Token

> Get information about an access token.



## OpenAPI

````yaml post /v1/oauth2/introspect
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
  /v1/oauth2/introspect:
    post:
      tags:
        - oauth2
        - public
      summary: Introspect Token
      description: Get information about an access token.
      operationId: oauth2:introspect_token
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              $ref: '#/components/schemas/IntrospectTokenRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IntrospectTokenResponse'
      security:
        - {}
components:
  schemas:
    IntrospectTokenRequest:
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
      title: IntrospectTokenRequest
      type: object
    IntrospectTokenResponse:
      properties:
        active:
          type: boolean
          title: Active
        client_id:
          type: string
          title: Client Id
        token_type:
          type: string
          enum:
            - access_token
            - refresh_token
          title: Token Type
        scope:
          type: string
          title: Scope
        sub_type:
          $ref: '#/components/schemas/SubType'
        sub:
          type: string
          title: Sub
        aud:
          type: string
          title: Aud
        iss:
          type: string
          title: Iss
        exp:
          type: integer
          title: Exp
        iat:
          type: integer
          title: Iat
      type: object
      required:
        - active
        - client_id
        - token_type
        - scope
        - sub_type
        - sub
        - aud
        - iss
        - exp
        - iat
      title: IntrospectTokenResponse
    SubType:
      type: string
      enum:
        - user
        - organization
      title: SubType
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.

````