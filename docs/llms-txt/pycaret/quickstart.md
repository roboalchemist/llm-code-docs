# Source: https://pycaret.gitbook.io/docs/get-started/quickstart.md

# Quickstart

## 🚀 Classification

PyCaret’s Classification Module is a supervised machine learning module that is used for classifying elements into groups.&#x20;

The goal is to predict the categorical class labels which are discrete and unordered. Some common use cases include predicting customer default (Yes or No), predicting customer churn (customer will leave or stay), the disease found (positive or negative).&#x20;

This module can be used for binary or multiclass problems.

### Setup

This function initializes the training environment and creates the transformation pipeline. Setup function must be called before executing any other function. It takes two required parameters: `data` and `target`. All the other parameters are optional.

{% code lineNumbers="true" %}

```python
# load sample dataset
from pycaret.datasets import get_data
data = get_data('diabetes')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5U2BBphBFsSfcSlsyGZM%2Fimage.png?alt=media\&token=e2b090c5-737e-41b8-9c45-bd39e1a5e405)

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'Class variable', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FW9pVJ19CD8Q33vG0xXWA%2Fimage.png?alt=media&#x26;token=154e96f6-c143-4f44-ae88-a84a256a17fe" alt=""><figcaption></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
from pycaret.classification import ClassificationExperiment
s = ClassificationExperiment()
s.setup(data, target = 'Class variable', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fk2GTFDdk4WumaLRUIqBs%2Fimage.png?alt=media&#x26;token=88050c7a-2a8c-4e84-a415-a4eed4cd8ae1" alt=""><figcaption></figcaption></figure>

### Compare Models

This function trains and evaluates the performance of all the estimators available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

{% code lineNumbers="true" %}

```python
# functional API
best = compare_models()

# OOP API
best = s.compare_models()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUtiB2Sp5BipJDf21um7v%2Fimage.png?alt=media&#x26;token=df4d3823-bad3-49d9-b2ad-c877f177cc4d" alt=""><figcaption></figcaption></figure>

```python
print(best)
```

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJP7j6x3oc8lHyl1yssmt%2Fimage.png?alt=media&#x26;token=f85c8171-e521-455b-9ad5-fe79374affd4" alt=""><figcaption></figcaption></figure>

### Analyze Model

This function analyzes the performance of a trained model on the test set. It may require re-training the model in certain cases.

{% code lineNumbers="true" %}

```python
# functional API
evaluate_model(best)

# OOP API
s.evaluate_model(best)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FcdCGBvM3Yd97lztq94FI%2Fimage.png?alt=media&#x26;token=4bfb4c8c-2f5f-4afe-85f0-c3f82f098fdf" alt=""><figcaption></figcaption></figure>

`evaluate_model` can only be used in Notebook since it uses `ipywidget` . You can also use the `plot_model` function to generate plots individually.

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'auc')

# OOP API
s.plot_model(best, plot = 'auc')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvO466Di18wa5YZucxgep%2Fimage.png?alt=media&#x26;token=fc6b8773-082b-4b01-ba21-01cc6a1132c0" alt=""><figcaption></figcaption></figure>

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'confusion_matrix')

# OOP API
s.plot_model(best, plot = 'confusion_matrix')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F89GckExsAGBkyTddfjLa%2Fimage.png?alt=media&#x26;token=3de87c3c-bf2f-44b7-91f4-705c3a32136b" alt=""><figcaption></figcaption></figure>

### Predictions

This function scores the data and returns `prediction_label` and `prediction_score` probability of the predicted class). When `data` is None, it predicts label and score on the test set (created during the `setup` function).

{% code lineNumbers="true" %}

```python
# functional API
predict_model(best)

# OOP API
s.predict_model(best)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FakE6oZLiQTuzhy4WfsC2%2Fimage.png?alt=media&#x26;token=25da01cb-8f1a-471e-94f9-a6fcb3b2b416" alt=""><figcaption></figcaption></figure>

The evaluation metrics are calculated on the test set. The second output is the `pd.DataFrame` with predictions on the test set (see the last two columns). To generate labels on the unseen (new) dataset, simply pass the dataset in the `data` parameter under `predict_model` function.

{% code lineNumbers="true" %}

```python
# functional API
predictions = predict_model(best, data=data)
predictions.head()

# OOP API
predictions = s.predict_model(best, data=data)
predictions.head()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Frb4GrxRl1x2d8jrkalhC%2Fimage.png?alt=media&#x26;token=0eda716b-367a-460e-9b02-38962b914174" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
`Score` means the probability of the predicted class (NOT the positive class). If `prediction_label` is 0 and `prediction_score` is 0.90, this means 90% probability of class 0. If you want to see the probability of both the classes, simply pass `raw_score=True` in the `predict_model` function.
{% endhint %}

{% code lineNumbers="true" %}

```python
# functional API
predictions = predict_model(best, data=data, raw_score=True)
predictions.head()

# OOP API
predictions = s.predict_model(best, data=data, raw_score=True)
predictions.head()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F44oYosDk7LRNA5TtPTfv%2Fimage.png?alt=media&#x26;token=d974854c-10a0-4622-8f5e-50e4ac9819da" alt=""><figcaption></figcaption></figure>

### Save the model

{% code lineNumbers="true" %}

```python
# functional API
save_model(best, 'my_best_pipeline')

# OOP API
s.save_model(best, 'my_best_pipeline')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FymY62Cxyr54JGDX445iF%2Fimage.png?alt=media&#x26;token=f756e58e-b9ae-4d76-b6d2-4b71f0825fa8" alt=""><figcaption></figcaption></figure>

#### To load the model back in environment:

{% code lineNumbers="true" %}

```python
# functional API
loaded_model = load_model('my_best_pipeline')
print(loaded_model)

# OOP API
loaded_model = s.load_model('my_best_pipeline')
print(loaded_model)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FIVKfnPAmLUj3abrs6Xuk%2Fimage.png?alt=media&#x26;token=4d69275f-928c-4b42-9194-1df96170959e" alt=""><figcaption></figcaption></figure>

## 🚀 Regression

PyCaret’s Regression Module is a supervised machine learning module that is used for estimating the relationships between a dependent variable (often called the ‘outcome variable’, or ‘target’) and one or more independent variables (often called ‘features’, ‘predictors’, or ‘covariates’).&#x20;

The objective of regression is to predict continuous values such as predicting sales amount, predicting quantity, predicting temperature, etc.&#x20;

### Setup

This function initializes the training environment and creates the transformation pipeline. Setup function must be called before executing any other function. It takes two required parameters: `data` and `target`. All the other parameters are optional.

{% code lineNumbers="true" %}

```python
# load sample dataset
from pycaret.datasets import get_data
data = get_data('insurance')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FsMxgjIJMlzBQ9AiURI7j%2Fimage.png?alt=media\&token=16244830-3866-4c0c-9ffa-c5b90be68453)

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
from pycaret.regression import *
s = setup(data, target = 'charges', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F0vc6dExhP75GbM9BI0q8%2Fimage.png?alt=media&#x26;token=de0a9fb5-6a17-40d8-b64a-546d50f67bdd" alt=""><figcaption></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
from pycaret.regression import RegressionExperiment
s = RegressionExperiment()
s.setup(data, target = 'charges', session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FroGTJqihiS3rbd7OhpCN%2Fimage.png?alt=media&#x26;token=f8c250cc-9ad1-4040-b604-c604164ab3a5" alt=""><figcaption></figcaption></figure>

### Compare Models

This function trains and evaluates the performance of all the estimators available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

{% code lineNumbers="true" %}

```python
# functional API
best = compare_models()

# OOP API
best = s.compare_models()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fq8hcDvd3mXX0cJmATwj3%2Fimage.png?alt=media&#x26;token=9b3437a5-c948-4c76-8e37-3b8c897aa979" alt=""><figcaption></figcaption></figure>

{% code lineNumbers="true" %}

```python
print(best)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FXt097C0ow7ogvG2gCWke%2Fimage.png?alt=media\&token=0b3ce25d-1179-4e64-8f7a-b009182c3e70)

### Analyze Model

This function analyzes the performance of a trained model on the test set. It may require re-training the model in certain cases.

{% code lineNumbers="true" %}

```python
# functional API
evaluate_model(best)

# OOP API
s.evaluate_model(best)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F3KetonD4noSlLz0OYLer%2Fimage.png?alt=media\&token=466ab784-3f96-4d8a-94ce-f7a4ebce48fe)

`evaluate_model` can only be used in Notebook since it uses `ipywidget` . You can also use the `plot_model` function to generate plots individually.

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'residuals')

# OOP API
s.plot_model(best, plot = 'residuals')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FeWhXaKw4ggYDxOJXOPzl%2Fimage.png?alt=media\&token=1c812d1d-f803-41d9-a36b-9fc30e6877b6)

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'feature')

# OOP API
s.plot_model(best, plot = 'feature')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FYOj4B77LuZPbkkkBCfii%2Fimage.png?alt=media\&token=a528b8a1-552e-449a-83fa-e1711704ce67)

### Predictions

This function predicts `prediction_label` using the trained model. When `data` is None, it predicts label and score on the test set (created during the `setup` function).

{% code lineNumbers="true" %}

```python
# functional API
predict_model(best)

# OOP API
s.predict_model(best)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FpIJP7YUoJSZSqAxrSfv0%2Fimage.png?alt=media&#x26;token=1e851c7b-8f50-4ba5-852a-3fec64bb69f6" alt=""><figcaption></figcaption></figure>

The evaluation metrics are calculated on the test set. The second output is the `pd.DataFrame` with predictions on the test set (see the last two columns). To generate labels on the unseen (new) dataset, simply pass the dataset in the `predict_model` function.

{% code lineNumbers="true" %}

```python
# functional API
predictions = predict_model(best, data=data)
predictions.head()

# OOP API
predictions = s.predict_model(best, data=data)
predictions.head()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FONUCKRAo9UFe10YhdoWl%2Fimage.png?alt=media&#x26;token=f5da4421-49ed-443e-b258-e7144d9a598d" alt=""><figcaption></figcaption></figure>

### Save the model

{% code lineNumbers="true" %}

```python
# functional API
save_model(best, 'my_best_pipeline')

# OOP API
s.save_model(best, 'my_best_pipeline')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5hsJmcbCMmhI4OzOE9dQ%2Fimage.png?alt=media&#x26;token=cd3821a3-a66a-4bd5-8771-bd6033363d3c" alt=""><figcaption></figcaption></figure>

#### To load the model back in the environment:

{% code lineNumbers="true" %}

```python
# functional API
loaded_model = load_model('my_best_pipeline')
print(loaded_model)

# OOP API
loaded_model = s.load_model('my_best_pipeline')
print(loaded_model)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FMLRgoqXUzYNPZfmYgaXA%2Fimage.png?alt=media&#x26;token=96d6555c-b6a5-4160-be00-02b17c7be36b" alt=""><figcaption></figcaption></figure>

## 🚀 Clustering

PyCaret’s Clustering Module is an unsupervised machine learning module that performs the task of grouping a set of objects in such a way that objects in the same group (also known as a cluster) are more similar to each other than to those in other groups.&#x20;

### Setup

This function initializes the training environment and creates the transformation pipeline. Setup function must be called before executing any other function. It takes only one required parameter: `data`. All the other parameters are optional.

{% code lineNumbers="true" %}

```python
# load sample dataset
from pycaret.datasets import get_data
data = get_data('jewellery')
```

{% endcode %}

<div align="left"><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fi8pTNJjO5DvuOoeJ56Ju%2Fimage.png?alt=media&#x26;token=db6f09a0-fbb7-40dd-88d2-5a05b9735667" alt=""></div>

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
from pycaret.clustering import *
s = setup(data, normalize = True)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FmqRTmwbY8f04OkDCijm6%2Fimage.png?alt=media&#x26;token=8be3e985-402d-4fdd-862b-87797b3ecaf6" alt=""><figcaption></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
from pycaret.clustering import ClusteringExperiment
s = ClusteringExperiment()
s.setup(data, normalize = True)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FEjj9MOX85rETkvisANga%2Fimage.png?alt=media&#x26;token=870947d6-0b3f-40fc-b09e-7584f383729e" alt=""><figcaption></figcaption></figure>

### Create Model

This function trains and evaluates the performance of a given model. Metrics evaluated can be accessed using the `get_metrics` function. Custom metrics can be added or removed using the `add_metric` and `remove_metric` function. All the available models can be accessed using the `models` function.

{% code lineNumbers="true" %}

```python
# functional API
kmeans = create_model('kmeans')

# OOP API
kmeans = s.create_model('kmeans')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FIKjzb4JfIAt8bO1WFK9i%2Fimage.png?alt=media\&token=78e46491-088b-4217-a513-a1e2a783d685)

```python
print(kmeans)
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FL7aJfstibPp8nsZGT7V0%2Fimage.png?alt=media\&token=3e08f809-0d0f-4185-a56c-f77c1ee5a1b1)

### Analyze Model

This function analyzes the performance of a trained model.

{% code lineNumbers="true" %}

```python
# functional API
evaluate_model(kmeans)

# OOP API
s.evaluate_model(kmeans)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdtVCfZPgB8pXNlxmzPJe%2Fimage.png?alt=media\&token=5dc4a5ec-2b33-44df-9710-c1e8e0fc7eb4)

`evaluate_model` can only be used in Notebook since it uses `ipywidget` . You can also use the `plot_model` function to generate plots individually.

{% code lineNumbers="true" %}

```python
# functional API
plot_model(kmeans, plot = 'elbow')

# OOP API
s.plot_model(kmeans, plot = 'elbow')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F6MfAIzbFMek1bqH1oQAC%2Fimage.png?alt=media\&token=1aceee9c-883b-433d-bd9e-7692fc54303d)

{% code lineNumbers="true" %}

```python
# functional API
plot_model(kmeans, plot = 'silhouette')

# OOP API
s.plot_model(kmeans, plot = 'silhouette')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FZ4keCAYY22ZrOb0yrVIS%2Fimage.png?alt=media\&token=169888ee-d044-4d2d-b0b5-2e001289bb05)

### Assign Model

This function assigns cluster labels to the training data, given a trained model.

{% code lineNumbers="true" %}

```python
# functional API
result = assign_model(kmeans)
result.head()

# OOP API
result = s.assign_model(kmeans)
result.head()
```

{% endcode %}

<div align="left"><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FMHYGUMkuZQOAvKmZANJV%2Fimage.png?alt=media&#x26;token=ea47e057-43d2-4115-81c5-f7fb0da707d1" alt=""></div>

### Predictions

This function generates cluster labels using a trained model on the new/unseen dataset.

{% code lineNumbers="true" %}

```python
# functional API
predictions = predict_model(kmeans, data = data)
predictions.head()

# OOP API
predictions = s.predict_model(kmeans, data = data)
predictions.head()
```

{% endcode %}

<div align="left"><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FQG8IAqb3EVJYRUHZmqpe%2Fimage.png?alt=media&#x26;token=7c97f2b6-77c9-4874-91f2-120b378077f3" alt=""></div>

### Save the model

{% code lineNumbers="true" %}

```python
# functional API
save_model(kmeans, 'kmeans_pipeline')

# OOP API
s.save_model(kmeans, 'kmeans_pipeline')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F3R2O1AVwL25AkK0hdWu3%2Fimage.png?alt=media&#x26;token=b3deb3b2-2ca0-4c3d-8b3f-3dfe0bde0309" alt=""><figcaption></figcaption></figure>

#### To load the model back in the environment:

{% code lineNumbers="true" %}

```python
# functional API
loaded_model = load_model('kmeans_pipeline')
print(loaded_model)

# OOP API
loaded_model = s.load_model('kmeans_pipeline')
print(loaded_model)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FeON83m6DILg4fY8C1ZtH%2Fimage.png?alt=media&#x26;token=caa804ba-1f6a-4d46-9f80-7c433892cb8b" alt=""><figcaption></figcaption></figure>

## 🚀 Anomaly Detection

PyCaret’s Anomaly Detection Module is an unsupervised machine learning module that is used for identifying rare items, events, or observations that raise suspicions by differing significantly from the majority of the data.&#x20;

Typically, the anomalous items will translate to some kind of problems such as bank fraud, a structural defect, medical problems, or errors.&#x20;

### Setup

This function initializes the training environment and creates the transformation pipeline. The `setup` function must be called before executing any other function. It takes only one required parameter only: `data`. All the other parameters are optional.

{% code lineNumbers="true" %}

```python
# load sample dataset
from pycaret.datasets import get_data
data = get_data('anomaly')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fn4jYt5goCQsXvU0ZUGxD%2Fimage.png?alt=media\&token=b6c718b3-0947-42f3-a2d7-6d4d4910fe20)

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
from pycaret.anomaly import *
s = setup(data, session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJHvav2KRFqjHsG9Qvx6l%2Fimage.png?alt=media&#x26;token=300a23b1-3129-45df-b6e5-0906661ac5f7" alt=""><figcaption></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
from pycaret.anomaly import AnomalyExperiment
s = AnomalyExperiment()
s.setup(data, session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Frj3Ug3xzDSNuEsI5rLv2%2Fimage.png?alt=media&#x26;token=58d2389c-acc9-4bb2-b11c-974aa47af735" alt=""><figcaption></figcaption></figure>

### Create Model

This function trains an unsupervised anomaly detection model. All the available models can be accessed using the `models` function.

{% code lineNumbers="true" %}

```python
# functional API
iforest = create_model('iforest')
print(iforest)

# OOP API
iforest = s.create_model('iforest')
print(iforest)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fjnpvo0N24riGLSshsuol%2Fimage.png?alt=media\&token=ae889ed8-d862-4f66-9fd6-d567306cc047)

{% code lineNumbers="true" %}

```python
# functional API
models()

# OOP API
s.models()
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FBejwdtktIW4DVqEUfYH6%2Fimage.png?alt=media\&token=106cd110-f184-4135-bc93-1932f75aeabd)

### Analyze Model

{% code lineNumbers="true" %}

```python
# functional API
plot_model(iforest, plot = 'tsne')

# OOP API
s.plot_model(iforest, plot = 'tsne')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FrgndrZdEr2sprihjun1e%2Fimage.png?alt=media\&token=a3c58124-d954-4628-9e94-7e2640b763cf)

{% code lineNumbers="true" %}

```python
# functional API
plot_model(iforest, plot = 'umap')

# OOP API
s.plot_model(iforest, plot = 'umap')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FMp15gZp687RIJWqSG7hV%2Fimage.png?alt=media\&token=9bfd1a62-11e9-4ad5-84af-76eacaf33272)

### Assign Model

This function assigns anomaly labels to the dataset for a given model. (1 = outlier, 0 = inlier).

{% code lineNumbers="true" %}

```python
# functional API
result = assign_model(iforest)
result.head()

# OOP API
result = s.assign_model(iforest)
result.head()
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F0PtlvN2PTuvVpbuooi8F%2Fimage.png?alt=media\&token=3a79d80c-ab05-441b-99bd-bc6df769e87c)

### Predictions

This function generates anomaly labels using a trained model on the new/unseen dataset.

{% code lineNumbers="true" %}

```python
# functional API
predictions = predict_model(iforest, data = data)
predictions.head()

# OOP API
predictions = s.predict_model(iforest, data = data)
predictions.head()
```

{% endcode %}

![Output from predict\_model(iforest, data = data)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FmuABcClAAEDc3mfFw5Eq%2Fimage.png?alt=media\&token=cd9af919-69a2-482c-8f69-6e045979b177)

### Save the model

{% code lineNumbers="true" %}

```python
# functional API
save_model(iforest, 'iforest_pipeline')

# OOP API
s.save_model(iforest, 'iforest_pipeline')
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdowXWwartS2QqUFAnUFH%2Fimage.png?alt=media&#x26;token=c52b295d-3cf1-4987-a91b-20a175b1b89e" alt=""><figcaption></figcaption></figure>

To load the model back in the environment:

{% code lineNumbers="true" %}

```python
# functional API
loaded_model = load_model('iforest_pipeline')
print(loaded_model)

# OOP API
loaded_model = s.load_model('iforest_pipeline')
print(loaded_model)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJE1Qv6Gw4MLzGicmbx0O%2Fimage.png?alt=media&#x26;token=731e3eac-8497-497a-a0e4-a02cb17c8fe4" alt=""><figcaption></figcaption></figure>

## 🚀 Time Series

PyCaret Time Series module is a powerful tool for analyzing and predicting time series data using machine learning and classical statistical techniques. This module enables users to easily perform complex time series forecasting tasks by automating the entire process from data preparation to model deployment.&#x20;

PyCaret Time Series Forecasting module supports a wide range of forecasting methods such as ARIMA, Prophet, and LSTM. It also provides various features to handle missing values, time series decomposition, and data visualizations.&#x20;

### Setup

This function initializes the training environment and creates the transformation pipeline. Setup function must be called before executing any other function.

{% code lineNumbers="true" %}

```python
# load sample dataset
from pycaret.datasets import get_data
data = get_data('airline')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FFYeu3MpPvc5eVdrhjegt%2Fimage.png?alt=media\&token=39a5f671-0e88-46ea-82f7-9f77821cd4e8)

PyCaret 3.0 has two API's. You can choose one of it based on your preference. The functionalities and experiment results are consistent.

#### Functional API

{% code lineNumbers="true" %}

```python
from pycaret.time_series import *
s = setup(data, fh = 3, fold = 5, session_id = 123)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FbQTARxuMTdAUbzzgteZZ%2Fimage.png?alt=media&#x26;token=f9a00b0b-10f7-49f9-af3e-3e5985f50a78" alt=""><figcaption><p>Output truncated</p></figcaption></figure>

#### OOP API

{% code lineNumbers="true" %}

```python
from pycaret.time_series import TSForecastingExperiment
s = TSForecastingExperiment()
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F8ghI5F3eEUg0DKEvSMSG%2Fimage.png?alt=media&#x26;token=09bee00e-f1f6-4f9d-8d04-dcd3968c173b" alt=""><figcaption><p>Output truncated</p></figcaption></figure>

### Compare Models

This function trains and evaluates the performance of all the estimators available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores. Metrics evaluated during CV can be accessed using the `get_metrics` function. Custom metrics can be added or removed using `add_metric` and `remove_metric` function.

{% code lineNumbers="true" %}

```python
# functional API
best = compare_models()

# OOP API
best = s.compare_models()
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FyB9dpGU7ZJNrSQdCXT2X%2Fimage.png?alt=media\&token=f0455c4c-282e-4bad-8ca7-a8f6855c3d7d)

### Analyze Model

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'forecast', data_kwargs = {'fh' : 24})

# OOP API
s.plot_model(best, plot = 'forecast', data_kwargs = {'fh' : 24})
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fidi4mCsq5BMdik12ztZl%2Fimage.png?alt=media\&token=0ecfb1c1-37ae-44a3-9587-3373e5629093)

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'diagnostics')

# OOP API
s.plot_model(best, plot = 'diagnostics')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FIUaAnqinawcIMzWmaLWf%2Fimage.png?alt=media\&token=16412565-1c7c-49fc-b689-5ea7de40ab34)

{% code lineNumbers="true" %}

```python
# functional API
plot_model(best, plot = 'insample')

# OOP API
s.plot_model(best, plot = 'insample')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FNeTCssJYbty65zO1SjP8%2Fimage.png?alt=media\&token=fe6d7f28-8d36-4c80-8137-863fd226f772)

### Predictions

{% code lineNumbers="true" %}

```python
# functional API
final_best = finalize_model(best)
predict_model(best, fh = 24)

# OOP API
final_best = s.finalize_model(best)
s.predict_model(best, fh = 24)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdXWSZsXgaATyDsptG2E2%2Fimage.png?alt=media&#x26;token=a4ff89f6-56e5-46ac-b3df-215607264a4f" alt=""><figcaption></figcaption></figure>

### Save the model

{% code lineNumbers="true" %}

```python
# functional API
save_model(final_best, 'my_final_best_model')

# OOP API
s.save_model(final_best, 'my_final_best_model')
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FILoJfxFlUCRojfL15Btm%2Fimage.png?alt=media\&token=73481456-10db-4235-8901-5d4e24589fdc)

#### To load the model back in the environment:

{% code lineNumbers="true" %}

```python
# functional API
loaded_model = load_model('my_final_best_model')
print(loaded_model)

# OOP API
loaded_model = s.load_model('my_final_best_model')
print(loaded_model)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1LvKBJv4w2YszHSDc9Kj%2Fimage.png?alt=media\&token=1718f72e-a678-49f9-a9de-69b5afa562dc)
