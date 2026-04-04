# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-model-monitor.md

# DESCRIBE MODEL MONITOR

Displays information about a specific [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md).
This command displays all the information shown by the [SHOW MODEL MONITORS](show-model-monitors.md) command, plus additional information.

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE MODEL MONITOR](create-model-monitor.md),
    [ALTER MODEL MONITOR](alter-model-monitor.md),
    [SHOW MODEL MONITORS](show-model-monitors.md),
    [DROP MODEL MONITOR](drop-model-monitor.md)

## Syntax

```sqlsyntax
{ DESCRIBE | DESC } MODEL MONITOR <monitor_name>
```

## Parameters

`monitor_name`
:   Specifies the identifier for the model monitor to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Output

The command output provides model monitor properties and metadata in the following columns:

| Column | Description |
| --- | --- |
| `created_on` | Date and time when the model monitor was created. |
| `name` | Name of the model monitor. |
| `database_name` | Database in which the model monitor is stored. |
| `schema_name` | Schema in which the model monitor is stored. |
| `warehouse_name` | Warehouse used to monitor the model. |
| `refresh_interval` | The refresh interval (target lag) for triggering refresh of the model monitor. |
| `aggregation_window` | The aggregation window for calculating metrics. |
| `model_task` | The task of the model being monitored, either TABULAR_BINARY_CLASSIFICATION or TABULAR_REGRESSION. |
| `monitor_state` | The state of the model monitor:   *ACTIVE: The model monitor is active and operating correctly.* SUSPENDED: Model monitoring is paused. *PARTIALLY_SUSPENDED: An error condition in which one of the underlying tables has stopped refreshing at the expected interval. See DESCRIBE for more details.* UNKNOWN: An error condition in which the state of the underlying tables cannot be identified. |
| `source` | String representation of a JSON object detailing the source table or view on which aggregations are based. If the table does not exist or is not accessible, the value is an empty string. See Table JSON object specification. |
| `baseline` | String representation of a JSON object detailing baseline table being used for monitoring, of which a clone is embedded in the model monitor object. See Table JSON object specification. |
| `model` | String representation of a JSON object containing information specifically about the model being monitored. See Model JSON object specification. |
| `comment` | Comment about the model monitor. |
| *The following columns are the additional columns displayed by DESCRIBE compared to SHOW* |  |
| `aggregation_status` | JSON object containing aggregation status for each dynamic table type.  **Keys:**   *`SOURCE_AGGREGATED` / `ACCURACY_AGGREGATED` (non-segment)* `SOURCE_AGGREGATED_<segment_column>` / `ACCURACY_AGGREGATED_<segment_column>` (segment-specific)   **Values:** `ACTIVE` or `SUSPENDED` |
| `aggregation_last_error` | JSON object containing the last error for each dynamic table type.  **Keys:** Same as `aggregation_status`  **Values:** Error message, or empty string if successful |
| `aggregation_last_data_timestamp` | JSON object containing the last update timestamp for each dynamic table type.  **Keys:** Same as `aggregation_status`  **Values:** Timestamp of last successful update |
| `columns` | A string representation of a JSON object that contains names of columns being used in the source table. See Column JSON object specification. |

### Table JSON object specification

The following is the format of the JSON representation of a table, as used by the `source` and `baseline` columns in the command output:

| `name` | Name of the source or baseline table or view. |
| --- | --- |
| `database_name` | Database in which the table or view is stored. |
| `schema_name` | Schema in which the table or view is stored. |
| `status` | The status of the table:   *ACTIVE: The table or view is accessible by the user.* MASKED: The current user does not have access to the table or view. Values of other fields appear masked (that is, as a series of asterisks). *DELETED: The table or view has been deleted.* NOT_SET: The status has not been set. |

### Model JSON object specification

The following is the format of the JSON representation of a model, as used by the `model` column in the command output:

| Field | Description |
| --- | --- |
| `model_name` | Name of the model being monitored. |
| `version_name` | Version name of the model version being monitored. |
| `function_name` | Name of the specific function being monitored in the specified model version. |
| `database_name` | Database in which the model is stored. |
| `schema_name` | Schema in which the model is stored. |
| `model_status` | The status of the model. Can be ACTIVE, MASKED, or DELETED. MASKED indicates that the user does not have access to the model; other fields show as a series of asterisks. |
| `version_status` | The status of the model version. Can be ACTIVE or DELETED. (MASKED is not a valid status for a model version, because they do not have access control.) |

### Column JSON object specification

The following is the format of the JSON representation of columns, as used by the `columns` column in the command output:

| Field | Description |
| --- | --- |
| `timestamp_column` | Name of the timestamp column in the data source. |
| `id_columns` | An array of string column names that, together, uniquely identify each row in the source data. |
| `prediction_class_columns` | An array of strings naming all prediction class columns in the data source. |
| `prediction_score_columns` | An array of strings naming all prediction score columns in the data source. |
| `actual_class_columns` | An array of strings naming all actual class columns in the data source. |
| `numerical_columns` | An array of strings naming all numerical feature columns that the model monitor uses from the source table. |
| `string_columns` | An array of strings naming all string (categorical) feature columns that the model monitor uses from the source table. |
| `boolean_columns` | An array of strings naming all Boolean (categorical) feature columns that the model monitor uses from the source table. |
| `segment_columns` | An array of strings naming all segment columns in the data source. For existing model monitors created without segments, this field will be an empty array. |

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| Any | Model monitor |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

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
