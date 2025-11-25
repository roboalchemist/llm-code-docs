# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-key-restriction.md

# Create Gateway Key Restriction

> `org:gateways:write`


## OpenAPI

````yaml post /gateways/{id}/access_tokens
paths:
  path: /gateways/{id}/access_tokens
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
                id: e8fe078b-38e8-4472-94e7-9023205232d2
                value: key
                createdAt: '2024-07-12T15:34:59.786198063Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````