# Source: https://docs.anchorbrowser.io/api-reference/extensions/get-extension-details.md

# Get Extension Details

> Get details of a specific extension by its ID

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/extensions/{id}
paths:
  path: /v1/extensions/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: The ID of the extension to retrieve
              format: uuid
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
              id:
                allOf:
                  - type: string
                    format: uuid
                    description: Unique identifier for the extension
              name:
                allOf:
                  - type: string
                    description: Extension name
              manifest:
                allOf:
                  - $ref: '#/components/schemas/ExtensionManifest'
              createdAt:
                allOf:
                  - type: string
                    format: date-time
                    description: Timestamp when the extension was created
              updatedAt:
                allOf:
                  - type: string
                    format: date-time
                    description: Timestamp when the extension was last updated
            refIdentifier: '#/components/schemas/ExtensionResponseSchema'
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
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
        description: Extension details retrieved successfully
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
        description: Extension not found
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
        description: Unable to get extension
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

````