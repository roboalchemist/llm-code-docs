# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/show_global_evaluation_metrics.md

# <model_name>!SHOW_GLOBAL_EVALUATION_METRICS

Returns overall evaluation metrics for models where evaluation was enabled at instantiation. This method
takes no arguments. See [Metrics in show_global_evaluation_metrics](../../../../user-guide/ml-functions/classification.md).

## Output

| Column | Type | Description |
| --- | --- | --- |
| `dataset_type` | [VARCHAR](../../../data-types-text.md) | The name of the dataset used for metrics calculation, currently EVAL. |
| `average_type` | [VARCHAR](../../../data-types-text.md) | The method of aggregation used to calculate overall metrics from the individual class metrics, currently MACRO. |
| `error_metric` | [VARCHAR](../../../data-types-text.md) | The error metric name. Can include Precision, Recall, F1, etc. |
| `metric_value` | [FLOAT](../../../data-types-numeric.md) | The error metric value |
| `logs` | [VARIANT](../../../data-types-semistructured.md) | Contains error or warning messages. |
