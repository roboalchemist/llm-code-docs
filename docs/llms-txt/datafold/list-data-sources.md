# Source: https://docs.datafold.com/api-reference/data-sources/list-data-sources.md

# List data sources

## OpenAPI

````yaml get /api/v1/data_sources
paths:
  path: /api/v1/data_sources
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - discriminator:
                    mapping:
                      athena: '#/components/schemas/ApiDataSourceAwsAthena'
                      aws_s3: '#/components/schemas/ApiDataSourceS3'
                      azure_synapse: '#/components/schemas/ApiDataSourceAzureSynapse'
                      bigquery: '#/components/schemas/ApiDataSourceBigQuery'
                      databricks: '#/components/schemas/ApiDataSourceDatabricks'
                      dremio: '#/components/schemas/ApiDataSourceDremio'
                      duckdb: '#/components/schemas/ApiDataSourceDuckDB'
                      files_azure_datalake: '#/components/schemas/ApiDataSourceAzureDataLake'
                      google_cloud_storage: '#/components/schemas/ApiDataSourceGCS'
                      mariadb: '#/components/schemas/ApiDataSourceMariaDB'
                      microsoft_fabric: '#/components/schemas/ApiDataSourceMicrosoftFabric'
                      mongodb: '#/components/schemas/ApiDataSourceMongoDB'
                      mssql: '#/components/schemas/ApiDataSourceMSSQL'
                      mysql: '#/components/schemas/ApiDataSourceMySQL'
                      netezza: '#/components/schemas/ApiDataSourceNetezza'
                      oracle: '#/components/schemas/ApiDataSourceOracle'
                      pg: '#/components/schemas/ApiDataSourcePostgres'
                      postgres_aurora: '#/components/schemas/ApiDataSourcePostgresAurora'
                      postgres_aws_rds: '#/components/schemas/ApiDataSourcePostgresRds'
                      redshift: '#/components/schemas/ApiDataSourceRedshift'
                      sap_hana: '#/components/schemas/ApiDataSourceSapHana'
                      snowflake: '#/components/schemas/ApiDataSourceSnowflake'
                      starburst: '#/components/schemas/ApiDataSourceStarburst'
                      teradata: '#/components/schemas/ApiDataSourceTeradata'
                      trino: '#/components/schemas/ApiDataSourceTrino'
                      vertica: '#/components/schemas/ApiDataSourceVertica'
                    propertyName: type
                  oneOf:
                    - $ref: '#/components/schemas/ApiDataSourceBigQuery'
                    - $ref: '#/components/schemas/ApiDataSourceDatabricks'
                    - $ref: '#/components/schemas/ApiDataSourceDuckDB'
                    - $ref: '#/components/schemas/ApiDataSourceMongoDB'
                    - $ref: '#/components/schemas/ApiDataSourceMySQL'
                    - $ref: '#/components/schemas/ApiDataSourceMariaDB'
                    - $ref: '#/components/schemas/ApiDataSourceMSSQL'
                    - $ref: '#/components/schemas/ApiDataSourceOracle'
                    - $ref: '#/components/schemas/ApiDataSourcePostgres'
                    - $ref: '#/components/schemas/ApiDataSourcePostgresAurora'
                    - $ref: '#/components/schemas/ApiDataSourcePostgresRds'
                    - $ref: '#/components/schemas/ApiDataSourceRedshift'
                    - $ref: '#/components/schemas/ApiDataSourceTeradata'
                    - $ref: '#/components/schemas/ApiDataSourceSapHana'
                    - $ref: '#/components/schemas/ApiDataSourceAwsAthena'
                    - $ref: '#/components/schemas/ApiDataSourceSnowflake'
                    - $ref: '#/components/schemas/ApiDataSourceDremio'
                    - $ref: '#/components/schemas/ApiDataSourceStarburst'
                    - $ref: '#/components/schemas/ApiDataSourceNetezza'
                    - $ref: '#/components/schemas/ApiDataSourceAzureDataLake'
                    - $ref: '#/components/schemas/ApiDataSourceGCS'
                    - $ref: '#/components/schemas/ApiDataSourceS3'
                    - $ref: '#/components/schemas/ApiDataSourceAzureSynapse'
                    - $ref: '#/components/schemas/ApiDataSourceMicrosoftFabric'
                    - $ref: '#/components/schemas/ApiDataSourceVertica'
                    - $ref: '#/components/schemas/ApiDataSourceTrino'
            title: Response List Data Sources Api V1 Data Sources Get
        examples:
          example:
            value:
              - catalog_exclude_list: <string>
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
    ApiDataSourceAwsAthena:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/AwsAthenaConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: athena
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceAwsAthena
      type: object
    ApiDataSourceAzureDataLake:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/AzureDataLakeConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: files_azure_datalake
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceAzureDataLake
      type: object
    ApiDataSourceAzureSynapse:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MSSQLConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: azure_synapse
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceAzureSynapse
      type: object
    ApiDataSourceBigQuery:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/BigQueryConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: bigquery
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceBigQuery
      type: object
    ApiDataSourceDatabricks:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/DatabricksConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: databricks
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceDatabricks
      type: object
    ApiDataSourceDremio:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/DremioConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: dremio
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceDremio
      type: object
    ApiDataSourceDuckDB:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/DuckDBConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: duckdb
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceDuckDB
      type: object
    ApiDataSourceGCS:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/GCSConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: google_cloud_storage
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceGCS
      type: object
    ApiDataSourceMSSQL:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MSSQLConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: mssql
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceMSSQL
      type: object
    ApiDataSourceMariaDB:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MariaDBConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: mariadb
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceMariaDB
      type: object
    ApiDataSourceMicrosoftFabric:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MicrosoftFabricConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: microsoft_fabric
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceMicrosoftFabric
      type: object
    ApiDataSourceMongoDB:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MongoDBConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: mongodb
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceMongoDB
      type: object
    ApiDataSourceMySQL:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/MySQLConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: mysql
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceMySQL
      type: object
    ApiDataSourceNetezza:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/NetezzaConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: netezza
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceNetezza
      type: object
    ApiDataSourceOracle:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/OracleConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: oracle
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceOracle
      type: object
    ApiDataSourcePostgres:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/PostgreSQLConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: pg
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourcePostgres
      type: object
    ApiDataSourcePostgresAurora:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: postgres_aurora
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourcePostgresAurora
      type: object
    ApiDataSourcePostgresRds:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: postgres_aws_rds
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourcePostgresRds
      type: object
    ApiDataSourceRedshift:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/RedshiftConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: redshift
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceRedshift
      type: object
    ApiDataSourceS3:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/AWSS3Config'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: aws_s3
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceS3
      type: object
    ApiDataSourceSapHana:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/SapHanaConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: sap_hana
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceSapHana
      type: object
    ApiDataSourceSnowflake:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/SnowflakeConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: snowflake
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceSnowflake
      type: object
    ApiDataSourceStarburst:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/StarburstConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: starburst
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceStarburst
      type: object
    ApiDataSourceTeradata:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/TeradataConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: teradata
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceTeradata
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
    ApiDataSourceTrino:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/TrinoConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: trino
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceTrino
      type: object
    ApiDataSourceVertica:
      properties:
        catalog_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Exclude List
        catalog_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Catalog Include List
        created_from:
          anyOf:
            - type: string
            - type: 'null'
          title: Created From
        data_retention_days:
          anyOf:
            - type: integer
            - type: 'null'
          title: Data Retention Days
        disable_profiling:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Profiling
        disable_schema_indexing:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Disable Schema Indexing
        float_tolerance:
          anyOf:
            - type: number
            - type: 'null'
          default: 0
          title: Float Tolerance
        groups:
          anyOf:
            - additionalProperties:
                type: boolean
              type: object
            - type: 'null'
          title: Groups
        hidden:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Hidden
        id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Id
        is_paused:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: Is Paused
        last_test:
          anyOf:
            - $ref: '#/components/schemas/ApiDataSourceTestStatus'
            - type: 'null'
        lineage_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Lineage Schedule
        max_allowed_connections:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Allowed Connections
        name:
          title: Name
          type: string
        oauth_dwh_active:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Oauth Dwh Active
        options:
          anyOf:
            - $ref: '#/components/schemas/VerticaConfig'
            - type: 'null'
        profile_exclude_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Exclude List
        profile_include_list:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Include List
        profile_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Profile Schedule
        queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Queue Name
        scheduled_queue_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Scheduled Queue Name
        schema_indexing_schedule:
          anyOf:
            - type: string
            - type: 'null'
          title: Schema Indexing Schedule
        schema_max_age_s:
          anyOf:
            - type: integer
            - type: 'null'
          title: Schema Max Age S
        secret_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Secret Id
        source:
          anyOf:
            - type: string
            - type: 'null'
          title: Source
        temp_schema:
          anyOf:
            - type: string
            - type: 'null'
          title: Temp Schema
        type:
          const: vertica
          title: Type
          type: string
        view_only:
          anyOf:
            - type: boolean
            - type: 'null'
          default: false
          title: View Only
      required:
        - name
        - type
      title: ApiDataSourceVertica
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