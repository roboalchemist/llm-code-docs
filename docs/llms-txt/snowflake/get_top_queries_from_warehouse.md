# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-insights/methods/get_top_queries_from_warehouse.md

# ANOMALY_INSIGHTS!GET_TOP_QUERIES_FROM_WAREHOUSE

Returns the queries in a warehouse that consumed the most credits. Helps investigate
[account-level cost anomalies](../../../../user-guide/cost-anomalies.md) in the current account.

## Syntax

```sqlsyntax
SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_TOP_QUERIES_FROM_WAREHOUSE(
  <warehouse_id>,
  '<date>',
  <number_of_queries> )
```

## Arguments

`warehouse_id`
:   Specifies the internal/system-generated identifier for the warehouse that ran the queries.

    You can find the warehouse ID by calling the [ANOMALY_INSIGHTS!GET_TOP_WAREHOUSES_ON_DATE](get_top_warehouses_on_date.md) method or querying the
    [WAREHOUSE_METERING_HISTORY view](../../../account-usage/warehouse_metering_history.md).

    Data type: NUMBER

`'date'`
:   Specifies the date for which you want to return consumption data.

    Data type: DATE

`number_of_queries`
:   Limits the number of queries returned by the method. For example, if you specify `5`, the method returns only the top five queries in
    terms of credits consumed.

    Data type: NUMBER

## Output

Returns a table with the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| WAREHOUSE_NAME | VARCHAR | Name of the warehouse used to execute the query. |
| CONSUMPTION | NUMBER | Credits consumed by the query. |
| USERNAME | VARCHAR | User who executed the query. |
| QUERY_ID | VARCHAR | Query ID. |
| DURATION_MS | NUMBER | How long it took the query to execute, in milliseconds. |
| START_TIME | DATETIME | Date and time the user started executing the query. |
| QUERY_TAG | VARCHAR | Query tag, if any, applied to the query. |

## Access control requirements

Users with any of the following roles can call this method:

* ACCOUNTADMIN system role
* GLOBALORGADMIN system role
* SNOWFLAKE.APP_USAGE_ADMIN application role
* SNOWFLAKE.APP_USAGE_VIEWER application role

## Usage notes

* This method returns consumption data for the current account. It cannot be used to return data for other accounts or the entire
  organization.
* You cannot use this method to return a currency as the unit of measure for the consumption.

## Example

Returns the top six queries that consumed the most credits on December 1, 2024, using a warehouse whose Warehouse ID is `838`.

```sqlexample
CALL SNOWFLAKE.LOCAL.ANOMALY_INSIGHTS!GET_TOP_QUERIES_FROM_WAREHOUSE(838, '2024-12-01', 6);
```
