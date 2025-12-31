# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-ip-address-restriction.md

# Create Gateway IP Address Restriction

> `org:gateways:write`


## OpenAPI

````yaml post /gateways/{id}/ips
paths:
  path: /gateways/{id}/ips
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
              ip:
                allOf:
                  - type: string
                    description: IP for the target Gateway
            example:
              ip: 1.1.1.1
        examples:
          example:
            value:
              ip: 1.1.1.1
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
                id: 66b6f3c5-2733-442b-a558-960be4b5a921
                value: 1.1.1.1
                createdAt: '2024-07-12T15:37:04.871996078Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````