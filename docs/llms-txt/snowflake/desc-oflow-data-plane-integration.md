# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-oflow-data-plane-integration.md

# DESCRIBE OPENFLOW DATA PLANE INTEGRATION

Describes the columns in an Openflow data plane integration.

See also:
:   [ALTER OPENFLOW DATA PLANE](alter-oflow-data-plane.md), [SHOW OPENFLOW DATA PLANE INTEGRATIONS](show-oflow-data-plane-integration.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } OPENFLOW DATA PLANE INTEGRATION <name>
```

## Parameters

`name`
:   The identifier for the openflow data plane integration to describe.
    If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

    See [SHOW OPENFLOW DATA PLANE INTEGRATIONS](show-oflow-data-plane-integration.md) for openflow data plane integration details, including openflow data plane integration **name**.

## Usage notes

* Openflow data plane integrations cannot be created directly, but rather are created when a deployment is created.
* To DESCRIBE an Openflow data plane integration, you must be using a role that
  has one of USAGE, MODIFY, or OWNERSHIP privilege on the data plane integration.

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

## Output

The command output provides properties and metadata for the Openflow data plane integration in the following columns:

|  |  |
| --- | --- |
| Column | Description |
| `enabled` | True if enabled, otherwise false. |
| `oauth_redirect_uri` | URI used for OATH2 authentication. |
| `data_plane_id` | Internal identifier for the data plane integration. |
| `event_table` | Fully qualified path to the <DATABASE>.<SCHEMA>.<EVENT TABLE NAME> is specified. |
| `comment` | Associated comment. |

## Examples

Describe the columns in the Openflow data plane integration with the specified name:

```sqlexample
DESC OPENFLOW DATA PLANE INTEGRATION edf6f909-d3ff-49d6-925f-xxxxx;
```

```output
+------------------------------------+----------------------------------+------------------+---------------+
|   enabled  |   oauth_redirect_uri  |   data_plane_id                  |   event_table    |   comment     |
+------------------------------------+----------------------------------+------------------+---------------+
|   true     |   https://...         |   edf6f909-d3ff-49d6-925f-xxxxx  |                  |   Example     |
+------------------------------------+----------------------------------+------------------+---------------+
```
