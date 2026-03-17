# Source: https://pycaret.gitbook.io/docs/get-started/functions/optimize.md

# Optimize

## tune\_model

This function tunes the hyperparameters of the model. The output of this function is a scoring grid with cross-validated scores by fold. The best model is selected based on the metric defined in `optimize` parameter. Metrics evaluated during cross-validation can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(data = boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model
tuned_dt = tune_model(dt)
```

{% endcode %}

![Output from tune\_model(dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhHdkpHKMTnPUHXNNxJOT%2Fimage.png?alt=media\&token=ae88ce2f-1604-40ca-8028-86b7e3827aee)

To compare the hyperparameters.

{% code lineNumbers="true" %}

```python
# default model
print(dt)

# tuned model
print(tuned_dt)
```

{% endcode %}

![Model hyperparameters before and after tuning](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FIPNr7C8n8VRLVDFvfPFO%2Fimage.png?alt=media\&token=1fe97343-c45e-4132-aa0a-a86139b4b241)

### Increasing the iteration

Hyperparameter tuning at the end of the day is an optimization that is constrained by the number of iterations, which eventually depends on how much time and resources you have available. The number of iterations is defined by `n_iter`. By default, it is set to `10`.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(data = boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model
tuned_dt = tune_model(dt, n_iter = 50)
```

{% endcode %}

![Output from tune\_model(dt, n\_iter = 50)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fgh42IXeyNvmVFM5UjBT0%2Fimage.png?alt=media\&token=d17c9921-9f75-4064-bfdc-ec3276d74b6c)

#### Comparison of 10 and 50 iterations

{% tabs %}
{% tab title="n\_iter = 10" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F2y9FjxQCHAVU1WeaVM8A%2Fimage.png?alt=media\&token=f96dbf67-6206-402b-98b0-3e93dcadf2df)
{% endtab %}

{% tab title="n\_iter = 50" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhL35vJn92QRenrlfE3qY%2Fimage.png?alt=media\&token=227c1df2-8890-4d05-b4f8-49baf78323e3)
{% endtab %}
{% endtabs %}

### Choosing the metric

When you are tuning the hyperparameters of the model, you must know which metric to optimize for. That can be defined under `optimize` parameter. By default, it is set to `Accuracy` for classification experiments and `R2` for regression.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(data = boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model
tuned_dt = tune_model(dt, optimize = 'MAE')
```

{% endcode %}

![Output from tune\_model(dt, optimize = 'MAE')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FBlS0jlbOLSIVGtEXWbbc%2Fimage.png?alt=media\&token=38675646-2c76-472e-8ac0-6751e031205f)

### Passing custom grid

The tuning grid for hyperparameters is already defined by PyCaret for all the models in the library. However, if you wish you can define your own search space by passing a custom grid using `custom_grid` parameter.&#x20;

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# define search space
params = {"max_depth": np.random.randint(1, (len(boston.columns)*.85),20),
          "max_features": np.random.randint(1, len(boston.columns),20),
          "min_samples_leaf": [2,3,4,5,6]}
          
# tune model
tuned_dt = tune_model(dt, custom_grid = params)
```

{% endcode %}

![Output from tune\_model(dt, custom\_grid = params)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7sV7GIM6TFDmCctJfiGv%2Fimage.png?alt=media\&token=8d495ef3-f440-45e5-808b-e1c0910fb169)

### Changing the search algorithm

PyCaret integrates seamlessly with many different libraries for hyperparameter tuning. This gives you access to many different types of search algorithms including random, bayesian, optuna, TPE, and a few others. All of this just by changing a parameter. By default, PyCaret using `RandomGridSearch` from the sklearn and you can change that by using `search_library` and `search_algorithm` parameter in the `tune_model` function.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model sklearn
tune_model(dt)

# tune model optuna
tune_model(dt, search_library = 'optuna')

# tune model scikit-optimize
tune_model(dt, search_library = 'scikit-optimize')

# tune model tune-sklearn
tune_model(dt, search_library = 'tune-sklearn', search_algorithm = 'hyperopt')
```

{% endcode %}

{% tabs %}
{% tab title="scikit-learn" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FfJFiRDk9Ze3bEJ6RWv6T%2Fimage.png?alt=media\&token=250a8c8b-a707-4bfa-a913-d2f8a7aebaa9)
{% endtab %}

{% tab title="optuna" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FXy0xCMPxsDBWODYSG1gr%2Fimage.png?alt=media\&token=34bef3b6-87af-4465-ad09-16fbd78ff3a5)
{% endtab %}

{% tab title="scikit-optimize" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FB8OstOonmsv5SCeAcbjz%2Fimage.png?alt=media\&token=944e888c-780c-4033-aa19-d33ffdc9541e)
{% endtab %}

{% tab title="tune-sklearn" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvGUEHQXvKpTD55fxLnIV%2Fimage.png?alt=media\&token=eeb5455f-c11c-4325-a089-a858166150b6)
{% endtab %}
{% endtabs %}

### Access the tuner

By default PyCaret's `tune_model` function only returns the best model as selected by the tuner. Sometimes you may need access to the tuner object as it may contain important attributes, you can use `return_tuner` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets importh get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model and return tuner
tuned_model, tuner = tune_model(dt, return_tuner=True)
```

{% endcode %}

![Output from tune\_model(dt, return\_tuner=True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FyIgZwcipADDlGuPXLcxu%2Fimage.png?alt=media\&token=235ac26b-17d9-460f-b8be-3ea97162c9a4)

{% code lineNumbers="true" %}

```python
type(tuned_model), type(tuner)
```

{% endcode %}

![Output from type(tuned\_model), type(tuner)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fy6X85zvE3EaeMzPX9W3L%2Fimage.png?alt=media\&token=702cbfba-0643-4587-8eb8-bd24a4705983)

{% code lineNumbers="true" %}

```python
print(tuner)
```

{% endcode %}

![Output from print(tuner)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FzabGCrHsPrpWHZp9Bkbj%2Fimage.png?alt=media\&token=94419c47-8660-476e-afd6-50b098313c48)

### Automatically choose better

Often times the `tune_model` will not improve the model performance. In fact, it may end up making performance worst than the model with default hyperparameters. This may be problematic when you are not actively experimenting in the Notebook rather you have a python script that runs a workflow of `create_model` --> `tune_model` or `compare_models` --> `tune_model`. To overcome this issue, you can use `choose_better`. When set to `True` it will always return a better performing model meaning that if hyperparameter tuning doesn't improve the performance, it will return the input model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# tune model
dt = tune_model(dt, choose_better = True)
```

{% endcode %}

![Output from tune\_model(dt, choose\_better = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FLgGHiJvzlydDWibW7sWo%2Fimage.png?alt=media\&token=df41bd3c-7b2a-4500-9bc0-fc1d68a4ccf9)

{% hint style="info" %}
**NOTE:** `choose_better` doesn't affect the scoring grid that is displayed on the screen. The scoring grid will always present the performance of the best model as selected by the tuner, regardless of the fact that output performance < input performance.
{% endhint %}

## ensemble\_model

This function ensembles a given estimator. The output of this function is a scoring grid with CV scores by fold. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# ensemble model
bagged_dt = ensemble_model(dt)
```

{% endcode %}

![Output from ensemble\_model(dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdMb6Yw8gIUnvXE2jJ3Ab%2Fimage.png?alt=media\&token=76409661-e52e-41db-9f29-73702aa81c65)

{% code lineNumbers="true" %}

```python
type(bagged_dt)
# >>> sklearn.ensemble._bagging.BaggingRegressor

print(bagged_dt)
```

{% endcode %}

![Output from print(bagged\_dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FDnwGe38rPLUdTeT5QixV%2Fimage.png?alt=media\&token=a296dee9-4ba0-4ec6-9791-4b91fa57f0c5)

### **Changing the fold param**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# ensemble model
bagged_dt = ensemble_model(dt, fold = 5)
```

{% endcode %}

![Output from ensemble\_model(dt, fold = 5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FWXE8uYmslordrGGwpt6S%2Fimage.png?alt=media\&token=c219f8bc-20b2-491e-b19f-f3d0c29fb4a6)

The model returned by this is the same as above, however, the performance evaluation is done using 5 fold cross-validation.&#x20;

### **Method: Bagging**

Bagging, also known as *Bootstrap aggregating*, is a machine learning ensemble meta-algorithm designed to improve the stability and accuracy of machine learning algorithms used in statistical classification and regression. It also reduces variance and helps to avoid overfitting. Although it is usually applied to decision tree methods, it can be used with any type of method. Bagging is a special case of the model averaging approach.

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FFXzkptzyZun6LXGEIwcT%2Fimage.png?alt=media\&token=f956cd5c-0e54-447a-9de2-46ac774b3b6b)

### **Method: Boosting**

Boosting is an ensemble meta-algorithm for primarily reducing bias and variance in supervised learning. Boosting is in the family of machine learning algorithms that convert weak learners to strong ones. A weak learner is defined to be a classifier that is only slightly correlated with the true classification (it can label examples better than random guessing). In contrast, a strong learner is a classifier that is arbitrarily well-correlated with the true classification.

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F61FlBrwHTtdqlS1n2w2j%2Fimage.png?alt=media\&token=73d0c25a-3440-4a11-9a42-339c6a45d6d3)

### Choosing the method

There are two possible ways you can ensemble your machine learning model with `ensemble_model`. You can define this in the `method` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# ensemble model
boosted_dt = ensemble_model(dt, method = 'Boosting')
```

{% endcode %}

![Output from ensemble\_model(dt, method = 'Boosting')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fmebhy4RIGsqVQTKYIuIv%2Fimage.png?alt=media\&token=45756008-f945-4681-a867-cd0b7360d849)

{% code lineNumbers="true" %}

```python
type(boosted_dt)
# >>> sklearn.ensemble._weight_boosting.AdaBoostRegressor

print(boosted_dt)
```

{% endcode %}

![Output from print(boosted\_dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fk9Z7sPNR8XeqF1sUzMfY%2Fimage.png?alt=media\&token=3f293f4d-72a9-49f4-8ce8-3185403cd470)

### Increasing the estimators

By default, PyCaret uses 10 estimators for both `Bagging` or `Boosting`. You can increase that by changing `n_estimators` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
dt = create_model('dt')

# ensemble model
ensemble_model(dt, n_estimators = 100)
```

{% endcode %}

![Output from ensemble\_model(dt, n\_estimators = 100)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhixYpXgNzLPfGNG4hGDi%2Fimage.png?alt=media\&token=c548c7ab-daa7-4fb9-9d5c-1f55bcb5829d)

### Automatically choose better

Often times the `ensemble_model` will not improve the model performance. In fact, it may end up making performance worst than the model with ensembling. This may be problematic when you are not actively experimenting in the Notebook rather you have a python script that runs a workflow of `create_model` --> `ensemble_model` or `compare_models` --> `ensemble_model`. To overcome this issue, you can use `choose_better`. When set to `True` it will always return a better performing model meaning that if hyperparameter tuning doesn't improve the performance, it will return the input model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data 
boston = get_data('boston') 

# init setup
from pycaret.regression import * 
reg1 = setup(boston, target = 'medv')

# train model
lr = create_model('lr')

# ensemble model
ensemble_model(lr, choose_better = True)
```

{% endcode %}

![Output from ensemble\_model(lr, choose\_better = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJJJcX5JCT9dsU9wSUrcj%2Fimage.png?alt=media\&token=720fcfc3-a10a-4f1f-a01b-e51abd20194a)

Notice that with `choose_better = True` the model returned from the `ensemble_model` is a simple `LinearRegression` instead of `BaggedRegressor`. This is because the performance of the model didn't improve after ensembling and hence input model is returned.&#x20;

## blend\_models

This function trains a Soft Voting / Majority Rule classifier for select models passed in the `estimator_list` parameter. The output of this function is a scoring grid with CV scores by fold. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender = blend_models([lr, dt, knn])
```

{% endcode %}

![Output from blend\_models(\[lr, dt, knn\])](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F8IrWtcxC4pFXOdAVEW7D%2Fimage.png?alt=media\&token=16e1256c-2d03-4504-9473-09dde9354070)

{% code lineNumbers="true" %}

```python
type(blender)
# >>> sklearn.ensemble._voting.VotingClassifier

print(blender)
```

{% endcode %}

![Output from print(blender)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FRkB7cStOzSXjta5ULz0Q%2Fimage.png?alt=media\&token=d98940a5-4cc8-4886-8f93-55ac29d93155)

### Changing the fold param

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender = blend_models([lr, dt, knn], fold = 5)
```

{% endcode %}

![Output from blend\_models(\[lr, dt, knn\], fold = 5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7fOOMmFhUzwaUFr1XIc8%2Fimage.png?alt=media\&token=a24c6811-1737-4e65-8b2a-24a555238876)

The model returned by this is the same as above, however, the performance evaluation is done using 5 fold cross-validation.&#x20;

### Dynamic input estimators

You can also automatically generate the list of input estimators using the [compare\_models](https://pycaret.gitbook.io/docs/get-started/train#compare_models) function. The benefit of this is that you do not have the change your script at all. Every time the top N models are used as an input list.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# blend models
blender = blend_models(compare_models(n_select = 3))
```

{% endcode %}

![Output from blend\_models(compare\_models(n\_select = 3))](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F9JkyxBCjjbdqy6482esM%2Fimage.png?alt=media\&token=e0d3ceb4-6ed9-4519-8433-74a9203319f0)

Notice here what happens. We passed `compare_models(n_select = 3` as an input to `blend_models`. What happened internally is that the `compare_models` function got executed first and the top 3 models are then passed as an input to the `blend_models` function.&#x20;

{% code lineNumbers="true" %}

```python
print(blender)
```

{% endcode %}

![Output from print(blender)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F10DwvBhXz4hwzfrH8gJZ%2Fimage.png?alt=media\&token=f69383d8-cc6d-4916-bb68-a294a830cb64)

In this example, the top 3 models as evaluated by the `compare_models` are `LogisticRegression`, `LinearDiscriminantAnalysis`, and `RandomForestClassifier`.

### Changing the method

When `method = 'soft'`, it predicts the class label based on the argmax of the sums of the predicted probabilities, which is recommended for an ensemble of well-calibrated classifiers.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender_soft = blend_models([lr,dt,knn], method = 'soft')
```

{% endcode %}

![Output from blend\_models(\[lr,dt,knn\], method = 'soft')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fgzq4vRMiQdphEz8BjT6K%2Fimage.png?alt=media\&token=45a38c23-5522-413d-b300-2d716bbdd254)

When the `method = 'hard'` , it uses the predictions (hard labels) from input models instead of probabilities.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender_hard = blend_models([lr,dt,knn], method = 'hard')
```

{% endcode %}

![Output from blend\_models(\[lr,dt,knn\], method = 'hard')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJh3yLorabKayZOavnOhg%2Fimage.png?alt=media\&token=6e918463-4b91-4fd6-9ad1-0e3506caa613)

The default method is set to `auto` which means it will try to use `soft` method and fall back to `hard` if the former is not supported, this may happen when one of your input models does not support `predict_proba` attribute.

{% hint style="info" %}
**NOTE:** Method parameter is only available in [Classification](https://pycaret.gitbook.io/docs/get-started/modules) module.
{% endhint %}

### Changing the weights

By default, all the input models are given equal weight when blending them but you can explicitly pass the weights to be given to each input model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender_weighted = blend_models([lr,dt,knn], weights = [0.5,0.2,0.3])
```

{% endcode %}

![Output from blend\_models(\[lr,dt,knn\], weights = \[0.5,0.2,0.3\])](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FR8yI9m4xGxGs9P9jNRN3%2Fimage.png?alt=media\&token=07838157-b7c2-4f6d-bca2-3f6896815551)

You can also tune the weights of the blender using the `tune_model`.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blender_weighted = blend_models([lr,dt,knn], weights = [0.5,0.2,0.3])

# tune blender
tuned_blender = tune_model(blender_weighted)
```

{% endcode %}

![Output from tune\_model(blender\_weighted)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F4uz8BqkCQYRsolTYJfUa%2Fimage.png?alt=media\&token=73a473b6-47c2-4ff0-8606-3bda788e3c49)

{% code lineNumbers="true" %}

```python
print(tuned_blender)
```

{% endcode %}

![Output from print(tuned\_blender)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FCK2twQKIZa3k3m5Iv8hW%2Fimage.png?alt=media\&token=dcd38182-fac2-4f99-931a-412bfa8ac81f)

### Automatically choose better

Often times the `blend_models` will not improve the model performance. In fact, it may end up making performance worst than the model with blending. This may be problematic when you are not actively experimenting in the Notebook rather you have a python script that runs a workflow of `compare_models` --> `blend_models`. To overcome this issue, you can use `choose_better`. When set to `True` it will always return a better performing model meaning that if blending the models doesn't improve the performance, it will return the single best performing input model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# blend models
blend_models([lr,dt,knn], choose_better = True)
```

{% endcode %}

![Output from blend\_models(\[lr,dt,knn\], choose\_better = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FjECdDxmsqB3mREFKJRDh%2Fimage.png?alt=media\&token=d406d748-f2aa-4501-af36-d79786c69d42)

Notice that because `choose_better=True` the final model returned by this function is `LogisticRegression` instead of `VotingClassifier` because the performance of Logistic Regression was most optimized out of all the given input models plus the blender.

## stack\_models

This function trains a meta-model over select estimators passed in the `estimator_list` parameter. The output of this function is a scoring grid with CV scores by fold. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# stack models
stacker = stack_models([lr, dt, knn])
```

{% endcode %}

![Output from stack\_models(\[lr, dt, knn\])](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FXohlwJ9tbYgnr9t76L1l%2Fimage.png?alt=media\&token=efd9d1da-9efc-4128-a096-f95364b26308)

### Changing the fold param

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# stack models
stacker = stack_models([lr, dt, knn], fold = 5)
```

{% endcode %}

![Output from stack\_models(\[lr, dt, knn\], fold = 5)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FpWyHosBweCIpu1ceHnfo%2Fimage.png?alt=media\&token=8f4dd930-2454-444d-aef3-dd6833a0d6a8)

The model returned by this is the same as above, however, the performance evaluation is done using 5 fold cross-validation.&#x20;

### Dynamic input estimators

You can also automatically generate the list of input estimators using the [compare\_models](https://pycaret.gitbook.io/docs/get-started/train#compare_models) function. The benefit of this is that you do not have the change your script at all. Every time the top N models are used as an input list.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# stack models
stacker = stack_models(compare_models(n_select = 3))
```

{% endcode %}

![Output from stack\_models(compare\_models(n\_select = 3))](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FQLJ0G2odCKx8YkcHvD0K%2Fimage.png?alt=media\&token=054f664d-ac99-49fc-9fe7-594b8714d1cd)

Notice here what happens. We passed `compare_models(n_select = 3` as an input to `stack_models`. What happened internally is that the `compare_models` function got executed first and the top 3 models are then passed as an input to the `stack_models` function.&#x20;

{% code lineNumbers="true" %}

```python
print(stacker)
```

{% endcode %}

![Output from print(stacker)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FxVxJCkXPevGNu9XEw69U%2Fimage.png?alt=media\&token=6b5a613a-a03e-4d1c-a6c8-770e9c6ee223)

In this example, the top 3 models as evaluated by the `compare_models` are `LogisticRegression`, `RandomForestClassifier`, and `LGBMClassifier`.

### Changing the method

There are a few different methods you can explicitly choose for stacking or pass `auto` to be automatically determined. When set to `auto`, it will invoke, for each model, `predict_proba`, `decision_function` or `predict` function in that order. Alternatively, you can define the method explicitly.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# stack models
stacker = stack_models([lr, dt, knn], method = 'predict')
```

{% endcode %}

![Output from stack\_models(\[lr, dt, knn\], method = 'predict')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FkLEZTDdOjnDQCiD9Q7hw%2Fimage.png?alt=media\&token=846333f3-9d94-4ea8-b4ab-2497eabdf40a)

### Changing the meta-model

When no `meta_model` is passed explicitly, `LogisticRegression` is used for Classification experiments and `LinearRegression` is used for Regression experiments. You can also pass a specific model to be used as a meta-model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# train meta-model
lightgbm = create_model('lightgbm')

# stack models
stacker = stack_models([lr, dt, knn], meta_model = lightgbm)
```

{% endcode %}

![Output from stack\_models(\[lr, dt, knn\], meta\_model = lightgbm)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJtT9tOUWVoGgjxjaNW6A%2Fimage.png?alt=media\&token=3c0e821d-15f2-4ce7-948a-db88e424bd34)

{% code lineNumbers="true" %}

```python
print(stacker.final_estimator_)
```

{% endcode %}

![Output from print(stacker.final\_estimator\_)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdaNfdOhk7GZqhK546E2V%2Fimage.png?alt=media\&token=4fbb098e-1290-4d51-9e3f-3e755452f263)

### Restacking

There are two ways you can stack models. (i) only the predictions of input models will be used as training data for meta-model, (ii) predictions as well as the original training data is used for training meta-model.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a few models
lr = create_model('lr')
dt = create_model('dt')
knn = create_model('knn')

# stack models
stacker = stack_models([lr, dt, knn], restack = False)
```

{% endcode %}

![Output from stack\_models(\[lr, dt, knn\], restack = False)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FufMyNtHXS3AEGfGgqykA%2Fimage.png?alt=media\&token=8333e738-286b-46f5-a178-1491206f6021)

## optimize\_threshold

This function optimizes the probability threshold for a trained model. It iterates over performance metrics at different `probability_threshold` with a step size defined in `grid_interval` parameter. This function will display a plot of the performance metrics at each probability threshold and returns the best model based on the metric defined under `optimize` parameter.

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a model
knn = create_model('knn')

# optimize threshold
optimized_knn = optimize_threshold(knn)
```

{% endcode %}

![Output from optimize\_threshold(knn)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FrVDxd2Z0oRuvnpEGBBaw%2Fimage.png?alt=media\&token=4884c1e6-d323-4953-b532-7936a49aedf6)

{% code lineNumbers="true" %}

```python
print(optimized_knn)
```

{% endcode %}

![Output from print(optimized\_knn)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FaQqd60HtAycdlAK26lrr%2Fimage.png?alt=media\&token=778ce66b-0bd0-459e-9900-10f6e2d4421b)

## calibrate\_model

This function calibrates the probability of a given model using isotonic or logistic regression. The output of this function is a scoring grid with CV scores by fold. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# train a model
dt = create_model('dt')

# calibrate model
calibrated_dt = calibrate_model(dt)
```

{% endcode %}

![Output from calibrate\_model(dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FheXcOAst84BhgKNUH3VD%2Fimage.png?alt=media\&token=ab59f451-cc18-444a-b2a3-1592bca1c712)

{% code lineNumbers="true" %}

```python
print(calibrated_dt)
```

{% endcode %}

![Output from print(calibrated\_dt)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fo591iaUMDkV7T18dhpiJ%2Fimage.png?alt=media\&token=1b6cb725-3230-4c05-b917-2b5c52369790)

### Before and after calibration

{% tabs %}
{% tab title="Before Calibration" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FIOVnnxBgLWBZzYyZZOnt%2Fimage.png?alt=media\&token=2d387074-337b-41d6-85b2-fa7afcfd7e6d)
{% endtab %}

{% tab title="After Calibration" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FGRPeHzcMMt2i4iXo3LPp%2Fimage.png?alt=media\&token=073bcaba-46ec-4c78-91b7-f05d79fb1ec0)
{% endtab %}
{% endtabs %}
