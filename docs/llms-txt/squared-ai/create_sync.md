# Source: https://docs.squared.ai/api-reference/syncs/create_sync.md

# Create Sync

## OpenAPI

````yaml POST /api/v1/syncs
paths:
  path: /api/v1/syncs
  method: post
  servers:
    - url: https://api.squared.ai
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              sync:
                allOf:
                  - type: object
                    properties:
                      source_id:
                        type: integer
                      destination_id:
                        type: integer
                      model_id:
                        type: integer
                      schedule_type:
                        type: string
                        enum:
                          - automated
                      configuration:
                        type: object
                        additionalProperties: true
                      stream_name:
                        type: string
                      sync_mode:
                        type: string
                        enum:
                          - full_refresh
                      sync_interval:
                        type: integer
                      sync_interval_unit:
                        type: string
                        enum:
                          - minutes
                      cron_expression:
                        type: string
                      cursor_field:
                        type: string
                    required:
                      - source_id
                      - destination_id
                      - model_id
                      - schedule_type
                      - configuration
                      - stream_name
                      - sync_mode
                      - sync_interval
                      - sync_interval_unit
            required: true
        examples:
          example:
            value:
              sync:
                source_id: 123
                destination_id: 123
                model_id: 123
                schedule_type: automated
                configuration: {}
                stream_name: <string>
                sync_mode: full_refresh
                sync_interval: 123
                sync_interval_unit: minutes
                cron_expression: <string>
                cursor_field: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
              type:
                allOf:
                  - type: string
                    enum:
                      - syncs
              attributes:
                allOf:
                  - type: object
                    properties:
                      source_id:
                        type: integer
                      destination_id:
                        type: integer
                      model_id:
                        type: integer
                      configuration:
                        type: object
                        additionalProperties: true
                      schedule_type:
                        type: string
                        enum:
                          - automated
                      sync_mode:
                        type: string
                        enum:
                          - full_refresh
                      sync_interval:
                        type: integer
                      sync_interval_unit:
                        type: string
                        enum:
                          - minutes
                      cron_expression:
                        type: string
                      cursor_field:
                        type: string
                      stream_name:
                        type: string
                      status:
                        type: string
        examples:
          example:
            value:
              id: <string>
              type: syncs
              attributes:
                source_id: 123
                destination_id: 123
                model_id: 123
                configuration: {}
                schedule_type: automated
                sync_mode: full_refresh
                sync_interval: 123
                sync_interval_unit: minutes
                cron_expression: <string>
                cursor_field: <string>
                stream_name: <string>
                status: <string>
        description: Sync operation created successfully
  deprecated: false
  type: path
components:
  schemas: {}

````