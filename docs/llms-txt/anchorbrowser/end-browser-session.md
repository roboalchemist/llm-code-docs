# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-browser-session.md

# End Browser Session

> Deletes the browser session associated with the provided browser session ID. Requires a valid API key for authentication.

## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/sessions/{session_id}
paths:
  path: /v1/sessions/{session_id}
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
        session_id:
          schema:
            - type: string
              required: true
              description: The ID of the browser session to end.
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
                      status:
                        type: string
            refIdentifier: '#/components/schemas/SuccessResponse'
        examples:
          example:
            value:
              data:
                status: <string>
        description: Browser session ended successfully.
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
        description: Invalid API Key or browser session ID
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