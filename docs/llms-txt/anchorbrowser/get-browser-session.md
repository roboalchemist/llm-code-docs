# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session.md

# Get Browser Session

> Retrieves detailed information about a specific browser session.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}
paths:
  path: /v1/sessions/{session_id}
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
              description: The ID of the session to retrieve.
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
              session_id:
                allOf:
                  - type: string
                    description: The unique identifier of the session.
              team_id:
                allOf:
                  - type: string
                    description: The team ID associated with the session.
              duration:
                allOf:
                  - type: integer
                    description: The duration of the session in seconds.
              status:
                allOf:
                  - type: string
                    description: The current status of the session.
              credits_used:
                allOf:
                  - type: number
                    description: The number of credits consumed by the session.
              configuration:
                allOf:
                  - type: object
                    description: The configuration settings for the session.
              playground:
                allOf:
                  - type: boolean
                    description: Whether this is a playground session.
              proxy_bytes:
                allOf:
                  - type: integer
                    description: The number of bytes transferred through the proxy.
              tokens:
                allOf:
                  - type: object
                    description: Token usage information.
              steps:
                allOf:
                  - type: array
                    items:
                      type: object
                    description: Array of steps executed in the session.
              tags:
                allOf:
                  - type: object
                    description: Tags associated with the session.
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    description: The timestamp when the session was created.
        examples:
          example:
            value:
              session_id: <string>
              team_id: <string>
              duration: 123
              status: <string>
              credits_used: 123
              configuration: {}
              playground: true
              proxy_bytes: 123
              tokens: {}
              steps:
                - {}
              tags: {}
              created_at: '2023-11-07T05:31:56Z'
        description: Session retrieved successfully.
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
        description: Session not found.
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
        description: Failed to fetch session.
  deprecated: false
  type: path
components:
  schemas: {}

````