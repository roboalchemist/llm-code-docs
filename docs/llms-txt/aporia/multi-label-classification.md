# Source: https://docs.aporia.com/model-types/multi-label-classification.md

# Source: https://docs.aporia.com/v1/model-types/multi-label-classification.md

# Source: https://docs.aporia.com/model-types/multi-label-classification.md

# Source: https://docs.aporia.com/v1/model-types/multi-label-classification.md

# Multi-Label Classification

Multi-label classification models predict multiple outcomes. In Aporia, these models are represented with the `multi-label` model type.

Examples of multi-label classification problems:

* Is this song sad, happy, funny, rock, jazz, or all simultaneously?
* Does this movie belong to one or more of the 'romantic', 'comedy', 'documentary', 'thriller' categories, or all simultaneously?

### Integration

To monitor a multi-label model, create a new model version with a `dict` field where keys are different labels and values are the probabilities for each label:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="multi-label"
  features={
     ...
  },
  predictions={
    "genres": "dict"
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
    "genres": {
        "action": 0.8,
        "horror": 0.7,
        "thriller": 0.9,
        "drama": 0.2,
        ...
    }
  },
)
```

If you don't have probabilities for each label, you can log zeros and ones instead. To log actuals for this prediction:

```python
apr_model.log_actuals(
  id="<PREDICTION_ID>",
  actuals={
    "genres": {
        "action": 1.0,
        "horror": 1.0,
        "thriller": 1.0,
        "drama": 0.0,
        ...
    }
  },
)
```

You can also log multiple `dict` fields if you have a multi-multi-label model :)
