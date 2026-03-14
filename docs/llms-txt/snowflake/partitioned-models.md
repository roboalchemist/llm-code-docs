# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/model-registry/partitioned-models.md

# Using partitioned models

Many datasets can be partitioned into multiple independent subsets. For example, a dataset containing sales data
for a chain of stores can be partitioned by store number. A separate model can then be trained for each partition.
Training and inference operations on the partitions can be parallelized, reducing the wall-clock time for these
operations. Furthermore, since individual stores likely differ significantly in how their features affect their
sales, this approach can lead to more accurate inference at the store level.

The Snowflake Model Registry supports distributed processing of training and inference of partitioned data when:

* The dataset contains a column that reliably identifies partitions in the data.
* The data in each individual partition is uncorrelated with the data in the other partitions and contains enough
  rows to train the model.

Models may be stateless (training is performed each time inference is called) or stateful (training is performed once
before inference and retained for use in multiple inference operations).

With the Snowflake Model Registry, implement partitioned training and inference using
[custom models](bring-your-own-model-types.md). During inference, the model
inference method partitions the dataset, generates predictions for each partition in parallel using all the nodes and
cores in your warehouse, and combines the results into a single dataset afterward.

> **Note:**
>
> For partitioned models, it’s important to distinguish the registered model from the individual models that
> are created by or compose the registered model. Where possible, we will refer to the individual underlying models
> as submodels.

## Defining and logging the model

The partitioned model class inherits from `snowflake.ml.model.custom_model.CustomModel`, and inference methods are
declared with the `@custom_model.partitioned_api` decorator. See
[Bring your own model types via serialized files](bring-your-own-model-types.md) for information on defining standard custom models.

```python
import pandas as pd

from snowflake.ml.model import custom_model

class ExamplePartitionedModel(custom_model.CustomModel):

  @custom_model.partitioned_api
  def predict(self, input: pd.DataFrame) -> pd.DataFrame:
      # All data in the partition will be loaded in the input dataframe.
      #… implement model logic here …
      return output_df

my_model = ExamplePartitionedModel()
```

When logging the model, provide a `function_type` of `TABLE_FUNCTION` in the `options` dictionary along with any
other [options](overview.md) your model requires.

```python
from snowflake.ml.registry import Registry

reg = Registry(session=sp_session, database_name="ML", schema_name="REGISTRY")
model_version = reg.log_model(my_model,
  model_name="my_model",
  version_name="v1",
  options={"function_type": "TABLE_FUNCTION"},    ###
  conda_dependencies=["scikit-learn"],
  sample_input_data=train_features
)
```

If your partitioned model also has regular (non-table) functions as methods, you can use the `method_options`
dictionary to specify the type of each method instead.

```python
model_version = reg.log_model(my_model,
    model_name="my_model",
    version_name="v1",
    options={
      "method_options": {                                 ###
        "METHOD1": {"function_type": "TABLE_FUNCTION"},   ###
        "METHOD2": {"function_type": "FUNCTION"}          ###
      }
    },
    conda_dependencies=["scikit-learn"],
    sample_input_data=train_features,
)
```

## Partitioned model inference

Use the `run` method of a Python `ModelVersion` object to invoke the table function methods in a partitioned
fashion, passing `partition_column` to specify the name of the column that contains a numeric or string value that
identifies the partition of each record. As usual, you may pass a Snowpark or pandas DataFrame (the latter is useful for
local testing). You will receive the same type of DataFrame as the result. In these examples, inference is partitioned
on a store number.

```python
model_version.run(
  input_df,
  function_name="PREDICT",
  partition_column="STORE_NUMBER"
)
```

You can also call the model table functions directly with SQL, as shown here.

```sqlexample
SELECT output1, output2, partition_column
  FROM input_table,
      TABLE(
          my_model!predict(input_table.input1, input_table.input2)
          OVER (PARTITION BY input_table.store_number)
      )
  ORDER BY input_table.store_number;
```

The input data is automatically split among the nodes and cores in your warehouse and the partitions are processed
in parallel.

For more information about table function syntax, see [Calling a UDF with SQL](../../udf/udf-calling-sql.md).

### Using parameters with partitioned models

Partitioned model methods decorated with `@partitioned_api` can accept optional inference parameters, the same way
as `@inference_api` methods. Define parameters as keyword-only arguments (after `*`), with type annotations and
default values:

```python
class PartitionedModelWithParams(custom_model.CustomModel):

  @custom_model.partitioned_api
  def predict(
      self,
      input_df: pd.DataFrame,
      *,
      n_estimators: int = 100,
      learning_rate: float = 0.1,
  ) -> pd.DataFrame:
      import xgboost
      training_data = ...

      my_model = xgboost.XGBRegressor(
          n_estimators=n_estimators,
          learning_rate=learning_rate,
      )
      my_model.fit(training_data)

      output_df = my_model.predict(...)
      return output_df
```

Pass parameters at inference time through `mv.run`:

```python
model_version.run(
    input_df,
    function_name="PREDICT",
    partition_column="STORE_NUMBER",
    params={"n_estimators": 200, "learning_rate": 0.05}
)
```

Or in SQL using positional or named arguments:

```sqlexample
-- Positional: input columns, then parameters
SELECT output1, output2, partition_column
  FROM input_table,
      TABLE(
          my_model!predict(input_table.input1, input_table.input2, 200, 0.05)
          OVER (PARTITION BY input_table.store_number)
      )
  ORDER BY input_table.store_number;

-- Named arguments (all arguments must be named)
SELECT output1, output2, partition_column
  FROM input_table,
      TABLE(
          my_model!predict(
              input1 => input_table.input1,
              input2 => input_table.input2,
              n_estimators => 200
          )
          OVER (PARTITION BY input_table.store_number)
      )
  ORDER BY input_table.store_number;
```

For more information about defining parameters, see
[Specifying model signatures](model-signature.md) and
[Defining inference parameters](bring-your-own-model-types.md).

## Stateless partitioned models

In the simplest application of partitioned models, training and inference are both done when `predict` is
called. The model is fitted, inference is run, and the fitted model is discarded immediately afterward. This type
of model is called “stateless” because no fit state is stored. Here is an example in which each partition trains
an XGBoost model:

```python
class ExampleStatelessPartitionedModel(custom_model.CustomModel):

  @custom_model.partitioned_api
  def predict(self, input_df: pd.DataFrame) -> pd.DataFrame:
      import xgboost
      # All data in the partition will be loaded in the input dataframe.
      # Construct training data by transforming input_df.
      training_data = ...

      # Train the model.
      my_model = xgboost.XGBRegressor()
      my_model.fit(training_data)

      # Generate predictions.
      output_df = my_model.predict(...)

      return output_df

my_model = ExampleStatelessPartitionedModel()
```

See the [Partitioned Model Quickstart Guide](https://quickstarts.snowflake.com/guide/partitioned-ml-model/)
for an example of a stateless partitioned model, including sample data.

## Stateful partitioned models

It’s also possible to implement stateful partitioned models that load stored submodel fit state. You do this by providing
models in memory via the `snowflake.ml.model.custom_model.ModelContext` or by providing file paths pointing to fitted
model artifacts and loading them during inference.

The following example shows how to provide models in memory to the model context.

```python
from snowflake.ml.model import custom_model

# `models` is a dict with model ids as keys, and fitted xgboost models as values.
models = {
  "model1": models[0],
  "model2": models[1],
  ...
}

model_context = custom_model.ModelContext(
  models=models
)
my_stateful_model = MyStatefulCustomModel(model_context=model_context)
```

When logging `my_stateful_model`, the submodels provided in the context are stored along with all model files.
They can then be accessed in the inference method logic by retrieving them from context, as shown below:

```python
class ExampleStatefulModel(custom_model.CustomModel):

  @custom_model.inference_api
  def predict(self, input: pd.DataFrame) -> pd.DataFrame:
    model1 = self.context.model_ref("model1")
    # ... use model1 for inference
```

It’s also possible to access the models programmatically by partition ID in the `predict` method. If a partition column is
provided as an input feature, it can be used to access a model fitted for the partition. For example, if the partition column
is `MY_PARTITION_COLUMN`, the following model class can be defined:

```python
class ExampleStatefulModel(custom_model.CustomModel):

  @custom_model.inference_api
  def predict(self, input: pd.DataFrame) -> pd.DataFrame:
    model_id = input["MY_PARTITION_COLUMN"][0]
    model = self.context.model_ref(model_id)
    # ... use model for inference
```

Similarly, submodels can be stored as artifacts and loaded at runtime. This approach is useful when the models are too
large to fit into memory. Provide string file paths to the model context. The filepaths are accessible during inference
with `self.context.path(artifact_id)`. For more information, see [Defining model context by keyword arguments](bring-your-own-model-types.md).

## Example

See the [Partitioned Model Quickstart Guide](https://quickstarts.snowflake.com/guide/partitioned-ml-model/)
for an example, including sample data.

See the [Many Model Inference in Snowflake Quickstart Guide](https://quickstarts.snowflake.com/guide/many-model-inference-in-snowflake/)
for an example of a stateful partitioned custom model.
