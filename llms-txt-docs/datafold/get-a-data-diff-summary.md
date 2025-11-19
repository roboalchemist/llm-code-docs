# Source: https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff-summary.md

# Get a data diff summary

## OpenAPI

````yaml get /api/v1/datadiffs/{datadiff_id}/summary_results
paths:
  path: /api/v1/datadiffs/{datadiff_id}/summary_results
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
              dependencies:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ApiCIDependency'
                    title: Dependencies
                    type: array
              materialized_results:
                allOf:
                  - $ref: '#/components/schemas/ApiMaterializedResults'
                    description: Results of the diff, materialized into tables.
              pks:
                allOf:
                  - $ref: '#/components/schemas/ApiDataDiffSummaryPKs'
              schema:
                allOf:
                  - $ref: '#/components/schemas/ApiDataDiffSummarySchema'
              status:
                allOf:
                  - enum:
                      - done
                      - success
                    title: Status
                    type: string
              values:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataDiffSummaryValues'
                      - type: 'null'
            title: ApiDataDiffSummaryForDone
            refIdentifier: '#/components/schemas/ApiDataDiffSummaryForDone'
            requiredProperties:
              - status
              - pks
              - dependencies
              - schema
              - materialized_results
          - type: object
            properties:
              pks:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataDiffSummaryPKs'
                      - type: 'null'
              status:
                allOf:
                  - enum:
                      - done
                      - success
                    title: Status
                    type: string
              values:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataDiffSummaryValues'
                      - type: 'null'
            title: ApiCrossDataDiffSummaryForDone
            refIdentifier: '#/components/schemas/ApiCrossDataDiffSummaryForDone'
            requiredProperties:
              - status
          - type: object
            properties:
              error:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataDiffError'
                      - additionalProperties: true
                        type: object
                    title: Error
              status:
                allOf:
                  - const: failed
                    title: Status
                    type: string
            title: ApiDataDiffSummaryForFailed
            refIdentifier: '#/components/schemas/ApiDataDiffSummaryForFailed'
            requiredProperties:
              - status
              - error
          - type: object
            properties:
              status:
                allOf:
                  - enum:
                      - running
                      - pending
                    title: Status
                    type: string
            title: ApiDataDiffSummaryForRunning
            refIdentifier: '#/components/schemas/ApiDataDiffSummaryForRunning'
            requiredProperties:
              - status
          - type: object
            properties:
              dependencies:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ApiCIDependency'
                    title: Dependencies
                    type: array
              status:
                allOf:
                  - enum:
                      - done
                      - success
                    title: Status
                    type: string
            title: InternalApiDataDiffDependencies
            refIdentifier: '#/components/schemas/InternalApiDataDiffDependencies'
            requiredProperties:
              - status
              - dependencies
        examples:
          example:
            value:
              dependencies:
                - data_source_id: 123
                  data_source_type: <string>
                  item_type: <string>
                  name: <string>
                  path:
                    - <string>
                  popularity: 123
                  primary_key: <string>
                  query_type: <string>
                  raw_sql: <string>
                  remote_id: <string>
                  table_name: <string>
                  uid: <string>
              materialized_results:
                diff:
                  - data_source_id: 123
                    is_sampled: true
                    path:
                      - <string>
                duplicates1:
                  - data_source_id: 123
                    is_sampled: true
                    path:
                      - <string>
                duplicates2:
                  - data_source_id: 123
                    is_sampled: true
                    path:
                      - <string>
                exclusives:
                  - data_source_id: 123
                    is_sampled: true
                    path:
                      - <string>
              pks:
                distincts:
                  - <any>
                dupes:
                  - <any>
                exclusives:
                  - <any>
                nulls:
                  - <any>
                total_rows:
                  - <any>
              schema:
                column_counts:
                  - <any>
                column_reorders: 123
                column_type_differs:
                  - <string>
                column_type_mismatches: 123
                columns_mismatched:
                  - <any>
                exclusive_columns:
                  - - <string>
              status: done
              values:
                columns_diff_stats:
                  - {}
                columns_with_differences: 123
                compared_columns: 123
                rows_with_differences: 123
                total_rows: 123
                total_values: 123
                values_with_differences: 123
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
    ApiCIDependency:
      properties:
        data_source_id:
          title: Data Source Id
          type: integer
        data_source_type:
          title: Data Source Type
          type: string
        item_type:
          title: Item Type
          type: string
        name:
          title: Name
          type: string
        path:
          items:
            type: string
          title: Path
          type: array
        popularity:
          anyOf:
            - type: integer
            - type: 'null'
          title: Popularity
        primary_key:
          anyOf:
            - type: string
            - type: 'null'
          title: Primary Key
        query_type:
          anyOf:
            - type: string
            - type: 'null'
          title: Query Type
        raw_sql:
          anyOf:
            - type: string
            - type: 'null'
          title: Raw Sql
        remote_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Remote Id
        table_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Table Name
        uid:
          title: Uid
          type: string
      required:
        - uid
        - item_type
        - name
        - path
        - data_source_id
        - data_source_type
      title: ApiCIDependency
      type: object
    ApiDataDiffError:
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
      title: ApiDataDiffError
      type: object
    ApiDataDiffSummaryPKs:
      properties:
        distincts:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Distincts
          type: array
        dupes:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Dupes
          type: array
        exclusives:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Exclusives
          type: array
        nulls:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Nulls
          type: array
        total_rows:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Total Rows
          type: array
      required:
        - total_rows
        - nulls
        - dupes
        - exclusives
        - distincts
      title: ApiDataDiffSummaryPKs
      type: object
    ApiDataDiffSummarySchema:
      properties:
        column_counts:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Column Counts
          type: array
        column_reorders:
          title: Column Reorders
          type: integer
        column_type_differs:
          items:
            type: string
          title: Column Type Differs
          type: array
        column_type_mismatches:
          title: Column Type Mismatches
          type: integer
        columns_mismatched:
          maxItems: 2
          minItems: 2
          prefixItems:
            - type: integer
            - type: integer
          title: Columns Mismatched
          type: array
        exclusive_columns:
          items:
            items:
              type: string
            type: array
          title: Exclusive Columns
          type: array
      required:
        - columns_mismatched
        - column_type_mismatches
        - column_reorders
        - column_counts
        - column_type_differs
        - exclusive_columns
      title: ApiDataDiffSummarySchema
      type: object
    ApiDataDiffSummaryValues:
      properties:
        columns_diff_stats:
          items:
            additionalProperties:
              anyOf:
                - type: number
                - type: string
            type: object
          title: Columns Diff Stats
          type: array
        columns_with_differences:
          title: Columns With Differences
          type: integer
        compared_columns:
          title: Compared Columns
          type: integer
        rows_with_differences:
          title: Rows With Differences
          type: integer
        total_rows:
          title: Total Rows
          type: integer
        total_values:
          title: Total Values
          type: integer
        values_with_differences:
          title: Values With Differences
          type: integer
      required:
        - total_rows
        - rows_with_differences
        - total_values
        - values_with_differences
        - compared_columns
        - columns_with_differences
        - columns_diff_stats
      title: ApiDataDiffSummaryValues
      type: object
    ApiMaterializedResult:
      properties:
        data_source_id:
          description: Id of the DataSource where the table is located
          title: Data Source Id
          type: integer
        is_sampled:
          description: If sampling was applied
          title: Is Sampled
          type: boolean
        path:
          description: Path segments of the table
          items:
            type: string
          title: Path
          type: array
      required:
        - data_source_id
        - path
        - is_sampled
      title: ApiMaterializedResult
      type: object
    ApiMaterializedResults:
      properties:
        diff:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiMaterializedResult'
              type: array
            - type: 'null'
          description: >-
            Results of row-to-row comparison between dataset A and B. Semantics
            is the same as for `exclusive_pks1` field.
          title: Diff
        duplicates1:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiMaterializedResult'
              type: array
            - type: 'null'
          description: >-
            Rows with duplicate primary keys detected in dataset A. Semantics is
            the same as for `exclusive_pks1` field.
          title: Duplicates1
        duplicates2:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiMaterializedResult'
              type: array
            - type: 'null'
          description: >-
            Rows with duplicate primary keys detected in dataset B. Semantics is
            the same as for `exclusive_pks1` field.
          title: Duplicates2
        exclusives:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiMaterializedResult'
              type: array
            - type: 'null'
          description: >-
            Rows with exclusive primary keys detected in dataset A and B. `None`
            if table is not ready yet or if materialization wasn't requested. If
            materialization is completed, for a diff inside a single database
            the field will contain a list with one element. If diff compares
            tables in different databases, the list may contain one or two
            entries.
          title: Exclusives
      title: ApiMaterializedResults
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