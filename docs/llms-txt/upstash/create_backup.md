# Source: https://upstash.com/docs/devops/developer-api/redis/backup/create_backup.md

# Create Backup

> This endpoint creates a backup for a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/create-backup/{id}
paths:
  path: /redis/create-backup/{id}
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
              description: The ID of the Redis database
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
                    description: Name of the backup
            required: true
            requiredProperties:
              - name
        examples:
          example:
            value:
              name: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Backup created successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/backup/create_backup
components:
  schemas: {}

````