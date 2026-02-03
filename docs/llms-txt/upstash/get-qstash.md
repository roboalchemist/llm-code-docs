# Source: https://upstash.com/docs/api-reference/qstash/get-qstash.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get QStash

> Retrieves detailed information about the authenticated user's QStash, including plan details, limits, and configuration



## OpenAPI

````yaml devops/developer-api/openapi.yml get /qstash/user
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
  /qstash/user:
    get:
      tags:
        - qstash
      summary: Get QStash
      description: >-
        Retrieves detailed information about the authenticated user's QStash,
        including plan details, limits, and configuration
      operationId: getQStashUser
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QStashUser'
      security:
        - basicAuth: []
components:
  schemas:
    QStashUser:
      type: object
      properties:
        customer_id:
          type: string
          description: Customer identifier (email or team ID)
          example: example@upstash.com
        id:
          type: string
          format: uuid
          description: Unique identifier for the QStash user account
          example: 99a4c327-31f0-490f-a594-043ade84085a
        password:
          type: string
          description: QStash authentication password
          example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
        token:
          type: string
          description: Authentication token for QStash operations
          example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
        active:
          type: boolean
          description: Whether the QStash account is active
          example: true
        state:
          type: string
          description: Current state of the QStash account
          enum:
            - active
            - passive
          example: active
        last_plan_upgrade_time:
          type: integer
          format: int64
          description: Unix timestamp of the last plan upgrade
          example: 1761267303
        max_message_size:
          type: integer
          description: Maximum message size in bytes
          example: 52428800
        max_requests_per_day:
          type: integer
          description: Soft limit for maximum requests per day
          example: 1000000
        max_requests_per_day_hard:
          type: integer
          description: Hard limit for maximum requests per day
          example: 10000000
        max_endpoints_per_topic:
          type: integer
          description: Maximum number of endpoints allowed per topic
          example: 1000
        max_requests_per_second:
          type: integer
          description: Maximum requests per second (rate limit)
          example: 500
        max_dlq_size:
          type: integer
          description: Maximum dead letter queue size
          example: 2147483647
        max_retries:
          type: integer
          description: Maximum number of retry attempts for failed messages
          example: 20
        max_topics:
          type: integer
          description: Maximum number of topics allowed
          example: 1000
        max_schedules:
          type: integer
          description: Maximum number of schedules allowed
          example: 1000000
        max_events_size:
          type: integer
          description: Maximum size for events
          example: 100000
        max_dlq_retention_time_milis:
          type: integer
          format: int64
          description: Maximum retention time for dead letter queue in milliseconds
          example: 2592000000
        max_delay:
          type: integer
          description: Maximum delay for scheduled messages in seconds
          example: 2147483647
        max_parallelism:
          type: integer
          description: Maximum parallel processing per endpoint
          example: 10
        max_global_parallelism:
          type: integer
          description: Maximum global parallel processing across all endpoints
          example: 200
        max_queues:
          type: integer
          description: Maximum number of queues allowed
          example: 1000
        prod_pack_enabled:
          type: boolean
          description: Whether production pack features are enabled
          example: false
        timeout:
          type: integer
          description: Request timeout in seconds
          example: 21600
        type:
          type: string
          description: Account plan type
          enum:
            - free
            - paid
          example: paid
        reserved_type:
          type: string
          description: >
            Indicates the reserved plan type for QStash.

            If a credit card is attached, this field reflects the associated
            reserved plan.

            If no credit card is added and the account is not on a pay-as-you-go
            plan, this field will be an empty string.
          enum:
            - paid
            - qstash_enterprise_1m
            - qstash_enterprise_10m
          example: qstash_enterprise_1m
        reserved_price:
          type: number
          format: float
          description: Reserved plan price
          example: 180
        created_by:
          type: string
          description: Email of the user who created this account
          example: example@upstash.com
        creation_time:
          type: integer
          format: int64
          description: Unix timestamp of account creation
          example: 1760423113
  securitySchemes:
    basicAuth:
      type: http
      scheme: basic

````