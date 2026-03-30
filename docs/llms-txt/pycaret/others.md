# Source: https://pycaret.gitbook.io/docs/get-started/functions/others.md

# Others

## pull

Returns the last printed scoring grid. Use `pull` function after any training function to store the scoring grid in `pandas.DataFrame`.

#### Example

{% code lineNumbers="true" %}

```python
# loading dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable')

# compare models
best_model = compare_models()

# get the scoring grid
results = pull()
```

{% endcode %}

![Output from pull()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FVGUqL622s64YrYgx3Ow3%2Fimage.png?alt=media\&token=03bb25da-0791-4d96-8f22-4bad02a47f06)

{% code lineNumbers="true" %}

```python
type(results)
# >>> pandas.core.frame.DataFrame
```

{% endcode %}

## models

Return a table containing all the models available in the imported module of the model library.

#### Example

{% code lineNumbers="true" %}

```python
# loading dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable')

# check model library
models()
```

{% endcode %}

![Output from models()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F4YDeJ9mCQMFD7Diev0pA%2Fimage.png?alt=media\&token=bc0c5dc3-007d-42cd-96d7-ee571182bceb)

If you want to see a little more information than this, you can pass `internal=True`.

{% code lineNumbers="true" %}

```python
# loading dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable')

# check model library
models(internal = True)
```

{% endcode %}

![Output from models(internal = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fe9nHXbSrVnWIUTeks9k0%2Fimage.png?alt=media\&token=d0e5058b-7529-4eeb-a7e5-dbf24d073b54)

## get\_config

This function retrieves the global variables created when initializing the [setup](https://pycaret.gitbook.io/docs/get-started/initialize#setup) function.&#x20;

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable')

# get X_train
get_config('X_train')
```

{% endcode %}

![Output from get\_config('X\_train')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUZNYnrndxCKFUykRCmii%2Fimage.png?alt=media\&token=d542803a-d601-4df6-8b25-5ef9d394dd3a)

To check all accessible parameters with `get_config`:

{% code lineNumbers="true" %}

```python
# check all available param
get_config()
```

{% endcode %}

Variables accessible by `get_config` function:

* 'USI'&#x20;
* 'X'&#x20;
* 'X\_test'&#x20;
* 'X\_test\_transformed'&#x20;
* 'X\_train'&#x20;
* 'X\_train\_transformed'&#x20;
* 'X\_transformed'&#x20;
* 'data'&#x20;
* 'dataset'&#x20;
* 'dataset\_transformed'&#x20;
* 'exp\_id'&#x20;
* 'exp\_name\_log'&#x20;
* 'fix\_imbalance'&#x20;
* 'fold\_generator'&#x20;
* 'fold\_groups\_param'&#x20;
* 'fold\_shuffle\_param'&#x20;
* 'gpu\_n\_jobs\_param'&#x20;
* 'gpu\_param'&#x20;
* 'html\_param'&#x20;
* 'idx'&#x20;
* 'is\_multiclass'&#x20;
* 'log\_plots\_param'&#x20;
* 'logging\_param'&#x20;
* 'memory'&#x20;
* 'n\_jobs\_param'&#x20;
* 'pipeline'&#x20;
* 'seed'&#x20;
* 'target\_param'&#x20;
* 'test'&#x20;
* 'test\_transformed'&#x20;
* 'train'&#x20;
* 'train\_transformed'&#x20;
* 'variable\_and\_property\_keys'&#x20;
* 'variables'&#x20;
* 'y'&#x20;
* 'y\_test'&#x20;
* 'y\_test\_transformed'&#x20;
* 'y\_train'&#x20;
* 'y\_train\_transformed'&#x20;
* 'y\_transformed'

## set\_config

This function resets the global variables.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', session_id = 123)

# reset environment seed
set_config('seed', 999) 
```

{% endcode %}

## get\_metrics

Returns the table of all the available metrics in the metric container. All these metrics are used for cross-validation.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', session_id = 123)

# get metrics
get_metrics()
```

{% endcode %}

![Output from get\_metrics()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FEDur3lvUfkO23jCBr6js%2Fimage.png?alt=media\&token=24cce1d2-5bb5-4357-b5d1-70f0ecb98d93)

## add\_metric

Adds a custom metric to the metric container.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', session_id = 123)

# add metric
from sklearn.metrics import log_loss
add_metric('logloss', 'Log Loss', log_loss, greater_is_better = False)
```

{% endcode %}

![Output from add\_metric('logloss', 'Log Loss', log\_loss, greater\_is\_better = False)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FzVy3zRL8VbYiUy063EyY%2Fimage.png?alt=media\&token=bbda0d68-f105-4a1f-b911-1720867ebba7)

Now if you check metric container:

{% code lineNumbers="true" %}

```python
get_metrics()
```

{% endcode %}

![Output from get\_metrics() (after adding log loss metric)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1ycC6K1UjVSFje6udG4y%2Fimage.png?alt=media\&token=b8cecc03-a6c2-479b-b740-9497bc643fa9)

## remove\_metric

Removes a metric from the metric container.

{% code lineNumbers="true" %}

```python
# remove metric
remove_metric('logloss')
```

{% endcode %}

No Output. Let's check the metric container again.

{% code lineNumbers="true" %}

```python
get_metrics()
```

{% endcode %}

![Output from get\_metrics() (after removing log loss metric)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fyo21HLnrHW7xBLgiFwU4%2Fimage.png?alt=media\&token=78fab954-a713-478d-8193-dbec2b47101f)

## automl

This function returns the best model out of all trained models in the current setup based on the `optimize` parameter. Metrics evaluated can be accessed using the `get_metrics` function.

#### Example

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
data = get_data('diabetes') 

# init setup 
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable') 

# compare models
top5 = compare_models(n_select = 5) 

# tune models
tuned_top5 = [tune_model(i) for i in top5]

# ensemble models
bagged_top5 = [ensemble_model(i) for i in tuned_top5]

# blend models
blender = blend_models(estimator_list = top5) 

# stack models
stacker = stack_models(estimator_list = top5) 

# automl 
best = automl(optimize = 'Recall')
print(best)
```

{% endcode %}

![Output from print(best)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUKooTHafYP7PZnmuTQHJ%2Fimage.png?alt=media\&token=bafb10a3-2c1c-43e2-bb0a-3b0e4c6fa1e9)

## get\_logs

Returns a table of experiment logs. Only works when `log_experiment = True` when initializing the [setup](https://pycaret.gitbook.io/docs/get-started/initialize#setup) function.

#### Example

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data, target = 'Class variable', log_experiment = True, experiment_name = 'diabetes1')

# compare models
top5 = compare_models()

# check ML logs
get_logs()
```

{% endcode %}

![Output from get\_logs()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FS6pOzAKuzRWgfw20q4F7%2Fimage.png?alt=media\&token=b03cda01-7dea-4327-9feb-1f1f529685f7)

## get\_current\_experiment

Obtain the current experiment object and return a class. This is useful when you are using a functional API and want to move to an OOP API.

{% code lineNumbers="true" %}

```python
# loading dataset
from pycaret.datasets import get_data
data = get_data('insurance')

# init setup using functional API
from pycaret.regression import *
s = setup(data, target = 'charges', session_id = 123)

# compare models
best = compare_models()

# return OOP class for current functional experiment
reg1 = get_current_experiment()
```

{% endcode %}

## set\_current\_experiment

Set the current experiment created using the OOP API to be used with the functional API.

{% code lineNumbers="true" %}

```python
# loading dataset
from pycaret.datasets import get_data
data = get_data('insurance')

# init setup using OOP API
from pycaret.regression import RegressionExperiment
reg1 = RegressionExperiment()
reg1.setup(data, target = 'charges', session_id = 123)

# compare models
best = compare_models()

# set OOP experiment as functional
set_current_experiment(reg1)
```

{% endcode %}
