# Source: https://docs.aporia.com/introduction/quickstart.md

# Source: https://docs.aporia.com/v1/introduction/quickstart.md

# Quickstart

With just a few lines of code, any Machine Learning model can be integrated and monitored in production with Aporia.

![Quickstart](https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FjFCV3GyHcgQt0GwHanVe%2Fquickstart.gif?alt=media)

In this guide, we will use Aporia's Python API to create a model in Aporia and log its predictions.

### Install the Aporia SDK

To get started, install the Aporia Python library:

```
pip3 install aporia --upgrade
```

Next, import and initialize the Aporia library:

```python
import aporia
aporia.init(token="<TOKEN>",
            environment="<ENVIRONMENT>",  # e.g prod
            verbose=True,
            raise_errors=True)
```

### Create Model

To create a new model to be monitored in Aporia, you can call the `aporia.create_model(...)` API:

```python
aporia.create_model("<MODEL_ID>", "<MODEL_NAME>")
```

This API will not recreate the model if the model ID already exists. You can also specify color, icon, tags and model owner:

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

```python
apr_model = aporia.create_model_version(
    model_id="<MODEL_ID>",
    model_version="v1",
    model_type="binary"
    
    features={
        "amount": "numeric",
        "owner": "string",
        "is_new": "boolean",
        "created_at": "datetime",
        "embeddings": {"type": "tensor", "dimensions": [768]},
    },

    predictions={
        "will_buy_insurance": "boolean",
        "proba": "numeric",
    },
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

### Log Predictions

Next, we will log some predictions to the newly created model version. These predictions will be kept in an Aporia-managed database.

In production, **we strongly recommend** [**storing your model's predictions in your own database**](https://docs.aporia.com/v1/storing-your-predictions) **that you have complete control over**- we've seen many of our customers do this anyway for retraining, auditing, and other purposes.

Aporia can then connect to your data directly and use it for model observability, stripping away the need for data duplication. However, this quickstart assumes you have no database and would simply like to log model inferences:

```python
apr_model.log_prediction(
    id=<PREDICTION_ID>,
    features={
        "amount": 15.3,
        "owner": "Joe",
        "is_new": True,
        "created_at": datetime.now(),
        "embeddings": [...],
    },
    predictions={
        "will_buy_insurance": True,
        "proba": 0.55,
    },
)
```

You must specify an ID for each prediction. This ID can later be used to log the prediction's actual value. If you don't care about this, just pass `str(uuid.uuid4())` as the prediction ID.

Both of these APIs are entirely asynchronous. This was done to avoid blocking your application, which may handle a large number of predictions per second.

You can now access Aporia and see your model, as well as create dashboards and monitors for it!
