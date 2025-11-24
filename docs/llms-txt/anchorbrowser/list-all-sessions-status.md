# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/list-all-sessions-status.md

# List All Sessions Status

> Retrieves status information for all browser sessions associated with the API key.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/all/status
paths:
  path: /v1/sessions/all/status
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
                  - type: object
                    properties:
                      count:
                        type: integer
                        description: Total number of browser sessions
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/SessionStatus'
            refIdentifier: '#/components/schemas/SessionListResponse'
        examples:
          example:
            value:
              data:
                count: 123
                items:
                  - session_id: <string>
                    status: <string>
                    created_at: '2023-11-07T05:31:56Z'
        description: Successfully retrieved status for all browser sessions
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
        description: Invalid API Key
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
  schemas:
    SessionStatus:
      type: object
      properties:
        session_id:
          type: string
          description: Unique identifier for the browser session
        status:
          type: string
          description: Current status of the browser session
        created_at:
          type: string
          format: date-time
          description: Timestamp when the browser session was created
      required:
        - session_id
        - status
        - created_at

````