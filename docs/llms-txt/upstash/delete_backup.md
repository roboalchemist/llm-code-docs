# Source: https://upstash.com/docs/devops/developer-api/redis/backup/delete_backup.md

# Delete Backup

> This endpoint deletes a backup of a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml delete /redis/delete-backup/{id}/{backup_id}
paths:
  path: /redis/delete-backup/{id}/{backup_id}
  method: delete
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
        backup_id:
          schema:
            - type: string
              required: true
              description: The ID of the backup to delete
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
        description: Backup deleted successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/backup/delete_backup
components:
  schemas: {}

````