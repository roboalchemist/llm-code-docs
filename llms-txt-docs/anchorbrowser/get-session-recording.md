# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/get-session-recording.md

# Get Session Recording

> Downloads the primary recording file for the specified browser session. Returns the recording as an MP4 file.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings/primary/fetch
paths:
  path: /v1/sessions/{session_id}/recordings/primary/fetch
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
        session_id:
          schema:
            - type: string
              required: true
              description: The ID of the browser session to download the recording for.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      video/mp4:
        schemaArray:
          - type: file
            contentEncoding: binary
        examples:
          example: {}
        description: The browser session recording file
    '401':
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
        description: Invalid API Key - Authentication failed or API key is missing.
    '404':
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
        description: Recording not found
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
        description: Internal Server Error
  deprecated: false
  type: path
components:
  schemas: {}

````