# Source: https://upstash.com/docs/devops/developer-api/redis/backup/list_backup.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List Backup

> This endpoint lists all backups for a Redis database.



## OpenAPI

````yaml devops/developer-api/openapi.yml get /redis/list-backup/{id}
openapi: 3.0.4
info:
  title: Developer API - Upstash
  description: >-
    This is a documentation to specify Developer API endpoints based on the
    OpenAPI 3.0 specification.
  contact:
    name: Support Team
    email: support@upstash.com
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0.html
  version: 1.0.0
servers:
  - url: https://api.upstash.com/v2
security: []
tags:
  - name: redis
    description: Manage redis databases.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: teams
    description: Manage teams and team members.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: vector
    description: Manage vector indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: search
    description: Manage search indices.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
  - name: qstash
    description: Manage QStash.
    externalDocs:
      description: Find out more
      url: https://upstash.com/docs/devops/developer-api/introduction
externalDocs:
  description: Find out more about Upstash
  url: https://upstash.com/
paths:
  /redis/list-backup/{id}:
    get:
      tags:
        - redis
      summary: List Backup
      description: This endpoint lists all backups for a Redis database.
      operationId: listBackup
      parameters:
        - name: id
          in: path
          description: The ID of the Redis database
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Backups retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Backup'
      security:
        - basicAuth: []
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
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````