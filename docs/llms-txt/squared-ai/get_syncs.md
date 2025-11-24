# Source: https://docs.squared.ai/api-reference/syncs/get_syncs.md

# List Syncs

## OpenAPI

````yaml GET /api/v1/syncs
paths:
  path: /api/v1/syncs
  method: get
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
      query:
        page[number]:
          schema:
            - type: integer
              required: false
              description: Page number for pagination
        page[size]:
          schema:
            - type: integer
              required: false
              description: Number of items per page for pagination
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: object
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
              links:
                allOf:
                  - type: object
                    properties:
                      self:
                        type: string
                        format: uri
                      first:
                        type: string
                        format: uri
                      prev:
                        type: string
                        format: uri
                      next:
                        type: string
                        format: uri
                      last:
                        type: string
                        format: uri
            requiredProperties:
              - data
              - links
        examples:
          example:
            value:
              data:
                - id: <string>
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
              links:
                self: <string>
                first: <string>
                prev: <string>
                next: <string>
                last: <string>
        description: A list of sync operations
  deprecated: false
  type: path
components:
  schemas: {}

````