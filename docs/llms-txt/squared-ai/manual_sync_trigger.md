# Source: https://docs.squared.ai/api-reference/syncs/manual_sync_trigger.md

# Manual Sync Trigger

> Trigger a manual Sync by providing the sync ID.

## OpenAPI

````yaml POST /api/v1/schedule_syncs
paths:
  path: /api/v1/schedule_syncs
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
              schedule_sync:
                allOf:
                  - type: object
                    properties:
                      sync_id:
                        type: integer
                        description: ID of the sync to be scheduled
                        example: 10
                    required:
                      - sync_id
            required: true
        examples:
          example:
            value:
              schedule_sync:
                sync_id: 10
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    example: Sync scheduled successfully
        examples:
          example:
            value:
              message: Sync scheduled successfully
        description: Sync scheduled successfully
  deprecated: false
  type: path
components:
  schemas: {}

````