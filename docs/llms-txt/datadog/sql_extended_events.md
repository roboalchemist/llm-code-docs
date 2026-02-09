# Source: https://docs.datadoghq.com/database_monitoring/guide/sql_extended_events.md

---
title: Configuring Query Completion and Query Error Capture on SQL Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Configuring Query
  Completion and Query Error Capture on SQL Server
---

# Configuring Query Completion and Query Error Capture on SQL Server

This feature collects query completion and query error events from your SQL Server instances using Extended Events (XE). It provides visibility into:

- Metrics and behavior of SQL queries with parameter values
- Errors and timeouts that occurred during execution

For information about query parameter capture across different database systems, see [Configuring Query Capture with Parameter Values](https://docs.datadoghq.com/database_monitoring/guide/parameterized_queries/).

This data is useful for:

- Performance analysis
- Debugging app behavior
- Auditing unexpected errors or timeouts

## Before you begin{% #before-you-begin %}

You must configure Database Monitoring for your [SQL Server](https://docs.datadoghq.com/database_monitoring/guide/parameterized_queries/) instance before continuing with this guide.

{% dl %}

{% dt %}
Supported databases
{% /dt %}

{% dd %}
SQL Server
{% /dd %}

{% dt %}
Supported deployments
{% /dt %}

{% dd %}
All deployment types.
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.67.0+
{% /dd %}

{% /dl %}

## Setup{% #setup %}

{% tab title="Non-Azure SQL Server" %}

1. In your SQL Server instance, create the following Extended Events (XE) sessions. These sessions can be created on any database within the instance.

The `datadog_query_completions` XE session captures long-running SQL queries (over 1 second) from RPC calls, SQL batches, and stored procedures.

```sql
-- Query completions: RPC, batch, and stored procedure events
IF EXISTS (
    SELECT * FROM sys.server_event_sessions WHERE name = 'datadog_query_completions'
)
    DROP EVENT SESSION datadog_query_completions ON SERVER;
GO

CREATE EVENT SESSION datadog_query_completions ON SERVER -- datadog requires this exact session name
ADD EVENT sqlserver.rpc_completed ( -- capture remote procedure call completions
    ACTION ( -- datadog requires these exact actions for rpc_completed
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
),
ADD EVENT sqlserver.sql_batch_completed( -- capture batch completions
    ACTION ( -- datadog requires these exact actions for sql_batch_completed
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
),
ADD EVENT sqlserver.module_end( -- capture stored procedure completions
    SET collect_statement = (1)
    ACTION ( -- datadog requires these exact actions for module_end
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
)
ADD TARGET package0.ring_buffer -- do not change, datadog is only configured to read from ring buffer at this time
(
  SET MAX_MEMORY = 1024
)
WITH (
    MAX_MEMORY = 1024 KB, -- do not exceed 1024, values above 1 MB may result in data loss due to SQLServer internals
    TRACK_CAUSALITY = ON, -- allows datadog to correlate related events across activity ID
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MEMORY_PARTITION_MODE = PER_NODE, -- improves performance on multi-core systems (not supported on RDS)
    STARTUP_STATE = ON
);

ALTER EVENT SESSION datadog_query_completions ON SERVER STATE = START;
GO
```

The datadog_query_errors XE session captures SQL errors of [severity â¥ 11](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-error-severities) and query timeouts (also known as [attention events](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/attention-event-class)), enabling Datadog to report query failures and timeouts.

```sql
-- Errors and timeouts: SQL errors and attention events
IF EXISTS (
    SELECT * FROM sys.server_event_sessions WHERE name = 'datadog_query_errors'
)
    DROP EVENT SESSION datadog_query_errors ON SERVER;
GO
CREATE EVENT SESSION datadog_query_errors ON SERVER
ADD EVENT sqlserver.error_reported(
    ACTION( -- datadog requires these exact actions for error_reported
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE severity >= 11
),
ADD EVENT sqlserver.attention(
    ACTION( -- datadog requires these exact actions for attention
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
)
ADD TARGET package0.ring_buffer -- do not change, datadog is only configured to read from ring buffer at this time
(
  SET MAX_MEMORY = 1024
)
WITH (
    MAX_MEMORY = 1024 KB, -- do not change, setting this larger than 1 MB may result in data loss due to SQLServer internals
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MEMORY_PARTITION_MODE = PER_NODE, -- improves performance on multi-core systems (not supported on RDS)
    STARTUP_STATE = ON
);

ALTER EVENT SESSION datadog_query_errors ON SERVER STATE = START;
GO
```

**Note**: If you're using Amazon RDS for SQL Server, remove the `MEMORY_PARTITION_MODE = PER_NODE` line from both session configurations, as this option is not supported on RDS instances.
In the Datadog Agent configuration, enable `xe_collection` in `sqlserver.d/conf.yaml`. See the [sample conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/sqlserver/datadog_checks/sqlserver/data/conf.yaml.example) for all available configuration options.
```yaml
  xe_collection:
    query_completions:
      enabled: true
    query_errors:
      enabled: true
```

To collect query statements with parameter values, enable `collect_raw_query_statement` in `sqlserver.d/conf.yaml`. For more information about parameter capture, see [Configuring Query Capture with Parameter Values](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-error-severities).

```yaml
  collect_raw_query_statement:
    enabled: true
```

{% alert level="info" %}
Raw query statements and execution plans may contain sensitive information (for example, passwords in query text) or personally identifiable information. Enabling this option allows Datadog to collect and ingest raw query statements and execution plans that appear in query samples or explain plans. This option is disabled by default.
{% /alert %}

{% /tab %}

{% tab title="Azure DB" %}

1. In your Azure SQL Server Database, create the following Extended Events (XE) sessions:

The `datadog_query_completions` XE session captures long-running SQL queries (over 1 second) from RPC calls, SQL batches, and stored procedures.

```sql
-- Query completions: RPC, batch, and stored procedure events
IF EXISTS (
    SELECT * FROM sys.database_event_sessions WHERE name = 'datadog_query_completions'
)
    DROP EVENT SESSION datadog_query_completions ON DATABASE;
GO

CREATE EVENT SESSION datadog_query_completions ON DATABASE -- datadog requires this exact session name
ADD EVENT sqlserver.rpc_completed ( -- capture remote procedure call completions
    ACTION ( -- datadog requires these exact actions for rpc_completed
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
),
ADD EVENT sqlserver.sql_batch_completed( -- capture batch completions
    ACTION ( -- datadog requires these exact actions for sql_batch_completed
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
),
ADD EVENT sqlserver.module_end( -- capture stored procedure completions
    SET collect_statement = (1)
    ACTION ( -- datadog requires these exact actions for module_end
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE (
        sql_text <> '' AND
        duration > 1000000 -- in microseconds, limit to queries with duration greater than 1 second
    )
)
ADD TARGET package0.ring_buffer -- do not change, datadog is only configured to read from ring buffer at this time
(
  SET MAX_MEMORY = 1024
)
WITH (
    MAX_MEMORY = 1024 KB, -- do not exceed 1024, values above 1 MB may result in data loss due to SQLServer internals
    TRACK_CAUSALITY = ON, -- allows datadog to correlate related events across activity ID
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MEMORY_PARTITION_MODE = PER_NODE, -- improves performance on multi-core systems
    STARTUP_STATE = ON
);

ALTER EVENT SESSION datadog_query_completions ON DATABASE STATE = START;
GO
```

The datadog_query_errors XE session captures SQL errors of [severity â¥ 11](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-error-severities) and query timeouts (also known as [attention events](https://learn.microsoft.com/en-us/sql/relational-databases/event-classes/attention-event-class)), enabling Datadog to report query failures and timeouts.

```sql
-- Errors and timeouts: SQL errors and attention events
IF EXISTS (
    SELECT * FROM sys.database_event_sessions WHERE name = 'datadog_query_errors'
)
    DROP EVENT SESSION datadog_query_errors ON DATABASE;
GO
CREATE EVENT SESSION datadog_query_errors ON DATABASE
ADD EVENT sqlserver.error_reported(
    ACTION( -- datadog requires these exact actions for error_reported
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
    WHERE severity >= 11
),
ADD EVENT sqlserver.attention(
    ACTION( -- datadog requires these exact actions for attention
        sqlserver.sql_text,
        sqlserver.database_name,
        sqlserver.username,
        sqlserver.client_app_name,
        sqlserver.client_hostname,
        sqlserver.session_id,
        sqlserver.request_id
    )
)
ADD TARGET package0.ring_buffer -- do not change, datadog is only configured to read from ring buffer at this time
(
  SET MAX_MEMORY = 1024
)
WITH (
    MAX_MEMORY = 1024 KB, -- do not change, setting this larger than 1 MB may result in data loss due to SQLServer internals
    EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
    MAX_DISPATCH_LATENCY = 30 SECONDS,
    MEMORY_PARTITION_MODE = PER_NODE, -- improves performance on multi-core systems
    STARTUP_STATE = ON
);

ALTER EVENT SESSION datadog_query_errors ON DATABASE STATE = START;
GO
```
In the Datadog Agent configuration, enable `xe_collection` in `sqlserver.d/conf.yaml`. See the [sample conf.yaml.example](https://github.com/DataDog/integrations-core/blob/master/sqlserver/datadog_checks/sqlserver/data/conf.yaml.example) for all available configuration options.
```yaml
  xe_collection:
    query_completions:
      enabled: true
    query_errors:
      enabled: true
```

To collect query statements with parameter values, enable `collect_raw_query_statement` in `sqlserver.d/conf.yaml`. For more information about parameter capture, see [Configuring Query Capture with Parameter Values](https://learn.microsoft.com/en-us/sql/relational-databases/errors-events/database-engine-error-severities).

```yaml
  collect_raw_query_statement:
    enabled: true
```

{% alert level="info" %}
Raw query statements and execution plans may contain sensitive information (for example, passwords in query text) or personally identifiable information. Enabling this option allows Datadog to collect and ingest raw query statements and execution plans that appear in query samples or explain plans. This option is disabled by default.
{% /alert %}

{% /tab %}

## Tuning extended events for your environment (optional){% #tuning-extended-events-for-your-environment-optional %}

You can customize the Extended Events sessions to better fit your specific needs:

### Query duration threshold{% #query-duration-threshold %}

The default query duration threshold is `duration > 1000000` (1 second). Adjust this value to control how many queries are captured:

- **Capture more queries**: Lower the threshold (for example, `duration > 500000` for 500 ms)
- **Capture fewer queries**: Raise the threshold (for example, `duration > 5000000` for 5 seconds)

{% alert level="danger" %}
Setting thresholds too low can result in excessive event collection that affects server performance, event loss due to buffer overflow, and incomplete data, as Datadog only collects the most recent 1000 events per collection interval.
{% /alert %}

### Memory allocation{% #memory-allocation %}

- The default value is `MAX_MEMORY = 1024 KB`.
- Do not exceed 1024 KB, as higher values may cause data loss due to [SQL Server internal limitations](https://techcommunity.microsoft.com/blog/sqlserversupport/you-may-not-see-the-data-you-expect-in-extended-event-ring-buffer-targets8230-/315838).
- For high-volume servers, keeping this at a maximum of 1024 KB is recommended.
- For lower-traffic servers, a setting of 512 KB may be sufficient.

### Event filtering{% #event-filtering %}

To reduce event volume, you can add filters to the `WHERE` clause. For example:

```sql
WHERE (
    sql_text <> '' AND
    duration > 1000000 AND
    -- Add custom filters here
    database_name = 'YourImportantDB' AND -- Only track specific databases
    username <> 'datadog' -- Exclude Datadog Agent queries or specific users
)
```

### Performance considerations{% #performance-considerations %}

Extended Events are designed to be lightweight, but they can introduce some overhead. If you notice performance issues, consider doing the following:

- Increase the query duration threshold to limit captured queries.
- Add more specific filters to reduce event volume.
- Disable one or both sessions during peak load periods by running:

```sql
IF EXISTS (
    SELECT * FROM sys.server_event_sessions WHERE name = 'datadog_query_completions'
)
    DROP EVENT SESSION datadog_query_completions ON SERVER;
GO
IF EXISTS (
    SELECT * FROM sys.server_event_sessions WHERE name = 'datadog_query_errors'
)
    DROP EVENT SESSION datadog_query_errors ON SERVER;
GO
```

### Azure-specific considerations{% #azure-specific-considerations %}

Azure SQL Database environments typically have more constrained resources. To minimize performance impact:

- Use more restrictive filters if you're on a lower-tier service level.
- If you're using elastic pools, monitor for performance impact across all databases.

## Further reading{% #further-reading %}

- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Setting Up SQL Server](https://docs.datadoghq.com/database_monitoring/setup_sql_server/)
- [Configuring Query Capture with Parameter Values](https://docs.datadoghq.com/database_monitoring/guide/parameterized_queries/)
- [Troubleshooting Database Monitoring](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
