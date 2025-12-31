# Source: https://docs.aporia.com/model-types/multiclass-classification.md

# Source: https://docs.aporia.com/v1/model-types/multiclass-classification.md

# Source: https://docs.aporia.com/model-types/multiclass-classification.md

# Source: https://docs.aporia.com/v1/model-types/multiclass-classification.md

# Multiclass Classification

Multiclass classification models predict one of more than two outcomes. In Aporia, these models are represented with the `multiclass` model type.

Examples of multiclass classification problems:

* Is this product a book, movie, or clothing?
* Is this movie a romantic comedy, documentary, or thriller?
* Which category of products is most interesting to this customer?

Frequently, multiclass models output a confidence value or a score for each class.

### Integration

To monitor a multiclass model, create a new model version with a `string` field representing the predicted class, and optionally a `dict` field with the probabilities for all classes:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="multiclass"
  features={
     ...
  },
  predictions={
    "product_type": "string",
    "proba": "dict"
  },
)
```

Next, connect to a data source or manually log predictions like so:

```python
apr_model.log_prediction(
  id="<PREDICTION_ID>",
  features={
    ...
  },
  predictions={
    "product_type": "book",
    "proba": {
        "book": 0.8,
        "movie": 0.1,
        "clothing": 0.1
    }
  },
)
```

To log actuals for this prediction:

```python
apr_model.log_actuals(
  id="<PREDICTION_ID>",
  actuals={
    "product_type": "book",
    "proba": {
        "book": 1.0,
        "movie": 0.0,
        "clothing": 0.0,
    },
  },
)
```

If you don't need to monitor probabilities, you may omit the `proba` field.
