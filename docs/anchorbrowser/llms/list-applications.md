# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-applications.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Applications

> Retrieves all applications for the authenticated team.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/applications
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
    get:
      tags:
        - Applications (Early Availability)
      summary: List Applications
      description: >
        Retrieves all applications for the authenticated team.


        **Beta** Capability. [Contact support](mailto:support@anchorbrowser.io)
        to enable.
      parameters:
        - name: search
          in: query
          required: false
          description: Search query to filter applications by name
          schema:
            type: string
      responses:
        '200':
          description: List of applications retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListApplicationsResponse'
        '500':
          description: Failed to list applications
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ListApplicationsResponse:
      type: object
      properties:
        applications:
          type: array
          items:
            $ref: '#/components/schemas/ApplicationItem'
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
    ApplicationItem:
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
        identity_count:
          type: integer
          description: Number of identities associated with this application
        auth_methods:
          type: array
          items:
            type: string
          description: Authentication methods available for this application
        allowed_domains:
          type: array
          items:
            type: string
          description: List of allowed domains for this application
        created_at:
          type: string
          format: date-time
          description: Timestamp when the application was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the application was last updated
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````