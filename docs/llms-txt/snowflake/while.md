# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/while.md

# WHILE (Snowflake Scripting)

A `WHILE` loop iterates while a specified condition is true.

For more information on loops, see [Working with loops](../../developer-guide/snowflake-scripting/loops.md).

> **Note:**
>
> This [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) construct is valid only within a
> [Snowflake Scripting block](../../developer-guide/snowflake-scripting/blocks.md).

See also:
:   [BREAK](break.md), [CONTINUE](continue.md)

## Syntax

```sqlsyntax
WHILE ( <condition> ) { DO | LOOP }
    <statement>;
    [ <statement>; ... ]
END { WHILE | LOOP } [ <label> ] ;
```

Where:

> `condition`
> :   An expression that evaluates to a BOOLEAN.
>
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

* Put parentheses around the condition in the `WHILE`. For example: `WHILE ( <condition> )`.
* If the `condition` never evaluates to FALSE, and the loop doesn’t contain a
  [BREAK (Snowflake Scripting)](break.md) command (or equivalent), then the loop will run and consume credits
  indefinitely.
* If the `condition` is NULL, then it is treated as FALSE.
* A loop can contain multiple statements. You can use, but are not required to use, a [BEGIN … END](begin.md)
  [block](../../developer-guide/snowflake-scripting/blocks.md) to contain those statements.
* Pair the keyword `DO` with `END WHILE`, and pair the keyword `LOOP` with `END LOOP`.
  For example:

  ```sqlexample
  WHILE (...) DO
      ...
  END WHILE;

  WHILE (...) LOOP
      ...
  END LOOP;
  ```

## Examples

This example uses a loop to calculate a power of 2. The `counter` variable is the loop counter. The
`power_of_2` variable stores the most recent power of 2 that was calculated. (This is an inefficient
solution, but it demonstrates looping.)

```sqlexample
CREATE PROCEDURE power_of_2()
RETURNS NUMBER(8, 0)
LANGUAGE SQL
AS
$$
DECLARE
  counter NUMBER(8, 0);      -- Loop counter.
  power_of_2 NUMBER(8, 0);   -- Stores the most recent power of 2 that we calculated.
BEGIN
  counter := 1;
  power_of_2 := 1;
  WHILE (counter <= 8) DO
    power_of_2 := power_of_2 * 2;
    counter := counter + 1;
  END WHILE;
  RETURN power_of_2;
END;
$$
;
```

Call the stored procedure:

```sqlexample
CALL power_of_2();
```

```output
+------------+
| POWER_OF_2 |
|------------|
|        256 |
+------------+
```

This example uses a loop and the [DATEADD](../functions/dateadd.md) function to add a day to a date
until the condition is met.

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET mydate := '2024-05-08';
  WHILE (mydate < '2024-05-20') DO
    mydate := DATEADD(day, 1, mydate);
  END WHILE;
  RETURN mydate;
END;
$$
;
```

```output
+-------------------------+
| anonymous block         |
|-------------------------|
| 2024-05-20 00:00:00.000 |
+-------------------------+
```

For more examples, see [WHILE loop](../../developer-guide/snowflake-scripting/loops.md).
