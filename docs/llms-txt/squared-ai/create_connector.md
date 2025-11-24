# Source: https://docs.squared.ai/api-reference/connectors/create_connector.md

# Create Connector

## OpenAPI

````yaml POST /api/v1/connectors
paths:
  path: /api/v1/connectors
  method: post
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
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              connector:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                      connector_type:
                        type: string
                        enum:
                          - source
                          - destination
                      connector_name:
                        type: string
                      configuration:
                        type: object
                        description: >-
                          Configuration details for the connector. Structure
                          depends on the connector definition.
                        additionalProperties: true
                    required:
                      - name
                      - connector_type
                      - connector_name
                      - configuration
            required: true
        examples:
          example:
            value:
              connector:
                name: <string>
                connector_type: source
                connector_name: <string>
                configuration: {}
  response:
    '201':
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
                            description: Specific configuration of the created connector.
                            additionalProperties: true
                          connector_name:
                            type: string
                          icon:
                            type: string
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
        description: Connector created
  deprecated: false
  type: path
components:
  schemas: {}

````