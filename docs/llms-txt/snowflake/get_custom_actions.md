# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_custom_actions.md

# <budget_name>!GET_CUSTOM_ACTIONS

ListS all [custom actions](../../../../user-guide/budgets/custom-actions.md) associated with a budget.

See also:
:   [<budget_name>!ADD_CUSTOM_ACTION](add_custom_action.md), [<budget_name>!REMOVE_CUSTOM_ACTIONS](remove_custom_actions.md)

## Syntax

```sqlsyntax
<budget_name>!GET_CUSTOM_ACTIONS()
```

## Returns

The method returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| ACTION_ID | VARCHAR | Unique identifier for the combination of the stored procedure fully qualified name, array of arguments, threshold, and trigger type. |
| PROCEDURE_FQN | VARCHAR | Fully qualified name of the stored procedure. |
| PROCEDURE_ARGS | ARRAY | Array of arguments passed to the stored procedure. |
| SPEND_STRATEGY | VARCHAR | Whether the custom action is triggered based on projected consumption or actual consumption. Valid values: `PROJECTED` or `ACTUAL`. |
| THRESHOLD | NUMBER | Percentage of the budget limit that triggers the stored procedure. |
| LAST_TRIGGER_ATTEMPT_TIME | TIMESTAMP_TZ | Last time the budget attempted to trigger the action, in UTC. |
| ADDED_TIMESTAMP | TIMESTAMP_TZ | Time when the action was added to the budget, in local time zone. |

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

List all custom actions for budget `my_budget` in schema `budget_db.sch1`:

```sqlexample
CALL budget_db.sch1.my_budget!GET_CUSTOM_ACTIONS();
```

List all custom actions for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_CUSTOM_ACTIONS();
```
