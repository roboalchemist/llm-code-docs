# Source: https://docs.datadoghq.com/database_monitoring/database_hosts.md

---
title: Exploring Database Hosts
description: Explore and dig into your database host health and configuration
breadcrumbs: Docs > Database Monitoring > Exploring Database Hosts
---

# Exploring Database Hosts

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/databases-list-4.e41dc13a857a12194a43e9f3a8a41790.png?auto=format"
   alt="The Databases page in Datadog" /%}

On the [Databases page](https://app.datadoghq.com/databases), you can assess the health and activity of your database hosts and clusters. Sort and filter the list to prioritize hosts and clusters with triggered alerts, high query volume, and other criteria. Click on any host in the list to open a details panel:

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-details-panel-cropped-3.73edfd9a5bc2bc4977bba454c9fe7be2.png?auto=format"
   alt="The details panel for a single database host on the Databases page" /%}

In addition to a filterable graph of active connections for that host, the host details panel displays the following features.

| Postgres              | SQL Server | MySQL | Oracle |
| --------------------- | ---------- | ----- | ------ |
| Top queries           | yes        | yes   | yes    | yes |
| Stored procedures     | yes        |
| Metrics               | yes        | yes   |
| Active connections    | yes        | yes   | yes    | yes |
| Schema                | yes        | yes   |
| Blocking queries      | yes        | yes   | yes    | yes |
| Calling services      | yes        | yes   | yes    |
| Configuration details | yes        | yes   | yes    |

## Cluster grouping{% #cluster-grouping %}

A **Group into clusters** toggle appears with the list of database hosts if host tags indicate the presence of cluster topology. Enable this toggle to group hosts into clusters within the list.

Cluster rows display a **Cluster** badge and show the number of instances in the cluster. Columns for cluster rows display aggregated data from all instances within the cluster. Select a cluster row to expand it and view a list of all instances that the cluster contains.

Cluster grouping supports the following database technology and cluster topologies:

| Database                               | Topologies                                    | Grouping Tags                                          | Cluster Name Source                                                                                                 |
| -------------------------------------- | --------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| Amazon RDS*(AWS integration required)* | - Multi-AZ clusters
  - Read replicas         | - `dbclusteridentifier`
  - `region`
  - `aws_account` | - `dbclusteridentifier`                                                                                             |
| PostgreSQL*(Agent v7.58+ required)*    | - Physical replication                        | - `system_identifier`
  - `env`                        | - `postgresql_cluster_name` (from instance `cluster_name` config)
  - Primary instance name
  - `system_identifier` |
| MySQL*(Agent v7.68+ required)*         | - Regular replication (not group replication) | - `cluster_uuid`
  - `env`                             | - Primary instance name
  - `cluster_uuid`                                                                          |

## Top queries{% #top-queries %}

On the **Top Queries** tab of the host details panel, you can sort the most common queries by maximum duration, average latency, and more.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-top-queries.3ee2db89b81b940e502ad814ac55c2b3.png?auto=format"
   alt="The Top Queries tab of the details panel for a single database host on the Databases page" /%}

Click on any query statement to open a details panel that includes:

- query insights
- graphs for average latency and other key metrics
- explain plans
- blocking activity
- hosts that have run the query
- calling services

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-query-details.62fe254335d800d3008bc50d96bcfbbe.png?auto=format"
   alt="The details panel for an individual top query" /%}

### Stored procedures{% #stored-procedures %}

Where supported, the **Top Queries** tab includes a **Stored Procedures** section that lists each stored procedure by name, along with its average duration, logical reads count, logical writes count, and more. Expand a stored procedure to view its individual SQL queries, and click on a query to view its details panel.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/stored-procedures.68b5cc5ab9fa44a50075a408a9563ea0.png?auto=format"
   alt="A list of stored procedures, with one expanded to show its SQL query" /%}

## Metrics{% #metrics %}

On the **Metrics** tab of the host details panel, you can view and filter metrics for system health, query activity, blocking operations, function performance, and other key areas.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-metrics.a4137bc19e56ce64f2f285daf7645a9b.png?auto=format"
   alt="The Metrics tab of the details panel for a single database host on the Databases page" /%}

## Active connections{% #active-connections %}

The **Active Connections** tab of the host details panel displays the live queries being executed on the host. Click on a query statement to open a panel that includes event attributes, related traces, and other relevant details.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-active-connections-2.e25fa7b9bf54fb1cb635fdb68934b0f8.png?auto=format"
   alt="The Active Connections tab of the details panel for a single database host on the Databases page" /%}

## Schema{% #schema %}

Use the **Schema** tab to explore database structures, tables, columns, data types, existing foreign keys, and indexing strategies for every database on a host.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-schema-tab.dac6c195829b72384ff5208d5916e5a3.png?auto=format"
   alt="The Schema tab of the details panel for a single database host on the Databases page" /%}

## Blocking queries{% #blocking-queries %}

On the **Blocking Queries** tab of host details panel, you can view visualizations for:

- blocking query durations
- blocking query executions
- the number of waiting queries

You can search and filter the queries or samples. Click any individual query row to view details.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-blocking-queries.e240e2fb9c03575d3f88795064a83f82.png?auto=format"
   alt="The Blocking Queries tab of the details panel for a single database host on the Databases page" /%}

## Calling services{% #calling-services %}

On the **Calling Services** tab of the host details panel, you can view the list of services that have called the host. The displayed service information includes when the service was deployed, the number of requests made to the host per second, how many database queries were executed, and more.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-calling-services.7c422fbd9380dc6e49efae9497012e99.png?auto=format"
   alt="The Calling Services tab of the details panel for a single database host on the Databases page" /%}

Click any service row to view its APM dashboard.

## Configuration details{% #configuration-details %}

{% alert level="info" %}
The host must have `collect_settings` enabled in its [instance configuration](https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example#L397) for this feature to work properly.
{% /alert %}

The **Configuration** tab of the host details panel provides a direct view into the host's configuration parameters without compromising database security. Use it to identify misconfigured database parameters and adjust settings to optimize database performance.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/db-list-configuration.dd9761721733d6fef0043009d7c9b8fc.png?auto=format"
   alt="The Configuration tab of the details panel for a single database host on the Databases page" /%}
