# Source: https://docs.aporia.com/api-reference/custom-metric-syntax.md

# Custom Metric Syntax

In Aporia, custom metrics are defined using syntax that is similar to python's.

There are three building blocks which can be used in order to create a custom metric expression:

* **Constants** - a numeric value (e.g. `2`, `0.5`, ..)
* **Functions** - out of the builtin function collection you can find below (e.g. `sum`, `count`, ...). All those functions return a numeric value.
* **Binary operation** - `+`, `-`, `*`, `/`, `**`. Operands can be both constants or function calls.

## Builtin Functions

Before we dive into each of the supported functions, let's take a look at a few examples of custom metric definitions.

```
// Average annual premium of those with a driving license
sum(column="annual_premium") / count()

// Mean predicted probability
mean(column="proba")

// Model revenue
5 * tp_count(column="will_buy_insurance") -2 * fp_count(column="will_buy_insurance")

// nDCG@4 per step
ndcg_at_k(column="p_views", k=4)
ndcg_at_k(column="p_add_to_cart", k=4)
ndcg_at_k(column="p_purchases", k=4)

// accuracy using custom threshold
accuracy(column="proba", type="numeric", threshold=0.2)

// R-squared - Expanding brackets to use available aggregations
rss = squared_error_sum(column="prediction")
tss = squared_sum(column="actual") - 2*mean(column="actual")*sum(column="actual") + column_count(column="actual")*(mean(column="actual")**2)
1 - rss/tss
```

### Filters within functions

Within Aporia we can always set a [segment](https://docs.aporia.com/core-concepts/tracking-data-segments) on our metrics as a whole, but sometimes this is just not enough. Many times we will need to pass a segment of our data to a specific function as part of our metric.&#x20;

Aporia supports these cases by passing another argument to functions called "**filter"**.

With the "**filter**" argument you'll be able to set any filtering to the data passed in the "**column"** argument using the [custom segment syntax](https://docs.aporia.com/api-reference/custom-segment-syntax).

**For example:**

```
// Ratio of the annual premium of people above 70 out of the total premium
sum(column="annual_premium", filter="age > 70") / sum(column="annual_premium")
```

To allow you to set any of your segments upon these metrics as a whole as well, setting a filter within a metric will create behind the scenes, the intersection of the segment within the filter with all of your existing filters. These segments will be counted as any regular segment.

### Supported functions

#### Numerical Measures

<details>

<summary>absolute_sum</summary>

Returns the sum of absolutes for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>count</summary>

Returns the total number of rows.

**Parameters**

No parameters needed.

</details>

<details>

<summary>column_count</summary>

Returns the number of rows with non-null values for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be any field.

</details>

<details>

<summary>max</summary>

Returns the maximum value for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>max_length</summary>

Returns the maximum length for the given column (items for arrays/embeddings, characters for text).

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be **text/array/numeric array/embedding** field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>median</summary>

Returns the median value for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>mean</summary>

Returns the average value for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>mean_length</summary>

Returns the average length for the given column (items for arrays/embeddings, characters for text).

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be **text/array/numeric array/embedding** field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>min</summary>

Returns the minimum value for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>min_length</summary>

Returns the minimum length for the given column (items for arrays/embeddings, characters for text).

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be **text/array/numeric array/embedding** field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>missing_count</summary>

Returns the number of rows with null values for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be any field.

</details>

<details>

<summary>missing_ratio</summary>

Returns the percentage of rows with null values for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be any field.

</details>

<details>

<summary>sum</summary>

Returns the sum for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>squared_sum</summary>

Returns the sum of squared values for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>squared_deviation_sum</summary>

Returns the sum of squares for the given column.

For column **x**, with **m** mean of all x samples, equals to sum of (x-m)².

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

<details>

<summary>value_count</summary>

Returns the number of entries where the given column is equal to the given value.

For example, value\_count(column="bool", value=True) will return count of entries where bool=TRUE.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be any **boolean/categorical** field.
* **value**: The value of the field to look for.

</details>

<details>

<summary>variance</summary>

Returns the variance for the given column.

**Parameters**

* **column**: the name of the field on which we want to apply the function. Can be numeric field of any group (`feature` / `raw_input` / `prediction` / `actual`)

</details>

#### Regression Metrics

<details>

<summary>absolute_error_sum</summary>

Returns the sum of absolute errors for the given prediction.&#x20;

For a prediction P and actual A, returns the sum of |P-A|.

**Parameters**

* **column**: the name of the **numeric prediction** field on which we want to apply the function. Must have a **numeric actual** mapped to it.

</details>

<details>

<summary>mae</summary>

Calculates MAE for the given prediction.

**Parameters**

* **column**: the name of the **numeric prediction** field on which we want to apply the function. Must have a **numeric actual** mapped to it.

</details>

<details>

<summary>mse</summary>

Calculates MSE for the given prediction.

**Parameters**

* **column**: the name of the **numeric prediction** field on which we want to apply the function. Must have a **numeric actual** mapped to it.

</details>

<details>

<summary>rmse</summary>

Calculates RMSE for the given prediction.

**Parameters**

* **column**: the name of the **numeric prediction** field on which we want to apply the function. Must have a **numeric actual** mapped to it.

</details>

<details>

<summary>squared_error_sum</summary>

Returns the sum of squared errors for the given prediction.&#x20;

For a prediction P and actual A, returns the sum of (P-A)².

**Parameters**

* **column**: the name of the **numeric prediction** field on which we want to apply the function. Must have a **numeric actual** mapped to it.

</details>

#### Binary Classification Metrics

<details>

<summary>accuracy</summary>

Calculates accuracy for the given prediction.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions**.
* **method**: will define the average strategy to use. Can be: "macro", "micro" or "weighted". Required for **categorical predictions**.

</details>

<details>

<summary>auc_roc</summary>

Calculates AUC ROC for the given prediction.

**Parameters**

* **column**: the name of the **numeric** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.

</details>

<details>

<summary>fn_count</summary>

Returns the number of False-Negative results.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions**.

</details>

<details>

<summary>fp_count</summary>

Returns the number of False-Positive results.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions**.

</details>

<details>

<summary>f1</summary>

Calculates f1-score for the given prediction.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions.**
* **method**: will define the average strategy to use. Can be: "macro", "micro" or "weighted". Required for **categorical predictions**.

</details>

<details>

<summary>precision</summary>

Calculates precision for the given prediction.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions.**
* **method**: will define the average strategy to use. Can be: "macro", "micro" or "weighted". Required for **categorical predictions**.

</details>

<details>

<summary>recall</summary>

Calculates recall for the given prediction.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions.**
* **method**: will define the average strategy to use. Can be: "macro", "micro" or "weighted". Required for **categorical predictions**.

</details>

<details>

<summary>tn_count</summary>

Returns the number of True-Negative results.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions**.

</details>

<details>

<summary>tp_count</summary>

Returns the number of True-Positive results.

**Parameters**

* **column**: the name of the **numeric/boolean** **prediction** field on which we want to apply the function. Must have a **boolean actual** mapped to it.
* **threshold**: probability threshold according to which we decide if a class is positive. Required for **numeric predictions**.

</details>

#### Multiclass Classification Metrics

<details>

<summary>accuracy_per_class</summary>

Calculates accuracy for the given prediction per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>fn_count_per_class</summary>

Returns the number of False-Negative results per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>fp_count_per_class</summary>

Returns the number of False-Positive results per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>f1_per_class</summary>

Calculates f1-score for the given prediction per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>precision_per_class</summary>

Calculates precision for the given prediction per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>recall_per_class</summary>

Calculates recall for the given prediction per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>tn_count_per_class</summary>

Returns the number of True-Negative results per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

<details>

<summary>tp_count_per_class</summary>

Returns the number of True-Positive results per the specified category class.

**Parameters**

* **column**: the name of the **categorical** **prediction** field on which we want to apply the function. Must have a **categorical** **actual** mapped to it.
* **class\_name**: the class on which we want to calculate the function.

</details>

#### Ranking Metrics

<details>

<summary>accuracy_at_k</summary>

Calculates Accuracy for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>

<details>

<summary>map_at_k</summary>

Calculates MAP (Mean-Average-Precision) for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>

<details>

<summary>mrr_at_k</summary>

Calculates MRR (Mean-Reciprocal-Rank) for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>

<details>

<summary>ndcg_at_k</summary>

Calculates NDCG for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>

<details>

<summary>precision_at_k</summary>

Calculates Precision for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>

<details>

<summary>recall_at_k</summary>

Calculates Recall for the given prediction on the top K items.

**Parameters**

* **column**: the name of the **array prediction** field on which we want to apply the function. Must have an **array actual** mapped to it. If using [candidate-level ranking](https://docs.aporia.com/model-types/ranking#integrating-candidate-level-data), can be a **boolean prediction** with a mapped **boolean actual**.
* **k**: numeric integer between 1 to 12. Only the top-k items will be considered.

</details>
