# Source: https://docs.snowflake.com/en/sql-reference/classes/forecast/methods/show_training_logs.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/show_training_logs.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-detection/methods/show_training_logs.md

# <model_name>!SHOW_TRAINING_LOGS

Returns logs from model training. Output is non-NULL only when `'ON_ERROR' = 'SKIP'` is set in the training
`CONFIG_OBJECT`.

If you need to select specific columns from the data returned by this method, you can call the method in the FROM clause of a
SELECT statement. See [Selecting columns from SQL class instance methods that return tabular data](../../../snowflake-db-classes.md).

## Syntax

```sqlsyntax
<model_name>!SHOW_TRAINING_LOGS();
```

## Returns

| Column | Type | Description |
| --- | --- | --- |
| SERIES | [VARIANT](../../../data-types-semistructured.md) | Series value (NULL if model was trained with single time series).  **Note:** Your single-series results may not have a SERIES column. [See recent change](../../../../release-notes/bcr-bundles/un-bundled/bcr-cortex-forecast-anomaly-detection-series-column.md). |
| LOGS | [OBJECT](../../../data-types-semistructured.md) | A log of errors encountered during training. The value for the key `Errors` is an array of training errors. If no errors were encountered, the LOGS column is NULL. |

## Examples

See [Detecting Anomalies](../../../../user-guide/ml-functions/anomaly-detection.md).
