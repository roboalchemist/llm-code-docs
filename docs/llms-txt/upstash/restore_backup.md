# Source: https://upstash.com/docs/devops/developer-api/redis/backup/restore_backup.md

# Restore Backup

> This endpoint restores data from an existing backup.

## OpenAPI

````yaml devops/developer-api/openapi.yml post /redis/restore-backup/{id}
paths:
  path: /redis/restore-backup/{id}
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
              backup_id:
                allOf:
                  - type: string
                    description: ID of the backup to restore
            required: true
            requiredProperties:
              - backup_id
        examples:
          example:
            value:
              backup_id: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: string
            example: OK
        examples:
          example:
            value: OK
        description: Backup restored successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/backup/restore_backup
components:
  schemas: {}

````