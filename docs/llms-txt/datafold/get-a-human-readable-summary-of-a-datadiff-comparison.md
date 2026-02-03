# Source: https://docs.datafold.com/api-reference/data-diffs/get-a-human-readable-summary-of-a-datadiff-comparison.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a human-readable summary of a DataDiff comparison

> Retrieves a comprehensive, human-readable summary of a completed data diff.

This endpoint provides the most useful information for understanding diff results:
- Overall status and result (success/failure)
- Human-readable feedback explaining the differences found
- Key statistics (row counts, differences, match rates)
- Configuration details (tables compared, primary keys used)
- Error messages if the diff failed

Use this after a diff completes to get actionable insights. For diffs still running,
check status with get_datadiff first.



## OpenAPI

````yaml openapi-public.json get /api/v1/datadiffs/{datadiff_id}/summary
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
  /api/v1/datadiffs/{datadiff_id}/summary:
    get:
      tags:
        - Data diffs
      summary: Get a human-readable summary of a DataDiff comparison
      description: >-
        Retrieves a comprehensive, human-readable summary of a completed data
        diff.


        This endpoint provides the most useful information for understanding
        diff results:

        - Overall status and result (success/failure)

        - Human-readable feedback explaining the differences found

        - Key statistics (row counts, differences, match rates)

        - Configuration details (tables compared, primary keys used)

        - Error messages if the diff failed


        Use this after a diff completes to get actionable insights. For diffs
        still running,

        check status with get_datadiff first.
      operationId: get_datadiff_summary
      parameters:
        - in: path
          name: datadiff_id
          required: true
          schema:
            title: Data diff id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiDataDiffSummary'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiDataDiffSummary:
      description: Summary of a DataDiff comparison with human-readable feedback.
      properties:
        algorithm:
          anyOf:
            - type: string
            - type: 'null'
          title: Algorithm
        created_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Created At
        data_source1_id:
          title: Data Source1 Id
          type: integer
        data_source1_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Data Source1 Name
        data_source2_id:
          title: Data Source2 Id
          type: integer
        data_source2_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Data Source2 Name
        diff_stats:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Diff Stats
        error:
          anyOf:
            - type: string
            - type: 'null'
          title: Error
        feedback:
          anyOf:
            - type: string
            - type: 'null'
          title: Feedback
        finished_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Finished At
        id:
          title: Id
          type: integer
        include_columns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Include Columns
        pk_columns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Pk Columns
        result:
          anyOf:
            - type: string
            - type: 'null'
          title: Result
        result_status:
          anyOf:
            - type: string
            - type: 'null'
          title: Result Status
        results_count:
          default: 0
          title: Results Count
          type: integer
        sampling_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Sampling Ratio
        status:
          $ref: '#/components/schemas/JobStatus'
        table1:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Table1
        table2:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Table2
      required:
        - id
        - status
        - data_source1_id
        - data_source2_id
      title: ApiDataDiffSummary
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````