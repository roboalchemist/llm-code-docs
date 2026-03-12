# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-notebook.md

# DROP NOTEBOOK

Removes the specified [notebook](../../user-guide/ui-snowsight/notebooks.md) from the current/specified schema, but retains a version of the
notebook so that it can be recovered using [UNDROP NOTEBOOK](undrop-notebook.md).

## Syntax

```sqlsyntax
DROP NOTEBOOK <name>
```

## Parameters

`name`
:   Specifies the identifier for the notebook to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE or OWNERSHIP | Notebook | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Examples

The following example drops the notebook named `mynotebook`:

```sqlexample
DROP NOTEBOOK mynotebook;
```
