# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/upload-files.md

# Upload Files

> Upload files directly to a browser session for use with web forms and file inputs.

Files are saved to the session's uploads directory and can be referenced in CDP commands.


## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{sessionId}/uploads
paths:
  path: /v1/sessions/{sessionId}/uploads
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
                    description: File to upload to the browser session
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
        description: File uploaded successfully
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
        description: Invalid request (no file uploaded or file too large)
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
        description: Failed to upload file
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