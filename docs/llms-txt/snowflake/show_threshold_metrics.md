# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/show_threshold_metrics.md

# <model_name>!SHOW_THRESHOLD_METRICS

Returns raw counts and metrics for a specific threshold for each class in models where evaluation was enabled at instantiation.
This method takes no arguments. See [Metrics in show_threshold_metrics](../../../../user-guide/ml-functions/classification.md).

## Output

| Column | Type | Description |
| --- | --- | --- |
| `dataset_type` | [VARCHAR](../../../data-types-text.md) | The name of the dataset used for metrics calculation, currently EVAL. |
| `class` | [VARCHAR](../../../data-types-text.md) | The predicted class. Each class has its own set of metrics, which are provided in multiple rows. |
| `threshold` | [FLOAT](../../../data-types-numeric.md) | Threshold used to generate predictions. |
| `precision` | [FLOAT](../../../data-types-numeric.md) | Precision for the given class. The ratio of true positives to the total predicted positives. |
| `recall` | [FLOAT](../../../data-types-numeric.md) | Recall for the given class. Also called “sensitivity.” The ratio of true positives to the total actual positives. |
| `f1` | [FLOAT](../../../data-types-numeric.md) | F1 score for the given class. |
| `tpr` | [FLOAT](../../../data-types-numeric.md) | True positive rate for the given class. |
| `fpr` | [FLOAT](../../../data-types-numeric.md) | False positive rate for the given class. |
| `tp` | [INTEGER](../../../data-types-numeric.md) | Total count of true positives in the given class. |
| `fp` | [INTEGER](../../../data-types-numeric.md) | Total count of false positives in the given class. |
| `tn` | [INTEGER](../../../data-types-numeric.md) | Total count of true negatives in the given class. |
| `fn` | [INTEGER](../../../data-types-numeric.md) | Total count of false negatives in the given class. |
| `accuracy` | [FLOAT](../../../data-types-numeric.md) | The accuracy (ratio of correct predictions, both positive and negative, to the total number of predictions) for the given class. |
| `support` | [INTEGER](../../../data-types-numeric.md) | The support (true positives plus false negatives) for the given class. |
| `logs` | [VARIANT](../../../data-types-semistructured.md) | Contains error or warning messages. |
