# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-authentication-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Authentication Flow

> Creates a new authentication flow for an application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/applications/{applicationId}/auth-flows
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
  /v1/applications/{applicationId}/auth-flows:
    post:
      tags:
        - Applications (Early Availability)
      summary: Create Authentication Flow
      description: >
        Creates a new authentication flow for an application.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: applicationId
          in: path
          required: true
          description: The ID of the application
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateAuthFlowRequest'
            examples:
              createAuthFlow:
                summary: Create an authentication flow with username/password
                value:
                  name: Standard Login
                  description: Username and password authentication
                  is_recommended: true
                  methods:
                    - username_password
                  custom_fields: []
      responses:
        '201':
          description: authentication flow created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateAuthFlowResponse'
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to create authentication flow
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    CreateAuthFlowRequest:
      type: object
      required:
        - name
        - methods
      properties:
        name:
          type: string
          description: Name of the authentication flow
        description:
          type: string
          description: Description of the authentication flow
        is_recommended:
          type: boolean
          description: Whether this is the recommended authentication flow
        methods:
          type: array
          items:
            type: string
            enum:
              - username_password
              - authenticator
              - custom
          minItems: 1
          description: Authentication methods in this flow
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/CustomFieldDefinition'
          description: Custom fields for this authentication flow
    CreateAuthFlowResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the authentication flow
        name:
          type: string
          description: Name of the authentication flow
        description:
          type: string
          nullable: true
          description: Description of the authentication flow
        is_recommended:
          type: boolean
          description: Whether this is the recommended authentication flow
        methods:
          type: array
          items:
            type: string
          description: Authentication methods in this flow
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/CustomFieldDefinition'
          description: Custom fields for this authentication flow
        created_at:
          type: string
          format: date-time
          description: Timestamp when the authentication flow was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the authentication flow was last updated
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
    CustomFieldDefinition:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Name of the custom field
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````