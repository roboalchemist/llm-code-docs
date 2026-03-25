# Source: https://docs.snowflake.com/en/sql-reference/classes/budget/methods/get_config.md

# <budget_name>!GET_CONFIG

View the configuration properties for a [budget](../../../../user-guide/budgets.md).

## Syntax

```sqlsyntax
<budget_name>!GET_CONFIG()
```

## Returns

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| NOTIFICATION_EMAIL | VARCHAR | The email address(es) that receive budget notifications. If there is more than one email address, the function returns a comma-separated list. |
| LAST_NOTIFICATION_TIME | NUMBER | UTC timestamp when the last notification was sent. If no notifications were sent out yet, the value in this column is `-1`. |
| SPEND_LIMIT | NUMBER | The spending limit (in credits) for the budget. |
| NOTIFICATION_MUTE_FLAG | BOOLEAN | TRUE if notifications are muted for the budget. |
| BUDGET_TYPE | VARCHAR | Type of budget. Valid values are: `ACCOUNT_ROOT_BUDGET` or `USER_BUDGET` |
| IS_ACTIVE | BOOLEAN | TRUE if the account budget has been activated.  *This column is only available for the account budget.* |
| ACTIVATION_TIMESTAMP | TIMESTAMP_TZ | Date and time the account budget was activated.  *This column is only available for the account budget.* |

## Access control requirements

* The following minimum privileges and roles are required to view results for *custom budgets*:

  * Any [instance role](../../../../user-guide/budgets.md) for the budget.
  * USAGE privilege on the database and schema that contains the budget instance.
* The following role is required to view results for the *account budget*:

  Any [application role](../../../../user-guide/budgets.md) for the account budget.

For more information, see [Budgets roles and privileges](../../../../user-guide/budgets.md).

## Usage notes

Calling this method does not return the object. Because of this, you can’t use method chaining to call another method on the
return value of this method. Instead, call each method in a separate SQL statement.

## Examples

View the budget configuration properties for `my_budget` in schema `budget_db.budget_schema`:

```sqlexample
CALL budget_db.budget_schema.my_budget!GET_CONFIG();
```

View the budget configuration properties for the account budget:

```sqlexample
CALL snowflake.local.account_root_budget!GET_CONFIG();
```
