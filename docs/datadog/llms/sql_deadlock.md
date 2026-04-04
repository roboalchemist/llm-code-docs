# Source: https://docs.datadoghq.com/database_monitoring/guide/sql_deadlock.md

---
title: Configuring Deadlock Monitoring on SQL Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Configuring Deadlock
  Monitoring on SQL Server
---

# Configuring Deadlock Monitoring on SQL Server

The Deadlock view enables you to explore deadlock events in your SQL Server database. A deadlock occurs when two or more processes are unable to proceed because each is waiting for the other to release resources.

## Before you begin{% #before-you-begin %}

You must configure Database Monitoring for your [SQL Server](https://docs.datadoghq.com/database_monitoring/setup_sql_server/) before following the steps in this guide.

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
All deployment types. Azure DB is supported for Agent versions 7.64.0 and later.
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.59.0+
{% /dd %}

{% /dl %}

## Setup{% #setup %}

{% tab title="All deployment types except Azure DB" %}

1. In the SQL Server database instance, create a Datadog Extended Events (XE) session. You can run the session on any database in the instance.

**Note**: If the Datadog XE session isn't created in the database, the Agent still attempts to collect deadlock events from the default SQL Server system health XE session.

```sql
  CREATE EVENT SESSION datadog
  ON SERVER
  ADD EVENT sqlserver.xml_deadlock_report
  ADD TARGET package0.ring_buffer
  (
    SET MAX_MEMORY = 1024
  )
  WITH (
      MAX_MEMORY = 1024 KB,
      EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
      MAX_DISPATCH_LATENCY = 30 SECONDS,
      MEMORY_PARTITION_MODE = PER_NODE, -- improves performance on multi-core systems (not supported on RDS)
      STARTUP_STATE = ON
  );
  GO

  ALTER EVENT SESSION datadog ON SERVER STATE = START;
  GO
```

**Note**: If you're using Amazon RDS for SQL Server, remove the `MEMORY_PARTITION_MODE = PER_NODE` line from the session configuration, as this option is not supported on RDS instances.
In the Datadog Agent, enable deadlocks in `sqlserver.d/conf.yaml`.
```yaml
  collect_deadlocks: # Renamed from deadlocks_collection in Agent version 7.70.
      enabled: true
```

{% /tab %}

{% tab title="Azure DB" %}

1. In the SQL Server database, create a Datadog Extended Events (XE) session.

```sql
  CREATE EVENT SESSION datadog
  ON database
  ADD EVENT sqlserver.database_xml_deadlock_report
  ADD TARGET package0.ring_buffer
  (
    SET MAX_MEMORY = 1024
  )
  WITH (
      MAX_MEMORY = 1024 KB,
      EVENT_RETENTION_MODE = ALLOW_SINGLE_EVENT_LOSS,
      MAX_DISPATCH_LATENCY = 30 SECONDS,
      STARTUP_STATE = ON
  );
  GO

  ALTER EVENT SESSION datadog ON DATABASE STATE = START;
  GO
```
In the Datadog Agent, enable deadlocks in `sqlserver.d/conf.yaml`.
```yaml
  collect_deadlocks: # Renamed from deadlocks_collection in Agent version 7.70.
      enabled: true
```

{% /tab %}

## Exploring deadlock events{% #exploring-deadlock-events %}

To access the deadlock view, navigate to the **APM** > **Database Monitoring** > **Databases** tab, then select a SQL Server host. Next, select the **Queries** tab, then select the **Deadlocks** tab. The Deadlocks tab displays details about the victim and survivor processes, and includes a link to the deadlock diagram.

**Note**: Because deadlocks occur infrequently, it's unlikely that any deadlock information will be visible right away.

## Further reading{% #further-reading %}

- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Setting Up SQL Server](https://docs.datadoghq.com/database_monitoring/setup_sql_server/)
- [Troubleshooting Database Monitoring](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
