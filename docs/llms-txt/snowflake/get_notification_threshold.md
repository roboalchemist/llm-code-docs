# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_notification_threshold.md

# <budget_name>!GET_NOTIFICATION_THRESHOLD

Returns the notification threshold for a [budget](../../../../user-guide/budgets.md). Notifications are sent when Snowflake predicts that spending
will exceed the threshold, which is a percentage of the budget limit.

## Syntax

```sqlsyntax
<budget_name>!GET_NOTIFICATION_THRESHOLD();
```

## Returns

Returns a VARCHAR value containing the notification threshold percentage.

## Access control requirements

The following minimum privileges and roles are required to call this method for *custom budgets*:

> * Any [instance role](../../../../user-guide/budgets.md) for the budget instance.
> * USAGE privilege on the database and schema that contains the budget instance.

The following minimum privileges and roles are required to call this method for the *account budget*:

> * Any [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Get the notification threshold for budget `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_NOTIFICATION_THRESHOLD();
```

Get the notification threshold for the account budget:

```sqlexample
CALL SNOWFLAKE.LOCAL.ACCOUNT_ROOT_BUDGET!GET_NOTIFICATION_THRESHOLD();
```
