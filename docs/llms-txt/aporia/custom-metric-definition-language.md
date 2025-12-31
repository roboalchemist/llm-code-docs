# Source: https://docs.aporia.com/v1/api-reference/custom-metric-definition-language.md

# Custom Metric Definition Language

In Aporia, custom metrics are defined using syntax that is similar to python's.

There are three building blocks which can be used in order to create a custom metric expression:

* **Constants** - a numeric value (e.g. `2`, `0.5`, ..)
* **Functions** - out of the builtin function collection you can find below (e.g. `sum`, `count`, ...). All those functions return a numeric value.
* **Binary operation** - `+`, `-`, `*`, `/`, `**`. Operands can be both constants or function calls.

### Builtin Functions

Before we dive into each of the supported function, there are two general concepts you should be familiar with regarding all functions - field expressions and data segment filters.

#### Field Expressions

A field expression can be described in the following format:

```
<field_category>.<field_name>[<segment filter>]
```

Field category is one of the following: `features` / `raw_inputs` / `predictions` / `actuals`. Note that you can only use categories which you defined in you schema while [creating your model version](https://docs.aporia.com/v1/introduction/quickstart). In addition, don't forget that `predictions` and `actuals` categories have the same field names.

The segment filter is optional, for further information about the filters read the section below.

#### Data Segment Filters

Data segment filters are boolean expressions, designed to reduce to a specific data segment the field on which we perform the function.

Each boolean condition in a segment filter is a comparison between a field and a constant value. For example:

```
[features.Driving_License == True] // will filter out records in which Driving_License != True
[raw_inputs.Age <= 35]             // will only include records in which Age <= 35
```

Conditions can be combined using `and` / `or` and all fields can be checked for missing values using `is None` / `is not None`.

The following describe the supported combinations:

| Type / Operation |         ==        |         !=        |         <         |         >         |         >=        |         <=        |
| ---------------- | :---------------: | :---------------: | :---------------: | :---------------: | :---------------: | :---------------: |
| Boolean          |     True/False    |     True/False    |         ✖️        |         ✖️        |         ✖️        |         ✖️        |
| Categorical      | numeric constants | numeric constants |         ✖️        |         ✖️        |         ✖️        |         ✖️        |
| String           | numeric constants | numeric constants |         ✖️        |         ✖️        |         ✖️        |         ✖️        |
| Numeric          | numeric constants | numeric constants | numeric constants | numeric constants | numeric constants | numeric constants |

The table cells indicates the type we can compare to.

**Examples**

```
// Average annual premium of those with a driving license
sum(features.Annual_Premium[features.Driving_License == True]) / prediction_count()

// Three time number of prediction of those who are under 35 years old and live in CA
prediction_count(raw_inputs.Age <= 35 and raw_inputs.Region_Code == 28) * 3

prediction_count(features.Age > 27) / (sum(features.Annual_Premium) + sum(features.Vintage))
```

#### Supported functions

<details>

<summary>accuracy</summary>

**Parameters**

* prediction: prediction field
* label: label field
* threshold: numeric. Probability threshold according to which we decide the if a class is positive
* filter: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>actuals_count</summary>

**Parameters**

No parameters needed, cannot apply filters on this metric.

</details>

<details>

<summary>actuals_ratio</summary>

**Parameters**

No parameters needed, cannot apply filters on this metric.

</details>

<details>

<summary>auc_roc</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>count</summary>

**Parameters**

No parameters needed, cannot apply filters on this metric.

</details>

<details>

<summary>f1_score</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **average**: the average strategy (micro / macro / weighted)
* **top\_k**: consider only top-k items.
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>fn_count</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>fp_count</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>fp_rate</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>logloss</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>mae</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>mape</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>max</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>mean</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>median</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>min</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>miss_rate</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>missing_count</summary>

**Parameters**

* **field**: the field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>missing_ratio</summary>

**Parameters**

* **field**: the field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>mse</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>ndcg</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **rank**: the rank position
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>not_missing_count</summary>

**Parameters**

* **field**: the field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>precision_score</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **average**: the average strategy (micro / macro / weighted)
* **top\_k**: consider only top-k items.
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>recall_score</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **average**: the average strategy (micro / macro / weighted)
* **top\_k**: consider only top-k items.
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>rmse</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>specificity</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>std</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict

</details>

<details>

<summary>sum</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict

</details>

<details>

<summary>tn_count</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>tp_count</summary>

**Parameters**

* **prediction**: prediction probability field
* **label**: label field
* **threshold**: numeric. Probability threshold according to which we decide the if a class is positive
* **filter**: the filter we want to apply on the records before calculating the metric

</details>

<details>

<summary>unique_count</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>value_count</summary>

**Parameters**

* **field**: the field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **value**: the value we want to count
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>value_percentage</summary>

**Parameters**

* **field**: the field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **value**: the value we want to count
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>variance</summary>

**Parameters**

* **field**: numeric or dict. The field for which the metric will be computed. Can be of any category (`feature` / `raw_input` / `prediction` / `actual`)
* **filter**: the filter we want to apply on the records before calculating the metric
* **keys**: keys to filter in when field type is dict.

</details>

<details>

<summary>wape</summary>

**Parameters**

* **prediction**: prediction field
* **label**: label field
* **filter**: the filter we want to apply on the records before calculating the metric

</details>
