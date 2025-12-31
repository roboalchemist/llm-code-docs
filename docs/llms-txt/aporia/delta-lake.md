# Source: https://docs.aporia.com/data-sources/delta-lake.md

# Source: https://docs.aporia.com/v1/data-sources/delta-lake.md

# Source: https://docs.aporia.com/data-sources/delta-lake.md

# Source: https://docs.aporia.com/v1/data-sources/delta-lake.md

# Delta Lake

This guide describes how to connect Aporia to a [Delta Lake](https://delta.io/) data source in order to monitor a new ML Model in production. We will assume that your model inputs, outputs, and optionally delayed actuals are stored in Delta Lake.

This data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Create a IAM role for S3 access

In order to provide access to Athena, create a IAM role with the necessary API permissions.

First, create a JSON file on your computer with the following content:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
		        "s3:ListBucket",
                "s3:GetObject*"
            ],
            "Resource": [
                "arn:aws:s3:::<BUCKET_NAME>",
                "arn:aws:s3:::<BUCKET_NAME>/*"
            ]
        }
    ]
}
```

Make sure to replace `<BUCKET_NAME>` with the name of the relevant S3 bucket.

### Creating an S3 data source in Aporia

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

Each raw input, feature or prediction is mapped by default to the column of the same name in the Athena query.

By creating a feature named `amount` or a prediction named `proba`, for example, the S3 data source will expect a column in the file named `amount` or `proba`, respectively.

Next, create an instance of `S3DataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
data_source = S3DataSource(
  object_path="s3://my-bucket/my-file.parquet"
  object_format="delta",

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
