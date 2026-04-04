# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_refresh_tier.md

# <budget_name>!GET_REFRESH_TIER

Retrieves the current [refresh interval of a budget](../../../../user-guide/budgets.md). The budget refresh interval controls how long it takes for a
budget to be refreshed with the most current consumption data.

See also:
:   [<budget_name>!SET_REFRESH_TIER](set_refresh_tier.md)

## Syntax

```sqlsyntax
<budget_name>!GET_REFRESH_TIER()
```

## Returns

Returns one of the following VARCHAR values:

* `'TIER_1H'` — The budget refresh interval is one hour.
* `'TIER_6H'` — The budget refresh interval is up to 6.5 hours.

## Access control requirements

* The following minimum privileges and roles are required to view results for *custom budgets*:

  * Any [instance role](../../../../user-guide/budgets.md) for the budget instance.
  * USAGE privilege on the database and schema that contains the budget instance.
* The following role is required to view results for the *account budget*:

  * Any [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

View the refresh interval for budget `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_REFRESH_TIER();
```

View the refresh interval for the account budget:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!GET_REFRESH_TIER();
```
