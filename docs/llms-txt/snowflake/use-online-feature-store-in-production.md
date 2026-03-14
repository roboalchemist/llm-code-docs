# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/feature-store/use-online-feature-store-in-production.md

# Use Snowflake online feature store in production

Snowflake ML Feature Store helps manage your features throughout the process of feature engineering.

For online applications that require low-latency inference, use the online feature store to serve your features.

The following sections go through productionizing the process of retrieving features within your Python application. These sections have
code examples that do the following:

1. Load the Iris dataset into Snowflake
2. Define the connection to Snowflake
3. Create the Feature Store and Feature Views
4. Retrieve the features and feature values
5. Generate predictions from your model

The code examples are written in Python. To go through this workflow for applications written in other languages, use a Snowflake driver
that’s specific to that language. For more information, see [Drivers](../../drivers.md).

## Prerequisites

To run online ML feature retrieval in Snowflake, you need the following:

* Data that you’ve already loaded into Snowflake
* A Snowflake feature store
* Feature views
* Online feature serving enabled for each feature view

You can use features from your own Snowflake feature store, but you can use the following code to load the Iris dataset into Snowflake if
you don’t already have a feature store.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import pandas as pd

from snowflake.snowpark.context import get_active_session

sf_session = get_active_session()

### Download the Iris dataset.

iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
# rename the columns to fit the Snowflake feature naming requirements
X.rename(columns={
    'sepal length (cm)': 'SEPAL_LENGTH_CM',
    'sepal width (cm)': 'SEPAL_WIDTH_CM',
    'petal length (cm)': 'PETAL_LENGTH_CM',
    'petal width (cm)': 'PETAL_WIDTH_CM'
}, inplace=True)
y = iris.target

### Load the data into Snowflake.
X = X.reset_index().rename(columns={"index": "ID"})
sepal_df = sf_session.write_pandas(
    X[['ID', 'SEPAL_LENGTH_CM', 'SEPAL_WIDTH_CM']],
    table_name="SEPAL_DATA",
    auto_create_table=True,
    overwrite=True
)
petal_df = sf_session.write_pandas(
    X[['ID', 'PETAL_LENGTH_CM', 'PETAL_WIDTH_CM']],
    table_name="PETAL_DATA",
    auto_create_table=True,
    overwrite=True
)
```

After you have the data in your environment, you create the feature store. The following code creates a feature store and the
`id_entity` entity for the different samples from the Iris dataset.

```python
### Install Snowflake ML
%pip install snowflake-ml-python==1.18.0

from snowflake.ml.feature_store import (
    FeatureStore,
    FeatureView,
    Entity,
    CreationMode,
)
from snowflake.ml.feature_store.feature_view import OnlineConfig

### Create Snowflake feature store

feature_store = FeatureStore(
    session=sf_session,
    database=sf_session.get_current_database(),
    name="MY_FEATURE_STORE",
    default_warehouse=sf_session.get_current_warehouse(),
    creation_mode=CreationMode.OR_REPLACE
)
sf_session.use_schema("MY_FEATURE_STORE")

id_entity = Entity(
    name='SAMPLE_ID',
    join_keys=["ID"],
    desc='sample id'
)
feature_store.register_entity(id_entity)
```

> **Note:**
>
> Snowflake ML Feature Store has the concept of entities. Entities are keys that organize features between feature views. For more information
> about entities, see [Working with entities](entities.md).

After you’ve created the feature store, you define the feature views. The following code defines the sepal and petal feature views from the
Iris dataset.

```python
### Create feature views with Online Serving.
sepal_fv = FeatureView(
    name='SEPAL_FEATURES',
    entities=[id_entity],
    feature_df=sepal_df,
    desc='Sepal features',
    refresh_freq='10 minutes',
    online_config=OnlineConfig(enable=True)
)
petal_fv = FeatureView(
    name='PETAL_FEATURES',
    entities=[id_entity],
    feature_df=petal_df,
    desc='Petal features',
    refresh_freq='10 minutes',
    online_config=OnlineConfig(enable=True)
)
sepal_fv = feature_store.register_feature_view(
    sepal_fv, version="v1", overwrite=True)
petal_fv = feature_store.register_feature_view(
    petal_fv, version="v1", overwrite=True)
```

## Retrieve the feature values

After you’ve registered the feature views and enabled online feature serving for each feature view, you can have the feature values from
each feature view served to your application.

To retrieve the feature values, you do the following:

1. Set up a connection to Snowflake
2. Create the session and Snowflake Feature Store objects that initialize when the application starts
3. Retrieve the features from your feature views
4. Create a prediction endpoint and get predictions from that endpoint

> **Important:**
>
> You must install `snowflake-ml-python>=1.18.0` into your application’s environment to use the Feature Store API.

To connect to Snowflake from your application, you must set up either a [Programmatic Access Token (PAT)](../../../user-guide/programmatic-access-tokens.md) or
[key-pair authentication](../../../user-guide/key-pair-auth.md) as an authentication method.

### Configure the client

When you initialize your application, it must connect to Snowflake ML Feature Store API and create the required Feature Store Python
objects.

Use the following sections to configure your client’s connection to the Snowflake ML Feature Store API.

### Configure a Programmatic Access Token (PAT)

Programmatic Access Token (PAT)Key Pair Authentication

Specify the following connection parameters in the following code to connect to Snowflake from your application:

* `schema` - the name of the Snowflake feature store
* `database` - the database containing the schema or feature store
* `role` - the role required to read from the feature store. For more information, see
  [Provide access to create and serve online features](create-and-serve-online-features-python.md).
* `password` - your PAT.

```python
import os

### Define connection parameters using PAT authentication.
snowflake_connection_parameters = {
    "account": "<account_identifier>",
    "user": "<user>",
    "password": pat,
    "role": "<FS_CONSUMER_ROLE>",
    "host": "<host>",
    "warehouse": "<warehouse>",
    "database": "<database>",
    "schema": "MY_FEATURE_STORE",
}
```

Specify the following connection parameters in the following code to connect to Snowflake from your application:

* `schema` - the name of the Snowflake feature store
* `database` - the database containing the schema or feature store
* `role` - the role required to read from the feature store. For more information, see
  [Create and serve online features](create-and-serve-online-features-python.md).
* `private_key_file` - the private key file
* `private_key_file_pwd` - the password to the private key file

```python
import os

### Define connection parameters for key-pair authentication.
snowflake_connection_parameters = {
    "account": "<account_identifier>",
    "user": "<user>",
    "private_key_file": "<private key file>",
    "private_key_file_pwd": "<private key file pwd>",
    "role": "<FS_CONSUMER_ROLE>",
    "host": "<host>",
    "warehouse": "<warehouse>",
    "database": "<database>",
    "schema": "MY_FEATURE_STORE",
}
```

**Create the Session and Feature Store Objects**

After you’ve defined your connection parameters, you create the session and Feature Store objects that your application uses to connect to
Snowflake.

The following code:

1. Creates the Snowflake Session, the client that your application uses to communicate with Snowflake.
2. Configures a thread pool executor to enable feature retrieval parallelism.
3. Lists the features that we’re retrieving from the feature store.
4. Initializes the feature store reader client. This object wraps the Snowflake session. It’s the main way your application interacts with the
   feature store.
5. Initializes the feature views that you’ve defined. You can replace these with your own features.

```python
import os
from concurrent.futures import ThreadPoolExecutor

from snowflake.snowpark.session import Session
from snowflake.ml.feature_store import FeatureStore, CreationMode

# 1.Start a Snowflake session
sf_session = Session.builder.configs(snowflake_connection_parameters).create()

# 2. Create a thread pool executor for feature store requests
MAX_WORKERS=os.cpu_count() * 2
executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

# 3. List individual features we are going to retrieve for inference. In this
#    example, we are listing Iris features described above in the
#    "Prerequisites" section.
PETAL_FEATURE_LIST = ["PETAL_WIDTH_CM", "PETAL_LENGTH_CM"]
SEPAL_FEATURE_LIST = ["SEPAL_WIDTH_CM", "SEPAL_LENGTH_CM"]

# 4. Initialize feature store consumer client
feature_store = FeatureStore(
    session=sf_session,
    database=sf_session.get_current_database(),
    name="MY_FEATURE_STORE",
    default_warehouse="<warehouse>",
    creation_mode=CreationMode.FAIL_IF_NOT_EXIST
)

# 5. Initialize the feature views
sepal_fv = feature_store.get_feature_view("SEPAL_FEATURES", version="v1")
petal_fv = feature_store.get_feature_view("PETAL_FEATURES", version="v1")
```

## Retrieve the online features on the serving path

After you’ve defined how the application initializes, you can create a prediction endpoint.

There are different ways where you can define how your application handles requests. The following Python code:

* Defines the prediction endpoint in your application
* Takes the keys from the JSON request
* Uses the keys to retrieve the feature values from the feature views
* Passes those feature values to the model
* Gets the predictions from the model
* Returns the predictions in the response

```python
from snowflake.ml.feature_store.feature_view import StoreType
import json
import flask

def _retrieve_features(
    feature_view: FeatureView,
    keys: List[int],
    feature_names: List[str]):
    """Retrieve features from the given feature view"""

    return feature_store.read_feature_view(
        feature_view,
        keys=[keys],
        feature_names=feature_names,
        store_type=StoreType.ONLINE  # Query the ONLINE store
    ).collect()

@app.route("/prediction-endpoint", methods=["POST"])
def prediction():
    if flask.request.content_type == 'application/json':
        input_data = flask.request.data.decode("utf-8")
        input_data = json.loads(data)
    else:
        return flask.Response(
            response="This predictor only supports JSON data",
            status=415,
            mimetype="text/plain"
        )

    # Expect that input data is a single key
    keys = [int(input_data["key"])]

    # Retrieve features from two feature views in parallel.
    sepal_features = executor.submit(
        _retrieve_features, sepal_fv, keys, SEPAL_FEATURE_LIST)
    petal_features = executor.submit(
        _retrieve_features, petal_fv, keys, PETAL_FEATURE_LIST)

    sepal_features = sepal_features.result()
    petal_features = petal_features.result()

    predictions = []
    if len(sepal_features) != 0 and len(petal_features) != 0:
        # Compose the feature vector, excluding the join keys.
        feature_vector = (
            list(sepal_features[0][1:])
            + list(petal_features[0][1:])
        )

        # Using a hypothetical run_inference function.
        predictions = run_inference(feature_vector)

    result = json.dumps({"results": list(predictions)})
    return flask.Response(response=result, status=200,
        mimetype="application/json")
```

The preceding code calls a hypothetical `run_inference` function. Your own inference function could get predictions from your model
regardless of whether it’s hosted remotely or in application memory.

The prediction endpoint in the preceding code accepts a key and returns the prediction for that key. Your data might have multiple keys
characterizing a single sample. The preceding code is meant to be an example that you can adapt to your own use case.

## Related content

* [Create and serve online features](create-and-serve-online-features-python.md)
* [Snowflake Feature Store](overview.md)
* [Feature Store SQL commands](../../../sql-reference/commands-feature-store.md)
* [Online feature store Notebook examples](https://github.com/Snowflake-Labs/sf-samples/tree/main/samples/ml/feature_store)
