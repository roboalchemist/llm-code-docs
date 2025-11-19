# Source: https://docs.datafold.com/api-reference/data-sources/list-data-source-types.md

# List data source types

## OpenAPI

````yaml get /api/v1/data_sources/types
paths:
  path: /api/v1/data_sources/types
  method: get
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path: {}
      query: {}
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
                - $ref: '#/components/schemas/ApiDataSourceType'
            title: Response Get Data Source Types Api V1 Data Sources Types Get
        examples:
          example:
            value:
              - configuration_schema: {}
                features:
                  - <string>
                name: <string>
                type: <string>
        description: Successful Response
  deprecated: false
  type: path
components:
  schemas:
    ApiDataSourceType:
      properties:
        configuration_schema:
          additionalProperties: true
          title: Configuration Schema
          type: object
        features:
          items:
            type: string
          title: Features
          type: array
        name:
          title: Name
          type: string
        type:
          title: Type
          type: string
      required:
        - name
        - type
        - configuration_schema
        - features
      title: ApiDataSourceType
      type: object

````