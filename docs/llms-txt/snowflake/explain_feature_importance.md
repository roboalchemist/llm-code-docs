# Source: https://docs.snowflake.com/en/sql-reference/classes/forecast/methods/explain_feature_importance.md

# Source: https://docs.snowflake.com/en/sql-reference/classes/anomaly-detection/methods/explain_feature_importance.md

# <model_name>!EXPLAIN_FEATURE_IMPORTANCE

Returns the relative feature importance for each feature used by the model.

If you need to select specific columns from the data returned by this method, you can call the method in the FROM clause of a
SELECT statement. See [Selecting columns from SQL class instance methods that return tabular data](../../../snowflake-db-classes.md).

## Syntax

```sqlsyntax
<model_name>!EXPLAIN_FEATURE_IMPORTANCE();
```

## Returns

| Column | Type | Description |
| --- | --- | --- |
| SERIES | [VARIANT](../../../data-types-semistructured.md) | Series value (NULL if model was trained with single time series). |
| RANK | [INTEGER](../../../data-types-numeric.md) | The importance rank of a feature for a specific series |
| FEATURE_NAME | [VARCHAR](../../../data-types-text.md) | The name of the feature used to train the model `aggregated_endogenous_features` represents all features derived as transformations of your target variable. |
| IMPORTANCE_SCORE | [FLOAT](../../../data-types-numeric.md) | The feature’s importance score: a value in [0, 1], with 0 being the lowest possible importance, and 1 the highest. |
| FEATURE_TYPE | [VARCHAR](../../../data-types-text.md) | The source of the feature, one of:   *`user_provided`* `derived_from_timestamp` * `derived_from_endogenous` |
