# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-details.md

# Gateway Details

> `org:gateways:read`


## OpenAPI

````yaml get /gateways/{id}
paths:
  path: /gateways/{id}
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
                id: 01dae16b-699c-472a-a61e-975a7b9777bd
                created_at: '2023-01-24T19:51:17.493Z'
                domain: restricted-example
                restrict: false
                custom_domains:
                  - domain: ipfs.pinata.cloud
                    domain_validation_status: pending
                    custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                    ssl_validation_status: initializing
                settings:
                  restriction_policies:
                    accessTokens:
                      - id: d199be6a-3bee-461b-b7fb-e1225eafe28e
                        value: key
                        createdAt: '2024-07-12T15:09:47.564042199Z'
                    allowedHosts:
                      - id: 8934893a-093c-4d3a-9cd8-2c034a7f4fb8
                        value: https://ipfs.pinata.cloud
                        createdAt: '2024-07-12T15:10:03.192988915Z'
                    allowedIPAddresses:
                      - id: e7d98003-d2b3-46ff-901e-2c666022004a
                        value: 1.1.1.1
                        createdAt: '2024-07-12T15:09:53.879274435Z'
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````