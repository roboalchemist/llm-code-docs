# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/activate.md

# account_root_budget!ACTIVATE

Activate the account budget. You must activate the account budget in order
to use the [budgets](../../../../user-guide/budgets.md) feature.

See also:
:   [account_root_budget!DEACTIVATE](deactivate.md)

## Syntax

```sqlsyntax
CALL account_root_budget!ACTIVATE()
```

## Returns

```output
activated
```

## Access control requirements

Only a user with the ACCOUNTADMIN role or a role granted the following privileges can activate the account budget:

* Application role SNOWFLAKE.BUDGET_ADMIN
* [Snowflake database role](../../../snowflake-db-roles.md) USAGE_VIEWER

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* After the account budget is activated:

  * You must set the spending limit in order for the budget to start tracking credit usage.
  * You must [set up notifications for the budget](../../../../user-guide/budgets/notifications.md). If you do not set up notifications
    for the budget, no notifications will be sent out.
* This method is only available on the account budget. Custom budgets do not require activation.
* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.

## Example

Activate the account budget for your account:

```sqlexample
CALL snowflake.local.account_root_budget!ACTIVATE();
```

## Error messages

To troubleshoot issues with account budget activation, see [You can’t activate the account budget](../../../../user-guide/budgets/troubleshoot.md).
