# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-host-origin-restriction.md

# Revoke Host Origin Restriction

> `org:gateways:write`


## OpenAPI

````yaml delete /gateways/{id}/hosts/{host_id}
paths:
  path: /gateways/{id}/hosts/{host_id}
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
              description: ID of the target Gateway
        host_id:
          schema:
            - type: string
              required: true
              description: ID of the target host restriction
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