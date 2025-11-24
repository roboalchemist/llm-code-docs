# Source: https://docs.squared.ai/api-reference/syncs/update_sync.md

# Update Sync

## OpenAPI

````yaml PUT /api/v1/syncs/{id}
paths:
  path: /api/v1/syncs/{id}
  method: put
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
      path:
        id:
          schema:
            - type: string
              required: true
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
                      configuration:
                        type: object
                        additionalProperties: true
                      stream_name:
                        type: string
                      sync_mode:
                        type: string
                      sync_interval:
                        type: integer
                      sync_interval_unit:
                        type: string
                      cron_expression:
                        type: string
            required: true
        examples:
          example:
            value:
              sync:
                source_id: 123
                destination_id: 123
                model_id: 123
                schedule_type: <string>
                configuration: {}
                stream_name: <string>
                sync_mode: <string>
                sync_interval: 123
                sync_interval_unit: <string>
                cron_expression: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              success:
                allOf:
                  - type: boolean
              message:
                allOf:
                  - type: string
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                        enum:
                          - syncs
                      attributes:
                        type: object
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
              success: true
              message: <string>
              data:
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
        description: Sync operation updated successfully
  deprecated: false
  type: path
components:
  schemas: {}

````