# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_notification_mute_flag.md

# <budget_name>!GET_NOTIFICATION_MUTE_FLAG

View the status of the notification mute flag for a [budget](../../../../user-guide/budgets.md). If the mute
flag is set to TRUE, no notifications are sent about the budget’s spending limit.

See also:
:   [<budget_name>!GET_NOTIFICATION_EMAIL](get_notification_email.md),
    [<budget_name>!GET_NOTIFICATION_INTEGRATION_NAME](get_notification_integration_name.md),
    [<budget_name>!SET_EMAIL_NOTIFICATIONS](set_email_notifications.md),
    [<budget_name>!SET_NOTIFICATION_MUTE_FLAG](set_notification_mute_flag.md)

## Syntax

```sqlsyntax
<budget_name>!GET_NOTIFICATION_MUTE_FLAG()
```

## Returns

* `TRUE` if notifications are disabled.
* `FALSE` if notifications are enabled.

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

View the state of the notification mute flag for `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_NOTIFICATION_MUTE_FLAG();
```

View the state of the notification mute flag for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_NOTIFICATION_MUTE_FLAG();
```
