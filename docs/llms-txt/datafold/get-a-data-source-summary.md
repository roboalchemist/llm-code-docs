# Source: https://docs.datafold.com/api-reference/data-sources/get-a-data-source-summary.md

# Get a data source summary

## OpenAPI

````yaml get /api/v1/data_sources/{data_source_id}/summary
paths:
  path: /api/v1/data_sources/{data_source_id}/summary
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
      path:
        data_source_id:
          schema:
            - type: integer
              required: true
              title: Data source id
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - title: Id
                    type: integer
              name:
                allOf:
                  - title: Name
                    type: string
              type:
                allOf:
                  - title: Type
                    type: string
            title: ApiDataSourceSummary
            description: >-
              Used in OSS data-diff with non-admin privileges to get a DS
              overview.
            refIdentifier: '#/components/schemas/ApiDataSourceSummary'
            requiredProperties:
              - id
              - name
              - type
        examples:
          example:
            value:
              id: 123
              name: <string>
              type: <string>
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