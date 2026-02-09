# Source: https://docs.datadoghq.com/database_monitoring/guide/sql_alwayson.md

---
title: Exploring SQL Server AlwaysOn Availability Groups
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Exploring SQL Server
  AlwaysOn Availability Groups
---

# Exploring SQL Server AlwaysOn Availability Groups

The Database Monitoring AlwaysOn Clusters view enables you to detect data synchronization issues, understand availability group behavior, and identify cluster bottlenecks in SQL Server availability groups.

To access the AlwaysOn Clusters view, navigate to the **APM** > **Database Monitoring** > **Databases** tab and select **AlwaysOn Clusters**.

## Determine the health of your nodes{% #determine-the-health-of-your-nodes %}

Use the AlwaysOn Clusters view to evaluate the health of your SQL Server availability groups. When selected, the page shows a color-coded visualization based on the current status of the primary (P) and secondary (S) nodes in each availability group.

To identify groups that are experiencing issues, use the status filters to show groups with nodes that are **Reverting**, **Not Synchronizing**, and so forth. You can also use the timeseries graphs to spot unusual performance activity in your clusters based on log, redo, and secondary lag time metrics.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_alwayson.19097ea5722e236a8dc67b87818bfd16.png?auto=format"
   alt="View SQL Server AlwaysOn groups" /%}

## Analyze historical metrics{% #analyze-historical-metrics %}

To evaluate how node synchronization states have fluctuated over time, select an availability group to open the details side panel. The **Historical Synchronization States** graph at the top of the panel shows the status of each node over the selected timeframe.

View additional information about all replicas and their associated databases on the **Replicas** tab. You can also use the timeseries graphs on the **Metrics** tab to spot abnormal behavior in individual replicas and databases based on send, redo, and lag metrics.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_alwayson_history.4bd619671157fe58f4b1a5939422963b.png?auto=format"
   alt="View SQL Server AlwaysOn groups" /%}

## Further Reading{% #further-reading %}

- [Database Monitoring](https://docs.datadoghq.com/database_monitoring/)
- [Setting Up SQL Server](https://docs.datadoghq.com/database_monitoring/setup_sql_server/)
- [Troubleshooting Database Monitoring](https://docs.datadoghq.com/database_monitoring/troubleshooting/)
