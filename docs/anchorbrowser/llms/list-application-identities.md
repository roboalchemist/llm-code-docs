# Source: https://docs.anchorbrowser.io/api-reference/applications-early-availability/list-application-identities.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Application Identities

> Retrieves all identities associated with a specific application.

**Beta** Capability. [Contact support](mailto:support@anchorbrowser.io) to enable.




## OpenAPI

````yaml openapi-mintlify.yaml get /v1/applications/{applicationId}/identities
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
  /v1/applications/{applicationId}/identities:
    get:
      tags:
        - Applications (Early Availability)
      summary: List Application Identities
      description: >
        Retrieves all identities associated with a specific application.


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
        - name: search
          in: query
          required: false
          description: Search query to filter identities by name
          schema:
            type: string
      responses:
        '200':
          description: List of identities retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListApplicationIdentitiesResponse'
        '500':
          description: Failed to list application identities
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    ListApplicationIdentitiesResponse:
      type: object
      properties:
        identities:
          type: array
          items:
            $ref: '#/components/schemas/ApplicationIdentityItem'
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
    ApplicationIdentityItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the identity
        name:
          type: string
          description: Name of the identity
        auth_flow:
          type: string
          nullable: true
          description: Authentication flow associated with this identity
        status:
          type: string
          enum:
            - pending
            - validated
            - failed
          description: Status of the identity
        created_at:
          type: string
          format: date-time
          description: Timestamp when the identity was created
        updated_at:
          type: string
          format: date-time
          description: Timestamp when the identity was last updated
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````