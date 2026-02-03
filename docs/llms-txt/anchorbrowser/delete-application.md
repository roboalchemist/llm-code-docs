# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/delete-application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Application

> Deletes an existing application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/applications/{applicationId}
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
  /v1/applications/{applicationId}:
    delete:
      tags:
        - Applications (Early Availability)
      summary: Delete Application
      description: >
        Deletes an existing application.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: applicationId
          in: path
          required: true
          description: The ID of the application to delete
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Application deleted successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteApplicationResponse'
        '404':
          description: Application not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to delete application
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    DeleteApplicationResponse:
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