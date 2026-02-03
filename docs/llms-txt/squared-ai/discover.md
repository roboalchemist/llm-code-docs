# Source: https://docs.squared.ai/api-reference/connectors/discover.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector Catalog



## OpenAPI

````yaml GET /api/v1/connectors/{id}/discover
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/connectors/{id}/discover:
    get:
      tags:
        - Connectors
      summary: Discovers catalog information for a specified connector
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
          description: Unique ID of the connector
        - name: refresh
          in: query
          required: false
          schema:
            type: boolean
          description: Set to true to force refresh the catalog
      responses:
        '200':
          description: Catalog information for the connector
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
                          connector_id:
                            type: integer
                          workspace_id:
                            type: integer
                          catalog:
                            type: object
                            properties:
                              streams:
                                type: array
                                description: >-
                                  Array of stream objects, varying based on
                                  connector ID.
                                items:
                                  type: object
                                  properties:
                                    name:
                                      type: string
                                    action:
                                      type: string
                                    json_schema:
                                      type: object
                                      additionalProperties: true
                                    url:
                                      type: string
                                    request_method:
                                      type: string
                          catalog_hash:
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