# Source: https://docs.aporia.com/v1/data-sources/bigquery.md

# BigQuery

This guide describes how to connect Aporia to a BigQuery data source in order to monitor a new ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals are stored in a BigQuery table, or can be queried with a BigQuery view.

The BigQuery data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Creating a service account

First, create a read-only service account for Aporia:

1. Under *IAM & Admin*, go to the *Service Accounts* section in your Google Cloud Platform console.
2. Click the *Create Service Account* button at the top of the tab.
3. Give the account a name and continue. We recommend naming the account "aporia".
4. Assign the `roles/bigquery.jobUser` role to the service account.
5. Click the *Create Key* button, select JSON as the type and click *Create*. A JSON file will be downloaded – please keep it safe.
6. Click *Done* to complete the creation of Aporia’s service account.

Next, add permissions to the relevant tables / views:

1. Go to the BigQuery service in your Google Cloud Platform console.
2. In the *Explorer* panel, expand your project and select a dataset.
3. Expand the dataset and select a table or view.
4. Click *Share*.
5. On the Share tab, Click *Add Principal*.
6. In *New principals*, enter the name of the Service Account you've created for Aporia in the previous step.
7. Select the `roles/bigquery.dataViewer` role.
8. Click *Save* to save the changes for the new user.

{% hint style="info" %}
**ServiceAccount credentials**

For authentication without service account credentials, please contact your Aporia account manager.
{% endhint %}

### Creating a BigQuery data source in Aporia

To create a new model to be monitored in Aporia, you can call the `aporia.create_model(...)` API:

```python
aporia.create_model("<MODEL_ID>", "<MODEL_NAME>")
```

Each model in Aporia contains different **Model Versions**. When you (re)train your model, you should create a new model version in Aporia.

```python
apr_model = aporia.create_model_version(
  model_id="<MODEL_ID>",
  model_version="v1",
  model_type="binary"
  
  raw_inputs={
    "raw_text": "text",
  },

  features={
    "amount": "numeric",
    "owner": "string",
    "is_new": "boolean",
    "embeddings": {"type": "tensor", "dimensions": [768]},
  },

  predictions={
    "will_buy_insurance": "boolean",
    "proba": "numeric",
  },
)
```

Each raw input, feature or prediction is mapped by default to the column of the same name in the BigQuery table or view.

By creating a feature named `amount` or a prediction named `proba`, for example, the BigQuery data source will expect a column in the BigQuery table named `amount` or `proba`, respectively.

If your data format does not fit exactly, you can use [BigQuery Views](https://cloud.google.com/bigquery/docs/views) to shape it in any way you want.

Next, create an instance of `BigQueryDataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
data_source = BigQueryDataSource(
  credentials_base64=base64.b64encode("<SERVICE_ACCOUNT_JSON>"),

  # Instead of table, you can also use a BigQuery view for custom queries
  table="my_model",
  dataset="<DATASET>",                     # Optional
  project="<PROJECT_NAME>",                # Optional
  parent_project="<PARENT_PROJECT_NAME>",  # Optional

  # Optional - use the select_expr param to apply additional Spark SQL 
  select_expr=["<SPARK_SQL>", ...],

  # Optional - use the read_options param to apply any Spark configuration
  # (e.g custom Spark resources necessary for this model)
  read_options={...}
)

apr_model.connect_serving(
  data_source=data_source,

  # Names of the prediction ID and prediction timestamp columns
  id_column="prediction_id",
  timestamp_column="prediction_timestamp",
)
```

Note that as part of the `connect_serving` API, you are required to specify additional 2 columns:

* `id_column` - A unique ID to represent this prediction.
* `timestamp_column` - A column representing when did this prediction occur.

### What's Next

For more information on:

* Advanced feature / prediction <-> column mapping
* How to integrate delayed actuals
* How to integrate training / test sets

Please see the [Data Sources Overview](https://docs.aporia.com/v1/data-sources) page.
