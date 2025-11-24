# Source: https://docs.anchorbrowser.io/api-reference/extensions/upload-extension.md

# Upload Extension

> Upload a new browser extension as a ZIP file. The extension will be validated and stored for use in browser sessions.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/extensions
paths:
  path: /v1/extensions
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
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: User-friendly name for the extension (1-255 characters)
              file:
                allOf:
                  - type: string
                    format: binary
                    description: ZIP file containing the browser extension
            required: true
            requiredProperties:
              - name
              - file
        examples:
          example:
            value:
              name: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - $ref: '#/components/schemas/ExtensionResponseSchema'
        examples:
          example:
            value:
              data:
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
        description: Extension uploaded successfully
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
        description: Invalid request or extension validation failed
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
        description: Unable to upload extension
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