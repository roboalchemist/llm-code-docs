# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-gateway-key.md

# Revoke Gateway Key

> `org:gateways:write`


## OpenAPI

````yaml delete /gateways/{id}/access_tokens/{access_token_id}
paths:
  path: /gateways/{id}/access_tokens/{access_token_id}
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
        access_token_id:
          schema:
            - type: string
              required: true
              description: ID of the target Gateway Key
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