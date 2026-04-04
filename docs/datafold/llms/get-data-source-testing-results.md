# Source: https://docs.datafold.com/api-reference/data-sources/get-data-source-testing-results.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get data source testing results



## OpenAPI

````yaml get /api/v1/data_sources/test/{job_id}
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/data_sources/test/{job_id}:
    get:
      tags:
        - Data sources
      summary: Get data source testing results
      operationId: get_data_source_test_result_api_v1_data_sources_test__job_id__get
      parameters:
        - in: path
          name: job_id
          required: true
          schema:
            title: Data source testing task id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AsyncDataSourceTestResults'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    AsyncDataSourceTestResults:
      properties:
        id:
          title: Id
          type: integer
        results:
          items:
            $ref: '#/components/schemas/TestResultStep'
          title: Results
          type: array
        status:
          $ref: '#/components/schemas/JobStatus'
      required:
        - id
        - status
        - results
      title: AsyncDataSourceTestResults
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
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
    ConfigurationCheckStep:
      enum:
        - connection
        - temp_schema
        - schema_download
        - lineage_download
      title: ConfigurationCheckStep
      type: string
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````