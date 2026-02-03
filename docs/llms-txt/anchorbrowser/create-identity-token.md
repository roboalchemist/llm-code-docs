# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-identity-token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Identity Token

> Creates an identity token for a specific application. This token is used to initiate
an authentication flow for linking user identities to the application.

The callback URL must use HTTPS and is where the user will be redirected after authentication.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/applications/{applicationId}/tokens
openapi: 3.1.0
info:
  title: AnchorBrowser API
  version: 1.0.0
  description: APIs to manage all browser-related actions and configuration.
servers:
  - url: https://api.anchorbrowser.io
    description: API server
security: []
paths:
  /v1/applications/{applicationId}/tokens:
    post:
      tags:
        - Applications (Early Availability)
      summary: Create Identity Token
      description: >
        Creates an identity token for a specific application. This token is used
        to initiate

        an authentication flow for linking user identities to the application.


        The callback URL must use HTTPS and is where the user will be redirected
        after authentication.
      parameters:
        - name: applicationId
          in: path
          required: true
          description: The unique identifier of the application
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIdentityTokenRequest'
            examples:
              createToken:
                summary: Create an identity token
                value:
                  callbackUrl: https://example.com/auth/callback
      responses:
        '201':
          description: Identity token created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IdentityTokenResponse'
        '400':
          description: Invalid request - callbackUrl must be a valid HTTPS URL
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Application not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to create identity token
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    CreateIdentityTokenRequest:
      type: object
      required:
        - callbackUrl
      properties:
        callbackUrl:
          type: string
          format: uri
          description: >-
            The HTTPS URL where the user will be redirected after
            authentication. Must use HTTPS protocol.
          example: https://example.com/callback
    IdentityTokenResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            token:
              type: string
              description: The generated identity token for authentication
            expires_at:
              type: string
              format: date-time
              description: The timestamp when the token expires
            token_hash:
              type: string
              description: A hash of the token for verification purposes
    ErrorResponse:
      type: object
      properties:
        error:
          type: object
          properties:
            code:
              type: integer
            message:
              type: string
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````