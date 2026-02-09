# Source: https://docs.datafold.com/api-reference/data-diffs/list-data-diffs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List data diffs

> All fields support multiple items, using just comma delimiter
Date fields also support ranges using the following syntax:

- ``<DATETIME`` = before DATETIME
- ``>DATETIME`` = after DATETIME
- ``DATETIME`` = between DATETIME and DATETIME + 1 MINUTE
- ``DATE`` = start of that DATE until DATE + 1 DAY
- ``DATETIME1<<DATETIME2`` = between DATETIME1 and DATETIME2
- ``DATE1<<DATE2`` = between DATE1 and DATE2



## OpenAPI

````yaml get /api/v1/datadiffs
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
  /api/v1/datadiffs:
    get:
      tags:
        - Data diffs
      summary: List data diffs
      description: |-
        All fields support multiple items, using just comma delimiter
        Date fields also support ranges using the following syntax:

        - ``<DATETIME`` = before DATETIME
        - ``>DATETIME`` = after DATETIME
        - ``DATETIME`` = between DATETIME and DATETIME + 1 MINUTE
        - ``DATE`` = start of that DATE until DATE + 1 DAY
        - ``DATETIME1<<DATETIME2`` = between DATETIME1 and DATETIME2
        - ``DATE1<<DATE2`` = between DATE1 and DATE2
      operationId: list_datadiffs_api_v1_datadiffs_get
      parameters:
        - in: query
          name: page
          required: false
          schema:
            default: 1
            title: Page
            type: integer
        - in: query
          name: page_size
          required: false
          schema:
            default: 100
            title: Page Size
            type: integer
        - in: query
          name: sort_order
          required: false
          schema:
            $ref: '#/components/schemas/ApiSortOrder'
            default: asc
        - in: query
          name: order_by
          required: false
          schema:
            $ref: '#/components/schemas/ApiSortFilters'
            default: id
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiDataDiffPage'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiSortOrder:
      enum:
        - asc
        - desc
      title: ApiSortOrder
      type: string
    ApiSortFilters:
      enum:
        - id
        - user_id
        - user_name
        - data_source1_id
        - data_source2_id
        - table1
        - table2
        - query1
        - query2
        - pk_columns
        - include_columns
        - exclude_columns
        - time_column
        - time_aggregate
        - filter1
        - filter2
        - done
        - time_interval_start
        - time_interval_end
        - created_at
        - updated_at
        - diff_stats_pks
        - diff_stats_rows
        - diff_stats_values
        - stats.match_ratio
        - tags
        - source
        - status
        - bisection_factor
        - bisection_threshold
        - ci_type
        - ci_run_id
        - pr_user_id
        - pr_username
        - pr_user_email
        - pr_user_display_name
        - pr_num
        - pr_branch
        - monitor_id
        - data_app_type
        - data_app_data_source_id
        - data_app_model1_id
        - data_app_model2_id
        - data_app_model1_name
        - data_app_model2_name
        - user_ref
        - result
        - archived
        - purged
        - kind
      title: ApiSortFilters
      type: string
    ApiDataDiffPage:
      properties:
        count:
          title: Count
          type: integer
        page:
          title: Page
          type: integer
        page_size:
          title: Page Size
          type: integer
        results:
          items:
            $ref: '#/components/schemas/ApiDataDiffFull'
          title: Results
          type: array
        total_pages:
          title: Total Pages
          type: integer
      required:
        - page
        - page_size
        - count
        - total_pages
        - results
      title: ApiDataDiffPage
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
    ApiDataDiffFull:
      properties:
        affected_columns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Affected Columns
        algorithm:
          anyOf:
            - $ref: '#/components/schemas/DiffAlgorithm'
            - type: 'null'
        archived:
          default: false
          title: Archived
          type: boolean
        bisection_factor:
          anyOf:
            - type: integer
            - type: 'null'
          title: Bisection Factor
        bisection_threshold:
          anyOf:
            - type: integer
            - type: 'null'
          title: Bisection Threshold
        ci_base_branch:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Base Branch
        ci_pr_branch:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr Branch
        ci_pr_num:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ci Pr Num
        ci_pr_sha:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr Sha
        ci_pr_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr Url
        ci_pr_user_display_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr User Display Name
        ci_pr_user_email:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr User Email
        ci_pr_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr User Id
        ci_pr_username:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Pr Username
        ci_run_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ci Run Id
        ci_sha_url:
          anyOf:
            - type: string
            - type: 'null'
          title: Ci Sha Url
        column_mapping:
          anyOf:
            - items:
                maxItems: 2
                minItems: 2
                prefixItems:
                  - type: string
                  - type: string
                type: array
              type: array
            - type: 'null'
          title: Column Mapping
        columns_to_compare:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Columns To Compare
        compare_duplicates:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Compare Duplicates
        created_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Created At
        data_app_metadata:
          anyOf:
            - $ref: '#/components/schemas/TDataDiffDataAppMetadata'
            - type: 'null'
        data_app_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Data App Type
        data_source1_id:
          title: Data Source1 Id
          type: integer
        data_source1_session_parameters:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Data Source1 Session Parameters
        data_source2_id:
          title: Data Source2 Id
          type: integer
        data_source2_session_parameters:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Data Source2 Session Parameters
        datetime_tolerance:
          anyOf:
            - type: integer
            - type: 'null'
          title: Datetime Tolerance
        diff_stats:
          anyOf:
            - $ref: '#/components/schemas/DiffStats'
            - type: 'null'
        diff_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Tolerance
        diff_tolerances_per_column:
          anyOf:
            - items:
                $ref: '#/components/schemas/ColumnTolerance'
              type: array
            - type: 'null'
          title: Diff Tolerances Per Column
        done:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Done
        download_limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Download Limit
        exclude_columns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Exclude Columns
        execute_as_user:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Execute As User
        file1:
          anyOf:
            - format: uri
              minLength: 1
              type: string
            - type: 'null'
          title: File1
        file1_options:
          anyOf:
            - discriminator:
                mapping:
                  csv: '#/components/schemas/CSVFileOptions'
                  excel: '#/components/schemas/ExcelFileOptions'
                  parquet: '#/components/schemas/ParquetFileOptions'
                propertyName: file_type
              oneOf:
                - $ref: '#/components/schemas/CSVFileOptions'
                - $ref: '#/components/schemas/ExcelFileOptions'
                - $ref: '#/components/schemas/ParquetFileOptions'
            - type: 'null'
          title: File1 Options
        file2:
          anyOf:
            - format: uri
              minLength: 1
              type: string
            - type: 'null'
          title: File2
        file2_options:
          anyOf:
            - discriminator:
                mapping:
                  csv: '#/components/schemas/CSVFileOptions'
                  excel: '#/components/schemas/ExcelFileOptions'
                  parquet: '#/components/schemas/ParquetFileOptions'
                propertyName: file_type
              oneOf:
                - $ref: '#/components/schemas/CSVFileOptions'
                - $ref: '#/components/schemas/ExcelFileOptions'
                - $ref: '#/components/schemas/ParquetFileOptions'
            - type: 'null'
          title: File2 Options
        filter1:
          anyOf:
            - type: string
            - type: 'null'
          title: Filter1
        filter2:
          anyOf:
            - type: string
            - type: 'null'
          title: Filter2
        finished_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Finished At
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        include_columns:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Include Columns
        kind:
          $ref: '#/components/schemas/DiffKind'
        materialization_destination_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Materialization Destination Id
        materialize_dataset1:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Materialize Dataset1
        materialize_dataset2:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Materialize Dataset2
        materialize_without_sampling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Materialize Without Sampling
        monitor_error:
          anyOf:
            - $ref: '#/components/schemas/QueryError'
            - type: 'null'
        monitor_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Monitor Id
        monitor_state:
          anyOf:
            - $ref: '#/components/schemas/MonitorRunState'
            - type: 'null'
        per_column_diff_limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Per Column Diff Limit
        pk_columns:
          items:
            type: string
          title: Pk Columns
          type: array
        purged:
          default: false
          title: Purged
          type: boolean
        query1:
          anyOf:
            - type: string
            - type: 'null'
          title: Query1
        query2:
          anyOf:
            - type: string
            - type: 'null'
          title: Query2
        result:
          anyOf:
            - enum:
                - error
                - bad-pks
                - different
                - missing-pks
                - identical
                - empty
              type: string
            - type: 'null'
          title: Result
        result_revisions:
          additionalProperties:
            type: integer
          default: {}
          title: Result Revisions
          type: object
        result_statuses:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Result Statuses
        run_profiles:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Run Profiles
        runtime:
          anyOf:
            - type: number
            - type: 'null'
          title: Runtime
        sampling_confidence:
          anyOf:
            - type: number
            - type: 'null'
          title: Sampling Confidence
        sampling_max_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Sampling Max Rows
        sampling_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Sampling Ratio
        sampling_threshold:
          anyOf:
            - type: integer
            - type: 'null'
          title: Sampling Threshold
        sampling_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          title: Sampling Tolerance
        source:
          anyOf:
            - $ref: '#/components/schemas/JobSource'
            - type: 'null'
        status:
          anyOf:
            - $ref: '#/components/schemas/JobStatus'
            - type: 'null'
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
        table_modifiers:
          anyOf:
            - items:
                $ref: '#/components/schemas/TableModifiers'
              type: array
            - type: 'null'
          title: Table Modifiers
        tags:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Tags
        temp_schema_override:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Temp Schema Override
        time_aggregate:
          anyOf:
            - $ref: '#/components/schemas/TimeAggregateEnum'
            - type: 'null'
        time_column:
          anyOf:
            - type: string
            - type: 'null'
          title: Time Column
        time_interval_end:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Time Interval End
        time_interval_start:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Time Interval Start
        time_travel_point1:
          anyOf:
            - type: integer
            - format: date-time
              type: string
            - type: string
            - type: 'null'
          title: Time Travel Point1
        time_travel_point2:
          anyOf:
            - type: integer
            - format: date-time
              type: string
            - type: string
            - type: 'null'
          title: Time Travel Point2
        tolerance_mode:
          anyOf:
            - $ref: '#/components/schemas/ToleranceModeEnum'
            - type: 'null'
        updated_at:
          anyOf:
            - format: date-time
              type: string
            - type: 'null'
          title: Updated At
        user_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: User Id
      required:
        - data_source1_id
        - data_source2_id
        - pk_columns
        - kind
      title: ApiDataDiffFull
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
    DiffAlgorithm:
      enum:
        - join
        - hash
        - hash_v2_alpha
        - fetch_and_join
      title: DiffAlgorithm
      type: string
    TDataDiffDataAppMetadata:
      properties:
        data_app_id:
          title: Data App Id
          type: integer
        data_app_model1_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Data App Model1 Id
        data_app_model1_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Data App Model1 Name
        data_app_model2_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Data App Model2 Id
        data_app_model2_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Data App Model2 Name
        data_app_model_type:
          title: Data App Model Type
          type: string
        meta_data:
          additionalProperties: true
          title: Meta Data
          type: object
      required:
        - data_app_id
        - data_app_model_type
        - meta_data
      title: TDataDiffDataAppMetadata
      type: object
    DiffStats:
      properties:
        diff_duplicate_pks:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Duplicate Pks
        diff_null_pks:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Null Pks
        diff_pks:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Pks
        diff_rows:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Rows
        diff_rows_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Diff Rows Count
        diff_rows_number:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Rows Number
        diff_schema:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Schema
        diff_values:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Values
        errors:
          anyOf:
            - type: integer
            - type: 'null'
          title: Errors
        match_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Match Ratio
        rows_added:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rows Added
        rows_removed:
          anyOf:
            - type: integer
            - type: 'null'
          title: Rows Removed
        sampled:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Sampled
        table_a_row_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Table A Row Count
        table_b_row_count:
          anyOf:
            - type: integer
            - type: 'null'
          title: Table B Row Count
        version:
          title: Version
          type: string
      required:
        - version
      title: DiffStats
      type: object
    ColumnTolerance:
      properties:
        column_name:
          title: Column Name
          type: string
        tolerance_mode:
          $ref: '#/components/schemas/ToleranceModeEnum'
        tolerance_value:
          title: Tolerance Value
          type: number
      required:
        - column_name
        - tolerance_value
        - tolerance_mode
      title: ColumnTolerance
      type: object
    CSVFileOptions:
      properties:
        delimiter:
          anyOf:
            - type: string
            - type: 'null'
          title: Delimiter
        file_type:
          const: csv
          default: csv
          title: File Type
          type: string
        skip_head_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Skip Head Rows
        skip_tail_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Skip Tail Rows
      title: CSVFileOptions
      type: object
    ExcelFileOptions:
      properties:
        file_type:
          const: excel
          default: excel
          title: File Type
          type: string
        sheet:
          anyOf:
            - type: string
            - type: 'null'
          title: Sheet
        skip_head_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Skip Head Rows
        skip_tail_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Skip Tail Rows
      title: ExcelFileOptions
      type: object
    ParquetFileOptions:
      properties:
        file_type:
          const: parquet
          default: parquet
          title: File Type
          type: string
      title: ParquetFileOptions
      type: object
    DiffKind:
      enum:
        - in_db
        - cross_db
      title: DiffKind
      type: string
    QueryError:
      properties:
        error_type:
          title: Error Type
          type: string
        error_value:
          title: Error Value
          type: string
      required:
        - error_type
        - error_value
      title: QueryError
      type: object
    MonitorRunState:
      enum:
        - ok
        - alert
        - error
        - learning
        - checking
        - created
        - skipped
        - cancelled
      title: MonitorRunState
      type: string
    JobSource:
      enum:
        - interactive
        - demo_signup
        - manual
        - api
        - ci
        - schedule
        - auto
      title: JobSource
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
    TableModifiers:
      enum:
        - case_insensitive_strings
      title: TableModifiers
      type: string
    TimeAggregateEnum:
      enum:
        - minute
        - hour
        - day
        - week
        - month
        - year
      title: TimeAggregateEnum
      type: string
    ToleranceModeEnum:
      enum:
        - absolute
        - relative
      title: ToleranceModeEnum
      type: string
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````