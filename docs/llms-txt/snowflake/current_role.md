# Source: https://docs.snowflake.com/en/sql-reference/functions/current_role.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# CURRENT_ROLE

Returns the name of the [primary role](../../user-guide/security-access-control-overview.md) in use for the current session when the primary role is an account-level role or NULL if the role in use for the current session is a database role.

To specify a different role for the session, execute the [USE ROLE](../sql/use-role.md)
command.

## Syntax

```sqlsyntax
CURRENT_ROLE()
```

## Arguments

None.

## Usage notes

* Granting access on a [secure UDF](../../developer-guide/secure-udf-procedure.md) or [secure view](../../user-guide/views-secure.md) that
  contains this function to a share is allowed. When the secure UDF or secure view is accessed from the data sharing consumer account, this
  function always returns a NULL value.
* Snowflake returns a NULL value if this function is used in a [masking policy](../../user-guide/security-column-intro.md) or
  [row access policy](../../user-guide/security-row-intro.md) that is assigned to a shared table or view.

## Examples

This demonstrates `CURRENT_ROLE()`:

```sqlexample
SELECT CURRENT_ROLE();
```

Output:

> ```sqlexample
> +----------------+
> | CURRENT_ROLE() |
> |----------------|
> | SYSADMIN       |
> +----------------+
> ```
