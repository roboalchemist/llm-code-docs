# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-iceberg-table.md

# DESCRIBE ICEBERG TABLE

Describes either the columns in an [Apache Iceberg™ table](../../user-guide/tables-iceberg.md) or the current values,
as well as the default values, for the properties of an Iceberg table.

DESCRIBE can be abbreviated to DESC.

Note that this topic refers to Iceberg tables as simply “tables” except where specifying *Iceberg tables* avoids confusion.

See also:
:   [ALTER ICEBERG TABLE](alter-iceberg-table.md), [DROP ICEBERG TABLE](drop-iceberg-table.md), [CREATE ICEBERG TABLE](create-iceberg-table.md), [SHOW ICEBERG TABLES](show-iceberg-tables.md)

## Syntax

```sqlsyntax
DESC[RIBE] [ ICEBERG ] TABLE <name> [ TYPE =  { COLUMNS | STAGE } ]
```

## Parameters

`name`
:   Specifies the identifier for the table to describe. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`TYPE = COLUMNS | STAGE`
:   Specifies whether to display the columns for the table or the stage properties (including their current and default values) for the
    table.

    Default: `TYPE = COLUMNS`

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| SELECT | Iceberg table |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* This command does not show the object parameters for a table. Instead, use
  [SHOW PARAMETERS IN TABLE](show-parameters.md).
* DESC ICEBERG TABLE, [DESCRIBE TABLE](desc-table.md), and [DESCRIBE VIEW](desc-view.md) are interchangeable. Any of these
  commands retrieves the details for the table or view that matches the criteria in the statement; however, `TYPE = STAGE` does
  not apply for views because views don’t have stage properties.
* The output includes a `POLICY NAME` column to indicate the [masking policy](../../user-guide/security-column-intro.md) set on the column.

  If a masking policy isn’t set on the column or if the Snowflake account isn’t Enterprise Edition or higher, Snowflake returns
  `NULL`.
* The command returns the `NAME_MAPPING` column only if you configure Iceberg Compatibility V2
  ([icebergCompatV2](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#iceberg-compatibility-v2)) for the Delta table
  that your Iceberg table is based on.

  > **Note:**
  >
  > To view the `NAME_MAPPING` column, you must also enable the 2025_01 behavior change bundle
  > in your account.
  >
  > To [enable this bundle in your account](../../release-notes/bcr-bundles/managing-behavior-change-releases.md),
  > execute the following statement:
  >
  > ```sqlexample
  > SELECT SYSTEM$ENABLE_BEHAVIOR_CHANGE_BUNDLE('2025_01');
  > ```

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

## Example

Create an example Iceberg table:

> ```sqlexample
> CREATE OR REPLACE ICEBERG TABLE my_iceberg_table
>   CATALOG='my_catalog_integration'
>   EXTERNAL_VOLUME='my_ext_volume'
>   METADATA_FILE_PATH='path/to/metadata/v2.metadata.json';
> ```

Describe the columns in the table:

> ```sqlexample
> DESC ICEBERG TABLE my_iceberg_table ;
> ```
