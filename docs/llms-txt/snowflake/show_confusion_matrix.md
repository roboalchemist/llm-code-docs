# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/show_confusion_matrix.md

# <model_name>!SHOW_CONFUSION_MATRIX

Returns a table containing the number of instances of each combination of actual class and predicted class in models
where evaluation was enabled at instantiation. You can use this dataset to plot a confusion matrix. This method takes no
arguments. See [Confusion Matrix in show_confusion_matrix](../../../../user-guide/ml-functions/classification.md).

## Output

| Column | Type | Description |
| --- | --- | --- |
| `dataset_type` | [VARCHAR](../../../data-types-text.md) | The name of the dataset used for metrics calculation, currently EVAL. |
| `actual_class` | [VARCHAR](../../../data-types-text.md) | The actual class. |
| `predicted_class` | [VARCHAR](../../../data-types-text.md) | The predicted class. |
| `count` | [INTEGER](../../../data-types-numeric.md) | The number of instances of the given combination of actual and predicted class. |
| `logs` | [VARIANT](../../../data-types-semistructured.md) | Contains error or warning messages. |
