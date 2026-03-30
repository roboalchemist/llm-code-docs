# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-snapshot.md

# ALTER SNAPSHOT

> **Note:**
>
> This operation is not currently covered by the Service Level set forth in
> [Snowflake’s Support Policy and Service Level Agreement](https://www.snowflake.com/legal/support-policy-and-service-level-agreement/).

Modifies the properties of an existing [snapshot of a block storage volume](../../developer-guide/snowpark-container-services/block-storage-volume.md).

See also:
:   [CREATE SNAPSHOT](create-snapshot.md) , [DESCRIBE SNAPSHOT](desc-snapshot.md), [DROP SNAPSHOT](drop-snapshot.md), [SHOW SNAPSHOTS](show-snapshots.md)

## Syntax

```sqlsyntax
ALTER SNAPSHOT [ IF EXISTS ] <name> SET COMMENT = '<string_literal>'
```

## Parameters

`name`
:   Specifies the identifier for the snapshot to alter.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Sets one or more specified properties or parameters for the snapshot:

    `COMMENT = string-literal`
    :   Specifies a comment for the snapshot.

## Access control requirements

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Snapshot | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

## Examples

The following example sets a comment on the `example_snapshot` snapshot.

```sqlexample
ALTER SNAPSHOT example_snapshot SET COMMENT = 'sample comment.';
```
