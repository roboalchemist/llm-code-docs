# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/repeat.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/repeat.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# REPEAT

Builds a string by repeating the input for the specified number of
times.

## Syntax

```sqlsyntax
REPEAT(<input>, <n>)
```

## Arguments

`input`
:   The input string from which the output string is built.

`n`
:   The number of times the input string should be repeated. The minimum
    valid number is 0 (which results in an empty string).

## Examples

```sqlexample
SELECT REPEAT('xy', 5);

-----------------+
 REPEAT('XY', 5) |
-----------------+
 xyxyxyxyxy      |
-----------------+
```
