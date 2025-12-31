# Source: https://docs.datafold.com/api-reference/bi/list-all-integrations.md

# List all integrations

> Return all integrations for Mode/Tableau/Looker

## OpenAPI

````yaml get /api/v1/lineage/bi/
paths:
  path: /api/v1/lineage/bi/
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
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