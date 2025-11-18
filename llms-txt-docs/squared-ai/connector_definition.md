# Source: https://docs.squared.ai/api-reference/connector_definitions/connector_definition.md

# Connector Definition

## OpenAPI

````yaml GET /api/v1/connector_definitions/{connector_name}
paths:
  path: /api/v1/connector_definitions/{connector_name}
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
        connector_name:
          schema:
            - type: string
              required: true
              description: Name of the connector
      query:
        type:
          schema:
            - type: enum<string>
              enum:
                - source
                - destination
              required: true
              description: Type of the connector (source or destination)
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              name:
                allOf:
                  - type: string
              connector_type:
                allOf:
                  - type: string
              connector_subtype:
                allOf:
                  - type: string
              documentation_url:
                allOf:
                  - type: string
              github_issue_label:
                allOf:
                  - type: string
              icon:
                allOf:
                  - type: string
              license:
                allOf:
                  - type: string
              release_stage:
                allOf:
                  - type: string
              support_level:
                allOf:
                  - type: string
              tags:
                allOf:
                  - type: array
                    items:
                      type: string
              connector_spec:
                allOf:
                  - type: object
                    properties:
                      documentation_url:
                        type: string
                      connection_specification:
                        type: object
                        additionalProperties: true
                      supports_normalization:
                        type: boolean
                      supports_dbt:
                        type: boolean
                      stream_type:
                        type: string
        examples:
          example:
            value:
              name: <string>
              connector_type: <string>
              connector_subtype: <string>
              documentation_url: <string>
              github_issue_label: <string>
              icon: <string>
              license: <string>
              release_stage: <string>
              support_level: <string>
              tags:
                - <string>
              connector_spec:
                documentation_url: <string>
                connection_specification: {}
                supports_normalization: true
                supports_dbt: true
                stream_type: <string>
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````