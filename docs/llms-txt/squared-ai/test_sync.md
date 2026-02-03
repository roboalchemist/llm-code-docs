# Source: https://docs.squared.ai/api-reference/syncs/test_sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Test Sync

> Triggers a test for the specified sync using the sync ID.



## OpenAPI

````yaml POST /enterprise/api/v1/syncs/{sync_id}/test
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /enterprise/api/v1/syncs/{sync_id}/test:
    post:
      tags:
        - Syncs
      summary: Trigger a Sync Test
      description: Triggers a test for the specified sync using the sync ID.
      operationId: testSync
      parameters:
        - name: sync_id
          in: path
          required: true
          description: The ID of the sync to be tested
          schema:
            type: integer
            example: 72
      responses:
        '200':
          description: Sync test triggered successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Sync test triggered successfully
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````