# Source: https://docs.anchorbrowser.io/api-reference/integrations/list-integrations.md

# List Integrations

> Retrieves all integrations for the authenticated team.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/integrations
paths:
  path: /v1/integrations
  method: get
  servers:
    - url: https://api.anchorbrowser.io
      description: API server
  request:
    security:
      - title: api key header
        parameters:
          query: {}
          header:
            anchor-api-key:
              type: apiKey
              description: API key passed in the header
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      integrations:
                        type: array
                        items:
                          $ref: '#/components/schemas/IntegrationItem'
            refIdentifier: '#/components/schemas/IntegrationListResponse'
        examples:
          example:
            value:
              data:
                integrations:
                  - id: 550e8400-e29b-41d4-a716-446655440000
                    name: My 1Password Integration
                    type: 1PASSWORD
                    path: integrations/team-id/550e8400-e29b-41d4-a716-446655440000
                    createdAt: '2024-01-01T00:00:00.000Z'
        description: List of integrations retrieved successfully
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: object
                    properties:
                      code:
                        type: integer
                      message:
                        type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to list integrations
  deprecated: false
  type: path
components:
  schemas:
    IntegrationType:
      type: string
      enum:
        - 1PASSWORD
      description: The type of integration
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

````