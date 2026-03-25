# Source: https://docs.snowflake.com/en/sql-reference-snowflake-scripting.md

# Snowflake Scripting reference

These topics provide reference information for the language elements supported in
[Snowflake Scripting](developer-guide/snowflake-scripting/index.md).

```sqlsyntax
-- Variable declaration
[ DECLARE ... ]
  ...
BEGIN
  ...
  -- Branching
  [ IF ... ]
  [ CASE ... ]

  -- Looping
  [ FOR ... ]
  [ WHILE ... ]
  [ REPEAT ... ]
  [ LOOP ... ]

  -- Loop termination (within a looping construct)
  [ BREAK ]
  [ CONTINUE ]

  -- Variable assignment
  [ LET ... ]

  -- Cursor management
  [ OPEN ... ]
  [ FETCH ... ]
  [ CLOSE ... ]

  -- Asynchronous child job management
  [ AWAIT ... ]
  [ CANCEL ... ]

  -- "No-op" (no-operation) statement (usually within a branch or exception)
  [ NULL ]

  -- Raising exceptions
  [ RAISE ... ]

  -- Returning a value
  [ RETURN ... ]

-- Exception handling
[ EXCEPTION ... ]

END;
```

**Next Topics:**

* [AWAIT](sql-reference/snowflake-scripting/await.md)
* [BEGIN … END](sql-reference/snowflake-scripting/begin.md)
* [BREAK](sql-reference/snowflake-scripting/break.md)
* [CANCEL](sql-reference/snowflake-scripting/cancel.md)
* [CASE](sql-reference/snowflake-scripting/case.md)
* [CLOSE](sql-reference/snowflake-scripting/close.md)
* [CONTINUE](sql-reference/snowflake-scripting/continue.md)
* [DECLARE](sql-reference/snowflake-scripting/declare.md)
* [EXCEPTION](sql-reference/snowflake-scripting/exception.md)
* [FETCH](sql-reference/snowflake-scripting/fetch.md)
* [FOR](sql-reference/snowflake-scripting/for.md)
* [IF](sql-reference/snowflake-scripting/if.md)
* [LET](sql-reference/snowflake-scripting/let.md)
* [LOOP](sql-reference/snowflake-scripting/loop.md)
* [NULL](sql-reference/snowflake-scripting/null.md)
* [OPEN](sql-reference/snowflake-scripting/open.md)
* [RAISE](sql-reference/snowflake-scripting/raise.md)
* [REPEAT](sql-reference/snowflake-scripting/repeat.md)
* [RETURN](sql-reference/snowflake-scripting/return.md)
* [WHILE](sql-reference/snowflake-scripting/while.md)
