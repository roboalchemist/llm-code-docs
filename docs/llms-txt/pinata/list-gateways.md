# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-gateways.md

# List Gateways

> `org:gateways:read`


## OpenAPI

````yaml get /gateways
paths:
  path: /gateways
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
      query:
        pageSize:
          schema:
            - type: integer
              description: Limits the number of results
        page:
          schema:
            - type: integer
              description: Paginates through results by offsetting the results
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
                count: 5
                rows:
                  - id: 01dae16b-699c-472a-a61e-975a7b9777bd
                    created_at: '2023-01-24T19:51:17.493Z'
                    domain: restricted-example
                    restrict: false
                    custom_domains:
                      - domain: ipfs.pinata.cloud
                        domain_validation_status: pending
                        custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                        ssl_validation_status: initializing
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````