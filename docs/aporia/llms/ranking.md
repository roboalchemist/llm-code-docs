# Source: https://docs.aporia.com/model-types/ranking.md

# Source: https://docs.aporia.com/v1/model-types/ranking.md

# Ranking

Ranking models are often used in recommendation systems, ads, search engines, etc. In Aporia, these models are represented with the `ranking` model type.

### Integration

If you have a ranking or recommendations model, then your database may look like the following:

<table><thead><tr><th width="80">id</th><th width="115">feature1 (numeric)</th><th width="114">feature2 (boolean)</th><th width="221">scores (array)</th><th width="210">relevance (array)</th><th width="194">timestamp (datetime)</th></tr></thead><tbody><tr><td>1</td><td>13.5</td><td>True</td><td><code>[9, 8, 10, ...]</code></td><td><code>[2, 0, 1, ...]</code></td><td>2014-10-19 10:23:54</td></tr><tr><td>2</td><td>-8</td><td>False</td><td><code>[4.5, 8.7, 9, ...]</code></td><td><code>[0, 1, 2, ...]</code></td><td>2014-10-19 10:24:24</td></tr></tbody></table>

To monitor a ranking model, create a new model version with an `array` field(s):

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>", # You will need to create a model with this MODEL_ID in advance
  model_version="v1",
  model_type="ranking"
  features={
     ...
  },
  predictions={
    "scores": "array"
  },
)
```

To connect your data source to this model in Aporia, please call the `connect_serving(...)` API:&#x20;

```python
apr_model.connect_serving(
  data_source=my_data_source,

  id_column="id",
  timestamp_column="timestamp",

  predictions={
    # Prediction name -> Column name representing 
    "relevance": "scores"
  }
)
```

Check out the [Data Sources](https://docs.aporia.com/v1/data-sources) section for further reading on the available data sources and how to connect to each one of them.
