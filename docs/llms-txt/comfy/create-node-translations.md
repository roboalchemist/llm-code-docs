# Source: https://docs.comfy.org/api-reference/registry/create-node-translations.md

# Create Node Translations

## OpenAPI

````yaml https://api.comfy.org/openapi post /nodes/{nodeId}/translations
paths:
  path: /nodes/{nodeId}/translations
  method: post
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path:
        nodeId:
          schema:
            - type: string
              required: true
              description: The unique identifier of the node.
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - additionalProperties:
                      additionalProperties: true
                      type: object
                    type: object
            required: true
        examples:
          example:
            value:
              data: {}
  response:
    '201':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Detailed information about a specific node
        examples: {}
        description: Detailed information about a specific node
    '400':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Bad Request
        examples: {}
        description: Bad Request
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - description: >-
                      Optional detailed information about the error or hints for
                      resolving it.
                    items:
                      type: string
                    type: array
              message:
                allOf:
                  - description: A clear and concise description of the error.
                    type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              details:
                - <string>
              message: <string>
        description: Node version not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
              message:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ErrorResponse'
            requiredProperties:
              - error
              - message
        examples:
          example:
            value:
              error: <string>
              message: <string>
        description: Internal server error
  deprecated: false
  type: path
components:
  schemas: {}

````