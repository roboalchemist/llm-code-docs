# Source: https://docs.squared.ai/api-reference/connector_definitions/connector_definitions.md

# Connector Definitions

## OpenAPI

````yaml GET /api/v1/connector_definitions
paths:
  path: /api/v1/connector_definitions
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
              description: Type of the connector (source or destination)
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
          - type: array
            items:
              allOf:
                - type: object
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
        examples:
          example:
            value:
              - name: <string>
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
        description: Successful response
  deprecated: false
  type: path
components:
  schemas: {}

````