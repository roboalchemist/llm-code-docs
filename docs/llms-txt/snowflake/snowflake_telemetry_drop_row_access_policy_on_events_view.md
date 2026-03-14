# Source: https://docs.snowflake.com/en/sql-reference/stored-procedures/snowflake_telemetry_drop_row_access_policy_on_events_view.md

# DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW

> **Note:**
>
> Using row access policies on the default event table is an [Enterprise Edition](../../user-guide/intro-editions.md) feature.

Deletes the specified [row access policy](../../user-guide/security-row-intro.md) bound to the
[EVENTS_VIEW](../telemetry/events_view.md).

The EVENTS_ADMIN role includes the USAGE privilege on this procedure.

## Syntax

```sqlsyntax
SNOWFLAKE.TELEMETRY.DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(
  <row_access_policy_reference>
)
```

## Arguments

`row_access_policy_reference`
:   A [reference](../references.md) to a row access policy object for the policy to drop.

## Returns

On successful execution, the procedure returns a string indicating success. Otherwise, the procedure returns an error.

## Usage notes

This stored procedure uses owner’s rights. For more details, see [Understanding caller’s rights and owner’s rights stored procedures](../../developer-guide/stored-procedure/stored-procedures-rights.md).

## Examples

Code in the following example drops the `ROW_ACCESS_POLICY` policy bound to the EVENTS_VIEW:

```sqlexample
CALL SNOWFLAKE.TELEMETRY.DROP_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(
  SYSTEM$REFERENCE('ROW_ACCESS_POLICY', 'mydb.myschema.mypolicy', 'SESSION', 'APPLY')
);
```
