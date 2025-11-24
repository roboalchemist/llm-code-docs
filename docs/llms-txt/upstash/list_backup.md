# Source: https://upstash.com/docs/devops/developer-api/redis/backup/list_backup.md

# List Backup

> This endpoint lists all backups for a Redis database.

## OpenAPI

````yaml devops/developer-api/openapi.yml get /redis/list-backup/{id}
paths:
  path: /redis/list-backup/{id}
  method: get
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
          - type: array
            items:
              allOf:
                - $ref: '#/components/schemas/Backup'
        examples:
          example:
            value:
              - database_id: 6gcqwafd-9627-4ec2-4g51-b1429h59c8d4
                customer_id: example@upstash.com
                name: test
                backup_id: 1d62p45b-c567-1239-b23e-449ads33a62e
                creation_time: 1757000716
                state: pending
                backup_size: 0
                daily_backup: 'false'
                hourly_backup: 'false'
                internal_backup_tag: ''
        description: Backups retrieved successfully
  deprecated: false
  type: path
  xMint:
    href: /devops/developer-api/redis/backup/list_backup
components:
  schemas:
    Backup:
      type: object
      properties:
        database_id:
          type: string
          description: ID of the database
          example: 6gcqwafd-9627-4ec2-4g51-b1429h59c8d4
        customer_id:
          type: string
          description: Customer ID
          example: example@upstash.com
        name:
          type: string
          description: Name of the backup
          example: test
        backup_id:
          type: string
          description: ID of the backup
          example: 1d62p45b-c567-1239-b23e-449ads33a62e
        creation_time:
          type: integer
          description: Creation time of the backup as Unix time
          format: int64
          example: 1757000716
        state:
          type: string
          description: State of the backup
          enum:
            - pending
            - completed
            - failed
          example: pending
        backup_size:
          type: integer
          description: Size of the backup
          format: int64
          example: 0
        daily_backup:
          type: string
          description: Daily backup status
          enum:
            - 'true'
            - 'false'
          example: 'false'
        hourly_backup:
          type: string
          description: Hourly backup status
          enum:
            - 'true'
            - 'false'
          example: 'false'
        internal_backup_tag:
          type: string
          description: Internal backup tag
          example: ''
      xml:
        name: backup

````