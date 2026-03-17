# Source: https://pycaret.gitbook.io/docs/get-started/functions/initialize.md

# Initialize

## setup

This function initializes the experiment in PyCaret and creates the transformation pipeline based on all the parameters passed in the function. The `setup` function must be called before executing any other function. It takes two required parameters: `data` and `target`. All the other parameters are optional.&#x20;

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F6fTDPXS1O6cC0i1x4AHi%2Fimage.png?alt=media&#x26;token=89776f47-d2f5-4c0f-a3d2-1b40a36a6e0c" alt=""><figcaption></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import ClassificationExperiment
clf1 = ClassificationExperiment()
clf1.setup(data = diabetes, target = 'Class variable', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F3vcmMgBfj8QifkB3Yxwa%2Fimage.png?alt=media&#x26;token=74a50111-e101-41e5-8213-81b00f1b824a" alt=""><figcaption></figcaption></figure>

### Required Parameters

There are only two required parameters in the `setup`:

* **target: float, int, str or sequence, default = -1**

  If int or str, respectively index or name of the target column in data. The default value selects the last column in the dataset. If sequence, it should have shape (n\_samples,).&#x20;
* **data\_func: Callable\[\[], DATAFRAME\_LIKE] = None**

  The function that generate `data` (the dataframe-like input). This is useful when the dataset is large, and you need parallel operations such as `compare_models`. It can avoid broadcasting large dataset from driver to workers. Notice one and only one of `data` and `data_func` must be set.
* **data: dataframe-like = None**

  Data set with shape (n\_samples, n\_features), where n\_samples is the number of samples and n\_features is the number of features. If data is not a pandas dataframe, it's converted to one using default column names.

{% hint style="info" %}
**NOTE:** target parameter is not required in `pycaret.clustering` and `pycaret.anomaly` module.
{% endhint %}

### Experiment Logging

You can automatically track entire experiments in PyCaret. A parameter in the setup can be enabled to automatically track all the metrics, hyperparameters, and model artifacts. By default, PyCaret uses `MLFlow` for experiment logging. Other available options are `wandb` `cometml` `dagshub`.&#x20;

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

Initialize the `MLflow` server on localhost:

{% code lineNumbers="true" %}

```python
# init server
!mlflow ui
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F6uTMlfKwzA24quhVm3aj%2Fimage.png?alt=media\&token=03dbf17b-be0f-4785-baf8-5ce84dfdd2e7)

To learn more about experiment tracking in PyCaret, [see this page](https://pycaret.gitbook.io/docs/preprocessing/other-setup-parameters#experiment-logging).

### Model Validation

There are quite a few parameters in the setup function that are not directly related to preprocessing or data transformation but are used as part of model validation and selection strategy such as `train_size`, `fold_strategy`, or number of `fold` for cross-validation. To learn more about all the model validation and selection settings in the setup, see [this page](https://pycaret.gitbook.io/docs/preprocessing/other-setup-parameters#model-selection).

### GPU Support&#x20;

With PyCaret, you can train models on GPU and speed up your workflow by 10x. To train models on GPU simply pass `use_gpu = True` in the setup function. There is no change in the use of the API, however, in some cases, additional libraries have to be installed as they are not installed with the default version or the full version. To learn more about GPU support, see [this page](https://pycaret.gitbook.io/docs/installation#gpu).

### Examples

To see the use of the `setup` in other modules of PyCaret, see below:

* [Classification](https://pycaret.gitbook.io/docs/quickstart#classification)
* [Regression](https://pycaret.gitbook.io/docs/quickstart#regression)
* [Clustering](https://pycaret.gitbook.io/docs/quickstart#clustering)
* [Anomaly Detection](https://pycaret.gitbook.io/docs/quickstart#anomaly-detection)
* [Time Series Forecasting](https://pycaret.gitbook.io/docs/quickstart#time-series)

{% hint style="info" %}
All the examples in the following sections are shown using Functional API only.
{% endhint %}
