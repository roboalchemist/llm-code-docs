# Source: https://docs.aporia.com/data-sources/snowflake.md

# Source: https://docs.aporia.com/v1/data-sources/snowflake.md

# Snowflake

This guide describes how to connect Aporia to a Snowflake data source in order to monitor a new ML Model in production.&#x20;

We will assume that your model inputs, outputs and optionally delayed actuals can be queried with Snowflake SQL. This data source may also be used to connect to your model's training/test set to be used as a baseline for model monitoring.

### Create a Service Account for Snowflake access

In order to provide access to Snowflake, read-only service account for Aporia in Snowflake.

Please use the SQL snippet below to create a service account for Aporia. Before using the snippet, you will need to populate the following:

* `<aporia_password>`: Strong password to be used by the service account user.
* `<your_database>`: Snowflake database with your ML training / inference data.

```sql
-- Configuration
set aporia_username='APORIA';
set aporia_password='<aporia_password>';
set aporia_role_name='APORIA_ROLE';
set dbname='<your_database>';

-- Set role for grants
USE ROLE ACCOUNTADMIN;

-- Create the role Aporia will use
CREATE ROLE IF NOT EXISTS identifier($aporia_role_name);

-- Create Aporia's user and grant access to role
CREATE USER IF NOT EXISTS identifier($aporia_username) PASSWORD=$aporia_password DEFAULT_ROLE=$aporia_role_name;
GRANT ROLE identifier($aporia_role_name) TO USER identifier($aporia_username);

-- Grant read-only privileges to the database
GRANT SELECT ON ALL TABLES IN DATABASE identifier($dbname) TO ROLE identifier($aporia_role_name);
GRANT SELECT ON ALL VIEWS IN DATABASE identifier($dbname) TO ROLE identifier($aporia_role_name);

USE DATABASE identifier($dbname);
```

### Creating an Snowflake data source in Aporia

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

Each raw input, feature or prediction is mapped by default to the column of the same name in the Snowflake query.

By creating a feature named `amount` or a prediction named `proba`, for example, the Snowflake data source will expect a column in the Snowflake query named `amount` or `proba`, respectively.

Next, create an instance of `SnowflakeDataSource` and pass it to `apr_model.connect_serving(...)` or `apr_model.connect_training(...)`:

```python
data_source = SnowflakeDataSource(
  url="<SNOWFLAKE_URL>",
  query='SELECT * FROM "my_db"."model_predictions"',
  user="APORIA",
  password="<SNOWFLAKE_PASSWORD>",
  database="<DATABASE_NAME>",
  schema="<DATABASE_SCHEMA>",
  warehouse="<WAREHOUSE_NAME>",  # Optional

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
