# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_cycle_start_action.md

# <budget_name>!GET_CYCLE_START_ACTION

Returns the [user-defined action](../../../../user-guide/budgets/cycle-start-actions.md) that is triggered when the budget cycle restarts.

See also:
:   [<budget_name>!SET_CYCLE_START_ACTION](set_cycle_start_action.md), [<budget_name>!REMOVE_CYCLE_START_ACTION](remove_cycle_start_action.md)

## Syntax

```sqlsyntax
<budget_name>!GET_CYCLE_START_ACTION()
```

## Returns

The method returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| ACTION_UUID | VARCHAR | Unique identifier for the cycle-start action. |
| PROCEDURE_FQN | VARCHAR | Fully qualified name of the stored procedure. |
| PROCEDURE_ARGS | ARRAY | Array of arguments passed to the stored procedure. |
| ADDED_TIMESTAMP | TIMESTAMP_TZ | Time when the action was added to the budget, in local time zone. |
| LAST_TRIGGERED_TIMESTAMP | TIMESTAMP_TZ | Last time the budget triggered the action, in UTC. |

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

Get the cycle-start action for budget `my_budget` in schema `budget_db.sch1`:

```sqlexample
CALL budget_db.sch1.my_budget!GET_CYCLE_START_ACTION();
```

Get the cycle-start action for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_CYCLE_START_ACTION();
```
