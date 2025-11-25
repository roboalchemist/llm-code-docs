# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway.md

# Create Gateway

> `org:gateways:write`


## OpenAPI

````yaml post /gateways
paths:
  path: /gateways
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              domain:
                allOf:
                  - type: string
                    description: Desired name for Gateway subdomain
            example:
              domain: dweb5
        examples:
          example:
            value:
              domain: dweb5
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
                id: 5eb8b151-77b3-4e46-8243-5b6282131a9e
                created_at: '2024-07-12T15:21:47.966866Z'
                domain: dweb3
                restrict: false
                custom_domains: []
                settings:
                  restriction_policies:
                    accessTokens: []
                    allowedHosts: []
                    allowedIPAddresses: []
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````