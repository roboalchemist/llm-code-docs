# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.athena_named_query.dataset.md

---
title: Athena Named Query
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Athena Named Query
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.athena_named_query.dataset/index.html
---

# Athena Named Query

Athena Named Query in AWS is a saved SQL query that you can create and reuse within Amazon Athena. It allows you to store commonly used queries for quick access, making it easier to run analyses without rewriting SQL each time. Named Queries can be shared with others in your account, helping standardize query logic and improve collaboration.

```
aws.athena_named_query
```

## Fields

| Title          | ID   | Type   | Data Type                                                | Description |
| -------------- | ---- | ------ | -------------------------------------------------------- | ----------- |
| _key           | core | string |
| account_id     | core | string |
| database       | core | string | The database to which the query belongs.                 |
| description    | core | string | The query description.                                   |
| name           | core | string | The query name.                                          |
| named_query_id | core | string | The unique identifier of the query.                      |
| query_string   | core | string | The SQL statements that make up the query.               |
| tags           | core | hstore |
| work_group     | core | string | The name of the workgroup that contains the named query. |
