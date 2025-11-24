# Source: https://docs.datafold.com/api-reference/bi/update-a-dbt-bi-integration.md

# Update a DBT BI integration

> Returns the integration with changed fields.

## OpenAPI

````yaml put /api/v1/lineage/bi/dbt/{bi_datasource_id}/
paths:
  path: /api/v1/lineage/bi/dbt/{bi_datasource_id}/
  method: put
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
      path:
        bi_datasource_id:
          schema:
            - type: integer
              required: true
              title: Tableau integration id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              ci_config_id:
                allOf:
                  - title: Ci Config Id
                    type: integer
              indexing_cron:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Indexing Cron
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
            required: true
            title: DbtDataSourceConfig
            refIdentifier: '#/components/schemas/DbtDataSourceConfig'
            requiredProperties:
              - ci_config_id
        examples:
          example:
            value:
              ci_config_id: 123
              indexing_cron: <string>
              name: <string>
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    title: Detail
                    type: array
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object

````