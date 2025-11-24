# Source: https://docs.datafold.com/api-reference/data-sources/create-a-data-source.md

# Create a data source

## OpenAPI

````yaml post /api/v1/data_sources
paths:
  path: /api/v1/data_sources
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
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_0
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_1
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_2
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_3
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_4
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_5
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_6
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_7
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_8
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_9
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_10
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_11
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_12
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_13
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_14
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_15
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_16
                    anyOf:
                      - $ref: '#/components/schemas/BigQueryConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_17
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_18
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_19
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_20
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_21
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_22
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_23
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_24
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_25
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_26
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_27
                    const: bigquery
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_28
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceBigQuery
            refIdentifier: '#/components/schemas/ApiDataSourceBigQuery'
            requiredProperties: &ref_29
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_30
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_31
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_32
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_33
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_34
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_35
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_36
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_37
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_38
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_39
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_40
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_41
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_42
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_43
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_44
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_45
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_46
                    anyOf:
                      - $ref: '#/components/schemas/DatabricksConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_47
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_48
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_49
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_50
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_51
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_52
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_53
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_54
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_55
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_56
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_57
                    const: databricks
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_58
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceDatabricks
            refIdentifier: '#/components/schemas/ApiDataSourceDatabricks'
            requiredProperties: &ref_59
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_60
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_61
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_62
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_63
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_64
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_65
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_66
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_67
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_68
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_69
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_70
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_71
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_72
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_73
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_74
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_75
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_76
                    anyOf:
                      - $ref: '#/components/schemas/DuckDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_77
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_78
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_79
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_80
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_81
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_82
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_83
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_84
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_85
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_86
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_87
                    const: duckdb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_88
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceDuckDB
            refIdentifier: '#/components/schemas/ApiDataSourceDuckDB'
            requiredProperties: &ref_89
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_90
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_91
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_92
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_93
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_94
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_95
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_96
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_97
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_98
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_99
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_100
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_101
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_102
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_103
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_104
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_105
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_106
                    anyOf:
                      - $ref: '#/components/schemas/MongoDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_107
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_108
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_109
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_110
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_111
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_112
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_113
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_114
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_115
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_116
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_117
                    const: mongodb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_118
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceMongoDB
            refIdentifier: '#/components/schemas/ApiDataSourceMongoDB'
            requiredProperties: &ref_119
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_120
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_121
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_122
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_123
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_124
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_125
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_126
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_127
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_128
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_129
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_130
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_131
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_132
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_133
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_134
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_135
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_136
                    anyOf:
                      - $ref: '#/components/schemas/MySQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_137
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_138
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_139
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_140
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_141
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_142
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_143
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_144
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_145
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_146
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_147
                    const: mysql
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_148
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceMySQL
            refIdentifier: '#/components/schemas/ApiDataSourceMySQL'
            requiredProperties: &ref_149
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_150
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_151
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_152
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_153
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_154
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_155
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_156
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_157
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_158
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_159
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_160
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_161
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_162
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_163
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_164
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_165
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_166
                    anyOf:
                      - $ref: '#/components/schemas/MariaDBConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_167
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_168
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_169
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_170
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_171
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_172
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_173
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_174
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_175
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_176
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_177
                    const: mariadb
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_178
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceMariaDB
            refIdentifier: '#/components/schemas/ApiDataSourceMariaDB'
            requiredProperties: &ref_179
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_180
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_181
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_182
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_183
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_184
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_185
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_186
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_187
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_188
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_189
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_190
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_191
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_192
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_193
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_194
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_195
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_196
                    anyOf:
                      - $ref: '#/components/schemas/MSSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_197
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_198
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_199
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_200
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_201
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_202
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_203
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_204
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_205
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_206
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_207
                    const: mssql
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_208
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceMSSQL
            refIdentifier: '#/components/schemas/ApiDataSourceMSSQL'
            requiredProperties: &ref_209
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_210
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_211
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_212
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_213
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_214
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_215
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_216
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_217
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_218
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_219
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_220
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_221
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_222
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_223
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_224
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_225
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_226
                    anyOf:
                      - $ref: '#/components/schemas/OracleConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_227
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_228
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_229
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_230
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_231
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_232
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_233
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_234
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_235
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_236
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_237
                    const: oracle
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_238
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceOracle
            refIdentifier: '#/components/schemas/ApiDataSourceOracle'
            requiredProperties: &ref_239
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_240
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_241
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_242
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_243
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_244
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_245
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_246
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_247
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_248
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_249
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_250
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_251
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_252
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_253
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_254
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_255
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_256
                    anyOf:
                      - $ref: '#/components/schemas/PostgreSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_257
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_258
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_259
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_260
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_261
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_262
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_263
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_264
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_265
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_266
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_267
                    const: pg
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_268
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourcePostgres
            refIdentifier: '#/components/schemas/ApiDataSourcePostgres'
            requiredProperties: &ref_269
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_270
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_271
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_272
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_273
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_274
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_275
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_276
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_277
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_278
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_279
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_280
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_281
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_282
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_283
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_284
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_285
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_286
                    anyOf:
                      - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_287
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_288
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_289
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_290
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_291
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_292
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_293
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_294
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_295
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_296
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_297
                    const: postgres_aurora
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_298
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourcePostgresAurora
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresAurora'
            requiredProperties: &ref_299
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_300
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_301
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_302
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_303
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_304
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_305
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_306
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_307
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_308
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_309
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_310
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_311
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_312
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_313
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_314
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_315
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_316
                    anyOf:
                      - $ref: '#/components/schemas/PostgreSQLAuroraConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_317
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_318
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_319
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_320
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_321
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_322
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_323
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_324
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_325
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_326
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_327
                    const: postgres_aws_rds
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_328
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourcePostgresRds
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresRds'
            requiredProperties: &ref_329
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_330
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_331
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_332
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_333
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_334
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_335
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_336
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_337
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_338
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_339
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_340
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_341
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_342
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_343
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_344
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_345
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_346
                    anyOf:
                      - $ref: '#/components/schemas/RedshiftConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_347
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_348
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_349
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_350
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_351
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_352
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_353
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_354
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_355
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_356
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_357
                    const: redshift
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_358
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceRedshift
            refIdentifier: '#/components/schemas/ApiDataSourceRedshift'
            requiredProperties: &ref_359
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_360
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_361
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_362
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_363
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_364
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_365
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_366
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_367
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_368
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_369
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_370
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_371
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_372
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_373
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_374
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_375
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_376
                    anyOf:
                      - $ref: '#/components/schemas/TeradataConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_377
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_378
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_379
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_380
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_381
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_382
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_383
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_384
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_385
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_386
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_387
                    const: teradata
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_388
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceTeradata
            refIdentifier: '#/components/schemas/ApiDataSourceTeradata'
            requiredProperties: &ref_389
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_390
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_391
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_392
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_393
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_394
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_395
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_396
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_397
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_398
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_399
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_400
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_401
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_402
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_403
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_404
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_405
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_406
                    anyOf:
                      - $ref: '#/components/schemas/SapHanaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_407
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_408
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_409
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_410
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_411
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_412
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_413
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_414
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_415
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_416
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_417
                    const: sap_hana
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_418
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceSapHana
            refIdentifier: '#/components/schemas/ApiDataSourceSapHana'
            requiredProperties: &ref_419
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_420
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_421
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_422
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_423
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_424
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_425
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_426
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_427
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_428
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_429
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_430
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_431
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_432
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_433
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_434
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_435
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_436
                    anyOf:
                      - $ref: '#/components/schemas/AwsAthenaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_437
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_438
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_439
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_440
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_441
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_442
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_443
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_444
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_445
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_446
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_447
                    const: athena
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_448
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceAwsAthena
            refIdentifier: '#/components/schemas/ApiDataSourceAwsAthena'
            requiredProperties: &ref_449
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_450
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_451
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_452
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_453
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_454
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_455
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_456
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_457
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_458
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_459
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_460
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_461
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_462
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_463
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_464
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_465
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_466
                    anyOf:
                      - $ref: '#/components/schemas/SnowflakeConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_467
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_468
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_469
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_470
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_471
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_472
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_473
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_474
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_475
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_476
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_477
                    const: snowflake
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_478
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceSnowflake
            refIdentifier: '#/components/schemas/ApiDataSourceSnowflake'
            requiredProperties: &ref_479
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_480
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_481
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_482
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_483
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_484
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_485
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_486
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_487
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_488
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_489
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_490
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_491
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_492
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_493
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_494
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_495
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_496
                    anyOf:
                      - $ref: '#/components/schemas/DremioConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_497
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_498
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_499
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_500
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_501
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_502
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_503
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_504
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_505
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_506
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_507
                    const: dremio
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_508
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceDremio
            refIdentifier: '#/components/schemas/ApiDataSourceDremio'
            requiredProperties: &ref_509
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_510
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_511
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_512
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_513
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_514
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_515
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_516
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_517
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_518
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_519
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_520
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_521
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_522
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_523
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_524
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_525
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_526
                    anyOf:
                      - $ref: '#/components/schemas/StarburstConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_527
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_528
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_529
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_530
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_531
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_532
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_533
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_534
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_535
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_536
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_537
                    const: starburst
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_538
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceStarburst
            refIdentifier: '#/components/schemas/ApiDataSourceStarburst'
            requiredProperties: &ref_539
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_540
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_541
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_542
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_543
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_544
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_545
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_546
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_547
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_548
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_549
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_550
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_551
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_552
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_553
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_554
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_555
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_556
                    anyOf:
                      - $ref: '#/components/schemas/NetezzaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_557
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_558
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_559
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_560
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_561
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_562
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_563
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_564
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_565
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_566
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_567
                    const: netezza
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_568
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceNetezza
            refIdentifier: '#/components/schemas/ApiDataSourceNetezza'
            requiredProperties: &ref_569
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_570
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_571
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_572
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_573
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_574
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_575
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_576
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_577
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_578
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_579
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_580
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_581
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_582
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_583
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_584
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_585
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_586
                    anyOf:
                      - $ref: '#/components/schemas/AzureDataLakeConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_587
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_588
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_589
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_590
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_591
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_592
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_593
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_594
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_595
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_596
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_597
                    const: files_azure_datalake
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_598
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceAzureDataLake
            refIdentifier: '#/components/schemas/ApiDataSourceAzureDataLake'
            requiredProperties: &ref_599
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_600
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_601
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_602
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_603
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_604
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_605
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_606
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_607
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_608
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_609
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_610
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_611
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_612
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_613
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_614
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_615
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_616
                    anyOf:
                      - $ref: '#/components/schemas/GCSConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_617
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_618
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_619
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_620
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_621
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_622
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_623
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_624
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_625
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_626
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_627
                    const: google_cloud_storage
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_628
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceGCS
            refIdentifier: '#/components/schemas/ApiDataSourceGCS'
            requiredProperties: &ref_629
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_630
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_631
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_632
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_633
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_634
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_635
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_636
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_637
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_638
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_639
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_640
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_641
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_642
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_643
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_644
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_645
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_646
                    anyOf:
                      - $ref: '#/components/schemas/AWSS3Config'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_647
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_648
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_649
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_650
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_651
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_652
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_653
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_654
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_655
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_656
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_657
                    const: aws_s3
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_658
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceS3
            refIdentifier: '#/components/schemas/ApiDataSourceS3'
            requiredProperties: &ref_659
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_660
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_661
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_662
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_663
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_664
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_665
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_666
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_667
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_668
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_669
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_670
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_671
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_672
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_673
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_674
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_675
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_676
                    anyOf:
                      - $ref: '#/components/schemas/MSSQLConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_677
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_678
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_679
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_680
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_681
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_682
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_683
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_684
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_685
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_686
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_687
                    const: azure_synapse
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_688
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceAzureSynapse
            refIdentifier: '#/components/schemas/ApiDataSourceAzureSynapse'
            requiredProperties: &ref_689
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_690
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_691
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_692
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_693
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_694
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_695
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_696
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_697
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_698
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_699
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_700
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_701
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_702
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_703
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_704
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_705
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_706
                    anyOf:
                      - $ref: '#/components/schemas/MicrosoftFabricConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_707
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_708
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_709
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_710
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_711
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_712
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_713
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_714
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_715
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_716
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_717
                    const: microsoft_fabric
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_718
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceMicrosoftFabric
            refIdentifier: '#/components/schemas/ApiDataSourceMicrosoftFabric'
            requiredProperties: &ref_719
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_720
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_721
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_722
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_723
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_724
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_725
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_726
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_727
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_728
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_729
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_730
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_731
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_732
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_733
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_734
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_735
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_736
                    anyOf:
                      - $ref: '#/components/schemas/VerticaConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_737
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_738
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_739
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_740
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_741
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_742
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_743
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_744
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_745
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_746
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_747
                    const: vertica
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_748
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceVertica
            refIdentifier: '#/components/schemas/ApiDataSourceVertica'
            requiredProperties: &ref_749
              - name
              - type
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - &ref_750
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Exclude List
              catalog_include_list:
                allOf:
                  - &ref_751
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Catalog Include List
              created_from:
                allOf:
                  - &ref_752
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Created From
              data_retention_days:
                allOf:
                  - &ref_753
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Data Retention Days
              disable_profiling:
                allOf:
                  - &ref_754
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Profiling
              disable_schema_indexing:
                allOf:
                  - &ref_755
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Disable Schema Indexing
              float_tolerance:
                allOf:
                  - &ref_756
                    anyOf:
                      - type: number
                      - type: 'null'
                    default: 0
                    title: Float Tolerance
              groups:
                allOf:
                  - &ref_757
                    anyOf:
                      - additionalProperties:
                          type: boolean
                        type: object
                      - type: 'null'
                    title: Groups
              hidden:
                allOf:
                  - &ref_758
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Hidden
              id:
                allOf:
                  - &ref_759
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Id
              is_paused:
                allOf:
                  - &ref_760
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: Is Paused
              last_test:
                allOf:
                  - &ref_761
                    anyOf:
                      - $ref: '#/components/schemas/ApiDataSourceTestStatus'
                      - type: 'null'
              lineage_schedule:
                allOf:
                  - &ref_762
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Lineage Schedule
              max_allowed_connections:
                allOf:
                  - &ref_763
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Max Allowed Connections
              name:
                allOf:
                  - &ref_764
                    title: Name
                    type: string
              oauth_dwh_active:
                allOf:
                  - &ref_765
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Oauth Dwh Active
              options:
                allOf:
                  - &ref_766
                    anyOf:
                      - $ref: '#/components/schemas/TrinoConfig'
                      - type: 'null'
              profile_exclude_list:
                allOf:
                  - &ref_767
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Exclude List
              profile_include_list:
                allOf:
                  - &ref_768
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Include List
              profile_schedule:
                allOf:
                  - &ref_769
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Profile Schedule
              queue_name:
                allOf:
                  - &ref_770
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Queue Name
              scheduled_queue_name:
                allOf:
                  - &ref_771
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Scheduled Queue Name
              schema_indexing_schedule:
                allOf:
                  - &ref_772
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Schema Indexing Schedule
              schema_max_age_s:
                allOf:
                  - &ref_773
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Schema Max Age S
              secret_id:
                allOf:
                  - &ref_774
                    anyOf:
                      - type: integer
                      - type: 'null'
                    title: Secret Id
              source:
                allOf:
                  - &ref_775
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Source
              temp_schema:
                allOf:
                  - &ref_776
                    anyOf:
                      - type: string
                      - type: 'null'
                    title: Temp Schema
              type:
                allOf:
                  - &ref_777
                    const: trino
                    title: Type
                    type: string
              view_only:
                allOf:
                  - &ref_778
                    anyOf:
                      - type: boolean
                      - type: 'null'
                    default: false
                    title: View Only
            required: true
            title: ApiDataSourceTrino
            refIdentifier: '#/components/schemas/ApiDataSourceTrino'
            requiredProperties: &ref_779
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
                jsonKeyFile: <string>
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
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_0
              catalog_include_list:
                allOf:
                  - *ref_1
              created_from:
                allOf:
                  - *ref_2
              data_retention_days:
                allOf:
                  - *ref_3
              disable_profiling:
                allOf:
                  - *ref_4
              disable_schema_indexing:
                allOf:
                  - *ref_5
              float_tolerance:
                allOf:
                  - *ref_6
              groups:
                allOf:
                  - *ref_7
              hidden:
                allOf:
                  - *ref_8
              id:
                allOf:
                  - *ref_9
              is_paused:
                allOf:
                  - *ref_10
              last_test:
                allOf:
                  - *ref_11
              lineage_schedule:
                allOf:
                  - *ref_12
              max_allowed_connections:
                allOf:
                  - *ref_13
              name:
                allOf:
                  - *ref_14
              oauth_dwh_active:
                allOf:
                  - *ref_15
              options:
                allOf:
                  - *ref_16
              profile_exclude_list:
                allOf:
                  - *ref_17
              profile_include_list:
                allOf:
                  - *ref_18
              profile_schedule:
                allOf:
                  - *ref_19
              queue_name:
                allOf:
                  - *ref_20
              scheduled_queue_name:
                allOf:
                  - *ref_21
              schema_indexing_schedule:
                allOf:
                  - *ref_22
              schema_max_age_s:
                allOf:
                  - *ref_23
              secret_id:
                allOf:
                  - *ref_24
              source:
                allOf:
                  - *ref_25
              temp_schema:
                allOf:
                  - *ref_26
              type:
                allOf:
                  - *ref_27
              view_only:
                allOf:
                  - *ref_28
            title: ApiDataSourceBigQuery
            refIdentifier: '#/components/schemas/ApiDataSourceBigQuery'
            requiredProperties: *ref_29
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_30
              catalog_include_list:
                allOf:
                  - *ref_31
              created_from:
                allOf:
                  - *ref_32
              data_retention_days:
                allOf:
                  - *ref_33
              disable_profiling:
                allOf:
                  - *ref_34
              disable_schema_indexing:
                allOf:
                  - *ref_35
              float_tolerance:
                allOf:
                  - *ref_36
              groups:
                allOf:
                  - *ref_37
              hidden:
                allOf:
                  - *ref_38
              id:
                allOf:
                  - *ref_39
              is_paused:
                allOf:
                  - *ref_40
              last_test:
                allOf:
                  - *ref_41
              lineage_schedule:
                allOf:
                  - *ref_42
              max_allowed_connections:
                allOf:
                  - *ref_43
              name:
                allOf:
                  - *ref_44
              oauth_dwh_active:
                allOf:
                  - *ref_45
              options:
                allOf:
                  - *ref_46
              profile_exclude_list:
                allOf:
                  - *ref_47
              profile_include_list:
                allOf:
                  - *ref_48
              profile_schedule:
                allOf:
                  - *ref_49
              queue_name:
                allOf:
                  - *ref_50
              scheduled_queue_name:
                allOf:
                  - *ref_51
              schema_indexing_schedule:
                allOf:
                  - *ref_52
              schema_max_age_s:
                allOf:
                  - *ref_53
              secret_id:
                allOf:
                  - *ref_54
              source:
                allOf:
                  - *ref_55
              temp_schema:
                allOf:
                  - *ref_56
              type:
                allOf:
                  - *ref_57
              view_only:
                allOf:
                  - *ref_58
            title: ApiDataSourceDatabricks
            refIdentifier: '#/components/schemas/ApiDataSourceDatabricks'
            requiredProperties: *ref_59
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_60
              catalog_include_list:
                allOf:
                  - *ref_61
              created_from:
                allOf:
                  - *ref_62
              data_retention_days:
                allOf:
                  - *ref_63
              disable_profiling:
                allOf:
                  - *ref_64
              disable_schema_indexing:
                allOf:
                  - *ref_65
              float_tolerance:
                allOf:
                  - *ref_66
              groups:
                allOf:
                  - *ref_67
              hidden:
                allOf:
                  - *ref_68
              id:
                allOf:
                  - *ref_69
              is_paused:
                allOf:
                  - *ref_70
              last_test:
                allOf:
                  - *ref_71
              lineage_schedule:
                allOf:
                  - *ref_72
              max_allowed_connections:
                allOf:
                  - *ref_73
              name:
                allOf:
                  - *ref_74
              oauth_dwh_active:
                allOf:
                  - *ref_75
              options:
                allOf:
                  - *ref_76
              profile_exclude_list:
                allOf:
                  - *ref_77
              profile_include_list:
                allOf:
                  - *ref_78
              profile_schedule:
                allOf:
                  - *ref_79
              queue_name:
                allOf:
                  - *ref_80
              scheduled_queue_name:
                allOf:
                  - *ref_81
              schema_indexing_schedule:
                allOf:
                  - *ref_82
              schema_max_age_s:
                allOf:
                  - *ref_83
              secret_id:
                allOf:
                  - *ref_84
              source:
                allOf:
                  - *ref_85
              temp_schema:
                allOf:
                  - *ref_86
              type:
                allOf:
                  - *ref_87
              view_only:
                allOf:
                  - *ref_88
            title: ApiDataSourceDuckDB
            refIdentifier: '#/components/schemas/ApiDataSourceDuckDB'
            requiredProperties: *ref_89
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_90
              catalog_include_list:
                allOf:
                  - *ref_91
              created_from:
                allOf:
                  - *ref_92
              data_retention_days:
                allOf:
                  - *ref_93
              disable_profiling:
                allOf:
                  - *ref_94
              disable_schema_indexing:
                allOf:
                  - *ref_95
              float_tolerance:
                allOf:
                  - *ref_96
              groups:
                allOf:
                  - *ref_97
              hidden:
                allOf:
                  - *ref_98
              id:
                allOf:
                  - *ref_99
              is_paused:
                allOf:
                  - *ref_100
              last_test:
                allOf:
                  - *ref_101
              lineage_schedule:
                allOf:
                  - *ref_102
              max_allowed_connections:
                allOf:
                  - *ref_103
              name:
                allOf:
                  - *ref_104
              oauth_dwh_active:
                allOf:
                  - *ref_105
              options:
                allOf:
                  - *ref_106
              profile_exclude_list:
                allOf:
                  - *ref_107
              profile_include_list:
                allOf:
                  - *ref_108
              profile_schedule:
                allOf:
                  - *ref_109
              queue_name:
                allOf:
                  - *ref_110
              scheduled_queue_name:
                allOf:
                  - *ref_111
              schema_indexing_schedule:
                allOf:
                  - *ref_112
              schema_max_age_s:
                allOf:
                  - *ref_113
              secret_id:
                allOf:
                  - *ref_114
              source:
                allOf:
                  - *ref_115
              temp_schema:
                allOf:
                  - *ref_116
              type:
                allOf:
                  - *ref_117
              view_only:
                allOf:
                  - *ref_118
            title: ApiDataSourceMongoDB
            refIdentifier: '#/components/schemas/ApiDataSourceMongoDB'
            requiredProperties: *ref_119
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_120
              catalog_include_list:
                allOf:
                  - *ref_121
              created_from:
                allOf:
                  - *ref_122
              data_retention_days:
                allOf:
                  - *ref_123
              disable_profiling:
                allOf:
                  - *ref_124
              disable_schema_indexing:
                allOf:
                  - *ref_125
              float_tolerance:
                allOf:
                  - *ref_126
              groups:
                allOf:
                  - *ref_127
              hidden:
                allOf:
                  - *ref_128
              id:
                allOf:
                  - *ref_129
              is_paused:
                allOf:
                  - *ref_130
              last_test:
                allOf:
                  - *ref_131
              lineage_schedule:
                allOf:
                  - *ref_132
              max_allowed_connections:
                allOf:
                  - *ref_133
              name:
                allOf:
                  - *ref_134
              oauth_dwh_active:
                allOf:
                  - *ref_135
              options:
                allOf:
                  - *ref_136
              profile_exclude_list:
                allOf:
                  - *ref_137
              profile_include_list:
                allOf:
                  - *ref_138
              profile_schedule:
                allOf:
                  - *ref_139
              queue_name:
                allOf:
                  - *ref_140
              scheduled_queue_name:
                allOf:
                  - *ref_141
              schema_indexing_schedule:
                allOf:
                  - *ref_142
              schema_max_age_s:
                allOf:
                  - *ref_143
              secret_id:
                allOf:
                  - *ref_144
              source:
                allOf:
                  - *ref_145
              temp_schema:
                allOf:
                  - *ref_146
              type:
                allOf:
                  - *ref_147
              view_only:
                allOf:
                  - *ref_148
            title: ApiDataSourceMySQL
            refIdentifier: '#/components/schemas/ApiDataSourceMySQL'
            requiredProperties: *ref_149
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_150
              catalog_include_list:
                allOf:
                  - *ref_151
              created_from:
                allOf:
                  - *ref_152
              data_retention_days:
                allOf:
                  - *ref_153
              disable_profiling:
                allOf:
                  - *ref_154
              disable_schema_indexing:
                allOf:
                  - *ref_155
              float_tolerance:
                allOf:
                  - *ref_156
              groups:
                allOf:
                  - *ref_157
              hidden:
                allOf:
                  - *ref_158
              id:
                allOf:
                  - *ref_159
              is_paused:
                allOf:
                  - *ref_160
              last_test:
                allOf:
                  - *ref_161
              lineage_schedule:
                allOf:
                  - *ref_162
              max_allowed_connections:
                allOf:
                  - *ref_163
              name:
                allOf:
                  - *ref_164
              oauth_dwh_active:
                allOf:
                  - *ref_165
              options:
                allOf:
                  - *ref_166
              profile_exclude_list:
                allOf:
                  - *ref_167
              profile_include_list:
                allOf:
                  - *ref_168
              profile_schedule:
                allOf:
                  - *ref_169
              queue_name:
                allOf:
                  - *ref_170
              scheduled_queue_name:
                allOf:
                  - *ref_171
              schema_indexing_schedule:
                allOf:
                  - *ref_172
              schema_max_age_s:
                allOf:
                  - *ref_173
              secret_id:
                allOf:
                  - *ref_174
              source:
                allOf:
                  - *ref_175
              temp_schema:
                allOf:
                  - *ref_176
              type:
                allOf:
                  - *ref_177
              view_only:
                allOf:
                  - *ref_178
            title: ApiDataSourceMariaDB
            refIdentifier: '#/components/schemas/ApiDataSourceMariaDB'
            requiredProperties: *ref_179
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_180
              catalog_include_list:
                allOf:
                  - *ref_181
              created_from:
                allOf:
                  - *ref_182
              data_retention_days:
                allOf:
                  - *ref_183
              disable_profiling:
                allOf:
                  - *ref_184
              disable_schema_indexing:
                allOf:
                  - *ref_185
              float_tolerance:
                allOf:
                  - *ref_186
              groups:
                allOf:
                  - *ref_187
              hidden:
                allOf:
                  - *ref_188
              id:
                allOf:
                  - *ref_189
              is_paused:
                allOf:
                  - *ref_190
              last_test:
                allOf:
                  - *ref_191
              lineage_schedule:
                allOf:
                  - *ref_192
              max_allowed_connections:
                allOf:
                  - *ref_193
              name:
                allOf:
                  - *ref_194
              oauth_dwh_active:
                allOf:
                  - *ref_195
              options:
                allOf:
                  - *ref_196
              profile_exclude_list:
                allOf:
                  - *ref_197
              profile_include_list:
                allOf:
                  - *ref_198
              profile_schedule:
                allOf:
                  - *ref_199
              queue_name:
                allOf:
                  - *ref_200
              scheduled_queue_name:
                allOf:
                  - *ref_201
              schema_indexing_schedule:
                allOf:
                  - *ref_202
              schema_max_age_s:
                allOf:
                  - *ref_203
              secret_id:
                allOf:
                  - *ref_204
              source:
                allOf:
                  - *ref_205
              temp_schema:
                allOf:
                  - *ref_206
              type:
                allOf:
                  - *ref_207
              view_only:
                allOf:
                  - *ref_208
            title: ApiDataSourceMSSQL
            refIdentifier: '#/components/schemas/ApiDataSourceMSSQL'
            requiredProperties: *ref_209
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_210
              catalog_include_list:
                allOf:
                  - *ref_211
              created_from:
                allOf:
                  - *ref_212
              data_retention_days:
                allOf:
                  - *ref_213
              disable_profiling:
                allOf:
                  - *ref_214
              disable_schema_indexing:
                allOf:
                  - *ref_215
              float_tolerance:
                allOf:
                  - *ref_216
              groups:
                allOf:
                  - *ref_217
              hidden:
                allOf:
                  - *ref_218
              id:
                allOf:
                  - *ref_219
              is_paused:
                allOf:
                  - *ref_220
              last_test:
                allOf:
                  - *ref_221
              lineage_schedule:
                allOf:
                  - *ref_222
              max_allowed_connections:
                allOf:
                  - *ref_223
              name:
                allOf:
                  - *ref_224
              oauth_dwh_active:
                allOf:
                  - *ref_225
              options:
                allOf:
                  - *ref_226
              profile_exclude_list:
                allOf:
                  - *ref_227
              profile_include_list:
                allOf:
                  - *ref_228
              profile_schedule:
                allOf:
                  - *ref_229
              queue_name:
                allOf:
                  - *ref_230
              scheduled_queue_name:
                allOf:
                  - *ref_231
              schema_indexing_schedule:
                allOf:
                  - *ref_232
              schema_max_age_s:
                allOf:
                  - *ref_233
              secret_id:
                allOf:
                  - *ref_234
              source:
                allOf:
                  - *ref_235
              temp_schema:
                allOf:
                  - *ref_236
              type:
                allOf:
                  - *ref_237
              view_only:
                allOf:
                  - *ref_238
            title: ApiDataSourceOracle
            refIdentifier: '#/components/schemas/ApiDataSourceOracle'
            requiredProperties: *ref_239
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_240
              catalog_include_list:
                allOf:
                  - *ref_241
              created_from:
                allOf:
                  - *ref_242
              data_retention_days:
                allOf:
                  - *ref_243
              disable_profiling:
                allOf:
                  - *ref_244
              disable_schema_indexing:
                allOf:
                  - *ref_245
              float_tolerance:
                allOf:
                  - *ref_246
              groups:
                allOf:
                  - *ref_247
              hidden:
                allOf:
                  - *ref_248
              id:
                allOf:
                  - *ref_249
              is_paused:
                allOf:
                  - *ref_250
              last_test:
                allOf:
                  - *ref_251
              lineage_schedule:
                allOf:
                  - *ref_252
              max_allowed_connections:
                allOf:
                  - *ref_253
              name:
                allOf:
                  - *ref_254
              oauth_dwh_active:
                allOf:
                  - *ref_255
              options:
                allOf:
                  - *ref_256
              profile_exclude_list:
                allOf:
                  - *ref_257
              profile_include_list:
                allOf:
                  - *ref_258
              profile_schedule:
                allOf:
                  - *ref_259
              queue_name:
                allOf:
                  - *ref_260
              scheduled_queue_name:
                allOf:
                  - *ref_261
              schema_indexing_schedule:
                allOf:
                  - *ref_262
              schema_max_age_s:
                allOf:
                  - *ref_263
              secret_id:
                allOf:
                  - *ref_264
              source:
                allOf:
                  - *ref_265
              temp_schema:
                allOf:
                  - *ref_266
              type:
                allOf:
                  - *ref_267
              view_only:
                allOf:
                  - *ref_268
            title: ApiDataSourcePostgres
            refIdentifier: '#/components/schemas/ApiDataSourcePostgres'
            requiredProperties: *ref_269
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_270
              catalog_include_list:
                allOf:
                  - *ref_271
              created_from:
                allOf:
                  - *ref_272
              data_retention_days:
                allOf:
                  - *ref_273
              disable_profiling:
                allOf:
                  - *ref_274
              disable_schema_indexing:
                allOf:
                  - *ref_275
              float_tolerance:
                allOf:
                  - *ref_276
              groups:
                allOf:
                  - *ref_277
              hidden:
                allOf:
                  - *ref_278
              id:
                allOf:
                  - *ref_279
              is_paused:
                allOf:
                  - *ref_280
              last_test:
                allOf:
                  - *ref_281
              lineage_schedule:
                allOf:
                  - *ref_282
              max_allowed_connections:
                allOf:
                  - *ref_283
              name:
                allOf:
                  - *ref_284
              oauth_dwh_active:
                allOf:
                  - *ref_285
              options:
                allOf:
                  - *ref_286
              profile_exclude_list:
                allOf:
                  - *ref_287
              profile_include_list:
                allOf:
                  - *ref_288
              profile_schedule:
                allOf:
                  - *ref_289
              queue_name:
                allOf:
                  - *ref_290
              scheduled_queue_name:
                allOf:
                  - *ref_291
              schema_indexing_schedule:
                allOf:
                  - *ref_292
              schema_max_age_s:
                allOf:
                  - *ref_293
              secret_id:
                allOf:
                  - *ref_294
              source:
                allOf:
                  - *ref_295
              temp_schema:
                allOf:
                  - *ref_296
              type:
                allOf:
                  - *ref_297
              view_only:
                allOf:
                  - *ref_298
            title: ApiDataSourcePostgresAurora
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresAurora'
            requiredProperties: *ref_299
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_300
              catalog_include_list:
                allOf:
                  - *ref_301
              created_from:
                allOf:
                  - *ref_302
              data_retention_days:
                allOf:
                  - *ref_303
              disable_profiling:
                allOf:
                  - *ref_304
              disable_schema_indexing:
                allOf:
                  - *ref_305
              float_tolerance:
                allOf:
                  - *ref_306
              groups:
                allOf:
                  - *ref_307
              hidden:
                allOf:
                  - *ref_308
              id:
                allOf:
                  - *ref_309
              is_paused:
                allOf:
                  - *ref_310
              last_test:
                allOf:
                  - *ref_311
              lineage_schedule:
                allOf:
                  - *ref_312
              max_allowed_connections:
                allOf:
                  - *ref_313
              name:
                allOf:
                  - *ref_314
              oauth_dwh_active:
                allOf:
                  - *ref_315
              options:
                allOf:
                  - *ref_316
              profile_exclude_list:
                allOf:
                  - *ref_317
              profile_include_list:
                allOf:
                  - *ref_318
              profile_schedule:
                allOf:
                  - *ref_319
              queue_name:
                allOf:
                  - *ref_320
              scheduled_queue_name:
                allOf:
                  - *ref_321
              schema_indexing_schedule:
                allOf:
                  - *ref_322
              schema_max_age_s:
                allOf:
                  - *ref_323
              secret_id:
                allOf:
                  - *ref_324
              source:
                allOf:
                  - *ref_325
              temp_schema:
                allOf:
                  - *ref_326
              type:
                allOf:
                  - *ref_327
              view_only:
                allOf:
                  - *ref_328
            title: ApiDataSourcePostgresRds
            refIdentifier: '#/components/schemas/ApiDataSourcePostgresRds'
            requiredProperties: *ref_329
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_330
              catalog_include_list:
                allOf:
                  - *ref_331
              created_from:
                allOf:
                  - *ref_332
              data_retention_days:
                allOf:
                  - *ref_333
              disable_profiling:
                allOf:
                  - *ref_334
              disable_schema_indexing:
                allOf:
                  - *ref_335
              float_tolerance:
                allOf:
                  - *ref_336
              groups:
                allOf:
                  - *ref_337
              hidden:
                allOf:
                  - *ref_338
              id:
                allOf:
                  - *ref_339
              is_paused:
                allOf:
                  - *ref_340
              last_test:
                allOf:
                  - *ref_341
              lineage_schedule:
                allOf:
                  - *ref_342
              max_allowed_connections:
                allOf:
                  - *ref_343
              name:
                allOf:
                  - *ref_344
              oauth_dwh_active:
                allOf:
                  - *ref_345
              options:
                allOf:
                  - *ref_346
              profile_exclude_list:
                allOf:
                  - *ref_347
              profile_include_list:
                allOf:
                  - *ref_348
              profile_schedule:
                allOf:
                  - *ref_349
              queue_name:
                allOf:
                  - *ref_350
              scheduled_queue_name:
                allOf:
                  - *ref_351
              schema_indexing_schedule:
                allOf:
                  - *ref_352
              schema_max_age_s:
                allOf:
                  - *ref_353
              secret_id:
                allOf:
                  - *ref_354
              source:
                allOf:
                  - *ref_355
              temp_schema:
                allOf:
                  - *ref_356
              type:
                allOf:
                  - *ref_357
              view_only:
                allOf:
                  - *ref_358
            title: ApiDataSourceRedshift
            refIdentifier: '#/components/schemas/ApiDataSourceRedshift'
            requiredProperties: *ref_359
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_360
              catalog_include_list:
                allOf:
                  - *ref_361
              created_from:
                allOf:
                  - *ref_362
              data_retention_days:
                allOf:
                  - *ref_363
              disable_profiling:
                allOf:
                  - *ref_364
              disable_schema_indexing:
                allOf:
                  - *ref_365
              float_tolerance:
                allOf:
                  - *ref_366
              groups:
                allOf:
                  - *ref_367
              hidden:
                allOf:
                  - *ref_368
              id:
                allOf:
                  - *ref_369
              is_paused:
                allOf:
                  - *ref_370
              last_test:
                allOf:
                  - *ref_371
              lineage_schedule:
                allOf:
                  - *ref_372
              max_allowed_connections:
                allOf:
                  - *ref_373
              name:
                allOf:
                  - *ref_374
              oauth_dwh_active:
                allOf:
                  - *ref_375
              options:
                allOf:
                  - *ref_376
              profile_exclude_list:
                allOf:
                  - *ref_377
              profile_include_list:
                allOf:
                  - *ref_378
              profile_schedule:
                allOf:
                  - *ref_379
              queue_name:
                allOf:
                  - *ref_380
              scheduled_queue_name:
                allOf:
                  - *ref_381
              schema_indexing_schedule:
                allOf:
                  - *ref_382
              schema_max_age_s:
                allOf:
                  - *ref_383
              secret_id:
                allOf:
                  - *ref_384
              source:
                allOf:
                  - *ref_385
              temp_schema:
                allOf:
                  - *ref_386
              type:
                allOf:
                  - *ref_387
              view_only:
                allOf:
                  - *ref_388
            title: ApiDataSourceTeradata
            refIdentifier: '#/components/schemas/ApiDataSourceTeradata'
            requiredProperties: *ref_389
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_390
              catalog_include_list:
                allOf:
                  - *ref_391
              created_from:
                allOf:
                  - *ref_392
              data_retention_days:
                allOf:
                  - *ref_393
              disable_profiling:
                allOf:
                  - *ref_394
              disable_schema_indexing:
                allOf:
                  - *ref_395
              float_tolerance:
                allOf:
                  - *ref_396
              groups:
                allOf:
                  - *ref_397
              hidden:
                allOf:
                  - *ref_398
              id:
                allOf:
                  - *ref_399
              is_paused:
                allOf:
                  - *ref_400
              last_test:
                allOf:
                  - *ref_401
              lineage_schedule:
                allOf:
                  - *ref_402
              max_allowed_connections:
                allOf:
                  - *ref_403
              name:
                allOf:
                  - *ref_404
              oauth_dwh_active:
                allOf:
                  - *ref_405
              options:
                allOf:
                  - *ref_406
              profile_exclude_list:
                allOf:
                  - *ref_407
              profile_include_list:
                allOf:
                  - *ref_408
              profile_schedule:
                allOf:
                  - *ref_409
              queue_name:
                allOf:
                  - *ref_410
              scheduled_queue_name:
                allOf:
                  - *ref_411
              schema_indexing_schedule:
                allOf:
                  - *ref_412
              schema_max_age_s:
                allOf:
                  - *ref_413
              secret_id:
                allOf:
                  - *ref_414
              source:
                allOf:
                  - *ref_415
              temp_schema:
                allOf:
                  - *ref_416
              type:
                allOf:
                  - *ref_417
              view_only:
                allOf:
                  - *ref_418
            title: ApiDataSourceSapHana
            refIdentifier: '#/components/schemas/ApiDataSourceSapHana'
            requiredProperties: *ref_419
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_420
              catalog_include_list:
                allOf:
                  - *ref_421
              created_from:
                allOf:
                  - *ref_422
              data_retention_days:
                allOf:
                  - *ref_423
              disable_profiling:
                allOf:
                  - *ref_424
              disable_schema_indexing:
                allOf:
                  - *ref_425
              float_tolerance:
                allOf:
                  - *ref_426
              groups:
                allOf:
                  - *ref_427
              hidden:
                allOf:
                  - *ref_428
              id:
                allOf:
                  - *ref_429
              is_paused:
                allOf:
                  - *ref_430
              last_test:
                allOf:
                  - *ref_431
              lineage_schedule:
                allOf:
                  - *ref_432
              max_allowed_connections:
                allOf:
                  - *ref_433
              name:
                allOf:
                  - *ref_434
              oauth_dwh_active:
                allOf:
                  - *ref_435
              options:
                allOf:
                  - *ref_436
              profile_exclude_list:
                allOf:
                  - *ref_437
              profile_include_list:
                allOf:
                  - *ref_438
              profile_schedule:
                allOf:
                  - *ref_439
              queue_name:
                allOf:
                  - *ref_440
              scheduled_queue_name:
                allOf:
                  - *ref_441
              schema_indexing_schedule:
                allOf:
                  - *ref_442
              schema_max_age_s:
                allOf:
                  - *ref_443
              secret_id:
                allOf:
                  - *ref_444
              source:
                allOf:
                  - *ref_445
              temp_schema:
                allOf:
                  - *ref_446
              type:
                allOf:
                  - *ref_447
              view_only:
                allOf:
                  - *ref_448
            title: ApiDataSourceAwsAthena
            refIdentifier: '#/components/schemas/ApiDataSourceAwsAthena'
            requiredProperties: *ref_449
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_450
              catalog_include_list:
                allOf:
                  - *ref_451
              created_from:
                allOf:
                  - *ref_452
              data_retention_days:
                allOf:
                  - *ref_453
              disable_profiling:
                allOf:
                  - *ref_454
              disable_schema_indexing:
                allOf:
                  - *ref_455
              float_tolerance:
                allOf:
                  - *ref_456
              groups:
                allOf:
                  - *ref_457
              hidden:
                allOf:
                  - *ref_458
              id:
                allOf:
                  - *ref_459
              is_paused:
                allOf:
                  - *ref_460
              last_test:
                allOf:
                  - *ref_461
              lineage_schedule:
                allOf:
                  - *ref_462
              max_allowed_connections:
                allOf:
                  - *ref_463
              name:
                allOf:
                  - *ref_464
              oauth_dwh_active:
                allOf:
                  - *ref_465
              options:
                allOf:
                  - *ref_466
              profile_exclude_list:
                allOf:
                  - *ref_467
              profile_include_list:
                allOf:
                  - *ref_468
              profile_schedule:
                allOf:
                  - *ref_469
              queue_name:
                allOf:
                  - *ref_470
              scheduled_queue_name:
                allOf:
                  - *ref_471
              schema_indexing_schedule:
                allOf:
                  - *ref_472
              schema_max_age_s:
                allOf:
                  - *ref_473
              secret_id:
                allOf:
                  - *ref_474
              source:
                allOf:
                  - *ref_475
              temp_schema:
                allOf:
                  - *ref_476
              type:
                allOf:
                  - *ref_477
              view_only:
                allOf:
                  - *ref_478
            title: ApiDataSourceSnowflake
            refIdentifier: '#/components/schemas/ApiDataSourceSnowflake'
            requiredProperties: *ref_479
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_480
              catalog_include_list:
                allOf:
                  - *ref_481
              created_from:
                allOf:
                  - *ref_482
              data_retention_days:
                allOf:
                  - *ref_483
              disable_profiling:
                allOf:
                  - *ref_484
              disable_schema_indexing:
                allOf:
                  - *ref_485
              float_tolerance:
                allOf:
                  - *ref_486
              groups:
                allOf:
                  - *ref_487
              hidden:
                allOf:
                  - *ref_488
              id:
                allOf:
                  - *ref_489
              is_paused:
                allOf:
                  - *ref_490
              last_test:
                allOf:
                  - *ref_491
              lineage_schedule:
                allOf:
                  - *ref_492
              max_allowed_connections:
                allOf:
                  - *ref_493
              name:
                allOf:
                  - *ref_494
              oauth_dwh_active:
                allOf:
                  - *ref_495
              options:
                allOf:
                  - *ref_496
              profile_exclude_list:
                allOf:
                  - *ref_497
              profile_include_list:
                allOf:
                  - *ref_498
              profile_schedule:
                allOf:
                  - *ref_499
              queue_name:
                allOf:
                  - *ref_500
              scheduled_queue_name:
                allOf:
                  - *ref_501
              schema_indexing_schedule:
                allOf:
                  - *ref_502
              schema_max_age_s:
                allOf:
                  - *ref_503
              secret_id:
                allOf:
                  - *ref_504
              source:
                allOf:
                  - *ref_505
              temp_schema:
                allOf:
                  - *ref_506
              type:
                allOf:
                  - *ref_507
              view_only:
                allOf:
                  - *ref_508
            title: ApiDataSourceDremio
            refIdentifier: '#/components/schemas/ApiDataSourceDremio'
            requiredProperties: *ref_509
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_510
              catalog_include_list:
                allOf:
                  - *ref_511
              created_from:
                allOf:
                  - *ref_512
              data_retention_days:
                allOf:
                  - *ref_513
              disable_profiling:
                allOf:
                  - *ref_514
              disable_schema_indexing:
                allOf:
                  - *ref_515
              float_tolerance:
                allOf:
                  - *ref_516
              groups:
                allOf:
                  - *ref_517
              hidden:
                allOf:
                  - *ref_518
              id:
                allOf:
                  - *ref_519
              is_paused:
                allOf:
                  - *ref_520
              last_test:
                allOf:
                  - *ref_521
              lineage_schedule:
                allOf:
                  - *ref_522
              max_allowed_connections:
                allOf:
                  - *ref_523
              name:
                allOf:
                  - *ref_524
              oauth_dwh_active:
                allOf:
                  - *ref_525
              options:
                allOf:
                  - *ref_526
              profile_exclude_list:
                allOf:
                  - *ref_527
              profile_include_list:
                allOf:
                  - *ref_528
              profile_schedule:
                allOf:
                  - *ref_529
              queue_name:
                allOf:
                  - *ref_530
              scheduled_queue_name:
                allOf:
                  - *ref_531
              schema_indexing_schedule:
                allOf:
                  - *ref_532
              schema_max_age_s:
                allOf:
                  - *ref_533
              secret_id:
                allOf:
                  - *ref_534
              source:
                allOf:
                  - *ref_535
              temp_schema:
                allOf:
                  - *ref_536
              type:
                allOf:
                  - *ref_537
              view_only:
                allOf:
                  - *ref_538
            title: ApiDataSourceStarburst
            refIdentifier: '#/components/schemas/ApiDataSourceStarburst'
            requiredProperties: *ref_539
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_540
              catalog_include_list:
                allOf:
                  - *ref_541
              created_from:
                allOf:
                  - *ref_542
              data_retention_days:
                allOf:
                  - *ref_543
              disable_profiling:
                allOf:
                  - *ref_544
              disable_schema_indexing:
                allOf:
                  - *ref_545
              float_tolerance:
                allOf:
                  - *ref_546
              groups:
                allOf:
                  - *ref_547
              hidden:
                allOf:
                  - *ref_548
              id:
                allOf:
                  - *ref_549
              is_paused:
                allOf:
                  - *ref_550
              last_test:
                allOf:
                  - *ref_551
              lineage_schedule:
                allOf:
                  - *ref_552
              max_allowed_connections:
                allOf:
                  - *ref_553
              name:
                allOf:
                  - *ref_554
              oauth_dwh_active:
                allOf:
                  - *ref_555
              options:
                allOf:
                  - *ref_556
              profile_exclude_list:
                allOf:
                  - *ref_557
              profile_include_list:
                allOf:
                  - *ref_558
              profile_schedule:
                allOf:
                  - *ref_559
              queue_name:
                allOf:
                  - *ref_560
              scheduled_queue_name:
                allOf:
                  - *ref_561
              schema_indexing_schedule:
                allOf:
                  - *ref_562
              schema_max_age_s:
                allOf:
                  - *ref_563
              secret_id:
                allOf:
                  - *ref_564
              source:
                allOf:
                  - *ref_565
              temp_schema:
                allOf:
                  - *ref_566
              type:
                allOf:
                  - *ref_567
              view_only:
                allOf:
                  - *ref_568
            title: ApiDataSourceNetezza
            refIdentifier: '#/components/schemas/ApiDataSourceNetezza'
            requiredProperties: *ref_569
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_570
              catalog_include_list:
                allOf:
                  - *ref_571
              created_from:
                allOf:
                  - *ref_572
              data_retention_days:
                allOf:
                  - *ref_573
              disable_profiling:
                allOf:
                  - *ref_574
              disable_schema_indexing:
                allOf:
                  - *ref_575
              float_tolerance:
                allOf:
                  - *ref_576
              groups:
                allOf:
                  - *ref_577
              hidden:
                allOf:
                  - *ref_578
              id:
                allOf:
                  - *ref_579
              is_paused:
                allOf:
                  - *ref_580
              last_test:
                allOf:
                  - *ref_581
              lineage_schedule:
                allOf:
                  - *ref_582
              max_allowed_connections:
                allOf:
                  - *ref_583
              name:
                allOf:
                  - *ref_584
              oauth_dwh_active:
                allOf:
                  - *ref_585
              options:
                allOf:
                  - *ref_586
              profile_exclude_list:
                allOf:
                  - *ref_587
              profile_include_list:
                allOf:
                  - *ref_588
              profile_schedule:
                allOf:
                  - *ref_589
              queue_name:
                allOf:
                  - *ref_590
              scheduled_queue_name:
                allOf:
                  - *ref_591
              schema_indexing_schedule:
                allOf:
                  - *ref_592
              schema_max_age_s:
                allOf:
                  - *ref_593
              secret_id:
                allOf:
                  - *ref_594
              source:
                allOf:
                  - *ref_595
              temp_schema:
                allOf:
                  - *ref_596
              type:
                allOf:
                  - *ref_597
              view_only:
                allOf:
                  - *ref_598
            title: ApiDataSourceAzureDataLake
            refIdentifier: '#/components/schemas/ApiDataSourceAzureDataLake'
            requiredProperties: *ref_599
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_600
              catalog_include_list:
                allOf:
                  - *ref_601
              created_from:
                allOf:
                  - *ref_602
              data_retention_days:
                allOf:
                  - *ref_603
              disable_profiling:
                allOf:
                  - *ref_604
              disable_schema_indexing:
                allOf:
                  - *ref_605
              float_tolerance:
                allOf:
                  - *ref_606
              groups:
                allOf:
                  - *ref_607
              hidden:
                allOf:
                  - *ref_608
              id:
                allOf:
                  - *ref_609
              is_paused:
                allOf:
                  - *ref_610
              last_test:
                allOf:
                  - *ref_611
              lineage_schedule:
                allOf:
                  - *ref_612
              max_allowed_connections:
                allOf:
                  - *ref_613
              name:
                allOf:
                  - *ref_614
              oauth_dwh_active:
                allOf:
                  - *ref_615
              options:
                allOf:
                  - *ref_616
              profile_exclude_list:
                allOf:
                  - *ref_617
              profile_include_list:
                allOf:
                  - *ref_618
              profile_schedule:
                allOf:
                  - *ref_619
              queue_name:
                allOf:
                  - *ref_620
              scheduled_queue_name:
                allOf:
                  - *ref_621
              schema_indexing_schedule:
                allOf:
                  - *ref_622
              schema_max_age_s:
                allOf:
                  - *ref_623
              secret_id:
                allOf:
                  - *ref_624
              source:
                allOf:
                  - *ref_625
              temp_schema:
                allOf:
                  - *ref_626
              type:
                allOf:
                  - *ref_627
              view_only:
                allOf:
                  - *ref_628
            title: ApiDataSourceGCS
            refIdentifier: '#/components/schemas/ApiDataSourceGCS'
            requiredProperties: *ref_629
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_630
              catalog_include_list:
                allOf:
                  - *ref_631
              created_from:
                allOf:
                  - *ref_632
              data_retention_days:
                allOf:
                  - *ref_633
              disable_profiling:
                allOf:
                  - *ref_634
              disable_schema_indexing:
                allOf:
                  - *ref_635
              float_tolerance:
                allOf:
                  - *ref_636
              groups:
                allOf:
                  - *ref_637
              hidden:
                allOf:
                  - *ref_638
              id:
                allOf:
                  - *ref_639
              is_paused:
                allOf:
                  - *ref_640
              last_test:
                allOf:
                  - *ref_641
              lineage_schedule:
                allOf:
                  - *ref_642
              max_allowed_connections:
                allOf:
                  - *ref_643
              name:
                allOf:
                  - *ref_644
              oauth_dwh_active:
                allOf:
                  - *ref_645
              options:
                allOf:
                  - *ref_646
              profile_exclude_list:
                allOf:
                  - *ref_647
              profile_include_list:
                allOf:
                  - *ref_648
              profile_schedule:
                allOf:
                  - *ref_649
              queue_name:
                allOf:
                  - *ref_650
              scheduled_queue_name:
                allOf:
                  - *ref_651
              schema_indexing_schedule:
                allOf:
                  - *ref_652
              schema_max_age_s:
                allOf:
                  - *ref_653
              secret_id:
                allOf:
                  - *ref_654
              source:
                allOf:
                  - *ref_655
              temp_schema:
                allOf:
                  - *ref_656
              type:
                allOf:
                  - *ref_657
              view_only:
                allOf:
                  - *ref_658
            title: ApiDataSourceS3
            refIdentifier: '#/components/schemas/ApiDataSourceS3'
            requiredProperties: *ref_659
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_660
              catalog_include_list:
                allOf:
                  - *ref_661
              created_from:
                allOf:
                  - *ref_662
              data_retention_days:
                allOf:
                  - *ref_663
              disable_profiling:
                allOf:
                  - *ref_664
              disable_schema_indexing:
                allOf:
                  - *ref_665
              float_tolerance:
                allOf:
                  - *ref_666
              groups:
                allOf:
                  - *ref_667
              hidden:
                allOf:
                  - *ref_668
              id:
                allOf:
                  - *ref_669
              is_paused:
                allOf:
                  - *ref_670
              last_test:
                allOf:
                  - *ref_671
              lineage_schedule:
                allOf:
                  - *ref_672
              max_allowed_connections:
                allOf:
                  - *ref_673
              name:
                allOf:
                  - *ref_674
              oauth_dwh_active:
                allOf:
                  - *ref_675
              options:
                allOf:
                  - *ref_676
              profile_exclude_list:
                allOf:
                  - *ref_677
              profile_include_list:
                allOf:
                  - *ref_678
              profile_schedule:
                allOf:
                  - *ref_679
              queue_name:
                allOf:
                  - *ref_680
              scheduled_queue_name:
                allOf:
                  - *ref_681
              schema_indexing_schedule:
                allOf:
                  - *ref_682
              schema_max_age_s:
                allOf:
                  - *ref_683
              secret_id:
                allOf:
                  - *ref_684
              source:
                allOf:
                  - *ref_685
              temp_schema:
                allOf:
                  - *ref_686
              type:
                allOf:
                  - *ref_687
              view_only:
                allOf:
                  - *ref_688
            title: ApiDataSourceAzureSynapse
            refIdentifier: '#/components/schemas/ApiDataSourceAzureSynapse'
            requiredProperties: *ref_689
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_690
              catalog_include_list:
                allOf:
                  - *ref_691
              created_from:
                allOf:
                  - *ref_692
              data_retention_days:
                allOf:
                  - *ref_693
              disable_profiling:
                allOf:
                  - *ref_694
              disable_schema_indexing:
                allOf:
                  - *ref_695
              float_tolerance:
                allOf:
                  - *ref_696
              groups:
                allOf:
                  - *ref_697
              hidden:
                allOf:
                  - *ref_698
              id:
                allOf:
                  - *ref_699
              is_paused:
                allOf:
                  - *ref_700
              last_test:
                allOf:
                  - *ref_701
              lineage_schedule:
                allOf:
                  - *ref_702
              max_allowed_connections:
                allOf:
                  - *ref_703
              name:
                allOf:
                  - *ref_704
              oauth_dwh_active:
                allOf:
                  - *ref_705
              options:
                allOf:
                  - *ref_706
              profile_exclude_list:
                allOf:
                  - *ref_707
              profile_include_list:
                allOf:
                  - *ref_708
              profile_schedule:
                allOf:
                  - *ref_709
              queue_name:
                allOf:
                  - *ref_710
              scheduled_queue_name:
                allOf:
                  - *ref_711
              schema_indexing_schedule:
                allOf:
                  - *ref_712
              schema_max_age_s:
                allOf:
                  - *ref_713
              secret_id:
                allOf:
                  - *ref_714
              source:
                allOf:
                  - *ref_715
              temp_schema:
                allOf:
                  - *ref_716
              type:
                allOf:
                  - *ref_717
              view_only:
                allOf:
                  - *ref_718
            title: ApiDataSourceMicrosoftFabric
            refIdentifier: '#/components/schemas/ApiDataSourceMicrosoftFabric'
            requiredProperties: *ref_719
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_720
              catalog_include_list:
                allOf:
                  - *ref_721
              created_from:
                allOf:
                  - *ref_722
              data_retention_days:
                allOf:
                  - *ref_723
              disable_profiling:
                allOf:
                  - *ref_724
              disable_schema_indexing:
                allOf:
                  - *ref_725
              float_tolerance:
                allOf:
                  - *ref_726
              groups:
                allOf:
                  - *ref_727
              hidden:
                allOf:
                  - *ref_728
              id:
                allOf:
                  - *ref_729
              is_paused:
                allOf:
                  - *ref_730
              last_test:
                allOf:
                  - *ref_731
              lineage_schedule:
                allOf:
                  - *ref_732
              max_allowed_connections:
                allOf:
                  - *ref_733
              name:
                allOf:
                  - *ref_734
              oauth_dwh_active:
                allOf:
                  - *ref_735
              options:
                allOf:
                  - *ref_736
              profile_exclude_list:
                allOf:
                  - *ref_737
              profile_include_list:
                allOf:
                  - *ref_738
              profile_schedule:
                allOf:
                  - *ref_739
              queue_name:
                allOf:
                  - *ref_740
              scheduled_queue_name:
                allOf:
                  - *ref_741
              schema_indexing_schedule:
                allOf:
                  - *ref_742
              schema_max_age_s:
                allOf:
                  - *ref_743
              secret_id:
                allOf:
                  - *ref_744
              source:
                allOf:
                  - *ref_745
              temp_schema:
                allOf:
                  - *ref_746
              type:
                allOf:
                  - *ref_747
              view_only:
                allOf:
                  - *ref_748
            title: ApiDataSourceVertica
            refIdentifier: '#/components/schemas/ApiDataSourceVertica'
            requiredProperties: *ref_749
          - type: object
            properties:
              catalog_exclude_list:
                allOf:
                  - *ref_750
              catalog_include_list:
                allOf:
                  - *ref_751
              created_from:
                allOf:
                  - *ref_752
              data_retention_days:
                allOf:
                  - *ref_753
              disable_profiling:
                allOf:
                  - *ref_754
              disable_schema_indexing:
                allOf:
                  - *ref_755
              float_tolerance:
                allOf:
                  - *ref_756
              groups:
                allOf:
                  - *ref_757
              hidden:
                allOf:
                  - *ref_758
              id:
                allOf:
                  - *ref_759
              is_paused:
                allOf:
                  - *ref_760
              last_test:
                allOf:
                  - *ref_761
              lineage_schedule:
                allOf:
                  - *ref_762
              max_allowed_connections:
                allOf:
                  - *ref_763
              name:
                allOf:
                  - *ref_764
              oauth_dwh_active:
                allOf:
                  - *ref_765
              options:
                allOf:
                  - *ref_766
              profile_exclude_list:
                allOf:
                  - *ref_767
              profile_include_list:
                allOf:
                  - *ref_768
              profile_schedule:
                allOf:
                  - *ref_769
              queue_name:
                allOf:
                  - *ref_770
              scheduled_queue_name:
                allOf:
                  - *ref_771
              schema_indexing_schedule:
                allOf:
                  - *ref_772
              schema_max_age_s:
                allOf:
                  - *ref_773
              secret_id:
                allOf:
                  - *ref_774
              source:
                allOf:
                  - *ref_775
              temp_schema:
                allOf:
                  - *ref_776
              type:
                allOf:
                  - *ref_777
              view_only:
                allOf:
                  - *ref_778
            title: ApiDataSourceTrino
            refIdentifier: '#/components/schemas/ApiDataSourceTrino'
            requiredProperties: *ref_779
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