# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/remove_custom_actions.md

# <budget_name>!REMOVE_CUSTOM_ACTIONS

Remove one or more [custom actions](../../../../user-guide/budgets/custom-actions.md) from a budget.

See also:
:   [<budget_name>!ADD_CUSTOM_ACTION](add_custom_action.md), [<budget_name>!GET_CUSTOM_ACTIONS](get_custom_actions.md)

## Syntax

```sqlsyntax
<budget_name>!REMOVE_CUSTOM_ACTIONS()

<budget_name>!REMOVE_CUSTOM_ACTIONS( <threshold> )

<budget_name>!REMOVE_CUSTOM_ACTIONS( <threshold>, '<stored_procedure>' )
```

## Arguments

`threshold`
:   Threshold percentage at which custom actions are triggered. If you don’t specify a procedure name, all custom actions set for this threshold
    are removed.

`'stored_procedure'`
:   Fully qualified name of the stored procedure associated with the custom action. Snowflake removes all custom actions that match the
    specified stored procedure and threshold.

    > **Note:**
    >
    > When passing the fully qualified name of the procedure, use the `PROCEDURE_FQN` value from the output of the
    > [GET_CUSTOM_ACTIONS](get_custom_actions.md) method.

## Returns

Returns a VARCHAR value indicating the number of custom actions that were successfully removed.

## Access control requirements

The following privileges and roles are required to call this method for a budget:

* ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
* USAGE privilege on the database and schema that contain the budget instance.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Remove all custom actions from budget `my_budget` in schema `budget_db.sch1`:

```sqlexample
CALL budget_db.sch1.my_budget!REMOVE_CUSTOM_ACTIONS();
```

Remove all custom actions that are triggered when consumption reaches 75% of the budget limit:

```sqlexample
CALL budget_db.sch1.my_budget!REMOVE_CUSTOM_ACTIONS(75);
```

Remove the custom action that calls the `code_db.sch1.my_sp` stored procedure when consumption reaches 75% of the budget limit:

```sqlexample
CALL budget_db.sch1.my_budget!REMOVE_CUSTOM_ACTIONS(75, 'code_db.sch1.my_sp');
```
