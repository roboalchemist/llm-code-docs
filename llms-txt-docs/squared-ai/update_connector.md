# Source: https://docs.squared.ai/api-reference/connectors/update_connector.md

# Update Connector

## OpenAPI

````yaml PUT /api/v1/connectors/{id}
paths:
  path: /api/v1/connectors/{id}
  method: put
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
                      configuration:
                        type: object
                        description: >-
                          Generic configuration structure. Specifics depend on
                          the connector type.
                        additionalProperties: true
                      connector_name:
                        type: string
                    required:
                      - name
                      - connector_type
                      - configuration
                      - connector_name
            required: true
        examples:
          example:
            value:
              connector:
                name: <string>
                connector_type: source
                configuration: {}
                connector_name: <string>
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
                            description: Specific configuration of the updated connector.
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
        description: Connector updated successfully
  deprecated: false
  type: path
components:
  schemas: {}

````