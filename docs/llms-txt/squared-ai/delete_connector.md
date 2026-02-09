# Source: https://docs.squared.ai/api-reference/connectors/delete_connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Connector



## OpenAPI

````yaml DELETE /api/v1/connectors/{id}
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/connectors/{id}:
    delete:
      tags:
        - Connectors
      summary: Deletes a specific connector by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Unique ID of the connector
      responses:
        '204':
          description: No content, indicating successful deletion
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````