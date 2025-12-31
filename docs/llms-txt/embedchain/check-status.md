# Source: https://docs.embedchain.ai/examples/rest-api/check-status.md

# Check status

> Endpoint to check the status of the API

## OpenAPI

````yaml get /ping
paths:
  path: /ping
  method: get
  request:
    security: []
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
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas: {}

````