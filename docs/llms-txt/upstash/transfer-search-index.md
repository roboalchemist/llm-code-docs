# Source: https://upstash.com/docs/api-reference/search/transfer-search-index.md

# Transfer Search Index

> Transfers ownership of a search index to another team.
Transferring to a personal account is not supported.
However, transferring from a personal account to a team is allowed.


## OpenAPI

````yaml devops/developer-api/openapi.yml post /search/{id}/transfer
paths:
  path: /search/{id}/transfer
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
              description: The ID of the search index
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
                    description: The ID of the target team account.
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
        description: Search index transferred successfully
  deprecated: false
  type: path
components:
  schemas: {}

````