# Source: https://docs.pinata.cloud/api-reference/endpoint/cancel-pin-by-cid.md

# Cancel Request

> `org:files:write`


## OpenAPI

````yaml DELETE /files/public/pin_by_cid/{id}
paths:
  path: /files/public/pin_by_cid/{id}
  method: delete
  servers:
    - url: https://api.pinata.cloud/v3
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: ID of the pin_by_cid request
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties: {}
            example:
              data: null
        examples:
          example:
            value:
              data: null
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````