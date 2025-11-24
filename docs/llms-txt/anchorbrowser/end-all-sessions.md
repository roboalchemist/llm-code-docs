# Source: https://docs.anchorbrowser.io/api-reference/browser-sessions/end-all-sessions.md

# End All Sessions

> Terminates all active browser sessions associated with the provided API key.

## OpenAPI

````yaml openapi-mintlify.yaml delete /v1/sessions/all
paths:
  path: /v1/sessions/all
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
                      status:
                        type: string
            refIdentifier: '#/components/schemas/SuccessResponse'
        examples:
          example:
            value:
              data:
                status: <string>
        description: Successfully terminated all active browser sessions.
  deprecated: false
  type: path
components:
  schemas: {}

````