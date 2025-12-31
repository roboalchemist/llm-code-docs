# Source: https://docs.anchorbrowser.io/api-reference/integrations/create-integration.md

# Create Integration

> Creates a new integration with a third-party service like 1Password. 
The integration can then be used in browser sessions to automatically load secrets and credentials.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/integrations
paths:
  path: /v1/integrations
  method: post
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
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    minLength: 1
                    description: Name for the integration
                    example: My 1Password Integration
              type:
                allOf:
                  - $ref: '#/components/schemas/IntegrationType'
              credentials:
                allOf:
                  - $ref: '#/components/schemas/ServiceAccountCredentials'
            required: true
            refIdentifier: '#/components/schemas/CreateIntegrationRequest'
            requiredProperties:
              - name
              - type
              - credentials
        examples:
          onePasswordIntegration:
            summary: Create a 1Password integration
            value:
              name: My 1Password Integration
              type: 1PASSWORD
              credentials:
                type: serviceAccount
                data:
                  serviceAccount: ops_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
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
                      integration:
                        $ref: '#/components/schemas/IntegrationItem'
            refIdentifier: '#/components/schemas/IntegrationResponse'
        examples:
          example:
            value:
              data:
                integration:
                  id: 550e8400-e29b-41d4-a716-446655440000
                  name: My 1Password Integration
                  type: 1PASSWORD
                  path: integrations/team-id/550e8400-e29b-41d4-a716-446655440000
                  createdAt: '2024-01-01T00:00:00.000Z'
        description: Integration created successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: object
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
        description: Invalid request or validation failed
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Failed to create integration
  deprecated: false
  type: path
components:
  schemas:
    IntegrationType:
      type: string
      enum:
        - 1PASSWORD
      description: The type of integration
    ServiceAccountCredentials:
      type: object
      required:
        - type
        - data
      properties:
        type:
          type: string
          enum:
            - serviceAccount
          description: Credential type
        data:
          type: object
          required:
            - serviceAccount
          properties:
            serviceAccount:
              type: string
              description: Service account token
              example: ops_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
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