# Source: https://docs.anchorbrowser.io/api-reference/integrations/create-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Integration

> Creates a new integration with a third-party service like 1Password. 
The integration can then be used in browser sessions to automatically load secrets and credentials.




## OpenAPI

````yaml openapi-mintlify.yaml post /v1/integrations
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
    post:
      tags:
        - Integrations
      summary: Create Integration
      description: >
        Creates a new integration with a third-party service like 1Password. 

        The integration can then be used in browser sessions to automatically
        load secrets and credentials.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateIntegrationRequest'
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
      responses:
        '200':
          description: Integration created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/IntegrationResponse'
        '400':
          description: Invalid request or validation failed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to create integration
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
    CreateIntegrationRequest:
      type: object
      required:
        - name
        - type
        - credentials
      properties:
        name:
          type: string
          minLength: 1
          description: Name for the integration
          example: My 1Password Integration
        type:
          $ref: '#/components/schemas/IntegrationType'
        credentials:
          $ref: '#/components/schemas/ServiceAccountCredentials'
    IntegrationResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            integration:
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
  securitySchemes:
    api_key_header:
      type: apiKey
      in: header
      name: anchor-api-key
      description: API key passed in the header

````