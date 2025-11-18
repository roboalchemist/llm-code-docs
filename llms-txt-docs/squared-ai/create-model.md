# Source: https://docs.squared.ai/api-reference/models/create-model.md

# Create Model

## OpenAPI

````yaml POST /api/v1/models
paths:
  path: /api/v1/models
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
              model:
                allOf:
                  - type: object
                    properties:
                      name:
                        type: string
                      description:
                        type: string
                      query:
                        type: string
                      query_type:
                        type: string
                      configuration:
                        type: object
                      primary_key:
                        type: string
                      connector_id:
                        type: integer
                    required:
                      - connector_id
                      - name
                      - query_type
        examples:
          example:
            value:
              model:
                name: <string>
                description: <string>
                query: <string>
                query_type: <string>
                configuration: {}
                primary_key: <string>
                connector_id: 123
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
                          description:
                            type: string
                          query:
                            type: string
                          query_type:
                            type: string
                          configuration:
                            type: object
                          primary_key:
                            type: string
                          connector_id:
                            type: integer
                          created_at:
                            type: string
                            format: date-time
                          updated_at:
                            type: string
                            format: date-time
        examples:
          example:
            value:
              data:
                id: <string>
                type: <string>
                attributes:
                  name: <string>
                  description: <string>
                  query: <string>
                  query_type: <string>
                  configuration: {}
                  primary_key: <string>
                  connector_id: 123
                  created_at: '2023-11-07T05:31:56Z'
                  updated_at: '2023-11-07T05:31:56Z'
        description: Model created
  deprecated: false
  type: path
components:
  schemas: {}

````