# Source: https://docs.snowflake.com/en/sql-reference-stored-procedures.md

# Stored procedures

Snowflake provides stored procedures to facilitate using certain Snowflake features. To find the stored procedures that are associated with a particular Snowflake Class, see [SQL class reference](sql-reference-classes.md).

Use [CALL](sql-reference/sql/call.md) to call a stored procedure. For example:

```sqlexample
CALL SYSTEM$CLASSIFY('hr.tables.empl_info', null);
```

Snowflake supports the following stored procedures, grouped by feature:

| Feature | Stored procedure |
| --- | --- |
| [Cortex Powered Object Descriptions](user-guide/sql-cortex-descriptions.md) | * [AI_GENERATE_TABLE_DESC](sql-reference/stored-procedures/ai_generate_table_desc.md) |
| [Data classification](user-guide/classify-intro.md) | *[ASSOCIATE_SEMANTIC_CATEGORY_TAGS](sql-reference/stored-procedures/associate_semantic_category_tags.md)* [SYSTEM$CLASSIFY](sql-reference/stored-procedures/system_classify.md) * [SYSTEM$CLASSIFY_SCHEMA](sql-reference/stored-procedures/system_classify_schema.md) * [SYSTEM$CANCEL_CLASSIFY_SCHEMA](sql-reference/stored-procedures/system_cancel_classify_schema.md) |
| [Data sharing and collaboration](guides-overview-sharing.md) | * [SYSTEM$REQUEST_LISTING_AND_WAIT](sql-reference/stored-procedures/system_request_listing_and_wait.md) |
| [Default event table](developer-guide/logging-tracing/event-table-setting-up.md) | *[ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](sql-reference/stored-procedures/snowflake_telemetry_add_row_access_policy_on_events_view.md)* [DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW](sql-reference/stored-procedures/snowflake_telemetry_drop_row_access_policy_on_events_view.md) |
| [Differential privacy](user-guide/diff-privacy/differential-privacy-overview.md) | * [RESET_PRIVACY_BUDGET](sql-reference/stored-procedures/reset_privacy_budget.md) |
| [Notifications](user-guide/notifications/about-notifications.md) | * [SYSTEM$SEND_SNOWFLAKE_NOTIFICATION](sql-reference/stored-procedures/system_send_snowflake_notification.md) * [SYSTEM$SEND_EMAIL](sql-reference/stored-procedures/system_send_email.md) |
| [Semantic views](user-guide/views-semantic/overview.md) | * [SYSTEM$CREATE_SEMANTIC_VIEW_FROM_YAML](sql-reference/stored-procedures/system_create_semantic_view_from_yaml.md) |
| [Synthetic data](user-guide/synthetic-data.md) | * [GENERATE_SYNTHETIC_DATA](sql-reference/stored-procedures/generate_synthetic_data.md) |
| [Trust Center](user-guide/trust-center/overview.md) | *[REGISTER_EXTENSION](sql-reference/stored-procedures/register_extension.md)* [DEREGISTER_EXTENSION](sql-reference/stored-procedures/deregister_extension.md) |
