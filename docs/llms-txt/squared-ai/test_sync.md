# Source: https://docs.squared.ai/api-reference/syncs/test_sync.md

# Test Sync

> Triggers a test for the specified sync using the sync ID.

## OpenAPI

````yaml POST /enterprise/api/v1/syncs/{sync_id}/test
paths:
  path: /enterprise/api/v1/syncs/{sync_id}/test
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
      path:
        sync_id:
          schema:
            - type: integer
              required: true
              description: The ID of the sync to be tested
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
                    example: Sync test triggered successfully
        examples:
          example:
            value:
              message: Sync test triggered successfully
        description: Sync test triggered successfully
  deprecated: false
  type: path
components:
  schemas: {}

````