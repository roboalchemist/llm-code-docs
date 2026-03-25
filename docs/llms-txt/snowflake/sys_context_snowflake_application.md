# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context_snowflake_application.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)

Returns information about the context in which a statement is executed within a
[Snowflake Native App](../../developer-guide/native-apps/native-apps-about.md).

You can call this function in the following contexts:

* A stored procedure or Streamlit app that is configured to use
  [owner’s rights](../../developer-guide/native-apps/restricted-callers-rights.md) and is within or owned by a Snowflake Native App.
* A UDF, view, or policy that is owned by a Snowflake Native App.
* A UDF, view, or policy that is part of the [shared data content](../../developer-guide/native-apps/preparing-data-content.md) of a
  Snowflake Native App.

In any other context, the function returns NULL.

See also:
:   [SYS_CONTEXT](sys_context.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)](sys_context_snowflake_environment.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)](sys_context_snowflake_organization_session.md) ,
    [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md) ,
    [IS_APPLICATION_ROLE_ACTIVATED (SYS_CONTEXT function)](is_application_role_activated.md)

## Syntax

**Syntax for retrieving properties:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$APPLICATION' ,
  '<property>'
)
```

**Syntax for calling functions:**

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$APPLICATION' ,
  '<function>' , '<argument>' [ , ... ]
)
```

## Arguments

`'SNOWFLAKE$APPLICATION'`
:   Specifies that you want to retrieve a property or call a function to return context information about the application in which
    the function is called.

`'property'`
:   Name of the property that you want to retrieve. You can specify the following properties:

    | Property | Description |
    | --- | --- |
    | `NAME` | Name of the application. |
    | `CURRENT_VERSION` | Current version of the application in which the current SQL statement is executed.  The value of the `CURRENT_VERSION` property can differ from the `INSTALLED_VERSION` property in the following situations:   * The SQL statement is executed in a [setup script](../../developer-guide/native-apps/creating-setup-script.md) that   upgrades the application to a new version.  In this case, `CURRENT_VERSION` is the new version, and `INSTALLED_VERSION` is the currently installed version that   is being upgraded. * A long-running procedure or query started executing before an upgrade completed.  In this case, `CURRENT_VERSION` is the version when the procedure or query started executing, and   `INSTALLED_VERSION` is the version after the upgrade completed. |
    | `CURRENT_PATCH` | Current patch number of the application in which the current SQL statement is executed. |
    | `INSTALLED_VERSION` | Installed version of the application in which the current SQL statement is executed. |
    | `INSTALLED_PATCH` | Installed patch number of the application in which the current SQL statement is executed. |
    | `IS_DEV_MODE` | `TRUE` if the application is in [development mode](../../developer-guide/native-apps/installing-testing-application.md); otherwise, `FALSE`.  To compare this value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the value to BOOLEAN. For example:  ```sqlexample SELECT SYS_CONTEXT('SNOWFLAKE$APPLICATION', 'IS_DEV_MODE')::BOOLEAN = TRUE; ``` |

`'function'`
:   Name of the function that you want to call. You can call the following functions:

    * [IS_APPLICATION_ROLE_ACTIVATED (SYS_CONTEXT function)](is_application_role_activated.md)

`'argument' [ , ... ]`
:   Arguments to pass to the function that you want to call.

## Returns

The function returns a VARCHAR value or NULL:

* The return value depends on
  the property that you are retrieving or
  the function that you are calling.
* If you call SYS_CONTEXT with the SNOWFLAKE$APPLICATION namespace outside of
  any of the supported contexts, the function returns NULL.

## Usage notes

* If you are specifying the function call in a double-quoted string in a shell, escape the `$` character with a backslash
  (`\`) so that `$APPLICATION` is not interpreted as a shell variable.

  For example, if you are using Snowflake CLI and you are
  [specifying the SQL statement as a command-line argument](../../developer-guide/snowflake-cli/sql/execute-sql.md) in double
  quotes:

  ```bash
  snow sql --query "SELECT SYS_CONTEXT('SNOWFLAKE\$APPLICATION', 'NAME');"
  ```

## Examples

The following example returns the current version of the application:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$APPLICATION', 'CURRENT_VERSION');
```
