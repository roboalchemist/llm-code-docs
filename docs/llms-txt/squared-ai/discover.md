# Source: https://docs.squared.ai/api-reference/connectors/discover.md

# Connector Catalog

## OpenAPI

````yaml GET /api/v1/connectors/{id}/discover
paths:
  path: /api/v1/connectors/{id}/discover
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
      query:
        refresh:
          schema:
            - type: boolean
              required: false
              description: Set to true to force refresh the catalog
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
        examples:
          example:
            value:
              data:
                id: <string>
                type: <string>
                attributes:
                  connector_id: 123
                  workspace_id: 123
                  catalog:
                    streams:
                      - name: <string>
                        action: <string>
                        json_schema: {}
                        url: <string>
                        request_method: <string>
                  catalog_hash: <string>
        description: Catalog information for the connector
  deprecated: false
  type: path
components:
  schemas: {}

````