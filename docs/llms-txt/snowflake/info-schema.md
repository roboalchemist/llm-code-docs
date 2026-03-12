# Source: https://docs.snowflake.com/en/sql-reference/info-schema.md

# Snowflake Information Schema

The Snowflake Information Schema (aka “Data Dictionary”) consists of a set of system-defined views and table functions that provide
extensive metadata information about the objects created in your account. The Snowflake Information Schema is based on the SQL-92 ANSI
Information Schema, but with the addition of views and functions that are specific to Snowflake.

The Information Schema is implemented as a schema named INFORMATION_SCHEMA that Snowflake automatically creates in every database in
an account.

> **Note:**
>
> ANSI uses the term “catalog” to refer to databases. To maintain compatibility with the standard, the Snowflake Information Schema
> topics use “catalog” in place of “database” where applicable. For all intents and purposes, the terms are conceptually equivalent
> and interchangeable.

## What is INFORMATION_SCHEMA?

Each database created in your account automatically includes a built-in, read-only schema named INFORMATION_SCHEMA. The schema contains
the following objects:

* Views for all the objects contained in the database, as well as views for account-level objects (i.e. non-database objects such as
  roles, warehouses, and databases)
* Table functions for historical and usage data across your account.

## List of Information Schema views

The views in INFORMATION_SCHEMA display metadata about objects defined in the database, as well as metadata for non-database,
account-level objects that are common across all databases. Each instance of INFORMATION_SCHEMA includes:

> * ANSI-standard views for the database and account-level objects that are relevant to Snowflake.
> * Snowflake-specific views for the non-standard objects that Snowflake supports (stages, file formats, etc.).

Information Schema views that are Snowflake-specific (that is, that are **not** ANSI-standard) are marked with ✔ in
the “Snowflake-specific” column in the following table.

| View | Type | Snowflake-specific | Notes |
| --- | --- | --- | --- |
| [APPLICABLE_ROLES](info-schema/applicable_roles.md) | Account |  |  |
| [APPLICATION_CONFIGURATIONS](info-schema/application_configurations.md) | Database | ✔ |  |
| [APPLICATION_SPECIFICATIONS](info-schema/application_specifications.md) | Database | ✔ |  |
| [CLASS_INSTANCE_FUNCTIONS](info-schema/class_instance_functions.md) | Database | ✔ |  |
| [CLASS_INSTANCE_PROCEDURES](info-schema/class_instance_procedures.md) | Database | ✔ |  |
| [CLASS_INSTANCES](info-schema/class_instances.md) | Database | ✔ |  |
| [CLASSES](info-schema/classes.md) | Database | ✔ |  |
| [COLUMNS](info-schema/columns.md) | Database |  |  |
| [CORTEX_SEARCH_SERVICE](info-schema/cortex_search.md) | Database | ✔ |  |
| [CORTEX_SEARCH_SERVICE_SCORING_PROFILES](info-schema/cortex_search_service_scoring_profiles.md) | Database | ✔ |  |
| [CURRENT_PACKAGES_POLICY](info-schema/current_packages_policy.md) | Database | ✔ |  |
| [DATABASES](info-schema/databases.md) | Account | ✔ |  |
| [ELEMENT_TYPES](info-schema/element_types.md) | Database |  |  |
| [ENABLED_ROLES](info-schema/enabled_roles.md) | Account |  |  |
| [EVENT_TABLES](info-schema/event_tables.md) | Database | ✔ |  |
| [EXTERNAL_TABLES](info-schema/external_tables.md) | Database | ✔ |  |
| [FIELDS](info-schema/fields.md) | Database |  |  |
| [FILE FORMATS](info-schema/file_formats.md) | Database | ✔ |  |
| [FUNCTIONS](info-schema/functions.md) | Database |  |  |
| [HYBRID_TABLES](info-schema/hybrid_tables.md) | Database | ✔ |  |
| [INDEXES](info-schema/indexes.md) | Database | ✔ |  |
| [INDEX_COLUMNS](info-schema/index_columns.md) | Database | ✔ |  |
| [INFORMATION_SCHEMA_CATALOG_NAME](info-schema/information_schema_catalog_name.md) | Account |  |  |
| [LISTINGS](info-schema/listings.md) | Account | ✔ |  |
| [LOAD_HISTORY](info-schema/load_history.md) | Account | ✔ | Data retained for 14 days. |
| [MODEL_VERSIONS](info-schema/model_versions.md) | Database | ✔ |  |
| [OBJECT_PRIVILEGES](info-schema/object_privileges.md) | Account |  |  |
| [PACKAGES](info-schema/packages.md) | Database | ✔ |  |
| [PIPES](info-schema/pipes.md) | Database | ✔ |  |
| [PROCEDURES](info-schema/procedures.md) | Database | ✔ |  |
| [REFERENTIAL_CONSTRAINTS](info-schema/referential_constraints.md) | Database |  |  |
| [REPLICATION_DATABASES](info-schema/replication_databases.md) | Account | ✔ |  |
| [REPLICATION_GROUPS](info-schema/replication_groups.md) | Account | ✔ |  |
| [SCHEMATA](info-schema/schemata.md) | Database |  |  |
| [SEMANTIC_DIMENSIONS](info-schema/semantic_dimensions.md) | Database | ✔ |  |
| [SEMANTIC_FACTS](info-schema/semantic_facts.md) | Database | ✔ |  |
| [SEMANTIC_METRICS](info-schema/semantic_metrics.md) | Database | ✔ |  |
| [SEMANTIC_RELATIONSHIPS](info-schema/semantic_relationships.md) | Database | ✔ |  |
| [SEMANTIC_TABLES](info-schema/semantic_tables.md) | Database | ✔ |  |
| [SEMANTIC_VIEW](info-schema/semantic_views.md) | Database | ✔ |  |
| [SEQUENCES](info-schema/sequences.md) | Database |  |  |
| [SERVICES](info-schema/services.md) | Database | ✔ |  |
| [SHARES](info-schema/shares.md) | Account | ✔ |  |
| [STAGES](info-schema/stages.md) | Database | ✔ |  |
| [TABLE_CONSTRAINTS](info-schema/table_constraints.md) | Database |  |  |
| [TABLE_PRIVILEGES](info-schema/table_privileges.md) | Database |  |  |
| [TABLE_STORAGE_METRICS](info-schema/table_storage_metrics.md) | Database | ✔ |  |
| [TABLES](info-schema/tables.md) | Database |  | Displays tables and views. |
| [USAGE_PRIVILEGES](info-schema/usage_privileges.md) | Database |  | Displays privileges on sequences only; to view privileges on other types of objects, use OBJECT_PRIVILEGES. |
| [VIEWS](info-schema/views.md) | Database |  |  |

## List of Information Schema table functions

The table functions in INFORMATION_SCHEMA can be used to return account-level usage and historical information for storage, warehouses,
user logins, and queries:

| Table Function | Data Retention | Notes |
| --- | --- | --- |
| [ALERT_HISTORY](functions/alert_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [APPLICATION_CALLBACK_HISTORY](functions/application_callback_history.md) | 365 days | Results depend on the privileges assigned to the user’s current role. |
| [APPLICATION_CONFIGURATION_VALUE_HISTORY](functions/application_configuration_value_history.md) | 365 days | Results depend on the privileges assigned to the user’s current role. |
| [APPLICATION_SPECIFICATION_STATUS_HISTORY](functions/application_specification_status_history.md) | 365 days | Results depend on the privileges assigned to the user’s current role. |
| [AUTOMATIC_CLUSTERING_HISTORY](functions/automatic_clustering_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [AUTO_REFRESH_REGISTRATION_HISTORY](functions/auto_refresh_registration_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [AVAILABLE_LISTINGS](functions/available_listings.md) | N/A | Results are returned for all listings that consumers can discover and access. |
| [AVAILABLE_LISTING_REFRESH_HISTORY](functions/available_listing_refresh_history.md) | 14 days | Results are only returned for consumers of listings who have any privilege on the available listing or mounted database. |
| [COMPLETE_TASK_GRAPHS](functions/complete_task_graphs.md) | 60 minutes | Results returned only for the ACCOUNTADMIN role, the task owner (i.e. the role with the OWNERSHIP privilege on the task), or a role with the global MONITOR EXECUTION privilege. |
| [COPY_HISTORY](functions/copy_history.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [CORTEX_SEARCH_REFRESH_HISTORY](functions/cortex_search_refresh_history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. |
| [CURRENT_TASK_GRAPHS](functions/current_task_graphs.md) | N/A | Results returned only for the ACCOUNTADMIN role, the task owner (i.e. the role with the OWNERSHIP privilege on the task), or a role with the global MONITOR EXECUTION privilege. |
| [DATA_METRIC_FUNCTION_REFERENCES](functions/data_metric_function_references.md) | N/A | Results depend on the privileges or database role assigned to the user’s current role. |
| [DATA_TRANSFER_HISTORY](functions/data_transfer_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [DATABASE_REFRESH_HISTORY](functions/database_refresh_history.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [DATABASE_REFRESH_PROGRESS , DATABASE_REFRESH_PROGRESS_BY_JOB](functions/database_refresh_progress.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [DATABASE_REPLICATION_USAGE_HISTORY](functions/database_replication_usage_history.md) | 14 days | Results returned only for the ACCOUNTADMIN role. |
| [DATABASE_STORAGE_USAGE_HISTORY](functions/database_storage_usage_history.md) | 6 months | Results depend on MONITOR USAGE privilege. [1] |
| [DBT_PROJECT_EXECUTION_HISTORY](functions/dbt_project_execution_history.md). | 7 days. | Results depend on MONITOR, OWNERSHIP, or USAGE privilege. |
| [DYNAMIC_TABLES](functions/dynamic_tables.md) | 7 days | Results depend on the privileges assigned to the user’s current role. For more information, see [Dynamic table access control](../user-guide/dynamic-tables-privileges.md). [1] |
| [DYNAMIC_TABLE_GRAPH_HISTORY](functions/dynamic_table_graph_history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. For more information, see [Dynamic table access control](../user-guide/dynamic-tables-privileges.md). [1] |
| [DYNAMIC_TABLE_REFRESH_HISTORY](functions/dynamic_table_refresh_history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. For more information, see [Dynamic table access control](../user-guide/dynamic-tables-privileges.md). [1] |
| [EXTERNAL_FUNCTIONS_HISTORY](functions/external_functions_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [EXTERNAL_TABLE_FILES](functions/external_table_files.md) | N/A | Results depend on the privileges assigned to the user’s current role. |
| [EXTERNAL_TABLE_FILE_REGISTRATION_HISTORY](functions/external_table_registration_history.md) | 30 days | Results depend on the privileges assigned to the user’s current role. |
| [ICEBERG_TABLE_FILES](functions/iceberg_table_files.md) | Varies | Results depend on the value of the [DATA_RETENTION_TIME_IN_DAYS](parameters.md) parameter set for the table. For more information, see [Metadata and retention for Apache Iceberg™ tables](../user-guide/tables-iceberg-metadata.md). |
| [ICEBERG_TABLE_SNAPSHOT_REFRESH_HISTORY](functions/iceberg_table_snapshot_refresh_history.md) | Varies | Results depend on the value of the [DATA_RETENTION_TIME_IN_DAYS](parameters.md) parameter set for the table. For more information, see [Metadata and retention for Apache Iceberg™ tables](../user-guide/tables-iceberg-metadata.md). |
| [LISTING_REFRESH_HISTORY](functions/listing_refresh_history.md) | 14 days | Results are only returned for a role with any privilege on Listing Auto-Fulfillment. |
| [LOGIN_HISTORY , LOGIN_HISTORY_BY_USER](functions/login_history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. |
| [MATERIALIZED_VIEW_REFRESH_HISTORY](functions/materialized_view_refresh_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [NOTIFICATION_HISTORY](functions/notification_history.md) | 14 days | Results returned only for the ACCOUNTADMIN role, the integration owner (i.e. the role with the OWNERSHIP privilege on the integration) or a role with the USAGE privilege on the integration. |
| [ONLINE_FEATURE_TABLE_REFRESH_HISTORY](functions/online-feature-table-refresh-history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. |
| [PIPE_USAGE_HISTORY](functions/pipe_usage_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [POLICY_REFERENCES](functions/policy_references.md) | N/A | Results returned only for the ACCOUNTADMIN role. |
| [QUERY_ACCELERATION_HISTORY](functions/query_acceleration_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [QUERY_HISTORY , QUERY_HISTORY_BY_\*](functions/query_history.md) | 7 days | Results depend on the privileges assigned to the user’s current role. |
| [REPLICATION_GROUP_DANGLING_REFERENCES](functions/replication_group_dangling_references.md) | N/A |  |
| [REPLICATION_GROUP_REFRESH_HISTORY, REPLICATION_GROUP_REFRESH_HISTORY_ALL](functions/replication_group_refresh_history.md) | 14 days | Results are only returned for a role with any privilege on the replication or failover group. |
| [REPLICATION_GROUP_REFRESH_PROGRESS, REPLICATION_GROUP_REFRESH_PROGRESS_BY_JOB, REPLICATION_GROUP_REFRESH_PROGRESS_ALL](functions/replication_group_refresh_progress.md) | 14 days | Results are only returned for a role with any privilege on the replication or failover group. |
| [REPLICATION_GROUP_USAGE_HISTORY](functions/replication_group_usage_history.md) | 14 days | Results depend on the MONITOR USAGE privilege. [1] |
| [REPLICATION_USAGE_HISTORY](functions/replication_usage_history.md) | 14 days | Results returned only for the ACCOUNTADMIN role. |
| [REST_EVENT_HISTORY](functions/rest_event_history.md) | 7 days | Results returned only for the ACCOUNTADMIN role. |
| [SEARCH_OPTIMIZATION_HISTORY](functions/search_optimization_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [SERVERLESS_ALERT_HISTORY](functions/serverless_alert_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [SERVERLESS_TASK_HISTORY](functions/serverless_task_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [STAGE_DIRECTORY_FILE_REGISTRATION_HISTORY](functions/stage_directory_file_registration_history.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [STAGE_STORAGE_USAGE_HISTORY](functions/stage_storage_usage_history.md) | 6 months | Results depend on MONITOR USAGE privilege. [1] |
| [STORAGE_LIFECYCLE_POLICY_HISTORY](functions/storage_lifecycle_policy_history.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [TAG_REFERENCES](functions/tag_references.md) | N/A | Results are only returned for the role that has access to the specified object. |
| [TAG_REFERENCES_ALL_COLUMNS](functions/tag_references_all_columns.md) | N/A | Results are only returned for the role that has access to the specified object. |
| [TASK_DEPENDENTS](functions/task_dependents.md) | N/A | Results returned only for the ACCOUNTADMIN role or task owner (role with OWNERSHIP privilege on task). |
| [TASK_HISTORY](functions/task_history.md) | 7 days | Results returned only for the ACCOUNTADMIN role, the task owner (i.e. the role with the OWNERSHIP privilege on the task), or a role with the global MONITOR EXECUTION privilege. |
| [VALIDATE_PIPE_LOAD](functions/validate_pipe_load.md) | 14 days | Results depend on the privileges assigned to the user’s current role. |
| [WAREHOUSE_LOAD_HISTORY](functions/warehouse_load_history.md) | 14 days | Results depend on MONITOR USAGE privilege. [1] |
| [WAREHOUSE_METERING_HISTORY](functions/warehouse_metering_history.md) | 6 months | Results depend on MONITOR USAGE privilege. [1] |

[1] Returns results if role has been assigned the MONITOR USAGE global privilege; otherwise, returns results only for the ACCOUNTADMIN role.

## General usage notes

* Each INFORMATION_SCHEMA schema is read-only (i.e. the schema, and all the views and table functions in the schema, cannot be modified
  or dropped).
* Queries on INFORMATION_SCHEMA views do not guarantee consistency with respect to concurrent DDL. For example, if a set of tables are
  created while a long-running INFORMATION_SCHEMA query is being executed, the result of the query may include some, none, or all of
  the tables created.
* The output of a view or table function depend on the privileges granted to the user’s current role. When querying an INFORMATION_SCHEMA
  view or table function, only objects for which the current role has been granted access privileges are returned.
* To prevent performance issues, the following error is returned if the filters specified in an INFORMATION_SCHEMA query are not
  sufficiently selective:

  > `Information schema query returned too much data. Please repeat query with more selective predicates.`
* The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
  For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.

> **Tip:**
>
> The Information Schema views are optimized for queries that retrieve a small subset of objects from the dictionary. Whenever possible,
> maximize the performance of your queries by filtering on schema and object names.
>
> For more usage information and details, see the
> [Snowflake Information Schema blog post](https://www.snowflake.com/blog/using-snowflake-information-schema/).

## Considerations for replacing SHOW commands with Information Schema views

The INFORMATION_SCHEMA views provide a SQL interface to the same information provided by the [SHOW <objects>](sql/show.md) commands.
You can use the views to replace these commands; however, there are some key differences to consider before switching:

| Considerations | SHOW Commands | Information Schema Views |
| --- | --- | --- |
| Warehouses | Not required to execute. | Warehouse must be running and currently in use to query the views. |
| Pattern matching/filtering | Case-insensitive (when filtering using LIKE). | Standard (case-sensitive) SQL semantics. Snowflake automatically converts unquoted, case-insensitive identifiers to uppercase internally, so unquoted object names must be queried in uppercase in the Information Schema views. |
| Query results | Most SHOW commands limit results to the current schema by default. | Views display all objects in the current/specified database. To query against a particular schema, you must use a filter predicate (e.g. `... WHERE table_schema = CURRENT_SCHEMA()...`). Note that Information Schema queries lacking sufficiently selective filters return an error and do not execute (see General Usage Notes in this topic). |

## Qualifying the names of Information Schema views and table functions in queries

When querying an INFORMATION_SCHEMA view or table function, you must use the qualified name of the view/table function or the
INFORMATION_SCHEMA schema must be in use for the session.

For example:

* To query using the fully-qualified names of the view and table function, in the form of `database.information_schema.name`:

  ```sqlexample
  SELECT table_name, comment FROM testdb.INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'PUBLIC' ... ;

  SELECT event_timestamp, user_name FROM TABLE(testdb.INFORMATION_SCHEMA.LOGIN_HISTORY( ... ));
  ```

* To query using the qualified names of the view and table function, in the form of `information_schema.name`:

  ```sqlexample
  USE DATABASE testdb;

  SELECT table_name, comment FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'PUBLIC' ... ;

  SELECT event_timestamp, user_name FROM TABLE(INFORMATION_SCHEMA.LOGIN_HISTORY( ... ));
  ```

* To query with the INFORMATION_SCHEMA schema in use for the session:

  ```sqlexample
  USE SCHEMA testdb.INFORMATION_SCHEMA;

  SELECT table_name, comment FROM TABLES WHERE TABLE_SCHEMA = 'PUBLIC' ... ;

  SELECT event_timestamp, user_name FROM TABLE(LOGIN_HISTORY( ... ));
  ```

  > **Note:**
  >
  > If you are using a database that was created from a share and you have selected INFORMATION_SCHEMA as the current schema for the
  > session, the SELECT statement might fail with the following error:
  >
  > INFORMATION_SCHEMA does not exist or is not authorized
  >
  > If this occurs, select a different schema for the current schema for the session.

For more detailed examples, see the reference documentation for each view/table function.
