# Source: https://docs.anchorbrowser.io/api-reference/extensions/list-extensions.md

# List Extensions

> Get all extensions for the authenticated user

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/extensions
paths:
  path: /v1/extensions
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
                  - type: array
                    items:
                      $ref: '#/components/schemas/ExtensionResponseSchema'
            refIdentifier: '#/components/schemas/ExtensionListResponse'
        examples:
          example:
            value:
              data:
                - id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
                  name: <string>
                  manifest:
                    name: <string>
                    version: <string>
                    manifest_version: 123
                    description: <string>
                    permissions:
                      - <string>
                  createdAt: '2023-11-07T05:31:56Z'
                  updatedAt: '2023-11-07T05:31:56Z'
        description: List of user extensions retrieved successfully
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
        description: Unable to list extensions
  deprecated: false
  type: path
components:
  schemas:
    ExtensionManifest:
      type: object
      properties:
        name:
          type: string
        version:
          type: string
        manifest_version:
          type: integer
        description:
          type: string
        permissions:
          type: array
          items:
            type: string
      additionalProperties: true
    ExtensionResponseSchema:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the extension
        name:
          type: string
          description: Extension name
        manifest:
          $ref: '#/components/schemas/ExtensionManifest'
        createdAt:
          type: string
          format: date-time
          description: Timestamp when the extension was created
        updatedAt:
          type: string
          format: date-time
          description: Timestamp when the extension was last updated

````