# Source: https://docs.squared.ai/api-reference/connectors/get_connector.md

# Get Connector

## OpenAPI

````yaml GET /api/v1/connectors/{id}
paths:
  path: /api/v1/connectors/{id}
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
      path:
        id:
          schema:
            - type: string
              required: true
              description: Unique ID of the connector
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
              data:
                allOf:
                  - type: object
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
                              Generic configuration for the connector. Structure
                              varies based on the connector_type.
                            additionalProperties: true
                          connector_name:
                            type: string
                          icon:
                            type: string
            additionalProperties: false
        examples:
          example:
            value:
              data:
                id: <string>
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
        description: A single connector object
  deprecated: false
  type: path
components:
  schemas: {}

````