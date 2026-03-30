# Source: https://docs.snowflake.com/en/sql-reference/stored-procedures/snowflake_telemetry_add_row_access_policy_on_events_view.md

# ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW

> **Note:**
>
> Using row access policies on the default event table is an [Enterprise Edition](../../user-guide/intro-editions.md) feature.

Binds a [row access policy](../../user-guide/security-row-intro.md) to the [EVENTS_VIEW](../telemetry/events_view.md) by
specifying an array of the table’s columns. The EVENTS_VIEW is a view on the [default event table](../../developer-guide/logging-tracing/event-table-setting-up.md).

The EVENTS_ADMIN role includes the USAGE privilege on this procedure.

## Syntax

```sqlsyntax
SNOWFLAKE.TELEMETRY.ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(
  <row_access_policy_reference>,
  <apply_on_columns>
)
```

## Arguments

`row_access_policy_reference`
:   A [reference](../references.md) to a row access policy object to apply for rows in the EVENTS_VIEW.

`apply_on_columns`
:   Array of view column names on which the policy should be applied.

    For the list of allowed column names, see [Event table columns](../../developer-guide/logging-tracing/event-table-columns.md).

## Returns

On successful execution, the procedure returns a string indicating success. Otherwise, the procedure returns an error.

## Usage notes

This stored procedure uses owner’s rights. For more details, see [Understanding caller’s rights and owner’s rights stored procedures](../../developer-guide/stored-procedure/stored-procedures-rights.md).

## Examples

Code in the following example binds the `ROW_ACCESS_POLICY` policy to two columns in the EVENTS_VIEW:

```sqlexample
CALL SNOWFLAKE.TELEMETRY.ADD_ROW_ACCESS_POLICY_ON_EVENTS_VIEW(
  SYSTEM$REFERENCE('ROW_ACCESS_POLICY', 'mydb.myschema.mypolicy', 'SESSION', 'APPLY'),
  ARRAY_CONSTRUCT('record_type', 'resource_attributes')
);
```
