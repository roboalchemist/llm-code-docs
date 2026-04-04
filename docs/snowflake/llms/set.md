# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/service-commands/set.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/spcs-commands/compute-pool-commands/set.md

# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/command-reference/native-apps-commands/release-directive/set.md

# Source: https://docs.snowflake.com/en/sql-reference/sql/set.md

# SET

Initializes the value of a [session variable](../session-variables.md) to the result of a SQL expression.

See also:
:   [SHOW VARIABLES](show-variables.md) , [UNSET](unset.md)

## Syntax

```sqlsyntax
SET <var> = <expr>

SET ( <var> [ , <var> ... ] )  = ( <expr> [ , <expr> ... ] )
```

## Parameters

`var`
:   Specifies the identifier for the variable to initialize.

`expr`
:   Specifies the SQL expression for the variable.

## Usage notes

* You can set multiple variables in the same statement.
* If you specify complex expressions, a running virtual warehouse might be required in the session.
* The number of expressions must match the number of variables to initialize.
* The size of string or binary variables is limited to 256 bytes.
* The identifier (i.e. name) for a SQL variable is limited to 256 characters.
* Variable names such as `CURRENT` or `PUBLIC` are reserved for future use by Snowflake and cannot be used.

## Examples

These two examples use constants to set variables:

```sqlexample
SET V1 = 10;

SET V2 = 'example';
```

This example sets more than one variable at a time:

```sqlexample
SET (V1, V2) = (10, 'example');
```

This example sets the variable to the value of a non-trivial expression that uses a SQL query:

```sqlexample
SET id_threshold = (SELECT COUNT(*)/2 FROM table1);
```

The following example shows the result when a SET command evaluates all of the expressions on the right-hand side of the assignment operator
before setting the first expression on the left-hand side of the operator. Note that the value of the variable named `max` is set
based on the old value of `min`, not the new value.

```sqlexample
SET (min, max) = (40, 70);
```

```sqlexample
SET (min, max) = (50, 2 * $min);

SELECT $max;
```

```output
+------+
| $MAX |
|------|
|   80 |
+------+
```
