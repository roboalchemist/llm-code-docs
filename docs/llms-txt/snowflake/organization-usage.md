# Source: https://docs.snowflake.com/en/sql-reference/organization-usage.md

# Organization Usage

Snowflake provides historical usage data for all accounts in your organization via the ORGANIZATION_USAGE schema in a shared database named
SNOWFLAKE.

## ORGANIZATION_USAGE views

The ORGANIZATION_USAGE schema contains the following views:

| View | Type | Latency [1] | Notes |
| --- | --- | --- | --- |
| [ACCESS_HISTORY](organization-usage/access_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [ACCOUNTS](organization-usage/accounts.md) | Object | 24 hours |  |
| [ALERT_HISTORY](organization-usage/alert_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [ANOMALIES_IN_CURRENCY_DAILY](organization-usage/anomalies_in_currency_daily.md) | Historical | 24 hours |  |
| [AUTOMATIC_CLUSTERING_HISTORY](organization-usage/automatic_clustering_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [BACKUP_OPERATION_HISTORY](organization-usage/backup_operation_history.md) | Historical | 6 hours | Data retained for 1 year. |
| [BACKUP_POLICIES](organization-usage/backup_policies.md) | Object | 6 hours |  |
| [BACKUP_SETS](organization-usage/backup_sets.md) | Object | 6 hours |  |
| [BACKUPS](organization-usage/backups.md) | Object | 6 hours |  |
| [CLASSES](organization-usage/classes.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [CLASS_INSTANCES](organization-usage/class_instances.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [COLUMNS](organization-usage/columns.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [COMPLETE_TASK_GRAPHS](organization-usage/complete_task_graphs.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [CONTRACT_ITEMS](organization-usage/contract_items.md) [2] | Historical | 24 hours |  |
| [COPY_HISTORY](organization-usage/copy_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [DATA_TRANSFER_DAILY_HISTORY](organization-usage/data_transfer_daily_history.md) | Historical | 2 hours | Data retained for 1 year. |
| [DATA_TRANSFER_HISTORY](organization-usage/data_transfer_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [DATABASE_STORAGE_USAGE_HISTORY](organization-usage/database_storage_usage_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [DATABASES](organization-usage/databases.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [FEATURE_POLICIES](organization-usage/feature_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [FILE_FORMATS](organization-usage/file_formats.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [FUNCTIONS](organization-usage/functions.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [GRANTS_TO_ROLES](organization-usage/grants_to_roles.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [GRANTS_TO_USERS](organization-usage/grants_to_users.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [LISTING_AUTO_FULFILLMENT_USAGE_HISTORY](organization-usage/listing_auto_fulfillment_usage_history.md) | Historical | 72 hours | Data retained for 1 year. |
| [LOAD_HISTORY](organization-usage/load_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [LOCK_WAIT_HISTORY](organization-usage/lock_wait_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [LOGIN_HISTORY](organization-usage/login_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [MARKETPLACE_DISBURSEMENT_REPORT](../collaboration/views/marketplace-disbursement-report-org.md) | Historical | 24 hours | Data retained for 1 year. |
| [MARKETPLACE_PAID_USAGE_DAILY](../collaboration/views/marketplace-paid-usage-daily-org.md) | Historical | 24 hours | Data retained for 1 year. |
| [MASKING_POLICIES](organization-usage/masking_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [MATERIALIZED_VIEW_REFRESH_HISTORY](organization-usage/materialized_view_refresh_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [METERING_DAILY_HISTORY](organization-usage/metering_daily_history.md) | Historical | 2 hours | Data retained for 1 year. |
| [METERING_HISTORY](organization-usage/metering_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [MONETIZED_USAGE_DAILY](../collaboration/views/monetized-usage-daily-org.md) | Historical | 24 hours | Data retained for 1 year. |
| [OBJECT_DEPENDENCIES](organization-usage/object_dependencies.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [PASSWORD_POLICIES](organization-usage/password_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [PIPE_USAGE_HISTORY](organization-usage/pipe_usage_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [PIPES](organization-usage/pipes.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [POLICY_REFERENCES](organization-usage/policy_references.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [PROCEDURES](organization-usage/procedures.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [QUERY_ACCELERATION_ELIGIBLE](organization-usage/query_acceleration_eligible.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [QUERY_ACCELERATION_HISTORY](organization-usage/query_acceleration_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [QUERY_ATTRIBUTION_HISTORY](organization-usage/query_attribution_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [QUERY_HISTORY](organization-usage/query_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [RATE_SHEET_DAILY](organization-usage/rate_sheet_daily.md) [2] | Historical | 24 hours |  |
| [REFERENTIAL_CONSTRAINTS](organization-usage/referential_constraints.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [REMAINING_BALANCE_DAILY](organization-usage/remaining_balance_daily.md) [2] | Historical | 72 hours |  |
| [REPLICATION_GROUP_REFRESH_HISTORY](organization-usage/replication_group_refresh_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [REPLICATION_GROUP_USAGE_HISTORY](organization-usage/replication_group_usage_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [REPLICATION_USAGE_HISTORY](organization-usage/replication_usage_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [RESOURCE_MONITORS](organization-usage/resource_monitors.md) |  | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [ROLES](organization-usage/roles.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [ROW_ACCESS_POLICIES](organization-usage/row_access_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [SCHEMATA](organization-usage/schemata.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [SEARCH_OPTIMIZATION_HISTORY](organization-usage/search_optimization_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [SEQUENCES](organization-usage/sequences.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [SESSION_POLICIES](organization-usage/session_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [SESSIONS](organization-usage/sessions.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [SNAPSHOT_OPERATION_HISTORY](organization-usage/snapshot_operation_history.md) | Historical | 6 hours | Data retained for 1 year. This view is deprecated. Use the [BACKUP_OPERATION_HISTORY](account-usage/backup_operation_history.md) view instead. |
| [SNAPSHOT_POLICIES](organization-usage/snapshot_policies.md) | Object | 6 hours | This view is deprecated. Use the [BACKUP_POLICIES](account-usage/backup_policies.md) view instead. |
| [SNAPSHOT_SETS](organization-usage/snapshot_sets.md) | Object | 6 hours | This view is deprecated. Use the [BACKUP_SETS](account-usage/backup_sets.md) view instead. |
| [SNAPSHOTS](organization-usage/snapshots.md) | Object | 6 hours | This view is deprecated. Use the [BACKUPS](account-usage/backups.md) view instead. |
| [STAGES](organization-usage/stages.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [STAGE_STORAGE_USAGE_HISTORY](organization-usage/stage_storage_usage_history.md) | Historical | 24 hours | Data retained for 1 year. |
| [STORAGE_DAILY_HISTORY](organization-usage/storage_daily_history.md) | Historical | 2 hours | Data retained for 1 year. |
| [STORAGE_LIFECYCLE_POLICIES](organization-usage/storage_lifecycle_policies.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [STORAGE_LIFECYCLE_POLICY_HISTORY](organization-usage/storage_lifecycle_policy_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). Data retained for 1 year. |
| [TABLE_CONSTRAINTS](organization-usage/table_constraints.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TABLE_STORAGE_METRICS](organization-usage/table_storage_metrics.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TABLES](organization-usage/tables.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TAG_REFERENCES](organization-usage/tag_references.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TAGS](organization-usage/tags.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TASK_HISTORY](organization-usage/task_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TASK_VERSIONS](organization-usage/task_versions.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [TRUST_CENTER_FINDINGS](organization-usage/trust_center_findings.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [USAGE_IN_CURRENCY_DAILY](organization-usage/usage_in_currency_daily.md) [2] | Historical | 72 hours |  |
| [USERS](organization-usage/users.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [VIEWS](organization-usage/views.md) | Object | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [WAREHOUSE_EVENTS_HISTORY](organization-usage/warehouse_events_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [WAREHOUSE_LOAD_HISTORY](organization-usage/warehouse_load_history.md) | Historical | 24 hours | [Premium view](../user-guide/organization-accounts-premium-views.md) (only available in organization account). |
| [WAREHOUSE_METERING_HISTORY](organization-usage/warehouse_metering_history.md) | Historical | 24 hours | Data retained for 1 year. |

[1] All latency times are approximate; in some instances, the actual latency may be lower.

[2] The organization billing views do not display the actual, final amount because some adjustments are made at the end of the month. Customers who signed a contract through a Snowflake reseller cannot access data in these views.

## Accessing the ORGANIZATION_USAGE schema

The ORGANIZATION_USAGE schema is available in the [organization account](../user-guide/organization-accounts.md) and a regular account that has the ORGADMIN role enabled. How you access the views in the schema differs depending on which type of account you are using. For details about accessing views, see the following:

* Access schema in the organization account
* Access schema in an ORGADMIN-enabled account

> **Note:**
>
> The views in the ORGANIZATION_USAGE schema are currently not available in
> [US SnowGov Regions](../user-guide/intro-regions.md) on AWS GovCloud and Microsoft Azure Government.

### Access schema in the organization account

By default, only users granted the GLOBALORGADMIN role can access ORGANIZATION_USAGE views in the [organization account](../user-guide/organization-accounts.md).

To grant access to other users, the organization administrator can grant the appropriate *application role* to an account role or user.

Users who have been granted the SNOWFLAKE.ORG_USAGE_ADMIN application role can access all views in the ORGANIZATION_USAGE schema of the
organization account. The following example lets user `joe` access all views in the schema:

```sqlexample
USE ROLE GLOBALORGADMIN;

GRANT APPLICATION ROLE SNOWFLAKE.ORG_USAGE_ADMIN TO ROLE custom_role;

GRANT ROLE custom_role TO USER joe;
```

The organization administrator can also grant access on a more granular level. For example, the ORGANIZATION_OBJECT_VIEWER application role
grants access to the DATABASES view but does not grant access to the TASK_HISTORY view.

Use the following list to determine which application role grants access to a specific view. These application roles are in the SNOWFLAKE
application. Use the fully qualified name of the application role when granting it to another role (for example,
SNOWFLAKE.ORGANIZATION_USAGE_VIEWER).

| View | Required application role |
| --- | --- |
| [ACCESS_HISTORY view](organization-usage/access_history.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [ACCOUNTS view](organization-usage/accounts.md) | ORGANIZATION_ACCOUNTS_VIEWER |
| [ALERT_HISTORY view](organization-usage/alert_history.md) | ORGANIZATION_USAGE_VIEWER |
| [AUTOMATIC_CLUSTERING_HISTORY view](organization-usage/automatic_clustering_history.md) | ORGANIZATION_USAGE_VIEWER |
| [CLASSES view](organization-usage/classes.md) | ORGANIZATION_USAGE_VIEWER |
| [CLASS_INSTANCES view](organization-usage/class_instances.md) | ORGANIZATION_USAGE_VIEWER |
| [COLUMNS view](organization-usage/columns.md) | ORGANIZATION_OBJECT_VIEWER |
| [COMPLETE_TASK_GRAPHS view](organization-usage/complete_task_graphs.md) | ORGANIZATION_OBJECT_VIEWER |
| [CONTRACT_ITEMS view](organization-usage/contract_items.md) | ORGANIZATION_BILLING_VIEWER |
| [COPY_HISTORY view](organization-usage/copy_history.md) | ORGANIZATION_USAGE_VIEWER |
| [DATABASE_STORAGE_USAGE_HISTORY view](organization-usage/database_storage_usage_history.md) | ORGANIZATION_USAGE_VIEWER |
| [DATABASES view](organization-usage/databases.md) | ORGANIZATION_OBJECT_VIEWER |
| [DATA_TRANSFER_DAILY_HISTORY view](organization-usage/data_transfer_daily_history.md) | ORGANIZATION_USAGE_VIEWER |
| [DATA_TRANSFER_HISTORY view](organization-usage/data_transfer_history.md) | ORGANIZATION_USAGE_VIEWER |
| [FILE_FORMATS view](organization-usage/file_formats.md) | ORGANIZATION_OBJECT_VIEWER |
| [FUNCTIONS view](organization-usage/functions.md) | ORGANIZATION_OBJECT_VIEWER |
| [GRANTS_TO_ROLES view](organization-usage/grants_to_roles.md) | ORGANIZATION_SECURITY_VIEWER |
| [GRANTS_TO_USERS view](organization-usage/grants_to_users.md) | ORGANIZATION_SECURITY_VIEWER |
| [LISTING_AUTO_FULFILLMENT_USAGE_HISTORY view](organization-usage/listing_auto_fulfillment_usage_history.md) | ORGANIZATION_BILLING_VIEWER |
| [LOAD_HISTORY view](organization-usage/load_history.md) | ORGANIZATION_USAGE_VIEWER |
| [LOCK_WAIT_HISTORY view](organization-usage/lock_wait_history.md) | ORGANIZATION_USAGE_VIEWER |
| [LOGIN_HISTORY view](organization-usage/login_history.md) | ORGANIZATION_SECURITY_VIEWER |
| [MARKETPLACE_DISBURSEMENT_REPORT View](../collaboration/views/marketplace-disbursement-report-org.md) | ORGANIZATION_BILLING_VIEWER |
| [MARKETPLACE_PAID_USAGE_DAILY View](../collaboration/views/marketplace-paid-usage-daily-org.md) | ORGANIZATION_USAGE_VIEWER |
| MARKETPLACE_PURCHASE_EVENTS view | ORGANIZATION_BILLING_VIEWER |
| [MASKING_POLICIES view](organization-usage/masking_policies.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [MATERIALIZED_VIEW_REFRESH_HISTORY view](organization-usage/materialized_view_refresh_history.md) | ORGANIZATION_USAGE_VIEWER |
| [METERING_DAILY_HISTORY view](organization-usage/metering_daily_history.md) | ORGANIZATION_USAGE_VIEWER |
| [METERING_HISTORY view](organization-usage/metering_history.md) | ORGANIZATION_USAGE_VIEWER |
| [MONETIZED_USAGE_DAILY](../collaboration/views/monetized-usage-daily-org.md) | ORGANIZATION_USAGE_VIEWER |
| [OBJECT_DEPENDENCIES view](organization-usage/object_dependencies.md) | ORGANIZATION_OBJECT_VIEWER |
| [PASSWORD_POLICIES view](organization-usage/password_policies.md) | ORGANIZATION_SECURITY_VIEWER |
| [PIPE_USAGE_HISTORY view](organization-usage/pipe_usage_history.md) | ORGANIZATION_USAGE_VIEWER |
| [PIPES view](organization-usage/pipes.md) | ORGANIZATION_OBJECT_VIEWER |
| [POLICY_REFERENCES view](organization-usage/policy_references.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [PROCEDURES view](organization-usage/procedures.md) | ORGANIZATION_OBJECT_VIEWER |
| [QUERY_ACCELERATION_ELIGIBLE view](organization-usage/query_acceleration_eligible.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [QUERY_ACCELERATION_HISTORY view](organization-usage/query_acceleration_history.md) | *ORGANIZATION_GOVERNANCE_VIEWER* ORGANIZATION_USAGE_VIEWER |
| [QUERY_ATTRIBUTION_HISTORY view](organization-usage/query_attribution_history.md) | *ORGANIZATION_GOVERNANCE_VIEWER* ORGANIZATION_USAGE_VIEWER |
| [QUERY_HISTORY view](organization-usage/query_history.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [RATE_SHEET_DAILY view](organization-usage/rate_sheet_daily.md) | ORGANIZATION_BILLING_VIEWER |
| [REFERENTIAL_CONSTRAINTS view](organization-usage/referential_constraints.md) | ORGANIZATION_OBJECT_VIEWER |
| [REMAINING_BALANCE_DAILY view](organization-usage/remaining_balance_daily.md) | ORGANIZATION_BILLING_VIEWER |
| [REPLICATION_GROUP_REFRESH_HISTORY view](organization-usage/replication_group_refresh_history.md) | ORGANIZATION_USAGE_VIEWER |
| [REPLICATION_GROUP_USAGE_HISTORY view](organization-usage/replication_group_usage_history.md) | ORGANIZATION_USAGE_VIEWER |
| [REPLICATION_USAGE_HISTORY view](organization-usage/replication_usage_history.md) | ORGANIZATION_USAGE_VIEWER |
| [RESOURCE_MONITORS view](organization-usage/resource_monitors.md) | ORGANIZATION_OBJECT_VIEWER |
| [ROLES view](organization-usage/roles.md) | ORGANIZATION_SECURITY_VIEWER |
| [ROW_ACCESS_POLICIES view](organization-usage/row_access_policies.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [SCHEMATA view](organization-usage/schemata.md) | ORGANIZATION_OBJECT_VIEWER |
| [SEARCH_OPTIMIZATION_HISTORY view](organization-usage/search_optimization_history.md) | ORGANIZATION_USAGE_VIEWER |
| [SEQUENCES view](organization-usage/sequences.md) | ORGANIZATION_OBJECT_VIEWER |
| [SESSION_POLICIES view](organization-usage/session_policies.md) | ORGANIZATION_SECURITY_VIEWER |
| [SESSIONS view](organization-usage/sessions.md) | ORGANIZATION_SECURITY_VIEWER |
| [STAGE_STORAGE_USAGE_HISTORY view](organization-usage/stage_storage_usage_history.md) | ORGANIZATION_USAGE_VIEWER |
| [STAGES view](organization-usage/stages.md) | ORGANIZATION_OBJECT_VIEWER |
| [STORAGE_LIFECYCLE_POLICIES view](organization-usage/storage_lifecycle_policies.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [STORAGE_LIFECYCLE_POLICY_HISTORY view](organization-usage/storage_lifecycle_policy_history.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [STORAGE_DAILY_HISTORY view](organization-usage/storage_daily_history.md) | ORGANIZATION_USAGE_VIEWER |
| [TABLE_CONSTRAINTS view](organization-usage/table_constraints.md) | ORGANIZATION_OBJECT_VIEWER |
| [TABLE_STORAGE_METRICS view](organization-usage/table_storage_metrics.md) | ORGANIZATION_USAGE_VIEWER |
| [TABLES view](organization-usage/tables.md) | ORGANIZATION_OBJECT_VIEWER |
| [TAG_REFERENCES view](organization-usage/tag_references.md) | ORGANIZATION_GOVERNANCE_VIEWER |
| [TAGS view](organization-usage/tags.md) | ORGANIZATION_OBJECT_VIEWER |
| [TASK_HISTORY view](organization-usage/task_history.md) | ORGANIZATION_USAGE_VIEWER |
| [TASK_VERSIONS view](organization-usage/task_versions.md) | ORGANIZATION_OBJECT_VIEWER |
| [TRUST_CENTER_FINDINGS view](organization-usage/trust_center_findings.md) | ORGANIZATION_SECURITY_VIEWER |
| [USAGE_IN_CURRENCY_DAILY view](organization-usage/usage_in_currency_daily.md) | ORGANIZATION_BILLING_VIEWER |
| [USERS view](organization-usage/users.md) | ORGANIZATION_SECURITY_VIEWER |
| [VIEWS view](organization-usage/views.md) | ORGANIZATION_OBJECT_VIEWER |
| [WAREHOUSE_EVENTS_HISTORY view](organization-usage/warehouse_events_history.md) | ORGANIZATION_USAGE_VIEWER |
| [WAREHOUSE_LOAD_HISTORY view](organization-usage/warehouse_load_history.md) | ORGANIZATION_USAGE_VIEWER |
| [WAREHOUSE_METERING_HISTORY view](organization-usage/warehouse_metering_history.md) | ORGANIZATION_USAGE_VIEWER |

### Access schema in an ORGADMIN-enabled account

An ORGADMIN-enabled account is a regular account that has the ORGADMIN role enabled. Within a ORGADMIN-enabled account, anyone who has
access to the shared SNOWFLAKE database has access to the ORGANIZATION_USAGE schema. By default, only the ACCOUNTADMIN role has privileges
to this database, which means the ORGADMIN role does not have the necessary privileges. To grant these privileges to the ORGADMIN role, see [Enabling other roles to use schemas in the SNOWFLAKE database](account-usage.md).

To grant access to non-administrators, the organization administrator can grant the appropriate *database role* to an account role or user.

Using the following list to determine which database role grants access to specific views.

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

For more information, refer to [GRANT DATABASE ROLE](sql/grant-database-role.md).

## General usage notes

The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.
