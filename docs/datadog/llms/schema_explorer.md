# Source: https://docs.datadoghq.com/database_monitoring/schema_explorer.md

---
title: Exploring Database Schemas
description: Explore and analyze database schemas, including tables, columns, and indexes.
breadcrumbs: Docs > Database Monitoring > Exploring Database Schemas
---

# Exploring Database Schemas

Schemas help you monitor performance, usage, and changes in your data models, enabling quicker issue identification and remediation.

{% alert level="info" %}
Schema Tracking is available for PostgreSQL, SQL Server, and MySQL.
{% /alert %}

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm-schemas-page.4b2ac4c1c17b5c3c5ce51150382ee8d1.png?auto=format"
   alt="Schemas page displaying tracked database tables and schema-level metrics in Datadog" /%}

## Configuration{% #configuration %}

To enable the schemas feature, add the `collect_schemas` parameter to your Database Monitoring configuration:

```yaml
init_config:
instances:
  - dbm: true
    host: localhost
    port: 5432
    username: datadog
    password: 'ENC[datadog_user_database_password]'
    collect_schemas:
      enabled: true
    ## Optional: Connect to a different database if needed for `custom_queries`
    # dbname: '<DB_NAME>'
```

## Tables overview{% #tables-overview %}

The Tables overview lists all tracked tables across your databases, grouped by table name, with the following columns:

| Column         | Description                                                                                                                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \# Variants    | Number of distinct versions of the table across all hosts.                                                                                                                                           |
| \# Instances   | Total number of table instances across all hosts. For example, if a table has two variants with seven and eight instances respectively, the total number of instances is 15.                         |
| \# Columns     | Count of unique columns across all variants of the table on all hosts. For example, if one variant has columns A, B, C and another has A, B, D, the total unique columns would be four (A, B, C, D). |
| Databases      | Names of all databases containing this table across all hosts.                                                                                                                                       |
| Schemas        | Schemas in which this table appears across all hosts.                                                                                                                                                |
| Database Hosts | Hosts where this table is present.                                                                                                                                                                   |

Each table row can be expanded to view its table variants and the following columns:

| Column         | Description                                                            |
| -------------- | ---------------------------------------------------------------------- |
| Variant ID     | Unique identifier for a variant (version) of this table.               |
| \# Instances   | Number of instances of this table for this variant.                    |
| \# Columns     | Number of unique columns in this table variant.                        |
| Databases      | Alphabetically sorted list of databases containing this table variant. |
| Schemas        | Alphabetically sorted list of schemas containing this table variant.   |
| Database Hosts | Alphabetically sorted list of hosts where this table variant appears.  |

### Viewing table variant details{% #viewing-table-variant-details %}

To view more details about a table variant, click its row to open the table variant panel.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/table-variant-panel.79a45aa88921db2e1bdae95ca892d6d9.png?auto=format"
   alt="Table variant panel showing column definitions and an index for the inventory table" /%}

This panel shows you information about the variant (version), such as:

- **Definition**: Includes columns, indexes, and foreign keys for this table variant.
- **Table Instances**: All instances associated with this table variant.
- **Metrics**: Table size, sequential scans, and other related metrics (last 7 days by default).
- **Queries**: Queries involving this table variant (last 7 days by default).
- **Changes**: Schema changes affecting this table variant (last 7 days by default).

### Viewing table instance details{% #viewing-table-instance-details %}

To view details for a specific table instance, go to the **Table Instances** tab in the table variant panel and click on a row.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/table-instance-details.df7d2102bbce29724df2231cd5496c5c.png?auto=format"
   alt="Table instance panel displaying column and index details for the inventory table." /%}

This opens a view similar to the table variant panel, showing the following information for the selected table instance:

- **Definition**: Includes columns, indexes, and foreign keys for this table instance.
- **Metrics**: Table size, sequential scans, and other related metrics (last 7 days by default).
- **Queries**: Queries involving this table instance (last 7 days by default).
- **Changes**: Schema changes affecting this table instance (last 7 days by default).

## Recommendations{% #recommendations %}

Recommendations highlight potential opportunities for schema optimization across your tables.

Each recommendation includes:

- A detected issue, such as a missing primary key or an inefficient index.
- An explanation of why the issue matters and how it impacts database performance or integrity.
- A suggested fix, often an SQL statement that can be executed on the affected database.

Recommendations are available in aggregate (at the top of the page) and per table, with each applicable table showing its corresponding recommendations. For more information, see [Recommendations](https://docs.datadoghq.com/database_monitoring/recommendations).

## Metrics overview{% #metrics-overview %}

The Metrics overview displays dashboards for metrics associated with tracked tables across each DBMS.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/metrics-overview.ebe7df62cac39691d4f697146c4a73af.png?auto=format"
   alt="Metrics overview showing total table instance count and key activity metrics across tracked database instances" /%}

Each dashboard includes the following metrics:

- Total Table Instance Count
- Fastest Changing Instances (%)
- Fastest Changes Instances (bytes)
- Most Accessed Instances
- Largest Instances
- Instances with Most Live Rows
- Instances with the Largest Index Sizes
- Instances with Access Exclusive Locks
- Instances with Most Dead Rows
- Instances with the Longest Last Vacuum Age
- Instances with the Longest Last Auto Vacuum Age
