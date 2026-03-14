# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-external-volume.md

# DROP EXTERNAL VOLUME

Removes an [external volume](../../user-guide/tables-iceberg.md) from the account, but retains a version of the
external volume so that it can be recovered using [UNDROP EXTERNAL VOLUME](undrop-external-volume.md). For more information, see Usage Notes (in this topic).

See also:
:   [CREATE EXTERNAL VOLUME](create-external-volume.md) , [ALTER EXTERNAL VOLUME](alter-external-volume.md) , [SHOW EXTERNAL VOLUMES](show-external-volumes.md) , [DESCRIBE EXTERNAL VOLUME](desc-external-volume.md)

## Syntax

```sqlsyntax
DROP EXTERNAL VOLUME [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the external volume to drop. If the identifier contains spaces, special characters, or mixed-case characters,
    the entire string must be enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | External volume | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* You can’t drop or replace an external volume if one or more Iceberg tables
  are associated with the external volume.

  To view the tables that depend on an external volume,
  you can use the [SHOW ICEBERG TABLES](show-iceberg-tables.md) command and
  a query using the [pipe operator](../operators-flow.md) (`->>`) that filters on
  the `external_volume_name` column.

  > **Note:**
  >
  > The column identifier (`external_volume_name`) is case-sensitive.
  > Specify the column identifier exactly as it appears in the SHOW ICEBERG TABLES output.

  For example:

  ```sqlexample
  SHOW ICEBERG TABLES
    ->> SELECT *
          FROM $1
          WHERE "external_volume_name" = 'my_external_volume_1';
  ```

* Dropping an external volume does not permanently remove it from the system. Snowflake retains a version of the dropped external volume in
  [Time Travel](../../user-guide/data-time-travel.md). You can restore a dropped external volume by using
  the [UNDROP EXTERNAL VOLUME](undrop-external-volume.md) command.
* After a dropped external volume has been purged, it cannot be recovered; it must be recreated.
* After dropping an external volume, creating an external volume with the same name creates a new version of the external volume.
  You can restore the dropped version of the previous external volume by following these steps:

  1. Rename the current version of the external volume.
  2. Use the [UNDROP EXTERNAL VOLUME](undrop-external-volume.md) command to restore the previous version.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

The following example drops an external volume named `my_external_volume`:

> ```sqlexample
> DROP EXTERNAL VOLUME my_external_volume;
> ```
