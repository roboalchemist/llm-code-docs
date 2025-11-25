# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-gateway-plugins.md

# List Gateway Plugins

> `org:gateways:read`


## OpenAPI

````yaml get /gateways/plugins
paths:
  path: /gateways/plugins
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
                  - type: array
                    items:
                      type: object
                      properties:
                        gateway_id:
                          type: string
                        plugin_id:
                          type: number
        examples:
          example:
            value:
              data:
                - gateway_id: 2bfaa2ae-b590-4cb4-bb9c-5af43c2c9541
                  plugin_id: 1
                - gateway_id: 2bfaa2ae-b590-4cb4-bb9c-5af43c2c9541
                  plugin_id: 2
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````