# Source: https://docs.anchorbrowser.io/api-reference/session-recordings/list-session-recordings.md

# List Session Recordings

> Retrieves the URLs of the browser session's video recordings. Requires a valid API key for authentication.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/recordings
paths:
  path: /v1/sessions/{session_id}/recordings
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
              description: The ID of the browser session to retrieve recordings for.
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
                        description: Total number of video recordings
                      items:
                        type: array
                        items:
                          $ref: '#/components/schemas/RecordingItem'
            refIdentifier: '#/components/schemas/RecordingListResponse'
        examples:
          example:
            value:
              data:
                count: 123
                items:
                  - id: <string>
                    is_primary: true
                    file_link: <string>
                    suggested_file_name: <string>
                    duration: <string>
                    size: 123
                    created_at: '2023-11-07T05:31:56Z'
        description: A set of recording URLs associated with the browser session.
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
        description: Invalid API Key.
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
        description: Session recordings not found.
    '429':
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
        description: Too many requests, please try again later.
  deprecated: false
  type: path
components:
  schemas:
    RecordingItem:
      type: object
      properties:
        id:
          type: string
          description: Unique identifier for the recording
        is_primary:
          type: boolean
          description: Indicates if this is the primary recording
        file_link:
          type: string
          description: URL to access the recording file
        suggested_file_name:
          type: string
          description: Suggested filename for the recording
        duration:
          type: string
          description: Duration of the recording
        size:
          type: number
          description: Size of the recording file in bytes
        created_at:
          type: string
          format: date-time
          description: Timestamp when the recording was created

````