# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-host-origin-restriction.md

# Create Gateway Host Origin Restriction

> `org:gateways:write`


## OpenAPI

````yaml post /gateways/{id}/hosts
paths:
  path: /gateways/{id}/hosts
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
        id:
          schema:
            - type: string
              required: true
              description: ID of the target Gateway
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              host:
                allOf:
                  - type: string
                    description: Host for target Gateway
            example:
              host: https://ipfs.pinata.cloud
        examples:
          example:
            value:
              host: https://ipfs.pinata.cloud
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
                id: b0165cb6-59e2-476e-aa60-b63b9326bcc6
                value: https://ipfs.pinata.cloud
                createdAt: '2024-07-12T15:40:40.258353687Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````