# Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-custom-domain-for-gateway.md

# Create Custom Domain for Gateway

> `org:gateways:write`


## OpenAPI

````yaml post /gateways/{id}/custom_domain
paths:
  path: /gateways/{id}/custom_domain
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
              domain:
                allOf:
                  - type: string
                    description: Custom domain for the target Gateway
            example:
              domain: ipfs2.pinata.cloud
        examples:
          example:
            value:
              domain: ipfs2.pinata.cloud
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
                domain: ipfs2.pinata.cloud
                domain_validation_status: pending
                custom_domain_id: 81bc0135-346d-4d81-ad81-1e313297702f
                ssl_validation_status: initializing
        description: OK
  deprecated: false
  type: path
components:
  schemas: {}

````