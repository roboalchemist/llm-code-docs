# Source: https://docs.squared.ai/api-reference/sync_records/get_sync_records.md

# List Sync Records

> Retrieves a list of sync records for a specific sync run, optionally filtered by status.

## OpenAPI

````yaml GET /api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}/sync_records
paths:
  path: /api/v1/syncs/{sync_id}/sync_runs/{sync_run_id}/sync_records
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
              description: The ID of the sync to list records for.
        sync_run_id:
          schema:
            - type: integer
              required: true
              description: The ID of the sync run to list records for.
      query:
        status:
          schema:
            - type: string
              description: Optional status to filter the sync records by.
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
                          example: sync_records
                        attributes:
                          type: object
                          properties:
                            sync_id:
                              type: integer
                            sync_run_id:
                              type: integer
                            record:
                              type: object
                              properties:
                                id:
                                  type: integer
                                state:
                                  type: string
                                last_name:
                                  type: string
                                first_name:
                                  type: string
                                phone_number:
                                  type: integer
                                email_address:
                                  type: string
                            status:
                              type: string
                            action:
                              type: string
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
                        nullable: true
                        format: uri
                      next:
                        type: string
                        nullable: true
                        format: uri
                      last:
                        type: string
                        format: uri
        examples:
          example:
            value:
              data:
                - id: <string>
                  type: sync_records
                  attributes:
                    sync_id: 123
                    sync_run_id: 123
                    record:
                      id: 123
                      state: <string>
                      last_name: <string>
                      first_name: <string>
                      phone_number: 123
                      email_address: <string>
                    status: <string>
                    action: <string>
                    error: <string>
                    created_at: '2023-11-07T05:31:56Z'
                    updated_at: '2023-11-07T05:31:56Z'
              links:
                self: <string>
                first: <string>
                prev: <string>
                next: <string>
                last: <string>
        description: A JSON array of sync records
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    example: SyncRun not found
              status:
                allOf:
                  - type: string
                    example: not_found
        examples:
          example:
            value:
              message: SyncRun not found
              status: not_found
        description: SyncRun not found
  deprecated: false
  type: path
components:
  schemas: {}

````