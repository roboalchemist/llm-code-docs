# Source: https://docs.snowflake.com/en/sql-reference/account-usage.md

# Account Usage

In the SNOWFLAKE database, the ACCOUNT_USAGE and READER_ACCOUNT_USAGE schemas enable querying object metadata, as well as historical
usage data, for your account and all reader accounts (if any) associated with the account.

## Overview of Account Usage schemas

ACCOUNT_USAGE:
:   Views that display object metadata and usage metrics for your account.

    In general, these views mirror the corresponding views and table functions in the Snowflake [Snowflake Information Schema](info-schema.md), but
    with the following differences:

    * Records for dropped objects included in each view.
    * Longer retention time for historical usage data.
    * Data latency.

    For more details, see Differences Between Account Usage and Information Schema (in this topic). For more details about each
    view, see ACCOUNT_USAGE Views (in this topic).

READER_ACCOUNT_USAGE:
:   Views that display object metadata and usage metrics for all the reader accounts that have been created for
    your account (as a [Secure Data Sharing](../guides-overview-sharing.md) provider).

    These views are a small subset of the ACCOUNT_USAGE views that apply to reader accounts. Also, each view in this schema contains an
    additional `READER_ACCOUNT_NAME` column for filtering results by reader account.

    For more details about each view, see READER_ACCOUNT_USAGE Views (in this topic).

    Note that these views are empty if no reader accounts have been created for your account.

## Differences between Account Usage and Information Schema

The Account Usage views and the corresponding views (or table functions) in the [Snowflake Information Schema](info-schema.md) utilize identical
structures and naming conventions, but with some key differences, as described in this section:

| Difference | Account Usage | Information Schema |
| --- | --- | --- |
| Includes dropped objects | Yes | No |
| Latency of data | From 45 minutes to 3 hours (varies by view) | None |
| Retention of historical data | 1 Year | From 7 days to 6 months (varies by view/table function) |

For more details, see the following sections.

### Dropped object records

Account usage views include records for all objects that have been dropped. Many of the views for object types contain an
additional `DELETED` column that displays the timestamp when the object was dropped.

In addition, because objects can be dropped and recreated with the same name, to differentiate between objects records that have the
same name, the account usage views include ID columns, where appropriate, that display the internal IDs generated and assigned to
each record by the system.

If a column for an object name (e.g. the `TABLE_NAME` column) is NULL, that object has been dropped. In this case, the
columns for the names and IDs of the parent objects (e.g. the `DATABASE_NAME` and `SCHEMA_NAME` columns) are also
NULL.

Note that in some views, the column for the object name might still contain the name of the object, even if the object has been
dropped.

### Data latency

Due to the process of extracting the data from Snowflake’s internal metadata store, the account usage views have some natural latency:

* For most of the views, the latency is 2 hours (120 minutes).
* For the remaining views, the latency varies between 45 minutes and 3 hours.

For details, see the list of views for each schema (in this topic). Also, note that these are all maximum time lengths; the actual
latency for a given view when the view is queried may be less.

In contrast, views/table functions in the [Snowflake Information Schema](info-schema.md) do not have any latency.

### Historical data retention

Certain account usage views provide historical usage metrics. The retention period for these views is 1 year (365 days).

In contrast, the corresponding views and table functions in the [Snowflake Information Schema](info-schema.md) have much shorter retention periods,
ranging from 7 days to 6 months, depending on the view.

## ACCOUNT_USAGE views

The ACCOUNT_USAGE schema contains the following views:

| View | Type | Latency [1] | Edition [3] | Notes |
| --- | --- | --- | --- | --- |
| [ACCESS_HISTORY](account-usage/access_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [AGGREGATE_ACCESS_HISTORY](account-usage/aggregate_access_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [AGGREGATE_QUERY_HISTORY](account-usage/aggregate_query_history.md) | Historical | 3 hours |  |  |
| [AGGREGATION_POLICIES](account-usage/aggregation_policies.md) | Object | 2 hours |  |  |
| [ALERT_HISTORY](account-usage/alert_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [ANOMALIES_DAILY](account-usage/anomalies_daily.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [APPLICATION_CALLBACK_HISTORY](account-usage/application_callback_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [APPLICATION_CONFIGURATIONS](account-usage/application_configurations.md) | Object | 3 hours |  | Data retained for 1 year. |
| [APPLICATION_CONFIGURATION_VALUE_HISTORY](account-usage/application_configuration_value_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [APPLICATION_DAILY_USAGE_HISTORY](account-usage/application_daily_usage_history.md) | Historical | 24 hours |  | Data retained for 1 year. |
| [APPLICATION_SPECIFICATION_STATUS_HISTORY](account-usage/application_specification_status_history.md) | Historical | 1 hour |  | Data retained for 1 year. |
| [APPLICATION_SPECIFICATIONS](account-usage/application_specifications.md) | Historical | 1 hour |  | Data for deleted app specifications is retained for 1 year. |
| [ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY](account-usage/archive_storage_data_retrieval_usage_history.md) | Historical | 1 hour |  | Data retained for 1 year. |
| [AUTOMATIC_CLUSTERING_HISTORY](account-usage/automatic_clustering_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [BACKUP_OPERATION_HISTORY](account-usage/backup_operation_history.md) | Historical | 6 hours |  | Data retained for 1 year. |
| [BACKUP_POLICIES](account-usage/backup_policies.md) | Object | 6 hours |  |  |
| [BACKUP_SETS](account-usage/backup_sets.md) | Object | 6 hours |  |  |
| [BACKUP_STORAGE_USAGE](account-usage/backup_storage_usage.md) | Historical | 6 hours |  | Data retained for 1 year. |
| [BACKUPS](account-usage/backups.md) | Object | 6 hours |  |  |
| [BLOCK_STORAGE_HISTORY](account-usage/block_storage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [BLOCK_STORAGE_SNAPSHOTS](account-usage/block_storage_snapshots.md) | Object | 3 hours |  |  |
| [CATALOG_LINKED_DATABASE_USAGE_HISTORY](account-usage/catalog_linked_database_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [CLASS_INSTANCES](account-usage/class_instances.md) | Object | 3 hours |  | Data retained for 1 year. |
| [CLASSES](account-usage/classes.md) | Object | 3 hours |  | Data retained for 1 year. |
| [COLUMN_QUERY_PRUNING_HISTORY](account-usage/column_query_pruning_history.md) | Historical | 4 hours |  | Data retained for 1 year. |
| [COLUMNS](account-usage/columns.md) | Object | 90 minutes |  |  |
| [COMPLETE_TASK_GRAPHS](account-usage/complete_task_graphs.md) | Historical | 45 minutes |  | Data retained for 1 year. |
| [COMPUTE_POOLS](account-usage/compute_pools.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [CONTACT_REFERENCES](account-usage/contact_references.md) | Object | 3 hours |  |  |
| [CONTACTS](account-usage/contacts.md) | Object | 3 hours |  |  |
| [COPY_FILES_HISTORY](account-usage/copy_files_history.md) | Historical |  |  | Data retained for 1 year. |
| [COPY_HISTORY](account-usage/copy_history.md) | Historical | 2 hours [2] |  | Data retained for 1 year. |
| [CORTEX_AGENT_USAGE_HISTORY](account-usage/cortex_agent_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_AI_FUNCTIONS_USAGE_HISTORY](account-usage/cortex_ai_functions_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_AISQL_USAGE_HISTORY](account-usage/cortex_aisql_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_ANALYST_USAGE_HISTORY](account-usage/cortex_analyst_usage_history.md) | Historical | One hour |  | Data retained for 1 year. |
| [CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY](account-usage/cortex_document_processing_usage_history.md) | Historical | 1 hour |  | Data retained for 1 year. |
| [CORTEX_FINE_TUNING_USAGE_HISTORY](account-usage/cortex_fine_tuning_usage_history.md) | Historical | 1 hour |  | Data retained for 1 year. |
| [CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY](account-usage/cortex_functions_query_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_FUNCTIONS_USAGE_HISTORY](account-usage/cortex_functions_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_PROVISIONED_THROUGHPUT_USAGE_HISTORY](account-usage/cortex_provisioned_throughput_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_REST_API_USAGE_HISTORY](account-usage/cortex_rest_api_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [CORTEX_SEARCH_DAILY_USAGE_HISTORY](account-usage/cortex_search_daily_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [CORTEX_SEARCH_SERVING_USAGE_HISTORY](account-usage/cortex_search_serving_usage_history.md) | Historical | 1 hour |  | Data retained for 1 year. |
| [CREDENTIALS](account-usage/credentials.md) | Object | 2 hours |  |  |
| [DATA_CLASSIFICATION_LATEST](account-usage/data_classification_latest.md) | Object | 3 hours | Enterprise Edition (or higher) | Data retained for as long as the table exists. |
| [DATA_METRIC_FUNCTION_EXPECTATIONS](account-usage/data_metric_function_expectations.md) | Object | 30 minutes | Enterprise Edition (or higher) |  |
| [DATA_METRIC_FUNCTION_REFERENCES](account-usage/data_metric_function_references.md) | Object | 3 hours | Enterprise Edition (or higher) |  |
| [DATA_QUALITY_MONITORING_USAGE_HISTORY](account-usage/data_quality_monitoring_usage_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [DATABASES](account-usage/databases.md) | Object | 3 hours |  |  |
| [DATABASE_REPLICATION_USAGE_HISTORY](account-usage/database_replication_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [DATABASE_STORAGE_USAGE_HISTORY](account-usage/database_storage_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [DATA_TRANSFER_HISTORY](account-usage/data_transfer_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [DOCUMENT_AI_USAGE_HISTORY](account-usage/document_ai_usage_history.md) | Historical |  |  | Data retained for 1 year. |
| [DYNAMIC_TABLE_REFRESH_HISTORY](account-usage/dynamic_table_refresh_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [ELEMENT_TYPES](account-usage/element_types.md) | Object | 90 minutes |  |  |
| [EVENT_USAGE_HISTORY](account-usage/event_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [EXTERNAL_ACCESS_HISTORY](account-usage/external_access_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [FIELDS](account-usage/fields.md) | Object | 90 minutes |  |  |
| [FILE_FORMATS](account-usage/file_formats.md) | Object | 2 hours |  |  |
| [FUNCTIONS](account-usage/functions.md) | Object | 2 hours |  |  |
| [GRANTS_TO_ROLES](account-usage/grants_to_roles.md) | Object | 2 hours |  |  |
| [GRANTS_TO_SHARES](account-usage/grants_to_shares.md) | Object | 3 hours |  |  |
| [GRANTS_TO_USERS](account-usage/grants_to_users.md) | Object | 2 hours |  |  |
| [HYBRID_TABLES](account-usage/hybrid_tables.md) | Object | 3 hours |  |  |
| [HYBRID_TABLE_USAGE_HISTORY](account-usage/hybrid_table_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. (As of March 1, 2026, hybrid table requests are no longer billed.) |
| [ICEBERG_STORAGE_OPTIMIZATION_HISTORY](account-usage/iceberg_storage_optimization_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [INDEX_COLUMNS](account-usage/index_columns.md) | Object | 3 hours |  |  |
| [INDEXES](account-usage/indexes.md) | Object | 3 hours |  |  |
| [INGRESS_NETWORK_ACCESS_HISTORY](account-usage/ingress_network_access_history.md) | Historical | 4 hours |  | Data retained for 1 year. |
| [INTERNAL_DATA_TRANSFER_HISTORY](account-usage/internal_data_transfer_history.md) | Historical | 3 hours |  |  |
| [INTERNAL_STAGE_NETWORK_ACCESS_HISTORY](account-usage/internal_stage_network_access_history.md) | Historical | 6 hours |  | Data retained for 1 year. |
| [JOIN_POLICIES](account-usage/join_policies.md) | Object | 2 hours |  |  |
| [LISTINGS](account-usage/listings.md) | Object | 3 hours |  |  |
| [LOAD_HISTORY](account-usage/load_history.md) | Historical | 90 minutes [2] |  | Data retained for 1 year. |
| [LOCK_WAIT_HISTORY](account-usage/lock_wait_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [LOGIN_HISTORY](account-usage/login_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [MASKING_POLICIES](account-usage/masking_policies.md) | Object | 2 hours |  |  |
| [MATERIALIZED_VIEW_REFRESH_HISTORY](account-usage/materialized_view_refresh_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [METERING_DAILY_HISTORY](account-usage/metering_daily_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [METERING_HISTORY](account-usage/metering_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [NETWORK_POLICIES](account-usage/network_policies.md) | Object | 2 hours |  |  |
| [NETWORK_RULE_REFERENCES](account-usage/network_rule_references.md) | Object | 2 hours |  |  |
| [NETWORK_RULES](account-usage/network_rules.md) | Object | 2 hours |  |  |
| [NOTEBOOKS_CONTAINER_RUNTIME_HISTORY](account-usage/notebooks_container_runtime_history.md) | Historical | 3 hours |  |  |
| [OBJECT_ACCESS_REQUEST_HISTORY](account-usage/object_access_request_history.md) | Historical | 3 hours |  |  |
| [OBJECT_DEPENDENCIES](account-usage/object_dependencies.md) | Historical | 3 hours |  |  |
| [ONLINE_FEATURE_TABLE_REFRESH_HISTORY](account-usage/online_feature_table_refresh_history.md) | Historical | 3 hours |  |  |
| [OPENFLOW_USAGE_HISTORY](account-usage/openflow_usage_history.md) | Historical | 3 hours |  |  |
| [OUTBOUND_PRIVATELINK_ENDPOINTS](account-usage/outbound_privatelink_endpoints.md) | Object | 2 hours | Business Critical (or higher) | Data for deleted endpoints is retained for 1 year. |
| [PASSWORD_POLICIES](account-usage/password_policies.md) | Object | 2 hours |  |  |
| [PIPES](account-usage/pipes.md) | Object | 2 hours |  |  |
| [PIPE_USAGE_HISTORY](account-usage/pipe_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [POLICY_REFERENCES](account-usage/policy_references.md) | Object | 2 hours |  |  |
| [POSTGRES_STORAGE_USAGE_HISTORY](account-usage/postgres_storage_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [PRIVACY_BUDGETS](account-usage/privacy_budgets.md) | Object | 24 hours | Enterprise Edition (or higher) |  |
| [PRIVACY_POLICIES](account-usage/privacy_policies.md) | Object | 2 hours | Enterprise Edition (or higher) |  |
| [PROCEDURES](account-usage/procedures.md) | Object | 2 hours |  |  |
| [PROJECTION_POLICIES](account-usage/projection_policies.md) | Object | 2 hours |  |  |
| [QUERY_ACCELERATION_ELIGIBLE](account-usage/query_acceleration_eligible.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [QUERY_ACCELERATION_HISTORY](account-usage/query_acceleration_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [QUERY_ATTRIBUTION_HISTORY](account-usage/query_attribution_history.md) | Historical | 8 hours |  | Data retained for 1 year. |
| [QUERY_HISTORY](account-usage/query_history.md) | Historical | 45 minutes |  | Data retained for 1 year. |
| [QUERY_INSIGHTS](account-usage/query_insights.md) | Historical |  |  | Data retained for 1 year. |
| [REFERENTIAL_CONSTRAINTS](account-usage/referential_constraints.md) | Object | 2 hours |  |  |
| [REPLICATION_GROUP_REFRESH_HISTORY](account-usage/replication_group_refresh_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [REPLICATION_GROUP_USAGE_HISTORY](account-usage/replication_group_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [REPLICATION_GROUPS](account-usage/replication_groups.md) | Object | 2 hours |  |  |
| [REPLICATION_USAGE_HISTORY](account-usage/replication_usage_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [RESOURCE_MONITORS](account-usage/resource_monitors.md) | Object | 2 hours |  |  |
| [ROLES](account-usage/roles.md) | Object | 2 hours |  |  |
| [ROW_ACCESS_POLICIES](account-usage/row_access_policies.md) | Object | 2 hours |  |  |
| [SCHEMATA](account-usage/schemata.md) | Object | 2 hours |  |  |
| [SEARCH_OPTIMIZATION_BENEFITS](account-usage/search_optimization_benefits.md) | Historical | 6 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [SEARCH_OPTIMIZATION_HISTORY](account-usage/search_optimization_history.md) | Historical | 3 hours | Enterprise Edition (or higher) | Data retained for 1 year. |
| [SECRETS](account-usage/secrets.md) | Object | 2 hours |  |  |
| [SEMANTIC_DIMENSIONS](account-usage/semantic_dimensions.md) | Object | 2 hours |  |  |
| [SEMANTIC_FACTS](account-usage/semantic_facts.md) | Object | 2 hours |  |  |
| [SEMANTIC_METRICS](account-usage/semantic_metrics.md) | Object | 2 hours |  |  |
| [SEMANTIC_RELATIONSHIPS](account-usage/semantic_relationships.md) | Object | 2 hours |  |  |
| [SEMANTIC_TABLES](account-usage/semantic_tables.md) | Object | 2 hours |  |  |
| [SEMANTIC_VIEWS](account-usage/semantic_views.md) | Object | 2 hours |  |  |
| [SEQUENCES](account-usage/sequences.md) | Object | 2 hours |  |  |
| [SERVERLESS_ALERT_HISTORY](account-usage/serverless_alert_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [SERVERLESS_TASK_HISTORY](account-usage/serverless_task_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [SERVICES](account-usage/services.md) | Object | 3 hours |  |  |
| [SESSION_POLICIES](account-usage/session_policies.md) | Object | 2 hours |  |  |
| [SESSIONS](account-usage/sessions.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [SHARES](account-usage/shares.md) | Object | 3 hours |  |  |
| [SNAPSHOT_OPERATION_HISTORY](account-usage/snapshot_operation_history.md) | Historical | 6 hours |  | Data retained for 1 year. This view is deprecated. Use the [BACKUP_OPERATION_HISTORY](account-usage/backup_operation_history.md) view instead. |
| [SNAPSHOT_POLICIES](account-usage/snapshot_policies.md) | Object | 6 hours |  | This view is deprecated. Use the [BACKUP_POLICIES](account-usage/backup_policies.md) view instead. |
| [SNAPSHOT_SETS](account-usage/snapshot_sets.md) | Object | 6 hours |  | This view is deprecated. Use the [BACKUP_SETS](account-usage/backup_sets.md) view instead. |
| [SNAPSHOT_STORAGE_USAGE](account-usage/snapshot_storage_usage.md) | Historical | 6 hours |  | Data retained for 1 year. This view is deprecated. Use the [BACKUP_STORAGE_USAGE](account-usage/backup_storage_usage.md) view instead. |
| [SNAPSHOTS](account-usage/snapshots.md) | Object | 6 hours |  | This view is deprecated. Use the [BACKUPS](account-usage/backups.md) view instead. |
| [SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY](account-usage/snowflake_intelligence_usage_history_view.md) | Historical |  |  | Data retained for 1 year. |
| [SNOWPARK_CONTAINER_SERVICES_HISTORY](account-usage/snowpark_container_services_history.md) | Historical | 3 hour |  | Data retained for 1 year. |
| [SNOWPIPE_STREAMING_CHANNEL_HISTORY](account-usage/snowpipe_streaming_channel_history.md) | Historical |  |  |  |
| [SNOWPIPE_STREAMING_CLIENT_HISTORY](account-usage/snowpipe_streaming_client_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [SNOWPIPE_STREAMING_FILE_MIGRATION_HISTORY](account-usage/snowpipe_streaming_file_migration_history.md) | Historical | 12 hours |  | Data retained for 1 year. |
| [STAGES](account-usage/stages.md) | Object | 2 hours |  |  |
| [STAGE_STORAGE_USAGE_HISTORY](account-usage/stage_storage_usage_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [STORAGE_LIFECYCLE_POLICIES](account-usage/storage_lifecycle_policies.md) | Object | 2 hours |  |  |
| [STORAGE_LIFECYCLE_POLICY_HISTORY](account-usage/storage_lifecycle_policy_history.md) | Historical | 2 hours |  | Data retained for 1 year. |
| [STORAGE_USAGE](account-usage/storage_usage.md) | Historical | 2 hours |  | Combined usage across all database tables and internal stages. Data retained for 1 year. |
| [TABLES](account-usage/tables.md) | Object | 90 minutes |  |  |
| [TABLE_CONSTRAINTS](account-usage/table_constraints.md) | Object | 2 hours |  |  |
| [TABLE_DML_HISTORY](account-usage/table_dml_history.md) | Historical | 6 hours |  | Data retained for 1 year. |
| [TABLE_PRUNING_HISTORY](account-usage/table_pruning_history.md) | Historical | 6 hours |  | Data retained for 1 year. |
| [TABLE_QUERY_PRUNING_HISTORY](account-usage/table_query_pruning_history.md) | Historical | 4 hours |  | Data retained for 1 year. |
| [TABLE_STORAGE_METRICS](account-usage/table_storage_metrics.md) | Object | 90 minutes |  |  |
| [TAG_REFERENCES](account-usage/tag_references.md) | Object | 2 hours |  |  |
| [TAGS](account-usage/tags.md) | Object | 2 hours |  |  |
| [TASK_HISTORY](account-usage/task_history.md) | Historical | 45 minutes |  |  |
| [TASK_VERSIONS](account-usage/task_versions.md) | Object | 3 hours |  |  |
| [TRUST_CENTER_FINDINGS](account-usage/trust_center_findings.md) | Historical | 1 hour |  |  |
| [USERS](account-usage/users.md) | Object | 2 hours |  |  |
| [VIEWS](account-usage/views.md) | Object | 90 minutes |  |  |
| [WAREHOUSE_EVENTS_HISTORY](account-usage/warehouse_events_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [WAREHOUSE_LOAD_HISTORY](account-usage/warehouse_load_history.md) | Historical | 3 hours |  | Data retained for 1 year. |
| [WAREHOUSE_METERING_HISTORY](account-usage/warehouse_metering_history.md) | Historical | 3 hours |  | Data retained for 1 year. |

[1] All latency times are approximate; in some instances, the actual latency may be lower.

[2] The latency of the views for a given table may be up to 2 days if both of the following conditions are true: 1. Fewer than 32 DML statements have been added to the given table since it was last updated in LOAD_HISTORY or COPY_HISTORY. 2. Fewer than 100 rows have been added to the given table since it was last updated in LOAD_HISTORY or COPY_HISTORY.

[3] Unless otherwise noted, the Account Usage view is available to all accounts.

### Account Usage table functions

Currently, Snowflake supports one ACCOUNT_USAGE table function:

| Table Function | Data Retention | Notes |
| --- | --- | --- |
| [TAG_REFERENCES_WITH_LINEAGE](functions/tag_references_with_lineage.md) | N/A | Results are only returned for the role that has access to the specified object. |

> **Note:**
>
> Similar to the Account Usage views, please account for latency when calling this table function. The expected latency for this table
> function is similar to the latency for the TAG_REFERENCES view.

## READER_ACCOUNT_USAGE views

The READER_ACCOUNT_USAGE schema contains the following views:

| View | Type | Latency [1] | Notes |
| --- | --- | --- | --- |
| [LOGIN_HISTORY](account-usage/login_history.md) | Historical | 2 hours | Data retained for 1 year. |
| [QUERY_HISTORY](account-usage/query_history.md) | Historical | 45 minutes | Data retained for 1 year. |
| [RESOURCE_MONITORS](account-usage/resource_monitors.md) | Object | 2 hours |  |
| [STORAGE_USAGE](account-usage/storage_usage.md) | Historical | 24 hours | Combined usage across all database tables and internal stages. Data retained for 1 year. |
| [WAREHOUSE_METERING_HISTORY](account-usage/warehouse_metering_history.md) | Historical | 24 hours | Data retained for 1 year. |

[1] All latency times are approximate; in some instances, the actual latency may be lower.

## Enabling other roles to use schemas in the SNOWFLAKE database

By default, the SNOWFLAKE database is visible to all users; however, access to schemas in this database can be granted by a user with the
ACCOUNTADMIN role using either of the following approaches:

* Grant IMPORTED PRIVILEGES on the SNOWFLAKE database.
* Grant a SNOWFLAKE database role to an account role.

> **Important:**
>
> To avoid unintentionally granting access to organization-level data, consider using SNOWFLAKE database roles to grant access to views in the ACCOUNT_USAGE schema.
>
> For more information, refer to [GRANT DATABASE ROLE](sql/grant-database-role.md).

For example, to grant IMPORTED PRIVILEGES on the SNOWFLAKE database to two additional roles:

> ```sqlexample
> USE ROLE ACCOUNTADMIN;
>
> GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE SYSADMIN;
> GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE customrole1;
> ```

A user with that is granted the `customrole1` role can query a view as follows:

> ```sqlexample
> USE ROLE customrole1;
>
> SELECT database_name, database_owner FROM SNOWFLAKE.ACCOUNT_USAGE.DATABASES;
> ```

For additional examples, see Querying the Account Usage views.

### ACCOUNT_USAGE schema SNOWFLAKE database roles

In addition, you can grant finer control to accounts using SNOWFLAKE Database roles.
For more information on database roles, see [database roles](../user-guide/security-access-control-considerations.md).

ACCOUNT_USAGE schemas have four defined SNOWFLAKE database roles, each granted the SELECT privilege on specific views.

| Role | Purpose and Description |
| --- | --- |
| OBJECT_VIEWER | The OBJECT_VIEWER role provides visibility into object metadata. |
| USAGE_VIEWER | The USAGE_VIEWER role provides visibility into historical usage information. |
| GOVERNANCE_VIEWER | The GOVERNANCE_VIEWER role provides visibility into data governance related information. |
| SECURITY_VIEWER | The SECURITY_VIEWER role provides visibility into security based information. |

### Database role required to access ACCOUNT_USAGE views

The OBJECT_VIEWER, USAGE_VIEWER, GOVERNANCE_VIEWER, and SECURITY_VIEWER roles have the SELECT privilege to query Account Usage
views in the shared SNOWFLAKE database. Use the following table to determine which database role has access to a view.

| View | Database Role |
| --- | --- |
| [ACCESS_HISTORY view](account-usage/access_history.md) | GOVERNANCE_VIEWER |
| [APPLICATION_CONFIGURATIONS view](account-usage/application_configurations.md) | SECURITY_VIEWER |
| [AGGREGATE_ACCESS_HISTORY view](account-usage/aggregate_access_history.md) | GOVERNANCE_VIEWER |
| [AGGREGATE_QUERY_HISTORY view](account-usage/aggregate_query_history.md) | GOVERNANCE_VIEWER |
| [AGGREGATION_POLICIES view](account-usage/aggregation_policies.md) | GOVERNANCE_VIEWER |
| [ANOMALIES_DAILY view](account-usage/anomalies_daily.md) | USAGE_VIEWER |
| [APPLICATION_CALLBACK_HISTORY view](account-usage/application_callback_history.md) | SECURITY_VIEWER |
| [APPLICATION_CONFIGURATION_VALUE_HISTORY view](account-usage/application_configuration_value_history.md) | SECURITY_VIEWER |
| [APPLICATION_DAILY_USAGE_HISTORY view](account-usage/application_daily_usage_history.md) | USAGE_VIEWER |
| [APPLICATION_SPECIFICATION_STATUS_HISTORY view](account-usage/application_specification_status_history.md) | SECURITY_VIEWER |
| [APPLICATION_SPECIFICATIONS view](account-usage/application_specifications.md) | SECURITY_VIEWER |
| [ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY view](account-usage/archive_storage_data_retrieval_usage_history.md) | USAGE_VIEWER |
| [AUTOMATIC_CLUSTERING_HISTORY view](account-usage/automatic_clustering_history.md) | USAGE_VIEWER |
| [BLOCK_STORAGE_HISTORY view](account-usage/block_storage_history.md) | USAGE_VIEWER |
| [BLOCK_STORAGE_SNAPSHOTS view](account-usage/block_storage_snapshots.md) | OBJECT_VIEWER |
| [CATALOG_LINKED_DATABASE_USAGE_HISTORY view](account-usage/catalog_linked_database_usage_history.md) | USAGE_VIEWER |
| [CLASS_INSTANCES view](account-usage/class_instances.md) | USAGE_VIEWER |
| [CLASSES view](account-usage/classes.md) | USAGE_VIEWER |
| [COLUMN_QUERY_PRUNING_HISTORY view](account-usage/column_query_pruning_history.md) | USAGE_VIEWER |
| [COLUMNS view](account-usage/columns.md) | OBJECT_VIEWER |
| [COMPLETE_TASK_GRAPHS view](account-usage/complete_task_graphs.md) | OBJECT_VIEWER |
| [CONTACT_REFERENCES view](account-usage/contact_references.md) | GOVERNANCE_VIEWER |
| [CONTACTS view](account-usage/contacts.md) | GOVERNANCE_VIEWER |
| [COPY_FILES_HISTORY view](account-usage/copy_files_history.md) | USAGE_VIEWER |
| [COPY_HISTORY view](account-usage/copy_history.md) | USAGE_VIEWER |
| [CORTEX_AI_FUNCTIONS_USAGE_HISTORY view](account-usage/cortex_ai_functions_usage_history.md) | USAGE_VIEWER |
| [CORTEX_AGENT_USAGE_HISTORY view](account-usage/cortex_agent_usage_history.md) | USAGE_VIEWER |
| [CORTEX_AISQL_USAGE_HISTORY view](account-usage/cortex_aisql_usage_history.md) | USAGE_VIEWER |
| [CORTEX_ANALYST_USAGE_HISTORY view](account-usage/cortex_analyst_usage_history.md) | USAGE_VIEWER |
| [CORTEX_DOCUMENT_PROCESSING_USAGE_HISTORY view](account-usage/cortex_document_processing_usage_history.md) | USAGE_VIEWER |
| [CORTEX_FINE_TUNING_USAGE_HISTORY view](account-usage/cortex_fine_tuning_usage_history.md) | USAGE_VIEWER |
| [CORTEX_FUNCTIONS_QUERY_USAGE_HISTORY view](account-usage/cortex_functions_query_usage_history.md) | USAGE_VIEWER |
| [CORTEX_FUNCTIONS_USAGE_HISTORY view](account-usage/cortex_functions_usage_history.md) | USAGE_VIEWER |
| [CORTEX_SEARCH_DAILY_USAGE_HISTORY view](account-usage/cortex_search_daily_usage_history.md) | USAGE_VIEWER |
| [CORTEX_PROVISIONED_THROUGHPUT_USAGE_HISTORY view](account-usage/cortex_provisioned_throughput_usage_history.md) | USAGE_VIEWER |
| [CORTEX_REST_API_USAGE_HISTORY view](account-usage/cortex_rest_api_usage_history.md) | USAGE_VIEWER |
| [CORTEX_SEARCH_SERVING_USAGE_HISTORY view](account-usage/cortex_search_serving_usage_history.md) | USAGE_VIEWER |
| [CREDENTIALS view](account-usage/credentials.md) | SECURITY_VIEWER |
| [DATA_CLASSIFICATION_LATEST view](account-usage/data_classification_latest.md) | GOVERNANCE_VIEWER |
| [DATA_METRIC_FUNCTION_EXPECTATIONS view](account-usage/data_metric_function_expectations.md) | USAGE_VIEWER or GOVERNANCE_VIEWER |
| [DATA_METRIC_FUNCTION_REFERENCES view](account-usage/data_metric_function_references.md) | USAGE_VIEWER or GOVERNANCE_VIEWER |
| [DATA_QUALITY_MONITORING_USAGE_HISTORY view](account-usage/data_quality_monitoring_usage_history.md) | USAGE_VIEWER |
| [DATA_TRANSFER_HISTORY view](account-usage/data_transfer_history.md) | USAGE_VIEWER |
| [DATABASE_STORAGE_USAGE_HISTORY view](account-usage/database_storage_usage_history.md) | USAGE_VIEWER |
| [DATABASES view](account-usage/databases.md) | OBJECT_VIEWER |
| [DOCUMENT_AI_USAGE_HISTORY view](account-usage/document_ai_usage_history.md) | USAGE_VIEWER |
| [DYNAMIC_TABLE_REFRESH_HISTORY view](account-usage/dynamic_table_refresh_history.md) | USAGE_VIEWER |
| [ELEMENT_TYPES view](account-usage/element_types.md) | OBJECT_VIEWER |
| [EVENT_USAGE_HISTORY view](account-usage/event_usage_history.md) | USAGE_VIEWER |
| [EXTERNAL_ACCESS_HISTORY view](account-usage/external_access_history.md) | USAGE_VIEWER |
| [FIELDS view](account-usage/fields.md) | OBJECT_VIEWER |
| [FILE_FORMATS view](account-usage/file_formats.md) | OBJECT_VIEWER |
| [FUNCTIONS view](account-usage/functions.md) | OBJECT_VIEWER |
| [GRANTS_TO_ROLES view](account-usage/grants_to_roles.md) | SECURITY_VIEWER |
| [GRANTS_TO_SHARES view](account-usage/grants_to_shares.md) | SECURITY_VIEWER |
| [GRANTS_TO_USERS view](account-usage/grants_to_users.md) | SECURITY_VIEWER |
| [HYBRID_TABLE_USAGE_HISTORY view](account-usage/hybrid_table_usage_history.md) | USAGE_VIEWER |
| [HYBRID_TABLES view](account-usage/hybrid_tables.md) | OBJECT_VIEWER |
| [ICEBERG_STORAGE_OPTIMIZATION_HISTORY view](account-usage/iceberg_storage_optimization_history.md) | USAGE_VIEWER |
| [INDEX_COLUMNS view](account-usage/index_columns.md) | OBJECT_VIEWER |
| [INDEXES view](account-usage/indexes.md) | OBJECT_VIEWER |
| [INGRESS_NETWORK_ACCESS_HISTORY view](account-usage/ingress_network_access_history.md) | SECURITY_VIEWER |
| [INTERNAL_DATA_TRANSFER_HISTORY view](account-usage/internal_data_transfer_history.md) | USAGE_VIEWER |
| [INTERNAL_STAGE_NETWORK_ACCESS_HISTORY view](account-usage/internal_stage_network_access_history.md) | SECURITY_VIEWER |
| [JOIN_POLICIES view](account-usage/join_policies.md) | GOVERNANCE_VIEWER |
| [LISTINGS view](account-usage/listings.md) | SECURITY_VIEWER |
| [LOAD_HISTORY view](account-usage/load_history.md) | USAGE_VIEWER |
| [LOGIN_HISTORY view](account-usage/login_history.md) | SECURITY_VIEWER |
| [MASKING_POLICIES view](account-usage/masking_policies.md) | GOVERNANCE_VIEWER |
| [MATERIALIZED_VIEW_REFRESH_HISTORY view](account-usage/materialized_view_refresh_history.md) | USAGE_VIEWER |
| [METERING_DAILY_HISTORY view](account-usage/metering_daily_history.md) | USAGE_VIEWER |
| [METERING_HISTORY view](account-usage/metering_history.md) | USAGE_VIEWER |
| [NETWORK_POLICIES view](account-usage/network_policies.md) | SECURITY_VIEWER |
| [NETWORK_RULE_REFERENCES view](account-usage/network_rule_references.md) | SECURITY_VIEWER |
| [NETWORK_RULES view](account-usage/network_rules.md) | SECURITY_VIEWER |
| [NOTEBOOKS_CONTAINER_RUNTIME_HISTORY view](account-usage/notebooks_container_runtime_history.md) | USAGE_VIEWER |
| [OBJECT_ACCESS_REQUEST_HISTORY view](account-usage/object_access_request_history.md) | OBJECT_VIEWER |
| [OBJECT_DEPENDENCIES view](account-usage/object_dependencies.md) | OBJECT_VIEWER |
| [ACCOUNT_USAGE.ONLINE_FEATURE_TABLE_REFRESH_HISTORY](account-usage/online_feature_table_refresh_history.md) | USAGE_VIEWER |
| [OPENFLOW_USAGE_HISTORY view](account-usage/openflow_usage_history.md) | USAGE_VIEWER |
| [OUTBOUND_PRIVATELINK_ENDPOINTS view](account-usage/outbound_privatelink_endpoints.md) | SECURITY_VIEWER |
| [PASSWORD_POLICIES view](account-usage/password_policies.md) | SECURITY_VIEWER |
| [PIPE_USAGE_HISTORY view](account-usage/pipe_usage_history.md) | USAGE_VIEWER |
| [PIPES view](account-usage/pipes.md) | OBJECT_VIEWER |
| [POLICY_REFERENCES view](account-usage/policy_references.md) | GOVERNANCE_VIEWER, SECURITY_VIEWER |
| [POSTGRES_STORAGE_USAGE_HISTORY view](account-usage/postgres_storage_usage_history.md) | USAGE_VIEWER |
| [PRIVACY_BUDGETS view](account-usage/privacy_budgets.md) | GOVERNANCE_VIEWER |
| [PRIVACY_POLICIES view](account-usage/privacy_policies.md) | GOVERNANCE_VIEWER |
| [PROCEDURES view](account-usage/procedures.md) | OBJECT_VIEWER |
| [PROJECTION_POLICIES view](account-usage/projection_policies.md) | GOVERNANCE_VIEWER |
| [QUERY_ACCELERATION_ELIGIBLE view](account-usage/query_acceleration_eligible.md) | GOVERNANCE_VIEWER |
| [QUERY_ATTRIBUTION_HISTORY view](account-usage/query_attribution_history.md) | USAGE_VIEWER, GOVERNANCE_VIEWER |
| [QUERY_HISTORY view](account-usage/query_history.md) | GOVERNANCE_VIEWER |
| [QUERY_INSIGHTS view](account-usage/query_insights.md) | GOVERNANCE_VIEWER |
| [REFERENTIAL_CONSTRAINTS view](account-usage/referential_constraints.md) | OBJECT_VIEWER |
| [REPLICATION_GROUP_REFRESH_HISTORY view](account-usage/replication_group_refresh_history.md) | USAGE_VIEWER |
| [REPLICATION_GROUP_USAGE_HISTORY view](account-usage/replication_group_usage_history.md) | USAGE_VIEWER |
| [REPLICATION_GROUPS view](account-usage/replication_groups.md) | OBJECT_VIEWER |
| [REPLICATION_USAGE_HISTORY view](account-usage/replication_usage_history.md) | USAGE_VIEWER |
| [RESOURCE_MONITORS view](account-usage/resource_monitors.md) | OBJECT_VIEWER |
| [ROLES view](account-usage/roles.md) | SECURITY_VIEWER |
| [ROW_ACCESS_POLICIES view](account-usage/row_access_policies.md) | GOVERNANCE_VIEWER |
| [SCHEMATA view](account-usage/schemata.md) | OBJECT_VIEWER |
| [SEARCH_OPTIMIZATION_BENEFITS view](account-usage/search_optimization_benefits.md) | USAGE_VIEWER |
| [SEARCH_OPTIMIZATION_HISTORY view](account-usage/search_optimization_history.md) | USAGE_VIEWER |
| [SECRETS view](account-usage/secrets.md) | SECURITY_VIEWER |
| [SEMANTIC_DIMENSIONS view](account-usage/semantic_dimensions.md) | OBJECT_VIEWER |
| [SEMANTIC_FACTS view](account-usage/semantic_facts.md) | OBJECT_VIEWER |
| [SEMANTIC_METRICS view](account-usage/semantic_metrics.md) | OBJECT_VIEWER |
| [SEMANTIC_RELATIONSHIPS view](account-usage/semantic_relationships.md) | OBJECT_VIEWER |
| [SEMANTIC_TABLES view](account-usage/semantic_tables.md) | OBJECT_VIEWER |
| [SEMANTIC_VIEWS view](account-usage/semantic_views.md) | OBJECT_VIEWER |
| [SEQUENCES view](account-usage/sequences.md) | OBJECT_VIEWER |
| [SERVERLESS_ALERT_HISTORY view](account-usage/serverless_alert_history.md) | USAGE_VIEWER |
| [SERVERLESS_TASK_HISTORY view](account-usage/serverless_task_history.md) | USAGE_VIEWER |
| [SERVICES view](account-usage/services.md) | OBJECT_VIEWER |
| [SESSION_POLICIES view](account-usage/session_policies.md) | SECURITY_VIEWER |
| [SESSIONS view](account-usage/sessions.md) | SECURITY_VIEWER |
| [SHARES view](account-usage/shares.md) | SECURITY_VIEWER |
| [SNAPSHOT_OPERATION_HISTORY view — Deprecated](account-usage/snapshot_operation_history.md) | OBJECT_VIEWER |
| [SNAPSHOT_POLICIES view — Deprecated](account-usage/snapshot_policies.md) | OBJECT_VIEWER |
| [SNAPSHOT_SETS view — Deprecated](account-usage/snapshot_sets.md) | OBJECT_VIEWER |
| [SNAPSHOT_STORAGE_USAGE view — Deprecated](account-usage/snapshot_storage_usage.md) | OBJECT_VIEWER |
| [SNAPSHOTS view — Deprecated](account-usage/snapshots.md) | OBJECT_VIEWER |
| [SNOWFLAKE_INTELLIGENCE_USAGE_HISTORY view](account-usage/snowflake_intelligence_usage_history_view.md) | USAGE_VIEWER |
| [SNOWPARK_CONTAINER_SERVICES_HISTORY view](account-usage/snowpark_container_services_history.md) | USAGE_VIEWER |
| [SNOWPIPE_STREAMING_CHANNEL_HISTORY view](account-usage/snowpipe_streaming_channel_history.md) | USAGE_VIEWER |
| [STAGE_STORAGE_USAGE_HISTORY view](account-usage/stage_storage_usage_history.md) | USAGE_VIEWER |
| [STAGES view](account-usage/stages.md) | OBJECT_VIEWER |
| [STORAGE_LIFECYCLE_POLICIES view](account-usage/storage_lifecycle_policies.md) | GOVERNANCE_VIEWER |
| [STORAGE_LIFECYCLE_POLICY_HISTORY view](account-usage/storage_lifecycle_policy_history.md) | GOVERNANCE_VIEWER |
| [STORAGE_USAGE view](account-usage/storage_usage.md) | USAGE_VIEWER |
| [TABLE_CONSTRAINTS view](account-usage/table_constraints.md) | OBJECT_VIEWER |
| [TABLE_DML_HISTORY view](account-usage/table_dml_history.md) | USAGE_VIEWER |
| [TABLE_PRUNING_HISTORY view](account-usage/table_pruning_history.md) | USAGE_VIEWER |
| [TABLE_QUERY_PRUNING_HISTORY view](account-usage/table_query_pruning_history.md) | USAGE_VIEWER |
| [TABLE_STORAGE_METRICS view](account-usage/table_storage_metrics.md) | USAGE_VIEWER |
| [TABLES view](account-usage/tables.md) | OBJECT_VIEWER |
| [TAG_REFERENCES view](account-usage/tag_references.md) | GOVERNANCE_VIEWER |
| [TAGS view](account-usage/tags.md) | OBJECT_VIEWER or GOVERNANCE_VIEWER |
| [TASK_HISTORY view](account-usage/task_history.md) | USAGE_VIEWER |
| [TRUST_CENTER_FINDINGS view](account-usage/trust_center_findings.md) | SECURITY_VIEWER |
| [USERS view](account-usage/users.md) | SECURITY_VIEWER |
| [VIEWS view](account-usage/views.md) | OBJECT_VIEWER |
| [WAREHOUSE_EVENTS_HISTORY view](account-usage/warehouse_events_history.md) | USAGE_VIEWER |
| [WAREHOUSE_LOAD_HISTORY view](account-usage/warehouse_load_history.md) | USAGE_VIEWER |
| [WAREHOUSE_METERING_HISTORY view](account-usage/warehouse_metering_history.md) | USAGE_VIEWER |

### READER_ACCOUNT_USAGE schema SNOWFLAKE database roles

The READER_USAGE_VIEWER SNOWFLAKE database role is granted SELECT privilege on all READER_ACCOUNT_USAGE views.
As reader accounts are created by clients, the READER_USAGE_VIEWER role is expected to be granted to those roles used to monitor reader account use.

| View |
| --- |
| [LOGIN_HISTORY view](account-usage/login_history.md) |
| [QUERY_HISTORY view](account-usage/query_history.md) |
| [RESOURCE_MONITORS view](account-usage/resource_monitors.md) |
| [STORAGE_USAGE view](account-usage/storage_usage.md) |
| [WAREHOUSE_METERING_HISTORY view](account-usage/warehouse_metering_history.md) |

## Querying the Account Usage views

This section includes considerations when querying the Account Usage views along with query examples.

### Selecting columns

The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.

### Reconciling cost views

There are several Account Usage views that contain data related to the cost of compute resources, storage, and data transfers. If you are trying to reconcile these views against a corresponding view in the [ORGANIZATION_USAGE schema](organization-usage.md), you must first set the timezone of the session to UTC.

For example, if you are trying to reconcile ACCOUNT_USAGE.WAREHOUSE_METERING_HISTORY to the account’s data in ORGANIZATION_USAGE.WAREHOUSE_METERING_HISTORY, you must run the following command before querying the Account Usage view:

```sqlexample
ALTER SESSION SET TIMEZONE = UTC;
```

### Examples

The following examples show some typical/useful queries using the views in the ACCOUNT_USAGE
schema.

> **Note:**
>
> * These examples assume the SNOWFLAKE database and the ACCOUNT_USAGE schema are in use for the current session. The examples also
>   assume the ACCOUNTADMIN role (or a role granted IMPORTED PRIVILEGES on the database) is in use. If they are not in use, execute
>   the following commands before running the queries in the examples:
>
>   ```sqlexample
>   USE ROLE ACCOUNTADMIN;
>
>   USE SCHEMA snowflake.account_usage;
>   ```

#### Examples: User login metrics

Average number of seconds between failed login attempts by user (month-to-date):

> ```sqlexample
> select user_name,
>        count(*) as failed_logins,
>        avg(seconds_between_login_attempts) as average_seconds_between_login_attempts
> from (
>       select user_name,
>              timediff(seconds, event_timestamp, lead(event_timestamp)
>                  over(partition by user_name order by event_timestamp)) as seconds_between_login_attempts
>       from login_history
>       where event_timestamp > date_trunc(month, current_date)
>       and is_success = 'NO'
>      )
> group by 1
> order by 3;
> ```

Failed logins by user (month-to-date):

> ```sqlexample
> select user_name,
>        sum(iff(is_success = 'NO', 1, 0)) as failed_logins,
>        count(*) as logins,
>        sum(iff(is_success = 'NO', 1, 0)) / nullif(count(*), 0) as login_failure_rate
> from login_history
> where event_timestamp > date_trunc(month, current_date)
> group by 1
> order by 4 desc;
> ```

Failed logins by user and connecting client (month-to-date):

> ```sqlexample
> select reported_client_type,
>        user_name,
>        sum(iff(is_success = 'NO', 1, 0)) as failed_logins,
>        count(*) as logins,
>        sum(iff(is_success = 'NO', 1, 0)) / nullif(count(*), 0) as login_failure_rate
> from login_history
> where event_timestamp > date_trunc(month, current_date)
> group by 1,2
> order by 5 desc;
> ```

#### Examples: Warehouse performance

This query calculates virtual warehouse performance metrics such as throughput and latency for 15-minute time intervals over the course of
one day.

In the code sample below, you can replace `CURRENT_WAREHOUSE()` with the name of a warehouse to calculate metrics for that warehouse. In
addition, change the `time_from` and `time_to` dates in the WITH clause to specify the time period.

> ```sqlexample
> WITH
> params AS (
> SELECT
>     CURRENT_WAREHOUSE() AS warehouse_name,
>     '2021-11-01' AS time_from,
>     '2021-11-02' AS time_to
> ),
>
> jobs AS (
> SELECT
>     query_id,
>     time_slice(start_time::timestamp_ntz, 15, 'minute','start') as interval_start,
>     qh.warehouse_name,
>     database_name,
>     query_type,
>     total_elapsed_time,
>     compilation_time AS compilation_and_scheduling_time,
>     (queued_provisioning_time + queued_repair_time + queued_overload_time) AS queued_time,
>     transaction_blocked_time,
>     execution_time
> FROM snowflake.account_usage.query_history qh, params
> WHERE
>     qh.warehouse_name = params.warehouse_name
> AND start_time >= params.time_from
> AND start_time <= params.time_to
> AND execution_status = 'SUCCESS'
> AND query_type IN ('SELECT','UPDATE','INSERT','MERGE','DELETE')
> ),
>
> interval_stats AS (
> SELECT
>     query_type,
>     interval_start,
>     COUNT(DISTINCT query_id) AS numjobs,
>     MEDIAN(total_elapsed_time)/1000 AS p50_total_duration,
>     (percentile_cont(0.95) within group (order by total_elapsed_time))/1000 AS p95_total_duration,
>     SUM(total_elapsed_time)/1000 AS sum_total_duration,
>     SUM(compilation_and_scheduling_time)/1000 AS sum_compilation_and_scheduling_time,
>     SUM(queued_time)/1000 AS sum_queued_time,
>     SUM(transaction_blocked_time)/1000 AS sum_transaction_blocked_time,
>     SUM(execution_time)/1000 AS sum_execution_time,
>     ROUND(sum_compilation_and_scheduling_time/sum_total_duration,2) AS compilation_and_scheduling_ratio,
>     ROUND(sum_queued_time/sum_total_duration,2) AS queued_ratio,
>     ROUND(sum_transaction_blocked_time/sum_total_duration,2) AS blocked_ratio,
>     ROUND(sum_execution_time/sum_total_duration,2) AS execution_ratio,
>     ROUND(sum_total_duration/numjobs,2) AS total_duration_perjob,
>     ROUND(sum_compilation_and_scheduling_time/numjobs,2) AS compilation_and_scheduling_perjob,
>     ROUND(sum_queued_time/numjobs,2) AS queued_perjob,
>     ROUND(sum_transaction_blocked_time/numjobs,2) AS blocked_perjob,
>     ROUND(sum_execution_time/numjobs,2) AS execution_perjob
> FROM jobs
> GROUP BY 1,2
> ORDER BY 1,2
> )
> SELECT * FROM interval_stats;
> ```
>
> > **Note:**
> >
> > Analyze different statement types separately (e.g., SELECT statements independent of INSERT or DELETE or other statements).

* The NUMJOBS value represents the throughput for that time interval.
* The P50_TOTAL_DURATION (median) and P95_TOTAL_DURATION (peak) values represent latency.
* The SUM_TOTAL_DURATION is the sum of the SUM_<job_stage>_TIME values for the different job stages (COMPILATION_AND_SCHEDULING, QUEUED,
  BLOCKED, EXECUTION).
* Analyze the <job_stage>_RATIO values when the load (NUMJOBS) increases. Look for ratio changes or deviations from the average.
* If the QUEUED_RATIO is high, there might not be sufficient capacity in the warehouse. Add more clusters or increase the warehouse size.

#### Examples: Warehouse credit usage

Credits used by each warehouse in your account (month-to-date):

> ```sqlexample
> select warehouse_name,
>        sum(credits_used) as total_credits_used
> from warehouse_metering_history
> where start_time >= date_trunc(month, current_date)
> group by 1
> order by 2 desc;
> ```

Credits used over time by each warehouse in your account (month-to-date):

> ```sqlexample
> select start_time::date as usage_date,
>        warehouse_name,
>        sum(credits_used) as total_credits_used
> from warehouse_metering_history
> where start_time >= date_trunc(month, current_date)
> group by 1,2
> order by 2,1;
> ```

#### Examples: Data storage usage

Billable terabytes stored in your account over time:

> ```sqlexample
> select date_trunc(month, usage_date) as usage_month
>   , avg(storage_bytes + stage_bytes + failsafe_bytes) / power(1024, 4) as billable_tb
> from storage_usage
> group by 1
> order by 1;
> ```

#### Examples: User query totals and execution times

Total jobs executed in your account (month-to-date):

> ```sqlexample
> select count(*) as number_of_jobs
> from query_history
> where start_time >= date_trunc(month, current_date);
> ```

Total jobs executed by each warehouse in your account (month-to-date):

> ```sqlexample
> select warehouse_name,
>        count(*) as number_of_jobs
> from query_history
> where start_time >= date_trunc(month, current_date)
> group by 1
> order by 2 desc;
> ```

Average query execution time by user (month-to-date):

> ```sqlexample
> select user_name,
>        avg(execution_time) as average_execution_time
> from query_history
> where start_time >= date_trunc(month, current_date)
> group by 1
> order by 2 desc;
> ```

Average query execution time by query type and warehouse size (month-to-date):

> ```sqlexample
> select query_type,
>        warehouse_size,
>        avg(execution_time) as average_execution_time
> from query_history
> where start_time >= date_trunc(month, current_date)
> group by 1,2
> order by 3 desc;
> ```

#### Examples: Obtain a query count for every login event

Join columns from LOGIN_HISTORY, QUERY_HISTORY, and SESSIONS to obtain a query count for each user login event.

> > **Note:**
> >
> > The SESSIONS view records information starting on July 20-21, 2020, therefore the query result will only contain overlapping
> > information for each of the three views starting from this date.
>
> ```sqlexample
> select l.user_name,
>        l.event_timestamp as login_time,
>        l.client_ip,
>        l.reported_client_type,
>        l.first_authentication_factor,
>        l.second_authentication_factor,
>        count(q.query_id)
> from snowflake.account_usage.login_history l
> join snowflake.account_usage.sessions s on l.event_id = s.login_event_id
> join snowflake.account_usage.query_history q on q.session_id = s.session_id
> group by 1,2,3,4,5,6
> order by l.user_name
> ;
> ```
