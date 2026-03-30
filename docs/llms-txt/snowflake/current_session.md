# Source: https://docs.snowflake.com/en/sql-reference/functions/current_session.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_SESSION

Returns a unique system identifier for the Snowflake session corresponding to the present connection. This will generally be a system-generated alphanumeric string. It is NOT derived from the user name or user account.

## Syntax

```sqlsyntax
CURRENT_SESSION()
```

## Returns

The data type of the returned value is VARCHAR.

## Examples

```sqlexample
SELECT CURRENT_SESSION();
-------------------+
 CURRENT_SESSION() |
-------------------+
 34359980038       |
-------------------+
```
