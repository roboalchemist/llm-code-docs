# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/get-browser-session-pages.md

# Get Browser Session Pages

> Retrieves a list of pages associated with a specific browser session.

## OpenAPI

````yaml openapi-mintlify.yaml get /v1/sessions/{session_id}/pages
paths:
  path: /v1/sessions/{session_id}/pages
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
              description: The ID of the session to retrieve pages for.
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    id:
                      type: string
                      description: The unique identifier of the page.
                    title:
                      type: string
                      description: The title of the page.
                    url:
                      type: string
                      description: The URL of the page.
                    frontend_url:
                      type: string
                      description: The frontend URL for accessing the page.
                  required:
                    - id
                    - title
                    - url
                    - frontend_url
        examples:
          example:
            value:
              - id: <string>
                title: <string>
                url: <string>
                frontend_url: <string>
        description: Session pages retrieved successfully.
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
        description: Invalid API Key or unauthorized access.
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
        description: Internal server error.
  deprecated: false
  type: path
components:
  schemas: {}

````