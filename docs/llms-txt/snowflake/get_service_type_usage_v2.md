# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_service_type_usage_v2.md

# <budget_name>!GET_SERVICE_TYPE_USAGE_V2

View the credit usage for a [budget](../../../../user-guide/budgets.md) by service type.

## Syntax

```sqlsyntax
<budget_name>!GET_SERVICE_TYPE_USAGE_V2( '<start_month>' , '<end_month>' )
```

## Arguments

`'start_month'`
:   Specifies the start of the time period for which you want to return usage information. Specified in the format `YYYY-MM`.

`'end_month'`
:   Specifies the end of the time period for which you want to return usage information. Specified in the format `YYYY-MM`.

## Returns

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_TYPE | VARCHAR | Lists the [service](../../../../user-guide/budgets.md) that used credits. |
| ENTITY_TYPE | VARCHAR | Type of object associated with the credit consumption. All table-like objects such as tables, views, materialized views, and external tables have a value of `TABLE`. |
| ENTITY_ID | NUMBER | Internal identifier for the object in the budget. |
| NAME | VARCHAR | Name of the object associated with the credit consumption. |
| CREDITS_USED | FLOAT | Number of credits used. This is the sum of CREDITS_COMPUTE and CREDITS_CLOUD. |
| CREDITS_COMPUTE | FLOAT | Number of compute credits used. |
| CREDITS_CLOUD | FLOAT | Number of cloud service credits used. |

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

## Example

Return credits consumed by objects associated with the budget `my_budget` in January, February, and March of 2025:

```sqlexample
CALL db.sch1.my_budget!GET_SERVICE_TYPE_USAGE_V2('2025-01', '2025-03');
```
