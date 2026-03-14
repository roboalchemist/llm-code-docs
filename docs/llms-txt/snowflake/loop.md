# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/loop.md

# LOOP (Snowflake Scripting)

A `LOOP` loop does not specify a number of iterations or a terminating condition. The user must explicitly
exit the loop by using [BREAK](break.md) or [RETURN](return.md) inside the loop.

For more information on loops, see [Working with loops](../../developer-guide/snowflake-scripting/loops.md).

> **Note:**
>
> This [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) construct is valid only within a
> [Snowflake Scripting block](../../developer-guide/snowflake-scripting/blocks.md).

See also:
:   [BREAK](break.md), [CONTINUE](continue.md), [RETURN](return.md)

## Syntax

```sqlsyntax
LOOP
    <statement>;
    [ <statement>; ... ]
END LOOP [ <label> ] ;
```

Where:

> `statement`
> :   A statement can be any of the following:
>
>     * A single SQL statement (including CALL).
>     * A control-flow statement (for example, a [looping](../../developer-guide/snowflake-scripting/loops.md) or
>       [branching](../../developer-guide/snowflake-scripting/branch.md) statement).
>     * A nested [block](../../developer-guide/snowflake-scripting/blocks.md).
>
> `label`
> :   An optional label. Such a label can be a jump target for a [BREAK](break.md) or
> [CONTINUE](continue.md) statement. A label must follow the naming rules for
> [Object identifiers](../identifiers.md).

## Usage notes

* A `LOOP` repeats until a `BREAK` or `RETURN` is executed. The `BREAK` or `RETURN` command is almost always
  inside a conditional expression (e.g. `IF` or `CASE`).
* A loop can contain multiple statements. You can use, but are not required to use, a [BEGIN … END](begin.md)
  [block](../../developer-guide/snowflake-scripting/blocks.md) to contain those statements.

## Examples

This loop inserts predictable test data into a table:

```sqlexample
CREATE TABLE dummy_data (ID INTEGER);

CREATE PROCEDURE break_out_of_loop()
RETURNS INTEGER
LANGUAGE SQL
AS
$$
    DECLARE
        counter INTEGER;
    BEGIN
        counter := 0;
        LOOP
            counter := counter + 1;
            IF (counter > 5) THEN
                BREAK;
            END IF;
            INSERT INTO dummy_data (ID) VALUES (:counter);
        END LOOP;
        RETURN counter;
    END;
$$
;
```

Here is the output of executing the stored procedure:

```sqlexample
CALL break_out_of_loop();
+-------------------+
| BREAK_OUT_OF_LOOP |
|-------------------|
|                 6 |
+-------------------+
```

Here is the content of the table after calling the stored procedure:

```sqlexample
SELECT *
    FROM dummy_data
    ORDER BY ID;
+----+
| ID |
|----|
|  1 |
|  2 |
|  3 |
|  4 |
|  5 |
+----+
```
