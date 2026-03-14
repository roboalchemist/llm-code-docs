# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/loops.md

# Working with loops

Snowflake Scripting supports the following types of loops:

* FOR
* WHILE
* REPEAT
* LOOP

This topic explains how to use each of these types of loops.

## FOR loop

A [FOR](../../sql-reference/snowflake-scripting/for.md) loop repeats a sequence of steps for a specified number of times or for each
row in a result set. Snowflake Scripting supports the following types of FOR loops:

* Counter-based FOR loops
* Cursor-based FOR loops
* RESULTSET-based FOR loops

The next sections explain how to use these types of FOR loops.

### Counter-based FOR loops

A counter-based FOR loop executes a specified number of times.

The syntax for a counter-based FOR loop is

```sqlsyntax
FOR <counter_variable> IN [ REVERSE ] <start> TO <end> { DO | LOOP }
  <statement>;
  [ <statement>; ... ]
END { FOR | LOOP } [ <label> ] ;
```

For example, the following FOR loop executes five times:

```sqlexample
DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  FOR i IN 1 TO maximum_count DO
    counter := counter + 1;
  END FOR;
  RETURN counter;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  FOR i IN 1 TO maximum_count DO
    counter := counter + 1;
  END FOR;
  RETURN counter;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               5 |
+-----------------+
```

You can include SQL statements inside Snowflake Scripting loops. For example, the following FOR loop executes an INSERT
statement five times to insert the value of the counter into a table:

```sqlexample
DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  CREATE OR REPLACE TABLE test_for_loop_insert(i INTEGER);
  FOR i IN 1 TO maximum_count DO
    INSERT INTO test_for_loop_insert VALUES (:i);
    counter := counter + 1;
  END FOR;
  RETURN counter || ' rows inserted';
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  counter INTEGER DEFAULT 0;
  maximum_count INTEGER default 5;
BEGIN
  CREATE OR REPLACE TABLE test_for_loop_insert(i INTEGER);
  FOR i IN 1 TO maximum_count DO
    INSERT INTO test_for_loop_insert VALUES (:i);
    counter := counter + 1;
  END FOR;
  RETURN counter || ' rows inserted';
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| 5 rows inserted |
+-----------------+
```

Query the table to view the inserted rows:

```sqlexample
SELECT * FROM test_for_loop_insert;
```

```output
+---+
| I |
|---|
| 1 |
| 2 |
| 3 |
| 4 |
| 5 |
+---+
```

For the full syntax and details about FOR loops, see [FOR (Snowflake Scripting)](../../sql-reference/snowflake-scripting/for.md).

### Cursor-based FOR loops

A [cursor-based](cursors.md) FOR loop iterates over a result set. The number of iterations is determined by the number of
rows in the [cursor](cursors.md).

The syntax for a cursor-based FOR loop is:

```sqlsyntax
FOR <row_variable> IN <cursor_name> DO
  <statement>;
  [ <statement>; ... ]
END FOR [ <label> ] ;
```

The example in this section uses the data in the following `invoices` table:

```sqlexample
CREATE OR REPLACE TABLE invoices (price NUMBER(12, 2));
INSERT INTO invoices (price) VALUES
  (11.11),
  (22.22);
```

The following example uses a FOR loop iterate over the rows in a cursor for the `invoices` table:

```sqlexample
DECLARE
  total_price FLOAT;
  c1 CURSOR FOR SELECT price FROM invoices;
BEGIN
  total_price := 0.0;
  FOR record IN c1 DO
    total_price := total_price + record.price;
  END FOR;
  RETURN total_price;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  total_price FLOAT;
  c1 CURSOR FOR SELECT price FROM invoices;
BEGIN
  total_price := 0.0;
  FOR record IN c1 DO
    total_price := total_price + record.price;
  END FOR;
  RETURN total_price;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|           33.33 |
+-----------------+
```

For the full syntax and details about FOR loops, see [FOR (Snowflake Scripting)](../../sql-reference/snowflake-scripting/for.md).

### RESULTSET-based FOR loops

A [RESULTSET-based](resultsets.md) FOR loop iterates over a result set. The number of iterations is determined by the number of
rows returned by the RESULTSET query.

The syntax for a RESULTSET-based FOR loop is:

```sqlsyntax
FOR <row_variable> IN <RESULTSET_name> DO
  <statement>;
  [ <statement>; ... ]
END FOR [ <label> ] ;
```

The example in this section uses the data in the following `invoices` table:

```sqlexample
CREATE OR REPLACE TABLE invoices (price NUMBER(12, 2));
INSERT INTO invoices (price) VALUES
  (11.11),
  (22.22);
```

The following block uses a FOR loop to iterate over the rows in a RESULTSET for the `invoices` table:

```sqlexample
DECLARE
  total_price FLOAT;
  rs RESULTSET;
BEGIN
  total_price := 0.0;
  rs := (SELECT price FROM invoices);
  FOR record IN rs DO
    total_price := total_price + record.price;
  END FOR;
  RETURN total_price;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  total_price FLOAT;
  rs RESULTSET;
BEGIN
  total_price := 0.0;
  rs := (SELECT price FROM invoices);
  FOR record IN rs DO
    total_price := total_price + record.price;
  END FOR;
  RETURN total_price;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|           33.33 |
+-----------------+
```

For the full syntax and details about FOR loops, see [FOR (Snowflake Scripting)](../../sql-reference/snowflake-scripting/for.md).

## WHILE loop

A [WHILE](../../sql-reference/snowflake-scripting/while.md) loop iterates while a condition is true. In a WHILE
loop, the condition is tested immediately before executing the body of the loop. If the condition is false before the first
iteration, then the body of the loop does not execute even once.

The syntax for a WHILE loop is:

```sqlsyntax
WHILE ( <condition> ) { DO | LOOP }
  <statement>;
  [ <statement>; ... ]
END { WHILE | LOOP } [ <label> ] ;
```

For example:

```sqlexample
BEGIN
  LET counter := 0;
  WHILE (counter < 5) DO
    counter := counter + 1;
  END WHILE;
  RETURN counter;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET counter := 0;
  WHILE (counter < 5) DO
    counter := counter + 1;
  END WHILE;
  RETURN counter;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               5 |
+-----------------+
```

For the full syntax and details about WHILE loops, see [WHILE (Snowflake Scripting)](../../sql-reference/snowflake-scripting/while.md).

## REPEAT loop

A [REPEAT](../../sql-reference/snowflake-scripting/repeat.md) loop iterates until a condition is true. In a REPEAT
loop, the condition is tested immediately after executing the body of the loop. As a result, the body of the loop always executes
at least once.

The syntax for a REPEAT loop is:

```sqlsyntax
REPEAT
  <statement>;
  [ <statement>; ... ]
UNTIL ( <condition> )
END REPEAT [ <label> ] ;
```

For example:

```sqlexample
BEGIN
  LET counter := 5;
  LET number_of_iterations := 0;
  REPEAT
    counter := counter - 1;
    number_of_iterations := number_of_iterations + 1;
  UNTIL (counter = 0)
  END REPEAT;
  RETURN number_of_iterations;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET counter := 5;
  LET number_of_iterations := 0;
  REPEAT
    counter := counter - 1;
    number_of_iterations := number_of_iterations + 1;
  UNTIL (counter = 0)
  END REPEAT;
  RETURN number_of_iterations;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               5 |
+-----------------+
```

For the full syntax and details about REPEAT loops, see [REPEAT (Snowflake Scripting)](../../sql-reference/snowflake-scripting/repeat.md).

## LOOP loop

A [LOOP](../../sql-reference/snowflake-scripting/loop.md) loop executes until a BREAK
command is executed. A BREAK command is normally embedded inside branching logic
(e.g. [IF statements](branch.md) or [CASE statements](branch.md)).

The syntax for a LOOP statement is:

```sqlsyntax
LOOP
  <statement>;
  [ <statement>; ... ]
END LOOP [ <label> ] ;
```

For example:

```sqlexample
BEGIN
  LET counter := 5;
  LOOP
    IF (counter = 0) THEN
      BREAK;
    END IF;
    counter := counter - 1;
  END LOOP;
  RETURN counter;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET counter := 5;
  LOOP
    IF (counter = 0) THEN
      BREAK;
    END IF;
    counter := counter - 1;
  END LOOP;
  RETURN counter;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
|               0 |
+-----------------+
```

For the full syntax and details about LOOP loops, see [LOOP (Snowflake Scripting)](../../sql-reference/snowflake-scripting/loop.md).

## Terminating a loop or iteration

In a loop construct, you can specify when the loop or an iteration of the loop must terminate early. The next sections explain
this in more detail:

* Terminating a loop
* Terminating an iteration without terminating the loop
* Specifying where execution should continue after termination

### Terminating a loop

You can explicitly terminate a loop early by executing the [BREAK](../../sql-reference/snowflake-scripting/break.md) command.
BREAK (and its synonym EXIT) immediately stops the current iteration, and skips any remaining iterations.
You can think of BREAK as jumping to the first executable statement after the end of the loop.

BREAK is required in a LOOP loop but is not necessary in WHILE, FOR, and REPEAT loops. In most cases,
if you have statements that you want to skip, you can use the standard branching constructs ([IF statements](branch.md) and
[CASE statements](branch.md)) to control which statements inside a loop are executed.

A BREAK command itself is usually inside an IF or CASE statement.

### Terminating an iteration without terminating the loop

You can use the CONTINUE (or ITERATE) command to jump to the end of an iteration of a loop, skipping the
remaining statements in the loop. The loop continues at the start of the next iteration.

Such jumps are rarely necessary. In most cases, if you have statements that you want to skip, you can use the
standard branching constructs ([IF statements](branch.md) and [CASE statements](branch.md)) to control which
statements inside a loop are executed.

A CONTINUE or ITERATE command itself is usually inside an IF or CASE statement.

### Specifying where execution should continue after termination

In a BREAK or CONTINUE command, if you need to continue execution at a specific point in the code (e.g. the outer
loop in a nested loop), specify a label that identifies the point at which execution should continue.

The following example demonstrates this in a nested loop:

```sqlexample
BEGIN
  LET inner_counter := 0;
  LET outer_counter := 0;
  LOOP
    LOOP
      IF (inner_counter < 5) THEN
        inner_counter := inner_counter + 1;
        CONTINUE OUTER;
      ELSE
        BREAK OUTER;
      END IF;
    END LOOP INNER;
    outer_counter := outer_counter + 1;
    BREAK;
  END LOOP OUTER;
  RETURN ARRAY_CONSTRUCT(outer_counter, inner_counter);
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET inner_counter := 0;
  LET outer_counter := 0;
  LOOP
    LOOP
      IF (inner_counter < 5) THEN
        inner_counter := inner_counter + 1;
        CONTINUE OUTER;
      ELSE
        BREAK OUTER;
      END IF;
    END LOOP INNER;
    outer_counter := outer_counter + 1;
    BREAK;
  END LOOP OUTER;
  RETURN ARRAY_CONSTRUCT(outer_counter, inner_counter);
END;
$$;
```

In this example:

* There is a loop labeled INNER that is nested in a loop labeled OUTER.
* CONTINUE OUTER starts another iteration of the loop with the label OUTER.
* BREAK OUTER terminates the inner loop and transfers control to the end of the outer loop (labeled OUTER).

The output of this command is:

```output
+-----------------+
| anonymous block |
|-----------------|
| [               |
|   0,            |
|   5             |
| ]               |
+-----------------+
```

As shown in the output:

* `inner_counter` is incremented up to 5. CONTINUE OUTER starts a new iteration of the outer loop, which starts a new
  iteration of the inner loop, which increments this counter up to 5. These iterations continue until the value of
  `inner_counter` equals 5 and BREAK OUTER terminates the inner loop.
* `outer_counter` is never incremented. The statement that increments this counter is never reached because BREAK OUTER
  transfers control to the end of the outer loop.
