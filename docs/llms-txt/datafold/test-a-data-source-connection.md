# Source: https://docs.datafold.com/api-reference/data-sources/test-a-data-source-connection.md

# Test a data source connection

## OpenAPI

````yaml post /api/v1/data_sources/{data_source_id}/test
paths:
  path: /api/v1/data_sources/{data_source_id}/test
  method: post
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
              job_id:
                allOf:
                  - title: Job Id
                    type: integer
            title: TestDataSourceAsyncResponse
            refIdentifier: '#/components/schemas/TestDataSourceAsyncResponse'
            requiredProperties:
              - job_id
        examples:
          example:
            value:
              job_id: 123
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