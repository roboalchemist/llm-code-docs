# Source: https://docs.squared.ai/api-reference/connector_definitions/connector_definitions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.squared.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Connector Definitions



## OpenAPI

````yaml GET /api/v1/connector_definitions
openapi: 3.0.1
info:
  title: AI Squared API
  version: 1.0.0
servers:
  - url: https://api.squared.ai
security: []
paths:
  /api/v1/connector_definitions:
    get:
      tags:
        - Connector Definitions
      summary: Retrieve connector definitions based on type
      parameters:
        - name: type
          in: query
          required: true
          schema:
            type: string
            enum:
              - source
              - destination
          description: Type of the connector (source or destination)
        - name: category
          in: query
          required: true
          schema:
            type: string
            enum:
              - data
              - ai_ml
          description: Category of the connector
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: array
                items:
                  type: object
                  properties:
                    name:
                      type: string
                    connector_type:
                      type: string
                    connector_subtype:
                      type: string
                    documentation_url:
                      type: string
                    github_issue_label:
                      type: string
                    icon:
                      type: string
                    license:
                      type: string
                    release_stage:
                      type: string
                    support_level:
                      type: string
                    tags:
                      type: array
                      items:
                        type: string
                    connector_spec:
                      type: object
                      properties:
                        documentation_url:
                          type: string
                        connection_specification:
                          type: object
                          additionalProperties: true
      security:
        - bearerAuth: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

````