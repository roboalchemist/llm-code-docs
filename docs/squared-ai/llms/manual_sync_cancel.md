# Source: https://docs.squared.ai/api-reference/syncs/manual_sync_cancel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Sync Cancel

> Cancel a Manual Sync using the sync ID.



## OpenAPI

````yaml DELETE /api/v1/schedule_syncs/{sync_id}
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/schedule_syncs/{sync_id}:
    delete:
      tags:
        - Syncs
      summary: Cancel a Manual Sync
      description: Cancel a Manual Sync using the sync ID.
      operationId: cancelSyncTrigger
      parameters:
        - name: sync_id
          in: path
          required: true
          description: The ID of the sync to be canceled
          schema:
            type: integer
            example: 72
      responses:
        '200':
          description: Sync cancelled successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Sync cancelled successfully
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````