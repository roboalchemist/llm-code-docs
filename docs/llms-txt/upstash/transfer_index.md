# Source: https://upstash.com/docs/devops/developer-api/vector/transfer_index.md

# Transfer Index

> This endpoint is used to transfer an index to another team. 
Transferring to a personal account is not supported. However, transferring an index from a personal account to a team is allowed.


## OpenAPI

````yaml devops/developer-api/openapi.yml post /vector/index/{id}/transfer
paths:
  path: /vector/index/{id}/transfer
  method: post
  servers:
    - url: https://api.upstash.com/v2
  request:
    security:
      - title: basicAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: basic
          cookie: {}
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
              description: The unique ID of the index to be transferred
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              target_account:
                allOf:
                  - type: string
                    description: The team ID of the target team.
                    example: 99a4c327-31f0-490f-a594-043ade84085a
            required: true
            requiredProperties:
              - target_account
        examples:
          example:
            value:
              target_account: 99a4c327-31f0-490f-a594-043ade84085a
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Index transferred successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/vector/transfer_index
components:
  schemas: {}

````