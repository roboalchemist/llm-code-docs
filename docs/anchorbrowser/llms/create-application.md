# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/create-application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Application

> Creates a new application for identity management.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/applications
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
  /v1/applications:
    post:
      tags:
        - Applications (Early Availability)
      summary: Create Application
      description: >
        Creates a new application for identity management.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateApplicationRequest'
            examples:
              createApplication:
                summary: Create a new application
                value:
                  source: https://example.com
                  name: Example App
                  description: An example application
      responses:
        '201':
          description: Application created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateApplicationResponse'
        '400':
          description: Invalid request parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to create application
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    CreateApplicationRequest:
      type: object
      required:
        - source
      properties:
        source:
          type: string
          format: uri
          description: The source URL of the application
        name:
          type: string
          description: Name of the application
        description:
          type: string
          description: Description of the application
    CreateApplicationResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the application
        name:
          type: string
          description: Name of the application
        url:
          type: string
          nullable: true
          description: URL of the application
        description:
          type: string
          nullable: true
          description: Description of the application
        created_at:
          type: string
          format: date-time
          description: Timestamp when the application was created
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