# Source: https://docs.snowflake.com/en/sql-reference/sql/create-projection-policy.md

# CREATE PROJECTION POLICY

Creates a new [projection policy](../../user-guide/projection-policies.md) in the current/specified schema or replaces an existing
projection policy.

After creating a projection policy, apply the projection policy to a table column using an
[ALTER TABLE … ALTER COLUMN](alter-table-column.md) command or a view column using the [ALTER VIEW](alter-view.md) command.

See also:
:   [Projection policy DDL reference](../../user-guide/projection-policies.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] PROJECTION POLICY [ IF NOT EXISTS ] <name>
  AS () RETURNS PROJECTION_CONSTRAINT -> <body>
  [ COMMENT = '<string_literal>' ]
```

## Parameters

`name`
:   Identifier for the projection policy; must be unique for your schema.

    The identifier value must start with an alphabetic character and cannot contain spaces or special characters unless the entire identifier
    string is enclosed in double quotes (e.g. `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

`body`
:   SQL expression that determines whether to project a column.

    The expression can contain CASE and other logic statements, but must call the PROJECTION_CONSTRAINT function:

    ```sqlsyntax
    PROJECTION_CONSTRAINT(ALLOW=>{TRUE|FALSE}, ENFORCEMENT=><enforcement_style>)
    ```

    * `ALLOW` (*boolean*) - TRUE allows the column to be projected. FALSE prevents the column from being projected, with the behavior
      specified by ENFORCEMENT. FALSE affects only columns that appear in the final results table.
    * `ENFORCEMENT` (*string, optional*) - If ALLOW=FALSE, specifies what should happen if a query includes a protected column.
      Supported values:

      + FAIL - The query will fail if a protected column is included in the outermost query.
      + NULLIFY - All rows in the protected column return the value NULL.

      Default: FAIL

`COMMENT = 'string_literal'`
:   Adds a comment or overwrites an existing comment for the projection policy.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE PROJECTION POLICY | Schema |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on projection policy DDL and privileges, see [Privileges and commands](../../user-guide/projection-policies.md).

## Usage notes

* If you want to update an existing projection policy and need to see the current definition of the policy, run the
  [DESCRIBE PROJECTION POLICY](desc-projection-policy.md) command or [GET_DDL](../functions/get_ddl.md) function.

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

Do not allow projecting a column:

> ```sqlexample
> CREATE OR REPLACE PROJECTION POLICY do_not_project AS ()
>   RETURNS PROJECTION_CONSTRAINT ->
>   PROJECTION_CONSTRAINT(ALLOW => false);
> ```

Project a column for the `analyst` custom role, otherwise allow the query, but replace all protected column values with NULL:

> ```sqlexample
> CREATE OR REPLACE PROJECTION POLICY project_analyst_only AS ()
>   RETURNS PROJECTION_CONSTRAINT ->
>     CASE
>       WHEN CURRENT_ROLE() = 'ANALYST'
>         THEN PROJECTION_CONSTRAINT(ALLOW => true)
>       ELSE PROJECTION_CONSTRAINT(ALLOW => false, ENFORCEMENT => 'NULLIFY')
>     END;
> ```
