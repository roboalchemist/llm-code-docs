# Source: https://docs.aporia.com/data-sources/athena.md

# Source: https://docs.aporia.com/v1/data-sources/athena.md

# Athena

This guide describes how to connect Aporia to an Athena data source in order to monitor a new ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with Athena SQL. This data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Create a workgroup for Aporia queries

Create a workgroup for Aporia to use to perform queries, see instructions [here](https://docs.aws.amazon.com/athena/latest/ug/workgroups-procedure.html).

An S3 location (bucket and folder) to which query results will be written must be designated. It is recommended that the bucket be in the same region as the catalog that Athena uses.

### Create a IAM role for Athena access

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
                "s3:GetBucketLocation"
            ],
            "Resource": [
                "arn:aws:s3:::<data-bucket>",
                "arn:aws:s3:::<results-bucket>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "s3:GetObject",
            "Resource": [
                "arn:aws:s3:::<data-bucket>/*",
                "arn:aws:s3:::<results-bucket>/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "s3:PutObject",
            "Resource": [
                "arn:aws:s3:::<results-bucket>/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "athena:StartQueryExecution",
                "athena:StopQueryExecution",
                "athena:GetQueryResults"
            ],
            "Resource": "arn:aws:athena:<region>:<account-id>:workgroup/<aporia-workgroup>"
        },
        {
            "Effect": "Allow",
            "Action": "athena:ListWorkGroups",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "athena:ListDatabases",
            "Resource": [
                "arn:aws:athena:<region>:<account-id>:datacatalog/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "glue:GetDatabases",
            "Resource": [
                "arn:aws:glue:<region>:<account-id>:catalog",
                "arn:aws:glue:<region>:<account-id>:database/<database-name>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "athena:GetQueryExecution",
                "athena:BatchGetQueryExecution",
                "athena:ListQueryExecutions",
                "athena:GetWorkGroup"
            ],
            "Resource": [
                "arn:aws:athena:<region>:<account-id>:workgroup/*",
                "arn:aws:athena:<region>:<account-id>:datacatalog/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "glue:GetTables",
                "glue:GetTable",
                "glue:GetPartitions",
                "glue:GetPartition"
            ],
            "Resource": [
                "arn:aws:glue:<region>:<account-id>:catalog",
                "arn:aws:glue:<region>:<account-id>:database/<database-name>",
                "arn:aws:glue:<region>:<account-id>:table/<database-name>/*"
            ]
        }
    ]
}
```

Make sure to replace the following placeholders:

* `<region>`: You can specify the Athena AWS region or `*` for the default region.
* `<account-id>`: The Athena AWS account ID.
* `<data-bucket>`: The S3 bucket storing the data for your Athena tables - if more than one bucket, just add the others to the resource list as well.
* `<database-name>`: You can specify one or more database names or use `*` to give Aporia access to all Athena databases.
* `<aporia-workgroup>`: The workgroup created on the previous step.
* `<results-bucket>`: The bucket configured for the workgroup.

Next, create a new user in AWS with programmatic access only, and grant it the role you've just created. Create security credentials for it (access and secret keys) and use them in the next section.

{% hint style="info" %}
**IAM Authentication**

For authentication without security credentials (access key and secret key), please contact your Aporia account manager.
{% endhint %}

### Creating an Athena data source in Aporia

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

By creating a feature named `amount` or a prediction named `proba`, for example, the Athena data source will expect a column in the Athena query named `amount` or `proba`, respectively.

Next, create an instance of `AthenaDataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
data_source = AthenaDataSource(
  url="jdbc:awsathena://AwsRegion=us-east-1",
  query='SELECT * FROM "my_db"."model_predictions"',
  user="<AWS_ACCESS_KEY_ID>",
  password="<AWS_SECRET_ACCESS_KEY>",
  s3_output_location="s3://my-athena-bucket",

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
