# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/running-examples.md

# Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector

This topic explains how to run the Snowflake Scripting examples in [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), and the [Python Connector](../python-connector/python-connector.md).

> **Note:**
>
> If you are using other clients and interfaces, such as [Snowflake CLI](../snowflake-cli/index.md) or the
> [JDBC driver](../jdbc/jdbc.md), you can skip this topic and refer to
> [Snowflake Scripting blocks](blocks.md).

## Introduction

Currently, the following interfaces do not correctly parse Snowflake Scripting blocks:

* [Snowflake CLI](../snowflake-cli/index.md)
* [SnowSQL](../../user-guide/snowsql.md)
* The `execute_stream()` and `execute_string()` methods in
  [Python Connector](../python-connector/python-connector.md) code

  > **Note:**
  >
  > The other Python Connector methods parse Snowflake Scripting blocks correctly.

Entering and running a Snowflake Scripting block can result in the following error:

```none
SQL compilation error: syntax error line 2 at position 25 unexpected '<EOF>'
```

To work around this, use delimiters around the start and end of a Snowflake Scripting block if you are using
these interfaces.

The following sections explain how to do this:

* Using string constant delimiters around a block in a stored procedure
* Passing a block as a string literal to EXECUTE IMMEDIATE

## Using string constant delimiters around a block in a stored procedure

If you are creating a stored procedure, enclose the Snowflake Scripting block in
[single quotes or double dollar signs](../../sql-reference/data-types-text.md). For example:

```sqlexample
CREATE OR REPLACE PROCEDURE myprocedure()
  RETURNS VARCHAR
  LANGUAGE SQL
  AS
  $$
    -- Snowflake Scripting code
    DECLARE
      radius_of_circle FLOAT;
      area_of_circle FLOAT;
    BEGIN
      radius_of_circle := 3;
      area_of_circle := pi() * radius_of_circle * radius_of_circle;
      RETURN area_of_circle;
    END;
  $$
  ;
```

> **Note:**
>
> When specifying the scripting block directly on the Snowflake CLI command line, the `$$` delimiters might not work for some shells because they interpret that delimiter as something else. For example, the bash and zsh shells interpret it as the process ID (PID). To address this limitation, you can use the following alternatives:
>
> * If you still want to specify the scripting block on the command line, you can escape the `$$` delimiters, as in `\$\$`.
> * You can also put the scripting block with the default `$$` delimiters into a separate file and call it with the `snow sql -f <filename>` command.

## Passing a block as a string literal to EXECUTE IMMEDIATE

If you are writing an [anonymous block](blocks.md), pass the block as a string literal to the
[EXECUTE IMMEDIATE](../../sql-reference/sql/execute-immediate.md) command. To delimit the string literal, use
[single quotes or double dollar signs](../../sql-reference/data-types-text.md).

For example:

```sqlexample
EXECUTE IMMEDIATE $$
-- Snowflake Scripting code
DECLARE
  radius_of_circle FLOAT;
  area_of_circle FLOAT;
BEGIN
  radius_of_circle := 3;
  area_of_circle := pi() * radius_of_circle * radius_of_circle;
  RETURN area_of_circle;
END;
$$
;
```

As an alternative, you can define a [session variable](../../sql-reference/session-variables.md) that is a string literal
containing the block, and you can pass that session variable to the EXECUTE IMMEDIATE command. For example:

```sqlexample
SET stmt =
$$
DECLARE
    radius_of_circle FLOAT;
    area_of_circle FLOAT;
BEGIN
    radius_of_circle := 3;
    area_of_circle := pi() * radius_of_circle * radius_of_circle;
    RETURN area_of_circle;
END;
$$
;

EXECUTE IMMEDIATE $stmt;
```

> **Note:**
>
> When specifying the scripting block directly on the Snowflake CLI command line, the `$$` delimiters might not work for some shells because they interpret that delimiter as something else. For example, the bash and zsh shells interpret it as the process ID (PID). To address this limitation, you can use the following alternatives:
>
> * If you still want to specify the scripting block on the command line, you can escape the `$$` delimiters, as in `\$\$`.
> * You can also put the scripting block with the default `$$` delimiters into a separate file and call it with the `snow sql -f <filename>` command.
