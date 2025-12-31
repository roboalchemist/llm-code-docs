# Source: https://docs.aporia.com/data-sources/redshift.md

# Source: https://docs.aporia.com/v1/data-sources/redshift.md

# Source: https://docs.aporia.com/data-sources/redshift.md

# Source: https://docs.aporia.com/v1/data-sources/redshift.md

# Redshift

This guide describes how to connect Aporia to an Redshift data source in order to monitor a new ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with Redshift SQL. This data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Create a IAM role for Redshift access

In order to provide access to Redshift, create a IAM role with the necessary API permissions.

First, create a JSON file on your computer with the following content:

```json
{
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": "redshift:GetClusterCredentials",
    "Resource": "arn:aws:redshift:<REGION>:<ACCOUNT_ID>:dbuser:<REDSHIFT_CLUSTER_NAME>/<DBUSER_NAME>"
  }
}
```

Make sure to replace the following placeholders:

* `<REGION>`: You can specify the Redshift AWS region or `*` for the default region.
* `<ACCOUNT_ID>`: The Redshift AWS account ID.
* `<REDSHIFT_CLUSTER_NAME>`: The Redshift cluster name.
* `<DBUSER_NAME>`: Name of the Redshift user.

For more information, see [Using IAM authentication to generate database user credentials](https://docs.aws.amazon.com/redshift/latest/mgmt/generating-user-credentials.html).

Next, create a new user in AWS with programmatic access only, and grant it the role you've just created. Create security credentials for it (access and secret keys) and use them in the next section.

{% hint style="info" %}
**IAM Authentication**

For authentication without security credentials (access key and secret key), please contact your Aporia account manager.&#x20;
{% endhint %}

### Creating an Redshift data source in Aporia

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

Each raw input, feature or prediction is mapped by default to the column of the same name in the Redshift query.

By creating a feature named `amount` or a prediction named `proba`, for example, the Redshift data source will expect a column in the Redshift query named `amount` or `proba`, respectively.

Next, create an instance of `RedshiftDataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
data_source = JDBCDataSource(
  url="jdbc:redshift:iam://<REDSHIFT_URL>:5439/company?AccessKeyID=<ACCESS_KEY>&SecretAccessKey=<SECRET_KEY>&DbUser=<DB_USER>&ssl=true&tcpKeepAlive=true",
  query="SELECT * FROM model_predictions",

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
