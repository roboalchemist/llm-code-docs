# Source: https://docs.squared.ai/api-reference/connector_definitions/check_connection.md

# Check Connection

## OpenAPI

````yaml POST /api/v1/connector_definitions/check_connection
paths:
  path: /api/v1/connector_definitions/check_connection
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
              type:
                allOf:
                  - type: string
                    enum:
                      - source
                      - destination
              name:
                allOf:
                  - type: string
              connection_spec:
                allOf:
                  - type: object
                    description: >-
                      Generic connection specification structure. Specifics
                      depend on the connector type.
                    additionalProperties: true
            required: true
        examples:
          example:
            value:
              type: source
              name: <string>
              connection_spec: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              result:
                allOf:
                  - type: string
                    enum:
                      - success
                      - failure
              details:
                allOf:
                  - type: string
            additionalProperties: false
        examples:
          example:
            value:
              result: success
              details: <string>
        description: Connection check successful
  deprecated: false
  type: path
components:
  schemas: {}

````