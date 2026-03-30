# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/query_acceleration_eligible.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/query_acceleration_eligible.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# QUERY_ACCELERATION_ELIGIBLE view

This Account Usage view can be used to identify queries that are eligible for the
[query acceleration service](../../user-guide/query-acceleration-service.md) (QAS).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| QUERY_ID | VARCHAR | Internal/system-generated identifier for the SQL statement. |
| QUERY_TEXT | VARCHAR | Text of the SQL statement. |
| START_TIME | TIMESTAMP_LTZ | Statement start time. |
| END_TIME | TIMESTAMP_LTZ | Statement end time. |
| WAREHOUSE_NAME | VARCHAR | Name of the warehouse that the query executed on. |
| WAREHOUSE_SIZE | VARCHAR | Size of the warehouse when this statement executed. |
| ELIGIBLE_QUERY_ACCELERATION_TIME | NUMBER | Amount of query execution time (in seconds) eligible for the query acceleration service. |
| UPPER_LIMIT_SCALE_FACTOR | NUMBER | Upper limit [scale factor](../sql/create-warehouse.md) for the given query. |
| QUERY_HASH | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the canonicalized SQL text. |
| QUERY_HASH_VERSION | NUMBER | The [version of the logic](../../user-guide/query-hash.md) used to compute `QUERY_HASH`. |
| QUERY_PARAMETERIZED_HASH | VARCHAR | The [hash value](../../user-guide/query-hash.md) computed based on the parameterized query. |
| QUERY_PARAMETERIZED_HASH_VERSION | NUMBER | The [version of the logic](../../user-guide/query-hash.md) used to compute `QUERY_PARAMETERIZED_HASH`. |
|  |  |  |

## Usage notes

* Latency for the view may be up to 180 minutes (three hours).

* Query acceleration is supported for the following SQL commands:

  > * SELECT
  > * INSERT
  > * CREATE TABLE AS SELECT (CTAS)
  > * COPY INTO <table>

  For more information about query eligibility, see [Eligible queries](../../user-guide/query-acceleration-service.md).
* This view only includes eligible queries that have *not* been accelerated. If you have enabled
  the query acceleration service and previously QAS-eligible queries are now accelerated, they
  are not included in this view.

## Examples

Identify the warehouses with the most queries eligible in a given period of time for the query acceleration service:

```sqlexample
SELECT warehouse_name, COUNT(query_id) AS num_eligible_queries
  FROM SNOWFLAKE.ACCOUNT_USAGE.QUERY_ACCELERATION_ELIGIBLE
  WHERE start_time >= '2024-06-01 00:00'::TIMESTAMP
  AND end_time <= '2024-06-07 00:00'::TIMESTAMP
  GROUP BY warehouse_name
  ORDER BY num_eligible_queries DESC;
```

For more example queries, see [Identifying queries and warehouses with the QUERY_ACCELERATION_ELIGIBLE view](../../user-guide/query-acceleration-service.md).
