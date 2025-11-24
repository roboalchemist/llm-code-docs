# Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/list-agent-resources.md

# List Agent Resources

> List all resources that have been uploaded to the browser session for agent use.
Returns resource metadata including name, size, type, and last modified timestamp.


## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{sessionId}/agent/files
paths:
  path: /v1/sessions/{sessionId}/agent/files
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
        sessionId:
          schema:
            - type: string
              required: true
              description: The browser session ID
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
              data:
                allOf:
                  - type: object
                    properties:
                      files:
                        type: array
                        items:
                          type: object
                          properties:
                            name:
                              type: string
                              description: The resource name
                            size:
                              type: integer
                              description: Resource size in bytes
                            type:
                              type: string
                              description: Resource extension/type
                            lastModified:
                              type: string
                              format: date-time
                              description: When the resource was last modified
        examples:
          example:
            value:
              data:
                files:
                  - name: <string>
                    size: 123
                    type: <string>
                    lastModified: '2023-11-07T05:31:56Z'
        description: Agent resources listed successfully
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - $ref: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                error:
                  code: 123
                  message: <string>
        description: Session is not running
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - $ref: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                error:
                  code: 123
                  message: <string>
        description: Session not found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - $ref: '#/components/schemas/ErrorResponse'
        examples:
          example:
            value:
              error:
                error:
                  code: 123
                  message: <string>
        description: Failed to list agent resources
  deprecated: false
  type: path
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

````