# Source: https://docs.snowflake.com/en/sql-reference/functions/current_organization_user.md

Categories:
:   [Context functions](../functions-context.md) (Session)

# CURRENT_ORGANIZATION_USER

Returns the name of the user currently logged into the system, but only if the user is an
[organization user](../../user-guide/organization-users.md).

## Syntax

```sqlsyntax
CURRENT_ORGANIZATION_USER()
```

## Arguments

None.

## Returns

If the current user is an organization user, returns a value of type VARCHAR.

If the current user is not an organization user, returns NULL.

## Usage notes

* To comply with the ANSI standard, this function can be called without parentheses in SQL statements.

  However, if you are setting a [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md)
  to an expression that calls the function (for example, `my_var := CURRENT_ORGANIZATION_USER();`), you must include the
  parentheses. For more information, see [the usage notes for context functions](../functions-context.md).
* Unlike the [CURRENT_USER](current_user.md) context function, this function can return a user when it’s called from a data
  sharing consumer account.

## Examples

```sqlexample
SELECT CURRENT_ORGANIZATION_USER();
```

```output
+-----------------------------+
| CURRENT_ORGANIZATION_USER() |
|-----------------------------|
| TSMITH                      |
+-----------------------------+
```
