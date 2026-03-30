# Source: https://docs.snowflake.com/en/sql-reference/functions/is_configuration_set.md

Categories:
:   [Context functions](../functions-context.md) (General)

# IS_CONFIGURATION_SET (SYS_CONTEXT function)

Returns the VARCHAR value `'TRUE'` if the specified configuration has a value set,
that is, the configuration’s status is `DONE`. Returns `FALSE` if the
configuration does not have a value set, that is, the configuration’s status is `PENDING`.

See also:
:   [SYS_CONTEXT (SNOWFLAKE$APPLICATION namespace)](sys_context_snowflake_application.md)

## Syntax

```sqlsyntax
SYS_CONTEXT(
  'SNOWFLAKE$APPLICATION' ,
  'IS_CONFIGURATION_SET' ,
  '<config_name>' ,
)
```

## Arguments

`'SNOWFLAKE$APPLICATION'`
:   Specifies that you want to call a function to return context information about the app in which the function is called.

`'IS_CONFIGURATION_SET'`
:   Calls the IS_CONFIGURATION_SET function.

`'config_name'`
:   Specifies the name of the configuration to check.

## Returns

The function returns one of the following VARCHAR values:

* `'TRUE'` if the configuration has a value set.
* `'FALSE'` if the configuration does not have a value set.

To compare this return value against the BOOLEAN value TRUE or FALSE, [cast](../data-type-conversion.md) the return
value to BOOLEAN. For example:

```sqlexample
SELECT SYS_CONTEXT('SNOWFLAKE$APPLICATION', 'IS_CONFIGURATION_SET', 'my_config_name')::BOOLEAN = TRUE;
```

## Usage notes

* This function can only be used by an app.
