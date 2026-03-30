# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/set_email_notifications.md

# <budget_name>!SET_EMAIL_NOTIFICATIONS

Set the email addresses to receive [budgets](../../../../user-guide/budgets.md) notifications.

See also:
:   [<budget_name>!GET_NOTIFICATION_EMAIL](get_notification_email.md),
    [<budget_name>!GET_NOTIFICATION_INTEGRATION_NAME](get_notification_integration_name.md),
    [<budget_name>!GET_NOTIFICATION_MUTE_FLAG](get_notification_mute_flag.md),
    [<budget_name>!SET_NOTIFICATION_MUTE_FLAG](set_notification_mute_flag.md)

## Syntax

```sqlsyntax
<budget_name>!SET_EMAIL_NOTIFICATIONS( [ '<notification_integration>', ]
                                       '<email> [ , <email> [ , ... ] ]' )
```

## Required arguments

`'email [ , email [ , ... ] ]'`
:   Specifies the email addresses to receive budget notification emails. Each email address in the list must be
    [verified](../../../../user-guide/notifications/email-notifications.md).

## Optional arguments

`'notification_integration'`
:   Specifies the identifier for the [email notification integration](../../../../user-guide/notifications/email-notifications.md).

    If the ALLOWED_RECIPIENTS parameter is set for the notification integration, each `email` in the notifications list
    must be included in the ALLOWED_RECIPIENTS list for the notification integration. Otherwise, you can include any verified
    email address in the notifications list.

## Returns

```output
The email integration is updated.
```

## Access control requirements

* The following minimum privileges and roles are required to call this method for *custom budgets*:

  * ADMIN [instance role](../../../../user-guide/budgets.md) for the budget instance.
  * USAGE privilege on the database and schema that contains the budget instance.
* The minimum role required to call this method for the *account budget* is the BUDGET_ADMIN
  [application role](../../../../user-guide/budgets.md).

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

* Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
  return value of this method. Instead, call each method in a separate SQL statement.
* If you are using a notification integration, the USAGE privilege on the notification integration must be granted to
  APPLICATION SNOWFLAKE:

  ```sqlexample
  GRANT USAGE ON INTEGRATION budgets_notification_integration
    TO APPLICATION SNOWFLAKE;
  ```

## Examples

Send email notifications for budget `my_budget` in the `budgets_db.budgets_schema` schema to
[costadmin@domain.com](mailto:costadmin%40domain.com) and [budgetadmin@domain.com](mailto:budgetadmin%40domain.com):

```sqlexample
CALL budgets_db.budgets_schema.my_budget!SET_EMAIL_NOTIFICATIONS(
   'costadmin@domain.com, budgetadmin@domain.com');
```

Send email notifications for the account budget to [budgetadmin@domain.com](mailto:budgetadmin%40domain.com):

```sqlexample
CALL snowflake.local.account_root_budget!SET_EMAIL_NOTIFICATIONS(
   'budgets_notification', 'budgetadmin@domain.com');
```

## Error messages

For a list of common error messages and their causes and solutions, see [You can’t set email notifications for a budget](../../../../user-guide/budgets/troubleshoot.md).
