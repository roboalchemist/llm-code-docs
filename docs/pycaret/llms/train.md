# Source: https://pycaret.gitbook.io/docs/get-started/functions/train.md

# Train

## compare\_models

This function trains and evaluates the performance of all estimators available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models()
```

{% endcode %}

![Output from compare\_models](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FO6JEaFQHynEGwM8IlUF7%2Fimage.png?alt=media\&token=20061f32-3107-4d37-8687-80621aa65f02)

The `compare_models` returns only the top-performing model based on the criteria defined in `sort` parameter. It is `Accuracy` for classification experiments and `R2` for regression. You can change the `sort` order by passing the name of the metric based on which you want to do model selection.&#x20;

### Change the sort order

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(sort = 'F1')
```

{% endcode %}

![Output from compare\_models(sort = 'F1')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FafWO5nju0CMhbaczf2CE%2Fimage.png?alt=media\&token=51932bd3-3d82-4f2d-b3ae-05eadc4cf5a7)

Notice that the sort order of scoring grid is changed now and also the best model returned by this function is selected based on `F1`.

{% code lineNumbers="true" %}

```python
print(best)
```

{% endcode %}

![Output from print(best)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5ngBmnqKTeuJVowssdTk%2Fimage.png?alt=media\&token=1f1492d1-e187-476a-9135-cf02f11f52d2)

### Compare only a few models

If you don't want to do horse racing on the entire model library, you can only compare a few models of your choice by using the `include` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(include = ['lr', 'dt', 'lightgbm'])
```

{% endcode %}

![Output from compare\_models(include = \['lr', 'dt', 'lightgbm'\])](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvzNTP7iOwq6xDTTWOMnK%2Fimage.png?alt=media\&token=2c7271d8-7540-40b2-9bd3-5f030c227b3d)

Alternatively, you can also use exclude parameter. This will compare all models except for the ones that are passed in the `exclude` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(exclude = ['lr', 'dt', 'lightgbm'])
```

{% endcode %}

![Output from compare\_models(exclude = \['lr', 'dt', 'lightgbm'\])](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FTYNCvAoQUBoQOw7hLj4q%2Fimage.png?alt=media\&token=3884c9cb-7c9a-47f1-96a4-c6e8d051db2c)

### Return more than one model

By default, `compare_models` only return the top-performing model but if you want you can get the Top N models instead of just one model.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(n_select = 3)
```

{% endcode %}

![Output from compare\_models(n\_select = 3)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F8hkXIsRavvljQG8L0ibj%2Fimage.png?alt=media\&token=759b0e3e-faeb-40bb-b004-cf0db8eeb278)

Notice that there is no change in the results, however, if you check the variable `best` , it will now contain a list of the top 3 models instead of just one model as seen previously.&#x20;

{% code lineNumbers="true" %}

```python
type(best)
# >>> list

print(best)
```

{% endcode %}

![Output from print(best)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvEbZ6aujo0TYEYhUk6Un%2Fimage.png?alt=media\&token=01bf6c44-e044-436c-8deb-01c78917f23f)

### Set the budget time

If you are running short on time and would like to set a fixed budget time for this function to run, you can do that by setting the `budget_time` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(budget_time = 0.5)
```

{% endcode %}

![Output from compare\_models(budget\_time = 0.5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FNZ5sDae2Yfdm3Wj676en%2Fimage.png?alt=media\&token=970e45e8-f0df-4770-bcd3-7b850a4ee21b)

### Set the probability threshold

When performing binary classification, you can change the probability threshold or cut-off value for hard labels. By default, all classifiers use `0.5` as a default threshold.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(probability_threshold = 0.25)
```

{% endcode %}

![Output from compare\_models(probability\_threshold = 0.25)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FqXhwTs6Ym1kcVLzlrwjr%2Fimage.png?alt=media\&token=a5e75c99-52d8-409e-923c-d220cc03057e)

Notice that all metrics except for `AUC` are now different. AUC doesn't change because it's not dependent on the hard labels, everything else is dependent on the hard label which is now obtained using `probability_threshold=0.25` .

{% hint style="info" %}
**NOTE:** This parameter is only available in the [Classification](https://pycaret.gitbook.io/docs/get-started/modules) module of PyCaret.
{% endhint %}

### Disable cross-validation

If you don't want to evaluate models using cross-validation and rather just train them and see the metrics on the test/hold-out set you can set the `cross_validation=False.`

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
best = compare_models(cross_validation=False)
```

{% endcode %}

![Output from compare\_models(cross\_validation=False)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FT7D0nITCxFaUbhzTfQVA%2Fimage.png?alt=media\&token=2dc52e3b-2a31-424a-97ae-10f15c391509)

The output looks pretty similar but if you focus, the metrics are now different and that's because instead of average cross-validated scores, these are now the metrics on the test/hold-out set.

{% hint style="info" %}
**NOTE:** This function is only available in [Classification](https://pycaret.gitbook.io/docs/get-started/modules) and [Regression](https://pycaret.gitbook.io/docs/get-started/modules) modules.
{% endhint %}

### Distributed training on a cluster

To scale on large datasets you can run `compare_models` function on a cluster in distributed mode using a parameter called `parallel`. It leverages the [Fugue](https://github.com/fugue-project/fugue/) abstraction layer to run `compare_models` on Spark or Dask clusters.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable', n_jobs = 1)

# create pyspark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# import parallel back-end
from pycaret.parallel import FugueBackend

# compare models
best = compare_models(parallel = FugueBackend(spark))
```

{% endcode %}

![Output from compare\_models(parallel = FugueBackend(spark))](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FEU5Ukw1mT5vKGgF0t2ff%2Fimage.png?alt=media\&token=f4906395-89eb-4f4e-bc4f-76940efd238e)

{% hint style="info" %}
Note that we need to set `n_jobs = 1` in the setup for testing with local Spark because some models will already try to use all available cores, and running such models in parallel can cause deadlocks from resource contention.&#x20;
{% endhint %}

For Dask, we can specify the `"dask"` inside `FugueBackend` and it will pull the available Dask client.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable', n_jobs = 1)

# import parallel back-end
from pycaret.parallel import FugueBackend

# compare models
best = compare_models(parallel = FugueBackend("dask"))
```

{% endcode %}

For the complete example and other features related to distributed execution, check [this example](https://github.com/pycaret/pycaret/blob/master/examples/PyCaret%202%20Fugue%20Integration.ipynb). This example also shows how to get the leaderboard in real-time. In a distributed setting, this involves setting up an RPCClient, but Fugue simplifies that.

## create\_model

This function trains and evaluates the performance of a given estimator using cross-validation. The output of this function is a scoring grid with CV scores by fold. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function. All the available models can be accessed using the `models` function.

### **Example**&#x20;

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train logistic regression
lr = create_model('lr')
```

{% endcode %}

![Output from create\_model('lr')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FmNkwwx9CNwwNoyiBKuKh%2Fimage.png?alt=media\&token=eb2db04d-3bb0-4b1e-a331-7c5f8469415a)

This function displays the performance metrics by fold and the average and standard deviation for each metric and returns the trained model. By default, it uses the `10` fold that can either be changed globally in the [setup](https://pycaret.gitbook.io/docs/get-started/initialize#setup) function or locally within `create_model`.

### Changing the fold param

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train logistic regression
lr = create_model('lr', fold = 5)
```

{% endcode %}

![Output from create\_model('lr', fold = 5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FZBxQ7Elrq0313aUBE4RT%2Fimage.png?alt=media\&token=3109946f-8287-48b7-9093-db2b0345bbe8)

The model returned by this is the same as above, however, the performance evaluation is done using 5 fold cross-validation.&#x20;

### Model library

To check the list of available models in any module, you can use `models` function.

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# check available models
models()
```

{% endcode %}

![Output from models()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FcRHj3GsfdC7793igsUvJ%2Fimage.png?alt=media\&token=69b5c9b5-3b39-4c14-a983-811bbfc369a3)

### Models with custom param

When you just run `create_model('dt')`, it will train Decision Tree with all default hyperparameter settings. If you would like to change that, simply pass the attributes in the `create_model` function.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train decision tree
dt = create_model('dt', max_depth = 5)
```

{% endcode %}

![Output from create\_model('dt', max\_depth = 5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FfkOOD4R5kSEd2vebwdOq%2Fimage.png?alt=media\&token=a5584777-dd6b-4ab4-8cf4-3254e35ab321)

```
# see models params
print(dt)
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FoftkuGPoxG5yy4cE9HCI%2Fimage.png?alt=media\&token=3c489e49-3546-4729-8505-1f5a7b6ff4e7)

### Access the scoring grid

The performance metrics/scoring grid you see after the `create_model` is only displayed and is not returned. As such, if you want to access that grid as `pandas.DataFrame` you will have to use `pull` command after `create_model`.

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train decision tree
dt = create_model('dt', max_depth = 5)

# access the scoring grid
dt_results = pull()
print(dt_results)
```

{% endcode %}

![Output from print(dt\_results)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FWFF9VTiMDcLoSwpjQtuZ%2Fimage.png?alt=media\&token=b4478c25-de52-4562-88e0-19a948207a1f)

{% code lineNumbers="true" %}

```python
# check type
type(dt_results)
# >>> pandas.core.frame.DataFrame

# select only Mean
dt_results.loc[['Mean']]
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1Q3yZq02cB5XwyoJBL8X%2Fimage.png?alt=media&#x26;token=2371107f-a2e5-4fd6-9cb8-712584965b45" alt=""><figcaption><p>Output from dt_results.loc[['Mean']</p></figcaption></figure>

### Disable cross-validation

If you don't want to evaluate models using cross-validation and rather just train them and see the metrics on the test/hold-out set you can set the `cross_validation=False.`

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train model without cv
lr = create_model('lr', cross_validation = False)
```

{% endcode %}

![Output from create\_model('lr', cross\_validation = False)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FbX2zeiBrfiJmPDhyIZcr%2Fimage.png?alt=media\&token=1a8c86f8-fc37-481d-8e49-6c959d633166)

These are the metrics on the test/hold-out set. That's why you only see one row as opposed to the 12 rows in the original output. When you disable `cross_validation`, the model is only trained one time, on the entire training dataset and scored using the test/hold-out set.

{% hint style="info" %}
**NOTE:** This function is only available in [Classification](https://pycaret.gitbook.io/docs/get-started/modules) and [Regression](https://pycaret.gitbook.io/docs/get-started/modules) modules.
{% endhint %}

### Return train score

The default scoring grid shows the performance metrics on the validation set by fold. If you want to see the performance metrics on the training set by fold as well to examine the over-fitting/under-fitting you can use `return_train_score` parameter.

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train model without cv
lr = create_model('lr', return_train_score = True)
```

{% endcode %}

![Output from createmodel('lr', return\_train\_score = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FOjtgtMNpuCY6bCkLXKr6%2Fimage.png?alt=media\&token=1f017a65-a3aa-49f8-bb3f-4540f398d944)

### Set the probability threshold

When performing binary classification, you can change the probability threshold or cut-off value for hard labels. By default, all classifiers use `0.5` as a default threshold.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train model with 0.25 threshold
lr = create_model('lr', probability_threshold = 0.25)
```

{% endcode %}

![Output from create\_model('lr', probability\_threshold = 0.25)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FcjYl91SP7JM4WX9HzZ4h%2Fimage.png?alt=media\&token=287c29fa-6ab5-4797-bf13-db85f1b08377)

{% code lineNumbers="true" %}

```python
# see the model
print(lr)
```

{% endcode %}

![Output from print(lr)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FXGE0MDdB7FHX2Q6A8UTL%2Fimage.png?alt=media\&token=eff38687-4b26-461c-9e1b-72f3ecec3c0a)

### Train models in a loop

You can use the `create_model` function in a loop to train multiple models or even the same model with different configurations and compare their results.

{% code lineNumbers="true" %}

```python
import numpy as npimport pandas as pd

# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# train models in a loop
lgbs  = [create_model('lightgbm', learning_rate = i) for i in np.arange(0.1,1,0.1)]
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fu7ijVTUFw0sL7Qj4hw2o%2Fimage.png?alt=media\&token=77bea015-da11-407a-999f-17bf72d0cfa0)

{% code lineNumbers="true" %}

```python
type(lgbs)
# >>> list

len(lgbs)
# >>> 9
```

{% endcode %}

If you want to keep track of metrics as well, as in most cases, this is how you can do it.

{% code lineNumbers="true" %}

```python
import numpy as np
import pandas as pd

# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# start a loop
models = []
results = []

for i in np.arange(0.1,1,0.1):
    model = create_model('lightgbm', learning_rate = i)
    model_results = pull().loc[['Mean']]
    models.append(model)
    results.append(model_results)
    
results = pd.concat(results, axis=0)
results.index = np.arange(0.1,1,0.1)
results.plot()
```

{% endcode %}

![Output from results.plot()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvGHX4tR3ipKNtCLNPYkh%2Fimage.png?alt=media\&token=a548a5e6-38e4-47ca-ab71-0febb610f79a)

### Train custom models

You can use your own custom models for training or models from other libraries which are not part of pycaret. As long as their API is consistent with `sklearn`, it will work like a breeze.

{% code lineNumbers="true" %}

```python
# install gplearn library
# pip install gplearn

# load dataset 
from pycaret.datasets import get_data 
diabetes = get_data('diabetes') 

# init setup
from pycaret.classification import * 
clf1 = setup(data = diabetes, target = 'Class variable')

# import custom model
from gplearn.genetic import SymbolicClassifier
sc = SymbolicClassifier()

# train custom model
sc_trained = create_model(sc)
```

{% endcode %}

![Output from create\_model(sc)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FMrBCZHlcBJKuFxgIu0tu%2Fimage.png?alt=media\&token=dce58b14-3d70-41e9-87a0-42d4043584d6)

{% code lineNumbers="true" %}

```python
type(sc_trained)
# >>> gplearn.genetic.SymbolicClassifier

print(sc_trained)
```

{% endcode %}

![Output from print(sc\_trained)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fh7YT9CAcCwvbZanBiEih%2Fimage.png?alt=media\&token=bd2a614b-eb04-4282-8f65-9e0b9bcfd46d)

### Write your own models

You can also write your own class with `fit` and `predict` function. PyCaret will be compatible with that. Here is a simple example:

{% code lineNumbers="true" %}

```python
# load dataset 
from pycaret.datasets import get_data 
insurance= get_data('insurance') 

# init setup
from pycaret.regression import * 
reg1 = setup(data = insurance, target = 'charges')

# create custom estimator
import numpy as np
from sklearn.base import BaseEstimator
class MyOwnModel(BaseEstimator):
    
    def __init__(self):
        self.mean = 0
        
    def fit(self, X, y):
        self.mean = y.mean()
        return self
    
    def predict(self, X):
        return np.array(X.shape[0]*[self.mean])
        
# create an instance
my_own_model = MyOwnModel()

# train model
my_model_trained = create_model(my_own_model)
```

{% endcode %}

![Output from create\_model(my\_own\_model)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FHET70Gt7KE8VBbJjRYqn%2Fimage.png?alt=media\&token=3c3d08ad-a995-4096-8688-853c20e6a12c)
