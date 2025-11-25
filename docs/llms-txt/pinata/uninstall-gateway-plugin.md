# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/uninstall-gateway-plugin.md

# Uninstall Gateway Plugin

> `org:gateways:write`


## OpenAPI

````yaml delete /gateways/plugins/{gateway_id}/plugin/{plugin_id}
paths:
  path: /gateways/plugins/{gateway_id}/plugin/{plugin_id}
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
        gateway_id:
          schema:
            - type: string
              required: true
        plugin_id:
          schema:
            - type: integer
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
              data: null
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````