# Source: https://docs.squared.ai/api-reference/sync_runs/get_sync_runs.md

# List Sync Runs

> Retrieves a list of sync runs for a specific sync, optionally filtered by status.

## OpenAPI

````yaml GET /api/v1/syncs/{sync_id}/sync_runs
paths:
  path: /api/v1/syncs/{sync_id}/sync_runs
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
              description: The ID of the sync to list runs for.
      query:
        status:
          schema:
            - type: string
              description: Optional status to filter the sync runs by.
        page:
          schema:
            - type: integer
              description: Page number for pagination.
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
                            skipped_rows:
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
                        nullable: true
                      next:
                        type: string
                        format: uri
                        nullable: true
                      last:
                        type: string
                        format: uri
        examples:
          example:
            value:
              data:
                - id: <string>
                  type: <string>
                  attributes:
                    sync_id: 123
                    status: <string>
                    started_at: '2023-11-07T05:31:56Z'
                    finished_at: '2023-11-07T05:31:56Z'
                    duration: 123
                    total_query_rows: 123
                    skipped_rows: 123
                    total_rows: 123
                    successful_rows: 123
                    failed_rows: 123
                    error: <string>
                    created_at: '2023-11-07T05:31:56Z'
                    updated_at: '2023-11-07T05:31:56Z'
              links:
                self: <string>
                first: <string>
                prev: <string>
                next: <string>
                last: <string>
        description: A JSON array of sync runs
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    example: Sync not found
              status:
                allOf:
                  - type: string
                    example: not_found
        examples:
          example:
            value:
              message: Sync not found
              status: not_found
        description: Sync not found
  deprecated: false
  type: path
components:
  schemas: {}

````