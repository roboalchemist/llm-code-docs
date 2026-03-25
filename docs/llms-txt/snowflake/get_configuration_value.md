# Source: https://docs.snowflake.com/en/sql-reference/functions/get_configuration_value.md

Categories:
:   [Context functions](../functions-context.md) (General)

# GET_CONFIGURATION_VALUE (SYS_CONTEXT function)

Returns the current value for the specified configuration.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$APPLICATION' ,
  'GET_CONFIGURATION_VALUE' ,
  '<config_name>' ,
)
```

## Arguments

`'SNOWFLAKE$APPLICATION'`
:   Specifies that you want to call a function to return context information about the application in which the function is called.

`'GET_CONFIGURATION_VALUE'`
:   Calls the GET_CONFIGURATION_VALUE function.

`'config_name'`
:   Specifies the name of the configuration to get the value for.

## Returns

The function returns the current value of the configuration.

## Usage notes

* This function can only be used by an app.
* For a configuration definition of type `APPLICATION_NAME`, the value returned is the current
  name of the application stored in the specified configuration.
