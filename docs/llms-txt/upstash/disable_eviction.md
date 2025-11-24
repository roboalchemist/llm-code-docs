# Source: https://upstash.com/docs/devops/developer-api/redis/disable_eviction.md

# Disable Eviction

> This endpoint disables eviction for given database.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/disable-eviction/{id}
paths:
  path: /redis/disable-eviction/{id}
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
              description: The ID of the database to disable eviction
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Eviction disabled successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/disable_eviction
components:
  schemas: {}

````