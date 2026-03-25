# Source: https://docs.snowflake.com/en/sql-reference/snowflake-db-roles.md

# SNOWFLAKE database roles

When an account is provisioned, the SNOWFLAKE database is automatically imported.
The database is an example of Snowflake using [Secure Data Sharing](../user-guide/data-sharing-gs.md) to provide object metadata and other usage metrics for your organization and accounts.

Access to schema objects in the SNOWFLAKE database is controlled by different [database roles](../user-guide/security-access-control-considerations.md).
The following sections describe each SNOWFLAKE database role, its associated privileges, and the associated schema objects the role is granted access to.

## ACCOUNT_USAGE schema

[ACCOUNT_USAGE](account-usage.md) schemas have four defined SNOWFLAKE database roles, each granted the SELECT privilege on specific views.

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

## READER_ACCOUNT_USAGE schema

The READER_USAGE_VIEWER SNOWFLAKE database role is granted SELECT privilege on all READER_ACCOUNT_USAGE views.
As reader accounts are created by clients, the READER_USAGE_VIEWER role is expected to be granted to those roles used to monitor reader account use.

| View |
| --- |
| [LOGIN_HISTORY view](account-usage/login_history.md) |
| [QUERY_HISTORY view](account-usage/query_history.md) |
| [RESOURCE_MONITORS view](account-usage/resource_monitors.md) |
| [STORAGE_USAGE view](account-usage/storage_usage.md) |
| [WAREHOUSE_METERING_HISTORY view](account-usage/warehouse_metering_history.md) |

## ORGANIZATION_USAGE schema

The ORGANIZATION_USAGE_VIEWER, ORGANIZATION_BILLING_VIEWER, and ORGANIZATION_ACCOUNTS_VIEWER SNOWFLAKE database roles are granted the SELECT privilege on Organization Usage views in the shared SNOWFLAKE database.

| View | ORGANIZATION_BILLING_VIEWER Role | ORGANIZATION_USAGE_VIEWER Role | ORGANIZATION_ACCOUNTS_VIEWER Role |
| --- | --- | --- | --- |
| [ACCOUNTS view](organization-usage/accounts.md) |  |  | ✔ |
| [ANOMALIES_IN_CURRENCY_DAILY view](organization-usage/anomalies_in_currency_daily.md) | ✔ |  |  |
| [CONTRACT_ITEMS view](organization-usage/contract_items.md) | ✔ |  |  |
| [LISTING_AUTO_FULFILLMENT_USAGE_HISTORY view](organization-usage/listing_auto_fulfillment_usage_history.md) | ✔ |  |  |
| [RATE_SHEET_DAILY view](organization-usage/rate_sheet_daily.md) | ✔ |  |  |
| [REMAINING_BALANCE_DAILY view](organization-usage/remaining_balance_daily.md) | ✔ |  |  |
| [USAGE_IN_CURRENCY_DAILY view](organization-usage/usage_in_currency_daily.md) | ✔ |  |  |
| [MARKETPLACE_DISBURSEMENT_REPORT View](../collaboration/views/marketplace-disbursement-report-org.md) | ✔ |  |  |
| [DATA_TRANSFER_DAILY_HISTORY view](organization-usage/data_transfer_daily_history.md) |  | ✔ |  |
| [DATA_TRANSFER_HISTORY view](organization-usage/data_transfer_history.md) |  | ✔ |  |
| [DATABASE_STORAGE_USAGE_HISTORY view](organization-usage/database_storage_usage_history.md) |  | ✔ |  |
| [AUTOMATIC_CLUSTERING_HISTORY view](organization-usage/automatic_clustering_history.md) |  | ✔ |  |
| [MARKETPLACE_PAID_USAGE_DAILY View](../collaboration/views/marketplace-paid-usage-daily-org.md) |  | ✔ |  |
| [MATERIALIZED_VIEW_REFRESH_HISTORY view](account-usage/materialized_view_refresh_history.md) |  | ✔ |  |
| [METERING_DAILY_HISTORY view](organization-usage/metering_daily_history.md) |  | ✔ |  |
| [MONETIZED_USAGE_DAILY View](../collaboration/views/monetized-usage-daily-org.md) |  | ✔ |  |
| [PIPE_USAGE_HISTORY view](organization-usage/pipe_usage_history.md) |  | ✔ |  |
| [QUERY_ACCELERATION_HISTORY view](organization-usage/query_acceleration_history.md) |  | ✔ |  |
| [REPLICATION_GROUP_USAGE_HISTORY view](organization-usage/replication_group_usage_history.md) |  | ✔ |  |
| [REPLICATION_USAGE_HISTORY view](organization-usage/replication_usage_history.md) |  | ✔ |  |
| [SEARCH_OPTIMIZATION_HISTORY view](organization-usage/search_optimization_history.md) |  | ✔ |  |
| [STAGE_STORAGE_USAGE_HISTORY view](organization-usage/stage_storage_usage_history.md) |  | ✔ |  |
| [STORAGE_DAILY_HISTORY view](organization-usage/storage_daily_history.md) |  | ✔ |  |
| [WAREHOUSE_METERING_HISTORY view](organization-usage/warehouse_metering_history.md) |  | ✔ |  |

## CORE schema

The CORE_VIEWER SNOWFLAKE database role is granted to the PUBLIC role in all Snowflake accounts containing a shared SNOWFLAKE database.
The USAGE privilege is granted to all Snowflake-defined functions and bundles in the CORE schema.

### Budget class

The BUDGET_CREATOR Snowflake database role is granted the USAGE privilege on the SNOWFLAKE.CORE schema and the BUDGET class
in the schema. This grant allows users with the BUDGET_CREATOR role to create instances of the BUDGET class.

For more information, see [Create a custom role to create budgets](../user-guide/budgets/custom-budget.md).

### Tag objects

The CORE_VIEWER database role is granted the APPLY privilege on the
[classification system tags](../user-guide/classify-intro.md) SNOWFLAKE.CORE.PRIVACY_CATEGORY and
SNOWFLAKE.CORE.SEMANTIC_CATEGORY. These grants allow users with a role that is granted the CORE_VIEWER database role to assign these system
tags to columns.

## ALERT schema

The ALERT_VIEWER SNOWFLAKE database role is granted the USAGE privilege on the functions defined in this schema.

## ML schema

The ML_USER SNOWFLAKE database role is granted to the PUBLIC role in all Snowflake accounts that contain a shared
SNOWFLAKE database and allows customers to access and use [ML functions](../guides-overview-ml-functions.md).
Users must also have the USAGE privilege on the ML schema to call these functions.

## MONITORING schema

The MONITORING_VIEWER database role has the SELECT privilege on all views in the MONITORING schema.

The MONITORING_VIEWER database role is granted to the PUBLIC role in all Snowflake accounts containing a shared SNOWFLAKE
database.

## SNOWFLAKE.CLASSIFICATION_ADMIN database role

The SNOWFLAKE.CLASSIFICATION_ADMIN database role allows a data engineer or steward to create an instance of the [CLASSIFICATION_PROFILE](classes/classification_profile.md) class.
A classification profile is used to implement [sensitive data classification](../user-guide/classify-auto.md).

## SNOWFLAKE.CORTEX_AGENT_USER database role

You can use the SNOWFLAKE.CORTEX_AGENT_USER database role to grant your users access to Snowflake Cortex Agents API without granting access to other Cortex
features. Using the Cortex Agents API requires *either* the SNOWFLAKE.CORTEX_USER database role *or* the
SNOWFLAKE.CORTEX_AGENT_USER database role.

By default, the SNOWFLAKE.CORTEX_USER database role is granted to the PUBLIC role. For fine-grained access control, revoke access from the PUBLIC role and grant access to the SNOWFLAKE.CORTEX_AGENT_USER database role.
For more information, see [Set up access to the agent](../user-guide/snowflake-cortex/cortex-agents-manage.md).

## SNOWFLAKE.CORTEX_EMBED_USER database role

The SNOWFLAKE.CORTEX_EMBED_USER database role is used to grant customers access to Snowflake Cortex embedding functions AI_EMBED,
SNOWFLAKE.CORTEX.EMBED_768, and SNOWFLAKE.CORTEX_EMBED_TEXT_1024 without granting access to other Cortex
features. Calling these embedding functions requires *either* the SNOWFLAKE.CORTEX_USER database role *or* the
SNOWFLAKE.CORTEX_EMBED_USER database role. This role is not granted to any roles by default.

By default, this role is not granted to any roles. If you want users to have access to the embedding functions,
grant this database role to appropriate roles. For details, see [Cortex LLM Functions required privileges](../user-guide/snowflake-cortex/aisql.md)

## SNOWFLAKE.CORTEX_USER database role

This SNOWFLAKE.CORTEX_USER database role is used to grant customers access to Snowflake Cortex features.
By default, this role is granted to the PUBLIC role. The PUBLIC role is automatically granted
to all users and roles, so this allows all users in your account to use Snowflake Cortex LLM functions.

If you don’t want all users to have this privilege, you can revoke access from the PUBLIC role and grant access to specific roles.
For details, see [Cortex LLM Functions required privileges](../user-guide/snowflake-cortex/aisql.md).

## SNOWFLAKE.COPILOT_USER database role

The SNOWFLAKE.COPILOT_USER database role allows customers to access Snowflake Copilot features. Initially, this database role
is granted to the PUBLIC role. The PUBLIC role is automatically granted to all users and roles, so this allows all users in your account
to use Snowflake Copilot. If you want to limit access to Snowflake Copilot features, you can revoke access from the PUBLIC role and grant access to
specific roles. For details, see [Access control requirements](../user-guide/snowflake-copilot.md).

## Using SNOWFLAKE database roles

Administrators can use the [GRANT DATABASE ROLE](sql/grant-database-role.md) to assign a SNOWFLAKE database role to another role,
which can then be granted to a user. This would allow the user to access a specific subset of views in the SNOWFLAKE database.

In the following example a role is created which can be used to view SNOWFLAKE database object metadata, and does the following:

1. Creates a custom role.
2. Grants the OBJECT_VIEWER role to the custom role.
3. Grants the custom role to a user.

To create and grant the custom role, do the following:

1. Create the `CAN_VIEWMD` role, using [CREATE ROLE](sql/create-role.md) that will be used to grant access to object metadata.

   Only users with the USERADMIN system role or higher, or another role with the CREATE ROLE privilege on the
   account, can create roles.

   ```sqlexample
   CREATE ROLE CAN_VIEWMD COMMENT = 'This role can view metadata per SNOWFLAKE database role definitions';
   ```

2. Grant the OBJECT_VIEWER role to the CAN_VIEWMD role.

   Only users with the OWNERSHIP role can grant SNOWFLAKE database roles. For additional information, refer to [GRANT DATABASE ROLE](sql/grant-database-role.md).

   ```sqlexample
   GRANT DATABASE ROLE OBJECT_VIEWER TO ROLE CAN_VIEWMD;
   ```

3. Assign `CAN_VIEWMD` role to user `smith`.

   Only users with the SECURITYADMIN role can grant roles to users. For additional options, refer to [GRANT ROLE](sql/grant-role.md).

   ```sqlexample
   GRANT ROLE CAN_VIEWMD TO USER smith;
   ```
