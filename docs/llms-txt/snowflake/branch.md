# Source: https://docs.snowflake.com/en/developer-guide/snowflake-scripting/branch.md

# Working with conditional logic

Snowflake Scripting supports the following branching constructs for conditional logic:

* IF-THEN-ELSEIF-ELSE
* CASE

## IF statements

In Snowflake Scripting, you can execute a set of statements if a condition is met by using an
[IF](../../sql-reference/snowflake-scripting/if.md) statement.

The syntax for the IF statement is:

```sqlsyntax
 IF (<condition>) THEN
   -- Statements to execute if the <condition> is true.

[ ELSEIF ( <condition_2> ) THEN
  -- Statements to execute if the <condition_2> is true.
]

[ ELSE
  -- Statements to execute if none of the conditions are true.
]

  END IF ;
```

In an IF statement:

* If you need to specify additional conditions, add an ELSEIF clause for each condition.
* To specify the statements to execute when none of the conditions evaluate to TRUE, add an ELSE clause.
* The ELSEIF and ELSE clauses are optional.

The following is a simple example of an IF statement:

```sqlexample
BEGIN
  LET count := 1;
  IF (count < 0) THEN
    RETURN 'negative value';
  ELSEIF (count = 0) THEN
    RETURN 'zero';
  ELSE
    RETURN 'positive value';
  END IF;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
BEGIN
  LET count := 1;
  IF (count < 0) THEN
    RETURN 'negative value';
  ELSEIF (count = 0) THEN
    RETURN 'zero';
  ELSE
    RETURN 'positive value';
  END IF;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| positive value  |
+-----------------+
```

For the full syntax and details about IF statements, see [IF (Snowflake Scripting)](../../sql-reference/snowflake-scripting/if.md).

For more examples that use the IF statement, see:

* [Examples for common use cases of Snowflake Scripting](use-cases.md) - Execute SQL statements based on IF conditions in loops.
* [BREAK](../../sql-reference/snowflake-scripting/break.md), [LOOP](../../sql-reference/snowflake-scripting/loop.md),
  and [Working with loops](loops.md) - Execute BREAK statements to terminate a loop based on IF conditions.
* [EXCEPTION](../../sql-reference/snowflake-scripting/exception.md) - Raise exceptions based on IF conditions.

## CASE statements

A CASE statement behaves similarly to an IF statement but provides a simpler way to specify multiple conditions.

Snowflake Scripting supports two forms of the CASE statement:

* Simple CASE statements
* Searched CASE statements

The next sections explain how to use these different forms.

> **Note:**
>
> Snowflake supports other uses of the keyword CASE outside of Snowflake Scripting (e.g. the
> conditional expression [CASE](../../sql-reference/functions/case.md)).

### Simple CASE statements

In a simple CASE statement, you define different branches (WHEN clauses) for different possible values of a given expression.

The syntax for the simple CASE statement is:

```sqlsyntax
CASE ( <expression_to_match> )

    WHEN <value_1_of_expression> THEN
        <statement>;
        [ <statement>; ... ]

    [ WHEN <value_2_of_expression> THEN
        <statement>;
        [ <statement>; ... ]
    ]

    ... -- Additional WHEN clauses for other possible values;

    [ ELSE
        <statement>;
        [ <statement>; ... ]
    ]

END [ CASE ] ;
```

Snowflake executes the first branch for which `value_n_of_expression` matches the value of `expression_to_match`.

For example, suppose that you want to execute different statements, based on the value of the `expression_to_evaluate` variable.
For each possible value of this variable (e.g. `value a`, `value b`, etc.), you can define a WHEN clause that
specifies the statement(s) to execute:

```sqlexample
DECLARE
  expression_to_evaluate VARCHAR DEFAULT 'default value';
BEGIN
  expression_to_evaluate := 'value a';
  CASE (expression_to_evaluate)
    WHEN 'value a' THEN
      RETURN 'x';
    WHEN 'value b' THEN
      RETURN 'y';
    WHEN 'value c' THEN
      RETURN 'z';
    WHEN 'default value' THEN
      RETURN 'default';
    ELSE
      RETURN 'other';
  END;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  expression_to_evaluate VARCHAR DEFAULT 'default value';
BEGIN
  expression_to_evaluate := 'value a';
  CASE (expression_to_evaluate)
    WHEN 'value a' THEN
      RETURN 'x';
    WHEN 'value b' THEN
      RETURN 'y';
    WHEN 'value c' THEN
      RETURN 'z';
    WHEN 'default value' THEN
      RETURN 'default';
    ELSE
      RETURN 'other';
  END;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| x               |
+-----------------+
```

For the full syntax and details about CASE statements, see [CASE (Snowflake Scripting)](../../sql-reference/snowflake-scripting/case.md).

### Searched CASE statements

In the searched CASE statement, you specify different conditions for each branch (WHEN clause). Snowflake
executes the first branch for which the expression evaluates to TRUE.

The syntax for the searched CASE statement is:

```sqlsyntax
CASE

  WHEN <condition_1> THEN
    <statement>;
    [ <statement>; ... ]

  [ WHEN <condition_2> THEN
    <statement>;
    [ <statement>; ... ]
  ]

  ... -- Additional WHEN clauses for other possible conditions;

  [ ELSE
    <statement>;
    [ <statement>; ... ]
  ]

END [ CASE ] ;
```

For example, when you execute the following CASE statement, the returned value is `a is x` because that branch is the first
branch in which the expression evaluates to TRUE:

```sqlexample
DECLARE
  a VARCHAR DEFAULT 'x';
  b VARCHAR DEFAULT 'y';
  c VARCHAR DEFAULT 'z';
BEGIN
  CASE
    WHEN a = 'x' THEN
      RETURN 'a is x';
    WHEN b = 'y' THEN
      RETURN 'b is y';
    WHEN c = 'z' THEN
      RETURN 'c is z';
    ELSE
      RETURN 'a is not x, b is not y, and c is not z';
  END;
END;
```

Note: If you use [Snowflake CLI](../snowflake-cli/index.md), [SnowSQL](../../user-guide/snowsql.md), the Classic Console, or the
`execute_stream` or `execute_string` method in [Python Connector](../python-connector/python-connector.md)
code, use this example instead (see [Using Snowflake Scripting in Snowflake CLI, SnowSQL, and Python Connector](running-examples.md)):

```sqlexample
EXECUTE IMMEDIATE $$
DECLARE
  a VARCHAR DEFAULT 'x';
  b VARCHAR DEFAULT 'y';
  c VARCHAR DEFAULT 'z';
BEGIN
  CASE
    WHEN a = 'x' THEN
      RETURN 'a is x';
    WHEN b = 'y' THEN
      RETURN 'b is y';
    WHEN c = 'z' THEN
      RETURN 'c is z';
    ELSE
      RETURN 'a is not x, b is not y, and c is not z';
  END;
END;
$$
;
```

```output
+-----------------+
| anonymous block |
|-----------------|
| a is x          |
+-----------------+
```

For the full syntax and details about CASE statements, see [CASE (Snowflake Scripting)](../../sql-reference/snowflake-scripting/case.md).
