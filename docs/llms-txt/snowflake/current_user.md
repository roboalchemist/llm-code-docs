# Source: https://docs.snowflake.com/en/sql-reference/functions/current_user.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_USER

Returns the name of the user currently logged into the system.

## Syntax

```sqlsyntax
CURRENT_USER()

CURRENT_USER
```

## Arguments

None.

## Returns

This function returns a value of type VARCHAR.

## Usage notes

* To comply with the ANSI standard, this function can be called without parentheses in SQL statements.

  However, if you are setting a [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md)
  to an expression that calls the function (for example, `my_var := CURRENT_USER();`), you must include the
  parentheses. For more information, see [the usage notes for context functions](../functions-context.md).
* Granting access on a [secure UDF](../../developer-guide/secure-udf-procedure.md) or [secure view](../../user-guide/views-secure.md) that
  contains this function to a share is allowed. When the secure UDF or secure view is accessed from the data sharing consumer account, this
  function always returns a NULL value.
* Snowflake returns a NULL value if this function is used in a [masking policy](../../user-guide/security-column-intro.md) or
  [row access policy](../../user-guide/security-row-intro.md) that is assigned to a shared table or view.

## Examples

This example calls the CURRENT_USER function:

```sqlexample
SELECT CURRENT_USER();
```

```output
+----------------+
| CURRENT_USER() |
|----------------|
| TSMITH         |
+----------------+
```
