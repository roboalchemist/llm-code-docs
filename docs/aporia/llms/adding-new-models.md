# Source: https://docs.aporia.com/ml-monitoring-as-code/adding-new-models.md

# Adding new models

## Overview

To add a new model to Aporia using the Python SDK, you'll need to:

1. **Define serving dataset** - This will include the SQL query or path to your serving / inference data.
2. **Define training dataset&#x20;*****(optional)*****&#x20;-** This will include the SQL query or path to your model's training set.&#x20;
3. **Define a model resource** - The model resource will include the display name and type of the model in Aporia, as well as the link to different versions and their serving / training datasets. &#x20;

### Initialization

Start by creating a new Python file with the following initialization code:

```python
import datetime
import os

from aporia import Aporia, MetricDataset, MetricParameters, TimeRange
import aporia.as_code as aporia

aporia_token = os.environ["APORIA_TOKEN"]
aporia_account = os.environ["APORIA_ACCOUNT"]
aporia_workspace = os.environ["APORIA_WORKSPACE"]

stack = aporia.Stack(
    host="https://platform.aporia.com",  # or "https://platform-eu.aporia.com"
    token=aporia_token,
    account=aporia_account,
    workspace=aporia_workspace,
)

# <Your model definition code goes here>


stack.apply(yes=True, rollback=False, config_path="config.json")

```

## Defining Datasets

To add a new model to Aporia, start by defining a dataset. Datasets can be used to specify the SQL query or file path for model monitoring.

There are currently two types of datasets in Aporia:

* **Serving dataset** - Includes the features and predictions of your model in production, as well as any other metadata you'd like to add for observability.&#x20;
  * The serving dataset can also include delayed labels / actuals, and Aporia will make sure to refresh this data when it's updated. This is used to calculate performance metrics such as AUC ROC, nDCG\@k, and so on.
* **Training dataset (optional)** - Includes the features, predictions, and labels of your model during training set.

```python
serving_dataset = aporia.Dataset(
  "my-model-serving",
  
  # Dataset type - can be "serving" or "training"
  type="serving",
  
  # Data source name from the "Integrations" page in Aporia
  # If you prefer to define data source as code, use the aporia.DataSource(...) API.
  data_source_name="MY_SNOWFLAKE",
  
  # SQL query or S3 path
  connection_data={
    "query": "SELECT * FROM model_predictions"
  },
  
  # Column to be used as a unique prediction ID
  id_column="prediction_id",
  
  # Column to be used as the prediction timestamp
  timestamp_column="prediction_timestamp"
  
  # Raw inputs are used to represent any metadata about the prediction.
  # Optional
  raw_inputs={
    "prediction_latency": "numeric",
    "raw_text": "text",
  },
  
  # Features
  features={
    "age": "numeric",
    "gender": "categorical",
    "text_embedding": "embedding",
    "image_embedding": "embedding",
  },
  
  # Predictions
  predictions={
    "score": "numeric",
  },
  
  # Delayed labels
  actuals={
    "purchased": "boolean",
  },
  actual_mapping={"purchased": "score"},
)
```

While the dataset represents a specific query or file that's relevant to a specific model, a **data source** includes the connection string data (e.g user, role, etc.).&#x20;

A data source can be shared across many different datasets. A data source is often created once, while datasets are added every time a new model is added.

The name of the data source should be identical to a data source that exists in the Integrations page in Aporia.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FJIa79H5oLTww6PTcDixA%2Fimage.png?alt=media&#x26;token=6c33ee8e-b0d3-45ec-af9b-baf96b87905c" alt=""><figcaption></figcaption></figure>

If you're using an SQL-based data source such as Databricks, Snowflake, Postgres, Glue Data Catalog, Athena, Redshift, or BigQuery, then the format of `connection_data` should be a dict with a `query` key as shown in the code example above.&#x20;

If you're using a file data source like S3, Azure Blob Stroage, or Google Cloud Storage, the `connection_data` dictionary should look like this:

```python
aporia.Dataset(
  ...,
  
  connection_data={
    # Files to read
    "regex": "my-model/v1/*.parquet",
    
    # Format of the file
    "object_format": "parquet" # Can also be "csv" / "delta" / "json",
    
    # For CSV, Read the first line of the file as column names? (optional)    
    # "header": true
  }
)
```

### Column Mapping

Aporia uses a simple dictionary format to map between column names to features, predictions, raw inputs, and actuals.

Here's a table to describe the different type of field groups that exist within Aporia:

<table><thead><tr><th width="154">Group</th><th width="353.3333333333333">Description</th><th>Required</th></tr></thead><tbody><tr><td>Features</td><td>Inputs to the model</td><td>Yes</td></tr><tr><td>Predictions</td><td>Outputs from the model</td><td>Yes</td></tr><tr><td>Raw Inputs</td><td>Any metadata about the prediction. Examples:<br><br>* Prediction latency<br>* Raw text<br>* Gender - might not be a feature of the model, but you still want to monitor for bias &#x26; fairness, so this is a good fit for raw inputs</td><td>No</td></tr><tr><td>Actuals</td><td>Delayed feedback after the prediction, used to calculate performance metrics.</td><td>No</td></tr></tbody></table>

You can specify each of these field groups as a Python dictionary in the `aporia.Dataset(...)` parameters. The key represents the column name from the file / SQL query, and the value represents the data type:

```
aporia.Dataset(
  ...,
  features={
    # columnName -> dataType
    "age": "numeric",
  }
)
```

### Data Types

Each column can be one of the following data types:

<table><thead><tr><th width="148">Data Type</th><th width="316.3333333333333">Description</th><th>Value examples</th></tr></thead><tbody><tr><td>numeric</td><td>Any continuous variable (e.g score, age, and so on).</td><td>53.4, 0.05, 20</td></tr><tr><td>categorical</td><td>Any discrete variable (e.g gender, country, state, etc.).</td><td>"US", "California", "5"</td></tr><tr><td>boolean</td><td>Any boolean value</td><td>true, false, 0, 1</td></tr><tr><td>datetime</td><td>Any datetime value</td><td>timestamp objects</td></tr><tr><td>text</td><td>Raw text</td><td>"Hello, how are you?"</td></tr><tr><td>array</td><td>List of discrete categories</td><td>["flight1911", "flight2020"]</td></tr><tr><td>embedding</td><td>Numeric vectors</td><td>[0.58201, 0.293948, ...]</td></tr><tr><td>image_url</td><td>Image URLs</td><td>https://my-website.com/img.png</td></tr></tbody></table>

### Actuals / Delayed Labels

To calculate performance metrics in Aporia, you can add actuals (or delayed labels) to the prediction data.&#x20;

While usually this data is not in the same table as the prediction data, you can use a SQL `JOIN` query to merge between the feature / prediction data and actuals. Aporia will take care of refreshing the data when it is updated. If you don't have actuals for a prediction yet, the value for the acshould be NULL. Therefore, it's often very common to use a `LEFT JOIN` query like this:

```sql
SELECT * FROM model_predictions
LEFT JOIN model_actuals USING prediction_id
```

Then, you can use the `actuals` and `actual_mapping` parameters when creating a dataset:

```python
serving_dataset = aporia.Dataset(
  predictions={
    "recommended_items": "array",
  },
  actuals={
    "relevant_items": "array",
  },
  actual_mapping={
    # Actual name -> Prediction name
    "relevant_items": "recommended_items"
  },
)
```

## Defining models

Next, to define a model simply create an `aporia.Model` object with links to the relevant datasets, and add it to your stack:

```python
model_version = aporia.Version(
    "model_version_v1.0.0",
    serving=serving_dataset,
    training=training_dataset,
    name="v1.0.0",
)

model = aporia.Model(
    "My Model",
    type=aporia.ModelType.RANKING,
    versions=[model_version],
)

stack.add(model)
stack.apply(yes=True, rollback=False, config_path="model.json")
```
