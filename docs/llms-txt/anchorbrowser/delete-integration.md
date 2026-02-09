# Source: https://docs.anchorbrowser.io/api-reference/integrations/delete-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.anchorbrowser.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Integration

> Deletes an existing integration and removes its stored credentials.



## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/integrations/{integrationId}
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
  /v1/integrations/{integrationId}:
    delete:
      tags:
        - Integrations
      summary: Delete Integration
      description: Deletes an existing integration and removes its stored credentials.
      parameters:
        - name: integrationId
          in: path
          required: true
          description: The ID of the integration to delete
          schema:
            type: string
            format: uuid
            example: 550e8400-e29b-41d4-a716-446655440000
      responses:
        '200':
          description: Integration deleted successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      integration:
                        type: object
                        properties:
                          id:
                            type: string
                            format: uuid
                          deleted:
                            type: boolean
                          path:
                            type: string
        '404':
          description: Integration not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to delete integration
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
      security:
        - api_key_header: []
components:
  schemas:
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