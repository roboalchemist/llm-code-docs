# Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/create-identity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Identity

> Creates a new identity with credentials for authentication.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/identities
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
  /v1/identities:
    post:
      tags:
        - Identities (Early Availability)
      summary: Create Identity
      description: >
        Creates a new identity with credentials for authentication.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: validateAsync
          in: query
          required: false
          description: Whether to validate the identity asynchronously. Defaults to true.
          schema:
            type: boolean
            default: true
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIdentityRequest'
            examples:
              createIdentityWithPassword:
                summary: Create identity with username/password
                value:
                  name: My Work Account
                  source: https://example.com/login
                  credentials:
                    - type: username_password
                      username: user@example.com
                      password: securepassword123
                  metadata:
                    department: Engineering
              createIdentityWithAuthenticator:
                summary: Create identity with authenticator
                value:
                  name: Two-Factor Account
                  source: https://secure.example.com/login
                  credentials:
                    - type: username_password
                      username: user@example.com
                      password: securepassword123
                    - type: authenticator
                      secret: JBSWY3DPEHPK3PXP
      responses:
        '201':
          description: Identity created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateIdentityResponse'
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to create identity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    CreateIdentityRequest:
      type: object
      required:
        - source
        - credentials
      properties:
        name:
          type: string
          description: >-
            Name of the identity. Defaults to "Unnamed Identity" if not
            provided.
        source:
          type: string
          format: uri
          description: The source URL for the identity (e.g., login page URL)
        credentials:
          type: array
          items:
            $ref: '#/components/schemas/CredentialData'
          description: Array of credentials for authentication
        metadata:
          type: object
          additionalProperties: true
          description: Optional metadata for the identity
        applicationName:
          type: string
          description: Optional application name to associate with the identity
        applicationDescription:
          type: string
          description: Optional application description
    CreateIdentityResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the identity
        name:
          type: string
          description: Name of the identity
        status:
          type: string
          enum:
            - pending
            - validated
            - failed
          description: Status of the identity
        metadata:
          type: object
          additionalProperties: true
          description: Metadata associated with the identity
        created_at:
          type: string
          format: date-time
          description: Timestamp when the identity was created
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