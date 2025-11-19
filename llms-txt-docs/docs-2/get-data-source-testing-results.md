# Source: https://docs.datafold.com/api-reference/data-sources/get-data-source-testing-results.md

# Get data source testing results

## OpenAPI

````yaml get /api/v1/data_sources/test/{job_id}
paths:
  path: /api/v1/data_sources/test/{job_id}
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
        job_id:
          schema:
            - type: integer
              required: true
              title: Data source testing task id
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
              results:
                allOf:
                  - items:
                      $ref: '#/components/schemas/TestResultStep'
                    title: Results
                    type: array
              status:
                allOf:
                  - $ref: '#/components/schemas/JobStatus'
            title: AsyncDataSourceTestResults
            refIdentifier: '#/components/schemas/AsyncDataSourceTestResults'
            requiredProperties:
              - id
              - status
              - results
        examples:
          example:
            value:
              id: 123
              results:
                - result: <any>
                  status: needs_confirmation
                  step: connection
              status: needs_confirmation
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
    ConfigurationCheckStep:
      enum:
        - connection
        - temp_schema
        - schema_download
        - lineage_download
      title: ConfigurationCheckStep
      type: string
    JobStatus:
      enum:
        - needs_confirmation
        - needs_authentication
        - waiting
        - processing
        - done
        - failed
        - cancelled
      title: JobStatus
      type: string
    TestResultStep:
      properties:
        result:
          anyOf:
            - {}
            - type: 'null'
          title: Result
        status:
          $ref: '#/components/schemas/JobStatus'
        step:
          $ref: '#/components/schemas/ConfigurationCheckStep'
      required:
        - step
        - status
      title: TestResultStep
      type: object
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