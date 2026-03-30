# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context_snowflake_organization_session.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)

Returns information about the session in which the function is called and the current organization user.

You can call this function in the following contexts:

* You can call this function directly in the current session.
* You can run a caller’s rights executable (for example, a caller’s rights stored procedure) that calls this function.
* You can run an owner’s rights executable (for example, an owner’s rights stored procedure) that calls this function, provided
  that:

  * The owner role has been granted the READ SESSION privilege on the account.
  * The account containing the owner role is the same organization as the current account for the session.

In any other context, the function returns NULL.

See also:
:   [SYS_CONTEXT](sys_context.md) ,
    [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)](sys_context_snowflake_environment.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md)

## Syntax

**Syntax for retrieving properties:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$ORGANIZATION_SESSION' ,
  '<property>'
)
```

## Arguments

`'SNOWFLAKE$ORGANIZATION_SESSION'`
:   Specifies that you want to retrieve a property or call a function to return information about the session in which the function
    is called, when the current account is in an organization.

`'property'`
:   Name of the property that you want to retrieve. You can specify the following properties:

    | Property | Description |
    | --- | --- |
    | `PRINCIPAL_NAME` | Name of the principal (the [organization user](../../user-guide/organization-users.md)) that started the session.  If the current user is not an organization user, the value of this property is NULL. |

## Returns

The function returns a VARCHAR value or NULL:

* The return value depends on
  the property that you are retrieving.
* If you call SYS_CONTEXT with the SNOWFLAKE$ORGANIZATION_SESSION namespace outside of
  any of the supported contexts, the function returns NULL.

## Usage notes

* If you are specifying the function call in a double-quoted string in a shell, escape the `$` character with a backslash
  (`\`) so that `$ORGANIZATION_SESSION` is not interpreted as a shell variable.

  For example, if you are using Snowflake CLI and you are
  [specifying the SQL statement as a command-line argument](../../developer-guide/snowflake-cli/sql/execute-sql.md) in double
  quotes:

  ```bash
  snow sql --query "SELECT SYS_CONTEXT('SNOWFLAKE\$ORGANIZATION_SESSION', 'PRINCIPAL_NAME');"
  ```

## Examples

The following example returns the name of the organization user for the current session:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ORGANIZATION_SESSION', 'PRINCIPAL_NAME');
```

```output
+-----------------------------------------------------------------+
| SYS_CONTEXT('SNOWFLAKE$ORGANIZATION_SESSION', 'PRINCIPAL_NAME') |
|-----------------------------------------------------------------|
| my_organization_user_name                                       |
+-----------------------------------------------------------------+
```
