# Source: https://docs.anchorbrowser.io/api-reference/integrations/list-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# List Integrations

> Retrieves all integrations for the authenticated team.



## OpenAPI

````yaml openapi-mintlify.yaml get /v1/integrations
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
  /v1/integrations:
    get:
      tags:
        - Integrations
      summary: List Integrations
      description: Retrieves all integrations for the authenticated team.
      responses:
        '200':
          description: List of integrations retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IntegrationListResponse'
        '500':
          description: Failed to list integrations
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    IntegrationListResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            integrations:
              type: array
              items:
                $ref: '#/components/schemas/IntegrationItem'
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
    IntegrationItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique integration ID
          example: 550e8400-e29b-41d4-a716-446655440000
        name:
          type: string
          description: Integration name
          example: My 1Password Integration
        type:
          $ref: '#/components/schemas/IntegrationType'
        path:
          type: string
          description: Storage path for the integration
          example: integrations/team-id/550e8400-e29b-41d4-a716-446655440000
        createdAt:
          type: string
          format: date-time
          description: Timestamp when the integration was created
          example: '2024-01-01T00:00:00.000Z'
    IntegrationType:
      type: string
      enum:
        - 1PASSWORD
      description: The type of integration
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````