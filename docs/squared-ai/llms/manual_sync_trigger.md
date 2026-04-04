# Source: https://docs.squared.ai/api-reference/syncs/manual_sync_trigger.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Sync Trigger

> Trigger a manual Sync by providing the sync ID.



## OpenAPI

````yaml POST /api/v1/schedule_syncs
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/schedule_syncs:
    post:
      tags:
        - Syncs
      summary: Trigger a manual Sync
      description: Trigger a manual Sync by providing the sync ID.
      operationId: manualSyncTrigger
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                schedule_sync:
                  type: object
                  properties:
                    sync_id:
                      type: integer
                      description: ID of the sync to be scheduled
                      example: 10
                  required:
                    - sync_id
      responses:
        '200':
          description: Sync scheduled successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Sync scheduled successfully
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````