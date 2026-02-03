# Source: https://docs.anchorbrowser.io/api-reference/identities-early-availability/update-identity.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Identity

> Updates an existing identity's name, metadata, or credentials.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml put /v1/identities/{identityId}
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
  /v1/identities/{identityId}:
    put:
      tags:
        - Identities (Early Availability)
      summary: Update Identity
      description: >
        Updates an existing identity's name, metadata, or credentials.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: identityId
          in: path
          required: true
          description: The ID of the identity to update
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateIdentityRequest'
            examples:
              updateIdentityName:
                summary: Update identity name
                value:
                  name: Updated Account Name
              updateIdentityCredentials:
                summary: Update identity credentials
                value:
                  credentials:
                    - type: username_password
                      username: newuser@example.com
                      password: newpassword123
      responses:
        '200':
          description: Identity updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateIdentityResponse'
        '404':
          description: Identity not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to update identity
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    UpdateIdentityRequest:
      type: object
      properties:
        name:
          type: string
          description: Name of the identity
        metadata:
          type: object
          additionalProperties: true
          description: Metadata for the identity
        credentials:
          type: array
          items:
            $ref: '#/components/schemas/CredentialData'
          description: Array of credentials for authentication
    UpdateIdentityResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the identity
        name:
          type: string
          description: Name of the identity
        metadata:
          type: object
          additionalProperties: true
          description: Metadata associated with the identity
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the identity was last updated
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