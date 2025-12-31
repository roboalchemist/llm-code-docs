# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-custom-domain-details.md

# Gateway Custom Domain Details

> `org:gateways:read`


## OpenAPI

````yaml get /gateways/{id}/custom_domain/{custom_domain_id}
paths:
  path: /gateways/{id}/custom_domain/{custom_domain_id}
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
        custom_domain_id:
          schema:
            - type: string
              required: true
              description: Custom domain ID of the target Gateway
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
                domain: ipfs.pinata.cloud
                domain_validation_status: pending
                custom_domain_id: 87980e39-fe71-4dba-9b05-3dfc66593539
                ssl_validation_status: initializing
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````