# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/resume-session-recording.md

# Resume Session Recording

> Resumes the video recording for the specified browser session.

## OpenAPI

````yaml openapi-mintlify.yaml post /v1/sessions/{session_id}/recordings/resume
paths:
  path: /v1/sessions/{session_id}/recordings/resume
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
        session_id:
          schema:
            - type: string
              required: true
              description: The ID of the browser session for which to resume recording.
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
                  - $ref: '#/components/schemas/SuccessResponse'
        examples:
          example:
            value:
              data:
                data:
                  status: <string>
        description: Recording resumed successfully.
    '401':
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
        description: Invalid API Key.
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
        description: Session not found.
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
        description: Failed to resume recording.
  deprecated: false
  type: path
components:
  schemas:
    SuccessResponse:
      type: object
      properties:
        data:
          type: object
          properties:
            status:
              type: string
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