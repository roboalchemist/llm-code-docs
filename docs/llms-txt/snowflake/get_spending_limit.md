# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_spending_limit.md

# <budget_name>!GET_SPENDING_LIMIT

View the spending limit for a [budget](../../../../user-guide/budgets.md).

See also:
:   [<budget_name>!SET_SPENDING_LIMIT](set_spending_limit.md)

## Syntax

```sqlsyntax
<budget_name>!GET_SPENDING_LIMIT()
```

## Returns

* The number of credits set as the spending limit for the budget.
* `-1` if the spending limit is not set.

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

View the spending limit for budget `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_SPENDING_LIMIT();
```

View the spending limit for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_SPENDING_LIMIT();
```
