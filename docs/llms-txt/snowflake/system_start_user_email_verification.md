# Source: https://docs.snowflake.com/en/sql-reference/functions/system_start_user_email_verification.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$START_USER_EMAIL_VERIFICATION

Starts the [email verification process for a user](../../user-guide/notifications/email-notifications.md). The system sends a verification email to the user’s email address.

## Syntax

```sqlsyntax
SYSTEM$START_USER_EMAIL_VERIFICATION( '<user_name>' )
```

## Arguments

`'user_name'`
:   Name of the user.

## Access control requirements

Only the specified user or the role with the OWNERSHIP privilege on that user can call this function.

## Usage notes

* `user_name` is a string literal that must be enclosed in single quotes.

  If the user name is [case-sensitive or includes any special characters or spaces](../identifiers-syntax.md), you must enclose the name in double quotes, and then enclose the resulting double-quoted name in single quotes. For example:

  ```sqlexample
  SELECT SYSTEM$START_USER_EMAIL_VERIFICATION(
    '"Case-Sensitive UserName"');
  ```

## Examples

Start email verification for a user when the user name follows the rules for [unquoted object identifiers](../identifiers-syntax.md):

```sqlexample
SELECT SYSTEM$START_USER_EMAIL_VERIFICATION('user_name');
```

Start email verification for a user with a case-sensitive name:

```sqlexample
SELECT SYSTEM$START_USER_EMAIL_VERIFICATION('"UserName"');
```
