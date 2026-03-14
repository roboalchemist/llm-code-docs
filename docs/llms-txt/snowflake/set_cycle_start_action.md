# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/set_cycle_start_action.md

# <budget_name>!SET_CYCLE_START_ACTION

Associates a stored procedure with a budget so that the procedure is called when the budget cycle restarts. The procedure must be associated by [reference](../../../references.md).

For more information, see [Cycle-start actions for budgets](../../../../user-guide/budgets/cycle-start-actions.md).

## Syntax

```sqlsyntax
<budget_name>!SET_CYCLE_START_ACTION (
  { '<stored_procedure_reference>' | <reference_statement> },
  { <array_of_arguments> | <array_construct_statement> } )
```

## Arguments

`'stored_procedure_reference'`
:   The serialized string representation that resolves to a procedure. This string is the output of
    the [SYSTEM$REFERENCE](../../../functions/system_reference.md) function.

`reference_statement`
:   A [SYSTEM$REFERENCE](../../../functions/system_reference.md) statement that creates a reference for the procedure to be associated with the budget.

`array_of_arguments`
:   Array of arguments to pass to the stored procedure.

`array_construct_statement`
:   An [ARRAY_CONSTRUCT](../../../functions/array_construct.md) statement that returns an array constructed from zero, one, or more
    inputs.

## Returns

Returns a VARCHAR value that indicates whether or not the procedure was successfully associated with the budget.

If the procedure could not be associated with the budget, the method returns an error message.

## Access control requirements

The following privileges and roles are required to call this method for a budget:

* ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
* USAGE privilege on the database and schema that contain the budget instance.
* USAGE privilege on the database and schema that contain the stored procedure.
* USAGE privilege on the stored procedure.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Associate the `reset_resources` stored procedure with the `budget_db.sch1.my_budget` budget so that it is
called when the budget cycle restarts:

```sqlexample
CALL budget_db.sch1.my_budget!SET_CYCLE_START_ACTION(
  SYSTEM$REFERENCE('PROCEDURE', 'code_db.sch1.reset_resources(STRING, STRING)'),
  ARRAY_CONSTRUCT('admin@example.com', 'Budget cycle restarted'));
```

Associate the `enable_access` stored procedure with the `budget_db.sch1.my_budget` budget so that it is called when
the budget cycle restarts:

```sqlexample
CALL budget_db.sch1.my_budget!SET_CYCLE_START_ACTION(
  SYSTEM$REFERENCE('PROCEDURE', 'code_db.sch1.enable_access(STRING)'),
  ARRAY_CONSTRUCT('Re-enable resources for new budget cycle'));
```
