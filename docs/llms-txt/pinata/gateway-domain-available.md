# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-domain-available.md

# Gateway Domain Available

> `org:gateways:read`


## OpenAPI

````yaml get /gateways/exists/{domain}
paths:
  path: /gateways/exists/{domain}
  method: get
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
        domain:
          schema:
            - type: string
              required: true
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
        examples:
          example:
            value:
              data:
                exists: true
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````