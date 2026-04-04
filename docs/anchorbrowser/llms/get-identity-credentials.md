# Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/get-identity-credentials.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Identity Credentials

> Retrieves the credentials for a specific identity. This endpoint returns sensitive credential data.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/identities/{identityId}/credentials
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
  /v1/identities/{identityId}/credentials:
    get:
      tags:
        - Identities (Early Availability)
      summary: Get Identity Credentials
      description: >
        Retrieves the credentials for a specific identity. This endpoint returns
        sensitive credential data.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: identityId
          in: path
          required: true
          description: The ID of the identity
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Identity credentials retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetIdentityCredentialsResponse'
        '404':
          description: Identity not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to get identity credentials
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    GetIdentityCredentialsResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the identity
        name:
          type: string
          description: Name of the identity
        source:
          type: string
          description: Source URL for the identity
        credentials:
          type: array
          items:
            $ref: '#/components/schemas/CredentialData'
          description: Array of credentials with sensitive data
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
    CredentialData:
      oneOf:
        - $ref: '#/components/schemas/UsernamePasswordCredential'
        - $ref: '#/components/schemas/AuthenticatorCredential'
        - $ref: '#/components/schemas/CustomCredential'
      discriminator:
        propertyName: type
    UsernamePasswordCredential:
      title: username_password
      type: object
      required:
        - type
        - username
        - password
      properties:
        type:
          type: string
          enum:
            - username_password
          description: Credential type
        username:
          type: string
          description: Username for authentication
        password:
          type: string
          description: Password for authentication
    AuthenticatorCredential:
      title: authenticator
      type: object
      required:
        - type
        - secret
      properties:
        type:
          type: string
          enum:
            - authenticator
          description: Credential type
        secret:
          type: string
          description: TOTP secret for authenticator
        otp:
          type: string
          description: Optional OTP code
    CustomCredential:
      title: custom
      type: object
      required:
        - type
        - fields
      properties:
        type:
          type: string
          enum:
            - custom
          description: Credential type
        fields:
          type: array
          items:
            $ref: '#/components/schemas/CustomFieldItem'
          description: Array of custom fields
    CustomFieldItem:
      type: object
      required:
        - name
        - value
      properties:
        name:
          type: string
          description: Field name
        value:
          type: string
          description: Field value
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````