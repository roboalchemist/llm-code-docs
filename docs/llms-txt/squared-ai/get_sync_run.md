# Source: https://docs.squared.ai/api-reference/sync_runs/get_sync_run.md

# Sync Run

> Retrieves a sync run using sync_run_id for a specific sync.

## OpenAPI

````yaml GET /api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}
paths:
  path: /api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}
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
      path:
        sync_id:
          schema:
            - type: integer
              required: true
              description: The ID of the sync.
        sync_run_id:
          schema:
            - type: integer
              required: true
              description: The ID of the sync_run.
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
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                      attributes:
                        type: object
                        properties:
                          sync_id:
                            type: integer
                          status:
                            type: string
                          started_at:
                            type: string
                            format: date-time
                          finished_at:
                            type: string
                            format: date-time
                          duration:
                            type: number
                            format: float
                          total_query_rows:
                            type: integer
                          total_rows:
                            type: integer
                          successful_rows:
                            type: integer
                          failed_rows:
                            type: integer
                          error:
                            type: string
                            nullable: true
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
        examples:
          example:
            value:
              data:
                id: <string>
                type: <string>
                attributes:
                  sync_id: 123
                  status: <string>
                  started_at: '2023-11-07T05:31:56Z'
                  finished_at: '2023-11-07T05:31:56Z'
                  duration: 123
                  total_query_rows: 123
                  total_rows: 123
                  successful_rows: 123
                  failed_rows: 123
                  error: <string>
                  created_at: '2023-11-07T05:31:56Z'
                  updated_at: '2023-11-07T05:31:56Z'
        description: A JSON object representing the sync run
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    example: Sync Run not found
              status:
                allOf:
                  - type: string
                    example: not_found
        examples:
          example:
            value:
              message: Sync Run not found
              status: not_found
        description: Sync not found
  deprecated: false
  type: path
components:
  schemas: {}

````