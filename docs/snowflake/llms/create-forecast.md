# Source: https://docs.snowflake.com/en/sql-reference/classes/forecast/commands/create-forecast.md

# CREATE SNOWFLAKE.ML.FORECAST

Creates a new forecast model from the training data you provide or replaces the forecast model of the same name.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] SNOWFLAKE.ML.FORECAST [ IF NOT EXISTS ] <model_name>(
  INPUT_DATA => <input_data>,
  [ SERIES_COLNAME => '<series_colname>', ]
  TIMESTAMP_COLNAME => '<timestamp_colname>',
  TARGET_COLNAME => '<target_colname>',
  [ CONFIG_OBJECT => <config_object> ]
)
[ [ WITH ] TAG ( <tag_name> = '<tag_value>' [ , <tag_name> = '<tag_value>' , ... ] ) ]
[ COMMENT = '<string_literal>' ]
```

> **Note:**
>
> Using named arguments makes argument order irrelevant and results in more readable code.
> However, you can also use positional arguments, as in the following example:
>
> ```sqlsyntax
> CREATE SNOWFLAKE.ML.FORECAST <name>(
>   '<input_data>', '<series_colname>', '<timestamp_colname>', '<target_colname>'
> );
> ```

## Parameters

`model_name`
:   Specifies the identifier for the model; must be unique for the schema in which the model is created.

    If the model identifier is not fully qualified (in the form of `db_name.schema_name.name` or
    `schema_name.name`), the command creates the model in the current schema for the session.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters
    unless the entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in
    double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../../../identifiers-syntax.md).

## Constructor arguments

**Required:**

`INPUT_DATA => input_data`
:   A [reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to the input data. Using a reference allows the
    training process, which runs with limited privileges, to use your privileges to access the data. You can use a reference to a
    table or a view if your data is already in that form, or you can use a
    [query reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to provide the query to be executed to obtain the data.

    To create this reference, you can use the [TABLE keyword](../../../snowflake-db-classes.md) with the table name, view name,
    or query, or you can call the [SYSTEM$REFERENCE](../../../functions/system_reference.md) or
    [SYSTEM$QUERY_REFERENCE](../../../functions/system_query_reference.md) function.

    The referenced data is the entire training data consumed by the forecasting model. If `input_data` contains any
    columns that are not named as `timestamp_colname`, `target_colname`, or `series_colname`, they
    are considered exogenous variables (additional features). Order of the columns in the input data is not important.

    Your input data must have columns with appropriate types for your use case. See
    [Examples](../../../../user-guide/ml-functions/forecasting.md) for details on each use case.

    | Use Case | Columns and types |
    | --- | --- |
    | Single time series | * Timestamp column: [TIMESTAMP_NTZ](../../../data-types-datetime.md). * Target value column: [FLOAT](../../../data-types-numeric.md). |
    | Multiple time series | * Series column: [VARIANT](../../../data-types-semistructured.md) containing numeric values and text. * Timestamp column: [TIMESTAMP_NTZ](../../../data-types-datetime.md). * Target value column: [FLOAT](../../../data-types-numeric.md). |
    | Single time series with exogenous variables | * Timestamp column: [TIMESTAMP_NTZ](../../../data-types-datetime.md). * Target value column: [FLOAT](../../../data-types-numeric.md). * Exogenous feature columns: [numeric](../../../data-types-numeric.md) or [text](../../../data-types-text.md). |
    | Multiple time series with exogenous variables | * Series column: [VARIANT](../../../data-types-semistructured.md) containing numeric values and text. * Timestamp column: [TIMESTAMP_NTZ](../../../data-types-datetime.md). * Target value column: [FLOAT](../../../data-types-numeric.md). * Exogenous feature columns: [numeric](../../../data-types-numeric.md) or [text](../../../data-types-text.md). |

`TIMESTAMP_COLNAME => 'timestamp_colname'`
:   Name of the column containing the timestamps in `input_data`.

`TARGET_COLNAME => 'target_colname'`
:   Name of the column containing the target (dependent value) in `input_data`.

**Optional:**

`SERIES_COLNAME => 'series_colname'`
:   For multiple time-series models, the name of the column defining the multiple time series in `input_data`.
    This column can be a value of any type, or an array of values from one or more other columns, as shown in
    [Forecast on multiple series](../../../../user-guide/ml-functions/forecasting.md).

    If you are providing arguments positionally, this must be the *second* argument.

`CONFIG_OBJECT => config_object`
:   An [OBJECT](../../../data-types-semistructured.md) containing key-value pairs used to configure the model training job.

    | Key | Type | Default | Description |
    | --- | --- | --- | --- |
    | `aggregation_categorical` | [STRING](../../../data-types-text.md) | `'MODE'` | The aggregation method for categorical features. Supported values are:   * `'MODE'`: The most frequent value. * `'FIRST'`: The earliest value. * `'LAST'`: The latest value. |
    | `aggregation_numeric` | [STRING](../../../data-types-text.md) | `'MEAN'` | The aggregation method for numeric features. Supported values are:   * `'MEAN'`: The average of the values. * `'MEDIAN'`: The middle value. * `MODE`: The most frequent value. * `'MIN'`: The smallest value. * `'MAX'`: The largest value. * `'SUM'`: The total of the values. * `'FIRST'`: The earliest value. * `'LAST'`: The latest value. |
    | `aggregation_target` | [STRING](../../../data-types-text.md) | Same as `aggregation_numeric`, or `'MEAN'` if not specified | The aggregation method for the target value. Supported values are:   * `'MEAN'`: The average of the values. * `'MEDIAN'`: The middle value. * `MODE`: The most frequent value. * `'MIN'`: The smallest value. * `'MAX'`: The largest value. * `'SUM'`: The total of the values. * `'FIRST'`: The earliest value. * `'LAST'`: The latest value. |
    | `aggregation_column` | [Object](../../../data-types-semistructured.md) | n/a | An object containing key-value pairs (both strings) that specify the aggregation method for specific columns. The key is the column name, and the value is the aggregation method. If a column is not specified, the model uses the method specified by `aggregation_numeric` or `aggregation_categorical`, or the default for that column type (`MEAN` for numeric, `MODE` for categorical). |
    | `evaluate` | [BOOLEAN](../../../data-types-logical.md) | TRUE | Whether evaluation metrics should be generated. If TRUE, then additional models are trained for cross-validation using the parameters in the `evaluation_config`. |
    | `evaluation_config` | [OBJECT](../../../data-types-semistructured.md) | See Evaluation configuration below. | A optional config object to specify how out-of-sample evaluation metrics should be generated. |
    | `frequency` | [STRING](../../../data-types-text.md) | n/a | The frequency of the time series. If not specified, the model infers the frequency. The value must be a string representing a time period, such as `'1 day'`. Supported units include seconds, minutes, hours, days, weeks, months, quarters, and years. You may use singular (“hour”) or plural (“hours”) for the interval name, but may not abbreviate. |
    | `method` | [STRING](../../../data-types-text.md) | `'best'` | String (constant) that specifies the algorithm used to train the model. Supported values are:   * `'best'`: Uses an ensemble of models to determine the best algorithm for the data. This ensemble   includes [Prophet](https://facebook.github.io/prophet/),   [ARIMA](https://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average) ,   [Exponential Smoothing](https://en.wikipedia.org/wiki/Exponential_smoothing) , and a   [gradient boosting machine (GBM)](https://en.wikipedia.org/wiki/Gradient_boosting) based algorithm. * `'fast'`: Uses a single algorithm - a GBM based algorithm - to train the model. This option is faster   than the `'best'` option, but may not be as accurate. We recommend using `'fast'` when your training data   has 10,000 or more individual series. |
    | `lower_bound` | [FLOAT](../../../data-types-numeric.md) or NULL | NULL | The lower bound for the target value. If specified, the model will not predict values below this threshold. |
    | `upper_bound` | [FLOAT](../../../data-types-numeric.md) or NULL | NULL | The upper bound for the target value. If specified, the model will not predict values above this threshold. |
    | `on_error` | [STRING](../../../data-types-text.md) | `'ABORT'` | String (constant) that specifies the error handling method for the model training task. This is most useful when training multiple series. Supported values are:   * `'abort'`: Abort the training operation if an error is encountered in any time series. * `'skip'`: Skip any time series where training encounters an error. This allows model training to   succeed for other time series. To see which series failed, use the model’s   [<model_name>!SHOW_TRAINING_LOGS](../methods/show_training_logs.md) method. |

## Evaluation configuration

The `evaluation_config` object contains key-value pairs that configure cross-validation. These parameters are from scikit-learn’s
[TimeSeriesSplit](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html).

> | Key | Type | Default | Description |
> | --- | --- | --- | --- |
> | `n_splits` | [INTEGER](../../../data-types-numeric.md) | 1 | Number of splits. |
> | `max_train_size` | [INTEGER](../../../data-types-numeric.md) or NULL (no maximum). | NULL | Maximum size for a single training set. |
> | `test_size` | [INTEGER](../../../data-types-numeric.md) or NULL. | NULL | Used to limit the size of the test set. |
> | `gap` | [INTEGER](../../../data-types-numeric.md) | 0 | Number of samples to exclude from the end of each training set before the test set. |
> | `prediction_interval` | [FLOAT](../../../data-types-numeric.md) | 0.95 | The prediction interval used in calculating interval metrics. |

## Usage notes

[Replication](../../../../user-guide/account-replication-intro.md) is supported only for instances
of the [CUSTOM_CLASSIFIER](../../custom_classifier.md) class.

## Examples

See [Examples](../../../../user-guide/ml-functions/forecasting.md).
