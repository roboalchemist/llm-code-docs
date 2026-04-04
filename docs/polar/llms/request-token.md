# Source: https://polar.sh/docs/api-reference/oauth2/connect/request-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://polar.sh/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Request Token

> Request an access token using a valid grant.



## OpenAPI

````yaml post /v1/oauth2/token
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
  /v1/oauth2/token:
    post:
      tags:
        - oauth2
        - public
      summary: Request Token
      description: Request an access token using a valid grant.
      operationId: oauth2:request_token
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              oneOf:
                - $ref: '#/components/schemas/AuthorizationCodeTokenRequest'
                - $ref: '#/components/schemas/RefreshTokenRequest'
                - $ref: '#/components/schemas/WebTokenRequest'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TokenResponse'
      security:
        - {}
components:
  schemas:
    AuthorizationCodeTokenRequest:
      properties:
        grant_type:
          const: authorization_code
          title: Grant Type
          type: string
        client_id:
          type: string
          title: Client Id
        client_secret:
          type: string
          title: Client Secret
        code:
          title: Code
          type: string
        redirect_uri:
          format: uri
          maxLength: 2083
          minLength: 1
          title: Redirect Uri
          type: string
      required:
        - grant_type
        - client_id
        - client_secret
        - code
        - redirect_uri
      title: AuthorizationCodeTokenRequest
      type: object
    RefreshTokenRequest:
      properties:
        grant_type:
          const: refresh_token
          title: Grant Type
          type: string
        client_id:
          type: string
          title: Client Id
        client_secret:
          type: string
          title: Client Secret
        refresh_token:
          title: Refresh Token
          type: string
      required:
        - grant_type
        - client_id
        - client_secret
        - refresh_token
      title: RefreshTokenRequest
      type: object
    WebTokenRequest:
      properties:
        grant_type:
          const: web
          title: Grant Type
          type: string
        client_id:
          type: string
          title: Client Id
        client_secret:
          type: string
          title: Client Secret
        session_token:
          title: Session Token
          type: string
        sub_type:
          default: user
          enum:
            - user
            - organization
          title: Sub Type
          type: string
        sub:
          anyOf:
            - type: string
              format: uuid4
            - type: 'null'
          default: null
          title: Sub
        scope:
          anyOf:
            - type: string
            - type: 'null'
          default: null
          title: Scope
      required:
        - grant_type
        - client_id
        - client_secret
        - session_token
      title: WebTokenRequest
      type: object
    TokenResponse:
      properties:
        access_token:
          type: string
          title: Access Token
        token_type:
          type: string
          const: Bearer
          title: Token Type
        expires_in:
          type: integer
          title: Expires In
        refresh_token:
          anyOf:
            - type: string
            - type: 'null'
          title: Refresh Token
        scope:
          type: string
          title: Scope
        id_token:
          type: string
          title: Id Token
      type: object
      required:
        - access_token
        - token_type
        - expires_in
        - refresh_token
        - scope
        - id_token
      title: TokenResponse
  securitySchemes:
    access_token:
      type: http
      scheme: bearer
      description: >-
        You can generate an **Organization Access Token** from your
        organization's settings.

````