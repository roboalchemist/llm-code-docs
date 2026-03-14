# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_spending_history.md

# <budget_name>!GET_SPENDING_HISTORY

View the spending history for a [budget](../../../../user-guide/budgets.md).

See also:
:   [<budget_name>!GET_SERVICE_TYPE_USAGE](get_service_type_usage.md)

## Syntax

```sqlsyntax
<budget_name>!GET_SPENDING_HISTORY( [ TIME_LOWER_BOUND => <constant_expr> ,
                                      TIME_UPPER_BOUND => <constant_expr> ] )
```

## Optional arguments

`TIME_LOWER_BOUND => constant_expr,` . `TIME_UPPER_BOUND => constant_expr`
:   Time range (in UTC timestamp format) during which the spending occurred.

    You must set both lower and upper time bounds to limit the results by a time range.

## Returns

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| MEASUREMENT_DATE | DATE | Date when the usage occurred. |
| SERVICE_TYPE | VARCHAR | [Type of service](../../../../user-guide/budgets.md) that is consuming credits, which can be one of the following:   *`AUTO_CLUSTERING`* `DATA_QUALITY_MONITORING` *`HYBRID_TABLE_REQUESTS`* `MATERIALIZED_VIEW` *`PIPE`* `QUERY_ACCELERATION` *`SEARCH_OPTIMIZATION`* `SERVERLESS_ALERTS` *`SERVERLESS_TASK`* `SNOWPIPE_STREAMING` *`WAREHOUSE_METERING`* `WAREHOUSE_METERING_READER` |
| CREDITS_SPENT | FLOAT | Number of credits used. |

## Access control requirements

* The following minimum privileges and roles are required to view results for *custom budgets*:

  * Any [instance role](../../../../user-guide/budgets.md) for the budget instance.
  * USAGE privilege on the database and schema that contains the budget instance.
  * [Snowflake database role](../../../snowflake-db-roles.md) USAGE_VIEWER.
* The following role is required to view results for the *account budget*:

  * Any [application role](../../../../user-guide/budgets.md) for the account budget.
  * [Snowflake database role](../../../snowflake-db-roles.md) USAGE_VIEWER.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

View the spending history for budget `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_SPENDING_HISTORY();
```

View the spending history for the last 7 days for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_SPENDING_HISTORY(
  TIME_LOWER_BOUND=>dateadd('days', -7, current_timestamp()),
  TIME_UPPER_BOUND=>current_timestamp()
);
```
