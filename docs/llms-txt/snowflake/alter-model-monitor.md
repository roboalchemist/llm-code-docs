# Source: https://docs.snowflake.com/en/sql-reference/sql/alter-model-monitor.md

# ALTER MODEL MONITOR

Modifies the properties of a [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md):

* Suspends or resumes the monitor.
* Sets the baseline table the monitor uses.
* Sets the refresh interval for dynamic table operations within the monitor.
* Sets the warehouse the monitor uses.
* Adds or removes segment columns for monitoring specific data segments.

See also:
:   [CREATE MODEL MONITOR](create-model-monitor.md),
    [SHOW MODEL MONITORS](show-model-monitors.md),
    [DESCRIBE MODEL MONITOR](desc-model-monitor.md),
    [DROP MODEL MONITOR](drop-model-monitor.md)

## Syntax

```sqlsyntax
ALTER MODEL MONITOR [ IF EXISTS ] <monitor_name> { SUSPEND | RESUME }

ALTER MODEL MONITOR [ IF EXISTS ] <monitor_name> SET
   [ BASELINE='<baseline_table_name>' ]
   [ REFRESH_INTERVAL='<refresh_interval>' ]
   [ WAREHOUSE=<warehouse_name> ]

ALTER MODEL MONITOR [ IF EXISTS ] <monitor_name> ADD segment_column = '<segment_column_name>'

ALTER MODEL MONITOR [ IF EXISTS ] <monitor_name> DROP segment_column = '<segment_column_name>'
```

## Parameters

`monitor_name`
:   Specifies the identifier (i.e. name) of the model monitor.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`SET ...`
:   Specifies one or more model monitor properties to be set.

    `BASELINE='<baseline_table_name>'`
    :   Sets the baseline table that the monitor uses.

    `WAREHOUSE = warehouse_name`
    :   Sets the warehouse that the monitor uses.

    `REFRESH_INTERVAL = 'refresh_interval'`
    :   The interval at which the monitor refreshes its internal state. The value must be a string representing a time period,
        such as `'1 day'`. The minimum refresh interval is `'60 seconds'`. Supported units include seconds, minutes, hours, and days.
        You may use singular (“hour”) or plural (“hours”) for the interval name.

`ADD segment_column = '<segment_column_name>'`
:   Adds a segment column to the monitor. The specified column must exist in the source data and be of type STRING.
    You can add up to 5 segment columns per monitor. Each segment column should have fewer than 25 unique values for optimal performance.

`DROP segment_column = '<segment_column_name>'`
:   Removes a segment column from the monitor.

For more information about segments, see [ML Observability: Monitoring model behavior over time](../../developer-guide/snowflake-ml/model-registry/model-observability.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| Modify | Model monitor |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).
