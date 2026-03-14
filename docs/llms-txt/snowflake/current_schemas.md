# Source: https://docs.snowflake.com/en/sql-reference/functions/current_schemas.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# CURRENT_SCHEMAS

Returns active search path schemas.

For more information about search path, see [Object name resolution](../name-resolution.md).

## Syntax

```sqlsyntax
CURRENT_SCHEMAS()
```

## Arguments

None.

## Usage notes

Do not confuse this function with the similarly named function
[CURRENT_SCHEMA](current_schema.md).

## Examples

Show the schemas that will be searched if a table or other database object
is referenced without a schema name:

> ```sqlexample
> SELECT CURRENT_SCHEMAS();
> ```
>
> Output:
>
> ```sqlexample
> +-----------------------------------------+
> | CURRENT_SCHEMAS()                       |
> |-----------------------------------------|
> | ["TEST_DB1.BILLING", "TEST_DB1.PUBLIC"] |
> +-----------------------------------------+
> ```
