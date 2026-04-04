# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-snapshot.md

# DROP SNAPSHOT

> **Note:**
>
> This operation is not currently covered by the Service Level set forth in
> [Snowflake’s Support Policy and Service Level Agreement](https://www.snowflake.com/legal/support-policy-and-service-level-agreement/).

Removes a [snapshot of a block storage volume](../../developer-guide/snowpark-container-services/block-storage-volume.md). A snapshot is persisted data that the customer pays for. DROP SNAPSHOT tells Snowflake to delete that data. The data is no longer available for use as a snapshot and the customer no longer pays for it.

See also:
:   [CREATE SNAPSHOT](create-snapshot.md) , [ALTER SNAPSHOT](alter-snapshot.md), [DESCRIBE SNAPSHOT](desc-snapshot.md), [SHOW SNAPSHOTS](show-snapshots.md)

## Syntax

```sqlsyntax
DROP SNAPSHOT [ IF EXISTS ] <name>;
```

## Parameters

`name`
:   Specifies the identifier for the snapshot to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Snapshot | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

* Dropping a snapshot does not immediately remove it from the system. A version of the dropped snapshot is retained in [Time Travel](../../user-guide/data-time-travel.md) for
  the number of days specified by the DATA_RETENTION_TIME_IN_DAYS parameter for the parent schema, database, or account:

  * Within the Time Travel retention period, a dropped snapshot can be restored using the UNDROP SNAPSHOT command.
  * After the Time Travel retention period, it is permanently removed; it must be recreated.

  For more information, see [Data retention period](../../user-guide/data-time-travel.md).
* To immediately drop a snapshot without retention, set DATA_RETENTION_TIME_IN_DAYS to 0 at the schema level where the snapshot resides. This setting also affects the retention period for other objects within that schema.

## Examples

The following example drops the snapshot named `example_snapshot`:

```sqlexample
DROP SNAPSHOT example_snapshot;
```

```output
+----------------------------------------+
| status                                 |
|----------------------------------------|
| EXAMPLE_SNAPSHOT successfully dropped. |
+----------------------------------------+
```
