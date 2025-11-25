# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/install-gateway-plugin.md

# Install Gateway Plugin

> `org:gateways:write`


## OpenAPI

````yaml post /gateways/plugins/{gateway_id}
paths:
  path: /gateways/plugins/{gateway_id}
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              plugin_id:
                allOf:
                  - type: number
                    description: ID of the plugin to install to target gateway
            example:
              plugin_id: 1
        examples:
          example:
            value:
              plugin_id: 1
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
                      gateway_id:
                        type: string
                      plugin_id:
                        type: number
        examples:
          example:
            value:
              data:
                gateway_id: 3ced949f-2013-47a0-8f4a-f8d8e8ee14ac
                plugin_id: 1
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````