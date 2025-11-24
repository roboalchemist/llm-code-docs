# Source: https://docs.squared.ai/api-reference/connectors/list_connectors.md

# List Connectors

## OpenAPI

````yaml GET /api/v1/connectors
paths:
  path: /api/v1/connectors
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
      path: {}
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - source
                - destination
              required: true
              description: Type of the connector
        category:
          schema:
            - type: enum<string>
              enum:
                - data
                - ai_ml
              required: true
              description: Category of the connector
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
                              description: >-
                                Generic configuration for the connector.
                                Structure varies based on the connector_type.
                              additionalProperties: true
                            connector_name:
                              type: string
                            icon:
                              type: string
              links:
                allOf:
                  - type: object
                    properties:
                      self:
                        type: string
                      first:
                        type: string
                      prev:
                        type: string
                      next:
                        type: string
                      last:
                        type: string
            additionalProperties: false
        examples:
          example:
            value:
              data:
                - id: <string>
                  type: <string>
                  attributes:
                    name: <string>
                    connector_type: <string>
                    workspace_id: 123
                    created_at: '2023-11-07T05:31:56Z'
                    updated_at: '2023-11-07T05:31:56Z'
                    configuration: {}
                    connector_name: <string>
                    icon: <string>
              links:
                self: <string>
                first: <string>
                prev: <string>
                next: <string>
                last: <string>
        description: A list of connectors
  deprecated: false
  type: path
components:
  schemas: {}

````