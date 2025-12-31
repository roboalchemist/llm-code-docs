# Source: https://upstash.com/docs/api-reference/qstash/reset-qstash-token.md

# Reset QStash Token

> Resets the authentication credentials for the QStash user account. 
This invalidates the old password and token, and generates new ones.
Returns the updated user information with new credentials.


## OpenAPI

````yaml devops/developer-api/openapi.yml post /qstash/user/rotatetoken
paths:
  path: /qstash/user/rotatetoken
  method: post
  servers:
    - url: https://api.upstash.com
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              customer_id:
                allOf:
                  - type: string
                    description: Customer identifier (email or team ID)
                    example: example@upstash.com
              id:
                allOf:
                  - type: string
                    format: uuid
                    description: Unique identifier for the QStash user account
                    example: 99a4c327-31f0-490f-a594-043ade84085a
              password:
                allOf:
                  - type: string
                    description: QStash authentication password
                    example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              token:
                allOf:
                  - type: string
                    description: Authentication token for QStash operations
                    example: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              active:
                allOf:
                  - type: boolean
                    description: Whether the QStash account is active
                    example: true
              state:
                allOf:
                  - type: string
                    description: Current state of the QStash account
                    enum:
                      - active
                      - passive
                    example: active
              last_plan_upgrade_time:
                allOf:
                  - type: integer
                    format: int64
                    description: Unix timestamp of the last plan upgrade
                    example: 1761267303
              max_message_size:
                allOf:
                  - type: integer
                    description: Maximum message size in bytes
                    example: 52428800
              max_requests_per_day:
                allOf:
                  - type: integer
                    description: Soft limit for maximum requests per day
                    example: 1000000
              max_requests_per_day_hard:
                allOf:
                  - type: integer
                    description: Hard limit for maximum requests per day
                    example: 10000000
              max_endpoints_per_topic:
                allOf:
                  - type: integer
                    description: Maximum number of endpoints allowed per topic
                    example: 1000
              max_requests_per_second:
                allOf:
                  - type: integer
                    description: Maximum requests per second (rate limit)
                    example: 500
              max_dlq_size:
                allOf:
                  - type: integer
                    description: Maximum dead letter queue size
                    example: 2147483647
              max_retries:
                allOf:
                  - type: integer
                    description: Maximum number of retry attempts for failed messages
                    example: 20
              max_topics:
                allOf:
                  - type: integer
                    description: Maximum number of topics allowed
                    example: 1000
              max_schedules:
                allOf:
                  - type: integer
                    description: Maximum number of schedules allowed
                    example: 1000000
              max_events_size:
                allOf:
                  - type: integer
                    description: Maximum size for events
                    example: 100000
              max_dlq_retention_time_milis:
                allOf:
                  - type: integer
                    format: int64
                    description: >-
                      Maximum retention time for dead letter queue in
                      milliseconds
                    example: 2592000000
              max_delay:
                allOf:
                  - type: integer
                    description: Maximum delay for scheduled messages in seconds
                    example: 2147483647
              max_parallelism:
                allOf:
                  - type: integer
                    description: Maximum parallel processing per endpoint
                    example: 10
              max_global_parallelism:
                allOf:
                  - type: integer
                    description: Maximum global parallel processing across all endpoints
                    example: 200
              max_queues:
                allOf:
                  - type: integer
                    description: Maximum number of queues allowed
                    example: 1000
              prod_pack_enabled:
                allOf:
                  - type: boolean
                    description: Whether production pack features are enabled
                    example: false
              timeout:
                allOf:
                  - type: integer
                    description: Request timeout in seconds
                    example: 21600
              type:
                allOf:
                  - type: string
                    description: Account plan type
                    enum:
                      - free
                      - paid
                    example: paid
              reserved_type:
                allOf:
                  - type: string
                    description: >
                      Indicates the reserved plan type for QStash.

                      If a credit card is attached, this field reflects the
                      associated reserved plan.

                      If no credit card is added and the account is not on a
                      pay-as-you-go plan, this field will be an empty string.
                    enum:
                      - paid
                      - qstash_enterprise_1m
                      - qstash_enterprise_10m
                    example: qstash_enterprise_1m
              reserved_price:
                allOf:
                  - type: number
                    format: float
                    description: Reserved plan price
                    example: 180
              created_by:
                allOf:
                  - type: string
                    description: Email of the user who created this account
                    example: example@upstash.com
              creation_time:
                allOf:
                  - type: integer
                    format: int64
                    description: Unix timestamp of account creation
                    example: 1760423113
            refIdentifier: '#/components/schemas/QStashUser'
        examples:
          example:
            value:
              customer_id: example@upstash.com
              id: 99a4c327-31f0-490f-a594-043ade84085a
              password: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              token: ZXhhbXBsZUB1cHN0YXNoLmNvbTpuYWJlcg==
              active: true
              state: active
              last_plan_upgrade_time: 1761267303
              max_message_size: 52428800
              max_requests_per_day: 1000000
              max_requests_per_day_hard: 10000000
              max_endpoints_per_topic: 1000
              max_requests_per_second: 500
              max_dlq_size: 2147483647
              max_retries: 20
              max_topics: 1000
              max_schedules: 1000000
              max_events_size: 100000
              max_dlq_retention_time_milis: 2592000000
              max_delay: 2147483647
              max_parallelism: 10
              max_global_parallelism: 200
              max_queues: 1000
              prod_pack_enabled: false
              timeout: 21600
              type: paid
              reserved_type: qstash_enterprise_1m
              reserved_price: 180
              created_by: example@upstash.com
              creation_time: 1760423113
        description: >-
          Token reset successfully, returns updated user information with new
          credentials
  deprecated: false
  type: path
components:
  schemas: {}

````