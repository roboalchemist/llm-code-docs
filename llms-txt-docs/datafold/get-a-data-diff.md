# Source: https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff.md

# Get a data diff

## OpenAPI

````yaml get /api/v1/datadiffs/{datadiff_id}
paths:
  path: /api/v1/datadiffs/{datadiff_id}
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
        datadiff_id:
          schema:
            - type: integer
              required: true
              title: Data diff id
      query:
        poll:
          schema:
            - type: any
              required: false
              title: Poll
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              affected_columns:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Affected Columns
              algorithm:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DiffAlgorithm'
                      - type: 'null'
              archived:
                allOf:
                  - default: false
                    title: Archived
                    type: boolean
              bisection_factor:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Bisection Factor
              bisection_threshold:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Bisection Threshold
              ci_base_branch:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Base Branch
              ci_pr_branch:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr Branch
              ci_pr_num:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Ci Pr Num
              ci_pr_sha:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr Sha
              ci_pr_url:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr Url
              ci_pr_user_display_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr User Display Name
              ci_pr_user_email:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr User Email
              ci_pr_user_id:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr User Id
              ci_pr_username:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Pr Username
              ci_run_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Ci Run Id
              ci_sha_url:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Ci Sha Url
              column_mapping:
                allOf:
                  - anyOf:
                      - items:
                          items:
                            - type: string
                            - type: string
                          maxItems: 2
                          minItems: 2
                          type: array
                        type: array
                      - type: 'null'
                    title: Column Mapping
              columns_to_compare:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Columns To Compare
              compare_duplicates:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Compare Duplicates
              created_at:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Created At
              data_app_metadata:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/TDataDiffDataAppMetadata'
                      - type: 'null'
              data_app_type:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Data App Type
              data_source1_id:
                allOf:
                  - title: Data Source1 Id
                    type: integer
              data_source1_session_parameters:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Data Source1 Session Parameters
              data_source2_id:
                allOf:
                  - title: Data Source2 Id
                    type: integer
              data_source2_session_parameters:
                allOf:
                  - anyOf:
                      - additionalProperties: true
                        type: object
                      - type: 'null'
                    title: Data Source2 Session Parameters
              diff_progress:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DiffProgress'
                      - type: 'null'
              diff_stats:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DiffStats'
                      - type: 'null'
              diff_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: Diff Tolerance
              diff_tolerances_per_column:
                allOf:
                  - anyOf:
                      - items:
                          $ref: '#/components/schemas/ColumnTolerance'
                        type: array
                      - type: 'null'
                    title: Diff Tolerances Per Column
              done:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Done
              download_limit:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Download Limit
              exclude_columns:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Exclude Columns
              execute_as_user:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Execute As User
              file1:
                allOf:
                  - anyOf:
                      - format: uri
                        minLength: 1
                        type: string
                      - type: 'null'
                    title: File1
              file1_options:
                allOf:
                  - anyOf:
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
                allOf:
                  - anyOf:
                      - format: uri
                        minLength: 1
                        type: string
                      - type: 'null'
                    title: File2
              file2_options:
                allOf:
                  - anyOf:
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
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Filter1
              filter2:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Filter2
              finished_at:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Finished At
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              include_columns:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Include Columns
              kind:
                allOf:
                  - $ref: '#/components/schemas/DiffKind'
              materialization_destination_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Materialization Destination Id
              materialize_dataset1:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Materialize Dataset1
              materialize_dataset2:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Materialize Dataset2
              materialize_without_sampling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Materialize Without Sampling
              monitor_error:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/QueryError'
                      - type: 'null'
              monitor_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Monitor Id
              monitor_state:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MonitorRunState'
                      - type: 'null'
              per_column_diff_limit:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Per Column Diff Limit
              pk_columns:
                allOf:
                  - items:
                      type: string
                    title: Pk Columns
                    type: array
              purged:
                allOf:
                  - default: false
                    title: Purged
                    type: boolean
              query1:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Query1
              query2:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Query2
              result:
                allOf:
                  - anyOf:
                      - enum:
                          - error
                          - bad-pks
                          - different
                          - missing-pks
                          - identical
                        type: string
                      - type: 'null'
                    title: Result
              result_revisions:
                allOf:
                  - additionalProperties:
                      type: integer
                    default: {}
                    title: Result Revisions
                    type: object
              result_statuses:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: string
                        type: object
                      - type: 'null'
                    title: Result Statuses
              run_profiles:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Run Profiles
              runtime:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: Runtime
              sampling_confidence:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: Sampling Confidence
              sampling_ratio:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: Sampling Ratio
              sampling_threshold:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Sampling Threshold
              sampling_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    title: Sampling Tolerance
              source:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/JobSource'
                      - type: 'null'
              status:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/JobStatus'
                      - type: 'null'
              table1:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Table1
              table2:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Table2
              table_modifiers:
                allOf:
                  - anyOf:
                      - items:
                          $ref: '#/components/schemas/TableModifiers'
                        type: array
                      - type: 'null'
                    title: Table Modifiers
              tags:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Tags
              temp_schema_override:
                allOf:
                  - anyOf:
                      - items:
                          type: string
                        type: array
                      - type: 'null'
                    title: Temp Schema Override
              time_aggregate:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/TimeAggregateEnum'
                      - type: 'null'
              time_column:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Time Column
              time_interval_end:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Time Interval End
              time_interval_start:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Time Interval Start
              time_travel_point1:
                allOf:
                  - anyOf:
                      - type: integer
                      - format: date-time
                        type: string
                      - type: string
                      - type: 'null'
                    title: Time Travel Point1
              time_travel_point2:
                allOf:
                  - anyOf:
                      - type: integer
                      - format: date-time
                        type: string
                      - type: string
                      - type: 'null'
                    title: Time Travel Point2
              tolerance_mode:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ToleranceModeEnum'
                      - type: 'null'
              updated_at:
                allOf:
                  - anyOf:
                      - format: date-time
                        type: string
                      - type: 'null'
                    title: Updated At
              user_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: User Id
            title: ApiDataDiffWithProgressState
            refIdentifier: '#/components/schemas/ApiDataDiffWithProgressState'
            requiredProperties:
              - data_source1_id
              - data_source2_id
              - pk_columns
              - kind
        examples:
          example:
            value:
              affected_columns:
                - <string>
              algorithm: join
              archived: false
              bisection_factor: 123
              bisection_threshold: 123
              ci_base_branch: <string>
              ci_pr_branch: <string>
              ci_pr_num: 123
              ci_pr_sha: <string>
              ci_pr_url: <string>
              ci_pr_user_display_name: <string>
              ci_pr_user_email: <string>
              ci_pr_user_id: <string>
              ci_pr_username: <string>
              ci_run_id: 123
              ci_sha_url: <string>
              column_mapping:
                - - <any>
              columns_to_compare:
                - <string>
              compare_duplicates: true
              created_at: '2023-11-07T05:31:56Z'
              data_app_metadata:
                data_app_id: 123
                data_app_model1_id: <string>
                data_app_model1_name: <string>
                data_app_model2_id: <string>
                data_app_model2_name: <string>
                data_app_model_type: <string>
                meta_data: {}
              data_app_type: <string>
              data_source1_id: 123
              data_source1_session_parameters: {}
              data_source2_id: 123
              data_source2_session_parameters: {}
              diff_progress:
                completed_steps: 123
                total_steps: 123
                version: <string>
              diff_stats:
                diff_duplicate_pks: 123
                diff_null_pks: 123
                diff_pks: 123
                diff_ratio: 123
                diff_rows: 123
                diff_rows_count: 123
                diff_rows_number: 123
                diff_schema: 123
                diff_values: 123
                errors: 123
                exclusive_ratio: 123
                match_ratio: 123
                rows_added: 123
                rows_removed: 123
                sampled: true
                table_a_row_count: 123
                table_b_row_count: 123
                version: <string>
              diff_tolerance: 123
              diff_tolerances_per_column:
                - column_name: <string>
                  tolerance_mode: absolute
                  tolerance_value: 123
              done: true
              download_limit: 123
              exclude_columns:
                - <string>
              execute_as_user: true
              file1: <string>
              file1_options:
                delimiter: <string>
                file_type: csv
                skip_head_rows: 123
                skip_tail_rows: 123
              file2: <string>
              file2_options:
                delimiter: <string>
                file_type: <string>
                skip_head_rows: 123
                skip_tail_rows: 123
              filter1: <string>
              filter2: <string>
              finished_at: '2023-11-07T05:31:56Z'
              id: 123
              include_columns:
                - <string>
              kind: in_db
              materialization_destination_id: 123
              materialize_dataset1: true
              materialize_dataset2: true
              materialize_without_sampling: true
              monitor_error:
                error_type: <string>
                error_value: <string>
              monitor_id: 123
              monitor_state: ok
              per_column_diff_limit: 123
              pk_columns:
                - <string>
              purged: false
              query1: <string>
              query2: <string>
              result: error
              result_revisions: {}
              result_statuses: {}
              run_profiles: true
              runtime: 123
              sampling_confidence: 123
              sampling_ratio: 123
              sampling_threshold: 123
              sampling_tolerance: 123
              source: interactive
              status: needs_confirmation
              table1:
                - <string>
              table2:
                - <string>
              table_modifiers:
                - case_insensitive_strings
              tags:
                - <string>
              temp_schema_override:
                - <string>
              time_aggregate: minute
              time_column: <string>
              time_interval_end: '2023-11-07T05:31:56Z'
              time_interval_start: '2023-11-07T05:31:56Z'
              time_travel_point1: 123
              time_travel_point2: 123
              tolerance_mode: absolute
              updated_at: '2023-11-07T05:31:56Z'
              user_id: 123
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
    DiffAlgorithm:
      enum:
        - join
        - hash
        - hash_v2_alpha
        - fetch_and_join
      title: DiffAlgorithm
      type: string
    DiffKind:
      enum:
        - in_db
        - cross_db
      title: DiffKind
      type: string
    DiffProgress:
      properties:
        completed_steps:
          anyOf:
            - type: integer
            - type: 'null'
          title: Completed Steps
        total_steps:
          anyOf:
            - type: integer
            - type: 'null'
          title: Total Steps
        version:
          title: Version
          type: string
      required:
        - version
      title: DiffProgress
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
        diff_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Diff Ratio
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
        exclusive_ratio:
          anyOf:
            - type: number
            - type: 'null'
          title: Exclusive Ratio
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
    ParquetFileOptions:
      properties:
        file_type:
          const: parquet
          default: parquet
          title: File Type
          type: string
      title: ParquetFileOptions
      type: object
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