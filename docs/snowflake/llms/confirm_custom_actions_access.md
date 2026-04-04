# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/confirm_custom_actions_access.md

# <budget_name>!CONFIRM_CUSTOM_ACTIONS_ACCESS

Validate that the stored procedures associated with [custom actions](../../../../user-guide/budgets/custom-actions.md) are still valid and that required access control privileges are still granted.

To fix any problems, see [Stored procedure requirements](../../../../user-guide/budgets/custom-actions.md).

See also:
:   [<budget_name>!ADD_CUSTOM_ACTION](add_custom_action.md), [<budget_name>!GET_CUSTOM_ACTIONS](get_custom_actions.md)

## Syntax

```sqlsyntax
<budget_name>!CONFIRM_CUSTOM_ACTIONS_ACCESS()
```

## Returns

The method returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| PROCEDURE_FQN | VARCHAR | Fully qualified name of the stored procedure. |
| IS_VALID | BOOLEAN | If TRUE, the stored procedure is still valid and the SNOWFLAKE application still has the required privileges on the procedure. |
| REASON | VARCHAR | Explanation of why the custom action is no longer valid. |

## Access control requirements

* The following minimum privileges and roles are required to view results for *custom budgets*:

  * Any [instance role](../../../../user-guide/budgets.md) for the budget instance.
  * USAGE privilege on the database and schema that contain the budget instance.
* The following role is required to view results for the *account budget*:

  * Any [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Verify the stored procedures and permissions for budget `my_budget` in schema `budget_db.sch1`:

```sqlexample
CALL budget_db.sch1.my_budget!CONFIRM_CUSTOM_ACTIONS_ACCESS();
```

Verify the stored procedures and permissions for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!CONFIRM_CUSTOM_ACTIONS_ACCESS();
```
