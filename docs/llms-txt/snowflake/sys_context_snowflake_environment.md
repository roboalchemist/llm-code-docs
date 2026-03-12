# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context_snowflake_environment.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)

Returns information about the environment (the client, current account, and current region) in which the function is called.

See also:
:   [SYS_CONTEXT](sys_context.md) ,
    [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)](sys_context_snowflake_organization_session.md) ,
    [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$ENVIRONMENT' ,
  '<property>'
)
```

## Arguments

`'SNOWFLAKE$ENVIRONMENT'`
:   Specifies that you want to retrieve a property to return context information about the environment in which the function is
    called.

`'property'`
:   Name of the property that you want to retrieve. You can specify the following properties:

    | Property | Description |
    | --- | --- |
    | `CLIENT` | Name and version of the client, driver, or library used to call the function.  If this function is called in Snowsight, the function returns the name and version of the Go Snowflake Driver.  If this function is called in Snowflake CLI, the function returns the name and version of the Snowflake Connector for Python.  The value of this property is the same as the return value of the [CURRENT_CLIENT](current_client.md) function. |
    | `ACCOUNT` | The [account locator](../../user-guide/admin-account-identifier.md) of the account for the current session.  The value of this property is the same as the return value of the [CURRENT_ACCOUNT](current_account.md) function. |
    | `REGION` | The name of the [region](../../user-guide/intro-regions.md) of the account for the current session.  For organizations that have accounts in multiple [region groups](../../user-guide/admin-account-identifier.md), the value of the property is `region_group.region`.  The value of this property is the same as the return value of the [CURRENT_REGION](current_region.md) function. |

## Returns

The function returns a VARCHAR value.

## Usage notes

* If you are specifying the function call in a double-quoted string in a shell, escape the `$` character with a backslash
  (`\`) so that `$ENVIRONMENT` is not interpreted as a shell variable.

  For example, if you are using Snowflake CLI and you are
  [specifying the SQL statement as a command-line argument](../../developer-guide/snowflake-cli/sql/execute-sql.md) in double
  quotes:

  ```bash
  snow sql --query "SELECT SYS_CONTEXT('SNOWFLAKE\$ENVIRONMENT', 'CLIENT');"
  ```

## Examples

The following example returns the name and version of the client used to execute the command:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ENVIRONMENT', 'CLIENT');
```

The following example returns the account locator of the account for the current session:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ENVIRONMENT', 'ACCOUNT');
```

The following example returns the region of the account for the current session:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$ENVIRONMENT', 'REGION');
```
