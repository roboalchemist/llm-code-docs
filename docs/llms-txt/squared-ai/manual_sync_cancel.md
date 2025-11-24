# Source: https://docs.squared.ai/api-reference/syncs/manual_sync_cancel.md

# Manual Sync Cancel

> Cancel a Manual Sync using the sync ID.

## OpenAPI

````yaml DELETE /api/v1/schedule_syncs/{sync_id}
paths:
  path: /api/v1/schedule_syncs/{sync_id}
  method: delete
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
        sync_id:
          schema:
            - type: integer
              required: true
              description: The ID of the sync to be canceled
              example: 72
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
              message:
                allOf:
                  - type: string
                    example: Sync cancelled successfully
        examples:
          example:
            value:
              message: Sync cancelled successfully
        description: Sync cancelled successfully
  deprecated: false
  type: path
components:
  schemas: {}

````