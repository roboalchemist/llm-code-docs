# Source: https://docs.snowflake.com/en/sql-reference/classes/classification/methods/show_feature_importance.md

# <model_name>!SHOW_FEATURE_IMPORTANCE

Returns the relative feature importance for each feature used by the model. This method takes no arguments.

## Syntax

```sqlsyntax
<model_name>!SHOW_FEATURE_IMPORTANCE();
```

## Output

| Column | Type | Description |
| --- | --- | --- |
| `rank` | [INTEGER](../../../data-types-numeric.md) | The importance rank of a feature. |
| `feature` | [VARCHAR](../../../data-types-text.md) | The name of the feature used to train the model. |
| `score` | [FLOAT](../../../data-types-numeric.md) | The feature’s importance score: a value in [0, 1], with 0 being the lowest possible importance, and 1 the highest. |
| `feature_type` | [VARCHAR](../../../data-types-text.md) | The source of the feature. Currently this is always `user_provided`, which denotes feature data provided by the user. |
