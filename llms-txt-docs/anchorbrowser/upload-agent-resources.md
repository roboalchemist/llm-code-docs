# Source: https://docs.anchorbrowser.io/api-reference/agentic-capabilities/upload-agent-resources.md

# Upload Agent Resources

> Upload files as agent resources to a browser session using multipart/form-data. 
If you upload a ZIP file, it will be automatically extracted and the files will be made available as agent resources.
If you upload a single file, it will be saved directly as an agent resource.
Resources are then accessible to AI agents for task completion and automation.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/agent/files
paths:
  path: /v1/sessions/{sessionId}/agent/files
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
    body:
      multipart/form-data:
        schemaArray:
          - type: object
            properties:
              file:
                allOf:
                  - type: string
                    format: binary
                    description: >-
                      File to upload as agent resource (ZIP files will be
                      extracted automatically)
            required: true
            requiredProperties:
              - file
        examples:
          example:
            value: {}
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
                      status:
                        type: string
                      message:
                        type: string
        examples:
          example:
            value:
              data:
                status: <string>
                message: <string>
        description: Agent resources uploaded successfully
    '400':
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
        examples:
          example:
            value:
              error:
                code: 123
                message: <string>
        description: Invalid request (no resource uploaded or file too large)
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
        description: Failed to upload or process agent resources
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