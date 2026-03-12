# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/deactivate.md

# account_root_budget!DEACTIVATE

Deactivate the account [budget](../../../../user-guide/budgets.md).

See also:
:   [account_root_budget!ACTIVATE](activate.md)

## Syntax

```sqlsyntax
CALL account_root_budget!DEACTIVATE()
```

## Returns

```output
Deactivated!
```

## Access control requirements

The role used to call this method must be granted the following role and privilege:

* BUDGET_ADMIN [application role](../../../../user-guide/budgets.md)
* [Snowflake database role](../../../snowflake-db-roles.md) USAGE_VIEWER

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* After you deactivate the account budget, you can no longer create new custom budgets using Snowsight.
  However, you can continue to create custom budgets using SQL.
* This method is only available on the account budget. Custom budgets can’t be deactivated. They must be dropped using
  the [DROP BUDGET](../commands/drop-budget.md) command.
* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.

## Example

Deactivate the account budget for your account:

```sqlexample
CALL snowflake.local.account_root_budget!DEACTIVATE();
```
