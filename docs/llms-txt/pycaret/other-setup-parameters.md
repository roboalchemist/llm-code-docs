# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing/other-setup-parameters.md

# Other setup parameters

### Required Parameters

There are only two required parameters in the setup function.

#### PARAMETERS

* **data: dataframe-like = None**

  Data set with shape (n\_samples, n\_features), where n\_samples is the number of samples and n\_features is the number of features. If data is not a pandas dataframe, it's converted to one using default column names.
* **data\_func: Callable\[\[], DATAFRAME\_LIKE] = None**

  The function that generate `data` (the dataframe-like input). This is useful when the dataset is large, and you need parallel operations such as `compare_models`. It can avoid broadcasting large dataset from driver to workers. Notice one and only one of `data` and `data_func` must be set.
* **target: float, int, str or sequence, default = -1**

  If int or str, respectively index or name of the target column in data. The default value selects the last column in the dataset. If sequence, it should have shape (n\_samples,).&#x20;
* **index: bool, int, str or sequence, default = False**

  Handle indices in the `data` dataframe.

  * If False: Reset to RangeIndex.
  * If True: Keep the provided index.
  * If int: Position of the column to use as index.
  * If str: Name of the column to use as index.
  * If sequence: Array with shape=(n\_samples,) to use as index.

### Experiment Logging

PyCaret can automatically log entire experiments, including setup parameters, model hyperparameters, performance metrics, and pipeline artifacts. The default settings use [`MLflow`](https://mlflow.org/) as the logging backend. [`wandb`](https://wandb.ai/), [`cometml`](https://www.comet.com/site/), [`dagshub`](https://www.dagshub.com) is also available for backend. A parameter in the setup can be enabled to automatically track all the metrics, hyperparameters, and model artifacts.

#### PARAMETERS

* **log\_experiment: bool or str or BaseLogger or list of str or BaseLogger, default = False**    A (list of) PyCaret `BaseLogger` or str (one of `mlflow`, `wandb`, `comet_ml`, or `dagshub`) corresponding to a logger to determine which experiment loggers to use. Setting to `True` will use just `MLFlow`.
* **experiment\_name: str, default = None**

  Name of the experiment for logging. Ignored when `log_experiment = False`.
* **experiment\_custom\_tags: dict, default = None**\
  Dictionary of tag\_name: String -> value: (String, but will be string-ified if not) passed to the mlflow\.set\_tags to add new custom tags for the experiment.
* **log\_plots: bool or list, default = False**

  When set to True, certain plots are logged automatically in the MLFlow server. To change the type of plots to be logged, pass a list containing plot IDs. Refer to documentation of `plot_model`. Ignored when `log_experiment = False`.&#x20;
* **log\_profile: bool, default = False**

  When set to True, data profile is logged on the MLflow server as a html file.

  Ignored when `log_experiment = False`
* **log\_data: bool, default = False**\
  When set to `True`, train and test dataset are logged as a CSV file.

#### Example

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', log_experiment = True, experiment_name = 'diabetes1')

# model training
best_model = compare_models() 
```

{% endcode %}

To initialize `MLflow` server you must run the following command from within the notebook or from the command line. Once the server is initialized, you can track your experiment on `https://localhost:5000`.

```
# init server
!mlflow ui
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FciBSVnPdDpQ9zPUuC3p4%2Fimage.png?alt=media\&token=43ce3c57-76c6-4395-b3a5-c4010e4bcdde)

#### Configure MLflow tracking server

When no backend is configured Data is stored locally at the provided file (or ./mlruns if empty). To configure the backend use `mlflow.set_tracking_uri` before executing the setup function.

* An empty string, or a local file path, prefixed with file:/. Data is stored locally at the provided file (or ./mlruns if empty).
* An HTTP URI like <https://my-tracking-server:5000>.
* A Databricks workspace, provided as the string “databricks” or, to use a Databricks CLI profile, “databricks\://\<profileName>”.

{% code overflow="wrap" lineNumbers="true" %}

```python
# set tracking uri 
import mlflow 
mlflow.set_tracking_uri('file:/c:/users/mlflow-server')

# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', log_experiment = True, experiment_name = 'diabetes1')
```

{% endcode %}

#### PyCaret on Databricks

When using PyCaret on Databricks `experiment_name` parameter in the setup must include complete path to storage.  See example below on how to log experiments when using Databricks:

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', log_experiment = True, experiment_name = '/Users/username@domain.com/experiment-name-here')
```

{% endcode %}

### Model Selection

Following parameters in the setup can be used for setting parameters for model selection process. These are not related to data preprocessing but can influence your model selection process.

#### PARAMETERS

* **train\_size: float, default = 0.7**\
  The proportion of the dataset to be used for training and validation.&#x20;
* **test\_data: dataframe-like or None, default = None**

  If not None, `test_data` is used as a hold-out set and `train_size` parameter is ignored. The columns in the `data` and `test_data` must match.
* **data\_split\_shuffle: bool, default = True**\
  When set to `False`, prevents shuffling of rows during `train_test_split`.
* **data\_split\_stratify: bool or list, default = True**\
  Controls stratification during the `train_test_split`. When set to `True`, it will stratify by target column. To stratify on any other columns, pass a list of column names. Ignored when `data_split_shuffle` is `False`.
* **fold\_strategy: str or scikit-learn** **CV generator object, default = ‘stratifiedkfold’**\
  Choice of cross-validation strategy. Possible values are:
  * ‘kfold’
  * ‘stratifiedkfold’
  * ‘groupkfold’
  * ‘timeseries’
  * a custom CV generator object compatible with scikit-learn.
  * For `groupkfold`, column name must be passed in `fold_groups` parameter. Example: `setup(fold_strategy="groupkfold", fold_groups="COLUMN_NAME")`
* **fold: int, default = 10**\
  The number of folds to be used in cross-validation. Must be at least 2. This is a global setting that can be over-written at the function level by using the `fold` parameter. Ignored when `fold_strategy` is a custom object.
* **fold\_shuffle: bool, default = False**\
  Controls the shuffle parameter of CV. Only applicable when `fold_strategy` is `kfold` or `stratifiedkfold`. Ignored when `fold_strategy` is a custom object.
* **fold\_groups: str or array-like, with shape (n\_samples,), default = None**

  Optional group labels when ‘GroupKFold’ is used for the cross-validation. It takes an array with shape (n\_samples, ) where n\_samples is the number of rows in the training dataset. When the string is passed, it is interpreted as the column name in the dataset containing group labels.

### Other Parameters

Following parameters in the setup can be used for controlling other experiment settings such as using GPU for training or setting verbosity of the experiment. They do not affect the data in any way.

#### PARAMETERS

* **n\_jobs: int, default = -1**\
  The number of jobs to run in parallel (for functions that support parallel processing) -1 means using all processors. To run all functions on single processor set `n_jobs = None`
* **use\_gpu: bool or str, default = False**\
  When set to `True`, it will use GPU for training with algorithms that support it and fall back to CPU if they are unavailable. When set to `force` it will only use GPU-enabled algorithms and raise exceptions when they are unavailable. When `False` all algorithms are trained using CPU only. GPU enabled algorithms:
  * Extreme Gradient Boosting, requires no further installation
  * CatBoost Classifier, requires no further installation (GPU training is only enabled when data > 50,000 rows)
  * Light Gradient Boosting Machine, requires GPU installation [Tutorial](https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html)&#x20;
  * Logistic Regression, Ridge Classifier, Random Forest, K Neighbors Classifier, Support Vector Machine, requires cuML >= 0.15 [cuML](https://github.com/rapidsai/cuml)
* **session\_id: int, default = None**\
  Controls the randomness of the experiment. It is equivalent to `random_state` in scikit-learn. When `None`, a pseudo-random number is generated. This can be used for later reproducibility of the entire experiment.
* **verbose: bool, default = True**\
  When set to `False`, Information grid is not printed.
* **profile: bool, default = False**\
  When set to `True`, an interactive EDA report is displayed.
* **profile\_kwargs: dict, default = {} (empty dict)**\
  Dictionary of arguments passed to the `ProfileReport` method used to create the EDA report. Ignored if `profile` is False.
* **custom\_pipeline: list of (str, transformer), dict or Pipeline, default = None**

  Additional custom transformers. If passed, they are applied to the pipeline last, after all the build-in transformers.
* **custom\_pipeline\_position: int, default = -1**    \
  Position of the custom pipeline in the overall preprocessing pipeline. The default value adds the custom pipeline last.
* **preprocess: bool, default = True**\
  When set to `False`, no transformations are applied except for `train_test_split` and custom transformations passed in `custom_pipeline` parameter. Data must be ready for modeling (no missing values, no dates, categorical data encoding) when preprocess is set to `False`.
* **system\_log: bool or str or logging.Logger, default = True**

  Whether to save the system logging file (as logs.log). If the input is a string, use that as the path to the logging file. If the input already is a logger object, use that one instead.
* **memory: str, bool or Memory, default=True**

  Used to cache the fitted transformers of the pipeline.&#x20;

  * If False: No caching is performed.
  * If True: A default temp directory is used.
  * If str: Path to the caching directory.
