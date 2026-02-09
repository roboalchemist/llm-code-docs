# Source: https://docs.squared.ai/api-reference/connectors/update_connector.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Connector



## OpenAPI

````yaml PUT /api/v1/connectors/{id}
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/connectors/{id}:
    put:
      tags:
        - Connectors
      summary: Updates a specific connector by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Unique ID of the connector
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                connector:
                  type: object
                  properties:
                    name:
                      type: string
                    connector_type:
                      type: string
                      enum:
                        - source
                        - destination
                    configuration:
                      type: object
                      description: >-
                        Generic configuration structure. Specifics depend on the
                        connector type.
                      additionalProperties: true
                    connector_name:
                      type: string
                  required:
                    - name
                    - connector_type
                    - configuration
                    - connector_name
      responses:
        '200':
          description: Connector updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: object
                    properties:
                      id:
                        type: string
                      type:
                        type: string
                      attributes:
                        type: object
                        properties:
                          name:
                            type: string
                          connector_type:
                            type: string
                          workspace_id:
                            type: integer
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
                          configuration:
                            type: object
                            description: Specific configuration of the updated connector.
                            additionalProperties: true
                          connector_name:
                            type: string
                          icon:
                            type: string
                additionalProperties: false
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````