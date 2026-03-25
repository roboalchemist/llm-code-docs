# Source: https://docs.snowflake.com/en/sql-reference/snowflake-scripting/let.md

# LET (Snowflake Scripting)

Assigns an expression to a Snowflake Scripting variable, cursor, or RESULTSET.

For more information on variables, cursors, and RESULTSETs, see:

* [Working with variables](../../developer-guide/snowflake-scripting/variables.md)
* [Working with cursors](../../developer-guide/snowflake-scripting/cursors.md)
* [Working with RESULTSETs](../../developer-guide/snowflake-scripting/resultsets.md)

> **Note:**
>
> This [Snowflake Scripting](../../developer-guide/snowflake-scripting/index.md) construct is valid only within a
> [Snowflake Scripting block](../../developer-guide/snowflake-scripting/blocks.md).

See also:
:   [DECLARE](declare.md)

## Syntax

```sqlsyntax
LET { <variable_assignment> | <cursor_assignment> | <resultset_assignment> }
```

The syntax for each type of assignment is described below in more detail.

* Variable assignment syntax
* Cursor assignment syntax
* RESULTSET assignment syntax

### Variable assignment syntax

Use the following syntax to assign an expression to a [variable](../../developer-guide/snowflake-scripting/variables.md).

```sqlsyntax
LET <variable_name> <type> { DEFAULT | := } <expression> ;

LET <variable_name> { DEFAULT | := } <expression> ;
```

Where:

> `variable_name`
> :   The name of the variable. The name must follow the naming rules for [object identifiers](../identifiers.md).
>
> `type`
> :   A [SQL data type](../../sql-reference-data-types.md).
>
> `DEFAULT expression` or . `:= expression`
> :   Assigns the value of `expression` to the variable.
>
>     If both `type` and `expression` are specified, the expression must evaluate to a data type that matches.

For example, the following `LET` statements declare three variables of type [NUMBER](../data-types-numeric.md),
with precision set to `38` and scale set to `2`. All three variables have a default value, using either `DEFAULT`
or `:=` to specify it.

```sqlexample
BEGIN
  ...
  LET profit NUMBER(38, 2) DEFAULT 0.0;
  LET revenue NUMBER(38, 2) DEFAULT 110.0;
  LET cost NUMBER(38, 2) := 100.0;
  ...
```

For more examples, see:

* [Working with variables](../../developer-guide/snowflake-scripting/variables.md)
* [IF statements](../../developer-guide/snowflake-scripting/branch.md)
* [Working with loops](../../developer-guide/snowflake-scripting/loops.md)
* [Examples for common use cases of Snowflake Scripting](../../developer-guide/snowflake-scripting/use-cases.md)

### Cursor assignment syntax

Use one of the following syntaxes to assign an expression to a [cursor](../../developer-guide/snowflake-scripting/cursors.md).

```sqlsyntax
LET <cursor_name> CURSOR FOR <query> ;
```

```sqlsyntax
LET <cursor_name> CURSOR FOR <resultset_name> ;
```

Where:

> `cursor_name`
> :   The name to give the cursor. This can be any valid Snowflake [identifier](../identifiers.md)
> that is not already in use in this block. The identifier is used by other cursor-related commands, such as [FETCH (Snowflake Scripting)](fetch.md).
>
> `query`
> :   The query that defines the result set that the cursor iterates over.
>
>     This can be almost any valid SELECT statement.
>
> `resultset_name`
> :   The name of the [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md) for the cursor to operate on.

For example, the following `LET` statement declares cursor `c1` for a query:

```sqlexample
BEGIN
  ...
  LET c1 CURSOR FOR SELECT price FROM invoices;
  ...
```

For more examples, see [Working with cursors](../../developer-guide/snowflake-scripting/cursors.md).

### RESULTSET assignment syntax

Use the following syntax to assign an expression to a [RESULTSET](../../developer-guide/snowflake-scripting/resultsets.md).

```sqlsyntax
<resultset_name> := ( <query> ) ;
```

Where:

> `resultset_name`
> :   The name to give the RESULTSET.
>
>     The name should be unique within the current scope.
>
>     The name must follow the naming rules for [Object identifiers](../identifiers.md).
>
> `DEFAULT query` or . `:= query`
> :   Assigns the value of `query` to the RESULTSET.

For example, the following `LET` statement declares RESULTSET `res` for a query:

```sqlexample
BEGIN
  ...
  LET res RESULTSET := (SELECT price FROM invoices);
  ...
```

For more examples, see [Working with RESULTSETs](../../developer-guide/snowflake-scripting/resultsets.md).
