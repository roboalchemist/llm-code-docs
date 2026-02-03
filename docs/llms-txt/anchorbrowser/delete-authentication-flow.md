# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/delete-authentication-flow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Authentication Flow

> Deletes an existing authentication flow.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/applications/{applicationId}/auth-flows/{authFlowId}
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
    delete:
      tags:
        - Applications (Early Availability)
      summary: Delete Authentication Flow
      description: >
        Deletes an existing authentication flow.


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
          description: The ID of the authentication flow to delete
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: authentication flow deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteAuthFlowResponse'
        '500':
          description: Failed to delete authentication flow
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    DeleteAuthFlowResponse:
      type: object
      properties:
        success:
          type: boolean
          description: Whether the deletion was successful
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