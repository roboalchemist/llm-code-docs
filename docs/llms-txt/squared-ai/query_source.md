# Source: https://docs.squared.ai/api-reference/connectors/query_source.md

# Query Source

## OpenAPI

````yaml POST /api/v1/connectors/{id}/query_source
paths:
  path: /api/v1/connectors/{id}/query_source
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
      path:
        id:
          schema:
            - type: integer
              required: true
              description: The ID of the connector to query
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              query:
                allOf:
                  - type: string
                    description: SQL query to be executed
            required: true
        examples:
          example:
            value:
              query: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  additionalProperties: true
        examples:
          example:
            value:
              - {}
        description: An array of generic JSON objects representing the preview data.
  deprecated: false
  type: path
components:
  schemas: {}

````