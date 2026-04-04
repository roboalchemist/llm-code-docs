# Source: https://docs.datafold.com/api-reference/data-diffs/get-a-data-diff-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a data diff summary



## OpenAPI

````yaml get /api/v1/datadiffs/{datadiff_id}/summary_results
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
  /api/v1/datadiffs/{datadiff_id}/summary_results:
    get:
      tags:
        - Data diffs
      summary: Get a data diff summary
      operationId: get_diff_summary_v1_api_v1_datadiffs__datadiff_id__summary_results_get
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
                anyOf:
                  - $ref: '#/components/schemas/ApiDataDiffSummaryForDone'
                  - $ref: '#/components/schemas/ApiCrossDataDiffSummaryForDone'
                  - $ref: '#/components/schemas/ApiDataDiffSummaryForFailed'
                  - $ref: '#/components/schemas/ApiDataDiffSummaryForRunning'
                  - $ref: '#/components/schemas/InternalApiDataDiffDependencies'
                title: >-
                  Response Get Diff Summary V1 Api V1 Datadiffs  Datadiff Id 
                  Summary Results Get
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiDataDiffSummaryForDone:
      properties:
        dependencies:
          items:
            $ref: '#/components/schemas/ApiCIDependency'
          title: Dependencies
          type: array
        materialized_results:
          $ref: '#/components/schemas/ApiMaterializedResults'
          description: Results of the diff, materialized into tables.
        pks:
          $ref: '#/components/schemas/ApiDataDiffSummaryPKs'
        schema:
          $ref: '#/components/schemas/ApiDataDiffSummarySchema'
        status:
          enum:
            - done
            - success
          title: Status
          type: string
        values:
          anyOf:
            - $ref: '#/components/schemas/ApiDataDiffSummaryValues'
            - type: 'null'
      required:
        - status
        - pks
        - dependencies
        - schema
        - materialized_results
      title: ApiDataDiffSummaryForDone
      type: object
    ApiCrossDataDiffSummaryForDone:
      properties:
        pks:
          anyOf:
            - $ref: '#/components/schemas/ApiDataDiffSummaryPKs'
            - type: 'null'
        status:
          enum:
            - done
            - success
          title: Status
          type: string
        values:
          anyOf:
            - $ref: '#/components/schemas/ApiDataDiffSummaryValues'
            - type: 'null'
      required:
        - status
      title: ApiCrossDataDiffSummaryForDone
      type: object
    ApiDataDiffSummaryForFailed:
      properties:
        error:
          anyOf:
            - $ref: '#/components/schemas/ApiDataDiffError'
            - additionalProperties: true
              type: object
          title: Error
        status:
          const: failed
          title: Status
          type: string
      required:
        - status
        - error
      title: ApiDataDiffSummaryForFailed
      type: object
    ApiDataDiffSummaryForRunning:
      properties:
        status:
          enum:
            - running
            - pending
          title: Status
          type: string
      required:
        - status
      title: ApiDataDiffSummaryForRunning
      type: object
    InternalApiDataDiffDependencies:
      properties:
        dependencies:
          items:
            $ref: '#/components/schemas/ApiCIDependency'
          title: Dependencies
          type: array
        status:
          enum:
            - done
            - success
          title: Status
          type: string
      required:
        - status
        - dependencies
      title: InternalApiDataDiffDependencies
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
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````