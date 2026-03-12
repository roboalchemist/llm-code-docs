# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-detection/methods/detect_anomalies.md

# <model_name>!DETECT_ANOMALIES

Detects and reports anomalies in the input data passed to the method. This is a method of the anomaly detector object that you create by executing the [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](../commands/create-anomaly-detection.md) command.

The method returns a table that labels each row of the input data as anomalous or not.

If you need to select specific columns from the data returned by this method, you can call the method in the FROM clause of a
SELECT statement. See [Selecting columns from SQL class instance methods that return tabular data](../../../snowflake-db-classes.md).

## Syntax

```sqlsyntax
<model_name>!DETECT_ANOMALIES(
  INPUT_DATA => <reference_to_data_to_analyze>,
  TIMESTAMP_COLNAME => '<timestamp_column_name>',
  TARGET_COLNAME => '<target_column_name>',
  [ CONFIG_OBJECT => <configuration_object>, ]
  [ SERIES_COLNAME => '<series_column_name>' ]
)
```

> **Note:**
>
> `model_name` is the object that you create by executing the [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](../commands/create-anomaly-detection.md) command.

## Arguments

**Required:**

`INPUT_DATA => reference_to_data_to_analyze`
:   A [reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to the table, view, or query that returns
    the data to analyze.

    To create this reference, you can use the [TABLE keyword](../../../snowflake-db-classes.md) with the table name, view name,
    or query, or you can call the [SYSTEM$REFERENCE](../../../functions/system_reference.md) or
    [SYSTEM$QUERY_REFERENCE](../../../functions/system_query_reference.md) function.

`TIMESTAMP_COLNAME => 'timestamp_column_name'`
:   The name of the column containing the timestamps (TIMESTAMP_NTZ) in the time-series data.

`TARGET_COLNAME => 'target_column_name'`
:   The name of the column containing the data to analyze (type NUMERIC or FLOAT).

**Optional:**

`SERIES_COLNAME => 'series_column_name'`
:   Name of the column containing the identifier for the series (for multi-series data). This column should be a
    VARIANT because it can be any type of value or values from multiple columns in an array.

`CONFIG_OBJECT => config_object`
:   An [OBJECT](../../../data-types-semistructured.md) containing key-value pairs used to configure the anomaly detection job.

    | Key | Type | Default | Description |
    | --- | --- | --- | --- |
    | `prediction_interval` | [FLOAT](../../../data-types-numeric.md) | 0.99 | Value between 0 and 1 that specifies the percentage of the observations that should be marked as anomalies:  * For less strict anomaly detection (that is, identifying fewer observations marked as anomalies), specify a higher value. * For more strict anomaly detection (that is, identifying more observations as anomalies), reduce this value. |
    | `on_error` | [STRING](../../../data-types-text.md) | `'ABORT'` | String (constant) that specifies the error handling for the anomaly detection task. This is most useful when detecting anomalies in multiple series. Supported values are:   * `'abort'`: Abort the operation if an error is encountered in any time series. * `'skip'`: Skip any time series where anomaly detection encounters an error. This allows anomaly detection   to succeed for other time series. Series that failed are absent from the output. |

## Returns

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERIES | [VARIANT](../../../data-types-semistructured.md) | Series value (NULL if model was trained with single time series). |
| TS | TIMESTAMP_NTZ | The timestamps of the data |
| Y | FLOAT | The values for the time series |
| FORECAST | FLOAT | The predicted value at the timestamp. |
| LOWER_BOUND | FLOAT | The lower bound of the value within the prediction interval. Values that are lower than this are flagged as anomalies. |
| UPPER_BOUND | FLOAT | The upper bound of the value within the prediction interval. Values that are higher than this are flagged as anomalies. |
| IS_ANOMALY | BOOLEAN | True if the value is an anomaly; False if not. |
| PERCENTILE | FLOAT | The corresponding percentile of the observed Y value given the prediction interval.  If the percentile is outside of `((1 - alpha) / 2, 1 - (1 - alpha) / 2)`, the value is flagged as an anomaly. For example, if the prediction interval is 0.95, a percentile of 0.96 **would not** be an anomaly, but a percentile of 0.98 would be.  If the `prediction_interval` field is not specified in the configuration object, the default is 0.99. |
| DISTANCE | FLOAT | The multiple of the standard deviation from the FORECAST column (z-score) |

## Usage notes

* The columns for the data specified in the [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](../commands/create-anomaly-detection.md) command (in the INPUT_DATA
  constructor argument) must match the columns for the data specified in the INPUT_DATA argument of this method.

  For example, if you passed the SERIES_COLNAME argument to the [CREATE SNOWFLAKE.ML.ANOMALY_DETECTION](../commands/create-anomaly-detection.md) command, you must also pass the
  SERIES_COLNAME argument to this method. If you omitted the SERIES_COLNAME argument in the command, you must omit that argument here.
* If the column names specified by the TIMESTAMP_COLNAME or TARGET_COLNAME arguments do not exist in the table, view, or query
  specified by the INPUT_DATA argument, an error occurs.
