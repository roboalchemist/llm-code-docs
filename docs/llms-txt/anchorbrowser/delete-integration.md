# Source: https://docs.anchorbrowser.io/api-reference/integrations/delete-integration.md

# Delete Integration

> Deletes an existing integration and removes its stored credentials.

## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/integrations/{integrationId}
paths:
  path: /v1/integrations/{integrationId}
  method: delete
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
      path:
        integrationId:
          schema:
            - type: string
              required: true
              description: The ID of the integration to delete
              format: uuid
              example: 550e8400-e29b-41d4-a716-446655440000
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
        examples:
          example:
            value:
              data:
                integration:
                  id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  deleted: true
                  path: <string>
        description: Integration deleted successfully
    '404':
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
        description: Integration not found
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
        description: Failed to delete integration
  deprecated: false
  type: path
components:
  schemas: {}

````