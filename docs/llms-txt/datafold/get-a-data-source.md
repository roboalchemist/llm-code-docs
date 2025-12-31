# Source: https://docs.datafold.com/api-reference/data-sources/get-a-data-source.md

# Get a data source

## OpenAPI

````yaml get /api/v1/data_sources/{data_source_id}
paths:
  path: /api/v1/data_sources/{data_source_id}
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
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/BigQueryConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: bigquery
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceBigQuery
            refIdentifier: '#/components/schemas/ApiDataSourceBigQuery'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DatabricksConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: databricks
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceDatabricks
            refIdentifier: '#/components/schemas/ApiDataSourceDatabricks'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DuckDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: duckdb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceDuckDB
            refIdentifier: '#/components/schemas/ApiDataSourceDuckDB'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MongoDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: mongodb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceMongoDB
            refIdentifier: '#/components/schemas/ApiDataSourceMongoDB'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MySQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: mysql
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceMySQL
            refIdentifier: '#/components/schemas/ApiDataSourceMySQL'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MariaDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: mariadb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceMariaDB
            refIdentifier: '#/components/schemas/ApiDataSourceMariaDB'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MSSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: mssql
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceMSSQL
            refIdentifier: '#/components/schemas/ApiDataSourceMSSQL'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/OracleConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: oracle
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceOracle
            refIdentifier: '#/components/schemas/ApiDataSourceOracle'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/PostgreSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: pg
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourcePostgres
            refIdentifier: '#/components/schemas/ApiDataSourcePostgres'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: postgres_aurora
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourcePostgresAurora
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresAurora'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: postgres_aws_rds
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourcePostgresRds
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresRds'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/RedshiftConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: redshift
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceRedshift
            refIdentifier: '#/components/schemas/ApiDataSourceRedshift'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/TeradataConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: teradata
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceTeradata
            refIdentifier: '#/components/schemas/ApiDataSourceTeradata'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/SapHanaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: sap_hana
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceSapHana
            refIdentifier: '#/components/schemas/ApiDataSourceSapHana'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AwsAthenaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: athena
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceAwsAthena
            refIdentifier: '#/components/schemas/ApiDataSourceAwsAthena'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/SnowflakeConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: snowflake
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceSnowflake
            refIdentifier: '#/components/schemas/ApiDataSourceSnowflake'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/DremioConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: dremio
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceDremio
            refIdentifier: '#/components/schemas/ApiDataSourceDremio'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/StarburstConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: starburst
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceStarburst
            refIdentifier: '#/components/schemas/ApiDataSourceStarburst'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/NetezzaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: netezza
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceNetezza
            refIdentifier: '#/components/schemas/ApiDataSourceNetezza'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AzureDataLakeConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: files_azure_datalake
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceAzureDataLake
            refIdentifier: '#/components/schemas/ApiDataSourceAzureDataLake'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/GCSConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: google_cloud_storage
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceGCS
            refIdentifier: '#/components/schemas/ApiDataSourceGCS'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/AWSS3Config'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: aws_s3
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceS3
            refIdentifier: '#/components/schemas/ApiDataSourceS3'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MSSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: azure_synapse
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceAzureSynapse
            refIdentifier: '#/components/schemas/ApiDataSourceAzureSynapse'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/MicrosoftFabricConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: microsoft_fabric
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceMicrosoftFabric
            refIdentifier: '#/components/schemas/ApiDataSourceMicrosoftFabric'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/VerticaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: vertica
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceVertica
            refIdentifier: '#/components/schemas/ApiDataSourceVertica'
            requiredProperties:
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - anyOf:
                      - $ref: '#/components/schemas/TrinoConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - const: trino
                    title: Type
                    type: string
              view_only:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            title: ApiDataSourceTrino
            refIdentifier: '#/components/schemas/ApiDataSourceTrino'
            requiredProperties:
              - name
              - type
        examples:
          example:
            value:
              catalog_exclude_list: <string>
              catalog_include_list: <string>
              created_from: <string>
              data_retention_days: 123
              disable_profiling: true
              disable_schema_indexing: true
              float_tolerance: 123
              groups: {}
              hidden: true
              id: 123
              is_paused: true
              last_test:
                results:
                  - result: <any>
                    status: needs_confirmation
                    step: connection
                tested_at: '2023-11-07T05:31:56Z'
              lineage_schedule: <string>
              max_allowed_connections: 123
              name: <string>
              oauth_dwh_active: true
              options:
                extraProjectsToIndex: |-
                  project1
                  project2
                jsonOAuthKeyFile: <string>
                location: US
                projectId: <string>
                totalMBytesProcessedLimit: 123
                useStandardSql: true
                userDefinedFunctionResourceUri: gs://bucket/date_utils.js
              profile_exclude_list: <string>
              profile_include_list: <string>
              profile_schedule: <string>
              queue_name: <string>
              scheduled_queue_name: <string>
              schema_indexing_schedule: <string>
              schema_max_age_s: 123
              secret_id: 123
              source: <string>
              temp_schema: <string>
              type: <string>
              view_only: true
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
    AWSS3Config:
      properties:
        bucket_name:
          title: Bucket Name
          type: string
        key_id:
          anyOf:
            - maxLength: 1024
              type: string
            - type: 'null'
          title: Key Id
        materialize_max_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Materialize Max Rows
        materialize_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Materialize Path
        region:
          title: Region
          type: string
        secret:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Secret
      required:
        - bucket_name
        - key_id
        - region
      title: AWSS3Config
      type: object
    ApiDataSourceTestStatus:
      properties:
        results:
          items:
            $ref: '#/components/schemas/TestResultStep'
          title: Results
          type: array
        tested_at:
          format: date-time
          title: Tested At
          type: string
      required:
        - tested_at
        - results
      title: ApiDataSourceTestStatus
      type: object
    AwsAthenaConfig:
      properties:
        aws_access_key_id:
          title: Aws Access Key Id
          type: string
        aws_secret_access_key:
          format: password
          title: Aws Secret Access Key
          type: string
          writeOnly: true
        catalog:
          default: awsdatacatalog
          title: Catalog
          type: string
        database:
          default: default
          title: Database
          type: string
        region:
          title: Region
          type: string
        s3_staging_dir:
          format: uri
          minLength: 1
          title: S3 Staging Dir
          type: string
      required:
        - aws_access_key_id
        - aws_secret_access_key
        - s3_staging_dir
        - region
      title: AwsAthenaConfig
      type: object
    AzureDataLakeConfig:
      properties:
        account_name:
          title: Account Name
          type: string
        client_id:
          anyOf:
            - maxLength: 1024
              type: string
            - type: 'null'
          title: Client Id
        client_secret:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Client Secret
        materialize_max_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Materialize Max Rows
        materialize_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Materialize Path
        tenant_id:
          anyOf:
            - maxLength: 1024
              type: string
            - type: 'null'
          title: Tenant Id
      required:
        - account_name
        - tenant_id
        - client_id
      title: AzureDataLakeConfig
      type: object
    BigQueryConfig:
      properties:
        extraProjectsToIndex:
          anyOf:
            - type: string
            - type: 'null'
          examples:
            - |-
              project1
              project2
          section: config
          title: List of extra projects to index (one per line)
          widget: multiline
        jsonKeyFile:
          format: password
          section: basic
          title: JSON Key File
          type: string
          writeOnly: true
        jsonOAuthKeyFile:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          section: basic
          title: JSON OAuth Key File
        location:
          default: US
          examples:
            - US
          section: basic
          title: Processing Location
          type: string
        projectId:
          section: basic
          title: Project ID
          type: string
        totalMBytesProcessedLimit:
          anyOf:
            - type: integer
            - type: 'null'
          section: config
          title: Scanned Data Limit (MB)
        useStandardSql:
          default: true
          section: config
          title: Use Standard SQL
          type: boolean
        userDefinedFunctionResourceUri:
          anyOf:
            - type: string
            - type: 'null'
          examples:
            - gs://bucket/date_utils.js
          section: config
          title: UDF Source URIs
      required:
        - projectId
        - jsonKeyFile
      title: BigQueryConfig
      type: object
    CertCheck:
      enum:
        - disable
        - dremio-cloud
        - customcert
      title: CertCheck
      type: string
    ConfigurationCheckStep:
      enum:
        - connection
        - temp_schema
        - schema_download
        - lineage_download
      title: ConfigurationCheckStep
      type: string
    DatabricksConfig:
      properties:
        database:
          anyOf:
            - type: string
            - type: 'null'
          title: Database
        host:
          maxLength: 128
          title: Host
          type: string
        http_password:
          format: password
          title: Access Token
          type: string
          writeOnly: true
        http_path:
          default: ''
          title: HTTP Path
          type: string
        oauth_dwh_client_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Oauth Dwh Client Id
        oauth_dwh_client_secret:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Oauth Dwh Client Secret
      required:
        - host
        - http_password
      title: DatabricksConfig
      type: object
    DremioConfig:
      properties:
        certcheck:
          anyOf:
            - $ref: '#/components/schemas/CertCheck'
            - type: 'null'
          default: dremio-cloud
          title: Certificate check
        customcert:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Custom certificate
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 443
          title: Port
          type: integer
        project_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Project id
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role (case sensitive)
        tls:
          default: false
          title: Encryption
          type: boolean
        token:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Token
        username:
          anyOf:
            - type: string
            - type: 'null'
          title: User ID (optional)
        view_temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temporary schema for views
      required:
        - host
      title: DremioConfig
      type: object
    DuckDBConfig:
      properties: {}
      title: DuckDBConfig
      type: object
    GCSConfig:
      properties:
        bucket_name:
          title: Bucket Name
          type: string
        bucket_region:
          title: Bucket Region
          type: string
        jsonKeyFile:
          format: password
          section: basic
          title: JSON Key File
          type: string
          writeOnly: true
        materialize_max_rows:
          anyOf:
            - type: integer
            - type: 'null'
          title: Materialize Max Rows
        materialize_path:
          anyOf:
            - type: string
            - type: 'null'
          title: Materialize Path
      required:
        - bucket_name
        - jsonKeyFile
        - bucket_region
      title: GCSConfig
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
    MSSQLConfig:
      properties:
        dbname:
          anyOf:
            - type: string
            - type: 'null'
          title: Dbname
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 1433
          title: Port
          type: integer
        require_encryption:
          default: false
          title: Require Encryption
          type: boolean
        session_script:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            The script to execute on connection; e.g. ALTER SESSION SET
            CONTAINER = ...
          title: Init script
        trust_server_certificate:
          default: false
          title: Trust Server Certificate
          type: boolean
        user:
          default: DATAFOLD
          title: User
          type: string
      required:
        - host
      title: MSSQLConfig
      type: object
    MariaDBConfig:
      description: |-
        Configuration for MariaDB connections.

        MariaDB is MySQL-compatible, so we reuse the MySQL configuration.
        Default port is 3306, same as MySQL.
      properties:
        db:
          title: Database name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          format: password
          title: Password
          type: string
          writeOnly: true
        port:
          default: 3306
          title: Port
          type: integer
        user:
          title: User
          type: string
      required:
        - host
        - user
        - password
        - db
      title: MariaDBConfig
      type: object
    MicrosoftFabricConfig:
      properties:
        client_id:
          description: Microsoft Entra ID Application (Client) ID
          title: Application (Client) ID
          type: string
        client_secret:
          description: Microsoft Entra ID Application Client Secret
          format: password
          title: Client Secret
          type: string
          writeOnly: true
        dbname:
          title: Dbname
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        session_script:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            The script to execute on connection; e.g. ALTER SESSION SET
            CONTAINER = ...
          title: Init script
        tenant_id:
          description: Microsoft Entra ID Tenant ID
          title: Tenant ID
          type: string
      required:
        - host
        - dbname
        - tenant_id
        - client_id
        - client_secret
      title: MicrosoftFabricConfig
      type: object
    MongoDBConfig:
      properties:
        auth_source:
          anyOf:
            - type: string
            - type: 'null'
          default: admin
          title: Auth Source
        database:
          title: Database
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          format: password
          title: Password
          type: string
          writeOnly: true
        port:
          default: 27017
          title: Port
          type: integer
        username:
          title: Username
          type: string
      required:
        - database
        - username
        - password
        - host
      title: MongoDBConfig
      type: object
    MySQLConfig:
      properties:
        db:
          title: Database name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          format: password
          title: Password
          type: string
          writeOnly: true
        port:
          default: 3306
          title: Port
          type: integer
        user:
          title: User
          type: string
      required:
        - host
        - user
        - password
        - db
      title: MySQLConfig
      type: object
    NetezzaConfig:
      properties:
        database:
          maxLength: 128
          title: Database
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 5480
          title: Port
          type: integer
        tls:
          default: true
          title: Encryption
          type: boolean
        username:
          anyOf:
            - type: string
            - type: 'null'
          title: User ID (optional)
      required:
        - host
        - database
      title: NetezzaConfig
      type: object
    OracleConfig:
      properties:
        database:
          anyOf:
            - type: string
            - type: 'null'
          title: Database
        database_type:
          anyOf:
            - enum:
                - service
                - sid
              type: string
            - type: 'null'
          title: Database Type
        ewallet_password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: EWallet password
        ewallet_pem_file:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: EWallet PEM
        ewallet_pkcs12_file:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: EWallet PKCS12
        ewallet_type:
          anyOf:
            - enum:
                - x509
                - pkcs12
              type: string
            - type: 'null'
          title: Ewallet Type
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          anyOf:
            - type: integer
            - type: 'null'
          title: Port
        session_script:
          anyOf:
            - type: string
            - type: 'null'
          description: >-
            The script to execute on connection; e.g. ALTER SESSION SET
            CONTAINER = ...
          title: Init script
        ssl:
          default: false
          title: Ssl
          type: boolean
        ssl_server_dn:
          anyOf:
            - type: string
            - type: 'null'
          description: 'e.g. C=US,O=example,CN=db.example.com; default: CN=<hostname>'
          title: Server's SSL DN
        user:
          default: DATAFOLD
          title: User
          type: string
      required:
        - host
      title: OracleConfig
      type: object
    PostgreSQLAuroraConfig:
      properties:
        aws_access_key_id:
          anyOf:
            - type: string
            - type: 'null'
          title: AWS Access Key
        aws_cloudwatch_log_group:
          anyOf:
            - type: string
            - type: 'null'
          title: Cloudwatch Postgres Log Group
        aws_region:
          anyOf:
            - type: string
            - type: 'null'
          title: AWS Region
        aws_secret_access_key:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: AWS Secret
        dbname:
          title: Database Name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        keep_alive:
          anyOf:
            - type: integer
            - type: 'null'
          title: Keep Alive timeout in seconds, leave empty to disable
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 5432
          title: Port
          type: integer
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role (case sensitive)
        rootcert:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Root certificate
        sslmode:
          $ref: '#/components/schemas/SslMode'
          default: prefer
          title: SSL Mode
        user:
          title: User
          type: string
      required:
        - host
        - user
        - dbname
      title: PostgreSQLAuroraConfig
      type: object
    PostgreSQLConfig:
      properties:
        dbname:
          title: Database Name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 5432
          title: Port
          type: integer
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role (case sensitive)
        rootcert:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Root certificate
        sslmode:
          $ref: '#/components/schemas/SslMode'
          default: prefer
          title: SSL Mode
        user:
          title: User
          type: string
      required:
        - host
        - user
        - dbname
      title: PostgreSQLConfig
      type: object
    RedshiftConfig:
      properties:
        adhoc_query_group:
          default: default
          section: config
          title: Query Group for Adhoc Queries
          type: string
        dbname:
          title: Database Name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 5432
          title: Port
          type: integer
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role (case sensitive)
        rootcert:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Root certificate
        scheduled_query_group:
          default: default
          section: config
          title: Query Group for Scheduled Queries
          type: string
        sslmode:
          $ref: '#/components/schemas/SslMode'
          default: prefer
          title: SSL Mode
        user:
          title: User
          type: string
      required:
        - host
        - user
        - dbname
      title: RedshiftConfig
      type: object
    SSLVerification:
      enum:
        - full
        - none
        - ca
      title: SSLVerification
      type: string
    SapHanaConfig:
      properties:
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          format: password
          title: Password
          type: string
          writeOnly: true
        port:
          default: 443
          title: Port
          type: integer
        user:
          default: DATAFOLD
          title: User
          type: string
      required:
        - host
        - password
      title: SapHanaConfig
      type: object
    SnowflakeConfig:
      properties:
        account:
          maxLength: 128
          title: Account
          type: string
        authMethod:
          anyOf:
            - enum:
                - password
                - keypair
              type: string
            - type: 'null'
          title: Authmethod
        data_source_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Source Id
        default_db:
          default: ''
          examples:
            - MY_DB
          title: Default DB (case sensitive)
          type: string
        default_schema:
          default: PUBLIC
          examples:
            - PUBLIC
          section: config
          title: Default schema (case sensitive)
          type: string
        keyPairFile:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Key Pair file (private-key)
        metadata_database:
          default: SNOWFLAKE
          examples:
            - SNOWFLAKE
          section: config
          title: Database containing metadata (usually SNOWFLAKE)
          type: string
        oauth_dwh_client_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Oauth Dwh Client Id
        oauth_dwh_client_secret:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Oauth Dwh Client Secret
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          anyOf:
            - type: integer
            - type: 'null'
          default: 443
          title: Port
        region:
          anyOf:
            - type: string
            - type: 'null'
          section: config
          title: Region
        role:
          default: ''
          examples:
            - PUBLIC
          title: Role (case sensitive)
          type: string
        sql_variables:
          anyOf:
            - type: string
            - type: 'null'
          examples:
            - |-
              variable_1=10
              variable_2=test
          section: config
          title: Session variables applied at every connection.
          widget: multiline
        user:
          default: DATAFOLD
          title: User
          type: string
        user_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: User Id
        warehouse:
          default: ''
          examples:
            - COMPUTE_WH
          title: Warehouse (case sensitive)
          type: string
      required:
        - account
      title: SnowflakeConfig
      type: object
    SslMode:
      enum:
        - prefer
        - require
        - verify-ca
        - verify-full
      title: SslMode
      type: string
    StarburstConfig:
      properties:
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 443
          title: Port
          type: integer
        tls:
          default: true
          title: Encryption
          type: boolean
        token:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Token
        username:
          anyOf:
            - type: string
            - type: 'null'
          title: User ID (optional)
      required:
        - host
      title: StarburstConfig
      type: object
    TeradataConfig:
      properties:
        database:
          title: Database
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          format: password
          title: Password
          type: string
          writeOnly: true
        port:
          anyOf:
            - type: integer
            - type: 'null'
          title: Port
        user:
          default: DATAFOLD
          title: User
          type: string
      required:
        - host
        - password
        - database
      title: TeradataConfig
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
    TrinoConfig:
      properties:
        dbname:
          title: Catalog Name
          type: string
        hive_timestamp_precision:
          anyOf:
            - enum:
                - 3
                - 6
                - 9
              type: integer
            - type: 'null'
          description: 'Optional: Timestamp precision if using Hive connector'
          title: Hive Timestamp Precision
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 8080
          title: Port
          type: integer
        ssl_verification:
          $ref: '#/components/schemas/SSLVerification'
          default: full
          title: SSL Verification
        tls:
          default: true
          title: Encryption
          type: boolean
        user:
          title: User
          type: string
      required:
        - host
        - user
        - dbname
      title: TrinoConfig
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
    VerticaConfig:
      properties:
        dbname:
          title: Database Name
          type: string
        host:
          maxLength: 128
          title: Host
          type: string
        password:
          anyOf:
            - format: password
              type: string
              writeOnly: true
            - type: 'null'
          title: Password
        port:
          default: 5433
          title: Port
          type: integer
        role:
          anyOf:
            - type: string
            - type: 'null'
          title: Role (case sensitive)
        sslmode:
          $ref: '#/components/schemas/SslMode'
          default: prefer
          title: SSL Mode
        user:
          title: User
          type: string
      required:
        - host
        - user
        - dbname
      title: VerticaConfig
      type: object

````