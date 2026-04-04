# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/close.md

# CLOSE (Snowflake Scripting)

Closes the specified cursor.

For more information on cursors, see [Working with cursors](../../developer-guide/snowflake-scripting/cursors.md).

> **Note:**
>
> This [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) construct is valid only within a
> [Snowflake Scripting block](../../developer-guide/snowflake-scripting/blocks.md).

See also:
:   [DECLARE](declare.md), [OPEN](open.md), [FETCH](fetch.md)

## Syntax

```sqlsyntax
CLOSE <cursor_name> ;
```

Where:

> `cursor_name`
> :   The name of the cursor.

## Usage notes

* After a cursor is closed, the cursor’s current row pointer is invalid. Re-opening the cursor causes the cursor to start from
  the beginning of the new result set.

## Examples

```sqlexample
CLOSE my_cursor_name;
```

For a more complete example of using a cursor, see
[the introductory cursor example](../../developer-guide/snowflake-scripting/cursors.md).

An example using a loop is included in the [documentation on FOR loops](for.md).
