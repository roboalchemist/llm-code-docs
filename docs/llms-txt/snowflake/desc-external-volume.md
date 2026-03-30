# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-external-volume.md

# DESCRIBE EXTERNAL VOLUME

Describes the properties of an [external volume](../../user-guide/tables-iceberg.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [ALTER EXTERNAL VOLUME](alter-external-volume.md) , [CREATE EXTERNAL VOLUME](create-external-volume.md) , [DROP EXTERNAL VOLUME](drop-external-volume.md) , [SHOW EXTERNAL VOLUMES](show-external-volumes.md)

## Syntax

```sqlsyntax
DESC[RIBE] EXTERNAL VOLUME <name>
```

## Parameters

`name`
:   Specifies the identifier for the external volume to describe. If the identifier contains spaces or special characters, the entire string
    must be enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also case-sensitive.

## Output

The output of the command includes the following columns, which describe the properties and metadata of the object:

| Column | Description |
| --- | --- |
| `parent_property` | The parent property. This column includes the `STORAGE_LOCATIONS` property, which holds a set of named cloud storage locations. |
| `property` | The name of the property. This column can include the properties listed in the following table. |
| `property_type` | The property type. |
| `property_value` | The value assigned to the property. |
| `property_default` | The default property value. |

The `property` column can include the following properties of an external volume object:

| Property | Description |
| --- | --- |
| `comment` | The comment set for the external volume, if any. |
| `allow_writes` | Specifies whether write operations are allowed for the external volume. |
| `storage_location_n` | Details for a cloud storage location associated with the external volume, where `n` is a unique number that distinguishes the location from others in the `STORAGE_LOCATIONS` list; for example, `storage_location_1`.  For more information about storage location properties, see [CREATE EXTERNAL VOLUME](create-external-volume.md). |
| `active` | The name of the [active storage location](../../user-guide/tables-iceberg-storage.md) for the external volume. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | External volume |  |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Examples

Describe an external volume:

```sqlexample
DESC EXTERNAL VOLUME my_external_volume;
```

The following shows the output of DESCRIBE EXTERNAL VOLUME for an external volume with one storage location.
The property value for `STORAGE_LOCATION_1` is abbreviated for display purposes.

```output
+-------------------+--------------------+---------------+-------------------------------------------------------------------------------------------+------------------+
| parent_property   | property           | property_type | property_value                                                                            | property_default |
|-------------------+--------------------+---------------+-------------------------------------------------------------------------------------------+------------------|
|                   | ALLOW_WRITES       | Boolean       | true                                                                                      | true             |
| STORAGE_LOCATIONS | STORAGE_LOCATION_1 | String        | {"NAME":"my_storage_us_west","STORAGE_PROVIDER":"S3","STORAGE_BASE_URL":"s3://...", ...}  |                  |
| STORAGE_LOCATIONS | ACTIVE             | String        | my_storage_us_west                                                                        |                  |
+-------------------+--------------------+---------------+-------------------------------------------------------------------------------------------+------------------+
```
