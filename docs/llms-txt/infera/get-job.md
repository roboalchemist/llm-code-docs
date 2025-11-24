# Source: https://docs.infera.org/api-reference/endpoint/get-job.md

# Get Job

## OpenAPI

````yaml get /worker/get_job
paths:
  path: /worker/get_job
  method: get
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
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