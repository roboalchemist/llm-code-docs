# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-application-authentication-flows.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Application Authentication Flows

> Retrieves all authentication flows for a specific application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/applications/{applicationId}/auth-flows
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
    get:
      tags:
        - Applications (Early Availability)
      summary: List Application Authentication Flows
      description: >
        Retrieves all authentication flows for a specific application.


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
      responses:
        '200':
          description: List of authentication flows retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListApplicationAuthFlowsResponse'
        '500':
          description: Failed to list application authentication flows
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ListApplicationAuthFlowsResponse:
      type: object
      properties:
        auth_flows:
          type: array
          items:
            $ref: '#/components/schemas/AuthFlowItem'
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
    AuthFlowItem:
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