# Source: https://docs.aporia.com/model-types/regression.md

# Source: https://docs.aporia.com/v1/model-types/regression.md

# Source: https://docs.aporia.com/model-types/regression.md

# Source: https://docs.aporia.com/v1/model-types/regression.md

# Regression

Regression models predict a `numeric` value. In Aporia, these models are represented with the `regression` model type.

Examples of regression problems:

* What will the temperature be in Seattle tomorrow?
* For product X, how many units will sell?
* How many days until this customer stops using the application?
* What price will this house sell for?

### Integration

Regression predictions are usually represented in a database with a `numeric` column. For example:

<table><thead><tr><th width="93">id</th><th width="116">feature1 (numeric)</th><th width="121">feature2 (boolean)</th><th width="215">predicted_temperature (numeric)</th><th width="190">actual_temperature (numeric)</th><th width="193">timestamp (datetime)</th></tr></thead><tbody><tr><td>1</td><td>13.5</td><td>True</td><td>22.83</td><td>24.12</td><td>2017-01-01 12:00:00</td></tr><tr><td>2</td><td>123</td><td>False</td><td>26.04</td><td>25.99</td><td>2017-01-01 12:01:00</td></tr><tr><td>3</td><td>42</td><td>True</td><td>29.01</td><td>11.12</td><td>2017-01-01 12:02:00</td></tr></tbody></table>

To monitor this model, we will create a new model version with a schema that includes a `numeric` prediction:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>", # You will need to create a model with this MODEL_ID in advance
  model_version="v1",
  model_type="regression"
  features={
     ...
  },
  predictions={
    "predicted_temperature": "numeric",
  },
)
```

To connect this model to Aporia from your data source, call the `connect_serving(...)` API:&#x20;

```python
apr_model.connect_serving(
  data_source=my_data_source,

  id_column="id",
  timestamp_column="timestamp",

  # Map the actual_temperature column as the label for the 
  # predicted_temperature. 
  labels={
    # Prediction name -> Column name
    "predicted_temperature": "actual_prediction"
  }
)
```

Check out the [data sources section](https://docs.aporia.com/v1/data-sources) for more information about how to connect all other available data sources.

{% hint style="info" %}
**Don't want to connect to a database?**

Don't worry - you can [log your predictions directly to Aporia.](https://docs.aporia.com/v1/storing-your-predictions/logging-to-aporia-directly)
{% endhint %}
