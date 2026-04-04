# Source: https://docs.snowflake.com/en/sql-reference/sql/create-model-monitor.md

# CREATE MODEL MONITOR

Create or replace a [model monitor](../../developer-guide/snowflake-ml/model-registry/model-observability.md) in the current or specified schema.

See also:
:   [ALTER MODEL MONITOR](alter-model-monitor.md),
    [SHOW MODEL MONITORS](show-model-monitors.md),
    [DESCRIBE MODEL MONITOR](desc-model-monitor.md),
    [DROP MODEL MONITOR](drop-model-monitor.md)

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] MODEL MONITOR [ IF NOT EXISTS ] <monitor_name> WITH
    MODEL = <model_name>
    VERSION = '<version_name>'
    FUNCTION = '<function_name>'
    SOURCE = <source_name>
    WAREHOUSE = <warehouse_name>
    REFRESH_INTERVAL = '<num> { seconds | minutes | hours | days }'
    AGGREGATION_WINDOW = '<num> days'
    TIMESTAMP_COLUMN = <timestamp_name>
    [ BASELINE = <baseline_name> ]
    [ ID_COLUMNS = <id_column_name_array> ]
    [ PREDICTION_CLASS_COLUMNS = <prediction_class_column_name_array> ]
    [ PREDICTION_SCORE_COLUMNS = <prediction_column-name_array> ]
    [ ACTUAL_CLASS_COLUMNS = <actual_class_column_name_array> ]
    [ ACTUAL_SCORE_COLUMNS = <actual_column_name_array> ]
    [ SEGMENT_COLUMNS = <segment_column_name_array> ]
    [ CUSTOM_METRIC_COLUMNS = <custom_metric_column_name_array> ]
```

## Required parameters

`monitor_name`
:   Specifies the identifier for the model monitor; must be unique in the schema where the monitor is created,
    and must be in the same schema as the model being monitored.

    If the monitor identifier is not fully qualified (in the form of `db_name.schema_name.name` or
    `schema_name.name`), the command creates the model in the current schema for the session.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`MODEL = model_name`
:   The name of the model to be monitored. Must be in the same schema where the monitor is created.

`VERSION = 'version_name'`
:   Name of the model version to be monitored.

`FUNCTION = function_name`
:   Name of the specific function in the model version to be monitored.

`SOURCE = source_name`
:   Name of the source table or view that contains the feature, inferences and ground truth labels.

`WAREHOUSE = warehouse_name`
:   The name of the Snowflake warehouse to use for the monitor’s internal compute operations.

`REFRESH_INTERVAL = 'num { seconds | minutes | hours | days }'`
:   The interval at which the monitor refreshes its internal state. The value must be a string representing a time period,
    such as `'1 day'`. The minimum refresh interval is `'60 seconds'`. Supported units include seconds, minutes, hours, and days.
    You may use singular (“hour”) or plural (“hours”) for the interval name.

`AGGREGATION_WINDOW = 'num days'`
:   The window over which the monitor aggregates data. The value must be a string representing a time period, such as `'1
    day'`. Only days are supported. You may use singular (“day”) or plural (“days”) for the interval name.

`TIMESTAMP_COLUMN = timestamp_name`
:   Name of the column in the source data that contains the timestamps. Must be of type TIMESTAMP_NTZ.

## Optional parameters

`BASELINE = baseline_name`
:   Name of the baseline table that contains a snapshot of data similar to SOURCE, which is used to compute drift.
    A snapshot of this data is embedded within the monitor object. Although this parameter is optional, if is not set, the
    monitor cannot detect drift.

`ID_COLUMNS = id_column_name_array`
:   An array of string column names that, together, uniquely identify each row in the source data. See [ARRAY constants](../data-types-semistructured.md).

> **Note:**
>
> At least one prediction column (either a prediction score or a prediction class) is mandatory.
>
> * For binary classification models: Predictions can be either scores or classes; actuals must be classes.
> * For multi-class classification models: Predictions and actuals must be classes.
> * For regression models: Both predictions and actuals must be numbers.

`PREDICTION_CLASS_COLUMNS = prediction_class_column_name_array`
:   An array of strings naming all prediction class columns in the data source. See [ARRAY constants](../data-types-semistructured.md).
    If the model task is `TABULAR_BINARY_CLASSIFICATION` or `TABULAR_REGRESSION`, the columns must be of type NUMBER.
    If the model task is `TABULAR_MULTI_CLASSIFICATION`, the columns must be of type STRING.

`PREDICTION_SCORE_COLUMNS = prediction_column_name_array`
:   An array of strings naming all prediction score columns in the data source. See [ARRAY constants](../data-types-semistructured.md).
    Columns must be of type NUMBER.

`ACTUAL_CLASS_COLUMNS = actual_class_column_name_array`
:   An array of strings naming all actual class columns in the data source. See [ARRAY constants](../data-types-semistructured.md).
    If the model task is `TABULAR_BINARY_CLASSIFICATION` or `TABULAR_REGRESSION`, the columns must be of type NUMBER.
    If the model task is `TABULAR_MULTI_CLASSIFICATION`, the columns must be of type STRING.

`ACTUAL_SCORE_COLUMNS = actual_column_name_array`
:   An array of strings naming all actual score columns in the data source. See [ARRAY constants](../data-types-semistructured.md).
    Columns must be of type NUMBER.

`SEGMENT_COLUMNS = segment_column_name_array`
:   An array of strings naming all segment columns in the data source. See [ARRAY constants](../data-types-semistructured.md).
    Segment columns must be of type STRING in source data.
    You can specify up to 5 segment columns per monitor. Each segment column should have fewer than 25 unique values for optimal performance.
    For more information about segments, see [ML Observability: Monitoring model behavior over time](../../developer-guide/snowflake-ml/model-registry/model-observability.md).

`CUSTOM_METRIC_COLUMNS = custom_metric_column_name_array`
:   An array of strings naming columns in the source data that are used for custom metrics. These columns are not treated as features. See [ARRAY constants](../data-types-semistructured.md).
    Columns must be of type NUMBER.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Model monitor | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| CREATE MODEL MONITOR | Schema |  |
| SELECT | Table or view specified by the SOURCE parameter |  |
| USAGE | Warehouse specified by the WAREHOUSE parameter |  |
| USAGE | Model specified by the MODEL parameter |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The following requirements apply to the parameters:

  * Model task must be `tabular_binary_classification` or `tabular_regression`.
  * Multiple-output models are not currently supported. Although the prediction and actual columns are arrays, the arrays
    must have only one element.
  * At least one of the prediction columns must be specified.
  * Actual columns are optional, but accuracy metrics are not computed if they are not specified.
  * A column may be specified once across all parameters (for example, an ID column cannot also be a prediction column).
* The number of monitored features is limited to 500.
* Segment column requirements:

  * Segment columns must be of type STRING.
  * A maximum of 5 segment columns per monitor (hard limit).
  * Each segment column should have fewer than 25 unique values (recommended limit).
  * Segment values are case sensitive and special characters are not supported for segment queries.
* The basic configuration of MODEL MONITOR instances, including the model it monitors and data sources it uses, cannot be
  changed after the monitor is created. You can modify only a few options using
  [ALTER MODEL MONITOR](alter-model-monitor.md). To change a monitor’s configuration, drop the instance and create a new
  one.
* [Replication](../../user-guide/account-replication-intro.md) is supported only for instances
  of the [CUSTOM_CLASSIFIER](../classes/custom_classifier.md) class.

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## Examples

**Basic example**

Create a model monitor that refreshes daily and uses single prediction and actual score columns.

```sqlexample
CREATE MODEL MONITOR my_monitor WITH
    MODEL = my_model
    VERSION = 'v1'
    FUNCTION = 'predict'
    SOURCE = mydb.myschema.scoring_data
    WAREHOUSE = compute_wh
    REFRESH_INTERVAL = '1 day'
    AGGREGATION_WINDOW = '1 day'
    TIMESTAMP_COLUMN = event_time
    PREDICTION_SCORE_COLUMNS = ( 'prediction_score' )
    ACTUAL_SCORE_COLUMNS = ( 'actual_score' );
```

**Example with CUSTOM_METRIC_COLUMNS**

Specify custom numeric columns to compute additional bespoke metrics.

```sqlexample
CREATE MODEL MONITOR my_monitor_custom WITH
    MODEL = my_model
    VERSION = 'v1'
    FUNCTION = 'predict'
    SOURCE = mydb.myschema.scoring_data
    WAREHOUSE = compute_wh
    REFRESH_INTERVAL = '1 day'
    AGGREGATION_WINDOW = '1 day'
    TIMESTAMP_COLUMN = event_time
    PREDICTION_SCORE_COLUMNS = ( 'prediction_score' )
    ACTUAL_SCORE_COLUMNS = ( 'actual_score' )
    CUSTOM_METRIC_COLUMNS = ( 'latency_ms', 'num_impressions' );
```

In this example, we include two custom metrics: `latency_ms` and `num_impressions`.
These are columns in the source data that are not features to the model, but are useful to track next to the model’s performance.
