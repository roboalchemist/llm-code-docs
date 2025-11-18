# Source: https://upstash.com/docs/devops/developer-api/redis/backup/enable_dailybackup.md

# Enable Daily Backup

> This endpoint enables daily backup for a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml patch /redis/enable-dailybackup/{id}
paths:
  path: /redis/enable-dailybackup/{id}
  method: patch
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
              description: The ID of the Redis database
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
        description: Daily backup enabled successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/backup/enable_dailybackup
components:
  schemas: {}

````