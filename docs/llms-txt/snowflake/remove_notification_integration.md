# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/remove_notification_integration.md

# <budget_name>!REMOVE_NOTIFICATION_INTEGRATION

Removes a queue or webhook notification integration from a [custom budget or the account budget](../../../../user-guide/budgets.md).

See also:
:   [<budget_name>!ADD_NOTIFICATION_INTEGRATION](add_notification_integration.md),
    [<budget_name>!GET_NOTIFICATION_INTEGRATIONS](get_notification_integrations.md)

## Syntax

```sqlsyntax
<budget_name>!REMOVE_NOTIFICATION_INTEGRATION( '<integration_name>' )
```

## Arguments

`'integration_name'`
:   The name of the queue or webhook notification integration to remove from the budget.

## Returns

Returns a VARCHAR value that indicates whether or not the notification integration was successfully removed.

* If the notification integration was removed successfully, the method returns `Integration removed successfully`.
* Otherwise, the method returns an error message.

## Access control requirements

The following minimum privileges and roles are required to call this method on a budget:

* ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
* USAGE privilege on the database and schema that contains the budget instance.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Remove the notification integration `budgets_notification_integration` from custom budget `my_budget` in schema
`budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!REMOVE_NOTIFICATION_INTEGRATION(
  'budgets_notification_integration');
```

Remove the notification integration `budgets_notification_integration` from the account budget:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!REMOVE_NOTIFICATION_INTEGRATION(
  'budgets_notification_integration');
```
