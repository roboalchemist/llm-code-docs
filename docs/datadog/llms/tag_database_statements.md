# Source: https://docs.datadoghq.com/database_monitoring/guide/tag_database_statements.md

---
title: Tagging SQL Statements
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Database Monitoring > Database Monitoring Guides > Tagging SQL
  Statements
---

# Tagging SQL Statements

This guide assumes that you have configured [Database Monitoring](https://docs.datadoghq.com/database_monitoring/#getting-started).

[Datadog Database Monitoring (DBM)](https://docs.datadoghq.com/database_monitoring/#getting-started) allows you to view explain plans and query samples running on your database hosts. This guide shows you how to add tags as SQL comments to your database queries, which can then be surfaced and leveraged in DBM.

## Before you begin{% #before-you-begin %}

{% dl %}

{% dt %}
Supported databases
{% /dt %}

{% dd %}
Postgres, MySQL, SQL Server
{% /dd %}

{% dt %}
Supported Agent versions
{% /dt %}

{% dd %}
7.36.1+
{% /dd %}

{% dt %}
Supported tagging formats
{% /dt %}

{% dd %}
[sqlcommenter](https://google.github.io/sqlcommenter), [marginalia](https://github.com/basecamp/marginalia)
{% /dd %}

{% /dl %}

## Manual tag injection{% #manual-tag-injection %}

Using any database API supporting execution of SQL statements, add a comment in your statement with tags formatted as per the [sqlcommenter](https://google.github.io/sqlcommenter) or [marginalia](https://github.com/basecamp/marginalia) formats.

```sql
/*key='val'*/ SELECT * from FOO
```

Separate multiple tags with commas:

```sql
/*key1='val1',key2='val2'*/ SELECT * from FOO
```

Full example:

```go
import (
    "database/sql"
)

func main() {
    db, err := sql.Open("postgres", "postgres://pqgotest:password@localhost/pqgotest?sslmode=disable")
    if err != nil {
        log.Fatal(err)
    }

    // Tag SQL statement with key:val
    rows, err := db.Query("/*key='val'*/ SELECT * from FOO")
    if err != nil {
        log.Fatal(err)
    }
    defer rows.Close()
}
```

## Explore the tags in DBM{% #explore-the-tags-in-dbm %}

On the [Samples page](https://app.datadoghq.com/databases/samples), filter the **Explain Plans** and **Query Samples** views by custom tag.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_filter_explain_plans_by_custom_tag.599af133f35fc32e688b5c0792f2b049.png?auto=format"
   alt="Filter explain plans by custom tag." /%}

You can also view a timeseries of explain plan costs filtered by tag.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_timeseries_by_custom_tag.9504f338fcc37e1e80032aaab68f0828.png?auto=format"
   alt="Explain plan cost by custom tag." /%}

When you select a query, the custom tags are shown on the **Sample Details** page under Propagated Tags.

{% image
   source="https://datadog-docs.imgix.net/images/database_monitoring/dbm_explain_plan_with_custom_tags.8eaa3d6d5a94508ed2282b9a2ec00520.png?auto=format"
   alt="View custom tags on explain plans." /%}
