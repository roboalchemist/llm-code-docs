# Source: https://docs.snowflake.com/en/sql-reference/classes/forecast.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/forecast/methods/forecast.md

# <model_name>!FORECAST

Generates a forecast from the previously trained model `model_name`.

If you need to select specific columns from the data returned by this method, you can call the method in the FROM clause of a
SELECT statement. See [Selecting columns from SQL class instance methods that return tabular data](../../../snowflake-db-classes.md).

## Syntax

The required arguments vary depending on what use case the model was trained for.

**For single-series models without exogenous variables:**

```sqlsyntax
<name>!FORECAST(
  FORECASTING_PERIODS => <forecasting_periods>,
  [ CONFIG_OBJECT => <config_object> ]
);
```

**For single-series models with exogenous variables:**

```sqlsyntax
<name>!FORECAST(
  INPUT_DATA => <input_data>,
  TIMESTAMP_COLNAME => '<timestamp_colname>',
  [ CONFIG_OBJECT => <config_object> ]
);
```

**For multiple-series models without exogenous variables:**

```sqlsyntax
<name>!FORECAST(
  SERIES_VALUE => <series>,
  FORECASTING_PERIODS => <forecasting_periods>,
  [ CONFIG_OBJECT => <config_object> ]
);
```

**For multiple-series models with exogenous variables:**

```sqlsyntax
<name>!FORECAST(
  SERIES_VALUE => <series>,
  SERIES_COLNAME => <series_colname>,
  INPUT_DATA => <input_data>,
  TIMESTAMP_COLNAME => '<timestamp_colname>',
  [ CONFIG_OBJECT => <config_object> ]
);
```

## Arguments

**Required:**

Not all of the following arguments are required for every use case.

`FORECASTING_PERIODS => forecasting_periods`
:   Required for forecasts without exogenous variables.

    The number of steps ahead to forecast. The interval between steps is inferred by the model during training.

`INPUT_DATA => input_data`
:   Required for forecasts with exogenous variables.

    A [reference](../../../../developer-guide/stored-procedure/stored-procedures-calling-references.md) to a table, view, or query
    that contains the future timestamps and values of the exogenous variables (additional user-provided features) that
    were passed as `input_data` when training the model. Using a reference allows the forecasting process, which
    runs with limited privileges, to use your privileges to access the data. Columns are matched between this argument and
    the original exogenous training data by name.

    To create this reference, you can use the [TABLE keyword](../../../snowflake-db-classes.md) with the table name, view name,
    or query, or you can call the [SYSTEM$REFERENCE](../../../functions/system_reference.md) or
    [SYSTEM$QUERY_REFERENCE](../../../functions/system_query_reference.md) function.

`TIMESTAMP_COLNAME => 'timestamp_colname'`
:   Required for forecasts with exogenous variables.

    The name of the column in `input_data` containing the timestamps.

`SERIES_COLNAME => 'series_colname'`
:   Required for multi-series forecasts with exogenous variables.

    The name of the column in `input_data` specifying the series.

`SERIES_VALUE => series`
:   Required for multi-series forecasts.

    The time series to forecast. Can be a single value (e.g., `'Series A'::variant`) or a [VARIANT](../../../data-types-semistructured.md), but must specify a series that
    the model has been trained on. If not specified, all trained series are predicted.

**Optional:**

`CONFIG_OBJECT => config_object`
:   An [OBJECT](../../../data-types-semistructured.md) containing key-value pairs used to configure the forecast job.

    | Key | Type | Default | Description |
    | --- | --- | --- | --- |
    | `prediction_interval` | [FLOAT](../../../data-types-numeric.md) | 0.95 | A value greater than or equal to 0.0 and less than 1.0. The default value of 0.95 means 95% of future points are expected to fall within the interval [lower_bound, upper_bound] from the forecast result. |
    | `on_error` | [STRING](../../../data-types-text.md) | `'ABORT'` | String (constant) specifying the error handling method. This is most useful when forecasting multiple series. Supported values are:   * `'abort'`: Abort the model forecasting operation if an error is encountered in any time series. * `'skip'`: Skip any time series where forecasting encounters an error. This allows forecasting   to succeed for other time series. Series that failed are absent from the model output. |

## Output

| Column | Type | Description |
| --- | --- | --- |
| SERIES | [VARIANT](../../../data-types-semistructured.md) | Series value (NULL if model was trained with single time series). |
| TS | [TIMESTAMP_NTZ](../../../data-types-datetime.md) | Timestamp. |
| FORECAST | [FLOAT](../../../data-types-numeric.md) | Forecast target value. |
| LOWER_BOUND | [FLOAT](../../../data-types-numeric.md) | Lower boundary of prediction interval. |
| UPPER_BOUND | [FLOAT](../../../data-types-numeric.md) | Upper boundary of prediction interval. |

## Examples

See [Examples](../../../../user-guide/ml-functions/forecasting.md).
