# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/update-authentication-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Authentication Flow

> Updates an existing authentication flow.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml patch /v1/applications/{applicationId}/auth-flows/{authFlowId}
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
  /v1/applications/{applicationId}/auth-flows/{authFlowId}:
    patch:
      tags:
        - Applications (Early Availability)
      summary: Update Authentication Flow
      description: >
        Updates an existing authentication flow.


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
        - name: authFlowId
          in: path
          required: true
          description: The ID of the authentication flow to update
          schema:
            type: string
            format: uuid
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateAuthFlowRequest'
            examples:
              updateAuthFlow:
                summary: Update authentication flow name and methods
                value:
                  name: Updated Login Flow
                  methods:
                    - username_password
                    - authenticator
      responses:
        '200':
          description: authentication flow updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateAuthFlowResponse'
        '500':
          description: Failed to update authentication flow
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    UpdateAuthFlowRequest:
      type: object
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
          description: Authentication methods in this flow
        custom_fields:
          type: array
          items:
            $ref: '#/components/schemas/CustomFieldDefinition'
          description: Custom fields for this authentication flow
    UpdateAuthFlowResponse:
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