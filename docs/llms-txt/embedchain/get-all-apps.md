# Source: https://docs.embedchain.ai/examples/rest-api/get-all-apps.md

# Get all apps

> Get all applications

## OpenAPI

````yaml get /apps
paths:
  path: /apps
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