# Source: https://docs.aporia.com/v1/storing-your-predictions/logging-to-aporia-directly.md

# Logging to Aporia directly

This section will teach you how to integrate Aporia using [Python SDK](https://aporia-sdk-ref.netlify.app/), but you can also use our [REST API](https://docs.aporia.com/v1/api-reference/rest-api) or the integrate to your own DB.

## Get Started

To get started, install the Aporia SDK:

```bash
pip3 install aporia --upgrade
```

And then initialize it in your code:

```python
import aporia
aporia.init(token="<TOKEN>",
            environment="<ENVIRONMENT>", # e.g "production"
            verbose=True,
            raise_errors=True)
```

### Create Model

To create a new model to be monitored in Aporia, you can call the `aporia.create_model(...)` API:

```python
aporia.create_model("<MODEL_ID>", "<MODEL_NAME>")
```

This API would not recreate the model if the model ID already exists. You can also specify color, icon, tags, and model owner:

```python
aporia.create_model(
    model_id="fraud-detection",
    model_name="Fraud Detection",
    color=ModelColor.ARCTIC_BLUE,
    icon=ModelIcon.FRAUD_DETECTION,
    tags={
        "framework": "xgboost",
        "coolness_level": 10
    },
    owner="fred@aporia.com", # Integrates with your enterprise auth system ;)
)
```

### Create Model Version

Each model in Aporia contains different **Model Versions**. When you (re)train your model, you should create a new model version in Aporia.

**Manual**

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="binary",
  features={
    "amount": "numeric",
    "owner": "string",
    "is_new": "boolean",
    "created_at": "datetime",
  },
  predictions={
    "will_buy_insurance": "boolean",
    "proba": "numeric",
  },
  # Optional
  feature_importance={
    "amount": 80,
    "owner": 10,
    "is_new": 70,
    "created_at": 20,
  }
)
```

**Inferring from Pandas DataFrame**

```python
# Example DataFrames, each one with one row
features_df = pd.DataFrame([[12.3, "John", True, pd.Timestamp.now()]], 
  columns=["amount", "owner", "is_new", "created_at"])

predictions_df = pd.DataFrame([[True, 0.7]], 
  columns=["will_buy_insurance", "proba"])


# Create a model version by inferring schemas from pandas DataFrames
apr_model = aporia.create_model_version(
    model_id="<MODEL_ID>",
    model_version="v1",
    model_type="binary",

    features=aporia.pandas.infer_schema_from_dataframe(features_df),
    predictions=aporia.pandas.infer_schema_from_dataframe(predictions_df),
      
    # Optional
    feature_importance={
      "amount": 80,
      "owner": 10,
      "is_new": 70,
      "created_at": 20,
    }
)
```

Model version parameter can be any string - you can use the model file's hash, git commit hash, experiment/run ID from MLFlow or anything else.

Model type can be [regression](https://docs.aporia.com/v1/model-types/regression), [binary](https://docs.aporia.com/v1/model-types/binary), [multiclass](https://docs.aporia.com/v1/model-types/multiclass-classification), [multi-label](https://docs.aporia.com/v1/model-types/multi-label-classification), or [ranking](https://docs.aporia.com/v1/model-types/ranking). Please refer to the relevant documentation on each model type for more info.

#### Field Types

* `numeric` - valid examples: 1, 2.87, 0.53, 300.13
* `boolean` - valid examples: True, False
* `categorical` - a categorical field with integer values
* `string` - a categorical field with string values
* `datetime` - contains either python datetime objects, or an ISO-8601 timestamp string
* `text` - freeform text
* `dict` - dictionaries - at the moment keys are strings and values are numeric
* `tensor` - useful for unstructured data, must specify shape, e.g. `{"type": "tensor", "dimensions": [768]}`
* `vector` - useful for arrays that can be different in sizes

#### Get a reference to an existing version

If you already created a version, for example during your training, and you want to use it again, you can receive a reference to the version.

```python
apr_model = aporia.Model("<MODEL_ID>", "v1")
```

## Logging Training / Test Sets

To log the training or test sets of your model, you can use the `apr_model.log_training_set` or `apr_model.log_test_set` functions, respectively.

For example, if we have the following training set:

```python
import pandas as pd

training_features = pd.DataFrame({
  "Age": [31, 20, 53],
  "Annual_Premium": [11234, 534534, 859403],
  "Previously_Insured": [False, True, True],
  "Vehicle_Age_LT_1_Year": [False, True, False],
  "Vehicle_Age_GT_2_Years": [True, False, True],
  "Vehicle_Damage_Yes": [True, False, False],
})

training_predictions = pd.DataFrame({
  "will_buy_insurance": [True, True, False],
})

training_labels = pd.DataFrame({
  "will_buy_insurance": [True, False, True],
})
```

Then you can run:

```
apr_model.log_training_set(
  features=training_features,
  predictions=training_predictions,
  labels=training_labels,
)
```

And similarly, you can use the `apr_model.log_test_set` to log your test set.

In both functions, you can pass `raw_inputs` to log the raw inputs of your training / test sets.

## Logging Serving Data

### Log Predictions

Use the `apr_model.log_prediction` API to log a new prediction.

```python
apr_model.log_prediction(
  id=<PREDICTION_ID>,
  features={
    "amount": 15.3,
    "owner": "Joe",
    "is_new": True,
    "created_at": datetime.now(),
  },
  predictions={
    "will_buy_insurance": True,
    "proba": 0.55,
  },
)
```

Note that for each prediction you must specify an ID. This ID can later be used to log the *actual* value of the prediction. If you don't care about actuals, you can simply pass `str(uuid.uuid4())` as prediction ID.

After logging your first prediction you'll be able to get into your model page on the dashboard.

To log multiple predictions in one call, check out [Batching](#batching).

### Raw Inputs

Raw inputs are the inputs of the model *before* preprocessing, and they're used to construct the features. Logging them is optional but can help you detect issues in your data pipeline.

**Example: Log raw inputs separately**

```python
apr_model.log_raw_inputs(
  id="a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
  raw_inputs={
    "Age": 27,
    "Vehicle_Damage": "Yes",
    "Annual_Premium": 12345,
    "Vehicle_Age": ">2 years"
  },
)
```

**Example: Log raw inputs in `log_prediction`**

```python
apr_model.log_prediction(
  id="a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
  features={
    "Age": 27,
    "Vehicle_Damage_Yes": True,
    "Annual_Premium": 12345,
    "Vehicle_Age_LT_1_Year": False,
    "Vehicle_Age_GT_2_Years": True,
  },
  predictions={
    "will_buy_insurance": True,
  },
  raw_inputs={
    "Age": 27,
    "Vehicle_Damage": "Yes",
    "Annual_Premium": 12345,
    "Vehicle_Age": ">2 years"
  },
)
```

### Actuals

In some cases, you will have access to the [actual value](https://github.com/aporia-ai/docs2/blob/main/core-concepts/actuals-ground-truth/README.md) of the prediction, based on real-world data.

For example, if your model predicted that a client will buy insurance, and a day later the client actually makes a purchase, then the actual value of that prediction is `True`

**Example: Log actuals separately**

```python
apr_model.log_actuals(
  id="a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
  actuals={
    "will_buy_insurance": True,
  },
)
```

**Example: Log actuals in `log_prediction`**

```python
apr_model.log_prediction(
  id="a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
  features={
    "Age": 27,
    "Vehicle_Damage_Yes": True,
    "Annual_Premium": 12345,
    "Vehicle_Age_LT_1_Year": False,
    "Vehicle_Age_GT_2_Years": True,
  },
  predictions={
    "will_buy_insurance": True,
  },
  actuals={
    "will_buy_insurance": True,
  },
)
```

### Batching

All of the function above log a single prediction. If you wish to log multiple predictions in one large batch, you can use the `log_batch_*` functions.

Each of these functions receive a list of dictionaries, such that each dict contains the parameters of the singular version of the function.

**Example: Logging batch predictions**

```python
apr_model.log_batch_prediction(
  [
    {
      "id":"a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
      "features": {
        "Age": 27,
        "Vehicle_Damage_Yes": True,
        "Annual_Premium": 12345,
        "Vehicle_Age_LT_1_Year": False,
        "Vehicle_Age_GT_2_Years": True,
      },
      "predictions": {
        "will_buy_insurance": True,
      },
    },
    {
      "id":"f2d1dccb-1aef-4955-a274-69e1acb8772f",
      "features": {
        "Age": 54,
        "Vehicle_Damage_Yes": False,
        "Annual_Premium": 54324,
        "Vehicle_Age_LT_1_Year": True,
        "Vehicle_Age_GT_2_Years": False,
      },
      "predictions": {
        "will_buy_insurance": False,
      },
    },
  ]
)
```

**Example: Logging batch actuals**

```python
apr_model.log_batch_actuals(
  [
    {
      "id":"a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
      "actuals": {
        "will_buy_insurance": True,
      },
    },
    {
      "id":"f2d1dccb-1aef-4955-a274-69e1acb8772f",
      "actuals": {
        "will_buy_insurance": False,
      },
    },
  ]
)
```

**Example: Logging batch raw inputs**

```python
apr_model.log_batch_raw_inputs(
  [
    {
      "id":"a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
      "raw_inputs": {
        "Age": 27,
        "Vehicle_Damage": "Yes",
        "Annual_Premium": 12345,
        "Vehicle_Age": ">2 years"
      },
    },
    {
      "id":"f2d1dccb-1aef-4955-a274-69e1acb8772f",
      "raw_inputs": {
        "Age": 54,
        "Vehicle_Damage": "No",
        "Annual_Premium": 54324,
        "Vehicle_Age": "<1 Year"
      },
    },
  ]
)
```

### Logging Pandas DataFrame / Series

If the data you wish to log is stored in a Pandas Series or DataFrame (with a single row), you can use the `aporia.pandas` utility API:

```python
from aporia.pandas.pandas_utils import pandas_to_dict

apr_model.log_prediction(
  id="a4dfcd4c-356c-4eed-8b93-b129b64fd55c",
  features=pandas_to_dict(features_dataframe),
  predictions={
    "will_buy_insurance": True,
  },
)
```

### Asynchronous logging

All of the logging functions described above log the data asynchronously to avoid blocking your program. If you wish to wait for the data to be sent, you can use the `flush` method:

```python
apr_model.flush()
```

### Troubleshooting

By default, the Aporia SDK is very silent: **it doesn't raise exceptions and doesn't write debug logs.** This was done because we never want to interrupt your application!

However, when first playing with the Aporia SDK, we highly recommend using the verbose argument, e.g:

```python
aporia.init(..., verbose=True)
```

This will print errors in a convenient way to make integration easier to debug. You can also pass `throw_errors=True`, which will make sure you aren't missing any errors.

If you have any further issues, please [contact us](mailto:support@aporia.com).

**Important:** Make sure to remove `throw_errors=True` before uploading to staging / production!

{% hint style="danger" %}
**Prediction isn't sent?**

If your application exits immediately after logging a prediction, the prediction might get discarded.

The reason for this is that predictions are added to a queue and are sent asynchronously.

In order to fix this, use the following API:

`apr_model.flush()`
{% endhint %}

## Pyspark

To log a Pyspark DataFrames directly, you can use the:

* `apr_model.log_batch_pyspark_prediction` for serving data
* `apr_model.log_pyspark_training_set` for training set
* `apr_model.log_pyspark_test_set` for test set

The API of these functions is similar to the `connect_serving` API (see [Data Sources - Overview](https://docs.aporia.com/v1/data-sources)).

Example:

```python
import aporia
aporia.init(host="<HOST>", 
            token="<TOKEN>", 
            environment="<ENVIRONMENT>", 
            verbose=True,
            raise_errors=True)


# Create a new model + model version in Aporia
model_id = aporia.create_model("my-model", "My Model")
apr_model = aporia.create_model_version(
    model_id=model_id,
    model_version="v1",
    model_type="binary",
    features={
      "f1": "numeric",
      "f2": "numeric",
      "f3": "numeric",
    },
    predictions={
      "score": "boolean",
    },
)

# Log training set
# We'll assume that there is a column in the dataframe for each feature / prediction
df_train = spark.sql("SELECT * FROM ...")
apr_model.log_pyspark_training_set(df)


# Load & log production data to Aporia
# We'll assume that there is a column in the dataframe for each feature / prediction
df = spark.sql("SELECT * FROM <>")
apr_model.log_batch_pyspark_prediction(
    data=df,

    # Names of the "ID" and "occurred_at" columns
    id_column="id",
    timestamp_column="occurred_at",

    # Map an prediction (from the schema) to a label
    labels={
        "<PREDICTION_NAME>": "<COLUMN_NAME>",
    },
)
```
