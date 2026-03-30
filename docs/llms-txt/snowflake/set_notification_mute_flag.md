# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/set_notification_mute_flag.md

# <budget_name>!SET_NOTIFICATION_MUTE_FLAG

Enable or disable notifications for a [budget](../../../../user-guide/budgets.md).

See also:
:   [<budget_name>!GET_NOTIFICATION_EMAIL](get_notification_email.md),
    [<budget_name>!GET_NOTIFICATION_INTEGRATION_NAME](get_notification_integration_name.md),
    [<budget_name>!GET_NOTIFICATION_MUTE_FLAG](get_notification_mute_flag.md),
    [<budget_name>!SET_EMAIL_NOTIFICATIONS](set_email_notifications.md)

## Syntax

```sqlsyntax
<budget_name>!SET_NOTIFICATION_MUTE_FLAG( { TRUE | FALSE } );
```

## Arguments

`{ TRUE | FALSE }`
:   *TRUE to disable notifications.
    * FALSE to enable notifications.

    Default: FALSE

## Returns

```output
The notification mute flag has been updated to <true | false>.
```

## Access control requirements

* The following minimum privileges and roles are required to call this method for *custom budgets*:

  * Any [instance role](../../../../user-guide/budgets.md) for the budget instance.
  * USAGE privilege on the database and schema that contains the budget instance.
* The following minimum privileges and roles are required to call this method for the *account budget*:

  Any [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

Disable notifications for budget `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!SET_NOTIFICATION_MUTE_FLAG(TRUE);
```

Enable notifications for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!SET_NOTIFICATION_MUTE_FLAG(FALSE);
```
