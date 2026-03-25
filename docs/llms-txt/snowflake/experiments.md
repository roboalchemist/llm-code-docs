# Source: https://docs.snowflake.com/en/developer-guide/snowflake-ml/experiments.md

# Run an experiment to compare and select models

With Snowflake ML Experiments, you can set up *experiments*, organized evaluations of the results of model training. This allows you to quickly compare the results of hyperparameter adjustment, different target metrics, and behavior of different model types in an organized fashion in order to select the best model for your needs. Each experiment consists of a series of *runs*, which are metadata and artifacts from your training. Snowflake is unopinionated about your run artifacts – you can submit anything that’s useful for your model evaluation process.

After you complete an experiment, the results are visible through Snowsight. You can also retrieve run artifacts at any time in Python or SQL.

> **Note:**
>
> Snowflake Experiments require `snowflake-ml-python` version 1.19.0 or later.

## Access control requirements

Creating an experiment requires the CREATE EXPERIMENT privilege on the schema where run artifacts are stored. Creating an experiment requires the USAGE privilege on the parent database and schema.

## Create an experiment

First, create an experiment. This requires an existing database and schema, used to store run information.

PythonSnowsight

Experiment support is available in the `snowflake.ml.experiment.ExperimentTracking` class. Use the `set_experiment(name: Optional[str])` method to both open an experiment with the given name and set it to the active experiment context for logs and artifacts. Experiments which don’t exist yet are created.

The following example shows how to create or open an experiment named `My_Experiment` in the active database and schema and set it as the active experiment, using an existing `session`:

```python
from snowflake.ml.experiment import ExperimentTracking

exp = ExperimentTracking(session=session)
exp.set_experiment("My_Experiment")
```

> **Important:**
>
> The `ExperimentTracking` class is a singleton, and only one run can be active at any time. Experiments and runs are not thread-safe and should only be modified from the thread where `ExperimentTracking` instance was configured.

1. In the navigation menu, select AI & ML » Experiments.
2. Select New Experiment.
3. Enter the Name of your experiment.
4. Select the database and schema to store your experiment’s run artifacts in.
5. Select Create to create the experiment, or Cancel to cancel.

## Start an experiment run

Each run in an experiment has its own set of metrics, parameters, and artifacts. This information is used in Snowsight to provide visualizations and data about your model training and its results.

Start a run with the `start_run(name: Optional[str])` method on your `ExperimentTracking` instance. This returns a new `Run`, which supports use in a `with` statement. Snowflake recommends that you use `with` statements, so that runs are cleanly completed and it’s easier to reason about run scope.

```python
with exp.start_run("my_run"):
  # .. Train your model and log artifacts
```

### Automatically log training information

You can autolog training information for XGBoost, LightGBM, or Keras models during model training. Autologging is performed by registering a callback which refers to your experiment and information about the model you’re training. Each time a method is called on your `Model` instance which adjusts a parameter or metric, it’s automatically logged to your experiment for the active run.

The following example shows how to configure your experiment’s callbacks for each supported model trainer and then start a basic training run to log artifacts.

XGBoostLightGBMKeras

```python
# exp: ExperimentTracking

from xgboost import XGBClassifier

from snowflake.ml.experiment.callback.xgboost import SnowflakeXgboostCallback
from snowflake.ml.model.model_signature import infer_signature

sig = infer_signature(X, y)
callback = SnowflakeXgboostCallback(
    exp, model_name="name", model_signature=sig
)
model = XGBClassifier(callbacks=[callback])
with exp.start_run("my_run"):
    model.fit(X, y, eval_set=[(X, y)])
```

```python
# exp: ExperimentTracking

from lightgbm import LGBMClassifier

from snowflake.ml.experiment.callback.lightgbm import SnowflakeLightgbmCallback
from snowflake.ml.model.model_signature import infer_signature

sig = infer_signature(X, y)
callback = SnowflakeLightgbmCallback(
    exp, model_name="name", model_signature=sig
)
model = LGBMClassifier()
with exp.start_run("my_run"):
    model.fit(X, y, eval_set=[(X, y)], callbacks=[callback])
```

```python
# exp: ExperimentTracking

import keras

from snowflake.ml.experiment.callback.keras import SnowflakeKerasCallback
from snowflake.ml.model.model_signature import infer_signature

sig = infer_signature(X, y)
callback = SnowflakeKerasCallback(
    exp, model_name="name", model_signature=sig
)
model = keras.Sequential()
model.add(keras.layers.Dense(1))
model.compile(
    optimizer=keras.optimizers.RMSprop(learning_rate=0.1),
    loss="mean_squared_error",
    metrics=["mean_absolute_error"],
)
with exp.start_run("my_run"):
    model.fit(X, y, validation_split=0.5, callbacks=[callback])
```

### Manually log training information and artifacts

For models which don’t support automatic logging or are pre-trained, you can manually log experiment information and upload artifacts in Python. Parameters are constant inputs to the training model, while metrics are evaluated at a model *step*. You can choose to represent a training epoch as a corresponding step. The following example shows how to log parameters, log metrics, and upload artifacts.

> **Note:**
>
> The default step value is `0`.

```python
# Logging requires an active run for the exp: ExperimentTracker instance.

# Log model parameters with the log_param(...) or log_params(...) methods
exp.log_param("learning_rate", 0.01)
exp.log_params({"optimizer": "adam", "batch_size": 64})

# Log model metrics with the log_metric(...) or log_metrics(...) methods
exp.log_metric("loss", 0.3, step=100)
exp.log_metrics({"loss": 0.4, "accuracy": 0.8}, step=200)

# Log your model to the experiment's model registry with the log_model(...) method.
exp.log_model(model, model_name="my_model", signatures={"predict": model_signature})
exp.log_model(model, model_name="my_model", sample_input_data=data)

# Log local artifacts to an experiment run with the log_artifact(...) method.
exp.log_artifact('/tmp/file.txt', artifact_path='artifacts')
```

> **Note:**
>
> Artifact logging isn’t supported on Warehouse Notebooks.

## Complete a run

Completing a run makes it immutable and presents it as finished in Snowsight.

If you started a run as part of a `with` statement, the run is automatically completed when exiting scope. Otherwise, you can end a run by calling your experiment’s `end_run(name: Optional[str])` method with the name of the run to complete:

```python
experiment.end_run("my_run")
```

## Compare runs within an experiment

Experiment evaluation is done through Snowsight. In the navigation menu, select AI & ML » Experiments and select your experiment to examine from the list.

The runs list displays Run name, Status, Created date, and a column for each metric. You can also toggle parameters as additional columns. View more details, such as artifacts, metric charts, and linked model versions from the run view and run comparison views.

> **Note:**
>
> Viewing linked model versions is part of the [Model Lineage feature](ml-lineage.md), which is only available for customers on Enterprise Edition and above.

You can select up to five runs in your experiment. To compare runs, select the Compare button. You’re presented with the comparison view, which displays run metadata, parameters, metrics, and model version information.

## Retrieve artifacts from a run

At any time during or after a run, you can retrieve artifacts. The following example shows how to list a run’s available artifacts in the `logs` path, and download the `logs/log0.txt` artifact for the run `my_run` in the experiment `my_experiment` to the local directory `/tmp`:

PythonSQL

```python
# exp: ExperimentTracking
exp.set_experiment("my_experiment")

exp.list_artifacts("my_run", artifact_path="logs")
exp.download_artifacts("my_run", artifact_path="logs/log0.txt", target_path="/tmp")
```

```sqlexample
LIST snow://experiment/my_experiment/versions/my_run/logs;
GET snow://experiment/my_experiment/versions/my_run/logs/log0.txt file:///tmp;
```

## Delete runs and experiments

After finishing an experiment, you can remove it and all of its associated run artifacts. The following example removes the experiment `my_experiment`:

PythonSQL

```python
# exp: ExperimentTracking
exp.delete_experiment("my_experiment")
```

```sqlexample
DROP EXPERIMENT my_experiment;
```

You can also remove an individual run from an experiment. The following example removes the run `my_run` from the experiment `my_experiment`:

PythonSQL

```python
# exp: ExperimentTracking
exp.set_experiment("my_experiment")
exp.delete_run("my_run")
```

```sqlexample
ALTER EXPERIMENT my_experiment DROP RUN my_run;
```

## Limitations

Snowflake Experiments are subject to the following limitations:

* Each schema is limited to 500 experiments.
* Each experiment is limited to 500 runs.
* Runs are stored for a maximum of one year.
* Runs are limited to 1000 unique parameters and 200 unique metrics.

## Cost considerations

There is no additional cost to use Snowflake Experiments. It incurs standard Snowflake consumption-based costs. These include the following:

* Cost of storing run artifacts. For general information about storage costs, see [Exploring storage cost](../../user-guide/cost-exploring-data-storage.md).
* Cost of logging data. For general information about costs incurred during logging of data, see [Viewing credit usage](../../user-guide/cost-exploring-compute.md).
* Cost of visualizing data. The charts in the UI are powered by virtual warehouses. For more information, see [Viewing credit usage](../../user-guide/cost-exploring-compute.md).
