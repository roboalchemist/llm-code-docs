# Source: https://docs.snowflake.com/en/sql-reference/functions/sys_context.md

Categories:
:   [Context functions](../functions-context.md) (General)

# SYS_CONTEXT

Returns information about the context in which the function is called.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ENVIRONMENT namespace)](sys_context_snowflake_environment.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION namespace)](sys_context_snowflake_organization.md) ,
    [SYS_CONTEXT (SNOWFLAKE$ORGANIZATION_SESSION namespace)](sys_context_snowflake_organization_session.md) ,
    [SYS_CONTEXT (SNOWFLAKE$SESSION namespace)](sys_context_snowflake_session.md)

## Syntax

**Syntax for retrieving properties:**

```sqlsyntax
SYS_CONTEXT(
  '<namespace>' ,
  '<property>'
)
```

**Syntax for calling functions:**

```sqlsyntax
SYS_CONTEXT(
  '<namespace>' ,
  '<function>' , '<argument>' [ , ... ]
)
```

## Arguments

`'namespace'`
:   Namespace of the property that you want to retrieve or the function that you want to call. You can specify one of the following
    namespaces:

    | Namespace | Description |
    | --- | --- |
    | [SNOWFLAKE$APPLICATION](sys_context_snowflake_application.md) | Properties and functions providing context around the application in which the function is called. |
    | [SNOWFLAKE$ENVIRONMENT](sys_context_snowflake_environment.md) | Properties providing context around the environment in which the function is called. These properties include information about:   * The client, driver, or library that is used to call the function. * The account associated with the session in which the function is called. * The region of that account. |
    | [SNOWFLAKE$ORGANIZATION](sys_context_snowflake_organization.md) | Functions providing context around the current organization. |
    | [SNOWFLAKE$ORGANIZATION_SESSION](sys_context_snowflake_organization_session.md) | Properties providing context around the session in which the function is called, when the current account is in an organization. |
    | [SNOWFLAKE$SESSION](sys_context_snowflake_session.md) | Properties and functions providing context around the session in which the function is called. |

`'property'`
:   Name of the property that you want to retrieve. The properties that you can specify depend on the namespace. See the
    documentation for a namespace for the list of properties that you can specify.

`'function'`
:   Name of the function that you want to call. The functions that you can call depend on the namespace. See the
    documentation for a namespace for the list of functions that you can call.

`'argument' [ , ... ]`
:   Arguments to pass to the function that you want to call.

## Returns

The function returns a VARCHAR value or NULL.

* The return value depends on the property that you are retrieving or the function that you are calling.

  See the documentation for each namespace for information about the properties and
  return values of functions in that namespace.
* The function returns NULL if:

  * The namespace is not accessible from within the context of the function call. For example, attempting to access properties in
    the SNOWFLAKE$APPLICATION namespace returns NULL if you are calling the function outside of application code.
  * The value of the property or the return value of the function call is NULL or non-existent.

Some properties and functions return Boolean values as the string `TRUE` or `FALSE`. To compare this return value against the
BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_ROLE_ACTIVATED', 'MY_CUSTOM_ROLE')::BOOLEAN = TRUE;
```

```output
+-----------------------------------------------------------------------------------------+
| SYS_CONTEXT('SNOWFLAKE$SESSION', 'IS_ROLE_ACTIVATED', 'MY_CUSTOM_ROLE')::BOOLEAN = TRUE |
|-----------------------------------------------------------------------------------------|
| True                                                                                    |
+-----------------------------------------------------------------------------------------+
```

## Access control requirements

See the documentation for each namespace for information about the access control
requirements for the properties and functions in that namespace.

## Usage notes

See the documentation for each namespace for usage notes for the properties and
functions in that namespace.

## Examples

See the documentation for each namespace for examples of retrieving the properties and
calling the functions in that namespace.
