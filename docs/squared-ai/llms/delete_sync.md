# Source: https://docs.squared.ai/api-reference/syncs/delete_sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Sync



## OpenAPI

````yaml DELETE /api/v1/syncs/{id}
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/syncs/{id}:
    delete:
      tags:
        - Syncs
      summary: Delete a specific sync operation
      operationId: deleteSync
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: The ID of the sync operation to delete
      responses:
        '204':
          description: No content, indicating the sync operation was successfully deleted
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````