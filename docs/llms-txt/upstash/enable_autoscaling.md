# Source: https://upstash.com/docs/devops/developer-api/redis/enable_autoscaling.md

# Enable Auto Upgrade

> This endpoint enables Auto Upgrade for given database.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/enable-autoupgrade/{id}
paths:
  path: /redis/enable-autoupgrade/{id}
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
              description: The ID of the database to enable auto upgrade
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
        description: Auto upgrade enabled successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/enable_autoscaling
components:
  schemas: {}

````