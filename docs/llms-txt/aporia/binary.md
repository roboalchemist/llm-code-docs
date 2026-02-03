# Source: https://docs.aporia.com/model-types/binary.md

# Source: https://docs.aporia.com/v1/model-types/binary.md

# Binary Classification

Binary classification models predict a binary outcome (one of two possible classes). In Aporia, these models are represented by the binary model type.

Examples of binary classification problems:

* Will the customer `buy` this product or `not_buy` this product?
* Is this email `spam` or `not_spam`?
* Is this review written by a `customer` or a `robot`?

Frequently, binary models output not only a yes/no answer, but also a *probability*.

### Example: Boolean Decision without Probability

If you have a model with a yes/no decision but without a probability value, then your database may look like the following:

<table><thead><tr><th width="76">id</th><th width="132">feature1 (numeric)</th><th width="141">feature2 (boolean)</th><th width="122">decision (boolean)</th><th>label (boolean)</th><th width="191">timestamp (datetime)</th></tr></thead><tbody><tr><td>1</td><td>13.5</td><td>True</td><td>True</td><td>True</td><td>2014-10-19 10:23:54</td></tr><tr><td>2</td><td>-8</td><td>False</td><td>False</td><td>True</td><td>2014-10-19 10:24:24</td></tr></tbody></table>

To monitor this model, we will create a new model version with a schema that include a `boolean` prediction:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="binary"
  features={
     ...
  },
  predictions={
    "decision": "boolean",
  },
)
```

To connect this model to Aporia from your data source, call the `connect_serving(...)` API:&#x20;

```python
apr_model.connect_serving(
  data_source=my_data_source,

  id_column="id",
  timestamp_column="timestamp",

  # Map the "label" column as the label for the "decision" prediction. 
  labels={
    # Prediction name -> Column name
    "decision": "label"
  }
)
```

Check out the [Data Sources](https://docs.aporia.com/v1/data-sources) section for further reading on the available data sources and how to connect to each one of them.

### Example: Boolean Decision with Probability

If you have a model with a yes/no decision *and* a probability / confidence value for it, then your database may look like the following:

<table><thead><tr><th width="82">id</th><th width="116">feature1 (numeric)</th><th width="112">feature2 (boolean)</th><th width="112">proba (numeric)</th><th width="138">decision (boolean)</th><th width="122">label (boolean)</th><th width="196">timestamp (datetime)</th></tr></thead><tbody><tr><td>1</td><td>13.5</td><td>True</td><td>0.8</td><td>True</td><td>True</td><td>2014-10-19 10:23:54</td></tr><tr><td>2</td><td>-8</td><td>False</td><td>0.5</td><td>False</td><td>True</td><td>2014-10-19 10:24:24</td></tr></tbody></table>

To monitor this model, it's recommended to create a new model version with a schema that includes the final decision as `boolean` field, and the probability as a `numeric` field:

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="binary"
  features={
     ...
  },
  predictions={
    "decision": "boolean",
    "proba": "numeric",
  },
)
```

To connect the model to Aporia from a data source, call the `connect_serving(...)` API:&#x20;

```python
apr_model.connect_serving(
  data_source=my_data_source,
    
  id_column="id",
  timestamp_column="timestamp",

  # Map the "label" column as the label for "decision" and "proba". 
  labels={
    # Prediction name -> Column name representing 
    "decision": "label",
    "proba": "label",
  }
)
```

Check out the [Data Sources](https://docs.aporia.com/v1/data-sources) section for further reading on the available data sources and how to connect to each one of them.

### Example: Probability Only

In cases when there is no threshold for your boolean prediction, and the final business result is actually a probability, you may simply omit the `decision` field from the examples in the previous section and only include the `proba` field for your prediction.&#x20;

{% hint style="info" %}
**Don't want to connect to a database?**

Don't worry - you can [log your predictions directly to Aporia.](https://docs.aporia.com/v1/storing-your-predictions/logging-to-aporia-directly)
{% endhint %}
