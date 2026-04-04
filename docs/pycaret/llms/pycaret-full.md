# Pycaret Documentation

Source: https://pycaret.gitbook.io/docs/llms-full.txt

---

# PyCaret 3.0

An open-source, low-code machine learning library in Python

PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. It is an end-to-end machine learning and model management tool that exponentially speeds up the experiment cycle and makes you more productive.

Compared with the other open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with a few lines only. This makes experiments exponentially fast and efficient. PyCaret is essentially a Python wrapper around several machine learning libraries and frameworks, such as scikit-learn, XGBoost, LightGBM, CatBoost, spaCy, Optuna, Hyperopt, Ray, and a few more.

The design and simplicity of PyCaret are inspired by the emerging role of citizen data scientists, a term first used by Gartner. Citizen Data Scientists are power users who can perform both simple and moderately sophisticated analytical tasks that would previously have required more technical expertise.

## Quick Links

| Learn PyCaret                                                              | Documentation                                                                  | Important Links                                                              |
| -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| ⭐[**Tutorials**](https://pycaret.gitbook.io/docs/get-started/tutorials)    | 📚 [**API Reference**](https://pycaret.readthedocs.io/en/latest/index.html)    | :cat: [**GitHub**](https://github.com/pycaret/pycaret/)                      |
| 📋 [**Examples**](https://nbviewer.org/github/pycaret/examples/tree/main/) | 🛠️ [**Release Notes**](https://github.com/pycaret/pycaret/releases)           | :link: [**LinkedIn**](https://www.linkedin.com/company/pycaret/)             |
| 📙 [**Blog**](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog) | 📢 [**Discussions**](https://github.com/pycaret/pycaret/discussions)           | :m: [**Meetup**](https://www.meetup.com/pycaret-user-group/)                 |
| 📺 [**Videos**](https://pycaret.gitbook.io/docs/learn-pycaret/videos)      | :outbox\_tray: [**GitHub Issues** ](https://github.com/pycaret/pycaret/issues) | :tv: [**YouTube**](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) |

## Features

PyCaret is an open-source, low-code machine learning library in Python that aims to reduce the hypothesis to insight cycle time in an ML experiment.  It enables data scientists to perform end-to-end experiments quickly and efficiently. In comparison with the other open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to perform complex machine learning tasks with only a few lines of code. PyCaret is simple and easy to use.&#x20;

### PyCaret for Citizen Data Scientists

The design and simplicity of PyCaret is inspired by the emerging role of citizen data scientists, a term first used by *Gartner*. Citizen Data Scientists are ‘power users’ who can perform both simple and moderately sophisticated analytical tasks that would previously have required more expertise. Seasoned data scientists are often difficult to find and expensive to hire but citizen data scientists can be an effective way to mitigate this gap and address data science challenges in the business setting.

### PyCaret deployment capabilities

PyCaret is a deployment ready library in Python which means all the steps performed in an ML experiment can be reproduced using a pipeline that is reproducible and guaranteed for production.  A pipeline can be saved in a binary file format that is transferable across environments.

### PyCaret is seamlessly integrated with BI

PyCaret and its Machine Learning capabilities are seamlessly integrated with environments supporting Python such as Microsoft Power BI, Tableau, Alteryx, and KNIME to name a few. This gives immense power to users of these BI platforms who can now integrate PyCaret into their existing workflows and add a layer of Machine Learning with ease.

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F39cmqXko47KE4ca9vUqh%2Fimage.png?alt=media\&token=597f36dd-235a-486c-88f1-a5c7f897c418)

#### PyCaret is ideal for:

* Experienced Data Scientists who want to increase productivity.
* Citizen Data Scientists who prefer a low code machine learning solution.
* Data Science Professionals who want to build rapid prototypes.
* Data Science and Machine Learning students and enthusiasts.

## PyCaret at a glance

### Classification

#### Functional API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdghtBxphPufGO3uOyHiU%2Fclassification_functional.png?alt=media&#x26;token=dbe9dfca-3c0e-45ca-b2b2-8a040115b9d4" alt=""><figcaption></figcaption></figure>

#### OOP API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUlyh83oeLnOyc6fhvjHA%2Fclassification_OOP.png?alt=media&#x26;token=cb581df7-ab2e-4fbf-b473-ce1080ed8c25" alt=""><figcaption></figcaption></figure>

### Regression

#### Functional API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FgTROKBMFONTsqypBKQcS%2Fregression_functional.png?alt=media&#x26;token=3e548aa2-eee5-46bf-ae22-7592d41588ca" alt=""><figcaption></figcaption></figure>

#### OOP API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7h8asJn6Yc6aZRilSxYS%2Fregression_OOP.png?alt=media&#x26;token=e1aee1a3-6329-4976-9206-d8ebf78aceb7" alt=""><figcaption></figcaption></figure>

### Time Series

#### Functional API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FTij7y5JkP2ZSUFUmY8dD%2Ftime_series_functional.png?alt=media&#x26;token=d39e0fdf-4bc1-4620-bf45-7949664c29bc" alt=""><figcaption></figcaption></figure>

#### OOP API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fdk1yQkqTgnLwObDWPJ9T%2Ftime_series_OOP.png?alt=media&#x26;token=0de8bdf7-a334-4b2a-88da-2780ebe53f3b" alt=""><figcaption></figcaption></figure>

### Clustering

#### Functional API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvEDQCt5tBO0mlQGmr6tE%2Fclustering_functional.png?alt=media&#x26;token=d6b5af69-392e-46f7-b03f-46c33b4598e0" alt=""><figcaption></figcaption></figure>

#### OOP API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhIWHp2Vy6MbJpLMXc6ez%2Fclustering_OOP.png?alt=media&#x26;token=de218477-dc13-446a-8e89-808e10b96078" alt=""><figcaption></figcaption></figure>

### Anomaly Detection

#### Functional API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FAQBEeiDcG4XyoJutIdYS%2Fanomaly_functional.png?alt=media&#x26;token=3c53b382-28f6-4128-a5ee-074c0c3e7b92" alt=""><figcaption></figcaption></figure>

#### OOP API

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FAgnYbu69MluRQ0nN2zkW%2Fanomaly_OOP.png?alt=media&#x26;token=21e8b1ce-db90-4626-80d6-1ac6c0b84830" alt=""><figcaption></figcaption></figure>

## Core Team

{% embed url="<https://github.com/moezali1>" %}
Moez Ali
{% endembed %}

{% embed url="<https://github.com/Yard1>" %}
Antoni Baum
{% endembed %}

{% embed url="<https://github.com/ngupta23>" %}
Nikhil Gupta
{% endembed %}

{% embed url="<https://github.com/tvdboom>" %}
Marco vd Boom
{% endembed %}

{% hint style="info" %}
**Contribute to PyCaret!** If you would like to contribute to this project, please see our [Contribution Guidelines](https://github.com/pycaret/pycaret/blob/master/CONTRIBUTING.md).
{% endhint %}

## Contributors

![](https://contributors-img.web.app/image?repo=pycaret/pycaret)

## Get Help

* The fastest way to get help is through [our Slack group](https://join.slack.com/t/pycaret/shared_invite/zt-row9phbm-BoJdEVPYnGf7_NxNBP307w).&#x20;
* You can also see our [Issue log](https://github.com/pycaret/pycaret/issues) or [Discussions](https://github.com/pycaret/pycaret/discussions) for answers to questions asked in the past by other members or raise a new question if it's not asked before.
* You can also look out for answers to common questions on [Stack Overflow](https://stackoverflow.com/questions/tagged/pycaret).
* We also have a pretty active [LinkedIn](https://www.linkedin.com/company/pycaret/) page.
* Check our [Frequently Asked Questions](https://pycaret.gitbook.io/docs/learn-pycaret/faqs) (FAQs) page.

## Citation

```
@Manual {PyCaret, 
    title = {PyCaret: An open source, low-code machine learning library in Python}, 
    author = {Moez Ali}, 
    year = {2020}, 
    month = {April}, 
    note = {PyCaret version 1.0}, 
    url = {https://www.pycaret.org
    }
```

## Support us

#### :star:Star **PyCaret** on GitHub  <a href="#star-fastapi-in-github" id="star-fastapi-in-github"></a>

Give us a star on our [GitHub repository](https://github.com/pycaret/pycaret) (click the star button on the top right corner)

#### :link: Follow us on LinkedIn

We have a pretty active [LinkedIn page](https://www.linkedin.com/company/36103360/admin/). Follow us for PyCaret updates and learning content.

#### :person\_tipping\_hand: Help others with issues on GitHub

You can see existing [open issues](https://github.com/pycaret/pycaret/issues) and [discussions](https://github.com/pycaret/pycaret/discussions) and help other members of the community by answering their questions.

#### :tv: Subscribe to our YouTube Channel

Subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) for learning content related to PyCaret.

#### :speaking\_head: Tweet about PyCaret

Help us spread the word. We love to hear success stories and use cases.

#### :writing\_hand: Blog on PyCaret

Like to write? You can write a medium blog and share it with us. Check out this [blog](https://moez-62905.medium.com/) by Author.

#### :m: Join our Meetup <a href="#blog-on-pycaret" id="blog-on-pycaret"></a>

Want to stay in touch and learn what's the latest and greatest in the community. Join our [Meetup](https://www.meetup.com/pycaret-user-group/).


# Installation

A step-by-step guide to install PyCaret in Python

## Option 1: Install via PyPi

PyCaret is tested and supported on 64-bit systems with:

* Python 3.8, 3.9, 3.10, and 3.11
* Ubuntu 16.04 or later
* Windows 7 or later

You can install PyCaret with Python's pip package manager:

{% code lineNumbers="true" %}

```bash
pip install pycaret
```

{% endcode %}

PyCaret's default installation will not install all the optional dependencies automatically. Depending on the use case, you may be interested in one or more extras:

```bash
# install analysis extras
pip install pycaret[analysis]

# models extras
pip install pycaret[models]

# install tuner extras
pip install pycaret[tuner]

# install mlops extras
pip install pycaret[mlops]

# install parallel extras
pip install pycaret[parallel]

# install test extras
pip install pycaret[test]

## 

# install multiple extras together
pip install pycaret[analysis,models]

```

Check out all [optional dependencies](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt). If you want to install everything including all the optional dependencies:

{% code lineNumbers="true" %}

```bash
# install full version
pip install pycaret[full]
```

{% endcode %}

## Option 2: Source

Install the development version of the library directly from the source. The API may be unstable. It is not recommended for production use.&#x20;

{% code lineNumbers="true" %}

```bash
pip install git+https://github.com/pycaret/pycaret.git@master --upgrade
```

{% endcode %}

## Option 3: Docker

Docker creates virtual environments with containers that keep a PyCaret installation separate from the rest of the system. PyCaret docker comes pre-installed with a Jupyter notebook. It can share resources with its host machine (access directories, use the GPU, connect to the Internet, etc.). The PyCaret Docker images are always tested for the latest major releases.

{% code lineNumbers="true" %}

```bash
# default version
docker run -p 8888:8888 pycaret/slim

# full version
docker run -p 8888:8888 pycaret/full
```

{% endcode %}

To learn more, check out the Docker page for [pycaret/slim](https://hub.docker.com/r/pycaret/slim) or [pycaret/full](https://hub.docker.com/r/pycaret/full).

## Environment

In order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment, e.g. python3 virtualenv (see [python3 virtualenv documentation](https://docs.python.org/3/tutorial/venv.html)) or [conda environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Using an isolated environment makes it possible to install a specific version of pycaret and its dependencies independently of any previously installed Python packages.&#x20;

{% code lineNumbers="true" %}

```bash
# create a conda environment
conda create --name yourenvname python=3.8

# activate conda environment
conda activate yourenvname

# install pycaret
pip install pycaret

# create notebook kernel
python -m ipykernel install --user --name yourenvname --display-name "display-name"
```

{% endcode %}

## Training on GPU

To train models on the GPU, simply pass `use_gpu = True` in the `setup` function. There is no change in the use of the API; however, in some cases, additional libraries have to be installed. The following models can be trained on GPUs:

* Extreme Gradient Boosting&#x20;
* Catboost
* Light Gradient Boosting Machine requires [GPU specific installation](https://lightgbm.readthedocs.io/en/latest/GPU-Tutorial.html)
* Logistic Regression, Ridge Classifier, Random Forest, K Neighbors Classifier, K Neighbors Regressor, Support Vector Machine, Linear Regression, Ridge Regression, Lasso Regression requires [cuML >= 0.15](https://github.com/rapidsai/cuml)

## PyCaret Intel sklearnex support

You can apply [Intel optimizations](https://github.com/intel/scikit-learn-intelex) for machine learning algorithms and speed up your workflows. To train models with Intel optimizations use `sklearnex` engine. There is no change in the use of the API, however, installation of Intel sklearnex is required:

{% code lineNumbers="true" %}

```bash
pip install scikit-learn-intelex
```

{% endcode %}


# Quickstart

Get Up and Running in No Time: A Beginner's Guide to PyCaret

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


# Tutorials

Tutorials developed and maintained by the core developers of PyCaret

### tutorials/

<table><thead><tr><th>Tutorial</th><th width="270.3333333333333">Module</th><th align="center">Link</th></tr></thead><tbody><tr><td>Binary Classification </td><td><code>pycaret.classification</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Binary%20Classification.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Binary%20Classification.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Binary%20Classification.ipynb">NBViewer</a></td></tr><tr><td>Multiclass Classification</td><td><code>pycaret.classification</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Multiclass%20Classification.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Multiclass%20Classification.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Multiclass%20Classification.ipynb">NBViewer</a></td></tr><tr><td>Regression</td><td><code>pycaret.regression</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Regression.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Regression.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Regression.ipynb">NBViewer</a></td></tr><tr><td>Time Series Forecasting</td><td><code>pycaret.time_series</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Time%20Series%20Forecasting.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Time%20Series%20Forecasting.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Time%20Series%20Forecasting.ipynb">NBViewer</a></td></tr><tr><td>Clustering</td><td><code>pycaret.clustering</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Clustering.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Clustering.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Clustering.ipynb">NBViewer</a></td></tr><tr><td>Anomaly Detection</td><td><code>pycaret.anomaly</code></td><td align="center"><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Anomaly%20Detection.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Anomaly%20Detection.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Anomaly%20Detection.ipynb">NBViewer</a></td></tr></tbody></table>

### tutorials/time\_series/forecasting

<table><thead><tr><th width="236.33333333333331">Tutorial</th><th width="272">Module</th><th>Link</th></tr></thead><tbody><tr><td>Univariate without exogeneous - Part 1</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part1.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part1.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part1.ipynb">NBViewer</a></td></tr><tr><td>Univariate without exogeneous - Part 2</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part2.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part2.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part2.ipynb">NBViewer</a></td></tr><tr><td>Univariate without exogeneous - Part 3</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part3.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part3.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_without_exogeneous_part3.ipynb">NBViewer</a></td></tr><tr><td>Univariate with exogeneous - Part I</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part1.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part1.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part1.ipynb">NBViewer</a></td></tr><tr><td>Univariate with exogeneous - Part 2</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part2.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part2.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part2.ipynb">NBViewer</a></td></tr><tr><td>Univariate with exogeneous - Part 3</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part3.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part3.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/univariate_with_exogeneous_part3.ipynb">NBViewer</a></td></tr><tr><td>Customizing experiments</td><td><code>pycaret.time_series</code></td><td><a href="https://colab.research.google.com/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/customizing_experiments.ipynb">Colab</a> | <a href="https://github.com/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/customizing_experiments.ipynb">GitHub</a> | <a href="https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/time_series/forecasting/customizing_experiments.ipynb">NBViewer</a></td></tr></tbody></table>

{% hint style="info" %}
For more examples, check out our [examples](https://github.com/pycaret/examples) repository.

Looking for video content? Check out this [section.](https://pycaret.gitbook.io/docs/learn-pycaret/videos)
{% endhint %}


# Modules

Machine Learning use-cases supported in PyCaret

{% tabs %}
{% tab title="Supervised ML" %}

### [Classification](https://pycaret.gitbook.io/docs/quickstart#classification)

In machine learning, classification refers to a predictive modeling problem where the target to be predicted is a *class label.*

* [Quickstart](https://pycaret.gitbook.io/docs/quickstart#classification)
* [API Docs](https://pycaret.readthedocs.io/en/latest/api/classification.html)
* [Tutorial](https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Binary%20Classification.ipynb)

### [Regression](https://pycaret.gitbook.io/docs/quickstart#regression)

In machine learning, regression refers to a predictive modeling problem where the target to be predicted is a *continuous variable*.

* [Quickstart](https://pycaret.gitbook.io/docs/quickstart#regression)
* [API Docs](https://pycaret.readthedocs.io/en/latest/api/regression.html)
* [Tutorial](https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Regression.ipynb)
  {% endtab %}

{% tab title="Unsupervised ML" %}

### [Clustering](https://pycaret.gitbook.io/docs/quickstart#clustering)

Clustering is the task of dividing the population or data points into a number of groups such that data points in the same groups are more similar to other data points in the same group than those in other groups.

* [Quickstart](https://pycaret.gitbook.io/docs/quickstart#clustering)
* [API Docs](https://pycaret.readthedocs.io/en/latest/api/clustering.html)
* [Tutorial](https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Clustering.ipynb)

### [Anomaly Detection](https://pycaret.gitbook.io/docs/quickstart#anomaly-detection)

Anomaly detection is identifying data points in data that don't fit the normal patterns. It can be useful to solve many problems including fraud detection, medical diagnosis, etc.

* [Quickstart](https://pycaret.gitbook.io/docs/quickstart#anomaly-detection)
* [API Docs](https://pycaret.readthedocs.io/en/latest/api/anomaly.html)
* [Tutorial](https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Anomaly%20Detection.ipynb)
  {% endtab %}

{% tab title="Time Series" %}

### [Time Series](https://pycaret.gitbook.io/docs/quickstart#time-series)

Time series forecasting is the process of analyzing time series data using statistics and modeling to make predictions and inform strategic decision-making

* [Quickstart](https://pycaret.gitbook.io/docs/quickstart#time-series)
* [API Docs](https://pycaret.readthedocs.io/en/latest/api/time_series.html)
* [Tutorial](https://nbviewer.org/github/pycaret/pycaret/blob/master/tutorials/Tutorial%20-%20Time%20Series%20Forecasting.ipynb)
  {% endtab %}

{% tab title="Datasets" %}

### [Datasets](https://pycaret.readthedocs.io/en/latest/api/datasets.html)

Module in PyCaret containing ML datasets. [Learn More](https://pycaret.readthedocs.io/en/latest/api/datasets.html).
{% endtab %}
{% endtabs %}


# Data Preprocessing

Data preprocessing and Transformations available in PyCaret

{% tabs %}
{% tab title="Data Preparation" %}

#### [Missing Values](https://pycaret.gitbook.io/docs/get-started/data-preparation#missing-values)

Datasets for various reasons may have missing values or empty records, often encoded as blanks or `NaN`. Most of the machine learning algorithms are not capable of dealing with the missing values.

#### [Data Types](https://pycaret.gitbook.io/docs/get-started/data-preparation#data-types)

Each feature in the dataset has an associated data type such as numeric, categorical, or Datetime. PyCaret automatically detects the data type of each feature.

#### [One-Hot Encoding](https://pycaret.gitbook.io/docs/get-started/data-preparation#one-hot-encoding)

Categorical features in the dataset contain the label values (ordinal or nominal) rather than continuous numbers. Most of the machine learning algorithms are not capable of handling categorical data without encoding.

#### [Ordinal Encoding](https://pycaret.gitbook.io/docs/get-started/data-preparation#ordinal-encoding)

When the categorical features in the dataset contain variables with intrinsic natural order such as *Low, Medium, and High*, these must be encoded differently than nominal variables (where there is no intrinsic order for e.g. Male or Female).

#### [Cardinal Encoding](https://pycaret.gitbook.io/docs/get-started/data-preparation#cardinal-encoding)

When categorical features in the dataset contain variables with many levels (also known as high cardinality features), then typical One-Hot Encoding leads to the creation of a very large number of new features.

#### [Target Imbalance](https://pycaret.gitbook.io/docs/get-started/data-preparation#target-imbalance)

When the training dataset has an unequal distribution of target class it can be fixed using the `fix_imbalance` parameter in the setup.

#### [Remove Outliers](https://pycaret.gitbook.io/docs/get-started/data-preparation#remove-outliers)

The `remove_outliers` function in PyCaret allows you to identify and remove outliers from the dataset before training the model.
{% endtab %}

{% tab title="Scale and Transform" %}

#### [Normalize](https://pycaret.gitbook.io/docs/get-started/scale-and-transform#normalize)

Normalization is a technique often applied as part of data preparation for machine learning. The goal of normalization is to rescale the values of numeric columns in the dataset without distorting the differences in the ranges of values.

#### [Feature Transform](https://pycaret.gitbook.io/docs/get-started/scale-and-transform#feature-transform)

While normalization rescales the data within new limits to reduce the impact of magnitude in the variance, Feature transformation is a more radical technique. Transformation changes the shape of the distribution.

#### [Target Transform](https://pycaret.gitbook.io/docs/get-started/scale-and-transform#target-transform)

Target Transformation is similar to feature transformation as it will change the shape of the distribution of the target variable instead of the features.
{% endtab %}

{% tab title="Feature Engineering" %}

#### [Feature Interaction](https://pycaret.gitbook.io/docs/get-started/feature-engineering#feature-interaction)

It is often seen in machine learning experiments when two features combined through an arithmetic operation become more significant in explaining variances in the data than the same two features separately.&#x20;

#### [Polynomial Features](https://pycaret.gitbook.io/docs/get-started/feature-engineering#polynomial-features)

In machine learning experiments the relationship between the dependent and independent variable is often assumed as linear, however, this is not always the case. Sometimes the relationship between dependent and independent variables is more complex.

#### [Group Features](https://pycaret.gitbook.io/docs/get-started/feature-engineering#group-features)

When a dataset contains features that are related to each other in some way, for example, features recorded at some fixed time intervals, then new statistical features such as mean, median, variance, and standard deviation for a group of such features.

#### [Bin Numeric Features](https://pycaret.gitbook.io/docs/get-started/feature-engineering#bin-numeric-features)

Feature binning is a method of turning continuous variables into categorical values using the pre-defined number of bins. It is effective when a continuous feature has too many unique values or few extreme values outside the expected range.

#### [Combine Rare Levels](https://pycaret.gitbook.io/docs/get-started/feature-engineering#combine-rare-levels)

Sometimes a dataset can have a categorical feature (or multiple categorical features) that has a very high number of levels (i.e. high cardinality features). If such feature (or features) are encoded into numeric values, then the resultant matrix is a sparse matrix.

#### [Create Clusters](https://pycaret.gitbook.io/docs/get-started/feature-engineering#create-clusters)

Creating Clusters using the existing features from the data is an unsupervised ML technique to engineer and create new features.
{% endtab %}

{% tab title="Feature Selection" %}

#### [Feature Selection](https://pycaret.gitbook.io/docs/get-started/feature-selection#feature-selection)

Feature Selection is a process used to select features in the dataset that contributes the most in predicting the target variable. Working with selected features instead of all the features reduces the risk of over-fitting, improves accuracy, and decreases the training time.&#x20;

#### [Remove Multicollinearity](https://pycaret.gitbook.io/docs/get-started/feature-selection#remove-multicollinearity)

Multicollinearity (also called *collinearity*) is a phenomenon in which one feature variable in the dataset is highly linearly correlated with another feature variable in the same dataset.&#x20;

#### [Principal Component Analysis](https://pycaret.gitbook.io/docs/get-started/feature-selection#principal-component-analysis)

Principal Component Analysis (PCA) is an unsupervised technique used in machine learning to reduce the dimensionality of the data. It does so by compressing the feature space.&#x20;

#### [Ignore Low Variance](https://pycaret.gitbook.io/docs/get-started/feature-selection#ignore-low-variance)

Sometimes a dataset may have a categorical feature with multiple levels, where the distribution of such levels is skewed and one level may dominate over other levels.&#x20;
{% endtab %}

{% tab title="Other setup parameters" %}

#### [Required Parameters](https://pycaret.gitbook.io/docs/get-started/other-setup-parameters#mandatory-parameters)

There are only two non-optional parameters in the setup function i.e. data and name of the target variable.

#### [Experiment Logging](https://pycaret.gitbook.io/docs/get-started/other-setup-parameters#experiment-logging)

PyCaret uses MLflow for experiment tracking. A parameter in the setup can be set to automatically track all the metrics, hyperparameters, and other model artifacts.&#x20;

#### [Model Selection](https://pycaret.gitbook.io/docs/get-started/other-setup-parameters#model-selection)

Parameters in the setup can be used for setting parameters for the model selection process. These are not related to data preprocessing but can influence your model selection process.&#x20;

#### [Other Miscellaneous](https://pycaret.gitbook.io/docs/get-started/other-setup-parameters#other-miscellaneous)&#x20;

Other miscellaneous parameters in the setup that are used for controlling experiment settings such as using GPU for training or setting verbosity of the experiment.&#x20;
{% endtab %}
{% endtabs %}


# Data Preparation

### **Missing Values**

Datasets for various reasons may have missing values or empty records, often encoded as blanks or `NaN`. Most machine learning algorithms can't deal with values that are missing or blank. Removing samples with missing values is a basic strategy that is sometimes used, but it comes with a cost of losing probable valuable data and the associated information or patterns. A better strategy is to impute the missing values.&#x20;

#### **PARAMETERS**

* **imputation\_type: string, default = 'simple'**\
  The type of imputation to use. It can be either `simple` or `iterative`. If None, no imputation of missing values is performed.
* **numeric\_imputation: int, float, or string, default = ‘mean’**\
  Imputing strategy for numerical columns. Ignored when `imputation_type= iterative`. Choose from:
  * **drop:** Drop rows containing missing values.&#x20;
  * **mean:** Impute with mean of column.&#x20;
  * **median:** Impute with median of column.
  * **mode:** Impute with most frequent value.
  * **knn:** Impute using a K-Nearest Neighbors approach.&#x20;
  * **int or float:** Impute with provided numerical value.
* **categorical\_imputation: string, default = ‘mode’**\
  Imputing strategy for categorical columns. Ignored when `imputation_type= iterative`. Choose from:&#x20;
  * **drop:** Drop rows containing missing values.
  * **mode:** Impute with most frequent value.
  * **str:** Impute with provided string.
* **iterative\_imputation\_iters: int, default = 5**\
  The number of iterations. Ignored when `imputation_type=simple`.
* **numeric\_iterative\_imputer: str or sklearn estimator, default = 'lightgbm'**\
  Regressor for iterative imputation of missing values in numeric features. If None, it uses LGBClassifier. Ignored when `imputation_type=simple`.'
* **categorical\_iterative\_imputer: str or sklearn estimator, default = 'lightgbm'**\
  Regressor for iterative imputation of missing values in categorical features. If None, it uses LGBClassifier. Ignored when `imputation_type=simple`.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
hepatitis = get_data('hepatitis')

# init setup
from pycaret.classification import *
clf1 = setup(data = hepatitis, target = 'Class')
```

{% endcode %}

#### Before

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FRdqK8uEeZoyRocQAPFiJ%2Fimage.png?alt=media\&token=0e3535dc-4e7e-4484-8439-3f9fce062ada)

#### **After**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fq7BxM7qhvq1QUFzzHYKq%2Fimage.png?alt=media\&token=9b306823-05ef-4594-9073-d505bf5d1343)

#### Comparison of Simple imputer vs. Iterative imputer

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FcSVCjvGS7LFY5cO11fku%2Fimage.png?alt=media\&token=87468faf-b539-47af-a431-ec6a86b82051)

To learn more about this experiment, you read [this article](https://www.linkedin.com/pulse/iterative-imputation-pycaret-22-antoni-baum/).&#x20;

### Data Types

Each feature in the dataset has an associated data type such as numeric, categorical, or Datetime. PyCaret’s inference algorithm automatically detects the data type of each feature. However, sometimes the data types inferred by PyCaret are incorrect. Ensuring data types are correct is important as several downstream processes depend on the data type of the features. One example could be that [Missing Values](#missing-values) for numeric and categorical features in the dataset are imputed differently. To overwrite the inferred data types, `numeric_features`, `categorical_features` and `date_features` parameters can be used in the setup function. You can also use `ignore_features` to ignore certain features for model training.

**PARAMETERS**

* **numeric\_features: list of string, default = None**\
  If the inferred data types are not correct, `numeric_features` can be used to overwrite the inferred data types.&#x20;
* **categorical\_features: list of string, default = None**\
  If the inferred data types are not correct, `categorical_features` can be used to overwrite the inferred data types.&#x20;
* **date\_features: list of string, default = None**\
  If the data has a `Datetime` column that is not automatically inferred when running the setup, `date_features` can be used to force the data type. It can work with multiple date columns. Datetime related features are not used in modeling. Instead, feature extraction is performed and original `Datetime` columns are ignored during model training. If the `Datetime` column includes a timestamp, features related to time will also be extracted.
* **create\_date\_columns: list of str, default = \["day", "month", "year"]**

  Columns to create from the date features. Note that created features with zero variance (e.g. the feature hour in a column that only contains dates) are ignored. Allowed values are datetime attributes from `pandas.Series.dt`. The datetime format of the feature is inferred automatically from the first non NaN value.
* **text\_features: list of str, default = None**\
  Column names that contain a text corpus. If None, no text features are selected.
* **text\_features\_method: str, default = 'tf-idf'**\
  Method with which to embed the text features in the dataset. Choose between 'bow' (Bag of Words - `CountVectorizer`) or 'tf-idf' (`TfidfVectorizer`). Be aware that the sparse matrix output of the transformer is converted internally to its full array. This can cause memory issues for large text embeddings.
* **ignore\_features: list of string, default = None**\
  `ignore_features` can be used to ignore features during model training. It takes a list of strings with column names that are to be ignored.
* **keep\_features: list of str, default = None**

  `keep_features` parameter can be used to always keep specific features during preprocessing, i.e. these features are never dropped by any kind of feature selection. It takes a list of strings with column names that are to be kept.

#### **Example 1 - Categorical Features**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
hepatitis = get_data('hepatitis')

# init setup
from pycaret.classification import *
clf1 = setup(data = hepatitis, target = 'Class', categorical_features = ['AGE'])
```

{% endcode %}

#### **Before**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FNnH2pHFZtpUU1xZJz5Iy%2Fimage.png?alt=media\&token=202c3695-640e-4844-9b0e-ab02e82be08c)

#### **After**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FotAWAZwXg1ySsGukRGJB%2Fimage.png?alt=media\&token=0ce751bd-153e-43b6-afe5-2b2bf3afd0c0)

#### Example 2 - Ignore Features

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
pokemon = get_data('pokemon')

# init setup
from pycaret.classification import *
clf1 = setup(data = pokemon, target = 'Legendary', ignore_features = ['#', 'Name'])
```

{% endcode %}

#### Before

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FkAHkCYyXrzUZn4Zg55MC%2Fimage.png?alt=media\&token=56157823-faa9-450c-92a4-03cf3e9acdf6)

#### After

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FNnQg1DWiCQeibwOIxofe%2Fimage.png?alt=media\&token=9cdbbe68-65c4-4981-b969-3a014a6447a6)

### One-Hot Encoding

Categorical features in the dataset contain the label values (ordinal or nominal) rather than continuous numbers. The majority of the machine learning algorithms cannot directly deal with categorical features and they must be transformed into numeric values before training a model. The most common type of categorical encoding is One-Hot Encoding (also known as *dummy encoding*) where each categorical level becomes a separate feature in the dataset containing binary values (1 or 0).&#x20;

Since this is an imperative step to perform an ML experiment, PyCaret will transform all categorical features in the dataset using one-hot encoding. This is ideal for features having nominal categorical data i.e. data cannot be ordered. In other different scenarios, other methods of encoding must be used. For example, when the data is ordinal i.e. data has intrinsic levels, [Ordinal Encoding](#ordinal-encoding) must be used. One-Hot Encoding works on all features that are either inferred as categorical or are forced as categorical using `categorical_features` in the setup function.&#x20;

**PARAMETERS**

* **max\_encoding\_ohe: int, default = 25** \
  Categorical columns with `max_encoding_ohe` or less unique values are encoded using OneHotEncoding. If more, the `encoding method` estimator is used. Note that columns with exactly two classes are always encoded ordinally. Set to below 0 to always use OneHotEncoding.

  **encoding\_method: category-encoders estimator, default = None** \
  A `category-encoders` estimator to encode the categorical columns with more than `max_encoding_ohe` unique values. If None, `category_encoders.leave_one_out.LeaveOneOutEncoder` is used by default.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
pokemon = get_data('pokemon')

# init setup
from pycaret.classification import *
clf1 = setup(data = pokemon, target = 'Legendary')
```

{% endcode %}

#### **Before**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fh5Ee5n1zjDDn0RqvZ747%2Fimage.png?alt=media\&token=e1ce5e63-8553-46fe-a7ea-e9e87e9106c4)

#### **After**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F3yDqkCouIqXMyuzQThrO%2Fimage.png?alt=media\&token=7cf413ac-63c2-418f-beee-a0f07c47821c)

### Ordinal Encoding

When the categorical features in the dataset contain variables with intrinsic natural order such as *Low, Medium, and High*, these must be encoded differently than nominal variables (where there is no intrinsic order for e.g. Male or Female). This can be achieved using  the `ordinal_features` parameter in the setup function that accepts a dictionary with feature names and the levels in the increasing order from lowest to highest.

#### **PARAMETERS**

* **ordinal\_features: dictionary, default = None**\
  When the data contains ordinal features, they must be encoded differently using the `ordinal_features`. If the data has a categorical variable with values of `low`, `medium`, `high` and it is known that low < medium < high, then it can be passed as `ordinal_features = { 'column_name' : ['low', 'medium', 'high'] }`. The list sequence must be in increasing order from lowest to highest.

#### **Example**

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
employee = get_data('employee')

# init setup
from pycaret.classification import *
clf1 = setup(data = employee, target = 'left', ordinal_features = {'salary' : ['low', 'medium', 'high']})
```

{% endcode %}

#### **Before**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FPBjaB9WezopbGQSvEnVK%2Fimage.png?alt=media\&token=7a9f9df4-0251-40f0-b5c2-4bc5b5dd3643)

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fe9YfwxENJHVHNGvtmU1g%2Fimage.png?alt=media\&token=6505c562-1090-42ef-81e0-e680fd833484)

### Target Imbalance

When the training dataset has an unequal distribution of target class it can be fixed using the `fix_imbalance` parameter in the setup. When set to `True`, SMOTE (Synthetic Minority Over-sampling Technique) is used as a default method for resampling. The method for resampling can be changed using the `fix_imbalance_method` within the setup.&#x20;

#### **PARAMETERS**

* **fix\_imbalance: bool, default = False**\
  When set to `True`, the training dataset is resampled using the algorithm defined in `fix_imbalance_method` . When `None`, SMOTE is used by default.
* **fix\_imbalance\_method: str or imblearn estimator, default = 'SMOTE'**\
  Estimator with which to perform class balancing. Choose from the name of an `imblearn` estimator, or a custom instance of such. Ignored when`fix_imbalance=False`.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
credit = get_data('credit')

# init setup
from pycaret.classification import *
clf1 = setup(data = credit, target = 'default', fix_imbalance = True)
```

{% endcode %}

#### Before and After SMOTE

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FD1MUP5z6VVgfAhuwXtUs%2Fimage.png?alt=media&#x26;token=9be7b95b-586f-4d5a-92c0-8b596d9b9cb7" alt=""><figcaption></figcaption></figure>

### Remove Outliers

The `remove_outliers` function in PyCaret allows you to identify and remove outliers from the dataset before training the model. Outliers are identified through PCA linear dimensionality reduction using the Singular Value Decomposition technique. It can be achieved using `remove_outliers` parameter within [setup](https://www.pycaret.org/setup). The proportion of outliers are controlled through `outliers_threshold` parameter.

#### **PARAMETERS**

* **remove\_outliers: bool, default = False**\
  When set to True, outliers from the training data are removed using an Isolation Forest.
* **outliers\_method: str, default = 'iforest'**\
  Method with which to remove outliers. Ignored when `remove_outliers=False`. Possible values are:
  * **'iforest':** Uses sklearn's IsolationForest.
  * **'ee'**: Uses sklearn's EllipticEnvelope.
  * **'lof':** Uses sklearn's LocalOutlierFactor.
* **outliers\_threshold: float, default = 0.05**\
  The percentage of outliers to be removed from the dataset. Ignored when `remove_outliers=False`.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
insurance = get_data('insurance')

# init setup
from pycaret.regression import *
reg1 = setup(data = insurance, target = 'charges', remove_outliers = True)
```

{% endcode %}

<div align="left"><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FqZQvNP30flhWuWc31nr1%2Fimage.png?alt=media&#x26;token=ac1d5eb7-26a5-487b-ae82-9174e41f3ea4" alt=""></div>

#### Before and After removing outliers

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FMYhLAE9aXNEqKFRVW8MA%2Fimage.png?alt=media\&token=d0bbebe8-7a03-49d7-92d4-e9d5edfc8921)


# Scale and Transform

### Normalize

Normalization is a technique often applied as part of data preparation for machine learning. The goal of normalization is to rescale the values of numeric columns in the dataset without distorting differences in the ranges of values or losing information. There are several methods available for normalization, by default, PyCaret uses `zscore`.

#### **PARAMETERS**

* **normalize: bool, default = False**\
  When set to `True`, the feature space is transformed using the method defined under the `normalized_method` parameter.&#x20;
* **normalize\_method: string, default = ‘zscore’**\
  Defines the method to be used for normalization. By default, the method is set to `zscore`. The other available options are:
  * **`z-score`** The standard zscore is calculated as z = (x – u) / s
  * **`minmax`** scales and translates each feature individually such that it is in the range of 0 – 1.
  * **`maxabs`** scales and translates each feature individually such that the maximal absolute value of each feature will be 1.0. It does not shift/center the data and thus does not destroy any sparsity.
  * **`robust`** scales and translates each feature according to the Interquartile range. When the dataset contains outliers, the robust scaler often gives better results.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
pokemon = get_data('pokemon')

# init setup
from pycaret.classification import *
clf1 = setup(data = pokemon, target = 'Legendary', normalize = True)
```

{% endcode %}

#### **Before**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FATe0PAG2cZwI5GtRsB1C%2Fimage.png?alt=media\&token=49c1f228-498b-4c76-8abd-eb1bae3ef7b8)

#### **After**

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Faeu8nCgR7sSwi6ddQ37I%2Fimage.png?alt=media\&token=4851e759-4b5c-45b2-9a8b-224f915437af)

#### Effect of Normalization:

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fd7gbKsHNY8so3JihYObo%2Fimage.png?alt=media\&token=5c0195f8-c5fb-4082-b3d7-cf8801d070fc)

### Feature Transform

While [normalization](#normalize) rescales the data within new limits to reduce the impact of magnitude in the variance, Feature transformation is a more radical technique. Transformation changes the shape of the distribution such that the transformed data can be represented by a normal or approximate normal distribution. There are two methods available for transformation `yeo-johnson` and `quantile`.

#### **PARAMETERS**

* **transformation: bool, default = False**\
  When set to `True`, a power transformer is applied to make the data more normal / Gaussian-like. This is useful for modeling issues related to heteroscedasticity or other situations where normality is desired. The optimal parameter for stabilizing variance and minimizing skewness is estimated through maximum likelihood.
* **transformation\_method: string, default = ‘yeo-johnson’**\
  Defines the method for transformation. By default, the transformation method is set to `yeo-johnson`. The other available option is `quantile` transformation. Both the transformation transforms the feature set to follow a Gaussian-like or normal distribution. Quantile transformer is non-linear and may distort linear correlations between variables measured at the same scale.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
pokemon = get_data('pokemon')

# init setup
from pycaret.classification import *
clf1 = setup(data = pokemon, target = 'Legendary', transformation = True)
```

{% endcode %}

#### **Before**

![Dataframe view before transformation](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FLYYqT9aIoiJ8h8LirfBa%2Fimage.png?alt=media\&token=31961351-bac8-4482-a7a1-aef08ed1ce5b)

#### **After**

![Dataframe view after transformation](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fn9y7gVvK1eqfKoxLabHK%2Fimage.png?alt=media\&token=74fb71b3-89b4-498f-8b50-4a4a0cddd0ab)

#### Effect of Feature Transformation:

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FbE22Za2TMcEBenMevY5d%2Fimage.png?alt=media\&token=f87dd7ac-77e9-48e0-ae56-a4ef7a78558b)

### Target Transform

Target Transformation is similar to Feature Transformation as it will change the shape of the distribution of the target variable instead of Features. This feature is only available in `pycaret.regression` module.

#### **PARAMETERS**

* **transform\_target: bool, default = False**\
  When set to True, target variable is transformed using the method defined in `transform_target_method` parameter. Target transformation is applied separately from feature transformations.
* **transform\_target\_method: string, default = ‘yeo-johnson’**\
  Defines the method for transformation. By default, the transformation method is set to `yeo-johnson`. The other available option for transformation is `quantile`. Ignored when `transform_target = False`.

#### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diamond = get_data('diamond')

# init setup
from pycaret.regression import *
reg1 = setup(data = diamond, target = 'Price', transform_target = True)
```

{% endcode %}

#### Before

![Dataframe view before target transformation](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJhBkkpAWlJUeCyqeMMIp%2Fimage.png?alt=media\&token=af46375f-3d63-4fa2-ab3c-45ee0867fb01)

#### After

![Dataframe view after target transformationn](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F9Z2DQ5qpyzsaf5bA5BPc%2Fimage.png?alt=media\&token=fef90f0c-01d0-4a6b-9dd8-fd582a719fd0)


# Feature Engineering

### Polynomial Features

In machine learning experiments, the relationship between the dependent and independent variables is often assumed to be linear; however, this is not always the case. Sometimes the relationship between dependent and independent variables is more complex. Creating new polynomial features sometimes might help in capturing that relationship, which otherwise may go unnoticed.&#x20;

#### **PARAMETERS**

* **polynomial\_features: bool, default = False**\
  When set to True, new features are created based on all polynomial combinations that exist within the numeric features in a dataset to the degree defined in the `polynomial_degree` parameter.
* **polynomial\_degree: int, default = 2**\
  Degree of polynomial features. For example, if an input sample is two dimensional and of the form \[a, b], the polynomial features with degree = 2 are: \[1, a, b, a^2, ab, b^2].

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
clf1 = setup(data = juice, target = 'Purchase', polynomial_features = True)
```

{% endcode %}

#### **Before**

![Dataframe view before polynomial features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fv07fr9Dt4gowTkwQEdvb%2Fimage.png?alt=media\&token=05d65758-fb69-4842-8d0b-e1d79de150fe)

#### **After**

![Dataframe view after polynomial features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1pCuNIE7Y8cewWmXLXrP%2Fimage.png?alt=media\&token=b4b0d844-32c2-4cdb-be57-382dd2530e1a)

### Group Features

When dataset contains features that are related to each other in someway, for example: features recorded at some fixed time intervals, then new statistical features such as **mean, median, variance and standard deviation** for a group of such features can be created from existing features using `group_features` parameter.

#### **PARAMETERS**

* **group\_features: list or list of list, default = None**\
  When a dataset contains features that have related characteristics, the group\_features param can be used for statistical feature extraction. For example, if a dataset has numeric features that are related with each other (i.e ‘Col1’, ‘Col2’, ‘Col3’), a list containing the column names can be passed under `group_features` to extract statistical information such as the mean, median, mode and standard deviation.
* **group\_names: list, default = None**\
  When group\_features is passed, a name of the group can be passed into the `group_names` parameter as a list containing strings. The length of a `group_names` list must equal to the length of `group_features`. When the length doesn’t match or the name is not passed, new features are sequentially named such as group\_1, group\_2 etc.

#### **Example**

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
credit = get_data('credit')

# init setup
from pycaret.classification import *
clf1 = setup(data = credit, target = 'default', group_features = ['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'])
```

{% endcode %}

#### **Before**

![Dataframe before group features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FBMnbqQfvTfFEK9U7zTz2%2Fimage.png?alt=media\&token=9d34fad8-c104-471d-aead-8512dec4fbf7)

#### **After**

![Dataframe after group features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F6KsFA6sUdhmhX2u9DRfy%2Fimage.png?alt=media\&token=84d825ce-afc7-44f1-b292-e935c892cee5)

### Bin Numeric Features

Feature binning is a method of turning continuous variables into categorical values using pre-defined number of bins. It is effective when a continuous feature has too many unique values or few extreme values outside the expected range. Such extreme values influence on the trained model, thereby affecting the prediction accuracy of the model. In PyCaret, continuous numeric features can be binned into intervals using `bin_numeric_features` parameter[. ](https://www.pycaret.org/setup)PyCaret uses the ‘sturges’ rule to determine the number of bins and uses K-Means clustering to convert continuous numeric features into categorical features.

#### **PARAMETERS**

* **bin\_numeric\_features: list, default = None**\
  When a list of numeric features is passed they are transformed into categorical features using K-Means, where values in each bin have the same nearest center of a 1D k-means cluster. The number of clusters are determined based on the 'sturges' method. It is only optimal for gaussian data and underestimates the number of bins for large non-gaussian datasets.

#### **Example**

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
income = get_data('income')

# init setup
from pycaret.classification import *
clf1 = setup(data = income, target = 'income >50K', bin_numeric_features = ['age'])
```

{% endcode %}

#### Before

![Dataframe view before bin numeric bin features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FPw8dPqCyNmvq0YXzs6jG%2Fimage.png?alt=media\&token=e64a1b3d-5e30-4340-b140-1ab395719de9)

#### After

![Dataframe view after numeric bin features](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FB0NlRZtxyUs77Nh68jOa%2Fimage.png?alt=media\&token=e59256c4-536e-4c66-9eb3-1cf26731700d)

### Combine Rare Levels

Sometimes a dataset can have a categorical feature (or multiple categorical features) that has a very high number of levels (i.e. high cardinality features). If such feature (or features) are encoded into numeric values, then the resultant matrix is a sparse matri&#x78;**.** This not only makes experiment slow due to manifold increment in the number of features and hence the size of the dataset, but also introduces noise in the experiment. Sparse matrix can be avoided by combining the rare levels in the feature(or features) having high cardinality. This can be achieved in PyCaret using `rare_to_value` parameter.

#### **PARAMETERS**

* **rare\_to\_value: float or None, default=None**

  Minimum fraction of category occurrences in a categorical column. If a category is less frequent than `rare_to_value * len(X)`, it is replaced with the string in `rare_value`. Use this parameter to group rare categories before encoding the column. If None, ignores this step.
* **rare\_value: str, default="rare"**

  Value with which to replace rare categories. Ignored when `rare_to_value` is None

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
income = get_data('income')

# init setup
from pycaret.classification import *
clf1 = setup(data = income, target = 'income >50K', rare_to_value = 0.1)
```

{% endcode %}

#### **Before**

![Dataframe view before combine rare levels](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FgsZpMakO3JN3xz0M8FON%2Fimage.png?alt=media\&token=a9e69b56-21f5-457a-816f-f2830f877deb)

#### After

![Dataframe view after combine rare levels](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FG5OsUuJgRJuIqvkc8fcp%2Fimage.png?alt=media\&token=3db75dc6-486a-46f7-9e89-e544c3c1809e)

#### Effect of combining rare levels

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5ZH4BrKrtie51rgFlMRf%2Fimage.png?alt=media\&token=6429b8c6-8db4-4093-b6aa-be75594b9c78)


# Feature Selection

### Feature Selection

**Feature Importance** is a process used to select features in the dataset that contribute the most in predicting the target variable. Working with selected features instead of all the features reduces the risk of over-fitting, improves accuracy, and decreases the training time. In PyCaret, this can be achieved using `feature_selection` parameter.&#x20;

#### **PARAMETERS**

* **feature\_selection: bool, default = False**\
  When set to True, a subset of features is selected based on a feature importance score determined by `feature_selection_estimator`.
* **feature\_selection\_method: str, default = 'classic'**

  Algorithm for feature selection. Choose from:

  * **'univariate':** Uses sklearn's SelectKBest.
  * **'classic':** Uses sklearn's SelectFromModel.
  * **'sequential':** Uses sklearn's SequentialFeatureSelector.
* **feature\_selection\_estimator: str or sklearn estimator, default = 'lightgbm'**

  Classifier used to determine the feature importance. The estimator should have a `feature_importances_` or `coef_` attribute after fitting. If None, it uses LGBClassifier. This parameter is ignored when feature\_selection\_method=univariate.
* **n\_features\_to\_select: int or float, default = 0.2**

  The maximum number of features to select with feature\_selection. If <1, it's the fraction of starting features. Note that this parameter doesn't take features in `ignore_features` or `keep_features` into account when counting.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.regression import *
clf1 = setup(data = diabetes, target = 'Class variable', feature_selection = True)
```

{% endcode %}

#### **Before**

![Dataframe before feature importance](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F6skExeLBkKBvE2SDS9qf%2Fimage.png?alt=media\&token=9fa7e459-1f06-4893-97a1-d5a2e58395ab)

#### **After**

![Dataframe after feature importance](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fy1ZemHdASW3KT5Wb8arR%2Fimage.png?alt=media\&token=853f3452-7978-472a-b0c6-e905bf157438)

### Remove Multicollinearity

**Multicollinearity** (also called *collinearity*) is a phenomenon in which one feature variable in the dataset is highly linearly correlated with another feature variable in the same dataset. Multicollinearity increases the variance of the coefficients, thus making them unstable and noisy for linear models. One such way to deal with Multicollinearity is to drop one of the two features that are highly correlated with each other. This can be achieved in PyCaret using `remove_multicollinearity` parameter.

#### PARAMETERS

* **remove\_multicollinearity: bool, default = False**\
  When set to True, features with the inter-correlations higher than the defined threshold are removed. For each group, it removes all except the feature with the highest correlation to `y`.
* **multicollinearity\_threshold: float, default = 0.9**\
  Minimum absolute Pearson correlation to identify correlated features. The default value removes equal columns. Ignored when `remove_multicollinearity` is not True.

#### **Example**

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
concrete = get_data('concrete')

# init setup
from pycaret.regression import *
reg1 = setup(data = concrete, target = 'strength', remove_multicollinearity = True, multicollinearity_threshold = 0.3)
```

{% endcode %}

#### **Before**

![Dataframe view before remove multicollinearity](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F2CknoyAxHsw2szbDXimb%2Fimage.png?alt=media\&token=df7a21d6-fff6-4d1c-a252-30c4955c9fbe)

#### **After**

![Dataframe view after remove multicollinearity](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FQGAJScPospfTBZLUsYAh%2Fimage.png?alt=media\&token=d8da725c-2736-40d5-bbb8-5d93dc19b5ab)

### Principal Component Analysis

Principal Component Analysis (PCA) is an unsupervised technique used in machine learning to reduce the dimensionality of a data. It does so by compressing the feature space by identifying a subspace that captures most of the information in the complete feature matrix. It projects the original feature space into lower dimensionality.&#x20;

**PARAMETERS**

* **pca: bool, default = False**\
  When set to True, dimensionality reduction is applied to project the data into a lower dimensional space using the method defined in `pca_method` parameter.
* **pca\_method: string, default = ‘linear’**\
  Method with which to apply PCA. Possible values are:
  * **'linear':** Uses Singular Value Decomposition.
  * **'kernel':** Dimensionality reduction through the use of RBF kernel.
  * **'incremental':** Similar to 'linear', but more efficient for large datasets.
* **pca\_components: int/float, default = 0.99**\
  Number of components to keep. if pca\_components is a float, it is treated as a target percentage for information retention. When pca\_components is an integer it is treated as the number of features to be kept. pca\_components must be strictly less than the original number of features in the dataset.
* **pca\_components: int, float, str or None, default = None** \
  Number of components to keep. This parameter is ignored when `pca=False`.&#x20;
  * **If None:** All components are kept.&#x20;
  * **If int:** Absolute number of components. -&#x20;
  * **If float:** Such an amount that the variance that needs to be explained is greater than the percentage specified by `n_components`. Value should lie between 0 and 1 (ony for pca\_method='linear').&#x20;
  * **If 'mle':** Minka’s MLE is used to guess the dimension (ony for pca\_method='linear').

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
income = get_data('income')

# init setup
from pycaret.classification import *
clf1 = setup(data = income, target = 'income >50K', pca = True, pca_components = 10)
```

{% endcode %}

#### **Before**

![Dataframe view before pca](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FldUXuuNVgWW9rZl2deXf%2Fimage.png?alt=media\&token=6616ee4b-556c-4414-aac0-f218d58338d6)

#### **After**

![Dataframe view after pca](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FzaNDip9O0uTK7HSPvrfP%2Fimage.png?alt=media\&token=5e132681-d3b6-40bc-a3e9-1e5dc33a3419)

### Ignore Low Variance

Sometimes a dataset may have a **categorical feature** with multiple levels, where distribution of such levels are skewed and one level may dominate over other levels. This means there is not much variation in the information provided by such feature.  For a ML model, such feature may not add a lot of information and thus can be ignored for modeling. This can be achieved in PyCaret using `low_variance_threshold` parameter.

#### **PARAMETERS**

* **low\_variance\_threshold: float or None, default = None**

  Remove features with a training-set variance lower than the provided threshold. If 0, keep all features with non-zero variance, i.e. remove the features that have the same value in all samples. If None, skip this transformation step.

#### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
mice = get_data('mice')

# filter dataset
mice = mice[mice['Genotype'] == 'Control']

# init setup
from pycaret.classification import *
clf1 = setup(data = mice, target = 'class', low_variance_threshold = 0.1)
```

{% endcode %}

#### **Before**

![Dataframe view before ignore low variance](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F0I9ZSGdU127KfpRTc26i%2Fimage.png?alt=media\&token=f9bfa0ca-26cf-4df1-bad9-b76157a51705)

#### **After**

![Dataframe view after ignore low variance](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FePQe428JFCvre65Qpirw%2Fimage.png?alt=media\&token=4614cd5c-b81c-48fd-9ef7-5c459eba4fd2)


# Other setup parameters

All other setup related parameters

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


# Functions

All functions in PyCaret

{% tabs %}
{% tab title="Initialize" %}

#### [setup](https://pycaret.gitbook.io/docs/get-started/initialize#setting-up-environment)

This function initializes the experiment in PyCaret and prepares the transformation pipeline based on all the parameters passed in the function. The setup function must be called before executing any other function. It only requires two parameters: `data` and `target`. All the other parameters are optional.
{% endtab %}

{% tab title="Train" %}

#### [compare\_models](https://pycaret.gitbook.io/docs/get-started/train#compare_models)

This function trains and evaluates the performance of all the models available in the model library using cross-validation. The output of this function is a scoring grid with average cross-validated scores.

#### [create\_model](https://pycaret.gitbook.io/docs/get-started/train#create_model)&#x20;

This function trains and evaluates the performance of a given model using cross-validation. The output of this function is a scoring grid with cross-validated scores along with mean and standard deviation.
{% endtab %}

{% tab title="Optimize" %}

#### [tune\_model](https://pycaret.gitbook.io/docs/get-started/optimize#tune_model)

This function tunes the hyperparameters of a given model. The output of this function is a scoring grid with cross-validated scores of the best model. Search spaces are pre-defined with the flexibility to provide your own. The search algorithm can be random, bayesian, and a few others with the ability to scale on large clusters.

#### [ensemble\_model](https://pycaret.gitbook.io/docs/get-started/optimize#ensemble_model)

This function ensembles a given model. The output of this function is a scoring grid with cross-validated scores of the ensembled model. Two methods `Bagging` or `Boosting` can be used for ensembling.

#### [blend\_models](https://pycaret.gitbook.io/docs/get-started/optimize#blend_models)

This function trains a Soft Voting / Majority Rule classifier for given models in a list. The output of this function is a scoring grid with cross-validated scores of a Voting Classifier or Regressor.

#### [stack\_models](https://pycaret.gitbook.io/docs/get-started/optimize#stack_models)

This function trains a meta-model over given models in a list. The output of this function is a scoring grid with cross-validated scores of a Stacking Classifier or Regressor.

#### [optimize\_threshold](https://pycaret.gitbook.io/docs/get-started/optimize#optimize_threshold)

This function optimizes the probability threshold for a given model. It iterates over performance metrics at different probability thresholds and returns a plot with performance metrics on the y-axis and threshold on the x-axis.

#### [calibrate\_model](https://pycaret.gitbook.io/docs/get-started/optimize#calibrate_model)

This function calibrates the probability of a given model using isotonic or logistic regression. The output of this function is a scoring grid with cross-validated scores of calibrated classifier.
{% endtab %}

{% tab title="Analyze" %}

#### [plot\_model](https://pycaret.gitbook.io/docs/get-started/analyze#plot_model)

This function analyzes the performance of a trained model on the hold-out set. It may require re-training the model in certain cases.

#### [evaluate\_model](https://pycaret.gitbook.io/docs/get-started/analyze#evaluate_model)

This function uses `ipywidgets` to display a basic user interface for analyzing the performance of a trained model.

#### [interpret\_model](https://pycaret.gitbook.io/docs/get-started/analyze#interpret_model)

This function analyzes the predictions generated from a trained model. Most plots in this function are implemented based on the SHAP (Shapley Additive exPlanations).

#### [dashboard](https://pycaret.gitbook.io/docs/get-started/analyze#dashboard)

This function generates the interactive dashboard for a trained model. The dashboard is implemented using the ExplainerDashboard project.

#### [check\_fairness](https://pycaret.gitbook.io/docs/get-started/analyze#check_fairness)

This function provides fairness-related metrics between different groups in the dataset for a given model. There are many approaches to evaluate fairness but this function uses the approach known as group fairness, which asks: which groups of individuals are at risk for experiencing harm.

#### [get\_leaderboard](https://pycaret.gitbook.io/docs/get-started/analyze#get_leaderboard)

This function returns the leaderboard of all models trained in the current setup.

#### [assign\_model](https://pycaret.gitbook.io/docs/get-started/analyze#assign_model)

This function assigns labels to the training dataset using the trained model. It is only available for unsupervised modules.
{% endtab %}

{% tab title="Deploy" %}

#### [predict\_model](https://pycaret.gitbook.io/docs/get-started/deploy#predict_model)

This function generates the label using a trained model.  When unseen data is not passed, it predicts the label and score on the holdout set.

#### [finalize\_model](https://pycaret.gitbook.io/docs/get-started/deploy#finalize_model)

This function refits a given model on the entire dataset.

#### [save\_model](https://pycaret.gitbook.io/docs/get-started/deploy#save_model)

This function saves the ML pipeline as a pickle file for later use.

#### [load\_model](https://pycaret.gitbook.io/docs/get-started/deploy#load_model)

This function loads a previously saved pipeline.

#### [save\_experiment](https://pycaret.gitbook.io/docs/get-started/deploy#save_experiment)

This function saves an experiment to a pickle file.

#### [load\_experiment](https://pycaret.gitbook.io/docs/get-started/deploy#load_experiment)

This function loads an experiment back into Python from a pickle file.&#x20;

#### [check\_drift](https://pycaret.gitbook.io/docs/get-started/deploy#check_drift)

This function generates a drift report file using the evidently library.&#x20;

#### [deploy\_model](https://pycaret.gitbook.io/docs/get-started/deploy#deploy_model)

This function deploys the entire ML pipeline on the cloud.&#x20;

#### [convert\_model](https://pycaret.gitbook.io/docs/get-started/deploy#convert_model)

This function transpiles the trained machine learning model's decision function in different programming languages such as Python, C, Java, Go, C#, etc.&#x20;

#### [create\_api](https://pycaret.gitbook.io/docs/get-started/deploy#create_api)

This function takes an input model and creates a POST API for inference. It only creates the API and doesn't run it automatically.

#### [create\_docker](https://pycaret.gitbook.io/docs/get-started/deploy#create_docker)

This function creates a Dockerfile and requirements.txt for deploying API.

#### [create\_app](https://pycaret.gitbook.io/docs/get-started/deploy#create_app)

This function creates a basic gradio app for inference.
{% endtab %}

{% tab title="Others" %}

#### [pull](https://pycaret.gitbook.io/docs/get-started/others#pull)

Returns the last printed scoring grid.

#### [models](https://pycaret.gitbook.io/docs/get-started/others#models)

Return a table containing all the models available in the imported module of the model library.

#### [get\_config](https://pycaret.gitbook.io/docs/get-started/others#get_config)

This function retrieves the global variables created by the setup function.&#x20;

#### [set\_config](https://pycaret.gitbook.io/docs/get-started/others#set_config)

This function resets the global variables.

#### [get\_metrics](https://pycaret.gitbook.io/docs/get-started/others#get_metrics)

Returns the table of all available metrics used for cross-validation.

#### [add\_metric](https://pycaret.gitbook.io/docs/get-started/others#add_metric)

Adds a custom metric to the metric container for cross-validation.

#### [remove\_metric](https://pycaret.gitbook.io/docs/get-started/others#remove_metric)

Removes a custom metric from the metric container.&#x20;

#### [automl](https://pycaret.gitbook.io/docs/get-started/others#automl)

This function returns the best model from all the models in the current setup.&#x20;

#### [get\_logs](https://pycaret.gitbook.io/docs/get-started/others#get_logs)

Returns a table of experiment logs. Only works when log\_experiment = True when initializing the setup function.&#x20;

#### [get\_current\_experiment](https://pycaret.gitbook.io/docs/get-started/others#get_current_experiment)

Obtain the current experiment object.&#x20;

#### [set\_current\_experiment](https://pycaret.gitbook.io/docs/get-started/others#set_current_experiment)

Set the current experiment to be used with the functional API.&#x20;
{% endtab %}
{% endtabs %}


# Initialize

Initialize experiment in PyCaret

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


# Train

Training functions in PyCaret

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


# Optimize

Optimization functions in PyCaret

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


# Analyze

Analysis and model explainability functions in PyCaret

## plot\_model

This function analyzes the performance of a trained model on the hold-out set. It may require re-training the model in certain cases.

### **Example**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
lr = create_model('lr')

# plot model
plot_model(lr, plot = 'auc')
```

{% endcode %}

![Output from plot\_model(lr, plot = 'auc')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FSFZTDE4RPTtKFxSq9dM1%2Fimage.png?alt=media\&token=4035979f-8173-489c-be93-62e65ce3938b)

### **Change the scale**

The resolution scale of the figure can be changed with `scale` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
lr = create_model('lr')

# plot model
plot_model(lr, plot = 'auc', scale = 3)
```

{% endcode %}

![Output from plot\_model(lr, plot = 'auc', scale = 3)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FpddJs2yIRrQqy5jFrx72%2Fimage.png?alt=media\&token=c1e98b7d-7575-418d-828a-01d4a568756d)

### Save the plot

You can save the plot as a `png` file using the `save` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
lr = create_model('lr')

# plot model
plot_model(lr, plot = 'auc', save = True)
```

{% endcode %}

![Output from plot\_model(lr, plot = 'auc', save = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fk6TCwKBfcPniCevGBDvv%2Fimage.png?alt=media\&token=d0e19ccd-87b1-488b-8eff-c7dd46bb9748)

### Customize the plot

PyCaret uses [Yellowbrick](https://www.scikit-yb.org/en/latest/) for most of the plotting work. Any argument that is acceptable for Yellowbrick visualizers can be passed as `plot_kwargs` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
lr = create_model('lr')

# plot model
plot_model(lr, plot = 'confusion_matrix', plot_kwargs = {'percent' : True})
```

{% endcode %}

![Output from plot\_model(lr, plot = 'confusion\_matrix', plot\_kwargs = {'percent' : True})](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FTljm811nVfASutHtIfv5%2Fimage.png?alt=media\&token=2dc27bd3-44c6-46d8-8e3d-b7ef7f41993d)

{% tabs %}
{% tab title="Before Customization" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdCLQ2sFXsMBZ79mQzWMJ%2Fimage.png?alt=media\&token=b45154bf-bc39-437d-92c9-3ca201c5d899)
{% endtab %}

{% tab title="After Customization" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FatcYyNvdskXaRQ4ZyL6p%2Fimage.png?alt=media\&token=a4dc488c-6c72-4736-b8df-46985d55e20f)
{% endtab %}
{% endtabs %}

### Use train data

If you want to assess the model plot on the train data, you can pass `use_train_data=True` in the `plot_model` function.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
lr = create_model('lr')

# plot model
plot_model(lr, plot = 'auc', use_train_data = True)
```

{% endcode %}

![Output from plot\_model(lr, plot = 'auc', use\_train\_data = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FRSiXeQsAHz25bguznH88%2Fimage.png?alt=media\&token=85c52950-15ec-4eef-be4f-cf23ba698fe1)

#### Plot on train data vs. hold-out data

{% tabs %}
{% tab title="Train Data" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fb4rZ67Qnk5jNqZCZM6yK%2Fimage.png?alt=media\&token=d626533b-dd95-4cd1-a433-3490d2e4999a)
{% endtab %}

{% tab title="Hold-out Data" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvXBoLHIr06Q3Cme07mnI%2Fimage.png?alt=media\&token=a91292f6-358a-4c6e-b241-81f1bab3c3b3)
{% endtab %}
{% endtabs %}

### **Examples by module**

#### **Classification**

| **Plot Name**               | **Plot**            |
| --------------------------- | ------------------- |
| Area Under the Curve        | ‘auc’               |
| Discrimination Threshold    | ‘threshold’         |
| Precision Recall Curve      | ‘pr’                |
| Confusion Matrix            | ‘confusion\_matrix’ |
| Class Prediction Error      | ‘error’             |
| Classification Report       | ‘class\_report’     |
| Decision Boundary           | ‘boundary’          |
| Recursive Feature Selection | ‘rfe’               |
| Learning Curve              | ‘learning’          |
| Manifold Learning           | ‘manifold’          |
| Calibration Curve           | ‘calibration’       |
| Validation Curve            | ‘vc’                |
| Dimension Learning          | ‘dimension’         |
| Feature Importance (Top 10) | ‘feature’           |
| Feature IImportance (all)   | 'feature\_all'      |
| Model Hyperparameter        | ‘parameter’         |
| Lift Curve                  | 'lift'              |
| Gain Curve                  | 'gain'              |
| KS Statistic Plot           | 'ks'                |

{% tabs %}
{% tab title="auc" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FGUgbUS1Q4aZzMoZ2AhWf%2Fimage.png?alt=media\&token=3f16fd33-721b-4ff5-8b4c-01e0d2d9bea3)
{% endtab %}

{% tab title="confusion\_matrix" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FpnCwxxDLJYhaOmvSI4KV%2Fimage.png?alt=media\&token=5010308c-5665-4f54-bbb4-b60ef756d496)
{% endtab %}

{% tab title="threshold" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fi5UNA6urxNV2LwKZEkt3%2Fimage.png?alt=media\&token=dfc66ca2-f5c3-4a7e-ae05-f7a6f4005a21)
{% endtab %}

{% tab title="pr" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FnxjrzY6JDA3VSrcLHFvy%2Fimage.png?alt=media\&token=efca2fdd-0c23-4430-9225-1285cfe0e20d)
{% endtab %}

{% tab title="error" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7Wts1JHYc8PHCXR61TK3%2Fimage.png?alt=media\&token=541b354f-5a0e-462e-924d-cf65d29c0914)
{% endtab %}

{% tab title="class\_report" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5zgVma9nYa0imruMt2Nc%2Fimage.png?alt=media\&token=267913db-5104-4255-be25-8bab0f5a9c7f)
{% endtab %}

{% tab title="rfe" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FKLtugMSKMtX9bj4y8zWt%2Fimage.png?alt=media\&token=ec546de0-6baa-4031-ad26-e626cb7d5c43)
{% endtab %}

{% tab title="learning" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FE8DEhI7juEXj6tblXXiP%2Fimage.png?alt=media\&token=eb53f905-8444-479a-99c8-688054b83985)
{% endtab %}

{% tab title="vc" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FYfYFlCCBhU3AGsbuk8jA%2Fimage.png?alt=media\&token=2c468b8d-11bf-44ca-8c5e-9c60dfa1de82)
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="feature" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FqlfsnQlBQnybOICrYULr%2Fimage.png?alt=media\&token=e4bf9761-b4af-4139-8b4a-db67dde3e883)
{% endtab %}

{% tab title="manifold" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FScvTsAKxZMm123CHtbyV%2Fimage.png?alt=media\&token=ef2c2024-57d7-4c4b-8a11-97c8cdae7819)
{% endtab %}

{% tab title="calibration" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJ9fq4EMHJayCAkkvzRiD%2Fimage.png?alt=media\&token=de14c091-bafb-41b2-94a0-8c7cbe88decd)
{% endtab %}

{% tab title="dimension" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FwtX44awZBnodALRwREux%2Fimage.png?alt=media\&token=4f9f6696-c8b3-49b2-b0bb-7a84ada539fc)
{% endtab %}

{% tab title="boundary" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhZgRj77QiZmPaQLD9feC%2Fimage.png?alt=media\&token=550c6b2f-b035-421e-83d0-684056e70aed)
{% endtab %}

{% tab title="lift" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FAJEqs0TktXo5uOw6iKou%2Fimage.png?alt=media\&token=784c0356-67e2-458c-8050-c3bb111e8789)
{% endtab %}

{% tab title="gain" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FeQHQ0PstIWPo37J0jY6O%2Fimage.png?alt=media\&token=92c76146-0ad7-4fb6-be5d-5e40225c8148)
{% endtab %}

{% tab title="ks" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5kfKHqvamuekQaFecuzo%2Fimage.png?alt=media\&token=2d42c04f-6525-432c-93ae-d864e2b549b5)
{% endtab %}

{% tab title="parameter" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FnPvFC9ohOoO4YhkmiGZ0%2Fimage.png?alt=media\&token=214adf73-6bec-4adc-9034-1f345f4ca2e2)
{% endtab %}
{% endtabs %}

#### Regression

| **Name**                    | **Plot**       |
| --------------------------- | -------------- |
| Residuals Plot              | ‘residuals’    |
| Prediction Error Plot       | ‘error’        |
| Cooks Distance Plot         | ‘cooks’        |
| Recursive Feature Selection | ‘rfe’          |
| Learning Curve              | ‘learning’     |
| Validation Curve            | ‘vc’           |
| Manifold Learning           | ‘manifold’     |
| Feature Importance (top 10) | ‘feature’      |
| Feature Importance (all)    | 'feature\_all' |
| Model Hyperparameter        | ‘parameter’    |

{% tabs %}
{% tab title="residuals" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FcLTPCV62Oo9ONqzz80ZW%2Fimage.png?alt=media\&token=8021da4d-2e7f-4bdd-9244-d11f56aa7475)
{% endtab %}

{% tab title="error" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F68ksvyFJXUSa8yyfYkyV%2Fimage.png?alt=media\&token=d099e984-8f01-4f37-beba-4ac9cc4a5677)
{% endtab %}

{% tab title="cooks" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FWVygIOxa8qcZXgId9d3T%2Fimage.png?alt=media\&token=82b7d25b-4984-4f0f-93c7-6424d7d1f9f6)
{% endtab %}

{% tab title="rfe" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FgTSKAzs77hSxwi3hWOxm%2Fimage.png?alt=media\&token=b7859dbc-e9df-4a70-9241-1edd7cb53766)
{% endtab %}

{% tab title="feature" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FK9LpggTwsrzwfWUC26mM%2Fimage.png?alt=media\&token=963058f1-63f1-48d9-8a34-5f0784065ceb)
{% endtab %}

{% tab title="learning" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7ZunDTB89p8B5f8Jv3z6%2Fimage.png?alt=media\&token=f2512b24-7128-4337-bdf5-94bd1f521e7f)
{% endtab %}

{% tab title="vc" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fzl15fNUn3BjWlfrV0EFn%2Fimage.png?alt=media\&token=e2c842b2-6b18-47e1-8fe8-2cceb6a5e661)
{% endtab %}

{% tab title="manifold" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fl3PJlhDcuOBzXTCDBd9w%2Fimage.png?alt=media\&token=4c8169ae-9f99-46b5-a943-05cd4089da79)
{% endtab %}
{% endtabs %}

#### Clustering

| **Name**              | **Plot**       |
| --------------------- | -------------- |
| Cluster PCA Plot (2d) | ‘cluster’      |
| Cluster TSnE (3d)     | ‘tsne’         |
| Elbow Plot            | ‘elbow’        |
| Silhouette Plot       | ‘silhouette’   |
| Distance Plot         | ‘distance’     |
| Distribution Plot     | ‘distribution’ |

{% tabs %}
{% tab title="cluster" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvdORfGM3ED6LOVSmdUtg%2Fimage.png?alt=media\&token=382110c9-b6e9-473b-b2c1-8becdf560b39)
{% endtab %}

{% tab title="tsne" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FhTqAwyl84uQTJJ0kZWFB%2Fimage.png?alt=media\&token=f0d8c6d9-1127-4725-8d11-2de33c0bec58)
{% endtab %}

{% tab title="elbow" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FqhbMVDTmSt1pmaV0SK9B%2Fimage.png?alt=media\&token=aa70c0c5-502b-407d-a003-be9493a567bf)
{% endtab %}

{% tab title="silhouette" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FPo0Z3hAdhrJEAbgSEQpJ%2Fimage.png?alt=media\&token=292682ab-46aa-441c-931a-c4956cca1b40)
{% endtab %}

{% tab title="distance" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F8GRV7MYRkK4L9QxlPvCA%2Fimage.png?alt=media\&token=bf5b2768-75ea-428e-b6e6-c442ce685fc6)
{% endtab %}

{% tab title="distribution" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fxjm1MgHw0vxif5toLuNP%2Fimage.png?alt=media\&token=4fb91e45-b2d3-4952-a2fd-9f5ddc142893)
{% endtab %}
{% endtabs %}

#### Anomaly Detection

| **Name**                  | **Plot** |
| ------------------------- | -------- |
| t-SNE (3d) Dimension Plot | ‘tsne’   |
| UMAP Dimensionality Plot  | ‘umap’   |

{% tabs %}
{% tab title="tsne" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FaTUgs5aDzfFwWZUIGd86%2Fimage.png?alt=media\&token=b5ea3868-6e7d-42ba-999c-8eb8da8d1ff3)
{% endtab %}

{% tab title="umap" %}
![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FFFnWG3BxbhsVnS2iebqT%2Fimage.png?alt=media\&token=4b17e9bc-35b6-4095-8d2d-0a7cd5be4c2d)
{% endtab %}
{% endtabs %}

## evaluate\_model

The `evaluate_model` displays a user interface for analyzing the performance of a trained model. It calls the [plot\_model](#plot_model) function internally.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# create model
lr = create_model('lr')

# launch evaluate widget
evaluate_model(lr)
```

{% endcode %}

![Output from evaluate\_model(lr)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FTRHCfF7xhHyFTFgsMkNs%2Fimage.png?alt=media\&token=52066707-446f-4ffe-8554-efd7b11c88b9)

{% hint style="info" %}
**NOTE:** This function only works in Jupyter Notebook or an equivalent environment.
{% endhint %}

## interpret\_model

This function analyzes the predictions generated from a trained model. Most plots in this function are implemented based on the SHAP (Shapley Additive exPlanations). For more info on this, please see <https://shap.readthedocs.io/en/latest/>

### Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost)
```

{% endcode %}

![Output from interpret\_model(xgboost)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FT5XkrbLn4c3d50yZi3w5%2Fimage.png?alt=media\&token=d7f03152-3c8d-4442-9b94-72227f3384b5)

### Save the plot

You can save the plot as a `png` file using the `save` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, save = True)
```

{% endcode %}

{% hint style="info" %}
**NOTE:** When `save=True` no plot is displayed in the Notebook.&#x20;
{% endhint %}

### Change plot type

There are a few different plot types available that can be changed by the `plot` parameter.

#### Correlation

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'correlation')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'correlation')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FWflxKk993rlbNu6pbHBF%2Fimage.png?alt=media\&token=bc905e44-2b48-4546-a276-301c85aafdfc)

By default, PyCaret uses the first feature in the dataset but that can be changed using `feature` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'correlation', feature = 'Age (years)')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'correlation', feature = 'Age (years)')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F47IHbZ399lyYDBcocF2P%2Fimage.png?alt=media\&token=7e35492c-672d-471c-a076-716007dceebc)

#### Partial Dependence Plot

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'pdp')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'pdp')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F7neJyI3odxe5WEuTh0qB%2Fimage.png?alt=media\&token=e6ce2428-b3b0-4b9b-8b08-78ad4e93fc29)

By default, PyCaret uses the first available feature in the dataset but this can be changed using the `feature` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'pdp', feature = 'Age (years)')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'pdp', feature = 'Age (years)')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F9Vgs03uZz6k11ymPRZWa%2Fimage.png?alt=media\&token=cb4e784a-55df-4349-a5cd-064f5a613cfd)

#### Morris Sensitivity Analysis

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'msa')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'msa')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FE8kP4bi8Vi7PmymnqqKJ%2Fimage.png?alt=media\&token=3a025322-8c38-42f8-8ed1-84b38807d924)

#### Permutation Feature Importance

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'pfi')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'pfi')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1oqO1ThMZak1OEtjnyr6%2Fimage.png?alt=media\&token=b613338a-bf2e-4d7f-a6a9-6a3c74e10957)

#### Reason Plot

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'reason')
```

{% endcode %}

![Output from interpret\_model(xgboost, plot = 'reason')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FSvhjGvrhHuTkzEfovZmb%2Fimage.png?alt=media\&token=280c96c2-8ad2-4c11-8c37-3e2c49556069)

When you generate `reason` plot without passing the specific index of test data, you will get the interactive plot displayed with the ability to select the x and y-axis. This will only be possible if you are using Jupyter Notebook or an equivalent environment. If you want to see this plot for a specific observation, you will have to pass the index in the `observation` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, plot = 'reason', observation = 1)
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FHQKug8TAzhifX6zgJkZy%2Fimage.png?alt=media\&token=641a49f8-b93b-4094-b392-94ee43b63dfa)

Here the `observation = 1` means index 1 from the test set.

### Use train data

By default, all the plots are generated on the test dataset. If you want to generate plots using a train data set (not recommended) you can use `use_train_data` parameter.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# creating a model
xgboost = create_model('xgboost')

# interpret model
interpret_model(xgboost, use_train_data = True)
```

{% endcode %}

![Output from interpret\_model(xgboost, use\_train\_data = True)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F4ZL0sYPJrArtrtIIuobf%2Fimage.png?alt=media\&token=da72b8a3-5ac0-4a61-99ad-37a34dded76c)

## dashboard

The `dashboard` function generates the interactive dashboard for a trained model. The dashboard is implemented using ExplainerDashboard ([explainerdashboard.readthedocs.io](https://explainerdashboard.readthedocs.io))

#### Dashboard Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# train model
lr = create_model('lr')

# launch dashboard
dashboard(lr)
```

{% endcode %}

![Dashboard (Classification Metrics)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FSC3Ozp5qO4sjrJeFVFvL%2Fimage.png?alt=media\&token=cc7562aa-029a-497f-9dee-c415fb10fac0)

![Dashboard (Individual Predictions)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FQp3LUFzgqewjWLyPVMgU%2Fimage.png?alt=media\&token=68981bc7-88db-4021-babe-bccfb89d79fb)

![Dashboard (What-if analysis)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FJ7TRZsxwOovuYbCaDntl%2Fimage.png?alt=media\&token=dcfacb31-363c-4ab8-acc3-075531a78faf)

#### Video:

{% embed url="<https://www.youtube.com/watch?v=FZ5-GtdYez0>" %}

## check\_fairness

There are many approaches to conceptualizing fairness. The `check_fairness` function follows the approach known as group fairness, which asks: which groups of individuals are at risk for experiencing harm. `check_fairness` provides fairness-related metrics between different groups (also called sub-population).

#### Check Fairness Example

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
income = get_data('income')

# init setup
from pycaret.classification import *
exp_name = setup(data = income,  target = 'income >50K')

# train model
lr = create_model('lr')

# check model fairness
lr_fairness = check_fairness(lr, sensitive_features = ['sex', 'race'])
```

{% endcode %}

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FkwLOlan0FV89pbPQmw3g%2Fimage.png?alt=media\&token=d2701724-901a-454c-a519-ae02b619f052)

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fl6cpxYLRQJyixqBHs4bu%2Fimage.png?alt=media\&token=662f19c0-a859-4aea-9850-622828f29110)

#### Video:

{% embed url="<https://www.youtube.com/watch?v=mjhDKuLRpM0>" %}

## get\_leaderboard

This function returns the leaderboard of all models trained in the current setup.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# compare models
top3 = compare_models(n_select = 3)

# tune top 3 models
tuned_top3 = [tune_model(i) for i in top3]

# ensemble top 3 tuned models
ensembled_top3 = [ensemble_model(i) for i in tuned_top3]

# blender
blender = blend_models(tuned_top3)

# stacker
stacker = stack_models(tuned_top3)

# check leaderboard
get_leaderboard()
```

{% endcode %}

![Output from get\_leaderboard()](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F8M0V4AukOOQgKMtEdpAy%2Fimage.png?alt=media\&token=0b9e54db-0c24-4b24-bbae-886ce1c040cf)

You can also access the trained Pipeline with this.&#x20;

{% code lineNumbers="true" %}

```python
# check leaderboard
lb = get_leaderboard()

# select top model
lb.iloc[0]['Model']
```

{% endcode %}

![Output from lb.iloc\[0\]\['Model'\]](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUhx4lsLDXcS5wl30xS8Y%2Fimage.png?alt=media\&token=e6990e29-e67d-43d0-ab3b-256d997d11dc)

## assign\_model

This function assigns labels to the training dataset using the trained model. It is available for [Clustering](https://pycaret.gitbook.io/docs/get-started/modules), [Anomaly Detection](https://pycaret.gitbook.io/docs/get-started/modules), and [NLP](https://pycaret.gitbook.io/docs/get-started/modules) modules.

#### Clustering

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
jewellery = get_data('jewellery')

# init setup
from pycaret.clustering import *
clu1 = setup(data = jewellery)

# train a model
kmeans = create_model('kmeans')

# assign model
assign_model(kmeans)
```

{% endcode %}

![Output from assign\_model(kmeans)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FsbLtBBSKYWc2JU8DcPBW%2Fimage.png?alt=media\&token=cad08736-480c-4031-b13f-5119fb87a87e)

#### Anomaly Detection

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
anomaly = get_data('anomaly')

# init setup
from pycaret.anomaly import *
ano1 = setup(data = anomaly)

# train a model
iforest = create_model('iforest')

# assign model
assign_model(iforest)
```

{% endcode %}

![Output from assign\_model(iforest)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FGsLNmTGTR8mGgaFY9L1i%2Fimage.png?alt=media\&token=61bbda81-6382-4779-b7fe-833ba88bcb2d)


# Deploy

MLOps and deployment related functions in PyCaret

## predict\_model

This function generates the label using a trained model.  When `data` is None, it predicts label and score on the holdout set.&#x20;

### **Hold-out predictions**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
xgboost = create_model('xgboost')

# predict on hold-out
predict_model(xgboost)
```

{% endcode %}

![Output from predict\_model(xgboost)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FxDoQCZokWwjWAoj6V3RG%2Fimage.png?alt=media\&token=b4b861cd-bf71-48fc-a059-20f276dd34f0)

### **Unseen data predictions**

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
xgboost = create_model('xgboost')

# predict on new data
new_data = diabetes.copy()
new_data.drop('Class variable', axis = 1, inplace = True)
predict_model(xgboost, data = new_data)
```

{% endcode %}

![Output from predict\_model(xgboost, data=new\_data)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fc6GqPUXIf7G1WWmgTUHp%2Fimage.png?alt=media\&token=f0287182-98f1-498c-9f97-f09e87ea8c22)

### Probability by class

{% hint style="info" %}
**NOTE:** This is only applicable for the [Classification](https://pycaret.gitbook.io/docs/get-started/modules) use-cases.&#x20;
{% endhint %}

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
xgboost = create_model('xgboost')

# predict on new data
new_data = diabetes.copy()
new_data.drop('Class variable', axis = 1, inplace = True)
predict_model(xgboost, raw_score = True, data = new_data)
```

{% endcode %}

![Output from predict\_model(xgboost, raw\_score = True, data = new\_data)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FwXESCzmpMTomRPTLjPdS%2Fimage.png?alt=media\&token=349b4985-7396-41be-b622-968d0d94344c)

### Setting probability threshold

{% hint style="info" %}
**NOTE:** This is only applicable for the [Classification](https://pycaret.gitbook.io/docs/get-started/modules) use-cases (binary only).
{% endhint %}

The threshold for converting predicted probability to the class labels. Unless this parameter is set, it will default to the value set during model creation. If that wasn’t set, the default will be 0.5 for all classifiers. Only applicable for binary classification.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
xgboost = create_model('xgboost')

# probability threshold 0.3
predict_model(xgboost, probability_threshold = 0.3)
```

{% endcode %}

![Output from predict\_model(xgboost, probability\_threshold = 0.3)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FI18qJsoiBqbV28pJhBMT%2Fimage.png?alt=media\&token=efaa70ce-e67b-400c-8dd9-91bc9cf24359)

#### Comparison between different thresholds on the hold-out data

![probability threshold = 0.5 vs. probability threshold = 0.3](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FDlMx2jStEp9xEro1wTg4%2Fimage.png?alt=media\&token=cf7c9745-94ed-4f65-a4ab-9e31d42b0f41)

## finalize\_model

This function trains a given model on the entire dataset including the hold-out set.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
rf = create_model('rf')

# finalize a model
finalize_model(rf)
```

{% endcode %}

![Output from finalize\_model(rf)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fh56NcrnyMOs3dIhuOrU5%2Fimage.png?alt=media\&token=fb783786-5568-4273-b50c-bbad7e915b82)

This function doesn't change any parameter of the model. It only refits on the entire dataset including the hold-out set.

## deploy\_model

This function deploys the entire ML pipeline on the cloud.

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
lr = create_model('lr')

# finalize a model
final_lr = finalize_model(lr)

# deploy a model
deploy_model(final_lr, model_name = 'lr_aws', platform = 'aws', authentication = { 'bucket'  : 'pycaret-test' })
```

{% endcode %}

![Output from deploy\_model(...)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FxQUVp2IUnC3QuFqu47Ib%2Fimage.png?alt=media\&token=b799b4af-d1a0-4a0a-9085-a22c2e966552)

### AWS

Before deploying a model to an AWS S3 (‘aws’), environment variables must be configured using the command-line interface. To configure AWS environment variables, type **aws configure** in your python command line. The following information is required which can be generated using the Identity and Access Management (IAM) portal of your amazon console account:

* AWS Access Key ID
* AWS Secret Key Access
* Default Region Name (can be seen under Global settings on your AWS console)
* Default output format (must be left blank)

### GCP

To deploy a model on Google Cloud Platform ('gcp'), the project must be created using the command-line or GCP console. Once the project is created, you must create a service account and download the service account key as a JSON file to set environment variables in your local environment.

Learn more about it: <https://cloud.google.com/docs/authentication/production>

### Azure

To deploy a model on Microsoft Azure ('azure'), environment variables for the connection string must be set in your local environment. Go to settings of storage account on Azure portal to access the connection string required.

* AZURE\_STORAGE\_CONNECTION\_STRING (required as environment variable)

Learn more about it: <https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?toc=%2Fpython%2Fazure%2FTOC.json>

## save\_model

This function saves the transformation pipeline and a trained model object into the current working directory as a pickle file for later use.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
dt = create_model('dt')

# save pipeline
save_model(dt, 'dt_pipeline')
```

{% endcode %}

![Output from save\_model(dt, 'dt\_pipeline')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fh74jxGDC5EojHs9Xuwhs%2Fimage.png?alt=media\&token=d9a27a4e-521e-4b00-aed2-843176b86a7e)

## load\_model

This function loads a previously saved pipeline.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# create a model
dt = create_model('dt')

# save pipeline
save_model(dt, 'dt_pipeline')

# load pipeline
load_model('dt_pipeline')
```

{% endcode %}

![Output from load\_model('dt\_pipeline')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FdlwPXLiInZk52WdFaQ8D%2Fimage.png?alt=media\&token=597f91a9-5d83-40f9-b333-5e3a22e17aa2)

## save\_experiment

The `save_experiment` function saves the experiment to a pickle file. The experiment is saved using cloudpickle to deal with lambda functions. The data or test data is NOT saved with the experiment and will need to be specified again when loading using `load_experiment`.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
diabetes = get_data('diabetes')

# init setup
from pycaret.classification import *
clf1 = setup(data = diabetes, target = 'Class variable')

# save experiment
save_experiment('my_saved_experiment1')
```

{% endcode %}

## load\_experiment

The `load_experiment` function loads an experiment from the path or a file. The `data` (and `test_data`) is not saved with the experiment and will need to be specified again at the time of loading.

{% code lineNumbers="true" %}

```python
# load data
data = get_data('diabetes')

# load experiment function
from pycaret.classification import load_experiment
clf2 = load_experiment('my_saved_experiment1', data = data)
```

{% endcode %}

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FkKo99DbyWzEIrvXkeDqw%2Fimage.png?alt=media&#x26;token=d76e2115-8428-48aa-98c8-cd7097cdb09e" alt=""><figcaption></figcaption></figure>

## check\_drift

The `check_drift` function generates a drift report file using the evidently library.

{% code overflow="wrap" lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
data = get_data('insurance')

# generate drift report
check_drift(reference_data = data.head(500), current_data = data.tail(500), target = 'charges')
```

{% endcode %}

It will generate a HTML report locally.&#x20;

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FSAiFjL4BupQMaNOTNUTS%2Fimage.png?alt=media&#x26;token=d0846e6a-d6b9-4336-a88c-b81a67ceb48b" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FYB5rlxVQF2XvGKUprQEd%2Fimage.png?alt=media&#x26;token=2ce24165-d67b-4930-8ad5-db485eb1f9f9" alt=""><figcaption></figcaption></figure>

## convert\_model

This function transpiles the trained machine learning model's decision function in different programming languages such as Python, C, Java, Go, C#, etc. It is very useful if you want to deploy models into environments where you can't install your normal Python stack to support model inference.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# train a model
lr = create_model('lr')

# convert a model
convert_model(lr, 'java')
```

{% endcode %}

![Output from convert\_model(lr, 'java')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FUNuM0Ay7LLiCjDPNUdC5%2Fimage.png?alt=media\&token=551b0075-552f-44bb-9be6-4cc2c59be930)

#### Video:

{% embed url="<https://www.youtube.com/watch?t=1s&v=xwQgfNC7808>" %}

## create\_api

This function takes an input model and creates a POST API for inference. It only creates the API and doesn't run it automatically. To run the API, you must run the Python file using `!python`.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# train a model
lr = create_model('lr')

# create api
create_api(lr, 'lr_api')

# run api
!python lr_api.py
```

{% endcode %}

![Output from create\_api(lr, 'lr\_api')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FChPOL5r6IcWgkj1OBm3h%2Fimage.png?alt=media\&token=83b701d8-1d3a-4ee1-a500-d7d11d4f7183)

Once you initialize API with the `!python` command. You can see the server on localhost:8000/docs.

![FastAPI server hosted on localhost](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FpzaQUHxf4Smt3390Mi2q%2Fimage.png?alt=media\&token=415d1363-b2c7-4e11-b2ae-80410682de23)

#### Video:

{% embed url="<https://www.youtube.com/watch?t=3s&v=88M9c5Hc-k0>" %}

## create\_docker

This function creates a `Dockerfile` and `requirements.txt` for productionalizing API end-point.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# train a model
lr = create_model('lr')

# create api
create_api(lr, 'lr_api')

# create docker
create_docker('lr_api')
```

{% endcode %}

![Output from create\_docker('lr\_api')](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F4Fpj68sWSQLSWcw5d7fr%2Fimage.png?alt=media\&token=6540627f-93ba-4877-8ef9-2a3ae3be7e6b)

You can see two files are created for you.&#x20;

![%load requirements.txt](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FiND3URES8duiUpF8YAwF%2Fimage.png?alt=media\&token=569dad5c-f88f-4f8f-89a3-ac0a6c1c1a79)

![%load DockerFile](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F2crfM6bIoe4u4CMIAcMo%2Fimage.png?alt=media\&token=36d8fbde-83cf-460c-a3b0-640b40d4dcb0)

#### Video:

{% embed url="<https://www.youtube.com/watch?t=1s&v=xMgwEJ57uxs>" %}

## create\_app

This function creates a basic `gradio` app for inference. It will later be expanded for other app types such `Streamlit`.

{% code lineNumbers="true" %}

```python
# load dataset
from pycaret.datasets import get_data
juice = get_data('juice')

# init setup
from pycaret.classification import *
exp_name = setup(data = juice,  target = 'Purchase')

# train a model
lr = create_model('lr')

# create app
create_app(lr)
```

{% endcode %}

![Output from create\_app(lr)](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F39qYrZUTzgeJPLcfgMpA%2Fimage.png?alt=media\&token=88638e7a-689a-4a92-941f-07037379ee83)

#### Video:

{% embed url="<https://www.youtube.com/watch?v=4JyYhbW6eCA>" %}


# Others

Other functions in PyCaret

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


# Blog

Official tutorials and guide written by the developers of PyCaret

### Announcements

* [Announcing PyCaret 1.0](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/announcing-pycaret-1.0)
* [Announcing PyCaret 2.0](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/announcing-pycaret-2.0)
* [PyCaret 2.1 Feature Summary](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/pycaret-2.1-feature-summary)
* [PyCaret 2.3.6 is here! Learn What's New?](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/pycaret-2.3.6-is-here-learn-whats-new)

### Machine Learning Use Cases

* [Predict Customer Churn](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/predict-customer-churn-using-pycaret)
* [Predict Lead Conversion Score](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/predict-lead-score-the-right-way-using-pycaret)
* [Predict Crash in Gold Prices](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/predicting-crashes-in-gold-prices-using-pycaret)
* [Predict Gold Prices using Machine Learning](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/predicting-gold-prices-using-machine-learning)

### Time Series

* [Time Series 101 for beginners](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/time-series-101-for-beginners)
* [Time Series Forecasting with PyCaret Regression](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/time-series-forecasting-with-pycaret-regression)
* [Time Series Anomaly Detection](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/time-series-anomaly-detection-with-pycaret)

### PyCaret add ML Deployment

* [Build and deploy your first machine learning web app](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/build-and-deploy-your-first-machine-learning-web-app)
* [Deploy ML Pipelines on Google Kubernetes](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/deploy-ml-pipeline-on-google-kubernetes)
* [Deployment PyCaret and Streamlit on AWS Fargate](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/deploy-pycaret-and-streamlit-on-aws-fargate-1)
* [Deploy ML App on Google Kubernetes](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/deploy-ml-app-on-google-kubernetes)
* [Deploy Machine Learning Pipeline on AWS Fargate](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/deploy-machine-learning-pipeline-on-aws-fargate)
* [Ship ML Models to SQL Server using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/ship-ml-models-to-sql-server-using-pycaret)
* [Build and deploy ML App with PyCaret and Streamlit](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/build-and-deploy-ml-app-with-pycaret-and-streamlit)

### PyCaret and MLOps

* [Easy MLOps with PyCaret and MLflow](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/easy-mlops-with-pycaret-and-mlflow)
* [Write and train custom ML models using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/write-and-train-custom-ml-models-using-pycaret)
* [Supercharge your ML with PyCaret and Gradio](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/supercharge-your-ml-with-pycaret-and-gradio)
* [Deploy PyCaret Models on edge with ONNX runtime](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/deploy-pycaret-models-on-edge-with-onnx-runtime)

### PyCaret and BI integrations

* [Machine Learning in Power BI using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/machine-learning-in-power-bi-using-pycaret)
* [Clustering Analysis in Power BI using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/clustering-analysis-in-power-bi-using-pycaret-1)
* [Anomaly Detector in Power BI using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/anomaly-detector-in-power-bi-using-pycaret)
* [Build your own AutoML in Power BI using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/build-your-own-automl-in-power-bi-using-pycaret)
* [Machine Learning in Alteryx with PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/machine-learning-in-alteryx-with-pycaret)
* [Machine Learning in KNIME with PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/machine-learning-in-knime-with-pycaret)
* [Machine Learning in Tableau with PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/machine-learning-in-tableau-with-pycaret)

### Natural Language Processing

* [NLP Text Classification in Python using PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/nlp-text-classification-in-python-using-pycaret)

### Other Tutorials

* [5 things you don't know about PyCaret](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog/5-things-you-dont-know-about-pycaret)


# Announcing PyCaret 1.0

![](https://cdn-images-1.medium.com/max/2000/1*Xtb7t4Rlxq8jFLXZn_sdyQ.png)

### Announcing PyCaret 1.0.0

#### An open source **low-code** machine learning library in Python.

#### by Moez Ali

We are excited to announce [PyCaret](https://www.pycaret.org), an open source machine learning library in Python to train and deploy supervised and unsupervised machine learning models in a **low-code** environment. PyCaret allows you to go from preparing data to deploying models within seconds from your choice of notebook environment.

In comparison with the other open source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few words only. This makes experiments exponentially fast and efficient. PyCaret is essentially a Python wrapper around several machine learning libraries and frameworks such as [scikit-learn](https://scikit-learn.org/stable/), [XGBoost](https://xgboost.readthedocs.io/en/latest/), [Microsoft LightGBM](https://github.com/microsoft/LightGBM), [spaCy](https://spacy.io/), and many more.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully orchestrated for \*\*deployment. \*\*Whether its imputing missing values, transforming categorical data, feature engineering or even hyperparameter tuning, PyCaret automates all of it. To learn more about PyCaret, watch this 1-minute video.

### Getting Started with PyCaret

The first stable release of PyCaret version 1.0.0 can be installed using pip. Using the command line interface or notebook environment, run the below cell of code to install PyCaret.

```
pip install pycaret
```

If you are using [Azure notebooks](https://notebooks.azure.com/) or [Google Colab](https://colab.research.google.com/), run the below cell of code to install PyCaret.

```
!pip install pycaret
```

When you install PyCaret, all dependencies are installed automatically. [Click here](https://github.com/pycaret/pycaret/blob/master/requirements.txt) to see the list of complete dependencies.

### It cannot get easier than this 👇

![](https://cdn-images-1.medium.com/max/2560/1*QG6SjFXOV6wqY_00D1fsLw.gif)

### 📘 Step-by-Step Tutorial

### 1. Getting Data

In this step-by-step tutorial, we will use \*\*‘diabetes’ \*\*dataset and the goal is to predict patient outcome (binary 1 or 0) based on several factors such as Blood Pressure, Insulin Level, Age etc. The dataset is available on PyCaret’s [github repository](https://github.com/pycaret/pycaret). Easiest way to import dataset directly from repository is by using \*\*get\_data \*\*function from **pycaret.datasets** modules.

```
from **pycaret.datasets** import **get_data**
diabetes = **get_data**('diabetes')
```

![output from get\_data](https://cdn-images-1.medium.com/max/2658/1*o1xpZeVNUfzm7yQ6f1IPvw.png)

💡 PyCaret can work directly with **pandas** dataframe.

### 2. Setting up Environment

The first step of any machine learning experiment in PyCaret is setting up the environment by importing the required module and initializing **setup**( ). The module used in this example is [\*\*pycaret.classification](https://www.pycaret.org/classification).\*\*

Once the module is imported, \*\*setup() \*\*is initialized by defining the dataframe (*‘diabetes’*) and the target variable (*‘Class variable’*).

```
from **pycaret.classification** import ***
**exp1 = **setup**(diabetes, target = 'Class variable')
```

![](https://cdn-images-1.medium.com/max/2000/1*WaVNaMkfoHIrD0lKPHFvJA.png)

All the preprocessing steps are applied within \*\*setup(). \*\*With over 20 features to prepare data for machine learning, PyCaret creates a transformation pipeline based on the parameters defined in \*setup \*function. It automatically orchestrates all dependencies in a \*\*pipeline \*\*so that you don’t have to manually manage the sequential execution of transformations on test or unseen dataset. PyCaret’s pipeline can easily be transferred across environments to run at scale or be deployed in production with ease. Below are preprocessing features available in PyCaret as of its first release.

![Preprocessing capabilities of PyCaret](https://cdn-images-1.medium.com/max/2000/1*jo9vPsQhQZmyXUhnrt9akQ.png)

💡 Data Preprocessing steps that are compulsory for machine learning such as missing values imputation, categorical variable encoding, label encoding (converting yes or no into 1 or 0), and train-test-split are automatically performed when setup() is initialized. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing abilities.

### 3. Compare Models

This is the first step recommended in supervised machine learning experiments ([classification](https://www.pycaret.org/classification) or [regression](https://www.pycaret.org/regression)). This function trains all the models in the model library and compares the common evaluation metrics using k-fold cross validation (by default 10 folds). The evaluation metrics used are:

* \*\*For Classification: \*\*Accuracy, AUC, Recall, Precision, F1, Kappa
* \*\*For Regression: \*\*MAE, MSE, RMSE, R2, RMSLE, MAPE

  **compare\_models**()

![Output from compare\_models( ) function](https://cdn-images-1.medium.com/max/2000/1*WaaSiqUkIFMiKbYofBRo7Q.png)

💡 Metrics are evaluated using 10-fold cross validation by default. It can be changed by changing the value of \*\*\*fold \*\*\*parameter.

💡 Table is sorted by ‘Accuracy’ (Highest to Lowest) value by default. It can be changed by changing the value of \*\*\*sort \*\*\*parameter.

### 4. Create Model

Creating a model in any module of PyCaret is as simple as writing \**create\_model.* \*\*\*It takes only one parameter i.e. the model name passed as string input. This function returns a table with k-fold cross validated scores and a trained model object.

```
adaboost = **create_model**('ada')
```

![](https://cdn-images-1.medium.com/max/2000/1*1twQHlWEbUbEtVEas0NQDQ.png)

Variable ‘adaboost’ stores a trained model object returned by **create\_model** function is a scikit-learn estimator. Original attributes of a trained object can be accessed by using \*period ( . ) \*after variable. See example below.

![Attributes of trained model object](https://cdn-images-1.medium.com/max/2560/1*Vlh9B3l6tFwlCNzJBfQEcQ.gif)

💡 PyCaret has over 60 open source ready-to-use algorithms. [Click here](https://www.pycaret.org/create-model) to see a complete list of estimators / models available in PyCaret.

### 5. Tune Model

The \*\*tune\_model **function is used for automatically tuning hyperparameters of a machine learning model**. \*\*PyCaret uses **random grid search** over a predefined search space. This function returns a table with k-fold cross validated scores and a trained model object.

```
tuned_adaboost = tune_model('ada')
```

![](https://cdn-images-1.medium.com/max/2000/1*pqsFYecRxZ_ruvwBXZWlQA.png)

💡 The \*\*tune\_model \*\*function in unsupervised modules such as [pycaret.nlp](https://www.pycaret.org/nlp), [pycaret.clustering](https://www.pycaret.org/clustering) and [pycaret.anomaly](https://www.pycaret.org/anomaly) can be used in conjunction with supervised modules. For example, PyCaret’s NLP module can be used to tune *number of topics* parameter by evaluating an objective / cost function from a supervised ML model such as ‘Accuracy’ or ‘R2’.

### 6. Ensemble Model

The \*\*ensemble\_model **function is used for ensembling trained models**. \*\*It takes only one parameter i.e. a trained model object. This functions returns a table with k-fold cross validated scores and a trained model object.

```
# creating a decision tree model
dt = **create_model**('dt')

# ensembling a trained dt model
dt_bagged = **ensemble_model**(dt)
```

![](https://cdn-images-1.medium.com/max/2000/1*uw2WmHc1oFeUfnnz-jYfhA.png)

💡 ‘Bagging’ method is used for ensembling by default which can be changed to ‘Boosting’ by using the ***method*** parameter within the ensemble\_model function.

💡 PyCaret also provide [blend\_models](https://www.pycaret.org/blend-models) and [stack\_models](https://www.pycaret.org/stack-models) functionality to ensemble multiple trained models.

### 7. Plot Model

Performance evaluation and diagnostics of a trained machine learning model can be done using the \*\*plot\_model \*\*function. It takes a trained model object and the type of plot as a string input within the **plot\_model** function.

```
# create a model
adaboost = **create_model**('ada')

# AUC plot
**plot_model**(adaboost, plot = 'auc')

# Decision Boundary
**plot_model**(adaboost, plot = 'boundary')

# Precision Recall Curve
**plot_model**(adaboost, plot = 'pr')

# Validation Curve
**plot_model**(adaboost, plot = 'vc')
```

![](https://cdn-images-1.medium.com/max/2376/1*JnfDw9wwuGxTDS676_hBXg.png)

[Click here](https://www.pycaret.org/plot-model) to learn more about different visualization in PyCaret.

Alternatively, you can use \*\*evaluate\_model \*\*function to see plots \*via \*user interface within notebook.

```
**evaluate_model**(adaboost)
```

![](https://cdn-images-1.medium.com/max/2560/1*TMuREzi-o7_edYCj4yIZfA.gif)

💡 **plot\_model** function in \*\*pycaret.nlp \*\*module can be used to visualize *text corpus* and *semantic topic models*. [Click here](https://pycaret.org/plot-model/#nlp) to learn more about it.

### 8. Interpret Model

When the relationship in data is non-linear which is often the case in real life we invariably see tree-based models doing much better than simple gaussian models. However, this comes at the cost of losing interpretability as tree-based models do not provide simple coefficients like linear models. PyCaret implements [SHAP (SHapley Additive exPlanations](https://shap.readthedocs.io/en/latest/) using \*\*interpret\_model \*\*function.

```
# create a model
xgboost = **create_model**('xgboost')

# summary plot
**interpret_model**(xgboost)

# correlation plot
**interpret_model**(xgboost, plot = 'correlation')
```

![](https://cdn-images-1.medium.com/max/2000/1*ct0UFJA2sxTpSTwSwO1-fQ.png)

Interpretation of a particular datapoint (also known as reason argument) in the test dataset can be evaluated using ‘reason’ plot. In the below example we are checking the first instance in our test dataset.

```
**interpret_model**(xgboost, plot = 'reason', observation = 0) 
```

![](https://cdn-images-1.medium.com/max/2184/1*hsM128hQ2sDk9TnTHBH9Bw.png)

### 9. Predict Model

So far the results we have seen are based on k-fold cross validation on training dataset only (70% by default). In order to see the predictions and performance of the model on the test / hold-out dataset, the **predict\_model** function is used.

```
# create a model
rf = **create_model**('rf')

# predict test / hold-out dataset
rf_holdout_pred **= predict_model**(rf)
```

![](https://cdn-images-1.medium.com/max/2000/1*e05Sd2KFexSjxORcaxAeFw.png)

\*\*predict\_model \*\*function is also used to predict unseen dataset. For now, we will use the same dataset we have used for training as a \*proxy \*for new unseen dataset. In practice, \*\*predict\_model \*\*function would be used iteratively, every time with a new unseen dataset.

```
predictions = **predict_model**(rf, data = diabetes)
```

![](https://cdn-images-1.medium.com/max/2200/1*TZwr8fI9cNqluSwnDa4IfA.png)

💡 predict\_model function can also predict a sequential chain of models which are created using [stack\_models](https://www.pycaret.org/stack-models) and [create\_stacknet](https://www.pycaret.org/classification/#create-stacknet) function.

💡 predict\_model function can also predict directly from the model hosted on AWS S3 using [deploy\_model](https://www.pycaret.org/deploy-model) function.

### 10. Deploy Model

One way to utilize the trained models to generate predictions on an unseen dataset is by using the predict\_model function in the same notebooks / IDE in which model was trained. However, making the prediction on an unseen dataset is an iterative process; depending on the use-case, the frequency of making predictions could be from real time predictions to batch predictions. PyCaret’s **deploy\_model** function allows deploying the entire pipeline including trained model on cloud from notebook environment.

```
**deploy_model**(model = rf, model_name = 'rf_aws', platform = 'aws', 
             authentication =  {'bucket'  : 'pycaret-test'})
```

### 11. Save Model / Save Experiment

Once training is completed the entire pipeline containing all preprocessing transformations and trained model object can be saved as a binary pickle file.

```
# creating model
adaboost = **create_model**('ada')

# saving model**
save_model**(adaboost, model_name = 'ada_for_deployment')
```

![](https://cdn-images-1.medium.com/max/2000/1*sW7Vn_mPiH-TWaJ3cZgE8Q.png)

You can also save the entire experiment consisting of all intermediary outputs as one binary file.

```
**save_experiment**(experiment_name = 'my_first_experiment')
```

![](https://cdn-images-1.medium.com/max/2000/1*GFLvTgyzESXgy1SytG45xQ.png)

💡 You can load saved model and saved experiment using \*\*load\_model \*\*and \*\*load\_experiment \*\*function available in all modules of PyCaret.

### 12. Next Tutorial

In the next tutorial, we will show how to consume a trained machine learning model in Power BI to generate batch predictions in a real production environment.

Please also see our beginner level notebooks for these modules:

[Regression](https://www.pycaret.org/reg101) [Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101)

### What’s in the development pipeline?

We are actively working on improving PyCaret. Our future development pipeline includes a new \*\*Time Series Forecasting \*\*module, Integration with \*\*TensorFlow \*\*and major improvements on scalability of PyCaret. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on website or leave a comment on our [GitHub](http://www.github.com/pycaret/) or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing ](https://www.pycaret.org/nlp)[Association Rule Mining](https://www.pycaret.org/association-rules)

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [Github Repository](http://www.github.com/pycaret/pycaret) [Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

Give us ⭐️ on our github repo if you like PyCaret.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).


# Announcing PyCaret 2.0

### Announcing PyCaret 2.0

#### by Moez Ali

![https://www.pycaret.org](https://cdn-images-1.medium.com/max/2126/1*oT-VYfpNDeKJ1L9vkpESdw.png)

We are excited to announce the second release of PyCaret today.

PyCaret is an open source, **low-code** machine learning library in Python that automates machine learning workflow. It is an end-to-end machine learning and model management tool that speeds up machine learning experiment cycle and makes you more productive.

In comparison with the other open source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few words only. This makes experiments exponentially fast and efficient.

See detailed [release notes](https://github.com/pycaret/pycaret/releases/tag/2.0) for PyCaret 2.0.

### **Why use PyCaret?**

![PyCaret 2.0 Features](https://cdn-images-1.medium.com/max/2066/1*wT0m1kx8WjY_P7hrM6KDbA.png)

### Installing PyCaret 2.0

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using virtual environment to avoid potential conflict with other libraries. See the following example code to create a ***conda*** \*\*\*environment \*\*\*and install pycaret within that conda environment:

```
**# create a conda environment **
conda create --name yourenvname python=3.6  

**# activate environment **
conda activate yourenvname  

**# install pycaret **
pip install **pycaret==2.0  **

**# create notebook kernel linked with the conda environment python -m **ipykernel install --user --name yourenvname --display-name "display-name"
```

If you are using Azure notebooks or Google Colab, run the following code to install PyCaret.

```
!pip install **pycaret==2.0**
```

All hard dependencies are automatically installed when you install PyCaret using pip. [Click here](https://github.com/pycaret/pycaret/blob/master/requirements.txt) to see the complete list of dependencies.

### 👉 Getting Started with PyCaret 2.0

The first step of any machine learning experiment in PyCaret is to set up an environment by importing the relevant module and initialize the \*\*setup function \*\*by passing dataframe and name of the target variable. See example code:

**Sample Output:**

![Output is truncated](https://cdn-images-1.medium.com/max/2000/1*di8zOe7rN7kWHO8t-6C6hg.png)

All the preprocessing transformations are applied within \*\*setup function. \*\*PyCaret provides over 20 different pre-processing transformation that can be defined within setup function. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing abilities.

![https://www.pycaret.org/preprocessing](https://cdn-images-1.medium.com/max/2000/1*EcfstE4cOIhazduR4iUX0w.png)

### 👉 **Compare Models**

This is the first step we recommend in any supervised machine learning task. This function trains all the models in the model library using default hyperparameters and evaluates performance metrics using cross validation. It returns the trained model object class. The evaluation metrics used are:

* \*\*For Classification: \*\*Accuracy, AUC, Recall, Precision, F1, Kappa, MCC
* \*\*For Regression: \*\*MAE, MSE, RMSE, R2, RMSLE, MAPE

Here are few ways you can use **compare\_models** function:

**Sample Output:**

![Sample output from compare\_models function](https://cdn-images-1.medium.com/max/2000/1*gUjKx0cQbpaWl226CzAdyw.png)

### 👉 **Create Model**

Create Model function trains a model using default hyperparameters and evaluates performance metrics using cross validation. This function is base to almost all other functions in PyCaret. It returns the trained model object class. Here are few ways you can use this function:

**Sample Output:**

![Sample output from create\_model function](https://cdn-images-1.medium.com/max/2000/1*NDwHzljCyqQpkH55ogHzTA.png)

To learn more about **create model** function, [click here](https://www.pycaret.org/create-model).

### 👉 Tune Model

Tune Model function tunes the hyperparameter of the model passed as an estimator. It uses Random grid search with pre-defined tuning grids that are fully customizable. Here are few ways you can use this function:

To learn more about **tune model** function, [click here](https://www.pycaret.org/tune-model).

### 👉 Ensemble Model

There are few functions available to ensemble base learners. **ensemble\_model**, \*\*blend\_models \*\*and \*\*stack\_models \*\*are three of them. Here are few ways you can use this function:

To learn more about ensemble models in PyCaret, [click here](https://www.pycaret.org/ensemble-model).

### 👉 Predict Model

As the name suggests, this function is used for inference / prediction. Here is how you can use it:

### 👉 Plot Model

Plot Model function is used to evaluate performance of the trained machine learning model. Here is an example:

![Sample output from plot\_model function](https://cdn-images-1.medium.com/max/2000/1*Do2ho2O_fg8w62VPuwVm7g.png)

[Click here](https://www.pycaret.org/plot-model) to learn more about different visualization in PyCaret.

Alternatively, you can use \*\*evaluate\_model \*\*function to see plots \*via \*the user interface within notebook.

![evaluate\_model function in PyCaret](https://cdn-images-1.medium.com/max/2560/1*AGsJlbX6bhCOG2r_uhvkKg.gif)

### 👉 Util functions

PyCaret 2.0 includes several new util functions that comes handy when managing your machine learning experiments with PyCaret. Some of them are shown below:

To see all new functions implemented in PyCaret 2.0, See [release notes](https://github.com/pycaret/pycaret/releases/tag/2.0).

### 👉 Experiment Logging

PyCaret 2.0 embeds MLflow tracking component as a backend API and UI for logging parameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results. Here is how you can log your experiment in PyCaret.

**Output (on localhost:5000)**

![https://localhost:5000](https://cdn-images-1.medium.com/max/3788/1*Z_08utFByIK_9nsps3rctA.png)

### 👉 Putting it all together — Create your own AutoML software

Using all the functions, let’s create a simple command line software that will train multiple models with default parameters, tune hyperparameters of top candidate models, try different ensembling techniques and returns / saves the best model. Here is the command line script:

This script will dynamically select and saves the best model. In just few lines of code you have developed your own Auto ML software with a full fledged logging system and even a UI presenting beautiful leaderboard.

There is no limit to what you can achieve using the light weight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our github repo if you like PyCaret.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

### Important Links

[Release Notes for PyCaret 2.0](https://github.com/pycaret/pycaret/releases/tag/2.0) [User Guide / Documentation](https://www.pycaret.org/guide)[ ](https://github.com/pycaret/pycaret/releases/tag/2.0)[Github](http://www.github.com/pycaret/pycaret) [Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)


# 5 things you dont know about PyCaret

### 5 things you don’t know about PyCaret

#### by Moez Ali

![From the author of PyCaret](https://cdn-images-1.medium.com/max/2000/1*1HEakzOhZRd21FfAT3TyZw.png)

### PyCaret

PyCaret is an open source machine learning library in Python to train and deploy supervised and unsupervised machine learning models in a **low-code** environment. It is known for its ease of use and efficiency.

In comparison with the other open source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with a few words only.

If you haven’t used PyCaret before or would like to learn more, a good place to start is [here](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46).

> ## “After talking to many data scientists who use PyCaret on a daily basis, I have shortlisted 5 features of PyCaret that are lesser known but they extremely powerful.” — Moez Ali

### 👉You can tune “n parameter” in unsupervised experiments

In unsupervised machine learning the “n parameter” i.e. the number of clusters for clustering experiments, the fraction of the outliers in anomaly detection, and the number of topics in topic modeling, is of fundamental importance.

When the eventual objective of the experiment is to predict an outcome (classification or regression) using the results from the unsupervised experiments, then the tune\_model() function in the \*\*pycaret.clustering **module**, \*\*the **pycaret.anomaly module,** and the \*\*pycaret.nlp \*\*module \*\*\*\*comes in very handy.

To understand this, let’s see an example using the “[Kiva](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/kiva.csv)” dataset.

![](https://cdn-images-1.medium.com/max/2000/1*-161ThHHhI7lMVHuY4jbsA.png)

This is a micro-banking loan dataset where each row represents a borrower with their relevant information. Column ‘en’ captures the loan application text of each borrower, and the column ‘status’ represents whether the borrower defaulted or not (default = 1 or no default = 0).

You can use \*\*tune\_model \*\*function in \*\*pycaret.nlp \*\*to optimize \*\*num\_topics \*\*parameter based on the target variable of supervised experiment (i.e. predicting the optimum number of topics required to improve the prediction of the final target variable). You can define the model for training using **estimator** parameter (‘xgboost’ in this case). This function returns a trained topic model and a visual showing supervised metrics at each iteration.

![](https://cdn-images-1.medium.com/max/2314/1*RIOVzRCYsA-r-c1Iy7x_5w.png)

### 👉You can improve results from hyperparameter tuning by increasing “n\_iter”

The \*\*tune\_model \*\*function in the \*\*pycaret.classification \*\*module and the **pycaret.regression** module employs random grid search over pre-defined grid search for hyper-parameter tuning. Here the default number of iterations is set to 10.

Results from \*\*tune\_model \*\*may not necessarily be an improvement on the results from the base models created using \*\*create\_model. \*\*Since the grid search is random, you can increase the \*\*n\_iter \*\*parameter to improve the performance. See example below:

![](https://cdn-images-1.medium.com/max/2000/1*LRu2R2f4rXYkOrWVC6ul5A.png)

### 👉You can programmatically define data types in the setup function

When you initialize the \*\*setup **function**, \*\*you will be asked to confirm data types through a user input. More often when you run the scripts as a part of workflows or execute it as remote kernels (for e.g. Kaggle Notebooks), then in such case, it is required to provide the data types programmatically rather than through the user input box.

See example below using “[insurance](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/insurance.csv)” dataset.

![](https://cdn-images-1.medium.com/max/2000/1*q2WFe3JgZ1SxSkiuuvonKQ.png)

the **silent** parameter is set to True to avoid input, \*\*categorical\_features \*\*parameter takes the name of categorical columns as string, and \*\*numeric\_features \*\*parameter takes the name of numeric columns as a string.

### 👉You can ignore certain columns for model building

On many occasions, you have features in dataset that you do not necessarily want to remove but want to ignore for training a machine learning model. A good example would be a clustering problem where you want to ignore certain features during cluster creation but later you need those columns for analysis of cluster labels. In such cases, you can use the \*\*ignore\_features \*\*parameter within the \*\*setup \*\*to ignore such features.

In the example below, we will perform a clustering experiment and we want to ignore **‘Country Name’** and **‘Indicator Name’**.

![](https://cdn-images-1.medium.com/max/2000/1*0xcKweKh77A-vgzb5u5_mw.png)

### 👉You can optimize the probability threshold % in binary classification

In classification problems, the cost of **false positives** is almost never the same as the cost of **false negatives**. As such, if you are optimizing a solution for a business problem where **Type 1** and **Type 2** errors have a different impact, you can optimize your classifier for a probability threshold value to optimize the custom loss function simply by defining the cost of true positives, true negatives, false positives and false negatives separately. By default, all classifiers have a threshold of 0.5.

See example below using “[credit](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/credit.csv)” dataset.

![](https://cdn-images-1.medium.com/max/2000/1*oCsUyp91pSJSDdzi-ho6QA.png)

You can then pass \*\*0.2 \*\*as \*\*probability\_threshold \*\*parameter in \*\*predict\_model \*\*function to use 0.2 as a threshold for classifying positive class. See example below:

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the data science community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Classification](https://www.pycaret.org/clf101) [Regression](https://www.pycaret.org/reg101) [Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# Build and deploy your first machine learning web app

### Build and deploy your first machine learning web app

#### A beginner’s guide to train and deploy machine learning pipelines in Python using PyCaret

#### by Moez Ali

![](https://cdn-images-1.medium.com/max/2000/1*NWklye0cNThqH_cTImozlA.png)

In our [last post](https://towardsdatascience.com/machine-learning-in-power-bi-using-pycaret-34307f09394a) we demonstrated how to train and deploy machine learning models in Power BI using [PyCaret](https://www.pycaret.org/). If you haven’t heard about PyCaret before, please read our [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to get a quick start.

In this tutorial we will use PyCaret to develop a **machine learning pipeline,** that will include preprocessing transformations and a regression model to predict patient hospitalization charges based on demographic and basic patient health risk metrics such as age, BMI, smoking status etc.

### 👉 What you will learn in this tutorial

* What is a deployment and why do we deploy machine learning models.
* Develop a machine learning pipeline and train models using PyCaret.
* Build a simple web app using a Python framework called ‘Flask’.
* Deploy a web app on ‘Heroku’ and see your model in action.

### 💻 What tools we will use in this tutorial?

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python to train and deploy machine learning pipelines and models in production. PyCaret can be installed easily using pip.

```
# for Jupyter notebook on your local computer
pip install **pycaret**

# for azure notebooks and google colab
!pip install **pycaret**
```

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a framework that allows you to build web applications. A web application can be a commercial website, a blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models. If you don’t have Flask installed, you can use pip to install it.

```
# install flask
pip install **Flask**
```

### GitHub

[GitHub](https://www.github.com/) is a cloud-based service that is used to host, manage and control code. Imagine you are working in a large team where multiple people (sometime hundreds of them) are making changes. PyCaret is itself an example of an open-source project where hundreds of community developers are continuously contributing to source code. If you haven’t used GitHub before, you can [sign up](https://github.com/join) for a free account.

### Heroku

[Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables the deployment of web apps based on a managed container system, with integrated data services and a powerful ecosystem. In simple words, this will allow you to take the application from your local machine to the cloud so that anybody can access it using a Web URL. In this tutorial we have chosen Heroku for deployment as it provides free resource hours when you [sign up](https://signup.heroku.com/) for new account.

![Machine Learning Workflow (from Training to Deployment on PaaS)](https://cdn-images-1.medium.com/max/2000/1*GCRVoOwIKL_AhmrwOtQwaA.png)

### Why Deploy Machine Learning Models?

The deployment of machine learning models is the process of making models available in production where web applications, enterprise software and APIs can consume the trained model by providing new data points and generating predictions.

Normally machine learning models are built so that they can be used to predict an outcome (binary value i.e. 1 or 0 for [Classification](https://www.pycaret.org/classification), continuous values for [Regression](https://www.pycaret.org/regression), labels for [Clustering](https://www.pycaret.org/clustering) etc. There are two broad ways of generating predictions (i) predict by batch; and (ii) predict in real-time. In our [last tutorial](https://towardsdatascience.com/machine-learning-in-power-bi-using-pycaret-34307f09394a) we demonstrated how to deploy machine learning model in Power BI and predict by batch. In this tutorial we will see how to deploy a machine learning model to predict in real-time.

### Business Problem

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/0*10e8RTwI5t0Wi8fg.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build a web application where demographic and health information of a patient is entered in a web form to predict charges.

### Tasks

* Train and validate models and develop a machine learning pipeline for deployment.
* Build a basic HTML front-end with an input form for independent variables (age, sex, bmi, children, smoker, region).
* Build a back-end of the web application using a Flask Framework.
* Deploy the web app on Heroku. Once deployed, it will become publicly available and can be accessed via Web URL.

### 👉 Task 1 — Model Training and Validation

Training and model validation are performed in Integrated Development Environment (IDE) or Notebook either on your local machine or on cloud. In this tutorial we will use PyCaret in Jupyter Notebook to develop machine learning pipeline and train regression models. If you haven’t used PyCaret before, [click here](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more about PyCaret or see [Getting Started Tutorials](https://www.pycaret.org/tutorial) on our [website](https://www.pycaret.org/).

In this tutorial, we have performed two experiments. The first experiment is performed with default preprocessing settings in PyCaret (missing value imputation, categorical encoding etc). The second experiment has some additional preprocessing tasks such as scaling and normalization, automatic feature engineering and binning continuous data into intervals. See the setup example for the second experiment:

```
# Experiment No. 2

from **pycaret.regression** import *****

r2 = **setup**(data, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True,
           feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'])
```

![Comparison of information grid for both experiments](https://cdn-images-1.medium.com/max/2000/0*lA_5MECr5Onj0nRS.png)

The magic happens with only a few lines of code. Notice that in **Experiment 2** the transformed dataset has 62 features for training derived from only 7 features in the original dataset. All of the new features are the result of transformations and automatic feature engineering in PyCaret.

![Columns in dataset after transformation](https://cdn-images-1.medium.com/max/2000/0*c6jeng5IXupSzJtE.png)

Sample code for model training and validation in PyCaret:

```
# Model Training and Validation 
lr = **create_model**('lr')
```

![10 Fold cross-validation of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2276/0*qGM8XwQdUpU5YK2z.png)

Notice the impact of transformations and automatic feature engineering. The R2 has increased by 10% with very little effort. We can compare the **residual plot** of linear regression model for both experiments and observe the impact of transformations and feature engineering on the \*\*heteroskedasticity \*\*of model.

```
# plot residuals of trained model**
plot_model**(lr, plot = 'residuals')
```

![Residual Plot of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2876/0*FJDkF4CzHtwfGlbg.png)

Machine learning is an \*iterative \*process. Number of iterations and techniques used within are dependent on how critical the task is and what the impact will be if predictions are wrong. The severity and impact of a machine learning model to predict a patient outcome in real-time in the ICU of a hospital is far more than a model built to predict customer churn.

In this tutorial, we have performed only two iterations and the linear regression model from the second experiment will be used for deployment. At this stage, however, the model is still only an object within notebook. To save it as a file that can be transferred to and consumed by other applications, run the following code:

```
# save transformation pipeline and model 
**save_model**(lr, model_name = 'c:/*username*/ins/deployment_28042020')
```

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/0*ZY7Ep3vsER-6G7ug.png)

We have finished our first task of training and selecting a model for deployment. The final machine learning pipeline and linear regression model is now saved as a file in the local drive under the location defined in the \*\*save\_model() \*\*function. (In this example: c:/*username*/ins/deployment\_28042020.pkl).

### 👉 Task 2 — Building Web Application

Now that our machine learning pipeline and model are ready we will start building a web application that can connect to them and generate predictions on new data in real-time. There are two parts of this application:

* Front-end (designed using HTML)
* Back-end (developed using Flask in Python)

### Front-end of Web Application

Generally, the front-end of web applications are built using HTML which is not the focus of this article. We have used a simple HTML template and a CSS style sheet to design an input form. Here’s the HTML snippet of the front-end page of our web application.

![Code snippet from home.html file](https://cdn-images-1.medium.com/max/2388/1*t0a5Ev7oFJf73oIY8lkHZQ.png)

You don’t need to be an expert in HTML to build simple applications. There are numerous free platforms that provide HTML and CSS templates as well as enable building beautiful HTML pages quickly by using a drag and drop interface.

\*\*CSS Style Sheet \*\*CSS (also known as Cascading Style Sheets) describes how HTML elements are displayed on a screen. It is an efficient way of controlling the layout of your application. Style sheets contain information such as background color, font size and color, margins etc. They are saved externally as a .css file and is linked to HTML but including 1 line of code.

![Code snippet from home.html file](https://cdn-images-1.medium.com/max/2392/1*2CecMn4-O-slFc6Tf1BK1w.png)

### Back-end of Web Application

The back-end of a web application is developed using a Flask framework. For beginner’s it is intuitive to consider Flask as a library that you can import just like any other library in Python. See the sample code snippet of our back-end written using a Flask framework in Python.

![Code snippet from app.py file](https://cdn-images-1.medium.com/max/2444/0*2KpsfiiecB5mCtab.png)

If you remember from the Step 1 above we have finalized linear regression model that was trained on 62 features that were automatically engineered by PyCaret. However, the front-end of our web application has an input form that collects only the six features i.e. age, sex, bmi, children, smoker, region.

How do we transform 6 features of a new data point in real-time into 62 features on which model was trained? With a sequence of transformations applied during model training, coding becomes increasingly complex and time-taking task.

In PyCaret all transformations such as categorical encoding, scaling, missing value imputation, feature engineering and even feature selection are automatically executed in real-time before generating predictions.

> ## *Imagine the amount of code you would have had to write to apply all the transformations in strict sequence before you could even use your model for predictions. In practice, when you think of machine learning, you should think about the entire ML pipeline and not just the model.*

\*\*Testing App \*\*One final step before we publish the application on Heroku is to test the web app locally. Open Anaconda Prompt and navigate to folder where **‘app.py’** is saved on your computer. Run the python file with below code:

```
python **app.py**
```

![Output in Anaconda Prompt when app.py is executed](https://cdn-images-1.medium.com/max/2204/0*NvcdEyGUoUWWoJKZ.png)

Once executed, copy the URL into a browser and it should open a web application hosted on your local machine (127.0.0.1). Try entering test values to see if the predict function is working. In the example below, the expected bill for a 19 year old female smoker with no children in the southwest is $20,900.

![Web application opened on local machine](https://cdn-images-1.medium.com/max/3780/0*GBP1kfSwpBzstWzI.png)

Congratulations! you have now built your first machine learning app. Now it’s time to take this application from your local machine into the cloud so other people can use it with a Web URL.

### 👉 Task 3 — Deploy the Web App on Heroku

Now that the model is trained, the machine learning pipeline is ready, and the application is tested on our local machine, we are ready to start our deployment on Heroku. There are couple of ways to upload your application source code onto Heroku. The simplest way is to link a GitHub repository to your Heroku account.

If you would like to follow along you can fork this [repository](https://github.com/pycaret/deployment-heroku) from GitHub. If you don’t know how to fork a repo, please [read this](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) official GitHub tutorial.

![https://www.github.com/pycaret/deployment-heroku](https://cdn-images-1.medium.com/max/2524/0*GPOio0x0TnQFr8r8.png)

By now you are familiar with all the files in repository shown above except for two files i.e. ‘**requirements.txt’** and ‘**Procfile’.**

![requirements.txt](https://cdn-images-1.medium.com/max/2440/0*XHMUGa90vc6csKfO.png)

\*\*requirements.txt \*\*file is a text file containing the names of the python packages required to execute the application. If these packages are not installed in the environment application is running, it will fail.

![Procfile](https://cdn-images-1.medium.com/max/2470/0*NFbZtaStgESRUIol.png)

\*\*Procfile \*\*is simply one line of code that provides startup instructions to web server that indicate which file should be executed first when somebody logs into the application. In this example the name of our application file is ‘\*\*app.py’ \*\*and the name of the application is also ‘**app’**. *(hence app:app)*

Once all the files are uploaded onto the GitHub repository, we are now ready to start deployment on Heroku. Follow the steps below:

**Step 1 — Sign up on heroku.com and click on ‘Create new app’**

![Heroku Dashboard](https://cdn-images-1.medium.com/max/3108/0*MXhm58jzLVET5Xa4.png)

**Step 2 — Enter App name and region**

![Heroku — Create new app](https://cdn-images-1.medium.com/max/2000/0*8Lu1Fc9A7iGnVJCm.png)

**Step 3 — Connect to your GitHub repository where code is hosted**

![Heroku — Connect to GitHub](https://cdn-images-1.medium.com/max/3092/0*VyAQvI2kDr2SsXYz.png)

**Step 4 — Deploy branch**

![Heroku — Deploy Branch](https://cdn-images-1.medium.com/max/3022/0*A5Tg_Qt5cZ6aLl92.png)

**Step 5 — Wait 5–10 minutes and BOOM**

![Heroku — Successful deployment](https://cdn-images-1.medium.com/max/3078/0*TFPIem6Q5k6DKszI.png)

App is published to URL: <https://pycaret-insurance.herokuapp.com/>

![https://pycaret-insurance.herokuapp.com/](https://cdn-images-1.medium.com/max/3772/0*Fr199orKNCkPMBSf.png)

There is one last thing to see before we end the tutorial.

So far we have built and deployed a web application that works with our machine learning pipeline. Now imagine that you already have an enterprise application in which you want to integrate predictions from your model. What you need is a web service where you can make an API call with input data points and get the predictions back. To achieve this we have created the ***predict\_api*** function in our **‘app.py’** file. See the code snippet:

![Code snippet from app.py file (back-end of web app)](https://cdn-images-1.medium.com/max/2000/0*JvwXvC3bBpKaPTE_.png)

Here’s how you can use this web service in Python using the requests library:

```
import **requests**url = 'https://pycaret-insurance.herokuapp.com/predict_api'pred = **requests.post(**url,json={'age':55, 'sex':'male', 'bmi':59, 'children':1, 'smoker':'male', 'region':'northwest'})**print**(pred.json())
```

![Make a request to a published web service to generate predictions in a Notebook](https://cdn-images-1.medium.com/max/2474/0*a9T8yMRXwymlccdr.png)

### Next Tutorial

In the next tutorial for deploying machine learning pipelines, we will dive deeper into deploying machine learning pipelines using docker containers. We will demonstrate how to easily deploy and run containerized machine learning applications on Linux.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### What’s in the development pipeline?

We are actively working on improving PyCaret. Our future development pipeline includes a new \*\*Time Series Forecasting \*\*module, integration with \*\*TensorFlow, \*\*and major improvements on the scalability of PyCaret. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Build your own AutoML in Power BI using PyCaret

### Build your own AutoML in Power BI using PyCaret 2.0

#### by Moez Ali

![PyCaret — An open source, low-code machine learning library in Python](https://cdn-images-1.medium.com/max/2664/1*Kx9YUt0hWPhU_a6h2vM5qA.png)

### **PyCaret 2.0**

Last week we have announced [PyCaret 2.0](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e), an open source, **low-code** machine learning library in Python that automates machine learning workflow. It is an end-to-end machine learning and model management tool that speeds up machine learning experiment cycle and helps data scientists become more efficient and productive.

In this post we present a **step-by-step tutorial** on how PyCaret can be used to build an Automated Machine Learning Solution within [Power BI](https://powerbi.microsoft.com/en-us/), thus allowing data scientists and analysts to add a layer of machine learning to their Dashboards without any additional license or software costs. PyCaret is an open source and \*\*free to use \*\*Python library that comes with a wide range of functions that are built to work within Power BI.

By the end of this article you will learn how to implement the following in Power BI:

* Setting up Python conda environment and install pycaret==2.0.
* Link the newly created conda environment with Power BI.
* Build your first AutoML solution in Power BI and present the performance metrics on dashboard.
* Productionalize / deploy your AutoML solution in Power BI.

### Microsoft Power BI

Power BI is a business analytics solution that lets you visualize your data and share insights across your organization, or embed them in your app or website. In this tutorial, we will use [Power BI Desktop](https://powerbi.microsoft.com/en-us/downloads/) for machine learning by importing the PyCaret library into Power BI.

### What is Automated Machine Learning?

Automated machine learning (AutoML) is the process of automating the time consuming, iterative tasks of machine learning. It allows data scientists and analysts to build machine learning models with efficiency while sustaining the model quality. The final goal of any AutoML solution is to finalize the best model based on some performance criteria.

Traditional machine learning model development process is resource-intensive, requiring significant domain knowledge and time to produce and compare dozens of models. With automated machine learning, you’ll accelerate the time it takes to get production-ready ML models with great ease and efficiency.

### **How Does PyCaret works?**

PyCaret is a workflow automation tool for supervised and unsupervised machine learning. It is organized into six modules and each module has a set of functions available to perform some specific action. Each function takes an input and returns an output, which in most cases is a trained machine learning model. Modules available as of the second release are:

* [Classification](https://www.pycaret.org/classification)
* [Regression](https://www.pycaret.org/regression)
* [Clustering](https://www.pycaret.org/clustering)
* [Anomaly Detection](https://www.pycaret.org/anomaly-detection)
* [Natural Language Processing](https://www.pycaret.org/nlp)
* [Association Rule Mining](https://www.pycaret.org/association-rules)

All modules in PyCaret supports data preparation (over 25+ essential preprocessing techniques, comes with a huge collection of untrained models & support for custom models, automatic hyperparameter tuning, model analysis and interpretability, automatic model selection, experiment logging and easy cloud deployment options.

![https://www.pycaret.org/guide](https://cdn-images-1.medium.com/max/2066/1*wT0m1kx8WjY_P7hrM6KDbA.png)

To learn more about PyCaret, [click here](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e) to read our official release announcement.

If you want to get started in Python, [click here](https://github.com/pycaret/pycaret/tree/master/examples) to see a gallery of example notebooks to get started.

> ## “PyCaret is democratizing machine learning and the use of advanced analytics by providing free, open source, and low-code machine learning solution for business analysts, domain experts, citizen data scientists, and experienced data scientists”.

### Before we start

If you are using Python for the first time, installing Anaconda Distribution is the easiest way to get started. [Click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/products/individual](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

#### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we need to create a virtual environment and install pycaret. This is a three-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Creating an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and execute the following code:

```
conda create --name **myenv** python=3.7
```

![Anaconda Prompt — Creating an environment](https://cdn-images-1.medium.com/max/2194/1*2D9jKJPM4eAy1-7lvcLlJQ.png)

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Installing PyCaret**

Execute the following code in Anaconda Prompt:

```
pip install **pycaret==2.0**
```

Installation may take 15–20 minutes. If you are having issues with installation, please see our [GitHub](https://www.github.com/pycaret/pycaret) page for known issues and resolutions.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Setting up a Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\AppData\Local\Continuum\anaconda3\envs\myenv

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*zQMKuyEk8LGrOPE-NByjrg.png)

### **👉 Lets get started**

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting the patient charges using the demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To train and select the best performing regression model that predicts patient charges based on the other variables in the dataset i.e. age, sex, bmi, children, smoker, and region.

### 👉 Step 1 — Load the dataset

You can load dataset directly from out GitHub by going to Power BI Desktop → Get Data → Web

Link to dataset: <https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/insurance.csv>

![Power BI Desktop → Get Data → Web](https://cdn-images-1.medium.com/max/2000/1*zZjZzF_TJudoThDCBGK3fQ.png)

Create a duplicate dataset in Power Query:

![Power Query → Create a duplicate dataset](https://cdn-images-1.medium.com/max/3436/1*mU8tl4P89WKMC__k6rM-Vw.png)

### 👉 Step 2— Run AutoML as Python Script

Run the following code in Power Query (Transform → Run Python script):

```
**# import regression module**
from pycaret.regression import *

**# init setup**
reg1 = setup(data=dataset, target = 'charges', silent = True, html = False)

**# compare models**
best_model = compare_models()

**# finalize best model
**best = finalize_model(best_model)

**# save best model**
save_model(best, 'c:/users/moezs/best-model-power')

**# return the performance metrics df
**dataset = pull()
```

![Script in Power Query](https://cdn-images-1.medium.com/max/2000/1*FOxy83SH1uy8pFLJT6sa3w.png)

The first two line of code is for importing the relevant module and initializing the setup function. The setup function performs several imperative steps required in machine learning such as cleaning missing values (if any), splitting the data into train and test, setting up cross validation strategy, defining metrics, performing algorithm-specific transformations etc.

The magic function that trains multiple models, compares and evaluates performance metrics is \*\*compare\_models. \*\*It returns the best model based on ‘\*\*sort’ \*\*parameter that can be defined inside compare\_models. By default, it uses ‘R2’ for regression use-case and ‘Accuracy’ for classification use-case.

Rest of the lines are for finalizing the best model returned through compare\_models and saving it as a pickle file in your local diretory. Last line returns the dataframe with details of model trained and their performance metrics.

Output:

![Output from Python Script](https://cdn-images-1.medium.com/max/3822/1*6CSYQDLfQUZeTtYwNllFSw.png)

With just few lines we have trained over 20 models and the table presents the performance metrics based on 10 fold cross validation.

Top performing model **Gradient Boosting Regressor** will be saved along with the entire transformation pipeline as a pickle file in your local directory. This file can be consumed later to generate predictions on a new dataset (see step 3 below).

![Transformation Pipeline and Model saved as a pickle file](https://cdn-images-1.medium.com/max/2000/1*euQRJQVAVvP2X5ASNWjjOg.png)

PyCaret works on the idea of modular automation. As such if you have more resources and time for training you can extend the script to perform hyperparameter tuning, ensembling, and other available modeling techniques. See example below:

```
**# import regression module**
from pycaret.regression import *

**# init setup**
reg1 = setup(data=dataset, target = 'charges', silent = True, html = False)

**# compare models**
top5 = compare_models(n_select = 5)
results = pull()

**# tune top5 models
**tuned_top5 = [tune_model(i) for i in top5]

**# select best model
**best = automl()

**# save best model**
save_model(best, 'c:/users/moezs/best-model-power')

**# return the performance metrics df
**dataset = results
```

We have now returned top 5 models instead of the one highest performing model. We have then created a list comprehension (loop) to tune hyperparameters of top candidate models and then finally \*\*automl function \*\*selects the single best performing model which is then saved as a pickle file (Note that we didn’t use \*\*finalize\_model \*\*this time because automl function returns the finalized model).

### **Sample Dashboard**

Sample dashboard is created. PBIX file is [uploaded here](https://github.com/pycaret/pycaret-powerbi-automl).

![Dashboard created using PyCaret AutoML results](https://cdn-images-1.medium.com/max/2664/1*Kx9YUt0hWPhU_a6h2vM5qA.png)

### 👉 Step 3 — Deploy Model to generate predictions

Once we have a final model saved as a pickle file we can use it to predict charges on the new dataset.

### **Loading new dataset**

For demonstration purposes, we will load the same dataset again and remove the ‘charges’ column from the dataset. Execute the following code as a Python script in Power Query to get the predictions:

```
**# load functions from regression module**
from pycaret.regression import load_model, predict_model

**# load model in a variable
**model = load_model(‘c:/users/moezs/best-model-powerbi’)

**# predict charges
**dataset = predict_model(model, data=dataset)
```

Output :

![predict\_model function output in Power Query](https://cdn-images-1.medium.com/max/3840/1*ZYWjwtu4njS7f7XMp90ofg.png)

### **Deploy on Power BI Service**

When you publish a Power BI report with Python scripts to the service, these scripts will also be executed when your data is refreshed through the on-premises data gateway.

To enable this, you must ensure that the Python runtime with the dependent Python packages are also installed on the machine hosting your personal gateway. Note, Python script execution is not supported for on-premises data gateways shared by multiple users. [Click here](https://powerbi.microsoft.com/en-us/blog/python-visualizations-in-power-bi-service/) to read more about this.

PBIX files used in this tutorial is uploaded on this GitHub Repository: <https://github.com/pycaret/pycaret-powerbi-automl>

If you would like to learn more about PyCaret 2.0, read this [announcement](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e).

If you have used PyCaret before, you might be interested in [release notes](https://github.com/pycaret/pycaret/releases/tag/2.0) for current release.

There is no limit to what you can achieve using this light-weight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our github repo.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

### **You may also be interested it:**

[Machine Learning in Power BI using PyCaret](https://towardsdatascience.com/machine-learning-in-power-bi-using-pycaret-34307f09394a) [Build your first Anomaly Detector in Power BI using PyCaret](https://towardsdatascience.com/build-your-first-anomaly-detector-in-power-bi-using-pycaret-2b41b363244e) [How to implement Clustering in Power BI using PyCaret](https://towardsdatascience.com/how-to-implement-clustering-in-power-bi-using-pycaret-4b5e34b1405b) [Topic Modeling in Power BI using PyCaret](https://towardsdatascience.com/topic-modeling-in-power-bi-using-pycaret-54422b4e36d6)

### Important Links

[Blog](https://medium.com/@moez_62905) [Release Notes for PyCaret 2.0](https://github.com/pycaret/pycaret/releases/tag/2.0) [User Guide / Documentation](https://www.pycaret.org/guide)[ ](https://github.com/pycaret/pycaret/releases/tag/2.0)[Github](http://www.github.com/pycaret/pycaret) [Stackoverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)


# Deploy ML Pipeline on Google Kubernetes

### Deploy Machine Learning Pipeline on Google Kubernetes Engine

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy ML pipeline on Google Kubernetes Engine](https://cdn-images-1.medium.com/max/2000/1*P-JjI7MXq6UJV9Xab-B9qg.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) on deploying a machine learning pipeline in the cloud, we demonstrated how to develop a machine learning pipeline in PyCaret, containerize it with Docker and serve as a web app using Microsoft Azure Web App Services. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will use the same machine learning pipeline and Flask app that we built and deployed previously. This time we will demonstrate how to containerize and deploy a machine learning pipeline on Google Kubernetes Engine.

### 👉 Learning Goals of this Tutorial

* Learn what is a Container, what is Docker, what is Kubernetes, and what is Google Kubernetes Engine?
* Build a Docker image and upload it on Google Container Registry (GCR).
* Create clusters and deploy a machine learning pipeline with a Flask app as a web service.
* See a web app in action that uses a trained machine learning pipeline to predict new data points in real-time.

Previously we demonstrated [how to deploy a ML pipeline on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) and [how to deploy a ML pipeline on Azure Web Services with a Docker container.](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)

This tutorial will cover the entire workflow starting from building a docker image, uploading it onto Google Container Registry and then deploying the pre-trained machine learning pipeline and Flask app onto Google Kubernetes Engine (GKE).

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install pycaret
```

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a framework that allows you to build web applications. A web application can be a commercial website, blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models. If you don’t have Flask installed, you can use pip to install it.

### Google Cloud Platform

Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail and YouTube. If you do not have an account with GCP, you can sign-up [here](https://console.cloud.google.com/getting-started). If you are signing up for the first time you will get free credits for 1 year.

### Let’s get started.

Before we get into Kubernetes, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, he or she should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → Programing language such as Python and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

> What’s Docker then?

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

Docker is a company that provides software (also called Docker) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/) that provides container solution.

Now that you understand containers and docker specifically, let’s understand what Kubernetes is all about.

### What is Kubernetes?

Kubernetes is a powerful open-source system developed by Google back in 2014, for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines. It is a platform designed to completely manage the life cycle of containerized applications.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/23216/0*2ZayMwt1Un8-9ZFA)

### Features

✔️ \*\*Load Balancing: \*\*Automatically distributes the load between containers.

✔️ \*\*Scaling: \*\*Automatically scale up or down by adding or removing containers when demand changes such as peak hours, weekends and holidays.

✔️ \*\*Storage: \*\*Keeps storage consistent with multiple instances of an application.

✔️ **Self-healing** Automatically restarts containers that fail and kills containers that don’t respond to your user-defined health check.

✔️ \*\*Automated Rollouts \*\*you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all of their resources to the new container.

### Why do you need Kubernetes if you have Docker?

Imagine a scenario where you have to run multiple docker containers on multiple machines to support an enterprise level ML application with varied workloads during day and night. As simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, and deal with failed containers or hardware. This is the problem Kubernetes is solving by allowing large numbers of containers to work together in harmony, reducing the operational burden.

> ## It’s a mistake to compare \*\*Docker with Kubernetes. \*\*These are two different technologies. Docker is a software that allows you to containerize applications while Kubernetes is a container management system that allows to create, scale and monitor hundreds and thousands of containers.

In the lifecycle of any application, Docker is used for packaging the application at the time of deployment, while kubernetes is used for rest of the life for managing the application.

![Lifecycle of an application deployed through Kubernetes / Docker](https://cdn-images-1.medium.com/max/3200/1*dBJjxZrfdMppXhdwjZLX6w.png)

### What is Google Kubernetes Engine?

Google Kubernetes Engine is implementation of *Google’s open source Kubernetes* on Google Cloud Platform. Simple!

Other popular alternatives to GKE are [Amazon ECS](https://aws.amazon.com/ecs/) and [Microsoft Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/).

### One final time, do you understand this?

* \*\*A Container \*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.
* \*\*Docker \*\*is a software used for building and managing containers.
* \*\*Kubernetes \*\*is an open-source system for managing containerized applications in a clustered environment.
* **Google Kubernetes Engine** is an implementation of the open source Kubernetes framework on Google Cloud Platform.

In this tutorial we will use Google Kubernetes Engine. In order to follow along, you must have a Google Cloud Platform account. [Click here](https://console.cloud.google.com/getting-started) to sign-up for free.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train and develop a machine learning pipeline for deployment.
* Build a web app using a Flask framework. It will use the trained ML pipeline to generate predictions on new data points in real-time.
* Build a docker image and upload a container onto Google Container Registry (GCR).
* Create clusters and deploy the app on Google Kubernetes Engine.

Since we have already covered the first two tasks in our initial tutorial, we will quickly recap them and then focus on the remaining items in the list above. If you are interested in learning more about developing a machine learning pipeline in Python using PyCaret and building a web app using a Flask framework, please read [this tutorial](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99).

### 👉 Develop a Machine Learning Pipeline

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*P7EXfIxqZZGrpeLgDdk1vQ.png)

### 👉 Build a Web Application

This tutorial is not focused on building a Flask application. It is only discussed here for completeness. Now that our machine learning pipeline is ready we need a web application that can connect to our trained pipeline to generate predictions on new data points in real-time. We have created the web application using Flask framework in Python. There are two parts of this application:

* Front-end (designed using HTML)
* Back-end (developed using Flask)

This is how our web application looks:

![Web application on local machine](https://cdn-images-1.medium.com/max/3780/1*tc_6S8NztYKB85rPUJd1uQ.png)

If you haven’t followed along so far, no problem. You can simply fork this [repository](https://github.com/pycaret/pycaret-deployment-google) from GitHub. This is how your project folder should look at this point:

![https://www.github.com/pycaret/pycaret-deployment-google](https://cdn-images-1.medium.com/max/3796/1*CcId22jB-BMCen8o1hWNdQ.png)

Now that we have a fully functional web application, we can start the process of containerizing and deploying the app on Google Kubernetes Engine.

### 10-steps to deploy a ML pipeline on Google Kubernetes Engine:

#### 👉 Step 1 — Create a new project in GCP Console

Sign-in to your GCP console and go to Manage Resources

![Google Cloud Platform Console → Manage Resources](https://cdn-images-1.medium.com/max/3832/1*OS16COUUns7uBnpyUxH9-w.png)

Click on **Create New Project**

![Google Cloud Platform Console → Manage Resources → Create New Project](https://cdn-images-1.medium.com/max/3834/1*QJz8fITeJJWP44yPm2v4vQ.png)

#### 👉 Step 2 — Import Project Code

Click the \*\*Activate Cloud Shell \*\*button at the top of the console window to open the Cloud Shell.

![Google Cloud Platform (Project Info Page)](https://cdn-images-1.medium.com/max/3834/1*Mbcd4RlkCcz98Pbf4KSUAA.png)

Execute the following code in Cloud Shell to clone the GitHub repository used in this tutorial.

```
git clone https://github.com/pycaret/pycaret-deployment-google.git
```

![git clone https://github.com/pycaret/pycaret-deployment-google.git](https://cdn-images-1.medium.com/max/3838/1*g_RQ30jDG4UsyS84mh-qrw.png)

#### 👉 Step 3— Set Project ID Environment Variable

Execute the following code to set the PROJECT\_ID environment variable.

```
export PROJECT_ID=**pycaret-kubernetes-demo**
```

*pycaret-kubernetes-demo* is the name of the project we chose in step 1 above.

#### 👉 Step 4— Build the docker image

Build the docker image of the application and tag it for uploading by executing the following code:

```
docker build -t gcr.io/${PROJECT_ID}/insurance-app:v1 .
```

![Message returned when docker build is successful](https://cdn-images-1.medium.com/max/3834/1*Zo7_W7pG6JhFvHbzyQeEsA.png)

You can check the available images by running the following code:

```
docker images
```

![Output of “docker images” command on Cloud Shell](https://cdn-images-1.medium.com/max/3834/1*0paobe_W8tmdCF1xhX4BgA.png)

#### 👉 Step 5— Upload the container image

1. Authenticate to [Container Registry](https://cloud.google.com/container-registry) (you need to run this only once):

   gcloud auth configure-docker
2. Execute the following code to upload the docker image to Google Container Registry:

   docker push gcr.io/${PROJECT\_ID}/insurance-app:v1

#### 👉 Step 6— Create Cluster

Now that the container is uploaded, you need a cluster to run the container. A cluster consists of a pool of Compute Engine VM instances, running Kubernetes.

1. Set your project ID and Compute Engine zone options for the gcloud tool:

   gcloud config set project $PROJECT\_ID gcloud config set compute/zone **us-central1**
2. Create a cluster by executing the following code:

   gcloud container clusters create **insurance-cluster** --num-nodes=2

![Google Cloud Platform → Kubernetes Engine → Clusters](https://cdn-images-1.medium.com/max/3832/1*l2sHrv5nuFjDKiyAtjYapQ.png)

#### 👉 Step 7— Deploy Application

To deploy and manage applications on a GKE cluster, you must communicate with the Kubernetes cluster management system. Execute the following command to deploy the application:

```
kubectl create deployment insurance-app --image=gcr.io/${PROJECT_ID}/insurance-app:v1
```

![Output returned on creating deployment through kubectl](https://cdn-images-1.medium.com/max/3836/1*p0_A6PZnfYJ4mnttM7lzzA.png)

#### 👉 Step 8— Expose your application to the internet

By default, the containers you run on GKE are not accessible from the internet because they do not have external IP addresses. Execute the following code to expose the application to the internet:

```
kubectl expose deployment insurance-app --type=LoadBalancer --port 80 --target-port 8080
```

#### 👉 Step 9— Check Service

Execute the following code to get the status of the service. **EXTERNAL-IP** is the web address you can use in browser to view the published app.

```
kubectl get service
```

![Cloud Shell → kubectl get service](https://cdn-images-1.medium.com/max/3832/1*aRWl7frtmvPYaYjAoloFgQ.png)

👉 Step 10— See the app in action on <http://34.71.77.61:8080>

![Final app uploaded on http://34.71.77.61:8080](https://cdn-images-1.medium.com/max/3838/1*bKuZiYSPdE8T5SLKXx5B_Q.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

[Link to GitHub Repository for this tutorial](https://www.github.com/pycaret/pycaret-deployment-google)

[Link to GitHub Repository for Microsoft Azure Deployment](https://www.github.com/pycaret/pycaret-azure-deployment)

[Link to GitHub Repository for Heroku Deployment](https://www.github.com/pycaret/deployment-heroku)

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Deploy PyCaret and Streamlit on AWS Fargate

### Deploy PyCaret and Streamlit app using AWS Fargate — serverless infrastructure

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy ML pipeline serverless on AWS Fargate](https://cdn-images-1.medium.com/max/2000/1*QznGlPsGrGQS4DadTunLXw.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb), we demonstrated how to develop a machine learning pipeline using PyCaret and serve it as a Streamlit web application deployed onto Google Kubernetes Engine. If you haven’t heard about PyCaret before, you can read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to get started.

In this tutorial, we will use the same web app and machine learning pipeline that we had built previously and demonstrate how to deploy it using AWS Fargate which is a serverless compute for containers.

By the end of this tutorial, you will be able to build and host a fully functional containerized web app on AWS without provisioning any server infrastructure.

![Web Application](https://cdn-images-1.medium.com/max/2800/1*TesAmfCyanOeMEPiYxInUg.png)

### 👉 Learning Goals of this Tutorial

* What is a Container? What is Docker? What is Kubernetes?
* What is Amazon Elastic Container Service (ECS), AWS Fargate and serverless deployment?
* Build and push a Docker image onto Amazon Elastic Container Registry.
* Deploy web app using serverless infrastructure i.e. AWS Fargate.

This tutorial will cover the entire workflow starting from building a docker image locally, uploading it onto Amazon Elastic Container Registry, creating a cluster and then defining and executing task using AWS-managed infrastructure.

In the past, we have covered deployment on other cloud platforms such as Azure and Google. If you are interested in learning more about those, you can read the following tutorials:

* [Deploy Streamlit app onto Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)
* [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)
* [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)
* [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b)
* [Deploy Machine Learning Pipeline on AWS Web Service](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)
* [Build and deploy your first machine learning web app on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install pycaret
```

### Streamlit

[Streamlit](https://www.streamlit.io/) is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science. Streamlit can be installed easily using pip.

```
pip install streamlit
```

### Docker Toolbox for Windows 10 Home

[Docker](https://www.docker.com/)\*\* \*\*is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers are used to package up an application with all of its necessary components, such as libraries and other dependencies, and ship it all out as one package. If you haven’t used docker before, this tutorial also covers the installation of Docker Toolbox (legacy) on **Windows 10 Home**. In the [previous tutorial](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) we covered how to install Docker Desktop on **Windows 10 Pro edition**.

### Amazon Web Services (AWS)

Amazon Web Services (AWS) is a comprehensive and broadly adopted cloud platform, offered by Amazon. It has over 175 fully-featured services from data centers globally. If you haven’t used AWS before, you can [sign-up](https://aws.amazon.com/) for a free account.

### ✔️Let’s get started…..

### What is a Container?

Before we get into implementation using AWS Fargate, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, they should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → The programing language such as Python and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

### What is Docker?

Docker is a company that provides software (also called **Docker**) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/).

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

Now that you theoretically understand what a container is and how Docker is used to containerize applications, let’s imagine a scenario where you have to run multiple containers across a fleet of machines to support an enterprise level machine learning application with varied workloads during day and night. This is pretty common for real-life and as simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, deal with failed containers or hardware and million other things!

This entire process of managing hundreds and thousands of containers to keep the application up and running is known as **container orchestration**. Don’t get caught up in the technical details yet.

At this point, you must recognize that managing real-life applications require more than one container and managing all of the infrastructure to keep containers up and running is cumbersome, manual and an administrative burden.

This brings us to **Kubernetes**.

### What is Kubernetes?

Kubernetes is an open-source system developed by Google in 2014 for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/14720/0*vscKcwTh1qNmKv3s)

While Kubernetes is an open-source system developed by Google, almost all major cloud service providers offer Kubernetes as a Managed Service. For example: \*\*Amazon Elastic Kubernetes Service (EKS) **offered by Amazon**, Google Kubernetes Engine (GKE) **offered by Google**, \*\*and \*\*Azure Kubernetes Service (AKS) \*\*offered by Microsoft.

So far we have discussed and understood:

✔️ A ***container***

✔️ Docker

✔️ Kubernetes

Before introducing AWS Fargate, there is only one thing left to discuss and that is Amazon’s own container orchestration service **Amazon Elastic Container Service (ECS).**

### AWS Elastic Container Service (ECS)

Amazon Elastic Container Service (Amazon ECS) is Amazon’s home-grown container orchestration platform. The idea behind ECS is similar to Kubernetes *(both of them are orchestration services)*.

ECS is an AWS-native service, meaning that it is only possible to use on AWS infrastructure. On the other hand, **EKS** is based on Kubernetes, an open-source project which is available to users running on multi-cloud (AWS, GCP, Azure) and even On-Premise.

Amazon also offers a Kubernetes based container orchestration service known as \*\*Amazon Elastic Kubernetes Service (Amazon EKS). \*\*Even though the purpose of ECS and EKS is pretty similar i.e. *orchestrating containerized applications*, there are quite a few differences in pricing, compatibility and security. There is no best answer and the choice of solution depends on the use-case.

Irrespective of whichever container orchestration service you are using (ECS or EKS), there are two ways you can implement the underlying infrastructure:

1. Manually manage the cluster and underlying infrastructure such as Virtual Machines / Servers / (also known as EC2 instances).
2. Serverless — Absolutely no need to manage anything. Just upload the container and that’s it. ← **This is AWS Fargate.**

![Amazon ECS underlying infrastructure](https://cdn-images-1.medium.com/max/2798/1*k4famzZ1w2Ee5XMHRo1Ggw.png)

### AWS Fargate — serverless compute for containers

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. You only pay for the resources required to run your containers, so there is no over-provisioning and paying for additional servers.

![How AWS Fargate works — https://aws.amazon.com/fargate/](https://cdn-images-1.medium.com/max/4668/1*WWQBLhVao-FN_FCrnkPhQg.png)

There is no best answer as to which approach is better. The choice between going serverless or manually managing an EC2 cluster depends on the use-case. Some pointers that can assist with this choice include:

**ECS EC2 (Manual Approach)**

* You are all-in on AWS.
* You have a dedicated Ops team in place to manage AWS resources.
* You have an existing footprint on AWS i.e. you are already managing EC2 instances

**AWS Fargate**

* You do not have huge Ops team to manage AWS resources.
* You do not want operational responsibility or want to reduce it.
* Your application is stateless *(A stateless app is an application that does not save client data generated in one session for use in the next session with that client)*.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train, validate and develop a machine learning pipeline using PyCaret.
* Build a front-end web application with two functionalities: (i) online prediction and (ii) batch prediction.
* Create a Dockerfile
* Create and execute a task to deploy the app using AWS Fargate serverless infrastructure.

Since we have already covered the first two tasks in our [last tutorial](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb), we will quickly recap them and then focus on the remaining items in the list above. If you are interested in learning more about developing a machine learning pipeline in Python using PyCaret and building a web app using a Streamlit framework, please read [this tutorial](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104).

### 👉 Task 1 — Model Training and Validation

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*P7EXfIxqZZGrpeLgDdk1vQ.png)

### 👉 Task 2 — Build a front-end web application

Now that our machine learning pipeline and model are ready to start building a front-end web application that can generate predictions on new datapoints. This application will support ‘Online’ as well as ‘Batch’ predictions through a csv file upload. Let’s breakdown the application code into three main parts:

### Header / Layout

This section imports libraries, loads the trained model and creates a basic layout with a logo on top, a jpg image and a dropdown menu on the sidebar to toggle between ‘Online’ and ‘Batch’ prediction.

![app.py — code snippet part 1](https://cdn-images-1.medium.com/max/2268/1*xAnCZ1N_BNoPW7FoA-NXrA.png)

#### Online Predictions

This section deals with the initial app function, Online one-by-one predictions. We are using streamlit widgets such as *number input, text input, drop down menu and checkbox* to collect the datapoints used to train the model such as Age, Sex, BMI, Children, Smoker, Region.

![app.py — code snippet part 2](https://cdn-images-1.medium.com/max/2408/1*eFeq1wINsUUnvLJfuL-GOA.png)

#### Batch Predictions

Predictions by batch is the second layer of the app’s functionality. The **file\_uploader** widget in streamlit is used to upload a csv file and then called the native \*\*predict\_model() \*\*function from PyCaret to generate predictions that are displayed using streamlit’s write() function.

![app.py — code snippet part 3](https://cdn-images-1.medium.com/max/2410/1*u-g2iLy_gV7hom71PM3CEA.png)

\*\*Testing App \*\*One final step before we deploy the application on AWS Fargate is to test the app locally. Open Anaconda Prompt and navigate to your project folder and execute the following code:

```
streamlit run app.py
```

![Streamlit application testing — Online Prediction](https://cdn-images-1.medium.com/max/2800/1*TesAmfCyanOeMEPiYxInUg.png)

### 👉 Task 3 — Create a Dockerfile

To containerize our application for deployment we need a docker image that becomes a container at runtime. A docker image is created using a Dockerfile. A Dockerfile is just a file with a set of instructions. The Dockerfile for this project looks like this:

The last part of this Dockerfile (starting at line 23) is Streamlit specific. Dockerfile is case-sensitive and must be in the project folder with the other project files.

### 👉 Task 4–Deploy on AWS Fargate:

Follow these simple 9 steps to deploy app on AWS Fargate:

#### 👉 Step 1 — Install Docker Toolbox (for Windows 10 Home)

In order to build a docker image locally, you will need Docker installed on your computer. If you are using Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later) you can download Docker Desktop from [DockerHub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).

However, if you are using Windows 10 Home, you would need to install the last release of legacy Docker Toolbox (v19.03.1) from [Dockers GitHub page](https://github.com/docker/toolbox/releases).

![https://github.com/docker/toolbox/releases](https://cdn-images-1.medium.com/max/2000/1*wn3zVxR0d5rZFDkvhEHi1Q.png)

Download and Run **DockerToolbox-19.03.1.exe** file.

The easiest way to check if the installation was successful is by opening the command prompt and typing in ‘docker’. It should print the help menu.

![Anaconda Prompt to check docker](https://cdn-images-1.medium.com/max/2198/1*f5l4Tds3EOTFSPx6CT5M7w.png)

#### 👉 Step 2 — Create a Repository in Elastic Container Registry (ECR)

**(a) Login to your AWS console and search for Elastic Container Registry:**

![AWS Console](https://cdn-images-1.medium.com/max/2000/1*XCvjm_Ho1CiaNg59y3MPiw.png)

**(b) Create a new repository:**

![Create New Repository on Amazon Elastic Container Registry](https://cdn-images-1.medium.com/max/3822/1*alFdHEfwYrdZ5J9d14gGgA.png)

![Create Repository](https://cdn-images-1.medium.com/max/3822/1*BeVF99WdFAPApWLS83SJ3Q.png)

Click on “Create Repository”.

**(c) Click on “View push commands”:**

![Push commands for pycaret-streamlit-aws repository](https://cdn-images-1.medium.com/max/2000/1*WC-0ShGuB0MB6LgTq07B0Q.png)

#### 👉 Step 3— Execute push commands

Navigate to your project folder using Anaconda Prompt and execute the commands you have copied in the step above. You must be in the folder where the Dockerfile and the rest of your code reside before executing these commands.

These commands are for building docker image and then uploading it on AWS ECR.

#### 👉 Step 4 — Check your uploaded image

Click on the repository you created and you will see an image URI of the uploaded image in the step above. Copy the image URI (it would be needed in step 6 below).

![](https://cdn-images-1.medium.com/max/3828/1*VuYsEXDoSmmHlEFfYgOAhg.png)

#### 👉 Step 5 — Create and Configure a Cluster

**(a) Click on “Clusters” on left-side menu:**

![Create Cluster — Step 1](https://cdn-images-1.medium.com/max/3834/1*eGOSlysIcdpDZi9GnPAhHw.png)

**(b) Select “Networking only” and click Next step:**

![Select Networking Only Template](https://cdn-images-1.medium.com/max/2000/1*a0VectBKdBhmZC_My5OylQ.png)

**(c) Configure Cluster (Enter cluster name) and click on Create:**

![Configure Cluster](https://cdn-images-1.medium.com/max/3780/1*6AMEaRIr4Rz1qt_ZmhDy4Q.png)

Click on “Create”.

**(d) Cluster Created:**

![Cluster Created](https://cdn-images-1.medium.com/max/3824/1*1UfMJt807V92-jc6Z9ZlfQ.png)

#### 👉 Step 6 — Create a new Task definition

A **task** definition is required to run Docker containers in Amazon ECS. Some of the parameters you can specify in a **task** definition include: The Docker image to use with each container in your **task**. How much CPU and memory to use with each **task** or each container within a **task**.

**(a) Click on “Create new task definition”:**

![Create a new task definition](https://cdn-images-1.medium.com/max/3820/1*6ET40juZ2owkA1xdDOsDHg.png)

**(b) Select “FARGATE” as launch type:**

![Select Launch Type Compatibility](https://cdn-images-1.medium.com/max/3822/1*1Ebz8wmfSisxcrultB86nQ.png)

**(c) Fill in the details:**

![Configure Task and container definitions (part 1)](https://cdn-images-1.medium.com/max/2000/1*JqrJPuts4QpVBUK2pKFPpg.png)

![Configure Task and container definitions (part 2)](https://cdn-images-1.medium.com/max/2000/1*SoM892EIZ2NpSzUCUg10rA.png)

**(d) Click on “Add Containers” and fill in the details:**

![Adding Container in task definitions](https://cdn-images-1.medium.com/max/2508/1*Kt9zGo0kk4bAUyrWhedU4Q.png)

Click “Create Task” on the bottom right.

![](https://cdn-images-1.medium.com/max/3828/1*DZpHXH5iy3daszNT4RYoEQ.png)

#### 👉 Step 7— Execute Task Definition

In last step we created a task that will start the container. Now we will execute the task by clicking **“Run Task”** under Actions.

![](https://cdn-images-1.medium.com/max/3836/1*nuUekT3eyCeDRoeZlTXk_Q.png)

**(a) Click on “Switch to launch type” to change the type to Fargate:**

![](https://cdn-images-1.medium.com/max/3850/1*_TMuygT58eKgMJQStWCwQw.png)

**(b) Select the VPC and Subnet from the dropdown:**

![](https://cdn-images-1.medium.com/max/3812/1*w7uipHeBNz9RhaBFsN85Bw.png)

Click on “Run Task” on bottom right.

#### 👉 Step 8— Allow inbound port 8501 from Network settings

One last step before we can see our application in action on Public IP address is to allow port 8501 (used by streamlit) by creating a new rule. In order to do that, follow these steps:

**(a) Click on Task**

![](https://cdn-images-1.medium.com/max/3834/1*lZh9LgN8vgctY3Xa_aeMrg.png)

**(b) Click on ENI Id:**

![](https://cdn-images-1.medium.com/max/3832/1*K1L_vExR8-2q-6b020voPQ.png)

**(c) Click on Security groups**

![](https://cdn-images-1.medium.com/max/3822/1*vPhVnBMZTXqBQj0ntWx5WA.png)

**(d) Scroll down and click on “Edit inbound rules”**

![](https://cdn-images-1.medium.com/max/3828/1*nWb74Ex5UWs-yJOZs5Ecew.png)

**(e) Add a Custom TCP rule of port 8501**

![](https://cdn-images-1.medium.com/max/3826/1*uqgV_Fr5NPGzWzwQ5LHAxw.png)

### 👉 Congratulations! You have published your app serverless on AWS Fargate. Use public IP address with port 8501 to access the application.

![App published on 99.79.189.46:8501](https://cdn-images-1.medium.com/max/3834/1*q9GXNH-YCL2vT7Q-Uj9clQ.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

[Link to GitHub Repository for this tutorial](https://www.github.com/pycaret/pycaret-streamlit-aws)

[Link to GitHub Repository for Google Kubernetes Deployment](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

[Link to GitHub Repository for Heroku Deployment](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Classification](https://www.pycaret.org/clf101) [Regression](https://www.pycaret.org/reg101) [Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# Anomaly Detector in Power BI using PyCaret

### Build your first Anomaly Detector in Power BI using PyCaret

#### A step-by-step tutorial for implementing anomaly detection in Power BI

#### by Moez Ali

![Anomaly Detection Dashboard in Power BI](https://cdn-images-1.medium.com/max/2000/1*sh9LrK5WiF1pBDDR1PCK0g.png)

In our last post, [Machine Learning in Power BI using PyCaret](https://towardsdatascience.com/machine-learning-in-power-bi-using-pycaret-34307f09394a), we presented a **step-by-step tutorial** on how PyCaret can be integrated within Power BI, thus allowing analysts and data scientists to add a layer of machine learning to their Dashboards and Reports without any additional license costs.

In this post, we will dive deeper and implement an Anomaly Detector in Power BI using PyCaret. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

### Learning Goals of this Tutorial

* What is Anomaly Detection? Types of Anomaly Detection?
* Train and implement an unsupervised anomaly detector in Power BI.
* Analyze results and visualize information in a dashboard.
* How to deploy the anomaly detector in Power BI production?

### Before we start

If you have used Python before, it is likely that you already have Anaconda Distribution installed on your computer. If not, [click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/products/individual](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install pycaret. It’s a three-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Create an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and execute the following code:

```
conda create --name **myenv** python=3.7
```

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Install PyCaret**

Execute the following code in Anaconda Prompt:

```
pip install pycaret
```

Installation may take 15–20 minutes. If you are having issues with installation, please see our [GitHub](https://www.github.com/pycaret/pycaret) page for known issues and resolutions.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Set Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\AppData\Local\Continuum\anaconda3\envs\myenv

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*zQMKuyEk8LGrOPE-NByjrg.png)

### What is Anomaly Detection?

Anomaly Detection \*\*\*\*is a technique in machine learning used for identifying **rare items**, **events** or **observations** which raise suspicions by differing significantly from the majority of the data.

Typically, the anomalous items will translate to some kind of problem such as bank fraud, a structural defect, medical problems or error. There are three ways to implement an anomaly detector:

\*\*(a) Supervised: \*\*Used when the data set has labels identifying which transactions are anomaly and which are normal. *(this is similar to a supervised classification problem)*.

\*\*(b) Semi-Supervised: \*\*The idea behind semi-supervised anomaly detection is to train a model on normal data only *(without any anomalies)*. When the trained model is then used on unseen data points, it can predict whether the new data point is normal or not (based on the distribution of the data in the trained model).

\*\*(c) Unsupervised: \*\*Exactly as it sounds, unsupervised means no labels and therefore no training and test data set. In unsupervised learning a model is trained on the complete dataset and assumes that the majority of the instances are normal. While looking for instances that seem to fit least to the remainder. There are several unsupervised anomaly detection algorithms such as Isolation Forest or One-Class Support Vector Machine. Each has their own method of identifying anomalies in the dataset.

This tutorial is about implementing unsupervised anomaly detection in Power BI using a Python library called PyCaret. Discussion of the specific details and mathematics behind these algorithms are out-of-scope for this tutorial.

![Goldstein M, Uchida S (2016) A Comparative Evaluation of Unsupervised Anomaly Detection Algorithms for Multivariate Data. PLo](https://cdn-images-1.medium.com/max/2800/1*-Cnyg6-F-Qd4r1Ptcf6nNw.png)

### Setting the Business Context

Many companies issue corporate credit cards (*also known as purchase cards or* *p-cards*) to employees for effectively managing operational purchasing. Normally there is a process in place for employees to submit those claims electronically. The data collected is typically transactional and likely to include date of transaction, vendor name, type of expense, merchant and amount.

In this tutorial we will use State Employees Credit Card Transactions from 2014–2019 for the Department of Education in the State of Delaware, US. The data is available online on their [open data](https://data.delaware.gov/Government-and-Finance/Credit-Card-Spend-by-Merchant/8pzf-ge27) platform.

![https://data.delaware.gov/Government-and-Finance/Credit-Card-Spend-by-Merchant/8pzf-ge27](https://cdn-images-1.medium.com/max/3058/1*c8KS7taBuTRlxJ7tTL964g.png)

**Disclaimer:** *This tutorial demonstrates the use of PyCaret in Power BI to build an anomaly detector. The sample dashboard that is built in this tutorial by no means reflects actual anomalies or is meant to identify anomalies.*

### 👉 Let’s get started

Now that you have setup the Anaconda Environment, installed PyCaret, understand the basics of Anomaly Detection and have the business context for this tutorial, let’s get started.

### 1. Get Data

The first step is importing the dataset into Power BI Desktop. You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

![Power BI Desktop → Get Data → Other → Web](https://cdn-images-1.medium.com/max/3840/1*WMQRdUPcw8VaG0HIOiGyQQ.png)

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/delaware\_anomaly.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/delaware_anomaly.csv)

### 2. Model Training

To train an anomaly detector in Power BI we will have to execute a Python script in Power Query Editor (Power Query Editor → Transform → Run python script). Run the following code as a Python script:

```
from **pycaret.anomaly** import *
dataset = **get_outliers**(dataset, ignore_features=['DEPT_NAME', 'MERCHANT', 'TRANS_DT'])
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*jLYtThjhL2rAlfOtZnG0gQ.png)

We have ignored a few columns in the dataset by passing them under **ignore\_features** parameter. There could be many reasons for which you might not want to use certain columns for training a machine learning algorithm.

PyCaret allows you to hide instead of drop unneeded columns from a dataset as you might require those columns for later analysis. For example, in this case we don't want to use transactional date for training an algorithm and hence we have passed it under **ignore\_features.**

There are over 10 ready-to-use anomaly detection algorithms in PyCaret.

![](https://cdn-images-1.medium.com/max/2000/1*piuoq_K4B2aiyzOCkDg8MA.png)

By default, PyCaret trains a **K-Nearest Neighbors Anomaly Detector** with 5% fraction (i.e. 5% of the total number of rows in the table will be flagged as outliers). Default values can be changed easily:

* To change the fraction value you can use the \*\*\*fraction \*\*\*parameter within the \*\*get\_outliers( ) \*\*function.
* To change the model type use the \*\*\*model \*\*\*parameter within **get\_outliers()**.

See an example code for training an **Isolation Forest** detector with 0.1 fraction:

```
from **pycaret.anomaly** import *
dataset = **get_outliers**(dataset, model = 'iforest', fraction = 0.1, ignore_features=['DEPT_NAME', 'MERCHANT', 'TRANS_DT'])
```

**Output:**

![Anomaly Detection Results (after execution of Python code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2280/1*dZbf7VmCxkPUcX_p7kKJ4w.png)

Two new columns are attached to the original table. Label (1 = outlier, 0 = inlier) and Score (data points with high scores are categorized as outlier). Apply the query to see results in Power BI data set.

![Results in Power BI Desktop (after applying query)](https://cdn-images-1.medium.com/max/2894/1*QFJ2DJX_bGSxutOdxNmwEg.png)

### 3. Dashboard

Once you have Outlier labels in Power BI, here’s an example of how you can visualize it in dashboard:

![Summary page of Dashboard](https://cdn-images-1.medium.com/max/2624/1*7qWjee_M6PTrAd0PJdU1yg.png)

![Details page of Dashboard](https://cdn-images-1.medium.com/max/2634/1*4ISkFG8r3LtVJq0P3793Wg.png)

You can download the PBIX file and the data set from our [GitHub](https://github.com/pycaret/powerbi-anomaly-detection).

### 👉 Implementing Anomaly Detection in Production

What has been demonstrated above was one simple way to implement Anomaly Detection in Power BI. However, it is important to note that the method shown above train the anomaly detector every time the Power BI dataset is refreshed. This may be a problem for two reasons:

* When the model is re-trained with new data, the anomaly labels may change (some transactions that were labeled as outliers earlier may not be considered outliers anymore)
* You don’t want to spend hours of time everyday re-training the model.

An alternative way to implement anomaly detection in Power BI when it is intended to be used in production is to pass the pre-trained model to Power BI for labeling instead of training the model in Power BI itself.

### **Training Model before-hand**

You can use any Integrated Development Environment (IDE)or Notebook for training machine learning models. In this example, we have used Visual Studio Code to train an anomaly detection model.

![Model Training in Visual Studio Code](https://cdn-images-1.medium.com/max/2014/1*zzymbb9ySyl3jeaFQoHxDg.png)

A trained model is then saved as a pickle file and imported into Power Query for generating anomaly labels (1 or 0).

![Anomaly Detection Pipeline saved as a file](https://cdn-images-1.medium.com/max/2000/1*fLnTzbd-dTRtqwxmPqI4kw.png)

If you would like to learn more about implementing Anomaly Detection in Jupyter notebook using PyCaret, watch this 2 minute video tutorial:

### Using the pre-trained model

Execute the below code as a Python script to generate labels from the pre-trained model.

```
from **pycaret.anomaly** import *
dataset = **predict_model**('c:/.../anomaly_deployment_13052020, data = dataset)
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*VMSuDzp7FpJgddT-NjTtUQ.png)

The output of this will be the same as the one we saw above. However, the difference is that when you use a pre-trained model, the label is generated on a new dataset using the same model instead of re-training the model every time you refresh the Power BI dataset.

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2280/1*dZbf7VmCxkPUcX_p7kKJ4w.png)

### **Making it work on Power BI Service**

Once you’ve uploaded the .pbix file to the Power BI service, a couple more steps are necessary to enable seamless integration of the machine learning pipeline into your data pipeline. These include:

* **Enable scheduled refresh for the dataset** — to enable a scheduled refresh for the workbook that contains your dataset with Python scripts, see [Configuring scheduled refresh](https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh), which also includes information about **Personal Gateway**.
* **Install the Personal Gateway** — you need a **Personal Gateway** installed on the machine where the file is located, and where Python is installed; the Power BI service must have access to that Python environment. You can get more information on how to [install and configure Personal Gateway](https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-personal-mode).

If you are Interested in learning more about Anomaly Detection, checkout our [Notebook Tutorial.](https://pycaret.org/ano101/)

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Deploy ML App on Google Kubernetes

### Deploy Machine Learning App built using Streamlit and PyCaret on Google Kubernetes Engine

#### A step-by-step beginner’s guide to containerize and deploy a Streamlit app on Google Kubernetes Engine

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy a streamlit app on Google Kubernetes Engine](https://cdn-images-1.medium.com/max/2000/1*q-xQMoYByRdI7OOfM1qFXg.png)

### RECAP

In our [last post](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) on deploying a machine learning pipeline in the cloud, we demonstrated how to develop a machine learning pipeline in PyCaret and deploy a trained model on Heroku PaaS as a web application built using a Streamlit open-source framework. If you haven’t heard about PyCaret before, you can read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will use the same machine learning pipeline and Streamlit app and demonstrate how to containerize and deploy them onto Google Kubernetes Engine.

By the end of this tutorial, you will be able to build and host a fully functional containerized web app on Google Kubernetes Engine. This web app can be used to generate online predictions (one-by-one) and predictions by batch (by uploading a csv file) using a trained machine learning model. The final app looks like this:

![Final App (Page 1 of 2)](https://cdn-images-1.medium.com/max/3832/1*GxVKpxijk0tlqk-bO5Q3JQ.png)

### 👉 What you will learn in this tutorial

* What is a Container, what is Docker, what is Kubernetes, and what is Google Kubernetes Engine?
* Build a Docker image and upload it onto Google Container Registry (GCR).
* Create a cluster on GCP and deploy a machine learning app as a web service.
* See a web app in action that uses a trained machine learning pipeline to predict new data points in real time.

In the past, we have covered containerization using docker and deployment on cloud platforms like Azure, GCP and AWS. If you are interested in learning more about those, you can read the following tutorials:

* [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)
* [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)
* [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b)
* [Deploy Machine Learning Pipeline on AWS Web Service](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)
* [Build and deploy your first machine learning web app on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install **pycaret**
```

### Streamlit

[Streamlit](https://www.streamlit.io/) is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science. Streamlit can be installed easily using pip.

```
pip install **streamlit**
```

### Google Cloud Platform

Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail and YouTube. If you do not have an account with GCP, you can sign-up [here](https://console.cloud.google.com/getting-started). If you are signing up for the first time you will get free credits for 1 year.

### Let’s get started.

Before we get into Kubernetes, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, he or she should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → A programing language such as Python and all the libraries and dependencies with the exact versions used when the application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

> ***What’s Docker then?***

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

\*\*Docker \*\*is a company that provides software (also called Docker) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/) that also provide container solutions.

Now that you understand containers and docker specifically, let’s understand what Kubernetes is all about.

### What is Kubernetes?

Kubernetes is a powerful open-source system developed by Google back in 2014, for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines. It is a platform designed to completely manage the life cycle of containerized applications.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/14720/0*49CVX837ZpkbRblC)

### Features

✔️ \*\*Load Balancing: \*\*Automatically distributes the load between containers.

✔️ \*\*Scaling: \*\*Automatically scale up or down by adding or removing containers when demand changes such as peak hours, weekends and holidays.

✔️ \*\*Storage: \*\*Keeps storage consistent with multiple instances of an application.

✔️ **Self-healing** Automatically restarts containers that fail and kills containers that don’t respond to your user-defined health check.

✔️ \*\*Automated Rollouts \*\*you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all of their resources to the new container.

### Why do you need Kubernetes if you have Docker?

Imagine a scenario where you have to run multiple docker containers on multiple machines to support an enterprise level ML application with varied workloads during day and night. As simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, and deal with failed containers or hardware. This is the problem Kubernetes is solving by allowing large numbers of containers to work together in harmony, reducing the operational burden.

### What is Google Kubernetes Engine?

Google Kubernetes Engine is an implementation of *Google’s open source Kubernetes* on Google Cloud Platform. Simple!

Other popular alternatives to GKE are [Amazon ECS](https://aws.amazon.com/ecs/) and [Microsoft Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/).

### One final time, do you understand this?

* \*\*A Container \*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.
* \*\*Docker \*\*is a software used for building and managing containers.
* \*\*Kubernetes \*\*is an open-source system for managing containerized applications in a clustered environment.
* **Google Kubernetes Engine** is an implementation of the open source Kubernetes framework on Google Cloud Platform.

In this tutorial, we will use Google Kubernetes Engine. In order to follow along, you must have a Google Cloud Platform account. [Click here](https://console.cloud.google.com/getting-started) to sign-up for free.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build a web application that supports online (one-by-one) as well as batch prediction using trained machine learning model and pipeline.

### Tasks

* Train, validate and develop a machine learning pipeline using PyCaret.
* Build a front-end web application with two functionalities: (i) online prediction and (ii) batch prediction.
* Create a Dockerfile
* Deploy the web app on Google Kubernetes Engine. Once deployed, it will become publicly available and can be accessed via Web URL.

### 👉 Task 1 — Model Training and Validation

Training and model validation are performed in an Integrated Development Environment (IDE) or Notebook either on your local machine or on cloud. If you haven’t used PyCaret before, [click here](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more about PyCaret or see [Getting Started Tutorials](https://www.pycaret.org/tutorial) on our [website](https://www.pycaret.org/).

In this tutorial, we have performed two experiments. The first experiment is performed with default preprocessing settings in PyCaret. The second experiment has some additional preprocessing tasks such as **scaling and normalization, automatic feature engineering and binning continuous data into intervals**. See the setup code for the second experiment:

```
**# Experiment No. 2**

from **pycaret.regression** import *****

r2 = **setup**(data, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True,
           feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'])
```

![Comparison of information grid for both experiments](https://cdn-images-1.medium.com/max/2000/1*TeqcOM-jBpkdeQu84c4Onw.png)

The magic happens with only a few lines of code. Notice that in **Experiment 2** the transformed dataset has 62 features for training derived from only 6 features in the original dataset. All of the new features are the result of transformations and automatic feature engineering in PyCaret.

![Columns in dataset after transformation](https://cdn-images-1.medium.com/max/2000/1*ju5RFYKGkAVEOvVjeoM5nQ.png)

Sample code for model training in PyCaret:

```
# Model Training and Validation 
lr = **create_model**('lr')
```

![10 Fold cross-validation of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2276/1*TX-IzWHBekZBRSQi2T_JTQ.png)

Notice the impact of transformations and automatic feature engineering. The R2 has increased by 10% with very little effort. We can compare the **residual plot** of linear regression model for both experiments and observe the impact of transformations and feature engineering on the \*\*heteroskedasticity \*\*of model.

```
# plot residuals of trained model**
plot_model**(lr, plot = 'residuals')
```

![Residual Plot of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2876/1*LxVMcK4hNvBvEj1tyqxfWQ.png)

Machine learning is an iterative process. The number of iterations and techniques used within are dependent on how critical the task is and what the impact will be if predictions are wrong. The severity and impact of a machine learning model to predict a patient outcome in real-time in the ICU of a hospital is far more than a model built to predict customer churn.

In this tutorial, we have performed only two iterations and the linear regression model from the second experiment will be used for deployment. At this stage, however, the model is still only an object within a Notebook / IDE. To save it as a file that can be transferred to and consumed by other applications, execute the following code:

```
# save transformation pipeline and model 
**save_model**(lr, model_name = 'deployment_28042020')
```

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created. All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*NWoHVWJzO7i7gIvrlBnIiQ.png)

We have finished training and model selection. The final machine learning pipeline and linear regression model is now saved as a pickle file (deployment\_28042020.pkl) that will be used in a web application to generate predictions on new datapoints.

### 👉 Task 2 — Build a front-end web application

Now that our machine learning pipeline and model are ready to start building a front-end web application that can generate predictions on new datapoints. This application will support ‘Online’ as well as ‘Batch’ predictions through a csv file upload. Let’s breakdown the application code into three main parts:

### Header / Layout

This section imports libraries, loads the trained model and creates a basic layout with a logo on top, a jpg image and a dropdown menu on the sidebar to toggle between ‘Online’ and ‘Batch’ prediction.

![app.py — code snippet part 1](https://cdn-images-1.medium.com/max/2268/1*xAnCZ1N_BNoPW7FoA-NXrA.png)

### Online Predictions

This section deals with the initial app function, Online one-by-one predictions. We are using streamlit widgets such as *number input, text input, drop down menu and checkbox* to collect the datapoints used to train the model such as Age, Sex, BMI, Children, Smoker, Region.

![app.py — code snippet part 2](https://cdn-images-1.medium.com/max/2408/1*eFeq1wINsUUnvLJfuL-GOA.png)

### Batch Predictions

Predictions by batch is the second layer of the app’s functionality. The **file\_uploader** widget in streamlit is used to upload a csv file and then called the native \*\*predict\_model() \*\*function from PyCaret to generate predictions that are displayed using streamlit’s write() function.

![app.py — code snippet part 3](https://cdn-images-1.medium.com/max/2410/1*u-g2iLy_gV7hom71PM3CEA.png)

If you remember from Task 1 above we finalized a linear regression model that was trained on 62 features that were extracted from the 6 original features. The front-end of web application has an input form that collects only the six features i.e. age, sex, bmi, children, smoker, region.

How do we transform these 6 features of a new data points into the 62 used to train the model? We do not need to worry about this part as PyCaret automatically handles this by orchestrating the transformation pipeline. When you call the predict function on a model trained using PyCaret, all transformations are applied automatically (in sequence) before generating predictions from the trained model.

\*\*Testing App \*\*One final step before we publish the application on Heroku is to test the web app locally. Open Anaconda Prompt and navigate to your project folder and execute the following code:

```
**streamlit** run app.py
```

![Streamlit application testing — Online Prediction](https://cdn-images-1.medium.com/max/3832/1*GxVKpxijk0tlqk-bO5Q3JQ.png)

![Streamlit application testing — Batch Prediction](https://cdn-images-1.medium.com/max/3836/1*P5tit2pMf5qiQqU_wjQMVg.png)

Now that we have a fully functional web application, we can start the process of containerizing and deploying the app on Google Kubernetes Engine.

### 👉 Task 3 — Create a Dockerfile

To containerize our application for deployment we need a docker image that becomes a container at runtime. A docker image is created using a Dockerfile. A Dockerfile is just a file with a set of instructions. The Dockerfile for this project looks like this:

The last part of this Dockerfile (starting at line 23) is Streamlit specific and not needed generally. Dockerfile is case-sensitive and must be in the project folder with the other project files.

### 👉 Task 4 — Deploy a ML pipeline on GKE:

If you would like to follow along you will have to fork this [repository](https://github.com/pycaret/pycaret-streamlit-google) from GitHub.

![https://github.com/pycaret/pycaret-streamlit-google](https://cdn-images-1.medium.com/max/3816/1*C5WvNEM3U59hHoAjFtE_EQ.png)

Follow through these simple 10 steps to deploy app on GKE Cluster.

#### Step 1 — Create a new project in GCP Console

Sign-in to your GCP console and go to Manage Resources

![Google Cloud Platform Console → Manage Resources](https://cdn-images-1.medium.com/max/3832/1*OS16COUUns7uBnpyUxH9-w.png)

Click on **Create New Project**

![Google Cloud Platform Console → Manage Resources → Create New Project](https://cdn-images-1.medium.com/max/3814/1*mI3sxfCPrUbt8OtLpa6ViQ.png)

#### Step 2 — Import Project Code

Click the \*\*Activate Cloud Shell \*\*button at the top right of the console window to open the Cloud Shell.

![Google Cloud Platform (Project Info Page)](https://cdn-images-1.medium.com/max/3828/1*KSlqCD2VMDvQo4Oft7nqaA.png)

Execute the following code in Cloud Shell to clone the GitHub repository used in this tutorial.

```
git clone [https://github.com/pycaret/pycaret-streamlit-google.git](https://github.com/pycaret/pycaret-streamlit-google.git)
```

#### Step 3 — Set Project ID Environment Variable

Execute the following code to set the PROJECT\_ID environment variable.

```
export PROJECT_ID=**pycaret-streamlit-gcp**
```

*pycaret-streamlit-gcp* is the name of the project we chose in step 1 above.

#### Step 4 — Build the docker image

Build the docker image of the application and tag it for uploading by executing the following code:

```
docker build -t gcr.io/${PROJECT_ID}/insurance-streamlit:v1 .
```

![Message returned when docker build is successful](https://cdn-images-1.medium.com/max/3830/1*5HY6RQRrRzDjsmQEZK_Qbg.png)

You can check the available images by running the following code:

```
**docker **images
```

#### Step 5 — Upload the container image

1. Authenticate to [Container Registry](https://cloud.google.com/container-registry) (you need to run this only once):

   gcloud auth configure-docker
2. Execute the following code to upload the docker image to Google Container Registry:

   docker push gcr.io/${PROJECT\_ID}/insurance-streamlit:v1

#### Step 6 — Create Cluster

Now that the container is uploaded, you need a cluster to run the container. A cluster consists of a pool of Compute Engine VM instances, running Kubernetes.

1. Set your project ID and Compute Engine zone options for the gcloud tool:

   gcloud config set project $PROJECT\_ID gcloud config set compute/zone **us-central1**
2. Create a cluster by executing the following code:

   gcloud container clusters create **streamlit-cluster** --num-nodes=2

![Google Cloud Platform → Kubernetes Engine → Clusters](https://cdn-images-1.medium.com/max/3832/1*hNX145tbVPjtTFOSLvjXnw.png)

#### Step 7 — Deploy Application

To deploy and manage applications on a GKE cluster, you must communicate with the Kubernetes cluster management system. Execute the following command to deploy the application:

```
kubectl create deployment insurance-streamlit --image=gcr.io/${PROJECT_ID}/insurance-streamlit:v1
```

#### Step 8 — Expose your application to the internet

By default, the containers you run on GKE are not accessible from the internet because they do not have external IP addresses. Execute the following code to expose the application to the internet:

```
kubectl expose deployment insurance-streamlit --type=LoadBalancer --port 80 --target-port **8501**
```

#### Step 9 — Check Service

Execute the following code to get the status of the service. **EXTERNAL-IP** is the web address you can use in browser to view the published app.

```
kubectl get service
```

#### Step 10 — See the app in action on web address

![App Published on https://34.70.49.248 — Page 1](https://cdn-images-1.medium.com/max/3834/1*zHRwykiazKdjL32SE_Uj8g.png)

![App Published on https://34.70.49.248 — Page 2](https://cdn-images-1.medium.com/max/3824/1*YhRqNABfQOIcMq2owc0pmw.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

[Link to GitHub Repository for this tutorial](https://github.com/pycaret/pycaret-streamlit-google)

[Link to GitHub Repository for Microsoft Azure Deployment](https://www.github.com/pycaret/pycaret-azure-deployment)

[Link to GitHub Repository for Heroku Deployment](https://www.github.com/pycaret/deployment-heroku)

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Classification](https://www.pycaret.org/clf101) [Regression](https://www.pycaret.org/reg101) [Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# Deploy Machine Learning Pipeline on GKE

### Deploy Machine Learning Pipeline on Google Kubernetes Engine

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy ML pipeline on Google Kubernetes Engine](https://cdn-images-1.medium.com/max/2000/1*P-JjI7MXq6UJV9Xab-B9qg.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) on deploying a machine learning pipeline in the cloud, we demonstrated how to develop a machine learning pipeline in PyCaret, containerize it with Docker and serve as a web app using Microsoft Azure Web App Services. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will use the same machine learning pipeline and Flask app that we built and deployed previously. This time we will demonstrate how to containerize and deploy a machine learning pipeline on Google Kubernetes Engine.

### 👉 Learning Goals of this Tutorial

* Learn what is a Container, what is Docker, what is Kubernetes, and what is Google Kubernetes Engine?
* Build a Docker image and upload it on Google Container Registry (GCR).
* Create clusters and deploy a machine learning pipeline with a Flask app as a web service.
* See a web app in action that uses a trained machine learning pipeline to predict new data points in real-time.

Previously we demonstrated [how to deploy a ML pipeline on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) and [how to deploy a ML pipeline on Azure Web Services with a Docker container.](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)

This tutorial will cover the entire workflow starting from building a docker image, uploading it onto Google Container Registry and then deploying the pre-trained machine learning pipeline and Flask app onto Google Kubernetes Engine (GKE).

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install pycaret
```

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a framework that allows you to build web applications. A web application can be a commercial website, blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models. If you don’t have Flask installed, you can use pip to install it.

### Google Cloud Platform

Google Cloud Platform (GCP), offered by Google, is a suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products, such as Google Search, Gmail and YouTube. If you do not have an account with GCP, you can sign-up [here](https://console.cloud.google.com/getting-started). If you are signing up for the first time you will get free credits for 1 year.

### Let’s get started.

Before we get into Kubernetes, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, he or she should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → Programing language such as Python and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

> What’s Docker then?

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

Docker is a company that provides software (also called Docker) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/) that provides container solution.

Now that you understand containers and docker specifically, let’s understand what Kubernetes is all about.

### What is Kubernetes?

Kubernetes is a powerful open-source system developed by Google back in 2014, for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines. It is a platform designed to completely manage the life cycle of containerized applications.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/23216/0*2ZayMwt1Un8-9ZFA)

### Features

✔️ \*\*Load Balancing: \*\*Automatically distributes the load between containers.

✔️ \*\*Scaling: \*\*Automatically scale up or down by adding or removing containers when demand changes such as peak hours, weekends and holidays.

✔️ \*\*Storage: \*\*Keeps storage consistent with multiple instances of an application.

✔️ **Self-healing** Automatically restarts containers that fail and kills containers that don’t respond to your user-defined health check.

✔️ \*\*Automated Rollouts \*\*you can automate Kubernetes to create new containers for your deployment, remove existing containers and adopt all of their resources to the new container.

### Why do you need Kubernetes if you have Docker?

Imagine a scenario where you have to run multiple docker containers on multiple machines to support an enterprise level ML application with varied workloads during day and night. As simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, and deal with failed containers or hardware. This is the problem Kubernetes is solving by allowing large numbers of containers to work together in harmony, reducing the operational burden.

> ## It’s a mistake to compare \*\*Docker with Kubernetes. \*\*These are two different technologies. Docker is a software that allows you to containerize applications while Kubernetes is a container management system that allows to create, scale and monitor hundreds and thousands of containers.

In the lifecycle of any application, Docker is used for packaging the application at the time of deployment, while kubernetes is used for rest of the life for managing the application.

![Lifecycle of an application deployed through Kubernetes / Docker](https://cdn-images-1.medium.com/max/3200/1*dBJjxZrfdMppXhdwjZLX6w.png)

### What is Google Kubernetes Engine?

Google Kubernetes Engine is implementation of *Google’s open source Kubernetes* on Google Cloud Platform. Simple!

Other popular alternatives to GKE are [Amazon ECS](https://aws.amazon.com/ecs/) and [Microsoft Azure Kubernetes Service](https://azure.microsoft.com/en-us/services/kubernetes-service/).

### One final time, do you understand this?

* \*\*A Container \*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.
* \*\*Docker \*\*is a software used for building and managing containers.
* \*\*Kubernetes \*\*is an open-source system for managing containerized applications in a clustered environment.
* **Google Kubernetes Engine** is an implementation of the open source Kubernetes framework on Google Cloud Platform.

In this tutorial we will use Google Kubernetes Engine. In order to follow along, you must have a Google Cloud Platform account. [Click here](https://console.cloud.google.com/getting-started) to sign-up for free.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train and develop a machine learning pipeline for deployment.
* Build a web app using a Flask framework. It will use the trained ML pipeline to generate predictions on new data points in real-time.
* Build a docker image and upload a container onto Google Container Registry (GCR).
* Create clusters and deploy the app on Google Kubernetes Engine.

Since we have already covered the first two tasks in our initial tutorial, we will quickly recap them and then focus on the remaining items in the list above. If you are interested in learning more about developing a machine learning pipeline in Python using PyCaret and building a web app using a Flask framework, please read [this tutorial](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99).

### 👉 Develop a Machine Learning Pipeline

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*P7EXfIxqZZGrpeLgDdk1vQ.png)

### 👉 Build a Web Application

This tutorial is not focused on building a Flask application. It is only discussed here for completeness. Now that our machine learning pipeline is ready we need a web application that can connect to our trained pipeline to generate predictions on new data points in real-time. We have created the web application using Flask framework in Python. There are two parts of this application:

* Front-end (designed using HTML)
* Back-end (developed using Flask)

This is how our web application looks:

![Web application on local machine](https://cdn-images-1.medium.com/max/3780/1*tc_6S8NztYKB85rPUJd1uQ.png)

If you haven’t followed along so far, no problem. You can simply fork this [repository](https://github.com/pycaret/pycaret-deployment-google) from GitHub. This is how your project folder should look at this point:

![https://www.github.com/pycaret/pycaret-deployment-google](https://cdn-images-1.medium.com/max/3796/1*CcId22jB-BMCen8o1hWNdQ.png)

Now that we have a fully functional web application, we can start the process of containerizing and deploying the app on Google Kubernetes Engine.

### 10-steps to deploy a ML pipeline on Google Kubernetes Engine:

#### 👉 Step 1 — Create a new project in GCP Console

Sign-in to your GCP console and go to Manage Resources

![Google Cloud Platform Console → Manage Resources](https://cdn-images-1.medium.com/max/3832/1*OS16COUUns7uBnpyUxH9-w.png)

Click on **Create New Project**

![Google Cloud Platform Console → Manage Resources → Create New Project](https://cdn-images-1.medium.com/max/3834/1*QJz8fITeJJWP44yPm2v4vQ.png)

#### 👉 Step 2 — Import Project Code

Click the \*\*Activate Cloud Shell \*\*button at the top of the console window to open the Cloud Shell.

![Google Cloud Platform (Project Info Page)](https://cdn-images-1.medium.com/max/3834/1*Mbcd4RlkCcz98Pbf4KSUAA.png)

Execute the following code in Cloud Shell to clone the GitHub repository used in this tutorial.

```
git clone https://github.com/pycaret/pycaret-deployment-google.git
```

![git clone https://github.com/pycaret/pycaret-deployment-google.git](https://cdn-images-1.medium.com/max/3838/1*g_RQ30jDG4UsyS84mh-qrw.png)

#### 👉 Step 3— Set Project ID Environment Variable

Execute the following code to set the PROJECT\_ID environment variable.

```
export PROJECT_ID=**pycaret-kubernetes-demo**
```

*pycaret-kubernetes-demo* is the name of the project we chose in step 1 above.

#### 👉 Step 4— Build the docker image

Build the docker image of the application and tag it for uploading by executing the following code:

```
docker build -t gcr.io/${PROJECT_ID}/insurance-app:v1 .
```

![Message returned when docker build is successful](https://cdn-images-1.medium.com/max/3834/1*Zo7_W7pG6JhFvHbzyQeEsA.png)

You can check the available images by running the following code:

```
docker images
```

![Output of “docker images” command on Cloud Shell](https://cdn-images-1.medium.com/max/3834/1*0paobe_W8tmdCF1xhX4BgA.png)

#### 👉 Step 5— Upload the container image

1. Authenticate to [Container Registry](https://cloud.google.com/container-registry) (you need to run this only once):

   gcloud auth configure-docker
2. Execute the following code to upload the docker image to Google Container Registry:

   docker push gcr.io/${PROJECT\_ID}/insurance-app:v1

#### 👉 Step 6— Create Cluster

Now that the container is uploaded, you need a cluster to run the container. A cluster consists of a pool of Compute Engine VM instances, running Kubernetes.

1. Set your project ID and Compute Engine zone options for the gcloud tool:

   gcloud config set project $PROJECT\_ID gcloud config set compute/zone **us-central1**
2. Create a cluster by executing the following code:

   gcloud container clusters create **insurance-cluster** --num-nodes=2

![Google Cloud Platform → Kubernetes Engine → Clusters](https://cdn-images-1.medium.com/max/3832/1*l2sHrv5nuFjDKiyAtjYapQ.png)

#### 👉 Step 7— Deploy Application

To deploy and manage applications on a GKE cluster, you must communicate with the Kubernetes cluster management system. Execute the following command to deploy the application:

```
kubectl create deployment insurance-app --image=gcr.io/${PROJECT_ID}/insurance-app:v1
```

![Output returned on creating deployment through kubectl](https://cdn-images-1.medium.com/max/3836/1*p0_A6PZnfYJ4mnttM7lzzA.png)

#### 👉 Step 8— Expose your application to the internet

By default, the containers you run on GKE are not accessible from the internet because they do not have external IP addresses. Execute the following code to expose the application to the internet:

```
kubectl expose deployment insurance-app --type=LoadBalancer --port 80 --target-port 8080
```

#### 👉 Step 9— Check Service

Execute the following code to get the status of the service. **EXTERNAL-IP** is the web address you can use in browser to view the published app.

```
kubectl get service
```

![Cloud Shell → kubectl get service](https://cdn-images-1.medium.com/max/3832/1*aRWl7frtmvPYaYjAoloFgQ.png)

👉 Step 10— See the app in action on <http://34.71.77.61:8080>

![Final app uploaded on http://34.71.77.61:8080](https://cdn-images-1.medium.com/max/3838/1*bKuZiYSPdE8T5SLKXx5B_Q.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

[Link to GitHub Repository for this tutorial](https://www.github.com/pycaret/pycaret-deployment-google)

[Link to GitHub Repository for Microsoft Azure Deployment](https://www.github.com/pycaret/pycaret-azure-deployment)

[Link to GitHub Repository for Heroku Deployment](https://www.github.com/pycaret/deployment-heroku)

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Deploy Machine Learning Pipeline on AWS Fargate

### Deploy Machine Learning Pipeline on AWS Fargate

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy ML pipeline serverless on AWS Fargate](https://cdn-images-1.medium.com/max/2000/1*-z21vlve2ZiyclbuFfFbJg.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) on deploying a machine learning pipeline in the cloud, we demonstrated how to develop a machine learning pipeline in PyCaret, containerize it with Docker and serve it as a web application using Google Kubernetes Engine. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will use the same machine learning pipeline and Flask app that we built and deployed previously. This time we will demonstrate how to containerize and deploy a machine learning pipeline serverless using AWS Fargate.

### 👉 Learning Goals of this Tutorial

* What is a Container? What is Docker? What is Kubernetes?
* What is Amazon Elastic Container Service (ECS)?
* What are AWS Fargate and serverless deployment?
* Build and push a Docker image onto Amazon Elastic Container Registry.
* Create and execute a task definition using AWS-managed infrastructure i.e. AWS Fargate.
* See a web app in action that uses a trained machine learning pipeline to predict new data points in real-time.

This tutorial will cover the entire workflow starting from building a docker image locally, uploading it onto Amazon Elastic Container Registry, creating a cluster and then defining and executing task using AWS-managed infrastructure i.e. AWS Fargate.

In the past, we have covered deployment on other cloud platforms such as Azure and Google. If you are interested in learning more about those, you can read the following stories:

* [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b)
* [Deploy Machine Learning Pipeline on AWS Web Service](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)
* [Build and deploy your first machine learning web app on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install pycaret
```

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a framework that allows you to build web applications. A web application can be a commercial website, blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models. If you don’t have Flask installed, you can use pip to install it.

### Docker Toolbox for Windows 10 Home

[Docker](https://www.docker.com/)\*\* \*\*is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers are used to package up an application with all of its necessary components, such as libraries and other dependencies, and ship it all out as one package. If you haven’t used docker before, this tutorial also covers the installation of Docker Toolbox (legacy) on **Windows 10 Home**. In the [previous tutorial](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) we covered how to install Docker Desktop on **Windows 10 Pro edition**.

### Amazon Web Services (AWS)

Amazon Web Services (AWS) is a comprehensive and broadly adopted cloud platform, offered by Amazon. It has over 175 fully-featured services from data centers globally. If you haven’t used AWS before, you can [sign-up](https://aws.amazon.com/) for a free account.

### ✔️Let’s get started…..

### What is a Container?

Before we get into implementation using AWS Fargate, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, he or she should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → The programing language such as Python and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

### What is Docker?

Docker is a company that provides software (also called **Docker**) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/).

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

Now that you theoretically understand what a container is and how Docker is used to containerize applications, let’s imagine a scenario where you have to run multiple containers across a fleet of machines to support an enterprise level machine learning application with varied workloads during day and night. This is pretty common for real-life and as simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, deal with failed containers or hardware and million other things!

This entire process of managing hundreds and thousands of containers to keep the application up and running is known as **container orchestration**. Don’t get caught up in the technical details yet.

At this point, you must recognize that managing real-life applications require more than one container and managing all of the infrastructure to keep containers up and running is cumbersome, manual and an administrative burden.

This brings us to **Kubernetes**.

### What is Kubernetes?

Kubernetes is an open-source system developed by Google in 2014 for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/23216/0*vGXFo8hG3fVCrJbN)

While Kubernetes is an open-source system developed by Google, almost all major cloud service providers offer Kubernetes as a Managed Service. For example: \*\*Amazon Elastic Kubernetes Service (EKS) **offered by Amazon**, Google Kubernetes Engine (GKE) **offered by Google**, \*\*and \*\*Azure Kubernetes Service (AKS) \*\*offered by Microsoft.

So far we have discussed and understood:

✔️ A ***container***

✔️ Docker

✔️ Kubernetes

Before introducing AWS Fargate, there is only one thing left to discuss and that is Amazon’s own container orchestration service **Amazon Elastic Container Service (ECS).**

### AWS Elastic Container Service (ECS)

Amazon Elastic Container Service (Amazon ECS) is Amazon’s home-grown container orchestration platform. The idea behind ECS is similar to Kubernetes *(both of them are orchestration services)*.

ECS is an AWS-native service, meaning that it is only possible to use on AWS infrastructure. On the other hand, **EKS** is based on Kubernetes, an open-source project which is available to users running on multi-cloud (AWS, GCP, Azure) and even On-Premise.

Amazon also offers a Kubernetes based container orchestration service known as \*\*Amazon Elastic Kubernetes Service (Amazon EKS). \*\*Even though the purpose of ECS and EKS is pretty similar i.e. *orchestrating containerized applications*, there are quite a few differences in pricing, compatibility and security. There is no best answer and the choice of solution depends on the use-case.

Irrespective of whichever container orchestration service you are using (ECS or EKS), there are two ways you can implement the underlying infrastructure:

1. Manually manage the cluster and underlying infrastructure such as Virtual Machines / Servers / (also known as EC2 instances in AWS).
2. Serverless — Absolutely no need to manage anything. Just upload the container and that’s it. ← **This is AWS Fargate.**

![Amazon ECS underlying infrastructure](https://cdn-images-1.medium.com/max/2798/1*k4famzZ1w2Ee5XMHRo1Ggw.png)

### AWS Fargate — serverless compute for containers

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. You only pay for the resources required to run your containers, so there is no over-provisioning and paying for additional servers.

![How AWS Fargate works — https://aws.amazon.com/fargate/](https://cdn-images-1.medium.com/max/4668/1*WWQBLhVao-FN_FCrnkPhQg.png)

There is no best answer as to which approach is better. The choice between going serverless or manually managing an EC2 cluster depends on the use-case. Some pointers that can assist with this choice include:

**ECS EC2 (Manual Approach)**

* You are all-in on AWS.
* You have a dedicated Ops team in place to manage AWS resources.
* You have an existing footprint on AWS i.e. you are already managing EC2 instances

**AWS Fargate**

* You do not have huge Ops team to manage AWS resources.
* You do not want operational responsibility or want to reduce it.
* Your application is stateless *(A stateless app is an application that does not save client data generated in one session for use in the next session with that client)*.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train and develop a machine learning pipeline for deployment.
* Build a web app using a Flask framework. It will use the trained ML pipeline to generate predictions on new data points in real-time.
* Build and push a Docker image onto Amazon Elastic Container Registry.
* Create and execute a task to deploy the app using AWS Fargate serverless infrastructure.

Since we have already covered the first two tasks in our initial tutorial, we will quickly recap them and then focus on the remaining items in the list above. If you are interested in learning more about developing a machine learning pipeline in Python using PyCaret and building a web app using a Flask framework, please read [this tutorial](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99).

### 👉 Develop a Machine Learning Pipeline

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*P7EXfIxqZZGrpeLgDdk1vQ.png)

### 👉 Build a Web Application

This tutorial is not focused on building a Flask application. It is only discussed here for completeness. Now that our machine learning pipeline is ready we need a web application that can connect to our trained pipeline to generate predictions on new data points in real-time. We have created the web application using Flask framework in Python. There are two parts of this application:

* Front-end (designed using HTML)
* Back-end (developed using Flask)

This is how our web application looks:

![Web application on local machine](https://cdn-images-1.medium.com/max/2800/1*EU4Cp9w1YHS2om8Mmfqh2g.png)

If you haven’t followed along so far, no problem. You can simply fork this [repository](https://www.github.com/pycaret/pycaret-deployment-aws) from GitHub. This is how your project folder should look at this point:

### 10-steps to deploy a ML pipeline using AWS Fargate:

#### 👉 Step 1 — Install Docker Toolbox (for Windows 10 Home)

In order to build a docker image locally, you will need Docker installed on your computer. If you are using Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later) you can download Docker Desktop from [DockerHub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).

However, if you are using Windows 10 Home, you would need to install the last release of legacy Docker Toolbox (v19.03.1) from [Dockers GitHub page](https://github.com/docker/toolbox/releases).

![https://github.com/docker/toolbox/releases](https://cdn-images-1.medium.com/max/2000/1*evIzHj_rmCk8iUhzQuUk0Q.png)

Download and Run **DockerToolbox-19.03.1.exe** file.

The easiest way to check if the installation was successful is by opening the command prompt and typing in ‘docker’. It should print the help menu.

![Anaconda Prompt to check docker](https://cdn-images-1.medium.com/max/2198/1*f5l4Tds3EOTFSPx6CT5M7w.png)

#### 👉 Step 2— Create a Dockerfile

The first step for creating a Docker image is to create a Dockerfile in the project directory. A Dockerfile is just a file with a set of instructions. The Dockerfile for this project looks like this:

A Dockerfile is case-sensitive and must be in the project folder with the other project files. A Dockerfile has no extension and can be created using any text editor. You can download the Dockerfile used in this project from this [GitHub Repository](https://www.github.com/pycaret/pycaret-deployment-aws).

#### 👉 Step 3— Create a Repository in Elastic Container Registry (ECR)

**(a) Login to your AWS console and search for Elastic Container Registry:**

![AWS Console](https://cdn-images-1.medium.com/max/3834/1*hRSh12jK8spjc98mf9lTvQ.png)

**(b) Create a new repository:**

![Create New Repository on Amazon Elastic Container Registry](https://cdn-images-1.medium.com/max/3828/1*Un0Vhv3Jaw5TkLhvRhEYSA.png)

*For this demo we have created ‘pycaret-deployment-aws-repository’.*

**(c) Click on “View push commands”:**

![pycaret-deployment-aws-repository](https://cdn-images-1.medium.com/max/3826/1*dsOf0Wn7GVs8P2eDMHsBcg.png)

**(d) Copy Push Commands:**

![Push commands for pycaret-deployment-aws-repository](https://cdn-images-1.medium.com/max/2032/1*lsBGf_Vb8xWVTjyJu0qhbw.png)

#### 👉 Step 4— Execute push commands

Navigate to your project folder using Anaconda Prompt and execute the commands you have copied in the step above. The code below is for demonstration only and may not work as it is. To get the right code to execute, you must get a copy of code from “View push commands” inside the repository.

You must be in the folder where the Dockerfile and the rest of your code reside before executing these commands.

```
**Command 1**
aws ecr get-login-password --region ca-central-1 | docker login --username AWS --password-stdin 212714531992.dkr.ecr.ca-central-1.amazonaws.com

**Command 2**
docker build -t pycaret-deployment-aws-repository .

**Command 3**
docker tag pycaret-deployment-aws-repository:latest 212714531992.dkr.ecr.ca-central-1.amazonaws.com/pycaret-deployment-aws-repository:latest

**Command 4**
docker push 212714531992.dkr.ecr.ca-central-1.amazonaws.com/pycaret-deployment-aws-repository:latest
```

#### 👉 Step 5— Check your uploaded image

Click on the repository you created and you will see an image URI of the uploaded image in the step above. Copy the image URI (it would be needed in step 7 below).

![](https://cdn-images-1.medium.com/max/3834/1*Y4fqgXHg8sQd3jQt-OtHaQ.png)

#### 👉 Step 6 — Create and Configure a Cluster

**(a) Click on “Clusters” on left-side menu:**

![Create Cluster — Step 1](https://cdn-images-1.medium.com/max/3832/1*SqYCrwX_Zg4IkYgx06NqCA.png)

**(b) Select “Networking only” and click Next step:**

![Select Networking Only Template](https://cdn-images-1.medium.com/max/2000/1*6ORi3iBEPvRS9uwAHbNcOg.png)

**(c) Configure Cluster (Enter cluster name) and click on Create:**

![Configure Cluster](https://cdn-images-1.medium.com/max/2000/1*q5HtOmTS8itYJVCrX5QgGg.png)

**(d) Cluster Created:**

![Cluster Created](https://cdn-images-1.medium.com/max/3744/1*vzl93C127k64ZSrnxUk_3g.png)

#### 👉 Step 7— Create a new Task definition

A **task** definition is required to run Docker containers in Amazon ECS. Some of the parameters you can specify in a **task** definition include: The Docker image to use with each container in your **task**. How much CPU and memory to use with each **task** or each container within a **task**.

**(a) Click on “Create new task definition”:**

![Create a new task definition](https://cdn-images-1.medium.com/max/3774/1*-qXr-OYzG6KNIGodUNX7fQ.png)

**(b) Select “FARGATE” as launch type:**

![Select Launch Type Compatibility](https://cdn-images-1.medium.com/max/2030/1*evmjs4KeHBUiYr7sEDsy3Q.png)

**(c) Fill in the details:**

![Configure Task and container definitions (part 1)](https://cdn-images-1.medium.com/max/2028/1*8mJVd9ICEyNsXW41P8a83g.png)

![Configure Task and container definitions (part 2)](https://cdn-images-1.medium.com/max/2000/1*8R5BmmT6JJ9rc5eyPRndfg.png)

**(d) Click on “Add Containers” and fill in the details:**

![Adding Container in task definitions](https://cdn-images-1.medium.com/max/2494/1*Ca3ueEM8MkaqSHYVISiasw.png)

**(e) Click “Create Task” on the bottom right.**

![](https://cdn-images-1.medium.com/max/3750/1*X9GdaMZsZufkmVTBLy-HPQ.png)

#### 👉 Step 8 —Execute Task Definition

In step 7 we created a task that will start the container. Now we will execute the task by clicking **“Run Task”** under Actions.

![Execute Task Definition](https://cdn-images-1.medium.com/max/3256/1*Sv3YF91f6E8wZyJSOU5Bdw.png)

**(a) Click on “Switch to launch type” to change the type to Fargate:**

![Running Task — Part 1](https://cdn-images-1.medium.com/max/2646/1*6mb1NPhQEGTad0210ra2eg.png)

**(b) Select the VPC and Subnet from the dropdown:**

![Running Task — Part 2](https://cdn-images-1.medium.com/max/2514/1*-llD_LjBr1PxSBYbscxsEg.png)

**(c) Click on “Run Task” on bottom right:**

![Task Created Successfully](https://cdn-images-1.medium.com/max/3236/1*9CKTS_xaTYxRo6l5PDq6Aw.png)

#### 👉 Step 9— Allow inbound port 5000 from Network settings

One last step before we can see our application in action on Public IP address is to allow port 5000 by creating a new rule. In order to do that, follow these steps:

**(a) Click on Task**

![](https://cdn-images-1.medium.com/max/3828/1*rtg6gCHCNXFQp_uiBF1jiw.png)

**(b) Click on ENI Id:**

![](https://cdn-images-1.medium.com/max/3184/1*iy3AvNVPkfbEbjDLcBQQng.png)

**(c) Click on Security groups**

![](https://cdn-images-1.medium.com/max/3302/1*Gce9zH8wQ0h2lGqvhulCXw.png)

**(d) Click on “Edit inbound rules”**

![](https://cdn-images-1.medium.com/max/3112/1*Jbk76SMfy6HhOCFpjlRNuQ.png)

**(e) Add a Custom TCP rule of port 5000**

![](https://cdn-images-1.medium.com/max/3568/1*RTCkc1QHT7PV0epSNt3vrQ.png)

#### 👉 Step 10 — See the app in action

Use public IP address with port 5000 to access the application.

![Task definition logs](https://cdn-images-1.medium.com/max/3214/1*BL9T96EM0VEJiQrdnA3WWQ.png)

![Final app uploaded on http://35.182.227.98:5000](https://cdn-images-1.medium.com/max/3830/1*YYoz3v8xU5wP01HWNswP8Q.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# Deploy ML Pipeline on the cloud with Docker

### Deploy Machine Learning Pipeline on the cloud using Docker Container

#### by Moez Ali

![](https://cdn-images-1.medium.com/max/2000/1*N3IRs4nRw4vcMt_AHmbkPA.png)

### **RECAP**

In our [last post](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99), we demonstrated how to develop a machine learning pipeline and deploy it as a web app using PyCaret and Flask framework in Python. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will use the same machine learning pipeline and Flask app that we built and deployed previously. This time we will demonstrate how to deploy a machine learning pipeline as a web app using the [Microsoft Azure Web App Service](https://azure.microsoft.com/en-us/services/app-service/web/).

In order to deploy a machine learning pipeline on Microsoft Azure, we will have to containerize our pipeline in a software called **“Docker”**. If you don’t know what does containerize means, *no problem* — this tutorial is all about that.

### 👉 Learning Goals of this Tutorial

* What is a container? What is Docker? and why do we need it?
* Build a Docker file on your local computer and publish it into [Azure Container Registry (ACR)](https://azure.microsoft.com/en-us/services/container-registry/).
* Deploy a web service on Azure using the container we uploaded into ACR.
* See a web app in action that uses a trained machine learning pipeline to predict on new data points in real-time.

In our last post, we covered the basics of model deployment and why it is needed. If you would like to learn more about model deployment, [click here](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) to read our last article.

This tutorial will cover the entire workflow of building a container locally to pushing it onto Azure Container Registry and then deploying our pre-trained machine learning pipeline and Flask app onto Azure Web Services.

![WORKFLOW: Create an image → Build container locally → Push to ACR → Deploy app on cloud](https://cdn-images-1.medium.com/max/2512/1*4McqTG9jDQvl_t-omPkEuA.png)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install **pycaret**
```

### Flask

[Flask](https://flask.palletsprojects.com/en/1.1.x/) is a framework that allows you to build web applications. A web application can be a commercial website, blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models. If you don’t have Flask installed, you can use pip to install it.

### **Docker**

[Docker](https://www.docker.com/)\*\* \*\*is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers are used to package up an application with all of its necessary components, such as libraries and other dependencies, and ship it all out as one package. If you haven’t used docker before, this tutorial also covers the installation of docker on Windows 10.

### **Microsoft Azure**

[Microsoft Azure](https://azure.microsoft.com/en-ca/overview/what-is-azure/) is a set of cloud services that is used to build, manage and deploy applications on a massive and global network. Other cloud services that are often used for deploying ML pipelines are [Amazon Web Services (AWS)](https://aws.amazon.com/), [Google Cloud](https://cloud.google.com), [IBM Cloud](https://www.ibm.com/cloud) and [Alibaba Cloud](https://www.alibabacloud.com/). We will cover most of them in our future tutorials.

If you haven’t used Microsoft Azure before you can [sign up](https://azure.microsoft.com/en-ca/free/search/?\&ef_id=EAIaIQobChMIm8Onqp6i6QIViY7ICh2QVA2jEAAYASAAEgK9FvD_BwE:G:s\&OCID=AID2000061_SEM_EAIaIQobChMIm8Onqp6i6QIViY7ICh2QVA2jEAAYASAAEgK9FvD_BwE:G:s\&dclid=CK6R8aueoukCFVbJyAoduGYLcQ) for a free account here. When you sign up for the first time you get a free credit for the first 30 days. You can utilize that credit in building your own web app by following this tutorial.

### What is a Container and why do we need it?

Have you ever had the problem where your python code (*or any other code*) works fine on your computer but when your friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, they should get the same results right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s Python environment is different than yours.

What does an environment include? → Python (*or any other language you have used*) and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can somehow create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Microsoft Azure), we can reproduce the results anywhere. Hence, **a** \*\*container \*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

> ## “Think about \*\*containers, \*\*when you think about containers.”

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

This is the most intuitive way to understand containers in data science. \*\*They are just like containers on a ship \*\*where the goal is to isolate the \*contents \*of one container from the others so they don’t get mixed up. This is exactly what containers are used for in data science.

Now that we understand the metaphor behind containers, let’s look at alternate options for creating an isolated environment for our application. One simple alternative is to have a separate machine for each of your applications.

(1 machine = 1 application = no conflict = everything is good)

Using a separate machine is straight forward but it doesn’t outweigh the benefits of using containers since maintaining multiple machines for each application is expensive, a nightmare-to-maintain and hard-to-scale. In short, it’s not practical in many real-life scenarios.

Another alternate for creating an isolated environment are \*\*virtual machines. \*\*Containers are again preferable here because they require fewer resources, are very portable, and are faster to spin up.

![Virtual Machines vs. Containers](https://cdn-images-1.medium.com/max/3840/1*snINBI0HUIYa0BWKyCO3Xg.jpeg)

Can you spot the difference between Virtual Machines and Containers? When you use containers, you do not require guest operating systems. Imagine 10 applications running on a virtual machine. This would require 10 guest operating systems compared to none required when you use containers.

#### I understand containers but what is Docker?

Docker is a company that provides software (also called Docker) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/) that provides container solution.

In this tutorial, we will use \*\*Docker Desktop for Windows \*\*to create a container that we will publish on Azure Container Registry. We will then deploy a web app using that container.

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

#### Docker Image vs. Docker Container

What is the difference between a docker image and a docker container? This is by far the most common question asked so let’s clear this right away. There are many technical definitions available, however, it is intuitive to think about a docker image as a mold based on which container is created. An image is essentially a snapshot of container.

If you prefer a slightly more technical definition then consider this: Docker images become containers at runtime when they run on a Docker Engine.

#### **Breaking the hype:**

At the end of the day, docker is just a file with a few lines of instructions that are saved under your project folder with the name ***“Dockerfile”***.

Another way to think about docker file is that they are like recipes you have invented in your own kitchen. When you share those recipes with somebody else and they follow the exact same instructions, they are able to produce the same dish. Similarly, you can share your docker file with other people, who can then create images and run containers based on that docker file.

Now that you understand containers, docker and why we should use them, let’s quickly set the business context.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train and develop a machine learning pipeline for deployment.
* Build a web app using Flask framework. It will use the trained ML pipeline to generate predictions on new data points in real-time.
* Create a docker image and container.
* Publish the container onto Azure Container Registry (ACR).
* Deploy the web app in the container by publishing onto ACR. Once deployed, it will become publicly available and can be accessed via a Web URL.

Since we have already covered the first two tasks in our last tutorial, we will quickly recap them and focus on the remaining tasks in the list above. If you are interested in learning more about developing machine learning pipeline in Python using PyCaret and building a web app using Flask framework, you can read our [last tutorial](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99).

### 👉 Develop Machine Learning Pipeline

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*NWoHVWJzO7i7gIvrlBnIiQ.png)

### 👉 Build Web Application

This tutorial is not focused on building a Flask application. It is only discussed here for completeness. Now that our machine learning pipeline is ready we need a web application that can connect to our trained pipeline to generate predictions on new data points in real-time. We have created the web application using Flask framework in Python. There are two parts of this application:

* Front-end (designed using HTML)
* Back-end (developed using Flask)

This is how our web application looks:

![Web application opened on local machine](https://cdn-images-1.medium.com/max/2800/1*EU4Cp9w1YHS2om8Mmfqh2g.png)

If you would like to see this web app in action, [click here](https://pycaret-insurance.herokuapp.com/) to open a deployed web app on Heroku (*It may take few minutes to open*).

If you haven’t followed along, no problem. You can simply fork this [repository](https://github.com/pycaret/deployment-heroku) from GitHub. If you don’t know how to fork a repo, please [read this](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) official GitHub tutorial. This is how your project folder should look at this point:

![https://github.com/pycaret/deployment-heroku](https://cdn-images-1.medium.com/max/2524/1*D2LzCUWv5au7AI6dsgGjUA.png)

Now that we have a fully functional web application, we can start the process of containerizing the app using Docker.

### 10-steps to deploy a ML pipeline in docker container:

#### 👉 **Step 1 — Install Docker Desktop for Windows**

You can use Docker Desktop on Mac as well as Windows. Depending on your operating system, you can download the Docker Desktop from [this link](https://docs.docker.com/docker-for-windows/install/). We will be using Docker Desktop for Windows in this tutorial.

![https://hub.docker.com/editions/community/docker-ce-desktop-windows/](https://cdn-images-1.medium.com/max/2692/1*jVBJIDIUyw9UJbzpv2zbpQ.png)

The easiest way to check if the installation was successful is by opening the command prompt and typing in ‘docker’. It should print the help menu.

![Command prompt](https://cdn-images-1.medium.com/max/2200/1*5XYrNYDi6XlLrmIO4ZNHdQ.png)

#### 👉 **Step 2 — Install Kitematic**

Kitematic is an intuitive graphical user interface (GUI) for running Docker containers on Windows or Mac. You can download Kitematic from [Docker’s GitHub repository](https://github.com/docker/kitematic/releases).

![https://github.com/docker/kitematic/releases](https://cdn-images-1.medium.com/max/2508/1*Tl5M7tNVH8smsnkaihxfpA.png)

Once downloaded, simply unzip the file into the desired location.

#### 👉 Step 3 — Create a Dockerfile

The first step of creating a Docker image is to create a Dockerfile. A Dockerfile is just a file with a set of instructions. The Dockerfile for this project looks like this:

Dockerfile is case-sensitive and must be in the project folder with the other project files. A Dockerfile has no extension and can be created using any editor. We have used [Visual Studio Code](https://code.visualstudio.com/) to create it.

#### 👉 Step 4— Create Azure Container Registry

If you don’t have a Microsoft Azure account or haven’t used it before, you can [sign up](https://azure.microsoft.com/en-ca/free/search/?\&ef_id=EAIaIQobChMIm8Onqp6i6QIViY7ICh2QVA2jEAAYASAAEgK9FvD_BwE:G:s\&OCID=AID2000061_SEM_EAIaIQobChMIm8Onqp6i6QIViY7ICh2QVA2jEAAYASAAEgK9FvD_BwE:G:s\&dclid=CK6R8aueoukCFVbJyAoduGYLcQ) for free. When you sign up for the first time you get a free credit for the first 30 days. You can utilize that credit to build and deploy a web app on Azure. Once you sign up, follow these steps:

* Login on <https://portal.azure.com>.
* Click on Create a Resource.
* Search for Container Registry and click on Create.
* Select Subscription, Resource group and Registry name (in our case: **pycaret.azurecr.io** is our registry name)

![https://portal.azure.com → Sign in → Create a Resource → Container Registry](https://cdn-images-1.medium.com/max/2560/1*InmsXcD7yfbeaMMzobwIJQ.png)

#### 👉 Step 5— Build Docker Image

Once a registry is created in Azure portal, the first step is to build a docker image using command line. Navigate to the project folder and execute the following code.

```
docker build -t pycaret.azurecr.io/pycaret-insurance:latest . 
```

![Building docker image using anaconda prompt](https://cdn-images-1.medium.com/max/2566/1*6cPcluJCHV8cpgziPXcGzw.png)

* **pycaret.azurecr.io** is the name of the registry that you get when you create a resource on Azure portal.
* **pycaret-insurance** is the name of the image and \*\*latest \*\*is the tag. This can be anything you want.

#### 👉 Step 6— Run container from docker image

Now that the image is created we will run a container locally and test the application before we push it to Azure Container Registry. To run the container locally execute the following code:

```
docker run -d -p 5000:5000 pycaret.azurecr.io/pycaret-insurance
```

Once this command is successfully executed it will return an ID of the container created.

![Running docker container locally](https://cdn-images-1.medium.com/max/2566/1*9g7OQNUA_8zLekDdWa3LHQ.png)

#### 👉 Step 7 — Test container on your local machine

Open Kitematic and you should be able to see an application up and running.

![Kitematic — A GUI for managing containers on Mac and Windows OS](https://cdn-images-1.medium.com/max/2690/1*CyJZ98AI5q7HbRa__-KWfg.png)

You can see the app in action by going to localhost:5000 in your internet browser. It should open up a web app.

![Application running on local container (localhost:5000)](https://cdn-images-1.medium.com/max/3824/1*wtDSmSt3Nsh1qQP7DC_kBg.png)

Make sure that once you are done with this, you stop the app using Kitematic, otherwise, it will continue to utilize resources on your computer.

#### 👉 Step 8— Authenticate Azure Credentials

One final step before you can upload the container onto ACR is to authenticate azure credentials on your local machine. Execute the following code in the command line to do that:

```
docker login pycaret.azurecr.io
```

You will be prompted for a Username and password. The username is the name of your registry (in this example username is “pycaret”). You can find your password under the Access keys of the Azure Container Registry resource you created.

![portal.azure.com → Azure Container Registry → Access keys](https://cdn-images-1.medium.com/max/3792/1*5pEA3466EIedSiPhe9CGcQ.png)

#### 👉 Step 9— Push Container onto Azure Container Registry

Now that you have authenticated to ACR, you can push the container you have created to ACR by executing the following code:

```
docker push pycaret.azurecr.io/pycaret-insurance:latest
```

Depending on the size of the container, the push command may take some time to transfer the container to the cloud.

#### 👉 Step 10— Create a Azure Web App and see your model in action

To create a web app on Azure, follow these steps:

* Login on <https://portal.azure.com>.
* Click on Create a Resource.
* Search for Web App and click on Create.
* Link your ACR image that you pushed in (step 9 above) to your app.

![portal.azure.com → Web App → Create → Basics](https://cdn-images-1.medium.com/max/2032/1*_4aEC8X867ybKhGrIl-L6A.png)

![portal.azure.com → Web App → Create → Docker](https://cdn-images-1.medium.com/max/2170/1*kcZWeLbntnrUKRWTE7EzkQ.png)

**BOOM!! The app is now up and running on Azure Web Services.**

![https://pycaret-insurance2.azurewebsites.net](https://cdn-images-1.medium.com/max/3812/1*zElHKEUtI_7NiEW6C5Z7dw.png)

**Note:** By the time this story is published, the app from <https://pycaret-insurance2.azurewebsites.net> will be removed to restrict resource consumption.

[\*\*Link to GitHub Repository for this tutorial.](https://github.com/pycaret/pycaret-deployment-azure)\*\*

[\*\*Link to GitHub Repository for Heroku Deployment.](https://www.github.com/pycaret/deployment-heroku) *(without docker)*\*\*

### Next Tutorial

In the next tutorial for deploying machine learning pipelines, we will dive deeper into deploying machine learning pipelines using the Kubernetes Service on Google Cloud and Microsoft Azure.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Clustering Analysis in Power BI using PyCaret

### How to implement Clustering in Power BI using PyCaret

#### by Moez Ali

![Clustering Dashboard in Power BI](https://cdn-images-1.medium.com/max/2632/1*sUeqYcENVII1RlyYA_-Uxg.png)

In our [last post](https://towardsdatascience.com/build-your-first-anomaly-detector-in-power-bi-using-pycaret-2b41b363244e), we demonstrated how to build an anomaly detector in Power BI by integrating it with PyCaret, thus allowing analysts and data scientists to add a layer of machine learning to their reports and dashboards without any additional license costs.

In this post, we will see how we can implement Clustering Analysis in Power BI using PyCaret. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

### Learning Goals of this Tutorial

* What is Clustering? Types of Clustering.
* Train and implement an unsupervised Clustering model in Power BI.
* Analyze results and visualize information in a dashboard.
* How to deploy the Clustering model in Power BI production?

### Before we start

If you have used Python before, it is likely that you already have Anaconda Distribution installed on your computer. If not, [click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/products/individual](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install pycaret. It’s a three-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Create an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and execute the following code:

```
conda create --name **myenv** python=3.7
```

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Install PyCaret**

Execute the following code in Anaconda Prompt:

```
pip install pycaret
```

Installation may take 15–20 minutes. If you are having issues with installation, please see our [GitHub](https://www.github.com/pycaret/pycaret) page for known issues and resolutions.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Set Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\AppData\Local\Continuum\anaconda3\envs\myenv

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*zQMKuyEk8LGrOPE-NByjrg.png)

### What is Clustering?

Clustering is a technique that groups data points with similar characteristics. These groupings are useful for exploring data, identifying patterns and analyzing a subset of data. Organising data into clusters helps in identify underlying structures in the data and finds applications across many industries. Some common business use cases for clustering are:

✔ Customer segmentation for the purpose of marketing.

✔ Customer purchasing behavior analysis for promotions and discounts.

✔ Identifying geo-clusters in an epidemic outbreak such as COVID-19.

### Types of Clustering

Given the subjective nature of clustering tasks, there are various algorithms that suit different types of problems. Each algorithm has its own rules and the mathematics behind how clusters are calculated.

This tutorial is about implementing a clustering analysis in Power BI using a Python library called PyCaret. Discussion of the specific algorithmic details and mathematics behind these algorithms are out-of-scope for this tutorial.

![Ghosal A., Nandy A., Das A.K., Goswami S., Panday M. (2020) A Short Review on Different Clustering Techniques and Their Applications.](https://cdn-images-1.medium.com/max/2726/1*2eQuIebjtTMJot27bWXgCQ.png)

In this tutorial we will use a K-Means algorithm which is one of the simplest and most popular unsupervised machine learning algorithms. If you would like to learn more about K-Means, you can read [this paper](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html).

### Setting the Business Context

In this tutorial we will use the current health expenditure dataset from the World Health Organization’s\*\*\* \*\*\*Global Health Expenditure database. The dataset contains health expenditure as a % of National GDP for over 200 countries from year 2000 through 2017.

Our objective is to find patterns and groups in this data by using a K-Means clustering algorithm.

[Source Data](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS)

![Sample Data points](https://cdn-images-1.medium.com/max/2366/1*E1z19x_qa7rko1FZpAw61Q.png)

### 👉 Let’s get started

Now that you have set up the Anaconda Environment, installed PyCaret, understand the basics of Clustering Analysis and have the business context for this tutorial, let’s get started.

### 1. Get Data

The first step is importing the dataset into Power BI Desktop. You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

![Power BI Desktop → Get Data → Other → Web](https://cdn-images-1.medium.com/max/3842/1*JZ3MwRe8rJXp5e0ac7lamw.png)

Link to csv file: <https://github.com/pycaret/powerbi-clustering/blob/master/clustering.csv>

### 2. Model Training

To train a clustering model in Power BI we will have to execute a Python script in Power Query Editor (Power Query Editor → Transform → Run python script). Run the following code as a Python script:

```
from **pycaret.clustering** import *
dataset = **get_clusters**(dataset, num_clusters=5, ignore_features=['Country'])
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*SK0XxzF9XZlwtGH1786OUQ.png)

We have ignored the ‘*Country*’ column in the dataset using the **ignore\_features** parameter. There could be many reasons for which you might not want to use certain columns for training a machine learning algorithm.

PyCaret allows you to hide instead of drop unneeded columns from a dataset as you might require those columns for later analysis. For example, in this case we don’t want to use ‘Country’ for training an algorithm and hence we have passed it under **ignore\_features.**

There are over 8 ready-to-use clustering algorithms available in PyCaret.

![](https://cdn-images-1.medium.com/max/2632/1*ihezKFr61Vrgu7E-0-JA5g.png)

By default, PyCaret trains a \*\*K-Means Clustering model \*\*with 4 clusters. Default values can be changed easily:

* To change the model type use the \*\*\*model \*\*\*parameter within **get\_clusters()**.
* To change the cluster number, use the \*\*\*num\_clusters \*\*\*parameter.

See the example code for **K-Modes Clustering** with 6 clusters.

```
from **pycaret.clustering **import *
dataset = **get_clusters**(dataset, model='kmodes', num_clusters=6, ignore_features=['Country'])
```

**Output:**

![Clustering Results (after execution of Python code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/3848/1*a6mAzuXC8Ta6gRyolaF5uA.png)

A new column which contains the cluster label is attached to the original dataset. All the year columns are then \*unpivoted \*to normalize the data so it can be used for visualization in Power BI.

Here’s how the final output looks like in Power BI.

![Results in Power BI Desktop (after applying query)](https://cdn-images-1.medium.com/max/2564/1*oy_X3VIdVPS32qQxkOeehw.png)

### 3. Dashboard

Once you have cluster labels in Power BI, here’s an example of how you can visualize it in dashboard to generate insights:

![Summary page of Dashboard](https://cdn-images-1.medium.com/max/2632/1*sUeqYcENVII1RlyYA_-Uxg.png)

![Details page of Dashboard](https://cdn-images-1.medium.com/max/2632/1*1ck--1zR_hRPqREKDC7ztg.png)

You can download the PBIX file and the data set from our [GitHub](https://github.com/pycaret/powerbi-clustering).

### 👉 Implementing Clustering in Production

What has been demonstrated above was one simple way to implement Clustering in Power BI. However, it is important to note that the method shown above trains the clustering model every time the Power BI dataset is refreshed. This may be a problem for two reasons:

* When the model is re-trained with new data, the cluster labels may change (eg: some data points that were labeled as Cluster 1 earlier might be labelled as Cluster 2 when re-trained)
* You don’t want to spend hours of time everyday re-training the model.

A more productive way to implement clustering in Power BI is to use a pre-trained model for generating cluster labels instead of re-training the model every time.

### Training Model before-hand

You can use any Integrated Development Environment (IDE)or Notebook for training machine learning models. In this example, we have used Visual Studio Code to train a clustering model.

![Model Training in Visual Studio Code](https://cdn-images-1.medium.com/max/2000/1*5roevyCmjxWthy0bYyf4ow.png)

A trained model is then saved as a pickle file and imported into Power Query for generating cluster labels.

![Clustering Pipeline saved as a pickle file](https://cdn-images-1.medium.com/max/2000/1*XxknQxv_O_Cx1WJ4kzwPkQ.png)

If you would like to learn more about implementing Clustering Analysis in Jupyter notebook using PyCaret, watch this 2 minute video tutorial:

### Using the pre-trained model

Execute the below code as a Python script to generate labels from the pre-trained model.

```
from **pycaret.clustering **import *
dataset = **predict_model**('c:/.../clustering_deployment_20052020, data = dataset)
```

The output of this will be the same as the one we saw above. The difference is that when you use a pre-trained model, the label is generated on a new dataset using the same model instead of re-training the model.

### Making it work on Power BI Service

Once you’ve uploaded the .pbix file to the Power BI service, a couple more steps are necessary to enable seamless integration of the machine learning pipeline into your data pipeline. These include:

* **Enable scheduled refresh for the dataset** — to enable a scheduled refresh for the workbook that contains your dataset with Python scripts, see [Configuring scheduled refresh](https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh), which also includes information about **Personal Gateway**.
* **Install the Personal Gateway** — you need a **Personal Gateway** installed on the machine where the file is located, and where Python is installed; the Power BI service must have access to that Python environment. You can get more information on how to [install and configure Personal Gateway](https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-personal-mode).

If you are Interested in learning more about Clustering Analysis, checkout our [Notebook Tutorial](https://www.pycaret.org/clu101).

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Deploy PyCaret Models on edge with ONNX Runtime

### Deploy PyCaret Models on Edge Devices with ONNX Runtime

#### A step-by-step tutorial on how to convert ML models trained using PyCaret to ONNX for high-performance scoring (CPU or GPU)

![Photo by Austin Distel on Unsplash](https://cdn-images-1.medium.com/max/12668/0*X79bEMfw0xAW7nKT)

### Introduction

In this tutorial, I will show you how you can train machine learning models using [PyCaret](https://www.pycaret.org/) — an open-source, low-code machine learning library in Python—and convert them in ONNX format for deployment on an edge device or any other non-Python environment. For example, you can train machine learning models using PyCaret in Python and deploy them in R, Java, or C. The Learning Goals of this tutorial are:

👉 What is PyCaret and how to get started?

👉 What are different types of model formats (pickle, onnx, pmml, etc.)

👉 What is ONNX (*pronounced as ONEX*) and what are its benefits?

👉 Train machine learning model using PyCaret and convert it in ONNX for deployment on edge.

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. PyCaret is known for its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end machine learning pipelines. To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

**Features:**

![PyCaret — An open-source, low-code machine learning library in Python](https://cdn-images-1.medium.com/max/2084/1*sESpLOGhMa2U1FsFdxxzIQ.png)

### skl2onnx

[skl2onnx](https://github.com/onnx/sklearn-onnx) is an open-source project that converts scikit-learn models to ONNX. Once in the ONNX format, you can use tools like ONNX Runtime for high-performance scoring. This project was started by the engineers and data scientists at Microsoft in 2017. To learn more about this project, check out their [GitHub](https://github.com/onnx/sklearn-onnx).

### Install

You will need to install the following libraries for this tutorial. The installation will take only a few minutes.

```
**# install pycaret
**pip install pycaret

**# install skl2onnx
**pip install skl2onnx

**# install onnxruntime
**pip install onnxruntime
```

### Different Model Formats

Before I introduce ONNX and the benefits, let’s see what are the different model formats available today for deployment.

### 👉**Pickle**

This is the most common format and default way of saving model objects into files for many Python libraries including PyCaret. [Pickle](https://docs.python.org/3/library/pickle.html) converts a Python object to a bitstream and allows it to be stored to disk and reloaded at a later time. It provides a good format to store machine learning models provided that the inference applications are also built-in python.

### 👉PMML

Predictive model markup language (PMML) is another format for machine learning models, relatively less common than Pickle. PMML has been around since 1997 and so has a large footprint of applications leveraging the format. Applications such as SAP \*\*and PEGA CRM are able to leverage certain versions of the PMML. There are open-source libraries available that can convert scikit-learn models (PyCaret) to PMML. The biggest drawback of the PMML format is that it doesn’t support all machine learning models.

### 👉ONNX

[ONNX](https://github.com/onnx), the Open Neural Network Exchange Format is an open format that supports the storing and porting of machine learning models across libraries and languages. This means that you can train your machine learning model using any framework in any language and then convert it into ONNX that can be used to generate inference in any environment (be it Java, C, .Net, Android, etc.). This language-agnostic capability of ONNX makes it really powerful compared to the other formats (For example You cannot use a model saved as a Pickle file in any other language than Python).

### What is ONNX?

[ONNX](https://onnx.ai/) is an open format to represent both deep learning and traditional models. With ONNX, AI developers can more easily move models between state-of-the-art tools and choose the combination that is best for them. ONNX is developed and supported by a community of partners such as Microsoft, Facebook, and AWS.

ONNX is widely supported and can be found in many frameworks, tools, and hardware. Enabling interoperability between different frameworks and streamlining the path from research to production helps increase the speed of innovation in the AI community. ONNX helps to solve the challenge of hardware dependency related to AI models and enables deploying the same AI models to several HW accelerated targets.

***Source: Microsoft***

![https://microsoft.github.io/ai-at-edge/docs/onnx/](https://cdn-images-1.medium.com/max/2000/0*9WvPLwTrLDynzQGM.PNG)

There are many excellent machine learning libraries in various languages — PyTorch, TensorFlow, scikit-learn, PyCaret, etc. The idea is that you can train a model with any tool, language, or framework and then deploy it using another language or application for inference and prediction. For example, let’s say you have a web application built with .Net, an Android app, or even an edge device and you want to integrate your machine learning model predictions into those downstream systems. You can do that by converting your model into ONNX format. *You cannot do that with Pickle or PMML format.*

### **Key Benefits:**

#### 👉 Interoperability

Develop in your preferred framework without worrying about downstream inferencing implications. ONNX enables you to use your preferred framework with your chosen inference engine.

#### 👉Hardware Access

ONNX makes it easier to access hardware optimizations. Use ONNX-compatible runtimes and libraries designed to maximize performance across hardware. This means that you can even use ONNX models on GPU for inference if latency is something you care about.

![Compatibility vs. Interoperability](https://cdn-images-1.medium.com/max/2000/0*CNFZ8AKtAPwDYki3.png)

### 👉Let's Get Started

### Dataset

For this tutorial, I am using a regression dataset from PyCaret’s repository called ***insurance***. You can download the data from [here](https://github.com/pycaret/pycaret/blob/master/datasets/insurance.csv).

![Sample Dataset](https://cdn-images-1.medium.com/max/2000/0*AlNXvwqZitdNOLUJ.png)

```
**# loading dataset
**from pycaret.datasets import get_data
data = get_data('insurance')

**# initialize setup / data preparation
**from pycaret.regression import *
s = setup(data, target = 'charges')
```

![Output from the setup function (compressed for display purpose)](https://cdn-images-1.medium.com/max/2000/1*wRI5YKWljqvtzKHNnc4osQ.png)

### 👉 Model Training & Selection

Now that data is ready for modeling, let’s start the training process by using compare\_models function. It will train all the algorithms available in the model library and evaluates multiple performance metrics using k-fold cross-validation.

```
**# compare all models**
best = compare_models()
```

![Output from compare\_models](https://cdn-images-1.medium.com/max/2000/1*7aZp9Tt2oPIyw6xbdzlnLQ.png)

Based on cross-validation metrics the best model is \*\*\*Gradient Boosting Regressor. \*\*\*You can save the model as a Pickle file with the save\_model function.

```
**# save model to drive
**save_model(best, 'c:/users/models/insurance')
```

This will save the model in a Pickle format.

### 👉 Generate Predictions using Pickle format

You can load the saved model back in the Python environment with the load\_model function and generate inference using predict\_model function.

```
**# load the model
**from pycaret.regression import load_model
loaded_model = load_model('c:/users/models/insurance')

**# generate predictions / inference
**from pycaret.regression import predict_model
pred = predict_model(loaded_model, data=data) # new data
```

![Predictions generated on the test set](https://cdn-images-1.medium.com/max/2000/1*vjO887TVlqS9H2utp2rY9A.png)

### 👉 ONNX Conversion

So far what we have seen is saving and loading trained models in Pickle format (which is the default format for PyCaret). However, using the skl2onnx library we can convert the model in ONNX:

```
**# convert best model to onnx**
from skl2onnx import to_onnx
X_sample = get_config('X_train')[:1]
model_onnx = to_onnx(best, X_sample.to_numpy())
```

We can also save the model\_onnx to local drive:

```
**# save the model to drive**
with open("c:/users/models/insurance.onnx", "wb") as f:
    f.write(model_onnx.SerializeToString())
```

Now to generate the inference from the insurance.onnx we will use onnxruntime library in Python (just to demonstrate the point). Essentially you can now use this insurance.onnx in any other platform or environment.

```
**# generate inference on onnx**
from onnxruntime import InferenceSession
sess = InferenceSession(model_onnx.SerializeToString())
X_test = get_config('X_test').to_numpy()
predictions_onnx = sess.run(None, {'X': X_test})[0]

**# print predictions_onnx
**print(predictions_onnx)
```

![predictions\_onnx](https://cdn-images-1.medium.com/max/2000/1*GnEcu24SeB7y2--rYT0qyA.png)

Notice that the output from predictions\_onnx is a numpy array compared to the pandas DataFrame when we have used predict\_model function from PyCaret but if you match the values, the numbers are all same (*with ONNX sometimes you will find minor differences beyond the 4th decimal point — very rarely*).

> **Mission Accomplished!**

### Coming Soon!

Next week I will take a deep dive into ONNX conversions and talk about how to convert the entire machine learning pipelines (*including imputers and transformers*) into ONNX. If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2412/0*PLdJpNCTXdttEn8W.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2402/0*IvqhUYDstXqz55eF.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### More PyCaret related tutorials:

[**Machine Learning in Alteryx with PyCaret** *A step-by-step tutorial on training and deploying machine learning models in Alteryx Designer using PyCaret*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-alteryx-with-pycaret-fafd52e2d4a) [**Machine Learning in KNIME with PyCaret** *A step-by-step guide on training and deploying end-to-end machine learning pipelines in KNIME using PyCaret*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-knime-with-pycaret-420346e133e2) [**Easy MLOps with PyCaret + MLflow** *A beginner-friendly, step-by-step tutorial on integrating MLOps in your Machine Learning experiments using PyCaret*towardsdatascience.com](https://towardsdatascience.com/easy-mlops-with-pycaret-mlflow-7fbcbf1e38c6) [**Write and train your own custom machine learning models using PyCaret** towardsdatascience.com](https://towardsdatascience.com/write-and-train-your-own-custom-machine-learning-models-using-pycaret-8fa76237374e) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe)


# GitHub is the best AutoML you will ever need

### GitHub is the best AutoML you will ever need

#### by Moez Ali

![PyCaret — An open source, low-code machine learning library in Python!](https://cdn-images-1.medium.com/max/2000/1*Qe1H5nFp506CKQJto0XU9A.png)

You may be wondering since when did GitHub get into the business of Automated Machine Learning. Well, it didn’t but you can use it for testing your personalized AutoML software. In this tutorial, we will show you how to build and containerize your own Automated Machine Learning software and test it on GitHub using Docker container.

We will use PyCaret 2.0, an open source, low-code machine learning library in Python to develop a simple AutoML solution and deploy it as a Docker container using GitHub actions. If you haven’t heard about PyCaret before, you can read official announcement for PyCaret 2.0 [here](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e) or check the detailed release notes [here](https://github.com/pycaret/pycaret/releases/tag/2.0).

### 👉 Learning Goals of this Tutorial

* Understanding what Automated Machine Learning is and how to build a simple AutoML software using PyCaret 2.0.
* Understand what is a container and how to deploy your AutoML solution as a Docker container.
* What are GitHub actions and how can you use them to test your AutoML.

### What is Automated Machine Learning?

Automated machine learning (AutoML) is a process of automating the time consuming, iterative tasks of machine learning. It allows data scientists and analysts to build machine learning models with efficiency while sustaining the model quality. The final goal of any AutoML software is to finalize the best model based on some performance criteria.

Traditional machine learning model development process is resource-intensive, requiring significant domain knowledge and time to produce and compare dozens of models. With automated machine learning, you’ll accelerate the time it takes to develop production-ready ML models with great ease and efficiency.

There are many AutoML software out there, paid as well as open source. Almost all of them use the same collection of transformations and base algorithms. Hence the quality and performances of the models trained under such software are approximately the same.

Paid AutoML software as a service are very expensive and financially infeasible if you does not have dozens of use-cases in your back pocket. Managed machine learning as a service platforms are relatively less expensive, but they are often hard to use and require knowledge of the specific platform.

Among many other open source AutoML libraries, PyCaret is relatively a new library and has a unique low-code approach to machine learning. The design and functionality of PyCaret is simple, human friendly, and intuitive. In short amount of time, PyCaret was adopted by over 100,000 data scientists globally and we are a growing community of developers.

### How Does PyCaret works?

PyCaret is a workflow automation tool for supervised and unsupervised machine learning. It is organized into six modules and each module has a set of functions available to perform some specific action. Each function takes an input and returns an output, which in most cases is a trained machine learning model. Modules available as of the second release are:

* [Classification](https://www.pycaret.org/classification)
* [Regression](https://www.pycaret.org/regression)
* [Clustering](https://www.pycaret.org/clustering)
* [Anomaly Detection](https://www.pycaret.org/anomaly-detection)
* [Natural Language Processing](https://www.pycaret.org/nlp)
* [Association Rule Mining](https://www.pycaret.org/association-rules)

All modules in PyCaret supports data preparation (over 25+ essential preprocessing techniques, comes with a huge collection of untrained models & support for custom models, automatic hyperparameter tuning, model analysis and interpretability, automatic model selection, experiment logging and easy cloud deployment options.

![https://www.pycaret.org/guide](https://cdn-images-1.medium.com/max/2066/1*wT0m1kx8WjY_P7hrM6KDbA.png)

To learn more about PyCaret, [click here](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e) to read our official release announcement.

If you want to get started in Python, [click here](https://github.com/pycaret/pycaret/tree/master/examples) to see a gallery of example notebooks to get started.

### 👉 Before we start

Let’s understand the following terminologies before starting to build an AutoML software. At this point all you need is some basic theoretical knowledge of these tools / terms that we are using in this tutorial. If you would like to go in more details, there are links at the end of this tutorial for you to explore later.

### **Container**

**Containers** provide a portable and consistent environment that can be deployed rapidly in different environments to maximize the accuracy, performance, and efficiency of **machine learning** applications. Environment contains run-time language (for e.g. Python), all the libraries, and the dependencies of your application.

### **Docker**

Docker is a company that provides software (also called Docker) that allows users to build, run, and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/) that also provide container solution.

### GitHub

[GitHub](https://www.github.com/) is a cloud-based service that is used to host, manage and control code. Imagine you are working in a large team where multiple people (sometime in hundreds) are making changes on the same code base. PyCaret is itself an example of an open-source project where hundreds of community developers are continuously contributing to source code. If you haven’t used GitHub before, you can [sign up](https://github.com/join) for a free account.

### **GitHub Actions**

GitHub Actions help you automate your software development workflows in the same place you store code and collaborate on pull requests and issues. You can write individual tasks, called actions, and combine them to create a custom workflow. Workflows are custom automated processes that you can set up in your repository to build, test, package, release, or deploy any code project on GitHub.

### 👉 Let’s get started

### Objective

To train and select the best performing regression model that predicts patient charges based on the other variables in the dataset i.e. age, sex, bmi, children, smoker, and region.

### 👉 **Step 1 — Develop app.py**

This is the main file for AutoML, which is also an entry point for Dockerfile (see below in step 2). If you have used PyCaret before then this code must be self-explanatory to you.

First five lines are about importing libraries and variables from the environment. Next three lines are for reading data as *pandas* dataframe. Line 12 to Line 15 is to import the relevant module based on environment variable and Line 17 onwards is about PyCaret’s functions to initialize the environment, compare base models and to save the best performing model on your device. The last line downloads the experiment logs as a csv file.

### 👉 Step 2— Create Dockerfile

Dockerfile is just a file with a few lines of instructions that are saved in your project folder with name “Dockerfile” (case-sensitive and no extension).

Another way to think about a Docker file is that it is like a recipe you have invented in your own kitchen. When you share such recipe with others and if they follow the exact same instructions in the recipe, they will able to reproduce the same dish with same quality. Similarly, you can share your docker file with others, who can then create images and run containers based on that docker file.

This Docker file for this project is simple and consist of 6 lines only. See below:

The first line in the Dockerfile imports the python:3.7-slim image. Next four lines create an app folder, update \*\*libgomp1 \*\*library, and install all the requirements from the \*\*requirements.txt \*\*file which in this case only requires pycaret. Finally, the last two lines define the entry point of your application; this means that when the container starts, it will execute the **app.py** file that we earlier saw above in step 1.

### 👉 Step 3 — Create action.yml

Docker actions require a metadata file. The metadata filename must be either action.yml or action.yaml. The data in the metadata file defines the inputs, outputs and main entrypoint for your action. Action file uses YAML syntax.

Environment variable dataset, target, and usecase are all declared in line 6, 9, and 14 respectively. See line 4–6 of app.py to understand how we have used these environment variables in our app.py file.

### 👉 Step 4 — Publish action on GitHub

At this point your project folder should look like this:

![https://github.com/pycaret/pycaret-git-actions](https://cdn-images-1.medium.com/max/2082/1*qBWs9Yk2Kgycu1wUtZe2Ow.png)

Click on **‘Releases’**:

![GitHub Action — Click on Releases](https://cdn-images-1.medium.com/max/2804/1*rrr51HMFW0Sc6gD4A0Agtg.png)

Draft a new release:

![GitHub Action — Draft a new release](https://cdn-images-1.medium.com/max/3698/1*od3eRb8OaoeRhW4IT5ZduA.png)

Fill in the details (tag, release title and description) and click on **‘Publish release’**:

![GitHub Action — Publish release](https://cdn-images-1.medium.com/max/2292/1*fW_n0JkZQEoUk-OBIP-4Sw.png)

Once published click on release and then click on **‘Marketplace’**:

![GitHub Action — Marketplace](https://cdn-images-1.medium.com/max/2814/1*Dfa9llJIIUw501qaAUomRw.png)

Click on **‘Use latest version’**:

![GitHub Action — use latest version](https://cdn-images-1.medium.com/max/2364/1*9F3GiDDYrIVcwvOmKIcMHA.png)

Save this information, this is the installation details of your software. This is what you will need to install this software on any public GitHub repository:

![GitHub Action — installation](https://cdn-images-1.medium.com/max/2000/1*UihPzGDhm2smpqOS2YW4Yg.png)

### 👉 Step 5— Install software on GitHub repository

To install and test the software we just created, we have created a new repository [\*\*pycaret-automl-test](https://github.com/pycaret/pycaret-automl-test) \*\*and uploaded a few sample datasets for classification and regression.

To install the software that we published in the previous step, click on ‘**Actions**’:

![https://github.com/pycaret/pycaret-automl-test/tree/master](https://cdn-images-1.medium.com/max/3776/1*MQKaHVJwqTZQWzwjNn5rcQ.png)

![Get started with GitHub Actions](https://cdn-images-1.medium.com/max/2000/1*h37nTkjLQhrbWRSwIL-VEQ.png)

Click on ‘**set up a workflow yourself**’ and copy this script into the editor and click on **‘Start commit’**.

This is an instruction file for GitHub to execute. First action starts from line 9. Line 9 to 15 is an action to install and execute the software we previously developed. Line 11 is where we have referenced the name of the software (see the last part of step 4 above). Line 13 to 15 is action to define environment variables such as the name of the dataset (csv file must be uploaded on the repository), name of the target variable, and usecase type. Line 16 onwards is another action from [this repository](https://github.com/actions/upload-artifact) to upload three files model.pkl, experiment logs as csv file, and system logs as a .log file.

Once you start commit, click on **‘actions’**:

![GitHub Action — Workflows](https://cdn-images-1.medium.com/max/2870/1*rYW8L7Yvtj1BIsFL18jquw.png)

This is where you can monitor the logs of your build as its building and once the workflow is completed, you can collect your files from this location as well.

![GitHub Action — Workflow build logs](https://cdn-images-1.medium.com/max/3062/1*SD4IMJjgg_PB-aAKxYDA0g.png)

![GitHub Action — Run Details](https://cdn-images-1.medium.com/max/3034/1*xmXuNcrm7pJ4F64R7mJXmQ.png)

You can download the files and unzip it on your device.

### **File: model**

This is a .pkl file for the final model along with the entire transformation pipeline. You can use this file to generate predictions on new dataset using predict\_model function. To learn more about it, [click here](https://www.pycaret.org/predict-model).

### File: experiment-logs

This is a .csv file that has all the details you will ever need for your model. It contains all the models that were trained in app.py script, their performance metrics, hyperparameters and other important meta data.

![experiment log file](https://cdn-images-1.medium.com/max/3830/1*i4fvedl-mtKMtOtWl2pfUQ.png)

### File: system-logs

This is a system logs file that PyCaret has generated. This can be used for auditing the process. It contains important meta deta information and is very useful for troubleshooting errors in your software.

![System logs file generated by PyCaret](https://cdn-images-1.medium.com/max/3838/1*QQ4Um9aRxLhyyLwW-oD4fg.png)

### **Disclosure**

GitHub Actions enables you to create custom software development lifecycle workflows directly in your GitHub repository. Each Account comes with included compute and storage quantities for use with Actions, depending on your Account plan, which can be found in the [Actions documentation](https://docs.github.com/en/github/automating-your-workflow-with-github-actions/about-github-actions#about-github-actions).

Actions and any elements of the Action service may not be used in violation of the Agreement, the [Acceptable Use Policy](https://docs.github.com/en/github/site-policy/github-acceptable-use-policies), or the GitHub Actions [service limitations](https://docs.github.com/en/github/automating-your-workflow-with-github-actions/about-github-actions#usage-limits). Additionally, Actions should not be used for:

* cryptomining;
* serverless computing;
* using our servers to disrupt, or to gain or to attempt to gain unauthorized access to, any service, device, data, account or network (other than those authorized by the [GitHub Bug Bounty program](https://bounty.github.com/))
* the provision of a stand-alone or integrated application or service offering Actions or any elements of Actions for commercial purposes; or,
* any other activity unrelated to the production, testing, deployment, or publication of the software project associated with the repository where GitHub Actions are used.

In order to prevent violations of these limitations and abuse of GitHub Actions, GitHub may monitor your use of GitHub Actions. Misuse of GitHub Actions may result in termination of jobs, or restrictions in your ability to use GitHub Actions.

### **Repositories used in this tutorial:**

[**pycaret/pycaret-git-actions** \*pycaret-git-actions. Contribute to pycaret/pycaret-git-actions development by creating an account on GitHub.\*github.com](https://github.com/pycaret/pycaret-git-actions) [**pycaret/pycaret-automl-test** \*pycaret-automl-test. Contribute to pycaret/pycaret-automl-test development by creating an account on GitHub.\*github.com](https://github.com/pycaret/pycaret-automl-test)

There is no limit to what you can achieve using this light-weight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our github repo.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

If you would like to learn more about PyCaret 2.0, read this [announcement](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e). If you have used PyCaret before, you might be interested in [release notes](https://github.com/pycaret/pycaret/releases/tag/2.0) for current release.

### You may also be interested it:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Blog](https://medium.com/@moez_62905) [Release Notes for PyCaret 2.0](https://github.com/pycaret/pycaret/releases/tag/2.0) [User Guide / Documentation](https://www.pycaret.org/guide)[ ](https://github.com/pycaret/pycaret/releases/tag/2.0)[Github](http://www.github.com/pycaret/pycaret) [Stackoverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)


# Deploy PyCaret and Streamlit on AWS Fargate

### Deploy PyCaret and Streamlit app using AWS Fargate — serverless infrastructure

#### by Moez Ali

![A step-by-step beginner’s guide to containerize and deploy ML pipeline serverless on AWS Fargate](https://cdn-images-1.medium.com/max/2000/1*QznGlPsGrGQS4DadTunLXw.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb), we demonstrated how to develop a machine learning pipeline using PyCaret and serve it as a Streamlit web application deployed onto Google Kubernetes Engine. If you haven’t heard about PyCaret before, you can read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to get started.

In this tutorial, we will use the same web app and machine learning pipeline that we had built previously and demonstrate how to deploy it using AWS Fargate which is a serverless compute for containers.

By the end of this tutorial, you will be able to build and host a fully functional containerized web app on AWS without provisioning any server infrastructure.

![Web Application](https://cdn-images-1.medium.com/max/2800/1*TesAmfCyanOeMEPiYxInUg.png)

### 👉 Learning Goals of this Tutorial

* What is a Container? What is Docker? What is Kubernetes?
* What is Amazon Elastic Container Service (ECS), AWS Fargate and serverless deployment?
* Build and push a Docker image onto Amazon Elastic Container Registry.
* Deploy web app using serverless infrastructure i.e. AWS Fargate.

This tutorial will cover the entire workflow starting from building a docker image locally, uploading it onto Amazon Elastic Container Registry, creating a cluster and then defining and executing task using AWS-managed infrastructure.

In the past, we have covered deployment on other cloud platforms such as Azure and Google. If you are interested in learning more about those, you can read the following tutorials:

* [Deploy Streamlit app onto Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)
* [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)
* [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)
* [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b)
* [Deploy Machine Learning Pipeline on AWS Web Service](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)
* [Build and deploy your first machine learning web app on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install pycaret
```

### Streamlit

[Streamlit](https://www.streamlit.io/) is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science. Streamlit can be installed easily using pip.

```
pip install streamlit
```

### Docker Toolbox for Windows 10 Home

[Docker](https://www.docker.com/)\*\* \*\*is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers are used to package up an application with all of its necessary components, such as libraries and other dependencies, and ship it all out as one package. If you haven’t used docker before, this tutorial also covers the installation of Docker Toolbox (legacy) on **Windows 10 Home**. In the [previous tutorial](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) we covered how to install Docker Desktop on **Windows 10 Pro edition**.

### Amazon Web Services (AWS)

Amazon Web Services (AWS) is a comprehensive and broadly adopted cloud platform, offered by Amazon. It has over 175 fully-featured services from data centers globally. If you haven’t used AWS before, you can [sign-up](https://aws.amazon.com/) for a free account.

### ✔️Let’s get started…..

### What is a Container?

Before we get into implementation using AWS Fargate, let’s understand what a container is and why we would need one?

![https://www.freepik.com/free-photos-vectors/cargo-ship](https://cdn-images-1.medium.com/max/2000/1*SlzsvRhA71oFOhAjE1Hs0A.jpeg)

Have you ever had the problem where your code works fine on your computer but when a friend tries to run the exact same code, it doesn’t work? If your friend is repeating the exact same steps, they should get the same results, right? The one-word answer to this is \*\**the environment*. \*\*Your friend’s environment is different than yours.

What does an environment include? → The programing language such as Python and all the libraries and dependencies with the exact versions using which application was built and tested.

If we can create an environment that we can transfer to other machines (for example: your friend’s computer or a cloud service provider like Google Cloud Platform), we can reproduce the results anywhere. Hence, \*\*\*a \*\*\*\*container \*\*\*is a type of software that packages up an application and all its dependencies so the application runs reliably from one computing environment to another.

### What is Docker?

Docker is a company that provides software (also called **Docker**) that allows users to build, run and manage containers. While Docker’s container are the most common, there are other less famous *alternatives* such as [LXD](https://linuxcontainers.org/lxd/introduction/) and [LXC](https://linuxcontainers.org/).

![](https://cdn-images-1.medium.com/max/2000/1*EJx9QN4ENSPKZuz51rC39w.png)

Now that you theoretically understand what a container is and how Docker is used to containerize applications, let’s imagine a scenario where you have to run multiple containers across a fleet of machines to support an enterprise level machine learning application with varied workloads during day and night. This is pretty common for real-life and as simple as it may sound, it is a lot of work to do manually.

You need to start the right containers at the right time, figure out how they can talk to each other, handle storage considerations, deal with failed containers or hardware and million other things!

This entire process of managing hundreds and thousands of containers to keep the application up and running is known as **container orchestration**. Don’t get caught up in the technical details yet.

At this point, you must recognize that managing real-life applications require more than one container and managing all of the infrastructure to keep containers up and running is cumbersome, manual and an administrative burden.

This brings us to **Kubernetes**.

### What is Kubernetes?

Kubernetes is an open-source system developed by Google in 2014 for managing containerized applications. In simple words, Kubernetes \*\*\*\*is a system for running and coordinating containerized applications across a cluster of machines.

![Photo by chuttersnap on Unsplash](https://cdn-images-1.medium.com/max/14720/0*vscKcwTh1qNmKv3s)

While Kubernetes is an open-source system developed by Google, almost all major cloud service providers offer Kubernetes as a Managed Service. For example: \*\*Amazon Elastic Kubernetes Service (EKS) **offered by Amazon**, Google Kubernetes Engine (GKE) **offered by Google**, \*\*and \*\*Azure Kubernetes Service (AKS) \*\*offered by Microsoft.

So far we have discussed and understood:

✔️ A ***container***

✔️ Docker

✔️ Kubernetes

Before introducing AWS Fargate, there is only one thing left to discuss and that is Amazon’s own container orchestration service **Amazon Elastic Container Service (ECS).**

### AWS Elastic Container Service (ECS)

Amazon Elastic Container Service (Amazon ECS) is Amazon’s home-grown container orchestration platform. The idea behind ECS is similar to Kubernetes *(both of them are orchestration services)*.

ECS is an AWS-native service, meaning that it is only possible to use on AWS infrastructure. On the other hand, **EKS** is based on Kubernetes, an open-source project which is available to users running on multi-cloud (AWS, GCP, Azure) and even On-Premise.

Amazon also offers a Kubernetes based container orchestration service known as \*\*Amazon Elastic Kubernetes Service (Amazon EKS). \*\*Even though the purpose of ECS and EKS is pretty similar i.e. *orchestrating containerized applications*, there are quite a few differences in pricing, compatibility and security. There is no best answer and the choice of solution depends on the use-case.

Irrespective of whichever container orchestration service you are using (ECS or EKS), there are two ways you can implement the underlying infrastructure:

1. Manually manage the cluster and underlying infrastructure such as Virtual Machines / Servers / (also known as EC2 instances).
2. Serverless — Absolutely no need to manage anything. Just upload the container and that’s it. ← **This is AWS Fargate.**

![Amazon ECS underlying infrastructure](https://cdn-images-1.medium.com/max/2798/1*k4famzZ1w2Ee5XMHRo1Ggw.png)

### AWS Fargate — serverless compute for containers

AWS Fargate is a serverless compute engine for containers that works with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). Fargate makes it easy for you to focus on building your applications. Fargate removes the need to provision and manage servers, lets you specify and pay for resources per application, and improves security through application isolation by design.

Fargate allocates the right amount of compute, eliminating the need to choose instances and scale cluster capacity. You only pay for the resources required to run your containers, so there is no over-provisioning and paying for additional servers.

![How AWS Fargate works — https://aws.amazon.com/fargate/](https://cdn-images-1.medium.com/max/4668/1*WWQBLhVao-FN_FCrnkPhQg.png)

There is no best answer as to which approach is better. The choice between going serverless or manually managing an EC2 cluster depends on the use-case. Some pointers that can assist with this choice include:

**ECS EC2 (Manual Approach)**

* You are all-in on AWS.
* You have a dedicated Ops team in place to manage AWS resources.
* You have an existing footprint on AWS i.e. you are already managing EC2 instances

**AWS Fargate**

* You do not have huge Ops team to manage AWS resources.
* You do not want operational responsibility or want to reduce it.
* Your application is stateless *(A stateless app is an application that does not save client data generated in one session for use in the next session with that client)*.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build and deploy a web application where the demographic and health information of a patient is entered into a web-based form which then outputs a predicted charge amount.

### Tasks

* Train, validate and develop a machine learning pipeline using PyCaret.
* Build a front-end web application with two functionalities: (i) online prediction and (ii) batch prediction.
* Create a Dockerfile
* Create and execute a task to deploy the app using AWS Fargate serverless infrastructure.

Since we have already covered the first two tasks in our [last tutorial](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb), we will quickly recap them and then focus on the remaining items in the list above. If you are interested in learning more about developing a machine learning pipeline in Python using PyCaret and building a web app using a Streamlit framework, please read [this tutorial](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104).

### 👉 Task 1 — Model Training and Validation

We are using PyCaret in Python for training and developing a machine learning pipeline which will be used as part of our web app. The Machine Learning Pipeline can be developed in an Integrated Development Environment (IDE) or Notebook. We have used a notebook to run the below code:

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created . All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Machine Learning Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*P7EXfIxqZZGrpeLgDdk1vQ.png)

### 👉 Task 2 — Build a front-end web application

Now that our machine learning pipeline and model are ready to start building a front-end web application that can generate predictions on new datapoints. This application will support ‘Online’ as well as ‘Batch’ predictions through a csv file upload. Let’s breakdown the application code into three main parts:

### Header / Layout

This section imports libraries, loads the trained model and creates a basic layout with a logo on top, a jpg image and a dropdown menu on the sidebar to toggle between ‘Online’ and ‘Batch’ prediction.

![app.py — code snippet part 1](https://cdn-images-1.medium.com/max/2268/1*xAnCZ1N_BNoPW7FoA-NXrA.png)

#### Online Predictions

This section deals with the initial app function, Online one-by-one predictions. We are using streamlit widgets such as *number input, text input, drop down menu and checkbox* to collect the datapoints used to train the model such as Age, Sex, BMI, Children, Smoker, Region.

![app.py — code snippet part 2](https://cdn-images-1.medium.com/max/2408/1*eFeq1wINsUUnvLJfuL-GOA.png)

#### Batch Predictions

Predictions by batch is the second layer of the app’s functionality. The **file\_uploader** widget in streamlit is used to upload a csv file and then called the native \*\*predict\_model() \*\*function from PyCaret to generate predictions that are displayed using streamlit’s write() function.

![app.py — code snippet part 3](https://cdn-images-1.medium.com/max/2410/1*u-g2iLy_gV7hom71PM3CEA.png)

\*\*Testing App \*\*One final step before we deploy the application on AWS Fargate is to test the app locally. Open Anaconda Prompt and navigate to your project folder and execute the following code:

```
streamlit run app.py
```

![Streamlit application testing — Online Prediction](https://cdn-images-1.medium.com/max/2800/1*TesAmfCyanOeMEPiYxInUg.png)

### 👉 Task 3 — Create a Dockerfile

To containerize our application for deployment we need a docker image that becomes a container at runtime. A docker image is created using a Dockerfile. A Dockerfile is just a file with a set of instructions. The Dockerfile for this project looks like this:

The last part of this Dockerfile (starting at line 23) is Streamlit specific. Dockerfile is case-sensitive and must be in the project folder with the other project files.

### 👉 Task 4–Deploy on AWS Fargate:

Follow these simple 9 steps to deploy app on AWS Fargate:

#### 👉 Step 1 — Install Docker Toolbox (for Windows 10 Home)

In order to build a docker image locally, you will need Docker installed on your computer. If you are using Windows 10 64-bit: Pro, Enterprise, or Education (Build 15063 or later) you can download Docker Desktop from [DockerHub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/).

However, if you are using Windows 10 Home, you would need to install the last release of legacy Docker Toolbox (v19.03.1) from [Dockers GitHub page](https://github.com/docker/toolbox/releases).

![https://github.com/docker/toolbox/releases](https://cdn-images-1.medium.com/max/2000/1*wn3zVxR0d5rZFDkvhEHi1Q.png)

Download and Run **DockerToolbox-19.03.1.exe** file.

The easiest way to check if the installation was successful is by opening the command prompt and typing in ‘docker’. It should print the help menu.

![Anaconda Prompt to check docker](https://cdn-images-1.medium.com/max/2198/1*f5l4Tds3EOTFSPx6CT5M7w.png)

#### 👉 Step 2 — Create a Repository in Elastic Container Registry (ECR)

**(a) Login to your AWS console and search for Elastic Container Registry:**

![AWS Console](https://cdn-images-1.medium.com/max/2000/1*XCvjm_Ho1CiaNg59y3MPiw.png)

**(b) Create a new repository:**

![Create New Repository on Amazon Elastic Container Registry](https://cdn-images-1.medium.com/max/3822/1*alFdHEfwYrdZ5J9d14gGgA.png)

![Create Repository](https://cdn-images-1.medium.com/max/3822/1*BeVF99WdFAPApWLS83SJ3Q.png)

Click on “Create Repository”.

**(c) Click on “View push commands”:**

![Push commands for pycaret-streamlit-aws repository](https://cdn-images-1.medium.com/max/2000/1*WC-0ShGuB0MB6LgTq07B0Q.png)

#### 👉 Step 3— Execute push commands

Navigate to your project folder using Anaconda Prompt and execute the commands you have copied in the step above. You must be in the folder where the Dockerfile and the rest of your code reside before executing these commands.

These commands are for building docker image and then uploading it on AWS ECR.

#### 👉 Step 4 — Check your uploaded image

Click on the repository you created and you will see an image URI of the uploaded image in the step above. Copy the image URI (it would be needed in step 6 below).

![](https://cdn-images-1.medium.com/max/3828/1*VuYsEXDoSmmHlEFfYgOAhg.png)

#### 👉 Step 5 — Create and Configure a Cluster

**(a) Click on “Clusters” on left-side menu:**

![Create Cluster — Step 1](https://cdn-images-1.medium.com/max/3834/1*eGOSlysIcdpDZi9GnPAhHw.png)

**(b) Select “Networking only” and click Next step:**

![Select Networking Only Template](https://cdn-images-1.medium.com/max/2000/1*a0VectBKdBhmZC_My5OylQ.png)

**(c) Configure Cluster (Enter cluster name) and click on Create:**

![Configure Cluster](https://cdn-images-1.medium.com/max/3780/1*6AMEaRIr4Rz1qt_ZmhDy4Q.png)

Click on “Create”.

**(d) Cluster Created:**

![Cluster Created](https://cdn-images-1.medium.com/max/3824/1*1UfMJt807V92-jc6Z9ZlfQ.png)

#### 👉 Step 6 — Create a new Task definition

A **task** definition is required to run Docker containers in Amazon ECS. Some of the parameters you can specify in a **task** definition include: The Docker image to use with each container in your **task**. How much CPU and memory to use with each **task** or each container within a **task**.

**(a) Click on “Create new task definition”:**

![Create a new task definition](https://cdn-images-1.medium.com/max/3820/1*6ET40juZ2owkA1xdDOsDHg.png)

**(b) Select “FARGATE” as launch type:**

![Select Launch Type Compatibility](https://cdn-images-1.medium.com/max/3822/1*1Ebz8wmfSisxcrultB86nQ.png)

**(c) Fill in the details:**

![Configure Task and container definitions (part 1)](https://cdn-images-1.medium.com/max/2000/1*JqrJPuts4QpVBUK2pKFPpg.png)

![Configure Task and container definitions (part 2)](https://cdn-images-1.medium.com/max/2000/1*SoM892EIZ2NpSzUCUg10rA.png)

**(d) Click on “Add Containers” and fill in the details:**

![Adding Container in task definitions](https://cdn-images-1.medium.com/max/2508/1*Kt9zGo0kk4bAUyrWhedU4Q.png)

Click “Create Task” on the bottom right.

![](https://cdn-images-1.medium.com/max/3828/1*DZpHXH5iy3daszNT4RYoEQ.png)

#### 👉 Step 7— Execute Task Definition

In last step we created a task that will start the container. Now we will execute the task by clicking **“Run Task”** under Actions.

![](https://cdn-images-1.medium.com/max/3836/1*nuUekT3eyCeDRoeZlTXk_Q.png)

**(a) Click on “Switch to launch type” to change the type to Fargate:**

![](https://cdn-images-1.medium.com/max/3850/1*_TMuygT58eKgMJQStWCwQw.png)

**(b) Select the VPC and Subnet from the dropdown:**

![](https://cdn-images-1.medium.com/max/3812/1*w7uipHeBNz9RhaBFsN85Bw.png)

Click on “Run Task” on bottom right.

#### 👉 Step 8— Allow inbound port 8501 from Network settings

One last step before we can see our application in action on Public IP address is to allow port 8501 (used by streamlit) by creating a new rule. In order to do that, follow these steps:

**(a) Click on Task**

![](https://cdn-images-1.medium.com/max/3834/1*lZh9LgN8vgctY3Xa_aeMrg.png)

**(b) Click on ENI Id:**

![](https://cdn-images-1.medium.com/max/3832/1*K1L_vExR8-2q-6b020voPQ.png)

**(c) Click on Security groups**

![](https://cdn-images-1.medium.com/max/3822/1*vPhVnBMZTXqBQj0ntWx5WA.png)

**(d) Scroll down and click on “Edit inbound rules”**

![](https://cdn-images-1.medium.com/max/3828/1*nWb74Ex5UWs-yJOZs5Ecew.png)

**(e) Add a Custom TCP rule of port 8501**

![](https://cdn-images-1.medium.com/max/3826/1*uqgV_Fr5NPGzWzwQ5LHAxw.png)

### 👉 Congratulations! You have published your app serverless on AWS Fargate. Use public IP address with port 8501 to access the application.

![App published on 99.79.189.46:8501](https://cdn-images-1.medium.com/max/3834/1*q9GXNH-YCL2vT7Q-Uj9clQ.png)

**Note:** By the time this story is published, the app will be removed from the public address to restrict resource consumption.

[Link to GitHub Repository for this tutorial](https://www.github.com/pycaret/pycaret-streamlit-aws)

[Link to GitHub Repository for Google Kubernetes Deployment](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

[Link to GitHub Repository for Heroku Deployment](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104)

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Classification](https://www.pycaret.org/clf101) [Regression](https://www.pycaret.org/reg101) [Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# Easy MLOps with PyCaret and MLflow

### Easy MLOps with PyCaret + MLflow

#### A beginner-friendly, step-by-step tutorial on integrating MLOps in your Machine Learning experiments using PyCaret

![Photo by Adi Goldstein on Unsplash](https://cdn-images-1.medium.com/max/7832/0*WSGn8A3YB42ALgSg)

### PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is known for its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end ML prototypes.

PyCaret is an alternate low-code library that can replace hundreds of code lines with few lines only. This makes the experiment cycle exponentially fast and efficient.

![PyCaret — An open-source, low-code machine learning library in Python](https://cdn-images-1.medium.com/max/2066/0*IOqb01w3mfxSYsRi.png)

To learn more about PyCaret, you can check out their [GitHub](https://www.github.com/pycaret/pycaret).

### MLflow

MLflow is an open-source platform to manage the ML lifecycle, including experimentation, reproducibility, deployment, and a central model registry. MLflow currently offers four components:

![MLflow is an open-source platform to manage ML lifecycle](https://cdn-images-1.medium.com/max/2852/1*EQ48xHBYlnqBKoas54URpQ.png)

To learn more about MLflow, you can check out [GitHub](https://github.com/mlflow/mlflow).

### Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret that only installs hard dependencies [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed. MLflow is part of PyCaret’s dependency and hence does not need to be installed separately.

### 👉 Let’s get started

Before I talk about MLOps, let’s talk a little bit about the machine learning lifecycle at a high level:

![Machine Learning Life Cycle — Image by Author (Read from left-to-right)](https://cdn-images-1.medium.com/max/2580/1*qYCj8HXZ0CUD4DROjU9MAg.png)

* \*\*Business Problem — \*\*This is the first step of the machine learning workflow. It may take from few days to a few weeks to complete, depending on the use case and complexity of the problem. It is at this stage, data scientists meet with subject matter experts (SME’s) to gain an understanding of the problem, interview key stakeholders, collect information, and set the overall expectations of the project.
* \*\*Data Sourcing & ETL — \*\*Once the problem understanding is achieved, it then comes to using the information gained during interviews to source the data from the enterprise database.
* \*\*Exploratory Data Analysis (EDA) — \*\*Modeling hasn’t started yet. EDA is where you analyze the raw data. Your goal is to explore the data and assess the quality of the data, missing values, feature distribution, correlation, etc.
* \*\*Data Preparation — \*\*Now it’s time to prepare the data model training. This includes things like dividing data into a train and test set, imputing missing values, one-hot-encoding, target encoding, feature engineering, feature selection, etc.
* \*\*Model Training & Selection — \*\*This is the step everyone is excited about. This involves training a bunch of models, tuning hyperparameters, model ensembling, evaluating performance metrics, model analysis such as AUC, Confusion Matrix, Residuals, etc, and finally selecting one best model to be deployed in production for business use.
* \*\*Deployment & Monitoring — \*\*This is the final step which is mostly about MLOps. This includes things like packaging your final model, creating a docker image, writing the scoring script, and then making it all work together, and finally publish it as an API that can be used to obtain predictions on the new data coming through the pipeline.

The old way of doing all this is pretty cumbersome, long, and requires a lot of technical know-how and I possibly cannot cover it in one tutorial. However, in this tutorial, I will use PyCaret to demonstrate how easy it has become for a data scientist to do all this very efficiently. Before we get to the practical part, let’s talk a little bit more about MLOps.

### 👉 **What is MLOps?**

MLOps is an engineering discipline that aims to combine machine learning development i.e. experimentation (model training, hyperparameter tuning, model ensembling, model selection, etc.), normally performed by Data Scientist with ML engineering and operations in order to standardize and streamline the continuous delivery of machine learning models in production.

If you are an absolute beginner, chances are you have no idea what I am talking about. No worries. Let me give you a simple, non-technical definition:

> \*MLOps are bunch of technical engineering and operational tasks that allows your machine learning model to be used by other users and applications accross the organization. Basically, it’s a way through which your work i.e. \*machine learning models *are published online, so other people can use them and satisfy some business objectives.*

This is a very toned-down definition of MLOps. In reality, it involved a little more work and benefits than this but it’s a good start for you if you are new to all this.

Now let’s follow the same workflow as shown in the diagram above to do a practical demo, make sure you have pycaret installed.

### 👉 Business Problem

For this tutorial, I will be using a very popular case study by Darden School of Business, published in [Harvard Business](https://hbsp.harvard.edu/product/UV0869-PDF-ENG). The case is regarding the story of two people who are going to be married in the future. The guy named \*Greg \*wanted to buy a ring to propose to a girl named *Sarah*. The problem is to find the ring Sarah will like, but after a suggestion from his close friend, Greg decides to buy a diamond stone instead so that Sarah can decide her choice. Greg then collects data of 6000 diamonds with their price and attributes like cut, color, shape, etc.

### 👉 Data

In this tutorial, I will be using a dataset from a very popular case study by the Darden School of Business, published in [Harvard Business](https://hbsp.harvard.edu/product/UV0869-PDF-ENG). The goal of this tutorial is to predict the diamond price based on its attributes like carat weight, cut, color, etc. You can download the dataset from [PyCaret’s repository](https://github.com/pycaret/pycaret/tree/master/datasets).

```
**# load the dataset from pycaret
**from pycaret.datasets import get_data
data = get_data('diamond')
```

![Sample rows from data](https://cdn-images-1.medium.com/max/2000/0*rDRvbnmVe7vDGPVM.png)

### 👉 Exploratory Data Analysis

Let’s do some quick visualization to assess the relationship of independent features (weight, cut, color, clarity, etc.) with the target variable i.e. Price

```
**# plot scatter carat_weight and Price**
import plotly.express as px
fig = px.scatter(x=data['Carat Weight'], y=data['Price'], 
                 facet_col = data['Cut'], opacity = 0.25, template = 'plotly_dark', trendline='ols',
                 trendline_color_override = 'red', title = 'SARAH GETS A DIAMOND - A CASE STUDY')
fig.show()
```

![Sarah gets a diamond case study](https://cdn-images-1.medium.com/max/2328/0*Lo6mo1OUPjb-Cenm.png)

Let’s check the distribution of the target variable.

```
**# plot histogram**
fig = px.histogram(data, x=["Price"], template = 'plotly_dark', title = 'Histogram of Price')
fig.show()
```

![](https://cdn-images-1.medium.com/max/2316/0*VjW1-hOpd7hVBtIj.png)

Notice that distribution of Price is right-skewed, we can quickly check to see if log transformation can make Price approximately normal to give fighting chance to algorithms that assume normality.

```
import numpy as np

**# create a copy of data**
data_copy = data.copy()

**# create a new feature Log_Price**
data_copy['Log_Price'] = np.log(data['Price'])

**# plot histogram**
fig = px.histogram(data_copy, x=["Log_Price"], title = 'Histgram of Log Price', template = 'plotly_dark')
fig.show()
```

![](https://cdn-images-1.medium.com/max/2322/0*KfvEU2c6f8LdjUPS.png)

This confirms our hypothesis. The transformation will help us to get away with skewness and make the target variable approximately normal. Based on this, we will transform the Price variable before training our models.

### 👉 Data Preparation

Common to all modules in PyCaret, the setup is the first and the only mandatory step in any machine learning experiment using PyCaret. This function takes care of all the data preparation required prior to training models. Besides performing some basic default processing tasks, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# initialize setup**
from pycaret.regression import *
s = setup(data, target = 'Price', transform_target = True, log_experiment = True, experiment_name = 'diamond')
```

![setup function in pycaret.regression module](https://cdn-images-1.medium.com/max/2736/0*dCiKXVXfpXyYQiYd.png)

When you initialize the setup function in PyCaret, it profiles the dataset and infers the data types for all input features. If all data types are correctly inferred, you can press enter to continue.

Notice that:

* I have passed log\_experiment = True and experiment\_name = 'diamond' , this will tell PyCaret to automatically log all the metrics, hyperparameters, and model artifacts behind the scene as you progress through the modeling phase. This is possible due to integration with [MLflow](https://www.mlflow.org).
* Also, I have used transform\_target = True inside the setup. PyCaret will transform the Price variable behind the scene using box-cox transformation. It affects the distribution of data in a similar way as log transformation *(technically different)*. If you would like to learn more about box-cox transformations, you can refer to this [link](https://onlinestatbook.com/2/transformations/box-cox.html).

![Output from setup — truncated for display](https://cdn-images-1.medium.com/max/2000/0*b5w1YKkwK2G9n_YA.png)

### 👉 Model Training & Selection

Now that data is ready for modeling, let’s start the training process by using compare\_models function. It will train all the algorithms available in the model library and evaluates multiple performance metrics using k-fold cross-validation.

```
**# compare all models**
best = compare_models()
```

![Output from compare\_models](https://cdn-images-1.medium.com/max/2000/0*FZAGMj-lU-C_kxRl.png)

```
**# check the residuals of trained model**
plot_model(best, plot = 'residuals_interactive')
```

![Residuals and QQ-Plot of the best model](https://cdn-images-1.medium.com/max/2590/0*yOzbuZjSXY4s2v4Z.png)

```
**# check feature importance**
plot_model(best, plot = 'feature')
```

![](https://cdn-images-1.medium.com/max/2068/0*m8k8VaglnYOkNx5x.png)

#### Finalize and Save Pipeline

Let’s now finalize the best model i.e. train the best model on the entire dataset including the test set and then save the pipeline as a pickle file.

```
**# finalize the model**
final_best = finalize_model(best)

**# save model to disk
**save_model(final_best, 'diamond-pipeline')
```

save\_model function will save the entire pipeline (including the model) as a pickle file on your local disk. By default, it will save the file in the same folder as your Notebook or script is in but you can pass the complete path as well if you would like:

```
save_model(final_best, 'c:/users/moez/models/diamond-pipeline'
```

### 👉 Deployment

Remember we passed log\_experiment = True in the setup function along with experiment\_name = 'diamond' . Let’s see the magic PyCaret has done with the help of MLflow behind the scene. To see the magic let’s initiate the MLflow server:

```
**# within notebook (notice ! sign infront)
**!mlflow ui

**# on command line in the same folder
**mlflow ui
```

Now open your browser and type “localhost:5000”. It will open a UI like this:

![https://localhost:5000](https://cdn-images-1.medium.com/max/3836/1*yZ4zThh0tnY0uW8SsLCpdw.png)

Each entry in the table above represents a training run resulting in a trained Pipeline and a bunch of metadata such as DateTime of a run, performance metrics, model hyperparameters, tags, etc. Let’s click on one of the models:

![Part I — CatBoost Regressor](https://cdn-images-1.medium.com/max/3776/1*TQEApDxCxDIoN6GWwvbBZw.png)

![Part II — CatBoost Regressor (continued)](https://cdn-images-1.medium.com/max/2438/1*RVC18B9Zk8rJkLp28jHkjA.png)

![Part II — CatBoost Regressor (continued)](https://cdn-images-1.medium.com/max/3392/1*1rsOUsPzyY3O0Djao2KlzQ.png)

Notice that you have an address path for the logged\_model. This is the trained Pipeline with Catboost Regressor. You can read this Pipeline using the load\_model function.

```
**# load model**
from pycaret.regression import load_model
pipeline = load_model('C:/Users/moezs/mlruns/1/b8c10d259b294b28a3e233a9d2c209c0/artifacts/model/model')

**# print pipeline
**print(pipeline)
```

![Output from print(pipeline)](https://cdn-images-1.medium.com/max/2916/1*E0dUApG1JQnddUfVHmCYvg.png)

Let’s now use this Pipeline to generate predictions on the new data

```
**# create a copy of data and drop Price
**data2 = data.copy()
data2.drop('Price', axis=1, inplace=True)

**# generate predictions
**from pycaret.regression import predict_model
predictions = predict_model(pipeline, data=data2)
predictions.head()
```

![Predictions generated from Pipeline](https://cdn-images-1.medium.com/max/2000/1*IVtFV6oRqcsgyNQTHbb3QA.png)

Woohoo! We now have inference from our trained Pipeline. Congrats, if this is your first one. Notice that all the transformations such as target transformation, one-hot-encoding, missing value imputation, etc. happened behind the scene automatically. You get a data frame with prediction in actual scale, and this is what you care about.

### Coming Soon!

What I have shown today is one out of many ways you can serve trained Pipelines from PyCaret in production with the help of MLflow. In the next tutorial, I plan to show how you can using MLflow native serving functionalities to register your models, version them and serve as an API.

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Clustering Analysis in Power BI using PyCaret

### How to implement Clustering in Power BI using PyCaret

#### by Moez Ali

![Clustering Dashboard in Power BI](https://cdn-images-1.medium.com/max/2632/1*sUeqYcENVII1RlyYA_-Uxg.png)

In our [last post](https://towardsdatascience.com/build-your-first-anomaly-detector-in-power-bi-using-pycaret-2b41b363244e), we demonstrated how to build an anomaly detector in Power BI by integrating it with PyCaret, thus allowing analysts and data scientists to add a layer of machine learning to their reports and dashboards without any additional license costs.

In this post, we will see how we can implement Clustering Analysis in Power BI using PyCaret. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

### Learning Goals of this Tutorial

* What is Clustering? Types of Clustering.
* Train and implement an unsupervised Clustering model in Power BI.
* Analyze results and visualize information in a dashboard.
* How to deploy the Clustering model in Power BI production?

### Before we start

If you have used Python before, it is likely that you already have Anaconda Distribution installed on your computer. If not, [click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/products/individual](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install pycaret. It’s a three-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Create an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and execute the following code:

```
conda create --name **myenv** python=3.7
```

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Install PyCaret**

Execute the following code in Anaconda Prompt:

```
pip install pycaret
```

Installation may take 15–20 minutes. If you are having issues with installation, please see our [GitHub](https://www.github.com/pycaret/pycaret) page for known issues and resolutions.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Set Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\AppData\Local\Continuum\anaconda3\envs\myenv

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*zQMKuyEk8LGrOPE-NByjrg.png)

### What is Clustering?

Clustering is a technique that groups data points with similar characteristics. These groupings are useful for exploring data, identifying patterns and analyzing a subset of data. Organising data into clusters helps in identify underlying structures in the data and finds applications across many industries. Some common business use cases for clustering are:

✔ Customer segmentation for the purpose of marketing.

✔ Customer purchasing behavior analysis for promotions and discounts.

✔ Identifying geo-clusters in an epidemic outbreak such as COVID-19.

### Types of Clustering

Given the subjective nature of clustering tasks, there are various algorithms that suit different types of problems. Each algorithm has its own rules and the mathematics behind how clusters are calculated.

This tutorial is about implementing a clustering analysis in Power BI using a Python library called PyCaret. Discussion of the specific algorithmic details and mathematics behind these algorithms are out-of-scope for this tutorial.

![Ghosal A., Nandy A., Das A.K., Goswami S., Panday M. (2020) A Short Review on Different Clustering Techniques and Their Applications.](https://cdn-images-1.medium.com/max/2726/1*2eQuIebjtTMJot27bWXgCQ.png)

In this tutorial we will use a K-Means algorithm which is one of the simplest and most popular unsupervised machine learning algorithms. If you would like to learn more about K-Means, you can read [this paper](https://stanford.edu/~cpiech/cs221/handouts/kmeans.html).

### Setting the Business Context

In this tutorial we will use the current health expenditure dataset from the World Health Organization’s\*\*\* \*\*\*Global Health Expenditure database. The dataset contains health expenditure as a % of National GDP for over 200 countries from year 2000 through 2017.

Our objective is to find patterns and groups in this data by using a K-Means clustering algorithm.

[Source Data](https://data.worldbank.org/indicator/SH.XPD.CHEX.GD.ZS)

![Sample Data points](https://cdn-images-1.medium.com/max/2366/1*E1z19x_qa7rko1FZpAw61Q.png)

### 👉 Let’s get started

Now that you have set up the Anaconda Environment, installed PyCaret, understand the basics of Clustering Analysis and have the business context for this tutorial, let’s get started.

### 1. Get Data

The first step is importing the dataset into Power BI Desktop. You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

![Power BI Desktop → Get Data → Other → Web](https://cdn-images-1.medium.com/max/3842/1*JZ3MwRe8rJXp5e0ac7lamw.png)

Link to csv file: <https://github.com/pycaret/powerbi-clustering/blob/master/clustering.csv>

### 2. Model Training

To train a clustering model in Power BI we will have to execute a Python script in Power Query Editor (Power Query Editor → Transform → Run python script). Run the following code as a Python script:

```
from **pycaret.clustering** import *
dataset = **get_clusters**(dataset, num_clusters=5, ignore_features=['Country'])
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*SK0XxzF9XZlwtGH1786OUQ.png)

We have ignored the ‘*Country*’ column in the dataset using the **ignore\_features** parameter. There could be many reasons for which you might not want to use certain columns for training a machine learning algorithm.

PyCaret allows you to hide instead of drop unneeded columns from a dataset as you might require those columns for later analysis. For example, in this case we don’t want to use ‘Country’ for training an algorithm and hence we have passed it under **ignore\_features.**

There are over 8 ready-to-use clustering algorithms available in PyCaret.

![](https://cdn-images-1.medium.com/max/2632/1*ihezKFr61Vrgu7E-0-JA5g.png)

By default, PyCaret trains a \*\*K-Means Clustering model \*\*with 4 clusters. Default values can be changed easily:

* To change the model type use the \*\*\*model \*\*\*parameter within **get\_clusters()**.
* To change the cluster number, use the \*\*\*num\_clusters \*\*\*parameter.

See the example code for **K-Modes Clustering** with 6 clusters.

```
from **pycaret.clustering **import *
dataset = **get_clusters**(dataset, model='kmodes', num_clusters=6, ignore_features=['Country'])
```

**Output:**

![Clustering Results (after execution of Python code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/3848/1*a6mAzuXC8Ta6gRyolaF5uA.png)

A new column which contains the cluster label is attached to the original dataset. All the year columns are then \*unpivoted \*to normalize the data so it can be used for visualization in Power BI.

Here’s how the final output looks like in Power BI.

![Results in Power BI Desktop (after applying query)](https://cdn-images-1.medium.com/max/2564/1*oy_X3VIdVPS32qQxkOeehw.png)

### 3. Dashboard

Once you have cluster labels in Power BI, here’s an example of how you can visualize it in dashboard to generate insights:

![Summary page of Dashboard](https://cdn-images-1.medium.com/max/2632/1*sUeqYcENVII1RlyYA_-Uxg.png)

![Details page of Dashboard](https://cdn-images-1.medium.com/max/2632/1*1ck--1zR_hRPqREKDC7ztg.png)

You can download the PBIX file and the data set from our [GitHub](https://github.com/pycaret/powerbi-clustering).

### 👉 Implementing Clustering in Production

What has been demonstrated above was one simple way to implement Clustering in Power BI. However, it is important to note that the method shown above trains the clustering model every time the Power BI dataset is refreshed. This may be a problem for two reasons:

* When the model is re-trained with new data, the cluster labels may change (eg: some data points that were labeled as Cluster 1 earlier might be labelled as Cluster 2 when re-trained)
* You don’t want to spend hours of time everyday re-training the model.

A more productive way to implement clustering in Power BI is to use a pre-trained model for generating cluster labels instead of re-training the model every time.

### Training Model before-hand

You can use any Integrated Development Environment (IDE)or Notebook for training machine learning models. In this example, we have used Visual Studio Code to train a clustering model.

![Model Training in Visual Studio Code](https://cdn-images-1.medium.com/max/2000/1*5roevyCmjxWthy0bYyf4ow.png)

A trained model is then saved as a pickle file and imported into Power Query for generating cluster labels.

![Clustering Pipeline saved as a pickle file](https://cdn-images-1.medium.com/max/2000/1*XxknQxv_O_Cx1WJ4kzwPkQ.png)

If you would like to learn more about implementing Clustering Analysis in Jupyter notebook using PyCaret, watch this 2 minute video tutorial:

### Using the pre-trained model

Execute the below code as a Python script to generate labels from the pre-trained model.

```
from **pycaret.clustering **import *
dataset = **predict_model**('c:/.../clustering_deployment_20052020, data = dataset)
```

The output of this will be the same as the one we saw above. The difference is that when you use a pre-trained model, the label is generated on a new dataset using the same model instead of re-training the model.

### Making it work on Power BI Service

Once you’ve uploaded the .pbix file to the Power BI service, a couple more steps are necessary to enable seamless integration of the machine learning pipeline into your data pipeline. These include:

* **Enable scheduled refresh for the dataset** — to enable a scheduled refresh for the workbook that contains your dataset with Python scripts, see [Configuring scheduled refresh](https://docs.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh), which also includes information about **Personal Gateway**.
* **Install the Personal Gateway** — you need a **Personal Gateway** installed on the machine where the file is located, and where Python is installed; the Power BI service must have access to that Python environment. You can get more information on how to [install and configure Personal Gateway](https://docs.microsoft.com/en-us/power-bi/connect-data/service-gateway-personal-mode).

If you are Interested in learning more about Clustering Analysis, checkout our [Notebook Tutorial](https://www.pycaret.org/clu101).

### PyCaret 1.0.1 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 1.0.1 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Machine Learning in Alteryx with PyCaret

### Machine Learning in Alteryx with PyCaret

#### A step-by-step tutorial on training and deploying machine learning models in Alteryx Designer using PyCaret

![](https://cdn-images-1.medium.com/max/2000/1*T6OjmWCOMcsm8wi0xQcjeQ.jpeg)

### Introduction

In this tutorial, I will show you how you can train and deploy machine learning pipelines in a very popular ETL tool [Alteryx](https://www.alteryx.com) using [PyCaret](https://www.pycaret.org) — an open-source, low-code machine learning library in Python. The Learning Goals of this tutorial are:

👉 What is PyCaret and how to get started?

👉 What is Alteryx Designer and how to set it up?

👉 Train end-to-end machine learning pipeline in Alteryx Designer including data preparation such as missing value imputation, one-hot-encoding, scaling, transformations, etc.

👉 Deploy trained pipeline and generate inference during ETL.

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. PyCaret is known for its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end machine learning pipelines. To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

### Alteryx Designer

[Alteryx Designer](https://www.alteryx.com/products/alteryx-platform/alteryx-designer) is a proprietary tool developed by [\*\*Alteryx](https://www.alteryx.com)\*\* and is used for automating every step of analytics, including data preparation, blending, reporting, predictive analytics, and data science. You can access any data source, file, application, or data type, and experience the simplicity and power of a self-service platform with 260+ drag-and-drop building blocks. You can download the one-month free trial version of Alteryx Designer from [here](https://www.alteryx.com/designer-trial/alteryx-free-trial).

![https://www.alteryx.com](https://cdn-images-1.medium.com/max/3648/1*OeDHEH-vFx2u3nF69Wu3DQ.png)

### Tutorial Pre-Requisites:

For this tutorial, you will need two things. The first one being the Alteryx Designer which is a desktop software that you can download from [here](https://www.alteryx.com/designer-trial/alteryx-free-trial). Second, you need Python. The easiest way to get Python is to download Anaconda Distribution. To download that, [click here](https://www.anaconda.com/distribution/).

### 👉We are ready now

Open Alteryx Designer and click on File → New Workflow

![New Workflow in Alteryx Designer](https://cdn-images-1.medium.com/max/3818/1*O7on438FoX76Ou9vjFDGpw.png)

On the top, there are tools that you can drag and drop on the canvas and execute the workflow by connecting each component to one another.

### Dataset

For this tutorial, I am using a regression dataset from PyCaret’s repository called ***insurance***. You can download the data from [here](https://github.com/pycaret/pycaret/blob/master/datasets/insurance.csv).

![Sample Dataset](https://cdn-images-1.medium.com/max/2000/0*_5ZOcQ4IBD55ADn6.png)

I will create two separate Alteryx workflows. First one for **model training and selection** and the second one for **scoring the new data** using the trained pipeline.

### 👉 Model Training & Selection

Let’s first read the CSV file from the \*\*Input Data \*\*tool followed by a \*\*Python Script. \*\*Inside the Python script execute the following code:

```
**# install pycaret
**from ayx import Package
Package.installPackages('pycaret')

**# read data from input data tool**
from ayx import Alteryx
data = Alteryx.read("#1")

**# init setup, prepare data**
from pycaret.regression import *
s = setup(data, target = 'charges', silent=True)

**# model training and selection
**best = compare_models()

**# store the results, print and save**
results = pull()
results.to_csv('c:/users/moezs/pycaret-demo-alteryx/results.csv', index = False)
Alteryx.write(results, 1)

**# finalize best model and save**
best_final = finalize_model(best)
save_model(best_final, 'c:/users/moezs/pycaret-demo-alteryx/pipeline')
```

This script is importing the regression module from pycaret, then initializing the setup function which automatically handles train\_test\_split and all the data preparation tasks such as missing value imputation, scaling, feature engineering, etc. compare\_models trains and evaluates all the estimators using kfold cross-validation and returns the best model.

pull function calls the model performance metric as a Dataframe which is then saved as results.csv on a drive and also written to the first anchor of Python tool in Alteryx (so that you can view results on screen).

Finally, save\_model saves the entire transformation pipeline including the best model as a pickle file.

![Training Workflow](https://cdn-images-1.medium.com/max/3836/1*2qny4Iy7SNePSpT7fZWSuw.png)

When you successfully execute this workflow, you will generate pipeline.pkl and results.csv file. You can see the output of the best models and their cross-validated metrics on-screen as well.

![](https://cdn-images-1.medium.com/max/2000/1*Vc6Pr88a6cxVfxxUGSp9yg.png)

This is what results.csv contains:

![](https://cdn-images-1.medium.com/max/2000/0*u9dRI79LDdDOrvw5.png)

These are the cross-validated metrics for all the models. The best model, in this case, is ***Gradient Boosting Regressor***.

### 👉 Model Scoring

We can now use our pipeline.pkl to score on the new dataset. Since I do not have a separate dataset for \*\*\*insurance.csv ***without the label***, \*\*\*what I will do is drop the target column i.e. ***charges**,* and then generate predictions using the trained pipeline.

![Scoring Workflow](https://cdn-images-1.medium.com/max/3830/1*ZVEhi6EdcXg_dKINWisR0g.png)

I have used the \*\*Select Tool \*\*to remove the target column i.e. charges . In the Python script execute the following code:

```
**# read data from the input tool**
from ayx import Alteryx**
**data = Alteryx.read("#1")

**# load pipeline
**from pycaret.regression import load_model, predict_model
pipeline = load_model('c:/users/moezs/pycaret-demo-alteryx/pipeline')

**# generate predictions and save to csv
**predictions = predict_model(pipeline, data)
predictions.to_csv('c:/users/moezs/pycaret-demo-alteryx/predictions.csv', index=False)

**# display in alteryx
**Alteryx.write(predictions, 1)
```

When you successfully execute this workflow, it will generate predictions.csv.

![predictions.csv](https://cdn-images-1.medium.com/max/2000/0*v6pthOCcVwNMww9S.png)

### Coming Soon!

Next week I will take a deep dive and focus on more advanced functionalities of PyCaret that you can use within Alteryx to enhance your machine learning workflows. If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2412/0*PLdJpNCTXdttEn8W.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2402/0*IvqhUYDstXqz55eF.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### More PyCaret related tutorials:

[**Machine Learning in KNIME with PyCaret** *A step-by-step guide on training and deploying end-to-end machine learning pipelines in KNIME using PyCaret*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-knime-with-pycaret-420346e133e2) [**Easy MLOps with PyCaret + MLflow** *A beginner-friendly, step-by-step tutorial on integrating MLOps in your Machine Learning experiments using PyCaret*towardsdatascience.com](https://towardsdatascience.com/easy-mlops-with-pycaret-mlflow-7fbcbf1e38c6) [**Write and train your own custom machine learning models using PyCaret** towardsdatascience.com](https://towardsdatascience.com/write-and-train-your-own-custom-machine-learning-models-using-pycaret-8fa76237374e) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe)


# Machine Learning in KNIME with PyCaret

### Machine Learning in KNIME with PyCaret

#### A step-by-step guide on training and scoring machine learning models in KNIME using PyCaret

![PyCaret is an open-source Python library and KNIME is an open-source data analytics platform](https://cdn-images-1.medium.com/max/2000/1*GCzo1_0f0E9HyK9jm7B2-w.png)

### PyCaret

[PyCaret](https://www.pycaret.org) is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. Its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end machine learning pipelines will amaze you.

PyCaret is an alternate low-code library that can replace hundreds of lines of code with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is \*\*simple and easy to use. \*\*All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it’s imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it. To learn more about PyCaret, watch this 1-minute video.

### KNIME

[KNIME Analytics Platform](https://www.knime.com/knime-analytics-platform) is open-source software for creating data science. Intuitive, open, and continuously integrating new developments, KNIME makes understanding data and designing data science workflows and reusable components accessible to everyone.

KNIME Analytics platform is one of the most popular open-source platforms used in data science to automate the data science process. KNIME has thousands of nodes in the node repository which allows you to drag and drop the nodes into the KNIME workbench. A collection of interrelated nodes creates a workflow that can be executed locally as well as can be executed in the KNIME web portal after deploying the workflow into the KNIME server.

![KNIME Analytics Platform — Creating Data Science](https://cdn-images-1.medium.com/max/2000/0*ct-Ux9jTTyDYyYHZ)

### Installation

For this tutorial, you will need two things. The first one being the KNIME Analytics Platform which is a desktop software that you can download from [here](https://www.knime.com/downloads). Second, you need Python.

The easiest way to get started with Python is to download Anaconda Distribution. To download, [click here](https://www.anaconda.com/distribution/).

Once you have both the KNIME Analytics Platform and Python installed, you need to create a separate conda environment in which we will install PyCaret. Open the Anaconda prompt and run the following commands:

```
***# create a conda environment*
**conda create --name knimeenv python=3.6

***# activate environment*
**conda activate knimeenv

***# install pycaret*
**pip install pycaret
```

Now open the KNIME Analytics Platform and go to File → Install KNIME Extensions → KNIME & Extensions → and select KNIME Python Extension and install it.

Once installation completes, go to File → Preferences → KNIME → Python and select your Python 3 environment. Notice that in my case the name of the environment is “powerbi”. If you have followed the commands above, the name of the environment is “knimeenv”.

![Python setup in KNIME Analytics Platform](https://cdn-images-1.medium.com/max/2000/1*KmNfJY16OzVldEbgfXh8kQ.png)

### 👉We are ready now

Click on “New KNIME Workflow” and a blank canvas will open.

![KNIME New Workflow](https://cdn-images-1.medium.com/max/3830/1*TdQQ1wfEMH487wd3zz9OJg.png)

On the left-hand side, there are tools that you can drag and drop on the canvas and execute the workflow by connecting each component to one another. All the actions in the repository on the left side are called *Nodes*.

### **Dataset**

For this tutorial, I am using a regression dataset from PyCaret’s repository called ‘insurance’. You can download the data from [here](https://github.com/pycaret/pycaret/blob/master/datasets/insurance.csv).

![Sample Dataset](https://cdn-images-1.medium.com/max/2000/1*mpP1hqC9HQ37WGQmdZAoFQ.png)

I will create two separate workflows. First one for model training and selection and the second one for scoring the new data using the trained pipeline.

### 👉 **Model Training & Selection**

Let’s first read the CSV file from the **CSV Reader** node followed by a \*\*Python Script. \*\*Inside the Python script execute the following code:

```
**# init setup, prepare data**
from pycaret.regression import *
s = setup(input_table_1, target = 'charges', silent=True)

**# model training and selection
**best = compare_models()

**# store the results, print and save**
output_table_1 = pull()
output_table_1.to_csv('c:/users/moezs/pycaret-demo-knime/results.csv', index = False)

**# finalize best model and save**
best_final = finalize_model(best)
save_model(best_final, 'c:/users/moezs/pycaret-demo-knime/pipeline')
```

This script is importing the regression module from pycaret, then initializing the setup function which automatically handles train\_test\_split and all the data preparation tasks such as missing value imputation, scaling, feature engineering, etc. compare\_models trains and evaluates all the estimators using kfold cross-validation and returns the best model. pull function calls the model performance metric as a Dataframe which is then saved as results.csv on a local drive. Finally, save\_model saves the entire transformation pipeline and model as a pickle file.

![Training Workflow](https://cdn-images-1.medium.com/max/2000/1*dgzEEn15t8NmEsKKKd9sBA.png)

When you successfully execute this workflow, you will generate pipeline.pkl and results.csv file in the defined folder.

![](https://cdn-images-1.medium.com/max/2000/1*d1rh9V4BApHEqNwXOR796A.png)

This is what results.csv contains:

![](https://cdn-images-1.medium.com/max/2000/1*8iQmxMyNmXW4NS5lzpOdWA.png)

These are the cross-validated metrics for all the models. The best model, in this case, is ***Gradient Boosting Regressor***.

### 👉 Model Scoring

We can now use our pipeline.pkl to score on the new dataset. Since I do not have a separate dataset for ‘insurance.csv’, what I will do is drop the target column from the same file, just to demonstrate.

![Scoring Workflow](https://cdn-images-1.medium.com/max/2000/1*JK5Dmk1_I7u7qa7Zrskv_A.png)

I have used the **Column Filter** node to remove the target column i.e. charges . In the Python script execute the following code:

```
**# load pipeline
**from pycaret.regression import load_model, predict_model
pipeline = load_model('c:/users/moezs/pycaret-demo-knime/pipeline')

**# generate predictions and save to csv**
output_table_1 = predict_model(pipeline, data = input_table_1)
output_table_1.to_csv('c:/users/moezs/pycaret-demo-knime/predictions.csv', index=False)
```

When you successfully execute this workflow, it will generate predictions.csv.

![predictions.csv](https://cdn-images-1.medium.com/max/2000/1*0NjNrFay0-93xe0pje8j_g.png)

I hope that you will appreciate the ease of use and simplicity in PyCaret. When used within an analytics platform like KNIME, it can save you many hours of coding and then maintaining that code in production. With less than 10 lines of code, I have trained and evaluated multiple models using PyCaret and deployed an ML Pipeline KNIME.

### Coming Soon!

Next week I will take a deep dive and focus on more advanced functionalities of PyCaret that you can use within KNIME to enhance your machine learning workflows. If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![Image by Author](https://cdn-images-1.medium.com/max/NaN/1*-Ul7wtRGqybl3eBm58ELcA.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/NaN/1*WSZ6hqiO_B3u5ReftUCGSA.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)

### More PyCaret related tutorials:

[**Easy MLOps with PyCaret + MLflow** *A beginner-friendly, step-by-step tutorial on integrating MLOps in your Machine Learning experiments using PyCaret*towardsdatascience.com](https://towardsdatascience.com/easy-mlops-with-pycaret-mlflow-7fbcbf1e38c6) [**Write and train your own custom machine learning models using PyCaret** towardsdatascience.com](https://towardsdatascience.com/write-and-train-your-own-custom-machine-learning-models-using-pycaret-8fa76237374e) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe) [**Time Series Forecasting with PyCaret Regression Module** *A step-by-step tutorial for time-series forecasting using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-forecasting-with-pycaret-regression-module-237b703a0c63) [**5 things you are doing wrong in PyCaret** *From the Creator of PyCaret*towardsdatascience.com](https://towardsdatascience.com/5-things-you-are-doing-wrong-in-pycaret-e01981575d2a) [**GitHub is the best AutoML you will ever need** *A step-by-step tutorial to build AutoML using PyCaret 2.0*towardsdatascience.com](https://towardsdatascience.com/github-is-the-best-automl-you-will-ever-need-5331f671f105) [**Build your own AutoML in Power BI using PyCaret** *A step-by-step tutorial to build AutoML solution in Power BI*towardsdatascience.com](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [**Deploy PyCaret and Streamlit app using AWS Fargate — serverless infrastructure** \*A step-by-step tutorial to containerize machine learning app and deploy it using AWS Fargate.\*towardsdatascience.com](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [**Deploy Machine Learning App built using Streamlit and PyCaret on Google Kubernetes Engine** *A step-by-step beginner’s guide to containerize and deploy a Streamlit app on Google Kubernetes Engine*towardsdatascience.com](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb) [**Build and deploy machine learning web app using PyCaret and Streamlit** *A beginner’s guide to deploying a machine learning app on Heroku PaaS*towardsdatascience.com](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [**Deploy Machine Learning Pipeline on AWS Fargate** *A beginner’s guide to containerize and deploy machine learning pipeline serverless on AWS Fargate*towardsdatascience.com](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [**Topic Modeling in Power BI using PyCaret** *A step-by-step tutorial for implementing Topic Model in Power BI*towardsdatascience.com](https://towardsdatascience.com/topic-modeling-in-power-bi-using-pycaret-54422b4e36d6) [**Deploy Machine Learning Pipeline on Google Kubernetes Engine** *A beginner’s guide to containerize and deploy machine learning pipeline on Google Kubernetes Engine*towardsdatascience.com](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [**How to implement Clustering in Power BI using PyCaret** *A step-by-step tutorial for implementing Clustering in Power BI*towardsdatascience.com](https://towardsdatascience.com/how-to-implement-clustering-in-power-bi-using-pycaret-4b5e34b1405b) [**Build your first Anomaly Detector in Power BI using PyCaret** *A step-by-step tutorial for implementing anomaly detection in Power BI*towardsdatascience.com](https://towardsdatascience.com/build-your-first-anomaly-detector-in-power-bi-using-pycaret-2b41b363244e) [**Deploy Machine Learning Pipeline on the cloud using Docker Container** \*A beginner’s guide to deploy machine learning pipelines on the cloud using PyCaret, Flask, Docker Container, and Azure Web…\*towardsdatascience.com](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [**Build and deploy your first machine learning web app** *A beginner’s guide to train and deploy machine learning pipelines in Python using PyCaret*towardsdatascience.com](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [**Machine Learning in Power BI using PyCaret** *A step-by-step tutorial for implementing machine learning in Power BI within minutes*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-power-bi-using-pycaret-34307f09394a)


# Machine Learning in SQL using PyCaret Part I

### Machine Learning in SQL using PyCaret

#### Ship your ML code to data by integrating PyCaret in SQL Server

#### by Umar Farooque

![](https://cdn-images-1.medium.com/max/8064/1*CxB6I95fPzYv_z9C6RRzVg.png)

This post is a **step-by-step tutorial** on how to train and deploy an Unsupervised Machine Learning Clustering model in SQL Server using [\*\*PyCaret](https://pycaret.org/)**(a low-code ML library in Python)**.\*\*

**Things we will cover in this article:**

1. How to download and install SQL Server for free
2. How to create a new database and importing data into a database
3. How to enable and use Python scripting in database
4. How to train a clustering algorithm in order to assign cluster labels to each observation in the dataset

### **I. Bringing Code to Data — The case for using Database for ML**

The go-to tools/ environments for performing ML experiments are Command-Line, IDEs, or Notebooks. However, such tools/environments may pose limitations when the data size gets very large, or when the ML model is required to be put in production. There has been a dire need to have the ability to programme and train models where data reside. MS SQL Server introduced this capability in their SQL Server version 2019. The distinct advantages of using SQL Server for Machine Learning are:

i. Extracting a large amount of data from the system is tedious and time-consuming. Conducting ML experiments on a server brings the code to data, rather than taking data to the code

ii. ML experiments are executed mostly in computer/cpu memory. Most of the machines hit a performance ceiling when training an ML algorithm on large data sets. ML on the SQL Server database avoids this

iii. It is easy to integrate and deploy ML Pipelines along with other ETL processes

### **II. SQL Server**

SQL Server is a Microsoft relational database management system. As a database server, it performs the primary function of storing and retrieving data as requested by different applications. In this tutorial, we will use [\*\*SQL Server 2019 \*\*\*\*Developer](https://www.microsoft.com/en-ca/sql-server/sql-server-downloads)\*\* for machine learning by importing PyCaret library into SQL Server.

### **III. Download Software**

If you have used SQL Server before, it is likely that you have it installed and have access to the database. If not, [\*\*click here](https://www.microsoft.com/en-ca/sql-server/sql-server-downloads)\*\* to download SQL Server 2019 Developer or other edition.

![](https://cdn-images-1.medium.com/max/2000/1*lt9GPAvrhixDQAP6iatTIQ.png)

### **IV. Setting up the Environment**

Before using PyCaret functionality into SQL Server, you’ll need to install SQL Server and PyCaret. This is a multi-step process:

#### Step 1 — Install SQL Server

Download the SQL Server 2019 Developer Edition file “**SQL2019-SSEI-Dev.exe**”

![](https://cdn-images-1.medium.com/max/2000/1*WYIssA8f1vpYIPced1miYA.png)

Open the file and follow the instructions to install (recommended to use Custom install option)

![](https://cdn-images-1.medium.com/max/2000/1*H2mr4UeI3q2DaidWtgldxQ.png)

Choose New SQL Server stand-alone installation

![](https://cdn-images-1.medium.com/max/2000/1*bxqUK4NIzdW7DW1LBKObiQ.png)

In the Instance Features option, select the features including “**Python**” under **Machine Learning Services and Language Extensions** and **Machine Learning Server (Standalone)**

![](https://cdn-images-1.medium.com/max/2000/1*OCXaVsXQmnGSBa5hPUh4GQ.png)

Click “**Accept**” to provide consent to install Python

![](https://cdn-images-1.medium.com/max/2000/1*rYm00TFsLe70EzW1503h1A.png)

Installation may take 15–20 minutes

#### Step 2 — Install Microsoft SQL Server Management Studio (SSMS)

[\*\*Click here](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?redirectedfrom=MSDN\&view=sql-server-ver15)\*\* or Open SQL Server Installation Center to download “SQL Server Management Tools” file “**SSMS-Setup-ENU.exe**”

![](https://cdn-images-1.medium.com/max/2000/1*VydYoU_rbKtzFKgsJ7fPpw.png)

Open “**SSMS-Setup-ENU.exe**” file to start the installation

![](https://cdn-images-1.medium.com/max/2000/1*Fnt_PmyaEh8AitkuQIy7og.png)

Installation may take 5–10 minutes

#### Step 3 — Create a database for Machine Learning

Once you have everything installed, you will need to start an instance of the server. To do so, start SSMS. At the login stage, you’ll be asked to the name of the SQL Server that you can choose from the drop-down menu. Once a connection is established, you can see all the objects from the server. If you have downloaded SQL Server for the first time and you do not have a database to work with, you will need to create a new database first.

In the Object Explorer panel, right-click on Databases, and choose New Database

![](https://cdn-images-1.medium.com/max/2000/1*4pzZ6-fk48V3ujaAIUhI2A.png)

Enter the database name and other information

The setup may take 2–3 minutes including creating a database, user and setting ownership

#### Step 4 — Import CSV File

You will now have to import a CSV file into a database using SQL Server Management Studio.

Create a table “**jewellery**” in the database

![](https://cdn-images-1.medium.com/max/2000/1*-kkwdIAo4GDkzZ1013GYog.png)

Right-click the database and select **Tasks** **->** **Import Data**

![](https://cdn-images-1.medium.com/max/2000/1*d07HzD7rwEr_SHkGsR_m-Q.png)

For Data Source, select **Flat File Source**. Then use the **Browse** button to select the CSV file. Spend some time configuring the data import before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/1*zNU8RuLdlIDNmoh93Mlu1w.png)

For Destination, select the correct database provider (e.g. SQL Server Native Client 11.0). Enter the **Server name**; check **Use SQL Server Authentication**, enter the **Username**, **Password**, and \*\*Database \*\*before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/1*jz9FIU8o-98-H_3vinmUfA.png)

In the Select Source Tables and Views window, you can Edit Mappings before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/1*q1RuWU3dVZmr0zvoVWrBLg.png)

Check Run immediately and click the \*\*Next \*\*button

![](https://cdn-images-1.medium.com/max/2000/1*P9yzJy0imJkl85yGgE6C7g.png)

Click the Finish button to run the package

![Data Loading Result](https://cdn-images-1.medium.com/max/2000/1*jBBq5kfftYJNR2DKWYmRuQ.png)

#### Step 5 — Enable SQL Server for Python Scripts

We will run Python “inside” the SQL Server by using the \*\*sp\_execute\_external\_script \*\*system stored procedure. To begin, you need to open a ‘**New Query**’. Execute the following query in your instance to enable the use of the procedure for remote script execution:

```
EXEC sp_configure ‘external scripts enabled’, 1

RECONFIGURE WITH OVERRIDE
```

**Note:** Restart the instance before proceeding to the next steps.

Following SQL Statements can be executed to check the Python path and list installed packages.

Check Python Path:

```
EXECUTE sp_execute_external_script

@language =N’Python’,

@script=N’import sys; print(“\n”.join(sys.path))’
```

![Script Execution Result](https://cdn-images-1.medium.com/max/2000/1*WDzLc0EXLpH1Zu3TEbfsiw.png)

List Installed Packages:

```
EXECUTE sp_execute_external_script

@language = N’Python’,

@script = N’

import pkg_resources

import pandas as pd

installed_packages = pkg_resources.working_set

installed_packages_list = sorted([“%s==%s” % (i.key, i.version) for i in installed_packages])

df = pd.DataFrame(installed_packages_list)

OutputDataSet = df’

WITH RESULT SETS (( PackageVersion nvarchar (150) ))
```

![Script Execution Result](https://cdn-images-1.medium.com/max/2000/1*1bSpU8-L-KYpzR_dDPaTPQ.png)

#### Step 6 — Adding PyCaret Python Package to SQL Server

To install PyCaret package, open a command prompt and browse to the location of Python packages where SQL Server is installed. The default location is:

```
C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\PYTHON_SERVICES
```

Navigate to “**Scripts**” directory and use pip command to install **PyCaret** package

```
pip.exe install pycaret
```

![Command Prompt — PyCaret Installation](https://cdn-images-1.medium.com/max/2000/1*EZ4cZxBOb6sJ8sTaObM5bA.png)

![Command Prompt — PyCaret Installation End](https://cdn-images-1.medium.com/max/2000/1*fAL6HpAkkuweGH_q90KU-Q.png)

**Note**: Make sure, you have access to the SQL Server directory to install package and/or change configurations. Otherwise, the package installation will fail.

Installation may take 5–10 minutes

**Note:** In case encounter issue about missing “*lightgbm*” module when running SQL script. Follow the instructions below:

i. Uninstall “*lightgbm*”

```
pip.exe uninstall lightgbm
```

ii. Reinstall “*lightgbm*”

```
pip.exe install lightgbm
```

Execute the following SQL to verify the PyCaret installation from SQL Server:

```
EXECUTE sp_execute_external_script

@language = N’Python’,

@script = N’

import pkg_resources

pckg_name = “pycaret”

pckgs = pandas.DataFrame([(i.key) for i in pkg_resources.working_set], columns = [“key”])

installed_pckg = pckgs.query(‘’key == @pckg_name’’)

print(“Package”, pckg_name, “is”, “not” if installed_pckg.empty else “”, “installed”) ’
```

![Script Execution Result](https://cdn-images-1.medium.com/max/2000/1*evwN5FoXycMQJETJcjawgA.png)

### V. ML Experiment Example — Clustering in SQL Server

Clustering is a machine learning technique that groups data points with similar characteristics. These groupings are useful for exploring data, identifying patterns, and analyzing a subset of data. Some common business use cases for clustering are:

✔ Customer segmentation for the purpose of marketing.

✔ Customer purchasing behaviour analysis for promotions and discounts.

✔ Identifying geo-clusters in an epidemic outbreak such as COVID-19.

In this tutorial, we will use the ‘\*\*jewellery.csv’ \*\*file that is available on PyCaret’s [Github repository](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/jewellery.csv).

![Sample Data points from jewellery dataset](https://cdn-images-1.medium.com/max/2000/1*itUa7b3dSjnzKFaaTJOkMg.png)

#### 1. K-Means Clustering

Run the following SQL code in SQL Server:

```
EXECUTE sp_execute_external_script

@language = N’Python’,

@script = N’dataset = InputDataSet

import pycaret.clustering as pc

dataset = pc.get_clusters(data = dataset)

OutputDataSet = dataset’,

@input_data_1 = N’SELECT [Age], [Income], [SpendingScore], [Savings] FROM [jewellery]’

WITH RESULT SETS(([Age] INT, [Income] INT, [SpendingScore] FLOAT, [Savings] FLOAT, [Cluster] varchar(15)));
```

#### 2. Output

![SQL Statement Result](https://cdn-images-1.medium.com/max/2000/1*AwXT-NmfgHJ9LDU6IWrPpA.png)

A new column ‘**Cluster’** containing the label is attached to the original table.

By default, PyCaret trains a **K-Means** clustering model with 4 clusters *(i.e. all the data points in the table are categorized into 4 groups*). Default values can be changed easily:

To change the number of clusters you can use **num\_clusters** parameter within **get\_**&#x63;lusters( ) function.

To change model type use **model** parameter within **get\_clusters( ).**

#### **3. K-Modes**

See the following code for training **K-Modes** model with **6 clusters**:

```
EXECUTE sp_execute_external_script

@language = N’Python’,

@script = N’dataset = InputDataSet

import pycaret.clustering as pc

dataset = pc.get_clusters(data = dataset, model=”kmodes”, num_clusters = 6)

OutputDataSet = dataset’,

@input_data_1 = N’SELECT [Age], [Income], [SpendingScore], [Savings] FROM [jewellery]’

WITH RESULT SETS(([Age] INT, [Income] INT, [SpendingScore] FLOAT, [Savings] FLOAT, [Cluster] varchar(15)));
```

Following these steps, you can assign cluster value to every observation point in the jewellery dataset. You can use similar steps on other datasets too, to perform clustering on them.

### VI. Conclusion

In this post, we learnt how to build a clustering model using running a Python library (PyCaret) in SQL Server. Similarly, you can build and run other types of supervised and unsupervised ML models depending on the need of the business problem.

You can further check out the [PyCaret](http://pycaret.org/) website for documentation on other supervised and unsupervised experiments that can be implemented in a similar manner within SQL Server.

My future posts will be tutorials on exploring supervised learning techniques (regression/classification) using Python and Pycaret within a SQL Server.

### VII. Important Links

[PyCaret](https://pycaret.org/)

[PyCaret: User guide and documentation](https://pycaret.org/guide/)

[PyCaret: Tutorials](https://pycaret.org/tutorial/)

[My LinkedIn Profile](https://www.linkedin.com/in/umarfarooque/)


# Machine Learning in Power BI using PyCaret

### Machine Learning in Power BI using PyCaret

#### A step-by-step tutorial for implementing machine learning in Power BI within minutes

#### by Moez Ali

![Machine Learning Meets Business Intelligence](https://cdn-images-1.medium.com/max/2000/1*Q34J2tT_yGrVV0NU38iMig.jpeg)

### **PyCaret 1.0.0**

Last week we announced [PyCaret](https://www.pycaret.org), an open source machine learning library in Python that trains and deploys machine learning models in a \*\*low-code \*\*environment. In our [previous post](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) we demonstrated how to use PyCaret in Jupyter Notebook to train and deploy machine learning models in Python.

In this post we present a **step-by-step tutorial** on how PyCaret can be integrated within [Power BI](https://powerbi.microsoft.com/en-us/), thus allowing analysts and data scientists to add a layer of machine learning to their Dashboards and Reports without any additional license or software costs. PyCaret is an open source and \*\*free to use \*\*Python library that comes with a wide range of functions that are exclusively built to work within Power BI.

By the end of this article you will learn how to implement the following in Power BI:

* **Clustering** — Group data points with similar characteristics.
* \*\*Anomaly Detection \*\*— Identify rare observations / outliers in the data.
* \*\*Natural Language Processing \*\*— Analyze text data *via* topic modeling.
* \*\*Association Rule Mining \*\*— Find interesting relationships in the data.
* \*\*Classification \*\*— Predict categorical class labels that are binary (1 or 0).
* \*\*Regression \*\*— Predict continuous value such as Sales, Price etc

> ## “PyCaret is democratizing machine learning and the use of advanced analytics by providing **free, open source, and low-code** machine learning solution for business analysts, domain experts, citizen data scientists, and experienced data scientists”.

### Microsoft Power BI

Power BI is a business analytics solution that lets you visualize your data and share insights across your organization, or embed them in your app or website. In this tutorial, we will use [Power BI Desktop](https://powerbi.microsoft.com/en-us/downloads/) for machine learning by importing the PyCaret library into Power BI.

### Before we start

If you have used Python before, it is likely that you already have Anaconda Distribution installed on your computer. If not, [click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/distribution/](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install pycaret. It’s a three-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Create an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and run the following code:

```
conda create --name **myenv** python=3.6
```

![Anaconda Prompt — Creating an environment](https://cdn-images-1.medium.com/max/2198/1*Yv-Ee99UJXCW2iTL1HUr5Q.png)

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Install PyCaret**

Run the following code in Anaconda Prompt:

```
conda activate **myenv**
pip install pycaret
```

Installation may take 10 – 15 minutes.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Set Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\AppData\Local\Continuum\anaconda3\envs\myenv

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*zQMKuyEk8LGrOPE-NByjrg.png)

### 📘 Example 1 — Clustering in Power BI

Clustering is a machine learning technique that groups data points with similar characteristics. These groupings are useful for exploring data, identifying patterns and analyzing a subset of data. Some common business use cases for clustering are:

✔ Customer segmentation for the purpose of marketing.

✔ Customer purchasing behavior analysis for promotions and discounts.

✔ Identifying geo-clusters in an epidemic outbreak such as COVID-19.

In this tutorial we will use **‘jewellery.csv’** file that is available on PyCaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/jewellery.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv File: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/jewellery.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/jewellery.csv)

![Power BI Desktop → Get Data → Other → Web](https://cdn-images-1.medium.com/max/2000/1*MdUeug0LSZu451-fBI5J_Q.png)

![Sample data points from jewellery.csv](https://cdn-images-1.medium.com/max/2000/1*XhXJjUHpEqOc7-RQ1fWoYQ.png)

#### **K-Means Clustering**

To train a clustering model we will execute Python script in Power Query Editor (Power Query Editor → Transform → Run python script).

![Ribbon in Power Query Editor](https://cdn-images-1.medium.com/max/2000/1*F18LNIkoWtAFr4P80J-U8Q.png)

Run the following code as a Python script:

```
from **pycaret.clustering **import *****
dataset = **get_clusters**(data = dataset)
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*nYqJWQM6NI3q3tLJXIVxtg.png)

#### **Output:**

![Clustering Results (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2000/1*PXWUtrYrNikCRDqhn_TgDw.png)

A new column \*\*‘Cluster’ \*\*containing label is attached to the original table.

Once you apply the query (Power Query Editor → Home → Close & Apply), Here is how you can visualize the clusters in Power BI:

![](https://cdn-images-1.medium.com/max/2000/1*8im-qPdXXBblPD7jiodQpg.png)

By default, PyCaret trains a **K-Means** clustering model with 4 clusters (*i.e. all the data points in the table are categorized into 4 groups*). Default values can be changed easily:

* To change the number of clusters you can use \*\*\*num\_clusters \*\*\*parameter within \*\*get\_clusters( ) \*\*function.
* To change model type use \*\*\*model \*\*\*parameter within **get\_clusters( )**.

See the following example code of training K-Modes model with 6 clusters:

```
from **pycaret.clustering **import *
dataset = **get_clusters**(dataset, model = 'kmodes', num_clusters = 6)
```

There are 9 ready-to-use clustering algorithms available in PyCaret:

![](https://cdn-images-1.medium.com/max/2000/1*Wdy201wGxmV3NwS9lzHwsA.png)

All the preprocessing tasks necessary to train a clustering model such as [missing value imputation](https://pycaret.org/missing-values/) (if table has any missing or \*null \*values), or [normalization](https://www.pycaret.org/normalization), or [one-hot-encoding](https://pycaret.org/one-hot-encoding/), they all are automatically performed before training a clustering model. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing capabilities.

💡 In this example we have used the \*\*get\_clusters( ) \*\*function to assign cluster labels in the original table. Every time the query is refreshed, clusters are recalculated. An alternate way to implement this would be to use the **predict\_model( )** function to predict cluster labels using a \*\*pre-trained model \*\*in Python or in Power BI (*see Example 5 below to see how to train machine learning models in Power BI environment*).

💡 If you want to learn how to train a clustering model in Python using Jupyter Notebook, please see our [Clustering 101 Beginner’s Tutorial](https://www.pycaret.org/clu101). *(no coding background needed).*

### 📘 Example 2 — Anomaly Detection in Power BI

Anomaly Detection is a machine learning technique used for identifying **rare items**, **events,** \*\*or observations \*\*by checking for rows in the table that differ significantly from the majority of the rows. Typically, the anomalous items will translate to some kind of problem such as bank fraud, a structural defect, medical problem or error. Some common business use cases for anomaly detection are:

✔ Fraud detection (credit cards, insurance, etc.) using financial data.

✔ Intrusion detection (system security, malware) or monitoring for network traffic surges and drops.

✔ Identifying multivariate outliers in the dataset.

In this tutorial we will use **‘anomaly.csv’** file available on PyCaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/anomaly.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/anomaly.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/anomaly.csv)

![Sample data points from anomaly.csv](https://cdn-images-1.medium.com/max/2476/1*M0uBBbcEYizdZgpeKlftlQ.png)

#### K-Nearest Neighbors Anomaly Detector

Similar to clustering, we will run Python script from Power Query Editor (Transform → Run python script) to train an anomaly detection model. Run the following code as a Python script:

```
from **pycaret.anomaly **import *****
dataset = **get_outliers**(data = dataset)
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*re7Oj-bPUHok7pCbmeWFuw.png)

#### **Output:**

![Anomaly Detection Results (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2002/1*J7_5ZAM7dFNVnMcgxV_N1A.png)

Two new columns are attached to the original table. Label (1 = outlier, 0 = inlier) and Score (data points with high scores are categorized as outlier).

Once you apply the query, here is how you can visualize the results from anomaly detection in Power BI:

![](https://cdn-images-1.medium.com/max/2000/1*tfn6W5vV1pUE11hTPCzdpA.png)

By default, PyCaret trains a **K-Nearest Neighbors Anomaly Detector** with 5% fraction (i.e. 5% of the total number of rows in the table will be flagged as outlier). Default values can be changed easily:

* To change the fraction value you can use \*\*\*fraction \*\*\*parameter within \*\*get\_outliers( ) \*\*function.
* To change model type use \*\*\*model \*\*\*parameter within **get\_outliers( )**.

See the following code for training an **Isolation Forest** model with 0.1 fraction:

```
from **pycaret.anomaly **import *
dataset = **get_outliers**(dataset, model = 'iforest', fraction = 0.1)
```

There are over 10 ready-to-use anomaly detection algorithms in PyCaret:

![](https://cdn-images-1.medium.com/max/2000/1*piuoq_K4B2aiyzOCkDg8MA.png)

All the preprocessing tasks necessary to train an anomaly detection model such as [missing value imputation](https://pycaret.org/missing-values/) (if table has any missing or \*null \*values), or [normalization](https://www.pycaret.org/normalization), or [one-hot-encoding](https://pycaret.org/one-hot-encoding/), they all are automatically performed before training an anomaly detection model. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing capabilities.

💡 In this example we have used the \*\*get\_outliers( ) \*\*function to assign outlier label and score for analysis. Every time the query is refreshed, outliers are recalculated. An alternate way to implement this would be to use the **predict\_model( )** function to predict outliers using a pre-trained model in Python or in Power BI (*see Example 5 below to see how to train machine learning models in Power BI environment*).

💡 If you want to learn how to train an anomaly detector in Python using Jupyter Notebook, please see our [Anomaly Detection 101 Beginner’s Tutorial](https://www.pycaret.org/ano101). *(no coding background needed).*

### 📘 Example 3 — Natural Language Processing

Several techniques are used to analyze text data among which \*\*Topic Modeling \*\*is a popular one. A topic model is a type of statistical model for discovering the abstract topics in a collection of documents. Topic modeling is a frequently used text-mining tool for the discovery of hidden semantic structures in a text data.

In this tutorial we will use \*\*\*\*the \*\*‘kiva.csv’ \*\*file available on PyCaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/kiva.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/kiva.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/kiva.csv)

#### **Latent Dirichlet Allocation**

Run the following code as a Python script in Power Query Editor:

```
from **pycaret.nlp **import *****
dataset = **get_topics**(data = dataset, text = 'en')
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*QNaOFbKVJtkG6TjH-z0nxw.png)

**‘en’** is the name of the column containing text in the table **‘kiva’**.

#### Output:

![Topic Modeling Results (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2536/1*kP9luTZMmeo7-uEI1lYKlQ.png)

Once the code is executed, new columns with weight of topics and dominant topic are attached to the original table. There are many ways to visualize the output of Topic Models in Power BI. See an example below:

![](https://cdn-images-1.medium.com/max/2000/1*yZHDO-9UXZ3L1lFBXMMCPg.png)

By default, PyCaret trains a Latent Dirichlet Allocation model with 4 topics. Default values can be changed easily:

* To change the number of topics you can use the \*\*\*num\_topics \*\*\*parameter within \*\*get\_topics( ) \*\*function.
* To change model type use the \*\*\*model \*\*\*parameter within the **get\_topics( )**.

See the example code for training a **Non-Negative Matrix Factorization Model** with 10 topics:

```
from **pycaret.nlp **import *
dataset = **get_topics**(dataset, 'en', model = 'nmf', num_topics = 10)
```

PyCaret has following ready-to-use algorithms for topic modeling:

![](https://cdn-images-1.medium.com/max/2000/1*YhRd9GgWw1kblnJezqZd5w.png)

### 📘 Example 4— Association Rule Mining in Power BI

Association Rule Mining \*\*\*\*is a \*\*rule-based machine learning \*\*technique for discovering interesting relations between variables in a database. It is intended to identify strong rules using measures of interestingness. Some common business use cases for association rule mining are:

✔ Market Basket Analysis to understand items frequently bought together.

✔ Medical Diagnosis to assist physicians in determining occurrence probability of illness given factors and symptoms.

In this tutorial we will use the **‘france.csv’** file available on PyCaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/france.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/france.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/france.csv)

![Sample data points from france.csv](https://cdn-images-1.medium.com/max/2484/1*2S-OwdafFh30hWTzFDC_WQ.png)

#### Apriori Algorithm

It should be clear by now that all PyCaret functions are executed as Python script in Power Query Editor (Transform → Run python script). Run the following code to train an association rule model using the Apriori algorithm:

```
from **pycaret.arules** import *
dataset = **get_rules**(dataset, transaction_id = 'InvoiceNo', item_id = 'Description')
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*c2QmWam_1008OCEf0Ct46w.png)

**‘InvoiceNo’** is the column containing transaction id and **‘Description’** contains the variable of interest i.e. the Product name.

#### **Output:**

![Association Rule Mining Results (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2518/1*H4rGqsxDtJyVu24yc_UWHw.png)

It returns a table with antecedents and consequents with related metrics such as support, confidence, lift etc. [Click here](https://www.pycaret.org/association-rule) to learn more about Association Rules Mining in PyCaret.

### 📘 Example 5 — Classification in Power BI

Classification is a supervised machine learning technique used to predict the categorical **class labels** (also known as binary variables). Some common business use case of classification are:

✔ Predicting customer loan / credit card default.

✔ Predicting customer churn (whether the customer will stay or leave)

✔ Predicting patient outcome (whether patient has disease or not)

In this tutorial we will use \*\*‘employee.csv’ \*\*file available on PyCaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/employee.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/employee.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/employee.csv)

\*\*Objective: \*\*The table **‘employee’** contains information of 15,000 active employees in a company such as time spent at the company, average monthly hours worked, promotion history, department etc. Based on all of these columns (also known as *features* in machine learning terminology) the objective is to predict whether the employee will leave the company or not, represented by the column \*\*‘left’ \*\*(1 means yes, 0 means no).

Unlike Clustering, Anomaly Detection, and NLP examples which fall under the umbrella of unsupervised Machine Learning, Classification is a \*\*supervised \*\*technique and hence it is implemented in two parts:

#### **Part 1: Training a Classification Model in Power BI**

The first step is to create a duplicate of the table **‘employee’** in Power Query Editor which will be used for training a model.

![Power Query Editor → Right Click ‘employee’ → Duplicate](https://cdn-images-1.medium.com/max/2760/1*9t8FyRshmdBqzONMgMRQcQ.png)

Run the following code in the newly created duplicate table **‘employee (model training)’** to train a classification model:

```
# import classification module and setup environment

from **pycaret.classification **import *****
clf1 = **setup**(dataset, target = 'left', silent = True)

# train and save xgboost model

xgboost = **create_model**('xgboost', verbose = False)
final_xgboost = **finalize_model**(xgboost)
**save_model**(final_xgboost, 'C:/Users/*username*/xgboost_powerbi')
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*0qLtTngg_uI31JTSPLNSiQ.png)

#### Output:

The output of this script will be a \*\*pickle file \*\*saved at the defined location. The pickle file contains the entire data transformation pipeline as well as trained model object.

💡 An alternate to this would be to train a model in Jupyter notebook instead of Power BI. In this case, Power BI will only be used to generate predictions on the front-end using a pre-trained model in Jupyter notebook that will be imported as a pickle file into Power BI (follow Part 2 below). To learn more about using PyCaret in Python, [click here](https://www.pycaret.org/tutorial).

💡 If you want to learn how to train a classification model in Python using Jupyter Notebook, please see our [Binary Classification 101 Beginner’s Tutorial](https://www.pycaret.org/clf101). *(no coding background needed).*

There are 18 ready-to-use classification algorithms available in PyCaret:

![](https://cdn-images-1.medium.com/max/2000/1*hvcdSTqA6Qla7YlWMkBmhA.png)

#### Part 2: Generate Predictions using Trained Model

We can now use the trained model on the original \*\*‘employee’ \*\*table to predict whether the employee will leave the company or not (1 or 0) and the probability %. Run the following code as python script to generate predictions:

```
from **pycaret.classification** import *****
xgboost = **load_model**('c:/users/*username*/xgboost_powerbi')
dataset = **predict_model**(xgboost, data = dataset)
```

#### Output:

![Classification Predictions (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2482/1*9Ib1KC_9MTYEV_xd8fHExQ.png)

Two new columns are attached to the original table. The **‘Label’** column indicates the prediction and **‘Score’** column is the probability of outcome.

In this example we have predicted on the same data that we have used for training the model for demonstration purpose only. In a real setting, the **‘Left’** column is the actual outcome and is unknown at the time of prediction.

In this tutorial we have trained an **Extreme Gradient Boosting** **(‘xgboost’)** model and used it to generate predictions. We have done this for simplicity only. Practically, you can use PyCaret to predict any type of model or chain of models.

PyCaret’s **predict\_model( )** function can work seamlessly with the pickle file created using PyCaret as it contains the entire transformation pipeline along with trained model object. [Click here](https://www.pycaret.org/predict-model) to learn more about the \*\*predict\_model \*\*function.

💡 All the preprocessing tasks necessary to train a classification model such as [missing value imputation](https://pycaret.org/missing-values/) (if table has any missing or \*null \*values), or [one-hot-encoding](https://pycaret.org/one-hot-encoding/), or [target encoding](https://www.pycaret.org/one-hot-encoding), they all are automatically performed before training a model. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing capabilities.

### 📘 Example 6— Regression in Power BI

\*\*Regression \*\*is a supervised machine learning technique used to predict the a continuous outcome in the best possible way given the past data and its corresponding past outcomes. Unlike Classification which is used for predicting a binary outcome such as Yes or No (1 or 0), Regression is used for predicting continuous values such as Sales, Price, quantity etc.

In this tutorial we will use the **‘boston.csv’** file available on pycaret’s [github repository](https://github.com/pycaret/pycaret/blob/master/datasets/boston.csv). You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

\*\*Link to csv file: [\*\*https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/boston.csv](https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/boston.csv)

\*\*Objective: \*\*The table **‘boston’** contains information on 506 houses in Boston such as average number of rooms, property tax rates, population etc. Based on these columns (also known as *features* in machine learning terminology) the objective is to predict the median value of house, represented by column **‘medv’**.

#### Part 1: Training a Regression Model in Power BI

The first step is to create a duplicate of the **‘boston’** table in Power Query Editor that will be used for training a model.

Run the following code in the new duplicate table as python script:

```
# import regression module and setup environment

from **pycaret.regression **import *****
clf1 = **setup**(dataset, target = 'medv', silent = True)

# train and save catboost model

catboost = **create_model**('catboost', verbose = False)
final_catboost = **finalize_model**(catboost)
**save_model**(final_catboost, 'C:/Users/*username*/catboost_powerbi')
```

#### Output:

The output of this script will be a \*\*pickle file \*\*saved at the defined location. The pickle file contains the entire data transformation pipeline as well as trained model object.

There are over 20 ready-to-use regression algorithms available in PyCaret:

![](https://cdn-images-1.medium.com/max/2000/1*2xlKljU-TjJlr7PuUzRRyA.png)

#### Part 2: Generate Predictions using Trained Model

We can now use the trained model to predict the median value of houses. Run the following code in the original table \**‘boston’* \*\*\*as a python script:

```
from **pycaret.classification** import *****
xgboost = **load_model**('c:/users/*username*/xgboost_powerbi')
dataset = **predict_model**(xgboost, data = dataset)
```

#### Output:

![Regression Predictions (after execution of code)](https://cdn-images-1.medium.com/max/2000/1*RCYtFO6XDGI2-qbZdYeMfQ.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/2408/1*0A1cf_nsj2SULtNEjEu4tA.png)

A new column **‘Label’** that contains predictions are attached to the original table.

In this example we have predicted on the same data that we have used for training the model for demonstration purpose only. In a real setting, the **‘medv’** column is the actual outcome and is unknown at the time of prediction.

💡 All the preprocessing tasks necessary to train a regression model such as [missing value imputation](https://pycaret.org/missing-values/) (if table has any missing or \*null \*values), or [one-hot-encoding](https://pycaret.org/one-hot-encoding/), or [target transformation](https://pycaret.org/transform-target/), they all are automatically performed before training a model. [Click here](https://www.pycaret.org/preprocessing) to learn more about PyCaret’s preprocessing capabilities.

### Next Tutorial

In the next tutorial of \*\*Machine Learning in Power BI using PyCaret \*\*series, we will go in more depth and explore advanced preprocessing features in PyCaret. We will also see how to productionalize a machine learning solution in Power BI and leverage the power of [PyCaret](https://www.pycaret.org) on the front-end of Power BI.

If you would like to learn more on this please stay connected.

Follow us on our [Linkedin](https://www.linkedin.com/company/pycaret/) page and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel.

### Also see:

Beginner level Python notebooks:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### What’s in the development pipeline?

We are actively working on improving PyCaret. Our future development pipeline includes a new \*\*Time Series Forecasting \*\*module, integration with \*\*TensorFlow, \*\*and major improvements on the scalability of PyCaret. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [Github ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [Github Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

Please give us ⭐️ on our [github repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Follow me on Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)


# Machine Learning in Tableau with PyCaret

### Machine Learning in Tableau with PyCaret

#### A step by step integration guide to setup ML pipelines within minutes

#### by Andrew Cowan-Nagora

[PyCaret](https://www.pycaret.org/) is a recently released open source machine learning library in Python that trains and deploys machine learning models in a \*\*low-code \*\*environment. To learn more about PyCaret, read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46).

This article will demonstrate how PyCaret can be integrated with Tableau Desktop and Tableau Prep which opens new avenues for analysts and data scientists to add a layer of machine learning to their dashboards, reports and visualizations. By reducing the time required to code as well as the need to purchase additional software, rapid prototyping is now possible in environments that are already familiar and available to analysts throughout the organization.

### Learning Goals

* Train a supervised machine learning model and create a ML pipeline in PyCaret
* Load a trained ML pipeline into Tableau Desktop and Tableau Prep
* Create a dashboard that communicates insights from the model
* Understand how the model can be deployed into production with Tableau

### Direct Marketing Business Context

The example here will focus on how to setup a basic direct marketing propensity model that uses a classification algorithm to predict which customers are most likely to initiate a visit after receiving an offer via text or email.

A dashboard will then be created that can take the trained model and predict how successful new campaigns are likely to be which is valuable for marketers who are designing promotional plans.

By using PyCaret and Tableau, the business can quickly setup reporting products that continuously generate predictive views using existing software and minimal up front development time.

### Before we start

The software that will be required to follow along:

**1 — Tableau Desktop**

[Tableau Desktop](https://www.tableau.com/products/desktop) is a visual analytics tool that is used to connect to data, build interactive dashboards and share insights across the organization.

![](https://cdn-images-1.medium.com/max/2604/1*XVjP6x5eMCCoEAlv_gb6-Q.png)

**2 — Tableau Prep**

[Tableau Prep](https://www.tableau.com/products/prep) provides a visual interface to combine, clean and shape data by setting up flows and schedules.

![](https://cdn-images-1.medium.com/max/3126/1*TEG93kgXECyKsgYqXTJ5gw.png)

**3 — Python 3.7 or greater**

Anaconda is a free, open-source distribution of the Python programming language for data science. If you haven’t used it before, you can download it [here](https://www.anaconda.com/products/individual).

![https://www.anaconda.com/distribution/](https://cdn-images-1.medium.com/max/2612/0*78DWA4r55DRuMs2P.png)

**4 — PyCaret Python Library**

To install the [PyCaret ](http://pycaret.org)library use the following code in Jupyter notebook or Anaconda prompt.

```
pip install pycaret
```

This may take up to 15 minutes. If any problems are encountered please see the project [GitHub](https://www.github.com/pycaret/pycaret) page for known issues.

**5 — TabPy Python Library**

TabPy is the Tableau supported library that is required run python scripts.

From the [GitHub](https://github.com/tableau/TabPy) page:

> TabPy (the Tableau Python Server) is an Analytics Extension implementation which expands Tableau’s capabilities by allowing users to execute Python scripts and saved functions via Tableau’s table calculations.

To install TabPy use the following code in Anaconda prompt or terminal.

```
pip install tabpy
```

Once installed use the following code to start up a local server using default settings.

```
tabpy
```

To connect Tableau to the TabPy server go to Help > Settings and Performance > Manage Analytics Extension Connection. Select TabPy and enter localhost, port 9004 (default) and test connection.

![](https://cdn-images-1.medium.com/max/2000/1*E9s7_2uOGuraAcz7lRf6-A.png)

Python scripts can now be run in Tableau through calculated fields that output as table calculations.

Please refer to the TabPy [GitHub](https://github.com/tableau/TabPy) page for custom server options. Running TabPy on external servers and/or clouds and configuring Tableau Server will not be covered in this post but please look [here](https://help.tableau.com/current/server/en-us/config_r_tabpy.htm) for more information.

### Direct Marketing Data

The data set that will be used contains information on various marketing offers that were sent to customers through text and email. It contains 64000 records organized into an ID column, 10 features that relate to the customer or message sent and a binary target that indicates if a visit occurred. The data can be downloaded [here](https://github.com/andrewcowannagora/PyCaret-Tableau/blob/master/direct_marketing.csv).

![](https://cdn-images-1.medium.com/max/2000/1*nixMpbPMN5_aW0IGKOCuxw.png)

### **Training a Model Beforehand**

While it is possible to perform the model training process inside Tableau, this is generally not the preferred approach since every time the data is refreshed or the user interacts with the view the script will re-run. This is problematic because:

* When the model is retrained with new data, the prediction may change unexpectedly.
* Constantly re-running a script will impact the performance of the dashboard.

A more appropriate approach is to use a pre-trained model in Tableau to generate predictions on new data. Jupyter notebook will be used in this example to demonstrate how PyCaret is used to make this process straight forward.

### Building a Model In PyCaret

Running the following code in Jupyter Notebook will train a Naive Bayes classification model and create a ML pipeline that is saved as a pickle file.

Notice that setting up and saving the model is accomplished in 4 lines of code. A complete notebook can be downloaded [here](https://github.com/andrewcowannagora/PyCaret-Tableau/blob/master/TabPy%20Direct%20Marketing.ipynb).

![](https://cdn-images-1.medium.com/max/2834/1*EP9lfNBQ53CYV80nO7yAkA.png)

![Pickle file containing trained model and pipeline](https://cdn-images-1.medium.com/max/2000/1*EoKanuGm98zMnLuURG7JHg.png)

The unseen data will be used to simulate a list of new customers that have not yet been sent an offer. When the dashboard is deployed in production, it would be connected to a database containing the information for new customers.

Note that in the setup phase PyCaret performs automatic pre-processing which in this case expanded the number of features from 10 to 39 via one hot encoding.

This is only scratching the surface of PyCaret’s built in functionality thus it is strongly recommended to look at the classification [module](https://pycaret.org/classification/) and [tutorials](https://pycaret.org/clf101/) on the PyCaret website. The specific details of the selected model will not be covered here.

### Loading the Model into Tableau Desktop

The unseen data will now be passed to the trained model and labelled in Tableau Desktop.

Instructions:

1. Open Tableau and connect to the text file new\_customer.csv that was created in the above code. This simply serves as an example but ideally the new or unlabelled customer data would reside in a database.

![](https://cdn-images-1.medium.com/max/3840/1*YwmmK9bL3SFfnfemKF1agA.png)

1. On a new sheet select analysis > create calculated field or simply right click in the data pane. Enter the following code:

   SCRIPT\_INT(" import pandas as pd import pycaret.classification

   nb = pycaret.classification.load\_model('C:/Users/owner/Desktop/nb\_direct')

   X\_pred = pd.DataFrame({'recency':\_arg1, 'history\_segment':\_arg2, 'history':\_arg3, 'mens':\_arg4, 'womens':\_arg5,'zip\_code':\_arg6, 'newbie':\_arg7, 'channel':\_arg8, 'segment':\_arg9, 'DM\_category':\_arg10})

   pred = pycaret.classification.predict\_model(nb, X\_pred) return pred\['Label'].tolist()

   ", SUM(\[recency]), ATTR(\[history\_segment]), SUM(\[history]), SUM(\[mens]), SUM(\[womens]), ATTR(\[zip\_code]), SUM(\[newbie]), ATTR(\[channel]), ATTR(\[segment]), SUM(\[DM\_category]) )

![](https://cdn-images-1.medium.com/max/2386/1*LmKKJVNSh8YS6aQZhWzkGg.png)

* The script function specifies the type of data that will be returned from the calculation. In this case it is the binary predicted label for visit.
* The load\_model() function from PyCaret loads the previously saved model and transformation pipeline that was saved as a pickle file.
* X\_pred is a dataframe that will map the data connected to Tableau as inputs through the \_arg1, \_arg2, \_arg3… notation. The fields are listed at the end of the script.
* predict\_model() takes the trained model and predicts against the new data input. Note that the new data is passed through the transformation pipeline created in the PyCaret setup phase (encoding).
* The labels are then returned as a list that can be viewed in Tableau.

1. By dragging the ID and Label columns into the view it is possible to see the model predictions.

![](https://cdn-images-1.medium.com/max/2498/1*lPZGQtE89stX1SjWqSiyTQ.png)

It is important to understand that the output is a table calculation which has some limitations:

* The script will only run when pulled into the view.
* It cannot be used as a base for further calculations unless both are in the view.
* The python generated data cannot be appended to Tableau extracts.
* The script runs each time the view is changed which can lead to long wait times.

These drawbacks are quite significant as dashboard options become limited when each record must be contained in the view and the script takes around 4 minutes to run with 3200 records in this case.

Viable applications would include generating scored lists that could be exported or summary views such as the one below.

![](https://cdn-images-1.medium.com/max/2400/1*DiaEihO8vjKM_16_zEYrvA.png)

An example insight from this could be that higher spend customers are the most likely to visit which makes sense business wise but could perhaps be an indicator of unnecessary discounting.

### Loading the Model into Tableau Prep

A great alternative to get around the limitations of running scripts directly in Tableau Desktop is to use Tableau Prep. New data can be connected and then passed to the model with the difference this time being that the predicted labels are appended to the output. When connected to Tableau, the new columns can be used normally rather than as table calculations.

Instructions:

1. Open Tableau Prep and connect to the text file new\_customer.csv that was created in the above code.

![](https://cdn-images-1.medium.com/max/3540/1*TxMr_QQR6jGACJzmSstITg.png)

1. Select the ‘+’ button next to the file in the flow pane and add the script option. Like in Tableau Desktop, connect to the TabPy server that should still be running in the background using localhost and 9004.

![](https://cdn-images-1.medium.com/max/2064/1*KaiZM_JXvB6qfjtyjglBIA.png)

1. Next, the following python script will need to be created and connected to prep using the browse option. It can be downloaded [here](https://github.com/andrewcowannagora/PyCaret-Tableau/blob/master/direct_marketing_prep.py).

![](https://cdn-images-1.medium.com/max/2000/1*HRl6t04aiKBP0eqTGys7Sw.png)

A function is created that loads the pickle file which holds the saved model and transformation pipeline. The data loaded into prep is automatically held in the df object and is passed to the model.

The PyCaret output will return the initial data set and two new appended columns; Label (prediction) and Score (probability of prediction). The output schema ensures that the columns and data types are correctly read into prep.

The function name must then be entered into prep.

![](https://cdn-images-1.medium.com/max/2000/1*Uh3neQ8weSZm9LJ_Ki6Qug.png)

1. Select the ‘+’ sign next to the script icon and choose output. It is possible to publish as a .tde or .hyper file to Tableau Server which would be the preferred method in a production environment but for this example a .csv file will be sent to the desktop.

![](https://cdn-images-1.medium.com/max/2384/1*mVe4CorNxcBRU7q_dPqHOQ.png)

Notice how the label and score columns are now appended to the original data set. Select ‘run flow’ to generate the output. The flow file can be downloaded [here](https://github.com/andrewcowannagora/PyCaret-Tableau/blob/master/DM_Model_Flow.tflx).

In a server environment it is possible to schedule when a flow runs and automate the scoring process before the data reaches the actual Tableau dashboard.

### Loading the Flow Output into Tableau

The newly labelled data can now be connected to Tableau Desktop without the table calculation limitations and slow downs.

Aggregations and any other desired calculations can be created to design a summary dashboard that displays various predictive metrics:

![](https://cdn-images-1.medium.com/max/2000/1*AhgzQQMLOfwe_5__eMMTIQ.png)

Once the data and ML pipeline is established, marketers and executives would quickly be able to track how upcoming campaigns could potentially perform with minimal intervention required. The Tableau file that contains the example dashboard and earlier script can be downloaded [here](https://github.com/andrewcowannagora/PyCaret-Tableau/blob/master/DM_Dashboard.twbx).

### Closing Remarks

This article has demonstrated how PyCaret can be integrated with Tableau Desktop and Tableau Prep to quickly add a layer of machine learning into existing workflows.

By using tools that are familiar to the organization and the PyCaret library, entire ML pipelines can be established in minutes which enables predictive analytics prototyping to get off the ground quickly.

### Useful Links

[PyCaret](https://pycaret.org/)

[PyCaret: User guide and documentation](https://pycaret.org/guide/)

[PyCaret: Tutorials](https://pycaret.org/tutorial/)

[PyCaret: Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g/featured)

[LinkedIn](http://www.linkedin.com/in/andrewcowannagora)


# Multiple Time Series Forecasting with PyCaret

### Multiple Time Series Forecasting with PyCaret

#### A step-by-step tutorial to forecast multiple time series with PyCaret

![PyCaret — An open-source, low-code machine learning library in Python](https://cdn-images-1.medium.com/max/2000/1*c8mBuCW7nP0KGhwXQC98Eg.png)

### PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is incredibly popular for its ease of use, simplicity, and ability to build and deploy end-to-end ML prototypes quickly and efficiently.

PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it’s imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it.

This tutorial assumes that you have some prior knowledge and experience with PyCaret. If you haven’t used it before, no problem — you can get a quick headstart through these tutorials:

* [PyCaret 2.2 is here — what’s new](https://towardsdatascience.com/pycaret-2-2-is-here-whats-new-ad7612ca63b)
* [Announcing PyCaret 2.0](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e)
* [Five things you don’t know about PyCaret](https://towardsdatascience.com/5-things-you-dont-know-about-pycaret-528db0436eec)

### **RECAP**

In my [last tutorial](https://towardsdatascience.com/time-series-forecasting-with-pycaret-regression-module-237b703a0c63), I have demonstrated how you can use PyCaret to forecast time-series data using Machine Learning through [PyCaret Regression Module](https://pycaret.readthedocs.io/en/latest/api/regression.html). If you haven’t read that yet, you can read [Time Series Forecasting with PyCaret Regression Module](https://towardsdatascience.com/time-series-forecasting-with-pycaret-regression-module-237b703a0c63) tutorial before continuing with this one, as this tutorial builds upon some important concepts covered in the last tutorial.

### Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret which only installs hard dependencies that are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed.

### 👉 PyCaret Regression Module

PyCaret **Regression Module** is a supervised machine learning module used for estimating the relationships between a **dependent variable** (often called the ‘outcome variable’, or ‘target’) and one or more **independent variables** (often called ‘features’, or ‘predictors’).

The objective of regression is to predict continuous values such as sales amount, quantity, temperature, number of customers, etc. All modules in PyCaret provide many [pre-processing](https://www.pycaret.org/preprocessing) features to prepare the data for modeling through the [setup ](https://www.pycaret.org/setup)function. It has over 25 ready-to-use algorithms and [several plots](https://www.pycaret.org/plot-model) to analyze the performance of trained models.

### 👉 Dataset

For this tutorial, I will show the end-to-end implementation of multiple time-series data forecasting, including both the training as well as predicting future values.

I have used the [Store Item Demand Forecasting Challenge](https://www.kaggle.com/c/demand-forecasting-kernels-only) dataset from Kaggle. This dataset has 10 different stores and each store has 50 items, i.e. total of 500 daily level time series data for five years (2013–2017).

![Sample Dataset](https://cdn-images-1.medium.com/max/2000/1*VY7MljIxivAiYWSMmAjN6g.png)

### 👉 Load and prepare the data

```
**# read the csv file
**import pandas as pd
data = pd.read_csv('train.csv')
data['date'] = pd.to_datetime(data['date'])

**# combine store and item column as time_series**
data['store'] = ['store_' + str(i) for i in data['store']]
data['item'] = ['item_' + str(i) for i in data['item']]
data['time_series'] = data[['store', 'item']].apply(lambda x: '_'.join(x), axis=1)
data.drop(['store', 'item'], axis=1, inplace=True)

**# extract features from date**
data['month'] = [i.month for i in data['date']]
data['year'] = [i.year for i in data['date']]
data['day_of_week'] = [i.dayofweek for i in data['date']]
data['day_of_year'] = [i.dayofyear for i in data['date']]

data.head()
```

![Samples rows from data](https://cdn-images-1.medium.com/max/2000/1*D3PBqLf-PsnGdTn7AjGmWw.png)

```
**# check the unique time_series**
data['time_series'].nunique()
>>> 500
```

### 👉 Visualize time-series

```
**# plot multiple time series with moving avgs in a loop**

import plotly.express as px

for i in data['time_series'].unique():
    subset = data[data['time_series'] == i]
    subset['moving_average'] = subset['sales'].rolling(30).mean()
    fig = px.line(subset, x="date", y=["sales","moving_average"], title = i, template = 'plotly_dark')
    fig.show()
```

![store\_1\_item\_1 time series and 30-day moving average](https://cdn-images-1.medium.com/max/2608/1*BlE7UEMFRCV6kbEK1oWTEA.png)

![store\_2\_item\_1 time series and 30-day moving average](https://cdn-images-1.medium.com/max/2616/1*Vhc8EP7IbA-_qdwyuENHaQ.png)

### 👉 Start the training process

Now that we have the data ready, let’s start the training loop. Notice that verbose = False in all functions to avoid printing results on the console while training.

The code below is a loop around time\_series column we created during the data preparatory step. There are a total of 150 time series (10 stores x 50 items).

Line 10 below is filtering the dataset for time\_series variable. The first part inside the loop is initializing the setup function, followed by compare\_models to find the best model. Line 24–26 captures the results and appends the performance metrics of the best model in a list called all\_results . The last part of the code uses the finalize\_model function to retrain the best model on the entire dataset including the 5% left in the test set and saves the entire pipeline including the model as a pickle file.

We can now create a data frame from all\_results list. It will display the best model selected for each time series.

```
concat_results = pd.concat(all_results,axis=0)
concat_results.head()
```

![sample\_rows from concat\_results](https://cdn-images-1.medium.com/max/2000/1*qgu9jP86L2gaZHi-TvM0SA.png)

### Training Process 👇

![Training process](https://cdn-images-1.medium.com/max/2560/1*SwI6InjXRuB-TlQwsKZZRQ.gif)

### 👉 Generate predictions using trained models

Now that we have trained models, let’s use them to generate predictions, but first, we need to create the dataset for scoring (X variables).

```
**# create a date range from 2013 to 2019**
all_dates = pd.date_range(start='2013-01-01', end = '2019-12-31', freq = 'D')

**# create empty dataframe**
score_df = pd.DataFrame()

**# add columns to dataset**
score_df['date'] = all_dates
score_df['month'] = [i.month for i in score_df['date']]
score_df['year'] = [i.year for i in score_df['date']]
score_df['day_of_week'] = [i.dayofweek for i in score_df['date']]
score_df['day_of_year'] = [i.dayofyear for i in score_df['date']]

score_df.head()
```

![sample rows from score\_df dataset](https://cdn-images-1.medium.com/max/2000/1*Dycm3JuIt0gsGPwPc4_8fw.png)

Now let’s create a loop to load the trained pipelines and use the predict\_model function to generate prediction labels.

```
from pycaret.regression import load_model, predict_model

all_score_df = []

for i in tqdm(data['time_series'].unique()):
    l = load_model('trained_models/' + str(i), verbose=False)
    p = predict_model(l, data=score_df)
    p['time_series'] = i
    all_score_df.append(p)

concat_df = pd.concat(all_score_df, axis=0)
concat_df.head()
```

![samples rows from concat\_df](https://cdn-images-1.medium.com/max/2000/1*2l9A8jStBQEAULk9fqMObA.png)

We will now join the dataand concat\_df .

```
final_df = pd.merge(concat_df, data, how = 'left', left_on=['date', 'time_series'], right_on = ['date', 'time_series'])
final_df.head()
```

![sample rows from final\_df](https://cdn-images-1.medium.com/max/2490/1*TN9d9WssEBkn-GFSYVgNWg.png)

We can now create a loop to see all plots.

```
for i in final_df['time_series'].unique()[:5]:
    sub_df = final_df[final_df['time_series'] == i]
    
    import plotly.express as px
    fig = px.line(sub_df, x="date", y=['sales', 'Label'], title=i, template = 'plotly_dark')
    fig.show()
```

![store\_1\_item\_1 actual sales and predicted labels](https://cdn-images-1.medium.com/max/2604/1*tvjEor2VvHVFgumGgEtfKQ.png)

![store\_2\_item\_1 actual sales and predicted labels](https://cdn-images-1.medium.com/max/2598/1*99cyEOPNr97uDMLKrnNqig.png)

I hope that you will appreciate the ease of use and simplicity in PyCaret. In less than 50 lines of code and one hour of experimentation, I have trained over 10,000 models (25 estimators x 500 time series) and productionalized 500 best models to generate predictions.

### Coming Soon!

Next week I will be writing a tutorial on unsupervised anomaly detection on time-series data using [PyCaret Anomaly Detection Module](https://pycaret.readthedocs.io/en/latest/api/anomaly.html). Please follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1) to get more updates.

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Predict Customer Churn using PyCaret

### Predict Customer Churn (the right way) using PyCaret

#### A step-by-step guide on how to predict customer churn the right way using PyCaret that actually optimizes the business objective and improves ROI

![Predict Customer Churn (the right way) using PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2630/1*mu45A-psfPHTIM1F_nUXBw.png)

### **Introduction**

Customer retention is one of the primary KPI for companies with a subscription-based business model. Competition is tough particularly in the SaaS market where customers are free to choose from plenty of providers. One bad experience and customer may just move to the competitor resulting in customer churn.

### **What is Customer Churn?**

Customer churn is the percentage of customers that stopped using your company’s product or service during a certain time frame. One of the ways to calculate a churn rate is to divide the number of customers lost during a given time interval by the number of active customers at the beginning of the period. For example, if you got 1000 customers and lost 50 last month, then your monthly churn rate is 5 percent.

Predicting customer churn is a challenging but extremely important business problem especially in industries where the cost of customer acquisition (CAC) is high such as technology, telecom, finance, etc. The ability to predict that a particular customer is at a high risk of churning, while there is still time to do something about it, represents a huge additional potential revenue source for companies.

### How is the Customer Churn machine learning model used in practice?

The primary objective of the customer churn predictive model is to retain customers at the highest risk of churn by proactively engaging with them. For example: Offer a gift voucher or any promotional pricing and lock them in for an additional year or two to extend their lifetime value to the company.

There are two broad concepts to understand here:

* We want a customer churn predictive model to predict the churn in advance (let’s say one month in advance, three months in advance, or even six months in advance — it all depends on the use-case). This means that you have to be extremely careful of the cut-off date i.e. You shouldn’t be using any information after the cut-off date as a feature in the machine learning model, otherwise it will be leakage. The period before the cut-off date is known as the **Event.**
* Normally for customer churn prediction, you will have to work a little bit to create a ***target column***, it’s generally not available in the form you would want it. For example, you want to predict if the customer will churn within the next quarter, and so you will iterate through all the active customers as of your event cut-off date and check if they left the company in the next quarter or not (1 for yes, 0 for no). The quarter in this case is called **Performance Window**.

![How to create customer churn dataset — Image by Author](https://cdn-images-1.medium.com/max/2000/1*yNaRKOY1ZjTF59U1LRnQ0g.png)

### Customer Churn Model Workflow

Now that you understand how the data is sourced and churn target is created (which is one of the most challenging parts of the problem), let’s discuss how this machine learning model will be used in the business. Read the below diagram from left-to-right:

* A model is trained on customer churn history (event period for X features and performance window for target variable).
* Every month active customer base is passed onto **Machine Learning Predictive Model** to return the probability of churn for each customer (in business lingo, this is sometimes called a score of churn).
* The list will be sorted from highest to lowest probability value (or score as they say it) and the customer retention teams will start engaging with the customer to stop the churn, normally by offering some kind of promotion or gift card to lock in few more years.
* Customers that have a very low probability of churn (or essentially model predicts no-churn) are happy customers. No actions are taken on them.

![Customer Churn Model Workflow— Image by Author](https://cdn-images-1.medium.com/max/2598/1*V_Yiyl5iWIC6mRXEiTC0Qg.png)

### Let’s get started with the practical example

In this section, I will demonstrate the complete end-to-end workflow for machine learning model training & selection, hyperparameter tuning, analysis, and interpretation of the results. I will also discuss the metrics that you can optimize and why conventional metrics like AUC, Accuracy, Recall may not be suitable for the customer churn models. I will be using [PyCaret](https://www.pycaret.org) — an open-source, low-code machine learning library to perform this experiment. This tutorial assumes you have basic knowledge of PyCaret.

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. PyCaret is known for its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end machine learning pipelines. To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

![Features of PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2084/0*KAZzGooA90037WgZ.png)

### Install PyCaret

```
**# install pycaret
**pip install pycaret
```

### 👉Dataset

For this tutorial, I am using a [Telecom Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn) dataset from Kaggle. The dataset already contains the target column that we can use as is. You can read this dataset directly from this [GitHub](https://raw.githubusercontent.com/srees1988/predict-churn-py/main/customer_churn_data.csv) link. (*Shoutout to srees1988*)

```
**# import libraries**
import pandas as pd
import numpy as np

**# read csv data
**data **= **pd.read_csv('[https://raw.githubusercontent.com/srees1988/predict-churn-py/main/customer_churn_data.csv'](https://raw.githubusercontent.com/srees1988/predict-churn-py/main/customer_churn_data.csv'))
```

![Sample dataset — Image by Author](https://cdn-images-1.medium.com/max/2702/1*mN9rTN4VxjI5opbTbnSZmQ.png)

### **👉 Exploratory Data Analysis**

```
**# check data types
**data.dtypes
```

![Data types — Image by Author](https://cdn-images-1.medium.com/max/2000/1*S7mP3s8pykG4EBCBnXlAGw.png)

Notice that TotalCharges is of an object type instead of float64. Upon investigation, I figured out there are some blank spaces in this column which has caused Python to force the data type as object . To fix that, we will have to trim blank spaces before changing the data type.

```
**# replace blanks with np.nan**
data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)

**# convert to float64**
data['TotalCharges'] = data['TotalCharges'].astype('float64')
```

Intuitively contract type, tenure (length of stay of the customer), and pricing plans are very important information when it comes to customer churn or retention. Let’s explore the relationship:

![Customer Churn by Tenure, Charges, and Contract Type (Image by Author)](https://cdn-images-1.medium.com/max/2406/1*I-h0lJJnHADHpk7rOUlYOg.png)

Notice that most churn can be seen in the contracts that are “Month-to-Month”. Makes sense, ofcourse. Also, I can see that as the tenure increases and so are the total charges, the likelihood of customers with high tenure and low charges is less compared to customers with high tenure and high charges.

**Missing Values**

```
**# check missing values
**data.isnull().sum()
```

![Missing Values — Image by Author](https://cdn-images-1.medium.com/max/2000/1*HP-9ncnzxgURBYwl6cG9DA.png)

Notice that because we replaced blank values with np.nan there are now 11 rows with missing values in TotalCharges. No problem — I will leave it with PyCaret to impute it automatically.

### **👉Data Preparation**

Common to all modules in PyCaret, the setup is the first and the only mandatory step in any machine learning experiment performed in PyCaret. This function takes care of all the data preparation required prior to training models. Besides performing some basic default processing tasks, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# init setup**
from pycaret.classification import *
s = setup(data, target = 'Churn', ignore_features = ['customerID'])
```

![setup function in pycaret.classification — Image by Author](https://cdn-images-1.medium.com/max/2000/1*w-tUxTQ4p0tDhgYv8DbNOg.png)

Whenever you initialize the setup function in PyCaret, it profiles the dataset and infers the data types for all input features. In this case, you can see except for tenure MonthlyCharges and TotalCharges , everything else is categorical, which is correct, you can now press enter to continue. If data types are not inferred correctly (which can happen sometimes), you can use numeric\_feature and categorical\_feature to overwrite the data types.

Also, notice that I have passed ignore\_features = \['customerID'] in the setup function so that it is not considered when training the models. The good thing about this is PyCaret will not remove the column from the dataset, it will just ignore it behind the scene for model training. As such when you generate predictions at the end, you don’t need to worry about joining IDs back by yourself.

![Output from setup — truncated for display — Image by Author](https://cdn-images-1.medium.com/max/2000/1*Y2N6dU1qvJFwOyTmTbgoCw.png)

### 👉 Model Training & Selection

Now that data preparation is done, let’s start the training process by using compare\_models functionality. This function trains all the algorithms available in the model library and evaluates multiple performance metrics using cross-validation.

```
**# compare all models**
best_model = compare_models(sort='AUC')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2000/1*eHvFHPaXU0IQoshg2_5rlw.png)

The best model based on **AUC**\* \*is Gradient Boosting Classifier . AUC using 10-fold cross-validation is 0.8472.

```
**# print best_model parameters**
print(best_model)
```

![Best Model Parameters — Image by Author](https://cdn-images-1.medium.com/max/2000/1*6TQiy5iPNmCYM0DolQ8Mjg.png)

### **Hyperparameter Tuning**

You can use the tune\_model function from PyCaret to automatically tune the hyperparameters of the model.

```
**# tune best model**
tuned_best_model = tune_model(best_model)
```

![tune\_model results — Image by Author](https://cdn-images-1.medium.com/max/2000/1*NY4wOQYZB0l3V2FkScz8xQ.png)

Notice that AUC has slightly increased from 0.8472 to 0.8478 .

### Model Analysis

```
**# AUC Plot**
plot_model(tuned_best_model, plot = 'auc')
```

![AUC Plot —Image by Author](https://cdn-images-1.medium.com/max/2000/1*QJNvMQmXxWk4n78VHF0jHQ.png)

```
**# Feature Importance Plot**
plot_model(tuned_gbc, plot = 'feature')
```

![Feature Importance Plot — Image by Author](https://cdn-images-1.medium.com/max/2440/1*tahIWrTGqWG-KJTe3MvF5g.png)

```
**# Confusion Matrix**
plot_model(tuned_best_model, plot = 'confusion_matrix')
```

![Confusion Matrix Gradient Boosting Classifier — Image by Author](https://cdn-images-1.medium.com/max/2000/1*5qW6fHWqXi-BPkhxYzcQmg.png)

This confusion matrix is on the test set which includes 30% of our data (2,113 rows) We have 309 ***True Positives*** (15%) — these are the customers for which we will be able to extend the lifetime value. If we wouldn’t have predicted, then there was no opportunity for intervention.

We also have 138 (7%) ***False Positives*** where we will lose money because the promotion offered to these customers will just be an extra cost.

1,388 (66%) are True Negatives (good customers) and 278 (13%) are ***False Negative*** (this is a missed opportunity).

So far we have trained multiple models to select the best model giving the highest AUC, followed by tuning the hyperparameters of the best model to squeeze a little more performance in terms of AUC. However, the best AUC doesn’t necessarily translate into the best model for business.

In a churn model, often the reward of ***true positives*** is way different than the cost of ***false positives***. Let’s use the following assumptions:

* $1,000 voucher will be offered to all the customers identified as churn (True Positive + False Positive);
* If we are able to stop the churn, we will gain $5,000 in customer lifetime value.

Using these assumptions and the confusion matrix above, we can calculate the $ impact of this model:

![$ Impact of Model over 2,113 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*FcLFdEVYe3Y9XWYj144Dgw.png)

It’s a good model but the problem is it’s not a business-smart model. It is doing a pretty good job compared to if you have no model but how can we train and select a model that maximizes the business value. In order to achieve that we have to train, select, and optimize models using business metrics instead of any conventional metric like AUC or Accuracy.

### **👉 Adding Custom Metric in PyCaret**

Thanks to PyCaret, it is extremely easy to achieve this using add\_metric function.

```
**# create a custom function
**def calculate_profit(y, y_pred):
    tp = np.where((y_pred==1) & (y==1), (5000-1000), 0)
    fp = np.where((y_pred==1) & (y==0), -1000, 0)
    return np.sum([tp,fp])

**# add metric to PyCaret
**add_metric('profit', 'Profit', calculate_profit)
```

Now let’s run compare\_models and see the magic.

```
**# compare all models**
best_model = compare_models(sort='Profit')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2046/1*J1eZLSvWgk67Fe4EdxUwAQ.png)

Notice that a new column Profit is added this time and surprisingly Naive Bayes which is a pretty bad model in terms of AUC is the best model when it comes to profit. Let’s see how:

```
**# confusion matrix**
plot_model(best_model, plot = 'confusion_matrix')
```

![Confusion Matrix Naive Bayes — Image by Author](https://cdn-images-1.medium.com/max/2000/1*WKTgO9-KhST6KK4d9qdH4Q.png)

The total number of customers is still the same (2,113 customers in the test set), what’s changed is now how the model is making errors over false positives and false negatives. Let’s put some $ value against it, using the same assumptions (as above):

![$ Impact of Model over 2,113 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*tqM7173iOXcLToPgy9WgUQ.png)

> ## \*\*\*BAM! \**We have just increased profit by \~$400,000 with a model that does 2% less in AUC than the best model. How does this happen? Well, for starters, AUC or any other out-of-the-box classification metric (Accuracy, Recall, Precision, F1, Kappa, etc.) is not a business-smart metric, so it does not take into account the risk and reward proposition. Adding a custom metric and using it for model selection or optimization is a great idea and right way to go with.*

I hope you will appreciate the simplicity and ease of use in PyCaret. With only a few lines of code, we were able to train multiple models and select the one that matters to the business. I am a regular blogger and I mostly write about PyCaret and its use-cases in the real world, If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2412/0*PLdJpNCTXdttEn8W.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2402/0*IvqhUYDstXqz55eF.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### More PyCaret related tutorials:

[**Machine Learning in Alteryx with PyCaret** *A step-by-step tutorial on training and deploying machine learning models in Alteryx Designer using PyCaret*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-alteryx-with-pycaret-fafd52e2d4a) [**Machine Learning in KNIME with PyCaret** *A step-by-step guide on training and deploying end-to-end machine learning pipelines in KNIME using PyCaret*towardsdatascience.com](https://towardsdatascience.com/machine-learning-in-knime-with-pycaret-420346e133e2) [**Easy MLOps with PyCaret + MLflow** *A beginner-friendly, step-by-step tutorial on integrating MLOps in your Machine Learning experiments using PyCaret*towardsdatascience.com](https://towardsdatascience.com/easy-mlops-with-pycaret-mlflow-7fbcbf1e38c6) [**Write and train your own custom machine learning models using PyCaret** towardsdatascience.com](https://towardsdatascience.com/write-and-train-your-own-custom-machine-learning-models-using-pycaret-8fa76237374e) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe)


# Predict Lead Score (the Right Way) Using PyCaret

### Predict Lead Score (the Right Way) Using PyCaret

#### A step-by-step guide on how to build a lead scoring model using PyCaret and increase the ROI on marketing campaigns.

![Predict Lead Conversions (the right way) using PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2674/1*UKajo1_fRw6h5UpW7lQhWQ.png)

### **Introduction**

Leads are the driving force of many businesses today. With the advancement of subscription-based business models particularly in the start-up space, the ability to convert leads into paying customers is key to survival. In simple terms, a “lead” represents a potential customer interested in buying your product/service.

Normally when you acquire the lead, either through a third party service or by running a marketing campaign yourself, it typically includes information like:

* Name and contact details of the lead
* Lead attributes (demographic, social, customer preferences)
* Source of origin (Facebook Ad, Website landing page, third party, etc.)
* Time spent on the website, number of clicks, etc.
* Referral details, etc.

### Lead Management process at a glance

![Lead Management Process at a glance — Image by Author](https://cdn-images-1.medium.com/max/2236/1*IvCN08YMCv2gh6Apt80SiA.png)

A significant amount of time, money, and effort is spent by marketing and sales departments on lead management, a concept that we will take to encompass the three key phases of lead generation, qualification, and monetization.

### 👉Lead Generation

Lead generation is the initiation of customer interest or inquiry into the products or services of your business. Leads are created with the intent of converting the interest or inquiry into sales. There is an unlimited number of third-party companies on the internet that promises to generate the best leads. However, you can also do it yourself by running marketing campaigns. The methods for generating leads typically fall under the umbrella of advertising, but may also include non-paid sources such as organic search engine results or referrals from existing customers.

### 👉 **Lead Qualification**

Lead qualification refers to the process of determining which potential customers are most likely to make an actual purchase. It’s an integral part of the sales funnel, which often takes in many leads but only converts a fraction of them. Lead qualification in simple terms means **assessing and prioritizing the leads to come up with the likelihood of conversion** so that your marketing and sales department can chase the prioritized leads instead of all the leads which can often by in thousands.

### 👉**Lead Conversion**

Lead conversion is a phase where you finally convert a qualified lead into paying customer. It entails all the marketing practices that stimulate a desire to buy a product or service and push a lead towards a purchasing decision\*. \*This is a monetization or closing phase and the outcome of this generally defines the success of the overall marketing campaign.

### 👉 **What does Lead Scoring really mean?**

Imagine your team has many leads (potential customers) but not enough resources to pursue them all. Whether you are a product-led business with tons of freemium users, have a great inbound funnel of leads, or simply an amazing door-to-door sales team, at the end of the day, **you need to prioritize the time of your sales teams and give them the “best” leads.**

> ## The question is how do you do it so you **maximize your win rate**?

One simple way of doing this is by analyzing the historic data and look at attributes based on which the leads have converted into sales. For example, there could be a particular country, city, or postal code where leads have converted to sales 90% of the time historically. Similarly, your data can also tell you customers who have spent more than 20 minutes on your website are converted into sales most of the time. Using these business rules you can create a \*\*Lead Scoring System \*\*that attaches scores (higher the better) to each lead using these business rules.

The problem with this approach is, there is only so much you can cover with business rules. As your business expands, the type and variety of data you can collect will grow exponentially. At some point, a manual rule-based system will not be robust enough to continue to add value.

> ## **Here comes Machine Learning**

You can approach the \*\*Leading Scoring System \*\*from a machine learning perspective, where you can train ML models on customer attributes, lead origin, referrals, and other details available and the target will be **Lead Converted (Yes or No)**.

How do you get the target variable? Well, most CRM systems like Salesforce, Zoho, or Microsoft Dynamics can track the individual lead and their status. The status of the lead will help you create the target variable.

> One word of caution is you have to make sure that you do not leak any information in the training dataset. For example, your CRM system could store the information regarding referral paid to third-party on lead conversion, imagine if you use that information in your training data, it is technically a leakage as you will only pay a referral fee on conversion, and this is something you know after the fact.

![Predictive Lead Scoring Workflow — Image Permission by Author](https://cdn-images-1.medium.com/max/2000/1*roT_nhFL9cdR5Dg0QfLR5A.png)

### Let’s get started with the practical example 👇

### What is PyCaret?

[PyCaret](https://www.pycaret.org/) is an open-source, low-code machine learning library and end-to-end model management tool in Python to automate machine learning workflows. Using PyCaret you can efficiently build and deploy end-to-end machine learning pipelines. To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

![Features of PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2084/0*FdaGo2BLH96-e-4_.png)

### Install PyCaret

```
**# install pycaret
**pip install pycaret
```

### 👉Dataset

For this tutorial, I am using a [Lead Conversion](https://www.kaggle.com/ashydv/leads-dataset) dataset from Kaggle. The dataset contains over 9,000 leads with customer features such as lead origin, source of lead, total time spent on the website, total visits on the website, demographics information, and the target column Converted (*indicating 1 for conversion and 0 for no conversion*).

```
**# import libraries**
import pandas as pd
import numpy as np

**# read csv data
**data **= **pd.read_csv('[Leads.csv'](https://raw.githubusercontent.com/srees1988/predict-churn-py/main/customer_churn_data.csv'))
data.head()
```

![Sample Dataset — Image by Author](https://cdn-images-1.medium.com/max/2076/1*SuUA__cJ_KdbQJzDrT9U0A.png)

### 👉 Exploratory Data Analysis

```
**# check data info
**data.info()
```

![data.info() — Image by Author](https://cdn-images-1.medium.com/max/2000/1*7s_MXGiVe7_4Bxf7fQ0SjA.png)

Notice that there are several columns that have many missing values. There are several ways to deal with missing values. I will leave it for PyCaret to automatically handle the missing values. If you would like to learn more about different methods of imputing missing values in PyCaret, check out this [documentation link](https://pycaret.org/missing-values/).

Intuitively time spent on the website and the activity score along with the source of lead are very important information when it comes to lead conversion. Let’s explore the relationship visually:

![Lead Conversion by total time spent on website, activity score, and origin — Image by Author](https://cdn-images-1.medium.com/max/2000/1*8TqGGUwZbaNpu4mDXVming.png)

Notice that leads coming from the “Add Forms” are likely to convert into sales irrespective of the time spent on the website or the score. For lead originated through API or landing page of the website tells a different story. A higher score along with higher time spent on the website is more likely to convert leads into final sales.

### 👉Data Preparation

Common to all modules in PyCaret, the setup is the first and the only mandatory step in any machine learning experiment performed in PyCaret. This function takes care of all the data preparation required prior to training models. Besides performing some basic default processing tasks, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# init setup**
from pycaret.classification import *
s = setup(data, target = 'Converted', ignore_features = ['Prospect ID', 'Lead Number'])
```

![setup function in pycaret.classification — Image by Author (Image truncated)](https://cdn-images-1.medium.com/max/2008/1*oVPHiRph-nzLSB04GIcryA.png)

Upon initializing the setup function in PyCaret, it automatically profiles the dataset and infers the data types for all input variables. If everything is inferred correctly you can press enter to continue. You can also use numeric\_features and categorical\_features parameter in the setup to force/overwrite the data types.

Also, notice that I have passed ignore\_features = \['Prospect ID', 'Lead Number'] in the setup function so that it is not considered when training the models. The good thing about this is PyCaret will not remove the column from the dataset, it will just ignore it behind the scene for model training. As such when you generate predictions at the end, you don’t need to worry about joining IDs back by yourself.

![Output from setup — truncated for display — Image by Author (Image truncated)](https://cdn-images-1.medium.com/max/2000/1*U-BErPLaoUkIePiO_6pQLQ.png)

### 👉 Model Training & Selection

Now that data preparation is done, let’s start the training process by using compare\_models functionality. This function trains all the algorithms available in the model library and evaluates multiple performance metrics using cross-validation.

```
**# compare all models**
best_model = compare_models(sort='AUC')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2000/1*2nhlUOcws5Fp3ahjZXXuGA.png)

The best model based on **AUC**\* \*is **Catboost Classifier**with an average 10 fold cross-validated AUC of **0.9864.**

```
**# print best_model parameters**
print(best_model.get_all_params())

**# except for catboost you can do this:**
print(best_model)
```

![Catboost Hyperparameters — Image by Author](https://cdn-images-1.medium.com/max/2000/1*bJhAnG55xtkNzIgGZNlciQ.png)

### 👉 Model Analysis

### **AUC-ROC Plot**

AUC — ROC curve is a performance measurement for the classification problems at various threshold settings. ROC is a probability curve and AUC represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes. The higher the AUC, the better the model is at predicting positive and negative classes. While it is very helpful to assess and compare the performance of different models, it is not easy to translate this metric into business value.

```
**# AUC Plot**
plot_model(best_model, plot = 'auc')
```

![AUC plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*r1FSRw2KrRS5U8k-xlKtRw.png)

### **SHAP Values**

Unlike AUC-ROC, shap values do not tell you anything about model performance but instead, interpret the impact of having a certain value for a given feature in comparison to the prediction we’d make if that feature took some baseline value. In the chart below, the y-axis (left) has all the important features of the model, the x-axis is the Shapley value of associated features and the color scale (on right) is the actual value of the feature. Each dot on a graph at each feature is a customer lead (from the test set) — overlapping each other.

The higher the shap value is (x-axis), the higher the likelihood of positive class (which in this case is conversion). So reading from the top, I will interpret this as leads that are tagged as “will revert after reading the email” has a high shap value compared to the base meaning a higher likelihood of conversion. On the contrary, if you see the tag “Ringing”, is exactly the opposite where shap values are on the left side of the base value i.e. negative shap values meaning that this feature is working against conversion. To get a more detailed understanding of shap values, see this [link](https://github.com/slundberg/shap).

```
**# Shapley Values**
interpret_model(best_model)
```

![Shapley Feature Importance plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*ww3sMXldXtxko2wKxQyBqg.png)

### Feature Importance Plot

A feature importance plot is just another way to interpret model results. While Shap values only work for complex tree-based model, feature importance plot is more common and can be used for different families of models. Unlike shap values, feature importance does not tell us the impact of the feature on a particular class, it only tells us if the feature is important.

```
**# Feature Importance
**plot_model(best_model, plot = 'feature')
```

![Feature Importance plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2140/1*2VrWvA8YG5OBcSqCpUt0eQ.png)

### Confusion Matrix

The confusion matrix is another way to look at model performance. Out of all the possible tools, this is perhaps the simplest one. It basically compared the predictions with actual labels and divide them into four quadrants:

* True Positive (**Prediction:** Conversion, **Actual:** Conversion)
* True Negative (**Prediction:** No Conversion, **Actual:** No Conversion)
* False Positive (\*\*Prediction: \*\*Conversion, **Actual:** No Conversion)
* False Negative (**Prediction:** No Conversion, **Actual:** Conversion)

If you sum up all the four quadrants, it will equal the number of customer leads in the test set (1667 + 70 + 84 + 952 = 2,773).

* 952 customers (bottom right quadrant) are true positives, these are the leads model predicted will convert and they converted;
* 70 leads are false positive (*this is where you might have spent efforts that will go to waste*);
* 84 leads are false negatives i.e. (*missed opportunities*); and
* 1,667 leads are true negatives (*no impact*).

  \*\*# Confusion Matrix \*\*plot\_model(best\_model, plot = 'confusion\_matrix')

![Confusion Matrix of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*LYCxb-mEI2PB_OAitEURZQ.png)

So far we have prepared the data for modeling (PyCaret does that automatically when you run the setup function), trained multiple models to select the best model based on the AUC, analyzed performance via different plots such as AUC-ROC, Feature Importance, Confusion Matrix, and Shapley values. However, we haven’t answered the most important question yet:

> ## **What’s the business value of this model and why should we use this model?**

In order to attach business value to this model, let us make few assumptions:

* Lead converted into sales will yield $120 in Revenue for the first year
* Time and efforts spent on chasing prioritized leads (as predicted by the model) is $15
* Opportunities missed by the model (False negatives) yield negative $120 as opportunity cost (*you may or may not add this as this is not the real cost but an opportunity cost, — totally depends on the use case*)

If you just do a little maths here, you will arrive at **$88,830 in profit**. Here’s how:

![$ Impact of Model over 2,773 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*2IzdyZeAL1HybxYwLYKEXw.png)

This may be a good model but it is not a business-smart model as we haven't fed in the assumptions of cost/profit yet. By default, any machine learning algorithm will optimize conventional metrics like AUC. In order to achieve the business goal, we have to train, select, and optimize models using business metrics.

### 👉 Adding Custom Metric in PyCaret

Thanks to PyCaret, it is extremely easy to achieve this using add\_metric function.

```
**# create a custom function
**def calculate_profit(y, y_pred):
    tp = np.where((y_pred==1) & (y==1), (120-15), 0)
    fp = np.where((y_pred==1) & (y==0), -15, 0)
    fn = np.where((y_pred==0) & (y==1), -120, 0)
    return np.sum([tp,fp,fn])

**# add metric to PyCaret
**add_metric('profit', 'Profit', calculate_profit)
```

Now let’s run compare\_models again:

```
**# compare all models**
best_model = compare_models(sort='Profit')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2000/1*nps6sq9lYaM4QkZkvXWRfg.png)

Notice that a new column **Profit** is added this time and \*\*Catboost Classifier \*\*is no more the best model based on Profit. It is \*\*Light Gradient Boosting Machine. \*\*Although the difference is not material in this example but depending on your data and assumptions, this could be millions of dollars sometimes.

```
**# confusion matrix**
plot_model(best_model, plot = 'confusion_matrix')
```

![Confusion Matrix for LightGBM — Image by Author](https://cdn-images-1.medium.com/max/2000/1*Lcipv42jm4ahagD5PX96mg.png)

The total number of customers is still the same (2,773 customers in the test set), what’s changed is now how the model is making errors over false positives and false negatives. Let’s put some $ value against it, using the same assumptions (as above):

![$ Impact of Model over 2,773 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*sp-3GdlsAyQZBCFxxj3ThA.png)

The profit is now $89,925 compared to $88,830 when Catboost Classifier was used. This is a 1.2% lift which depending on the magnitude and cost of false positive and false negative could translate into millions of dollars. There are few other things you can do on top of this such as tune hyperparameters of your best model by explicitly optimizing **Profit** instead of AUC, Accuracy, Recall, Precision, or any other conventional metric.

### How to use the model to generate a lead score?

Well, you must be asking now that we have selected the best model, how do I apply this model to new leads to generate the score? Well, that ain’t hard.

```
**# create copy of data
**data_new = data.copy()
data_new.drop('Converted', axis=1, inplace=True)

**# generate labels using predict_model
**predict_model(best_model, data=data_new, raw_score=True)
```

![Predictions generated using the best \_model — Image by Author](https://cdn-images-1.medium.com/max/2258/1*HZO6S5ObCgEDhTcMIOcmuQ.png)

Notice the last three columns are added to the dataset — Label (1 = conversion, 0 = no conversion), Score\_0, and Score\_1 is the probability for each class between 0 to 1. For example, the first observation Score\_0 is 0.9973 meaning 99.7% probability for no conversion.

I am a regular blogger and I mostly write about PyCaret and its use-cases in the real world, If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2412/0*PLdJpNCTXdttEn8W.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2402/0*IvqhUYDstXqz55eF.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### More PyCaret related tutorials:

[**Predict Customer Churn (the right way) using PyCaret** towardsdatascience.com](https://towardsdatascience.com/predict-customer-churn-the-right-way-using-pycaret-8ba6541608ac) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe)


# NLP Text Classification in Python using PyCaret

### NLP Text-Classification in Python: PyCaret Approach Vs The Traditional Approach

#### A comparative analysis between The Traditional Approach and PyCaret Approach

#### by Prateek Baghel

### I. Introduction

In this post we’ll see a demonstration of an NLP-Classification problem with 2 different approaches in python:

**1-The Traditional approach**: In this approach, we will:

* preprocess the given text data using different NLP techniques
* embed the processed text data with different embedding techniques
* build classification models from more than one ML family on the embedded text data -see the performances of different models and then tune the hyper-parameters of some selected models
* and finally, see the performance of the tuned models. Clearly, doing so in python means writing hundreds of lines of code and that may take at least two to three hours of your time.

**2- The PyCaret approach**: A new approach, wherein we use a low-code Python library, PyCaret, to do all the things in the above mentioned traditional approach but we write less than 30 lines of code and get the results and insights in minutes.

To give you an idea about the difference between the two approaches, please take a look at this rough comparison table below:

![](https://cdn-images-1.medium.com/max/2000/1*ivuj02wvmHjBQ8prmQrirA.png)

You can see that PyCaret approach provides many more solutions and functionalities, all in less time and effort!

### II. The NLP-Classification Problem

Here the task at hand is to identify whether a given SMS is a Spam or a Ham. Here is a glimpse of the raw data and you can find the raw data from this [\*Link](https://github.com/prateek025/SMS_Spam_Ham/blob/master/SMS_Spam_Ham_Raw.csv).\* The data set has 5574 SMS to be classified.

![Head and Tail of raw dataset](https://cdn-images-1.medium.com/max/NaN/1*Jg5TUgAG0NgawLEiRYgg6A.png)

As you may have figured it out that this problem is two-staged: NLP on the raw text data, followed by Classification on the processed text data.

Let’s now begin and see the 2 approaches! I’ll share a link of my code on Github at the bottom of this post.

### III. Traditional Approach

#### Stage 1. Data Setup and Preprocessing on the text data

Before preprocessing, we’ll convert the \*Flag \*column from categorical data type to numeric data type. The resultant dataset looks like this:

![Head and Tail of Dataset with Flag column converted into numeric/dummy values](https://cdn-images-1.medium.com/max/2000/1*f60BNHwh86hhufJOth3Dqg.png)

Next, under the preprocessing step, I have performed the following operations on the text data: -removed HTTP tags -lowered the case -removed all punctuation and Unicode -removed stopwords -lemmatization(converting a word into its root form considering the relevant Part of Speech associated with the word)

After performing all of the 5 operations above, the dataset looks like this:

![Head and Tail of the dataset after preprocessing operations](https://cdn-images-1.medium.com/max/2000/1*1JDtR1AMZnyhp0UON1pA0w.png)

Before we begin with embedding, a quick exploratory analysis of most common words and most rare words might give us an idea on how Spam and Ham SMS may differ from each other.

![15 most common words: They seem to be mostly appearing in the HAM SMS](https://cdn-images-1.medium.com/max/2000/1*uAyqUWFZzeQQrBNfTfAgWQ.png)

![15 most rare words: They seem to be mostly appearing in the SPAM SMS](https://cdn-images-1.medium.com/max/2000/1*Cv5lCR18OhwudRMFS35ASg.png)

Generally, such exploratory analysis helps us in identifying and removing words that may have very less predictive power(because such words appear in abundance) or that they may have induced noise in the model(because such words appear so rarely). However, I have not dropped any more words from the processed text data and have moved to the embedding stage.

#### Stage 2. Embedding on the processed text data

I have used two embedding techniques here. a. *Bag of Words* method: This method creates a term document matrix, wherein every unique word/term becomes a column. In Python, we use \*CountVectorizer() \*function for *BoW embedding*.

![Transformed dataset with BoW embedding](https://cdn-images-1.medium.com/max/2388/1*DrpB6TM-i4D2pGil4X2TfQ.png)

b. *Term Frequency-Inverse Document Frequency* method: This method creates a term document matrix, wherein some weight is applied to each term in the matrix. The weights depend on how common a word occurs in a document and in the entire corpus. In Python, we use \*TfidfVectorizer() \*function for TF-IDF embedding.

![Transformed dataset with TF-IDF embedding](https://cdn-images-1.medium.com/max/2566/1*5UHgqdqV2zc0qRRL-rOLvQ.png)

#### Stage 3. Model Building

Before deciding what models to build, I have split the data with 85% of the data(4737 rows) in the *Training data set*, and the remainder 15%(837 rows) in the *Test data set*. The testing dataset allows us to asses the model performance on the unseen data

![Output of the Train/Test Split of the data](https://cdn-images-1.medium.com/max/2000/1*MAa3Z6FIDhEq17iB05C1MQ.png)

* Here, I have built classification models from four randomly decided ML families: *Random Forest Classifier, Adaboost Classifier, Gradient Boosting Classifier, Naive Bayes Classifier.*
* I have built the above models first on the *BoW embedded* dataset and then on the *TF-IDF embedded* dataset.
* Model performance metrics used are: *Confusion Matrix, Accuracy Score, Precision Score, Recall Score, and ROC-AUC score*.
* I am sharing here only the results of the base models(the \*hyper-parameters \*are not tuned) built on the dataset with *BoW embedding*. I have shared the model performance results on a dataset with *TF-IDF embedd*ing on my Github repository. You can check that on the link provided below:

![1. Results for Random Forest Classifier](https://cdn-images-1.medium.com/max/3040/1*PCZbMiNQyWPi4JFccJRyXQ.png)

![2. Results for AdaBoost Classifier](https://cdn-images-1.medium.com/max/3190/1*WPga77czNgNEYIzekbCwvA.png)

![3. Results for Gradient Boosting Classifier](https://cdn-images-1.medium.com/max/3194/1*PMNt_3CouFENUIvVZwTsqA.png)

![4. Results for Naive-Bayes Classifier](https://cdn-images-1.medium.com/max/3102/1*AxWAiD277nuYuIiRLQwvxw.png)

#### Stage 4. Hyperparameter Tuning

For convenience, I have done hyper-parameter tuning for models built on the dataset with *BoW embedding*. Doing same for the models on \*TF-IDF \*embedded dataset will require repeating and adding around 30–40 \*\*lines of code.

I further decided to go forward with tuning the hyper-parameters for the \*Random Forest Classifier \*and the \*Adaboost Classifier \*models as these two models seem to perform better than the other two models. For hyper-parameter tuning, I have used the Grid-Search method.

![Here is a snippet of the code for hyperparameter tuning, for full code please see the Github link to code repository at the bottom of the link at the bottom of this post.](https://cdn-images-1.medium.com/max/2148/1*CaRuyN7g7rt4XUj251PrvA.png)

The same model performances metrics were used as they were earlier: \*Confusion Matrix, Accuracy score, Precision score, Recall score, ROC-AUC score. \*The results also display *tuned hyper-parameter* values, as well as the 10-Fold cross-validation value of the *Accuracy score* of the tuned model.

The following were the performance results of the tuned models :

![1. Results of the tuned AdaBoost Classifier Model](https://cdn-images-1.medium.com/max/3520/1*2LMSESB_nbtkDNx7LW8Akw.png)

![2. Results of the tuned Random Forest Classifier model](https://cdn-images-1.medium.com/max/3516/1*r3Oq4lxFmcYnMatCb6xt4w.png)

Comparing the two tuned models, *AdaBoost Classifier* performs better on *Cross Validation Accuracy* score.

Now let's explore the PyCaret method..!

### IV. PyCaret Approach

We’ll repeat all the steps carried out under the traditional approach, but you’ll notice how quick and easy this approach is.

#### Stage 1. Data Setup and Preprocessing on the text data

Before performing any ML experiment in PyCaret, you have to set up a PyCaret module environment. This allows for the reproducibility, scalability, and deployment of an ML experiment conducted for more than one time. You can see that it takes only 2 lines of command to do so.

![Output for setting up PyCaret’s NLP module](https://cdn-images-1.medium.com/max/2054/1*5DK96jC_oBQLC_-MCF3xOw.png)

What is great about this function is that it automatically performs all the NLP pre-processing operations(lowering case, removing all the punctuations and stopwords, stemming, lemmatization, and other operations) on your raw text data. This entire step got completed in 21 seconds!

#### Stage 2. Embedding on the processed text data

PyCaret currently supports Topic Modelling embedding techniques only. In this example, we will use the *Latent Dirichlet Allocation(LDA)* technique and the \*Non-Negative Matrix Factorization(NMF) \*technique for embedding. Therefore, it won’t be an apple to apple comparison because we used *BoW embedding and TF-IDF embedding* in the Traditional Method

The embedding process is much easier in PyCaret. You can see in the snippet below that we need only 2 lines of code to embed the processed data. By default *nlp module’s create\_model()* creates 4 topics. You can change the toping numbers by passing the desired numerical value in this function.

![Snippet for LDA embedding and resultant dataset](https://cdn-images-1.medium.com/max/2394/1*180D4bhkXQK2UY4aJkwZZQ.png)

Using the same 2 lines of code but changing the *model parameter*, you can create a dataset with *NMF* embedding.

In addition, PyCaret also provides options wiith multiple graphs for exploratory data analysis at this stage. Again you need just 1 line of code to do so. Though, it must be noted that the exploratory data analysis is based on the \*Topics \*created during the embedding stage.

![Output of \*evaluate\_model() command. \*Click on any of the 5 tabs and select any one of the 4 Topics from the drop-down menu for additional exploratory analysis and insights.](https://cdn-images-1.medium.com/max/2014/1*O5Q_rG8NFRULGi55k4BYCQ.png)

#### Stage 3. Model Building

After NLP, the second part of the overall problem is classification. Therefore, we need a different setup environment to perform the classification experiments.

We will build models on both the *LDA embedded* dataset and the *NMF embedded* dataset. However, we’ll have to drop unnecessary variables(\*SMS, Dominant Topic \*etc.) from both the embedded datasets so that classification models can be built upon it.

![LDA embedded dataset after dropping the three unnecessary variables](https://cdn-images-1.medium.com/max/2000/1*h6YjjxvOxYJ3WSTQprsexA.png)

We used PyCaret’s \*nlp \*module for NLP operation, similarly, we use PyCaret’s *classification* module for Classification part of the problem. To setup *Classification module* just 2 lines of code of are required. In addition, we also have to specify the *Target Variable* and the *Train-Test split* ratio.

![Output from the Classification setup command.](https://cdn-images-1.medium.com/max/2000/1*ABfkCw-evo-BRXvb-cmGng.png)

Just like in the \*nlp \*setup where pre-processing operations are performed automatically, in the \*classification \*setup, depending upon the data, PyCaret automatically creates new features and preforms other preprocessing steps!

If you thought, setting up PyCaret environment and getting automated feature engineering was easy, model building is even easier! All you have to do is write just one command and see the result!

![Output from compare models command. LDA embedded dataset was used here](https://cdn-images-1.medium.com/max/2000/1*WnA-NEHIHmKaUqcDgRH-XQ.png)

You can see PyCaret automatically built base models from 18 different ML classification families and arranged the 15 best models in descending order of *Accuracy score*. It further points out that for a particular performance metric what model performs the best(metric score highlighted in yellow).

All of that done by just 1 command and results were up there in around 1 minute!

We see *Random Forest Classifier model* performs the best in \*Accuracy. \*Let's tune *Random Forest Classifier model.*

#### Stage 4. Hyperparameter Tuning

This is a 3 step process in PyCaret: Create a model, Tune it, Evaluate its performance. Each of the steps requires just 1 line of code!

Tuning \*\*the *Random Forest Classifier built on LDA embedded dataset:*

* In the Input-Output snippet below, each step requires just 1 line of code.
* In order to create a *Random Forest classifier* model you have to pass *‘rf’* value
* *You can observe that the tuned model metrics are better than the base model metrics*
* PyCaret offers 15 evaluation plots. Click on any of the 15 tabs to select the evaluation plot you want to use to obtain further insights.

![3 steps of Tuning a model and Evaluating its performance results](https://cdn-images-1.medium.com/max/4054/1*PXvktJa_-1d5Fa23fmb0Aw.png)

I repeated the same process to tune the models built on the *NMF embedded* data. I tuned an \*Extra Trees Classifier \*model this time with a few changes.

* After setting up a new environment, the results of *compare\_models*() show that the \*Extra Trees Classifier \*model performs the best, hence I decided to tune it.

![Output from setup() and compare\_model() command on the NMF embedded data](https://cdn-images-1.medium.com/max/3118/1*8Wxt-e5bXGHyHlN-CxjMMw.png)

* Here I am repeating the same steps that I followed with LDA embedded data: \*create\_model(), \*then \*tune\_model(), \*and then *evaluate\_model().* You can observe that to create and tune an \*Extra Trees Classifier \*model, you have to pass *‘et’* value. This time I decided to optimize the \*AUC value \*instead of the *Accuracy score* while tuning the hyper-parameters. To do so, I had to pass \*‘AUC’ \*value.

![Creating, tuning, and evaluating an Extra-Tress Classifier model on NMF-embedded data](https://cdn-images-1.medium.com/max/3400/1*sLiMNkki4J4uGkkFWEq1mQ.png)

### V. Comparison of two methods

It can be seen that PyCaret provides solutions, with more options and functionalities, in much fewer lines of code, and even lesser execution time when compared with the traditional method.

I’d like to further point out that comparing the performance results of the models the traditional method with the performance results of the models from the PyCaret method is not an apple to apple comparison, as both methods use different embedding techniques on the text data. We’ll have to wait for a newer version of PyCaret’s *nlp-module* that supports the embedding techniques used in the traditional method.

However, depending upon the business problem, it is important to see that the time and the effort saved, and the insights options gained under the PyCaret method are far more valuable than getting the evaluation metrics values increased by some decimal values under the traditional method.

Here is the rough comparison table to highlight the key differences between the two approaches again.

![](https://cdn-images-1.medium.com/max/2000/1*ivuj02wvmHjBQ8prmQrirA.png)

### VI. Important Links

* [Complete code repository for this comparison](https://github.com/prateek025/SMS_Spam_Ham/blob/master/Spam-Ham.ipynb)
* [PyCaret: User guide and documentation](https://pycaret.org/guide/)
* [PyCaret: Tutorials](https://pycaret.org/tutorial/)

Thank you for reading this post. Happy learning!


# Predict Lead Score (the Right Way) Using PyCaret

### Predict Lead Score (the Right Way) Using PyCaret

#### A step-by-step guide on how to build a lead scoring model using PyCaret and increase the ROI on marketing campaigns.

![Predict Lead Conversions (the right way) using PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2674/1*UKajo1_fRw6h5UpW7lQhWQ.png)

### **Introduction**

Leads are the driving force of many businesses today. With the advancement of subscription-based business models particularly in the start-up space, the ability to convert leads into paying customers is key to survival. In simple terms, a “lead” represents a potential customer interested in buying your product/service.

Normally when you acquire the lead, either through a third party service or by running a marketing campaign yourself, it typically includes information like:

* Name and contact details of the lead
* Lead attributes (demographic, social, customer preferences)
* Source of origin (Facebook Ad, Website landing page, third party, etc.)
* Time spent on the website, number of clicks, etc.
* Referral details, etc.

### Lead Management process at a glance

![Lead Management Process at a glance — Image by Author](https://cdn-images-1.medium.com/max/2236/1*IvCN08YMCv2gh6Apt80SiA.png)

A significant amount of time, money, and effort is spent by marketing and sales departments on lead management, a concept that we will take to encompass the three key phases of lead generation, qualification, and monetization.

### 👉Lead Generation

Lead generation is the initiation of customer interest or inquiry into the products or services of your business. Leads are created with the intent of converting the interest or inquiry into sales. There is an unlimited number of third-party companies on the internet that promises to generate the best leads. However, you can also do it yourself by running marketing campaigns. The methods for generating leads typically fall under the umbrella of advertising, but may also include non-paid sources such as organic search engine results or referrals from existing customers.

### 👉 **Lead Qualification**

Lead qualification refers to the process of determining which potential customers are most likely to make an actual purchase. It’s an integral part of the sales funnel, which often takes in many leads but only converts a fraction of them. Lead qualification in simple terms means **assessing and prioritizing the leads to come up with the likelihood of conversion** so that your marketing and sales department can chase the prioritized leads instead of all the leads which can often by in thousands.

### 👉**Lead Conversion**

Lead conversion is a phase where you finally convert a qualified lead into paying customer. It entails all the marketing practices that stimulate a desire to buy a product or service and push a lead towards a purchasing decision\*. \*This is a monetization or closing phase and the outcome of this generally defines the success of the overall marketing campaign.

### 👉 **What does Lead Scoring really mean?**

Imagine your team has many leads (potential customers) but not enough resources to pursue them all. Whether you are a product-led business with tons of freemium users, have a great inbound funnel of leads, or simply an amazing door-to-door sales team, at the end of the day, **you need to prioritize the time of your sales teams and give them the “best” leads.**

> ## The question is how do you do it so you **maximize your win rate**?

One simple way of doing this is by analyzing the historic data and look at attributes based on which the leads have converted into sales. For example, there could be a particular country, city, or postal code where leads have converted to sales 90% of the time historically. Similarly, your data can also tell you customers who have spent more than 20 minutes on your website are converted into sales most of the time. Using these business rules you can create a \*\*Lead Scoring System \*\*that attaches scores (higher the better) to each lead using these business rules.

The problem with this approach is, there is only so much you can cover with business rules. As your business expands, the type and variety of data you can collect will grow exponentially. At some point, a manual rule-based system will not be robust enough to continue to add value.

> ## **Here comes Machine Learning**

You can approach the \*\*Leading Scoring System \*\*from a machine learning perspective, where you can train ML models on customer attributes, lead origin, referrals, and other details available and the target will be **Lead Converted (Yes or No)**.

How do you get the target variable? Well, most CRM systems like Salesforce, Zoho, or Microsoft Dynamics can track the individual lead and their status. The status of the lead will help you create the target variable.

> One word of caution is you have to make sure that you do not leak any information in the training dataset. For example, your CRM system could store the information regarding referral paid to third-party on lead conversion, imagine if you use that information in your training data, it is technically a leakage as you will only pay a referral fee on conversion, and this is something you know after the fact.

![Predictive Lead Scoring Workflow — Image Permission by Author](https://cdn-images-1.medium.com/max/2000/1*roT_nhFL9cdR5Dg0QfLR5A.png)

### Let’s get started with the practical example 👇

### What is PyCaret?

[PyCaret](https://www.pycaret.org/) is an open-source, low-code machine learning library and end-to-end model management tool in Python to automate machine learning workflows. Using PyCaret you can efficiently build and deploy end-to-end machine learning pipelines. To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

![Features of PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2084/0*FdaGo2BLH96-e-4_.png)

### Install PyCaret

```
**# install pycaret
**pip install pycaret
```

### 👉Dataset

For this tutorial, I am using a [Lead Conversion](https://www.kaggle.com/ashydv/leads-dataset) dataset from Kaggle. The dataset contains over 9,000 leads with customer features such as lead origin, source of lead, total time spent on the website, total visits on the website, demographics information, and the target column Converted (*indicating 1 for conversion and 0 for no conversion*).

```
**# import libraries**
import pandas as pd
import numpy as np

**# read csv data
**data **= **pd.read_csv('[Leads.csv'](https://raw.githubusercontent.com/srees1988/predict-churn-py/main/customer_churn_data.csv'))
data.head()
```

![Sample Dataset — Image by Author](https://cdn-images-1.medium.com/max/2076/1*SuUA__cJ_KdbQJzDrT9U0A.png)

### 👉 Exploratory Data Analysis

```
**# check data info
**data.info()
```

![data.info() — Image by Author](https://cdn-images-1.medium.com/max/2000/1*7s_MXGiVe7_4Bxf7fQ0SjA.png)

Notice that there are several columns that have many missing values. There are several ways to deal with missing values. I will leave it for PyCaret to automatically handle the missing values. If you would like to learn more about different methods of imputing missing values in PyCaret, check out this [documentation link](https://pycaret.org/missing-values/).

Intuitively time spent on the website and the activity score along with the source of lead are very important information when it comes to lead conversion. Let’s explore the relationship visually:

![Lead Conversion by total time spent on website, activity score, and origin — Image by Author](https://cdn-images-1.medium.com/max/2000/1*8TqGGUwZbaNpu4mDXVming.png)

Notice that leads coming from the “Add Forms” are likely to convert into sales irrespective of the time spent on the website or the score. For lead originated through API or landing page of the website tells a different story. A higher score along with higher time spent on the website is more likely to convert leads into final sales.

### 👉Data Preparation

Common to all modules in PyCaret, the setup is the first and the only mandatory step in any machine learning experiment performed in PyCaret. This function takes care of all the data preparation required prior to training models. Besides performing some basic default processing tasks, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# init setup**
from pycaret.classification import *
s = setup(data, target = 'Converted', ignore_features = ['Prospect ID', 'Lead Number'])
```

![setup function in pycaret.classification — Image by Author (Image truncated)](https://cdn-images-1.medium.com/max/2008/1*oVPHiRph-nzLSB04GIcryA.png)

Upon initializing the setup function in PyCaret, it automatically profiles the dataset and infers the data types for all input variables. If everything is inferred correctly you can press enter to continue. You can also use numeric\_features and categorical\_features parameter in the setup to force/overwrite the data types.

Also, notice that I have passed ignore\_features = \['Prospect ID', 'Lead Number'] in the setup function so that it is not considered when training the models. The good thing about this is PyCaret will not remove the column from the dataset, it will just ignore it behind the scene for model training. As such when you generate predictions at the end, you don’t need to worry about joining IDs back by yourself.

![Output from setup — truncated for display — Image by Author (Image truncated)](https://cdn-images-1.medium.com/max/2000/1*U-BErPLaoUkIePiO_6pQLQ.png)

### 👉 Model Training & Selection

Now that data preparation is done, let’s start the training process by using compare\_models functionality. This function trains all the algorithms available in the model library and evaluates multiple performance metrics using cross-validation.

```
**# compare all models**
best_model = compare_models(sort='AUC')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2000/1*2nhlUOcws5Fp3ahjZXXuGA.png)

The best model based on **AUC**\* \*is **Catboost Classifier**with an average 10 fold cross-validated AUC of **0.9864.**

```
**# print best_model parameters**
print(best_model.get_all_params())

**# except for catboost you can do this:**
print(best_model)
```

![Catboost Hyperparameters — Image by Author](https://cdn-images-1.medium.com/max/2000/1*bJhAnG55xtkNzIgGZNlciQ.png)

### 👉 Model Analysis

### **AUC-ROC Plot**

AUC — ROC curve is a performance measurement for the classification problems at various threshold settings. ROC is a probability curve and AUC represents the degree or measure of separability. It tells how much the model is capable of distinguishing between classes. The higher the AUC, the better the model is at predicting positive and negative classes. While it is very helpful to assess and compare the performance of different models, it is not easy to translate this metric into business value.

```
**# AUC Plot**
plot_model(best_model, plot = 'auc')
```

![AUC plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*r1FSRw2KrRS5U8k-xlKtRw.png)

### **SHAP Values**

Unlike AUC-ROC, shap values do not tell you anything about model performance but instead, interpret the impact of having a certain value for a given feature in comparison to the prediction we’d make if that feature took some baseline value. In the chart below, the y-axis (left) has all the important features of the model, the x-axis is the Shapley value of associated features and the color scale (on right) is the actual value of the feature. Each dot on a graph at each feature is a customer lead (from the test set) — overlapping each other.

The higher the shap value is (x-axis), the higher the likelihood of positive class (which in this case is conversion). So reading from the top, I will interpret this as leads that are tagged as “will revert after reading the email” has a high shap value compared to the base meaning a higher likelihood of conversion. On the contrary, if you see the tag “Ringing”, is exactly the opposite where shap values are on the left side of the base value i.e. negative shap values meaning that this feature is working against conversion. To get a more detailed understanding of shap values, see this [link](https://github.com/slundberg/shap).

```
**# Shapley Values**
interpret_model(best_model)
```

![Shapley Feature Importance plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*ww3sMXldXtxko2wKxQyBqg.png)

### Feature Importance Plot

A feature importance plot is just another way to interpret model results. While Shap values only work for complex tree-based model, feature importance plot is more common and can be used for different families of models. Unlike shap values, feature importance does not tell us the impact of the feature on a particular class, it only tells us if the feature is important.

```
**# Feature Importance
**plot_model(best_model, plot = 'feature')
```

![Feature Importance plot of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2140/1*2VrWvA8YG5OBcSqCpUt0eQ.png)

### Confusion Matrix

The confusion matrix is another way to look at model performance. Out of all the possible tools, this is perhaps the simplest one. It basically compared the predictions with actual labels and divide them into four quadrants:

* True Positive (**Prediction:** Conversion, **Actual:** Conversion)
* True Negative (**Prediction:** No Conversion, **Actual:** No Conversion)
* False Positive (\*\*Prediction: \*\*Conversion, **Actual:** No Conversion)
* False Negative (**Prediction:** No Conversion, **Actual:** Conversion)

If you sum up all the four quadrants, it will equal the number of customer leads in the test set (1667 + 70 + 84 + 952 = 2,773).

* 952 customers (bottom right quadrant) are true positives, these are the leads model predicted will convert and they converted;
* 70 leads are false positive (*this is where you might have spent efforts that will go to waste*);
* 84 leads are false negatives i.e. (*missed opportunities*); and
* 1,667 leads are true negatives (*no impact*).

  \*\*# Confusion Matrix \*\*plot\_model(best\_model, plot = 'confusion\_matrix')

![Confusion Matrix of the best\_model — Image by Author](https://cdn-images-1.medium.com/max/2000/1*LYCxb-mEI2PB_OAitEURZQ.png)

So far we have prepared the data for modeling (PyCaret does that automatically when you run the setup function), trained multiple models to select the best model based on the AUC, analyzed performance via different plots such as AUC-ROC, Feature Importance, Confusion Matrix, and Shapley values. However, we haven’t answered the most important question yet:

> ## **What’s the business value of this model and why should we use this model?**

In order to attach business value to this model, let us make few assumptions:

* Lead converted into sales will yield $120 in Revenue for the first year
* Time and efforts spent on chasing prioritized leads (as predicted by the model) is $15
* Opportunities missed by the model (False negatives) yield negative $120 as opportunity cost (*you may or may not add this as this is not the real cost but an opportunity cost, — totally depends on the use case*)

If you just do a little maths here, you will arrive at **$88,830 in profit**. Here’s how:

![$ Impact of Model over 2,773 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*2IzdyZeAL1HybxYwLYKEXw.png)

This may be a good model but it is not a business-smart model as we haven't fed in the assumptions of cost/profit yet. By default, any machine learning algorithm will optimize conventional metrics like AUC. In order to achieve the business goal, we have to train, select, and optimize models using business metrics.

### 👉 Adding Custom Metric in PyCaret

Thanks to PyCaret, it is extremely easy to achieve this using add\_metric function.

```
**# create a custom function
**def calculate_profit(y, y_pred):
    tp = np.where((y_pred==1) & (y==1), (120-15), 0)
    fp = np.where((y_pred==1) & (y==0), -15, 0)
    fn = np.where((y_pred==0) & (y==1), -120, 0)
    return np.sum([tp,fp,fn])

**# add metric to PyCaret
**add_metric('profit', 'Profit', calculate_profit)
```

Now let’s run compare\_models again:

```
**# compare all models**
best_model = compare_models(sort='Profit')
```

![Output from compare\_models — Image by Author](https://cdn-images-1.medium.com/max/2000/1*nps6sq9lYaM4QkZkvXWRfg.png)

Notice that a new column **Profit** is added this time and \*\*Catboost Classifier \*\*is no more the best model based on Profit. It is \*\*Light Gradient Boosting Machine. \*\*Although the difference is not material in this example but depending on your data and assumptions, this could be millions of dollars sometimes.

```
**# confusion matrix**
plot_model(best_model, plot = 'confusion_matrix')
```

![Confusion Matrix for LightGBM — Image by Author](https://cdn-images-1.medium.com/max/2000/1*Lcipv42jm4ahagD5PX96mg.png)

The total number of customers is still the same (2,773 customers in the test set), what’s changed is now how the model is making errors over false positives and false negatives. Let’s put some $ value against it, using the same assumptions (as above):

![$ Impact of Model over 2,773 Customers — Image by Author](https://cdn-images-1.medium.com/max/2000/1*sp-3GdlsAyQZBCFxxj3ThA.png)

The profit is now $89,925 compared to $88,830 when Catboost Classifier was used. This is a 1.2% lift which depending on the magnitude and cost of false positive and false negative could translate into millions of dollars. There are few other things you can do on top of this such as tune hyperparameters of your best model by explicitly optimizing **Profit** instead of AUC, Accuracy, Recall, Precision, or any other conventional metric.

### How to use the model to generate a lead score?

Well, you must be asking now that we have selected the best model, how do I apply this model to new leads to generate the score? Well, that ain’t hard.

```
**# create copy of data
**data_new = data.copy()
data_new.drop('Converted', axis=1, inplace=True)

**# generate labels using predict_model
**predict_model(best_model, data=data_new, raw_score=True)
```

![Predictions generated using the best \_model — Image by Author](https://cdn-images-1.medium.com/max/2258/1*HZO6S5ObCgEDhTcMIOcmuQ.png)

Notice the last three columns are added to the dataset — Label (1 = conversion, 0 = no conversion), Score\_0, and Score\_1 is the probability for each class between 0 to 1. For example, the first observation Score\_0 is 0.9973 meaning 99.7% probability for no conversion.

I am a regular blogger and I mostly write about PyCaret and its use-cases in the real world, If you would like to be notified automatically, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2412/0*PLdJpNCTXdttEn8W.png)

![PyCaret — Image by Author](https://cdn-images-1.medium.com/max/2402/0*IvqhUYDstXqz55eF.png)

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### More PyCaret related tutorials:

[**Predict Customer Churn (the right way) using PyCaret** towardsdatascience.com](https://towardsdatascience.com/predict-customer-churn-the-right-way-using-pycaret-8ba6541608ac) [**Build with PyCaret, Deploy with FastAPI** \*A step-by-step, beginner-friendly tutorial on how to build an end-to-end Machine Learning Pipeline with PyCaret and…\*towardsdatascience.com](https://towardsdatascience.com/build-with-pycaret-deploy-with-fastapi-333c710dc786) [**Time Series Anomaly Detection with PyCaret** *A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret*towardsdatascience.com](https://towardsdatascience.com/time-series-anomaly-detection-with-pycaret-706a6e2b2427) [**Supercharge your Machine Learning Experiments with PyCaret and Gradio** *A step-by-step tutorial to develop and interact with machine learning pipelines rapidly*towardsdatascience.com](https://towardsdatascience.com/supercharge-your-machine-learning-experiments-with-pycaret-and-gradio-5932c61f80d9) [**Multiple Time Series Forecasting with PyCaret** *A step-by-step tutorial on forecasting multiple time series using PyCaret*towardsdatascience.com](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe)


# Predicting Crashes in Gold Prices Using PyCaret

#### [Gold Prediction](https://towardsdatascience.com/tagged/gold-price-prediction)

### Predicting Crashes in Gold Prices Using Machine Learning

#### by Mohammad Riazuddin

#### Part — III of Gold Prediction Series. Step by step guide to predict a crash in Gold prices using Classification with PyCaret

![Gold Price Movement](https://cdn-images-1.medium.com/max/3666/0*etQrkJsMtNUP9EWE.png)

### Approach

In the previous two parts of the [Gold Prediction](https://towardsdatascience.com/machine-learning-to-predict-gold-price-returns-4bdb0506b132) series, we discussed how to import data from free yahoofinancials API and build a regression model to predict return from Gold over two horizons. i.e 14-Day and 22-Day.

In this part, we will try to predict if there would be a ‘sharp fall’ or ‘crash’ in Gold Prices over next 22-Day period. We would be using a classification technique for this experiment. We will also learn how to use the trained model to make a prediction on new data every day. The steps for this exercise would be:

1. \*\*Import and shape the data \*\*— This would be similar to what was explained in Part-I here. You can also download the final dataset from my git [repo](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Training%20Data.csv).
2. **Define&#x20;*****‘sharp fall’*** in Gold Prices. Sharp is not an absolute measure. We will try to define *‘sharp fall’* objectively
3. \*\*Create Label \*\*— Based on the definition of *‘sharp fall’*, we would create labels on historical data
4. Train models to predict the \*‘sharp fall’ \*and use trained model to make prediction on new data

### Preparing Data

This part is exactly the same as we did in Part I. The [notebook](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Classification/Gold%20Prediction%20Experiment%20%20Classification-%20PyCaret.ipynb) contains the entire code chunk for data import and manipulation or you can directly start by loading the dataset which can be downloaded from the link [here](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Training%20Data.csv).

### Defining ‘Sharp Fall’

Any classification problem needs labels. Here we need to create labels by defining and quantifying *‘sharp fall’.*

To define ‘sharp’, I am defining a threshold such that the probability of returns being lower than the threshold for any window (22 Days here and 14 Days here) is 15% (basically left tail of normal distribution with p=0.15). For this, I will need to assume that the distribution of returns is normal. Looking at the distribution of returns, this is a very reasonable assumption to make.

![](https://cdn-images-1.medium.com/max/2000/1*hjdmU6aYxcPQfqQ0QncN5w.png)

![Histogram of Returns for both 14 and 22 Day window. Very close to Normal Distribution](https://cdn-images-1.medium.com/max/2000/1*LiI4fq4eFHkKzvdXamWfxA.png)

To get to the threshold return level for both the windows (14-Day and 22-Day), I would first define the p-value of the left tail of the distribution, which would be 15% in this case. Using this p-value, we get the z-value of the -1.0364 from a standard normal distribution. The following code would do it for us.

```
import scipy.stats as st
#Select Threshold p (left tail probability)
p= 0.15
#Get z-Value
z = st.norm.ppf(p)
print(z)
```

Now, based on the above z-value and Mean and SD of returns for each window, we will get threshold return levels. The forward returns for 14 Day and 22 Day period are in columns “Gold-T+14” and “Gold-T+22” in the ‘data’.

```
#Calculating Threshold (t) for each Y
t_14 = round((z*np.std(data[“Gold-T+14”]))+np.mean(data[“Gold-T+14”]),5)
t_22 = round((z*np.std(data[“Gold-T+22”]))+np.mean(data[“Gold-T+22”]),5)

print(“t_14=”,t_14)
print(“t_22=”,t_22)

t_14= -0.03733
t_22= -0.04636
```

So the threshold return levels are -0.0373 or -3.73% for 14-Day window and -0.0463 or -4.63% for 22-Day window. What this implies is, there is only 15% probability of 14-Day returns being lower than -3.73% and 22-Day return being lower than -4.63%. This is a concept similar to what is used in the calculation of Value At Risk (VAR).

### Creating Labels

We will use the above threshold levels to create labels. Any returns in the two windows lower than the respective threshold will be labeled as 1, else as 0.

```
#Creating Labels
data[‘Y-14’] = (data[‘Gold-T+14’]< t_14)*1
data[‘Y-22’]= (data[‘Gold-T+22’]< t_22)*1
print(“Y-14”, sum(data[‘Y-14’]))
print(“Y-22”, sum(data[‘Y-22’]))

Y-14 338
Y-22 356
```

Out of total 2,379 instances, there have been 338 instances where 14-Day returns have been lower than the threshold of -3.73% and 356 instances for 22-Day when returns have been lower than threshold of -4.63%.

Once we have these labels, we do not actually need the returns columns and hence we delete the actual returns columns.

```
data = data.drop([’Gold-T+14',’Gold-T+22'],axis=1)
data.head()
```

### Modelling with PyCaret

#### 22-Day Window

We will start with the 22-Day window here. I will be using PyCaret’s Classification module here for experimentation.

We import the module above form PyCaret and then delete the label for 14-Day since we are working with 22-Day window here. Just like in Regression, to begin the classification exercise, we need to run *setup()* command to point out the data and target column. Remember all the basic pre-processing is taken care of by PyCaret in the background.

```
from pycaret.classification import *

data_22 = data.drop([’Y-14'],axis=1)
s22 = setup(data=data_22, target=’Y-22', session_id=11, silent=True);
```

To evaluate the set of all the models, we will run the \*compare\_models() \*command with *turbo* set to ***False*** because I want to evaluate all the models currently available in the library.

```
compare_models(turbo=False)
```

![Compare Models Output](https://cdn-images-1.medium.com/max/2832/1*Wmvq7DeuVtmcMdkpz4B94w.png)

Before proceeding with the selection of models, we need to understand which metric is most valuable to us. Choosing a metric in a classification experiment depends on the business problem. There is always a trade-off between Precision and Recall. This means we have to choose and favor a balance between True Positives and False Negatives.

Here, the final model will be used to create a flag for the investor/analyst warning him about the possibility of an impending crash. The investor will then make the decision to hedge his position against the possible fall. Therefore, it is very important that the model is able the predict all/most of the drastic falls. In other words, we want to choose a model with a better ability to have True Positives (better Recall), even if it comes with the cost of some False Positives (lower Precision). In other words, we do not want the model to miss the possibility of \*‘sharp fall’. \*We can afford to have some False Positive because if the model predicts that there will be a sharp fall, and the investor hedges his position, but the fall does not occur, the investor will lose opportunity cost of remaining invested or at most hedge cost (say if he buys out of money Put Options). This cost will be lower than the cost of false negative where the model predicts no *‘Sharp Fall’*, but a massive fall does happen. We need to however keep a tab on the trade-offs in \*\*Precision \*\*and **AUC**.

We will go ahead and create four models namely MLP Classifier (*mlp)*, Extra-Tree Classifier (*et)*, Cat Boost Classifier (*catb*) and Light Gradient Boosting Machine (*lgbm*) with best \*\*Recall \*\*and reasonable **AUC/Precision.**

![](https://cdn-images-1.medium.com/max/2000/1*OUz2ZUmbZLTYwgFn0m3Hvw.png)

![](https://cdn-images-1.medium.com/max/2000/1*AFDkbDD6Mxv7YDz1G_5rbg.png)

![](https://cdn-images-1.medium.com/max/2000/1*kJUEp_A989tlTGHiaFsz2g.png)

![](https://cdn-images-1.medium.com/max/2000/1*LYnj_G6F7yx4x5JmYOdcxA.png)

Based on the results we have, MLP Classifier appears to be the best choice with the highest recall and very decent ***AUC of 94.7%***.

**Hyper-Parameter Tuning**

Once we have the top four models which we would want to pursue further, we need to find the best hyperparameters for the models. PyCaret has a very convenient function of \*\*\*tune\_model() \*\*\*which loops through pre-defined hyper-parameter grids to find the best parameters for our model through 10 fold cross-validation. PyCaret uses the standard ***Randomized-Grid*** search to iterate through the parameters. The number of iterations (*n\_iter*) can be specified to a high number based on compute capacity and time constrain. Within the ***tune\_function()***, PyCaret also allows us to specify the metric we want to optimize. The default is Accuracy, but we can choose other metrics as well. Like we would choose **Recall** here since it is the metric we would want to increase/optimize.

![CatBoost Tuned Output](https://cdn-images-1.medium.com/max/2000/1*D8_Opw0chItS8Z1HB8OCVA.png)

The code above tunes the Cat-Boost classifier to optimize \*\*‘Recall’ \*\*by iterating 50 times over the defined grid and displays the 6 metrics for each fold. We see that **Mean Recall** has improved from ***58.2%*** in base Cat-Boost to ***62.6%*** here. This is a massive jump, not so common at the tuning stage. However, it still remains lower than ***66.6%*** of base ***‘mlp***’ that we created earlier. For the other three models, we did not see improvement in performance by tuning (example in the [notebook](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Classification/Gold%20Prediction%20Experiment%20%20Classification-%20PyCaret.ipynb)). The reason being the random nature of iterating through the parameters. There however would exist a parameter that would equal or exceed the performance of the base model, but for that, we need to increase *n\_iter* even more, which means more compute time.

So currently our top-4 models are:

![](https://cdn-images-1.medium.com/max/2000/1*ok58GJ9EY2YGkhRrhBdpVg.png)

#### **Evaluate Models**

Before moving ahead, let us evaluate the model performance. We will exploit ***evaluate\_model()*** function of PyCaret to evaluate and highlight important aspects of the winning models.

**Confusion Matrix**

![](https://cdn-images-1.medium.com/max/2000/1*W7dfGY1PnVEepgq9Y4LzgA.png)

**Feature Importance**

Since *mlp* and *catb\_tuned* do not provide feature importance, we will use \*lgbm \*to see which features are most important in our predictions:

![](https://cdn-images-1.medium.com/max/2000/1*k9IZNrOlsfgiT4jm27HXOA.png)

We can see that Return of Gold in the past 180 days is the most important factor here. This is also intuitive because if the Gold prices have increased a lot in the past, their chances of falling/correcting are higher and vice-versa. The next 3 features are returns from Silver over 250, 60 and 180 days. Again, Silver and Gold are two most widely traded and correlated precious metals, hence the relationship is very intuitive.

#### **Ensemble Models**

After having tuned the hyper-parameters of the model, we can try Ensembling methods to improve performance. Two ensembling methods we can try is [‘Bagging’ and ‘Boosting’](https://towardsdatascience.com/ensemble-methods-bagging-boosting-and-stacking-c9214a10a205) . Models that do not provide probability estimates cannot be used for Boosting. Hence, we can use Boosting with ‘lgbm’ and ‘et’ only. For others, we tried bagging to see if there were any improvements in performance or not. Below are the code snapshots and the 10-fold results.

![](https://cdn-images-1.medium.com/max/2000/1*lknUUSTHIjRxQ8s0_BRohQ.png)

![Ensembling Results](https://cdn-images-1.medium.com/max/2000/1*aGIg3u79djyiWCE9poQ-BA.png)

As we can see above, the results did not improve for the two models. For other models as well, there was deterioration in performance (check [notebook](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Classification/Gold%20Prediction%20Experiment%20%20Classification-%20PyCaret.ipynb)). Hence our winning model remains the same.

**Blending Models**

Blending models is basically building a voting classifier on top of estimators. For models that provide prediction probability, we can use soft voting (using their probabilities), while for others, we would use hard-voting. The ***blend\_model()*** function defaults to using hard voting, which can be changed manually. I built two blends to see if there was some additional performance that can be extracted.

![](https://cdn-images-1.medium.com/max/2000/1*UwqjMhfu0JtQJKfCOV1VYw.png)

![](https://cdn-images-1.medium.com/max/2000/1*dokZi-hH-1jL2ifHmyAjow.png)

Though none of the models could dethrone ***‘mlp’*** from top position, it is very interesting to see the second blend, ***‘blend2’***, which is a soft combination of ***‘lgbm’*** and ***‘et’***. The performance on **Recall** and **AUC** of **62.25%** and **97.43%** is higher than both ***‘lgbm’*** and ***‘et’*** individually. This exhibits the benefit of blending models. Now our winner models would be reduced to 3.

![](https://cdn-images-1.medium.com/max/2000/1*owcSPrycYFxoW9KrfrJ96g.png)

[\*\*Creating StackNet](https://www.coursera.org/lecture/competitive-data-science/stacknet-s8RLi)\*\*

[Stacking models](https://www.geeksforgeeks.org/stacking-in-machine-learning/) is a method where we allow predictions of one models (or set of models) in one layer to be used as a feature for subsequent layers and finally, the meta-model is allowed to train on the predictions of previous layers and the original features (if *restack=True*) to make the final prediction. PyCaret has a very easy implementation of this where we can build a stack with one layer and one meta-model using ***stack\_model()*** or multiple layers and one meta-model using ***create\_stacknet()***. I have used a different combination to build different stacks and evaluate performance.

![Results of Stack-1](https://cdn-images-1.medium.com/max/2000/1*d6PR6Hj2ZYrBFAifh-KSvw.png)

In the first stack, ***‘stack1’***, I used the under-performing models, ***catb\_tuned*** and ***blend2*** in the first layer to pass on their predictions to the leader model ***mlp*** which would help it to make predictions and the prediction of ***mlp*** are used by meta-model ,which is \*\*Logistic-Regression (LR) \*\*here by default, to make the final prediction. Since ***LR*** did not do very well with complete data (see compare models results) I used *restack=False*, which means only the predictions from previous models gets passed to subsequent estimators, not the original features. What we see here is nothing short of magic. The **Recall** jumps from **66.63%** of our best model ***‘mlp’*** to massive **77.8%** and so does **AUC** and **Precision**. ***‘stack1’*** is definitely far superior to all the models we built earlier. Obviously I had to try other configurations as well to see if better performance can be achieved. And I did find a better configuration:

![Results of Stack 3](https://cdn-images-1.medium.com/max/2000/1*n5ZY0N_c4kBaSVpxn78siw.png)

The stack above, ***‘stack3***, had most resounding success with **Recall** averaging **80.7%**, i.e **14%** higher than our winner ***‘mlp’*** model without sacrificing on **Accuracy** (*95%, an improvement of 3%*), **AUC** (*97.34%, an improvement of 2.5%*) or **Precision** (*86.28%, improvement of massive 7.7%*)

We can use this model to predict on the Test-Data, *(30% of the total observations)* that we separated at the setup stage. We can do that by using *predict\_model()*

![](https://cdn-images-1.medium.com/max/2000/1*lJGUuf_sa1xsaaCB58QG0w.png)

We can see that the performance of the model on test data is even better with \*\*Recall \*\*of **86.9%**

Since we have ***‘stack3’*** as the leading model, we would fit the model on the entire data (including the Test data) and save the model for prediction on new data.

```
classifier_22 = finalize_model(stack3)

save_model(classifier_22,”22D Classifier”)
```

The code above fits the model on entire data and using the ***save\_model()*** function, I have saved the trained model and the pre-processing pipeline in a *pkl* file named [“***22D Classifier***”](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Classification/22D%20Classifier.pkl) in my active directory. This saved model can and will be called on to predict on new data.

#### Predicting on New Data

For making prediction we will need to import the raw prices data just the way we did it the beginning of the exercise to extract the features and then load the model to make the predictions. The only difference would be that we would be importing data till the last trading day to make a prediction on the most recent data, just like we would do in real life. The notebook titled ***‘***[***Gold Prediction New Data — Classification’***](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Classification/Gold%20Prediction%20New%20Data%20-%20Classification.ipynb) in the repo exhibits the data import, preparation and prediction codes.

We will skip the data import and preparation part (check notebook for details) and see the prediction process.

```
from pycaret.classification import *
***#Loading the stored model***
classifier_22 = load_model(“22D Classifier”);
***#Making Predictions***
prediction = predict_model(classifier_22,data=prediction_data)
```

Using ***predict\_model()*** we can apply the loaded model on new set of data to generate the prediction (1 or 0) and the score (the probability attached to the prediction). The *‘prediction’* dataframe will also contain all the features that we extracted.

![Prediction Tail](https://cdn-images-1.medium.com/max/2000/1*MW9Qm_DdhnQFonTPD-meeg.png)

Looking at the Label and Score column of the prediction, the model did not predict a significant fall on any of the days. For example, given the historical returns as of 29th April, the model predicts that a significant fall in Gold Prices over the next 22-Day period is ***not likely***, hence **Label = 0**, with a probability of a meagre 9.19%.

### Conclusion

So here I have walked through steps to create a classifier to predict a significant fall in prices over the next 22-Day period in Gold Prices. The notebook contains codes for 14- Day model as well. You can try to create labels and try to predict similar fall over different windows of time in a similar fashion. Till now, we have created a [regression](https://towardsdatascience.com/machine-learning-to-predict-gold-price-returns-4bdb0506b132) and a classification model. In future, we will try to use the prediction from classification models as features in the regression problem and see if it improves the performance of regression.

### Important Links

[\*\*\*Git-hub Repository](https://github.com/Riazone/Gold-Return-Prediction/tree/master/Classification)\*\*\*

[\*\*\*Part-I and II — Regression](https://towardsdatascience.com/machine-learning-to-predict-gold-price-returns-4bdb0506b132)\*\*\*

[\*\*\*PyCaret](https://pycaret.org/)\*\*\*

[\*\*\*My LinkedIn profile](https://www.linkedin.com/in/riazuddin-mohammad/)\*\*\*


# Predicting Gold Prices Using Machine Learning

#### [Gold Prediction](https://towardsdatascience.com/tagged/gold-price-prediction)

### Predicting Gold Prices Using Machine Learning

#### by Mohammad Riazuddin

#### Part- I Importing and Preparing Data

### Introduction

I have been a student of financial markets for over a decade and have been studying different asset classes and their behavior in different economic conditions. It is difficult to find an asset class which has greater polarization than Gold. There are people who love it and people who hate it, and more often than not, they remain in the same camp forever. Since Gold has very little fundamentals of its own (again a source of polarization), in this multi-part series I will try to predict Gold Price returns using several Machine Learning techniques. Listed below is how I (currently) envisage the series to be:

***Part I : Defining the approach, gathering and preparing data***

***Part II : Regression modelling using PyCaret***

***Part III: Classification modelling using PyCaret***

***Part IV: Time Series modelling using Prophet (Facebook)***

***Part V : Evaluating integration of approaches***

> “Please note that Gold is a very widely traded asset in an extremely competitive market. Making money consistently from any strategy for a long time is extremely difficult, if not impossible. The article is only to share my experience and not a prescription or advocacy to invest or trade. However, to students of the field like myself, the idea can be extended and developed into trading algorithms with individual efforts.”

### Background

Gold has been the original store of value and medium of exchange to mankind for centuries till paper currency took over a couple of centuries ago. However, most of the sustainable paper currencies were backed by Gold till as late as 1971, when the Bretton Woods agreement was scrapped and world currencies became a true ′𝐹𝑖𝑎𝑡′ currency.

Gold, however, continues to garner interest not only as a metal of choice for jewelry, but also as a store of value and often advisable part of a diversified investment portfolio as it tends to be an effective inflation hedge and safe haven when economies are going through a rough patch.

### Approach

In the series we will take different approaches to predict returns from Gold prices using \*\*Machine learning \*\*as highlighted in introduction section

First we will go the regression route to predict future returns of Gold over next 2 and 3 week period. We will do this by using historical returns of different instruments which I believe impact the outlook towards Gold. The fundamental reason is, that I term Gold as a \*‘reactionary’ \*asset. It has little fundamentals of its own and movement in prices often is a derivative of how investors view other asset classes (equities, commodities etc.).

### Importing Data

For this and subsequent exercises, we will need closing price of several instruments for past 10 years . There are various paid (Reuters, Bloomberg) and free resources (IEX, Quandl, Yahoofinance, Google finance) that we can use to import data. Since this project needed different type of asset classes (Equities, Commodities, Debt and precious metals) I found the **‘**[**\*yahoofinancials**](https://pypi.org/project/yahoofinancials/)**\*’** package to be very helpful and straight forward.

```
***#Importing Libraries***
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials
```

I have prepared a list of instruments for which we need to import data. ***yahoofinancials*** package requires Yahoo ticker symbols. The list contains the ticker symbols and their descriptions. The excel file containing the list can be found [here](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Ticker%20List.xlsx) with the name ‘Ticker List’ . We import that file and extract the ticker symbols and the names as separate lists. ([\*see notebook](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Regression/Gold%20Prediction%20Experiment%20%20Regression-%20PyCaret.ipynb)\*)

```
ticker_details = pd.read_excel(“Ticker List.xlsx”)
ticker = ticker_details['Ticker'].to_list()
names = ticker_details['Description'].to_list()
ticker_details.head(20)
```

![](https://cdn-images-1.medium.com/max/2000/1*8j73ugtxNcnvJt4iwFvnLg.png)

Once we have the list, we need to define what date range we need to import the data for. The period I have chosen is Jan 2010 till 1st Mar 2020. The reason I did not pull data prior to that is because the \*\*Global Financial Crisis (GFC) \*\*in 2008–09 massively changed the economic and market landscapes. Relationships prior to that period might be of less relevance now.

We create a date-range and write it to an empty dataframe named ***values*** where we would extract and paste data we pull from yahoofinancials.

```
***#Creating Date Range and adding them to values table***
end_date= “2020–03–01”
start_date = “2010–01–01”
date_range = pd.bdate_range(start=start_date,end=end_date)
values = pd.DataFrame({ ‘Date’: date_range})
values[‘Date’]= pd.to_datetime(values[‘Date’])
```

Once we have the date range in dataframe, we need to use ticker symbols to pull out data from the API. \*\*\*yahoofinancials \*\*\*returns the output in a JSON format. The following code loops over the the list of ticker symbols and extracts just the closing prices for all the historical dates and adds them to the dataframe horizontally merging on the date. Given these asset classes might have different regional and trading holidays, the date ranges for every data pull might not be the same. By merging, we will eventually have several *NAs* which we will *frontfill* later on.

```
***#Extracting Data from Yahoo Finance and Adding them to Values table using date as key
***for i in ticker:
 raw_data = YahooFinancials(i)
 raw_data = raw_data.get_historical_price_data(start_date, end_date, “daily”)
 df = pd.DataFrame(raw_data[i][‘prices’])[[‘formatted_date’,’adjclose’]]
 df.columns = [‘Date1’,i]
 df[‘Date1’]= pd.to_datetime(df[‘Date1’])
 values = values.merge(df,how=’left’,left_on=’Date’,right_on=’Date1')
 values = values.drop(labels=’Date1',axis=1)

***#Renaming columns to represent instrument names rather than their ticker codes for ease of readability***
names.insert(0,’Date’)
values.columns = names
print(values.shape)
print(values.isna().sum())


***#Front filling the NaN values in the data set***
values = values.fillna(method="ffill",axis=0)
values = values.fillna(method="bfill",axis=0)
values.isna().sum()

***# Coercing numeric type to all columns except Date***
cols=values.columns.drop('Date')
values[cols] = values[cols].apply(pd.to_numeric,errors='coerce').round(decimals=1)
values.tail()
```

![Tail of values table](https://cdn-images-1.medium.com/max/2000/1*n9DrEpRxVpV2rDzJBtsDhg.png)

### Preparing Data

In approach above, we highlighted that we will be using lagged returns of the listed instruments to predict future returns on Gold. Here we go on to calculate short-term historical returns of all the instruments and longer term historical returns of few selected instruments.

The fundamental idea behind it is, that if a certain asset has highly outperformed or under performed, there is greater likelihood of portfolio re balancing which would impact returns on other asset classes going forward. \*Eg: If the stock markets (say S\&P500) has shown stupendous returns in past 6 months, asset managers might want to book profits and allocate some funds to say precious metals and prepare for stock market correction. \*The chart below shows how the price movement and correlation between Gold and S\&P500 in different market conditions.

![](https://cdn-images-1.medium.com/max/2334/1*YIsV9sx5qw_GqWVjA4QF_Q.png)

![Sources: Bloomberg, ICE Benchmark Administration, World Gold Council. link](https://cdn-images-1.medium.com/max/2000/1*x6xtsbW5IqY9m1O1ymhYBQ.jpeg)

We can see above that Gold exhibits negative correlation when S\&P500 has an extreme negative movement. Recent sharp fall in stock markets also highlights a similar relationship when Gold rose in anticipation of the fall recording 11% gain YTD compared to 11% YTD loss for S\&P500.

We will however, use Machine Learning to evaluate the hypothesis. You can directly download the values data from my [git-hub repo](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Training%20Data_Values.csv) contained in file name ‘Training Data\_Values’

```
imp = [‘Gold’,’Silver’, ‘Crude Oil’, ‘S&P500’,’MSCI EM ETF’]

***# Calculating Short term -Historical Returns***
change_days = [1,3,5,14,21]

data = pd.DataFrame(data=values[‘Date’])
for i in change_days:
 print(data.shape)
 x= values[cols].pct_change(periods=i).add_suffix(“-T-”+str(i))
 data=pd.concat(objs=(data,x),axis=1)
 x=[]
print(data.shape)

***# Calculating Long term Historical Returns***
change_days = [60,90,180,250]

for i in change_days:
 print(data.shape)
 x= values[imp].pct_change(periods=i).add_suffix(“-T-”+str(i))
 data=pd.concat(objs=(data,x),axis=1)
 x=[]
print(data.shape)
```

Besides the lagged returns, we also see how far the current Gold price is from its moving averages for different windows. This is a very commonly used metric in technical analysis where moving averages offer supports and resistances for asset prices. We use a combination of simple and exponential moving averages. We then add these moving averages to the existing feature space.

```
***#Calculating Moving averages for Gold***
moving_avg = pd.DataFrame(values[‘Date’],columns=[‘Date’])
moving_avg[‘Date’]=pd.to_datetime(moving_avg[‘Date’],format=’%Y-%b-%d’)
***#Adding Simple Moving Average***
moving_avg[‘Gold/15SMA’] = (values[‘Gold’]/(values[‘Gold’].rolling(window=15).mean()))-1
moving_avg[‘Gold/30SMA’] = (values[‘Gold’]/(values[‘Gold’].rolling(window=30).mean()))-1
moving_avg[‘Gold/60SMA’] = (values[‘Gold’]/(values[‘Gold’].rolling(window=60).mean()))-1
moving_avg[‘Gold/90SMA’] = (values[‘Gold’]/(values[‘Gold’].rolling(window=90).mean()))-1
moving_avg[‘Gold/180SMA’] = (values[‘Gold’]/(values[‘Gold’].rolling(window=180).mean()))-1

***#Adding Exponential Moving Average
***moving_avg[‘Gold/90EMA’] = (values[‘Gold’]/(values[‘Gold’].ewm(span=90,adjust=True,ignore_na=True).mean()))-1
moving_avg[‘Gold/180EMA’] = (values[‘Gold’]/(values[‘Gold’].ewm(span=180,adjust=True,ignore_na=True).mean()))-1
moving_avg = moving_avg.dropna(axis=0)
print(moving_avg.shape)
moving_avg.head(20)
```

![Output of Moving Average Dataframe](https://cdn-images-1.medium.com/max/2000/1*nPd7K-2XXRt_e9m3K4pP4g.png)

```
***#Merging Moving Average values to the feature space***
data[‘Date’]=pd.to_datetime(data[‘Date’],format=’%Y-%b-%d’)
data = pd.merge(left=data,right=moving_avg,how=’left’,on=’Date’)
print(data.shape)
data.isna().sum()
```

This was all about features. Now we need to create targets, i.e what we want to predict. Since we are predicting returns, we need to pick a horizon for which we need to predict returns. I have chosen 14-day and 22-day horizons because other smaller horizons tend to be very volatile and lack predictive power. One can however, experiment with other horizons as well.

```
***#Calculating forward returns for Target***
y = pd.DataFrame(data=values[‘Date’])
y[‘Gold-T+14’]=values[“Gold”].pct_change(periods=-14)
y[‘Gold-T+22’]=values[“Gold”].pct_change(periods=-22)
print(y.shape)
y.isna().sum()

***# Removing NAs***

data = data[data[‘Gold-T-250’].notna()]
y = y[y[‘Gold-T+22’].notna()]

***#Adding Target Variables***
data = pd.merge(left=data,right=y,how=’inner’,on=’Date’,suffixes=(False,False))
print(data.shape)
```

Now we have the complete data set ready to start modelling. In the next part we will experiment with different algorithms using the extremely innovative and efficient PyCaret library. I will also exhibit how a pipeline can be created to continuously import new data to generate predictions using the trained models.

### Predicting Gold Prices Using Machine Learning

#### Part- II Regression Modelling with PyCaret

In Part-I, we discussed importing data from open source free API and prepared it in a manner which is suitable for our intended Machine Learning exercise. You can refer to Part-I for the codes or import the final dataset in file name ‘Training Data’ from the [github repo](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Training%20Data.csv).

PyCaret is an open source machine learning library in Python which can be used across any notebook environment and drastically reduces the coding effort making the process extremely efficient and productive. In section below we will see how\*\*\* [PyCaret ](https://pycaret.org/)\*\*\*can supercharge any machine learning experiment. To begin, you will need to install PyCaret using :

```
!pip install pycaret
```

#### 22-Day Model

We take up 22-Day horizon as the target. This means, given the historical data, we will try to predict return in Gold over the next three weeks.

```
***#If you are importing downloaded dataset***
data = pd.read_csv("Training Data.csv")

from pycaret.regression import *

***#We have two target columns. We will remove the T+14 day Target
***data_22= data.drop(['Gold-T+14'],axis=1)
```

**Setup**

To begin any modelling exercise in PyCaret, the first step is the ‘setup’ function. The mandatory variables here are the dataset and the target label in the dataset. All the elementary and necessary data transformations like dropping IDs, One-Hot Encoding the categorical factors and missing value imputation happens behind the scene automatically. PyCaret also offers over 20 pre-processing options. For this example we would go with basics in setup and would try different pre-processing techniques in later experiments.

```
a=setup(data_22,target='Gold-T+22',
        ignore_features=['Date'],session_id=11,
        silent=True,profile=False);
```

In the code above, dataset passed as ‘data\_22’ and target is pointed to the column labeled ‘Gold-T+22’. I have specifically mentioned ‘Date’ column to be ignored so as to prevent PyCaret to create time based features on the date column, which might be very helpful in other cases, but we are not evaluating that now. If you want to see the distribution and correlation between variables, you can keep the argument ‘profile=True’, which displays a panda profiler output. I have intentionally provided ‘session\_id=11’ to be able to recreate the results.

**The Magic Command....*****compare\_models( )***

In the next step I will employ one of my favorite feature of PyCaret, which cuts down hundreds of lines of codes to basically 2 words — ‘compare\_models’. The function uses all the algorithms (25 as now) and fits them to the data, runs a 10-fold cross-validation and spits out 6 evaluation metrics for each model. All this with just 2-words. Two additional arguments that can be used in the function in the interest of time are:

**a. turbo=False** — True in default. When turbo=True, compare models does not evaluate few of the more costly algorithms, namely Kernel Ridge (kr), Automatic Relevance Determination (ard) and Multi-level Perceptron (mlp)

**b. blacklist** — Here, one can pass list of algorithm abbreviations (see docstring) which are known to take much longer time and with little performance improvement. Eg: Below I have blacklisted Theilsen Regressor (tr)

```
compare_models(blacklist=['tr'],turbo=True)
```

![output of compare\_models](https://cdn-images-1.medium.com/max/2000/1*qyHVCx4o4J7DfvHByLWcvA.png)

We will use R-Square (R2) as the metric of choice here. We see that ET, Catboost and KNN are the top three models. In the next step we would tune the hyper-parameters of the three models.

**Tuning Model Hyper-parameters**

PyCaret has a pre-defined grid for every algorithm and ***tune\_model()*** function uses a randomized grid search to find the set of parameters that optimize the choice of metrics (Rsquare here) and displays the cross-validated score for the optimized model. It does not accept a trained model, and needs abbreviation of an estimator passed as string. We will tune Extra Tree (et), K Nearest Neighbors(knn) and CatBoost (catboost) regressors .

```
et_tuned = tune_model(‘et’)
```

![](https://cdn-images-1.medium.com/max/2000/1*Uyr9_ZMPPj1ymb7qQLVEVw.png)

```
catb_tuned = tune_model(‘catboost’)
```

![](https://cdn-images-1.medium.com/max/2000/1*n_Ss1NREh9Bgjcmveb3jIw.png)

```
knn_tuned = tune_model(‘knn’,n_iter=150)

*#I have increased the iteration in knn because increasing iterations have shown to perform better for knn rather than other models in question without significantly increasing the training time.*
```

![](https://cdn-images-1.medium.com/max/2000/1*jNwXyUhJAiWNr2BTb63eEA.png)

We can see above that knn’s R2 increased significantly to 87.86% after tuning, much higher than et and catboost, which did not improve after tuning. This can be because of randomization in the grid search process. At some very high number of iterations, they might improve.

I would also create a base Extra Tree (et) model since its original performance (before tuning ) was very close to tuned knn. We will use the ***create\_model()*** function in PyCaret to create the model.

```
et = create_model(‘et’)
```

**Evaluate Model**

It is important to conduct some model diagnostics on trained models. We will use the \*\*\*evaluate\_model() \*\*\*function in PyCaret to see collection of plots and other diagnostics. It takes in a trained model to return selection of model diagnostic plots and model definitions. We would do do model diagnostics on both of our top models i.e knn\_tuned and et.

![Cook’s Distance Plot knn\_tuned](https://cdn-images-1.medium.com/max/2000/1*vecSoo26snJEaae8bi8OzA.png)

Above, we can see that clearly within the first 500 observations, there were many outliers which not only impact the model performance, but might also impact model generalization in future. Hence, it might be worthy to remove these outliers. But before we do that we will see the feature importance through et (knn does no offer feature importance)

![](https://cdn-images-1.medium.com/max/2000/1*98uU-bVryZsx-ew8k52bJg.png)

We see that return on Silver and EM ETF have on of the highest feature importance, underlining the fact that Silver and Gold often move in pairs while portfolio allocation does shift between Emerging Market equity and Gold.

**Removing Outliers**

To remove outliers, we need to go back to the setup stage and use PyCaret’s inbuilt outlier remover and create the models again to see the impact.

```
b=setup(data_22,target=’Gold-T+22', ignore_features=[‘Date’], session_id=11,silent=True,profile=False,remove_outliers=True);
```

If the \*\*\*‘remove\_outliers’ \*\*\*argument is set to true, PyCaret removes outliers identified through PCA linear dimensionality reduction using the Singular Value Decomposition (SVD) technique. The default impurity level is 5%. This means it will remove 5% of the observation which it feels are outliers.

After removing the outliers, we run our top models again to see if there is any performance improvement, and there clearly is.

![](https://cdn-images-1.medium.com/max/2000/1*XV-SkGw8rAQgNGZZc9p_CA.png)

![et and knn\_tuned results after outlier removal](https://cdn-images-1.medium.com/max/2000/1*Iq5k-FAxyNo9NC_FxB74nw.png)

We see that performance of et has improved from 85.43% to 86.16% and that of knn\_tuned has improved from 87.86% to 88.3%. There has also been reduction in SD across folds.

**Ensemble Models**

We can also try to see if bagging/boosting can improve the model performance. We can use the \*\*\*ensemble\_model() \*\*\*function in PyCaret to quickly see how ensembling methods can improve results through following codes:

```
et_bagged = ensemble_model(et,method=’Bagging’)
knn_tuned_bagged = ensemble_model(knn_tuned, method='Bagging')
```

The above codes will show a similar cross validated score, which did not show much improvement. The results can be seen in the notebook link in the repo.

**Blending Models**

We can blend the top 2 models (et and knn\_tuned) to see if blended models can perform better. It is often seen that blended models often learn different patterns and together they have better predictive powers. I will use the \*\*\*blend\_models() \*\*\*function of PyCaret for this. It takes a list of trained models and returns a blended model and 10-fold cross validated scores.

```
blend_knn_et = blend_models(estimator_list=[knn_tuned,et])
```

![Results of Blended models](https://cdn-images-1.medium.com/max/2000/1*KBFj0LhJQrw8tI1frwPntg.png)

In the table above we see that blend of \*\*\*knn\_tuned \*\*\*and ***et*** returns Mean R2 better than both. It is 1.9% increase in mean R2 and reduction in SD of R2 over \*\*\*knn\_tuned \*\*\*implying a better and more consistent performance across folds.

The mean R2 of 90.2% imply that our model is able to capture on an average 90.2% of the variation in Gold returns from the features we have provided.

**Stacking Models**

Though the results from blending models is great, I like to see if there is a possibility of extracting few more basis points of R2 from the data. To do that we would build a multi level stack of models. This is different from blending as in layers of models are stacked in sequence such that predictions of from models in one layer are passed to the next layer of model along with the original features (if restack = True). The predictions from one set of models help subsequent models immensely in predicting. At the end of the chain is the meta-model (linear by default). PyCaret guide has more details on the [topic](https://pycaret.org/stack-models/). In the notebook I have tried several architectures. Presenting below is the one with best performance:

```
stack2 = create_stacknet(estimator_list=[[catb,et,knn_tuned],[blend_knn_et]], restack=True)
```

![Results of stack2 (Multi-Layer stack)](https://cdn-images-1.medium.com/max/2000/1*C0bE6lZdqnuM1sQ4N1idpg.png)

As we can see above, ***stack2*** model has 1% better R2 than ***blend\_knn\_et***, we would chose ***stack2*** as the best model and save it for prediction.

**Saving Model**

Once the model is trained, we need to save the model in order to use it on new data to make the prediction. We can achieve this by save\_model(). This saves the model in the current directory or any defined path. The code below would save the model and pre-processing pipeline with the name ***‘22Day Regressor’***

```
save_model(model=stack2, model_name=’22Day Regressor’)
```

**Making Prediction on New Data**

Once we have saved our model, we would want to make prediction on new data as they arrive. We can rely on the yahoofinancials package to give us the closing prices of all the instruments, however, we need to prepare the new data again to be able to use the model. The steps will be similar to the what we did while preparing the training data, only difference is we will import the latest data and we will not be creating labels (we cant as we do not have future prices). The following code chuck should import and shape the data making it ready for prediction.

```
***#Importing Libraries***
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from yahoofinancials import YahooFinancials

ticker_details = pd.read_excel("Ticker List.xlsx")
ticker = ticker_details['Ticker'].to_list()
names = ticker_details['Description'].to_list()

***#Preparing Date Range***
end_date= datetime.strftime(datetime.today(),'%Y-%m-%d')
start_date = "2019-01-01"
date_range = pd.bdate_range(start=start_date,end=end_date)
values = pd.DataFrame({ 'Date': date_range})
values['Date']= pd.to_datetime(values['Date'])

***#Extracting Data from Yahoo Finance and Adding them to Values table using date as key***
for i in ticker:
    raw_data = YahooFinancials(i)
    raw_data = raw_data.get_historical_price_data(start_date, end_date, "daily")
    df = pd.DataFrame(raw_data[i]['prices'])[['formatted_date','adjclose']]
    df.columns = ['Date1',i]
    df['Date1']= pd.to_datetime(df['Date1'])
    values = values.merge(df,how='left',left_on='Date',right_on='Date1')
    values = values.drop(labels='Date1',axis=1)

***#Renaming columns to represent instrument names rather than their ticker codes for ease of readability***
names.insert(0,'Date')
values.columns = names

***#Front filling the NaN values in the data set***
values = values.fillna(method="ffill",axis=0)
values = values.fillna(method="bfill",axis=0)

***# Co-ercing numeric type to all columns except Date***
cols=values.columns.drop('Date')
values[cols] = values[cols].apply(pd.to_numeric,errors='coerce').round(decimals=1)
imp = ['Gold','Silver', 'Crude Oil', 'S&P500','MSCI EM ETF']

***# Calculating Short term -Historical Returns***
change_days = [1,3,5,14,21]

data = pd.DataFrame(data=values['Date'])
for i in change_days:
    x= values[cols].pct_change(periods=i).add_suffix("-T-"+str(i))
    data=pd.concat(objs=(data,x),axis=1)
    x=[]

***# Calculating Long term Historical Returns***
change_days = [60,90,180,250]

for i in change_days:
    x= values[imp].pct_change(periods=i).add_suffix("-T-"+str(i))
    data=pd.concat(objs=(data,x),axis=1)
    x=[]

***#Calculating Moving averages for Gold***
moving_avg = pd.DataFrame(values['Date'],columns=['Date'])
moving_avg['Date']=pd.to_datetime(moving_avg['Date'],format='%Y-%b-%d')
moving_avg['Gold/15SMA'] = (values['Gold']/(values['Gold'].rolling(window=15).mean()))-1
moving_avg['Gold/30SMA'] = (values['Gold']/(values['Gold'].rolling(window=30).mean()))-1
moving_avg['Gold/60SMA'] = (values['Gold']/(values['Gold'].rolling(window=60).mean()))-1
moving_avg['Gold/90SMA'] = (values['Gold']/(values['Gold'].rolling(window=90).mean()))-1
moving_avg['Gold/180SMA'] = (values['Gold']/(values['Gold'].rolling(window=180).mean()))-1
moving_avg['Gold/90EMA'] = (values['Gold']/(values['Gold'].ewm(span=90,adjust=True,ignore_na=True).mean()))-1
moving_avg['Gold/180EMA'] = (values['Gold']/(values['Gold'].ewm(span=180,adjust=True,ignore_na=True).mean()))-1
moving_avg = moving_avg.dropna(axis=0)

***#Merging Moving Average values to the feature space***

data['Date']=pd.to_datetime(data['Date'],format='%Y-%b-%d')
data = pd.merge(left=data,right=moving_avg,how='left',on='Date')
data = data[data['Gold-T-250'].notna()]
prediction_data = data.copy()
```

Once data is prepared, we need to load the model and make prediction. To load the model, we will again use the PyCaret’s regression module. The codes below would load the model, make prediction on the new data, and give use the historic prices, Projected Return and the forecasted prices in 3 weeks for each date in the dataset.

```
from pycaret.regression import *

***#Loading the stored model
***regressor_22 = load_model("22Day Regressor");

***#Making Predictions
***predicted_return_22 = predict_model(regressor_22,data=prediction_data)
predicted_return_22=predicted_return_22[['Date','Label']]
predicted_return_22.columns = ['Date','Return_22']

***#Adding return Predictions to Gold Values***
predicted_values = values[['Date','Gold']]
predicted_values = predicted_values.tail(len(predicted_return_22))
predicted_values = pd.merge(left=predicted_values,right=predicted_return_22,on=['Date'],how='inner')
predicted_values['Gold-T+22']=(predicted_values['Gold']*(1+predicted_values['Return_22'])).round(decimals =1)

***#Adding T+22 Date
***from datetime import datetime, timedelta

predicted_values['Date-T+22'] = predicted_values['Date']+timedelta(days = 22)
predicted_values.tail()
```

![](https://cdn-images-1.medium.com/max/2000/1*OKAIYzGtwmhzagdQ1rIXlQ.png)

The table output above shows that closing price of Gold on 17th April 2020 was $1,694.5 and the model predicts that in next 22-Days the returns would be -2.3% resulting in a price target of $1,655 by 9th of May 2020. I have created a separate notebook for prediction titled ***“Gold Prediction New Data — Regression”*** which can be found in the repo [here](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Regression/Gold%20Prediction%20New%20Data%20-%20Regression.ipynb).

We can use the same concepts and techniques for T+14 day prediction. The codes and output can be found in the Jupyter notebook titles ***“Gold Prediction Experiment Regression — PyCaret”*** in the repo [here](https://github.com/Riazone/Gold-Return-Prediction/blob/master/Regression/Gold%20Prediction%20Experiment%20%20Regression-%20PyCaret.ipynb).

### Important Links

***Link to Part-III —*** [***Predicting Crashes in Gold Prices***](https://towardsdatascience.com/predicting-crashes-in-gold-prices-using-machine-learning-5769f548496)

***Link to the*** [***Github Repository***](https://github.com/Riazone/Gold-Return-Prediction)

***Follow me on*** [***LinkedIn***](https://www.linkedin.com/in/riazuddin-mohammad/)

***Guide to*** [***PyCaret***](https://pycaret.org/guide/)


# PyCaret 2.1 Feature Summary

![PyCaret 2.1 is now available for download using pip. https://www.pycaret.org](https://cdn-images-1.medium.com/max/4800/1*OYS6O-iLkoE88fBbd3IKcw.jpeg)

### PyCaret 2.1 is here — What’s new?

We are excited to announce PyCaret 2.1 — update for the month of Aug 2020.

PyCaret is an open-source, **low-code** machine learning library in Python that automates the machine learning workflow. It is an end-to-end machine learning and model management tool that speeds up the machine learning experiment cycle and makes you 10x more productive.

In comparison with the other open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few words only. This makes experiments exponentially fast and efficient.

If you haven’t heard or used PyCaret before, please see our [previous announcement](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e) to get started quickly.

### Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using virtual environment to avoid potential conflict with other libraries. See the following example code to create a \*\*\*conda environment \*\*\*and install pycaret within that conda environment:

```
**# create a conda environment **
conda create --name yourenvname python=3.6  

**# activate environment **
conda activate yourenvname  

**# install pycaret **
pip install **pycaret==2.1  **

**# create notebook kernel linked with the conda environment 
**python -m ****ipykernel install --user --name yourenvname --display-name "display-name"
```

### **PyCaret 2.1 Feature Summary**

### 👉 Hyperparameter Tuning on GPU

In PyCaret 2.0 we have announced GPU-enabled training for certain algorithms (XGBoost, LightGBM and Catboost). What’s new in 2.1 is now you can also tune the hyperparameters of those models on GPU.

```
**# train xgboost using gpu**
xgboost = create_model('xgboost', tree_method = 'gpu_hist')

**# tune xgboost 
**tuned_xgboost **= **tune_model(xgboost)
```

No additional parameter needed inside \*\*tune\_model \*\*function as it automatically inherits the tree\_method from xgboost instance created using the \*\*create\_model \*\*function. If you are interested in little comparison, here it is:

> **100,000 rows with 88 features in a Multiclass problem with 8 classes**

![XGBoost Training on GPU (using Google Colab)](https://cdn-images-1.medium.com/max/2180/1*1lAya7O3sEad9-epPH1sUw.jpeg)

### 👉 Model Deployment

Since the first release of PyCaret in April 2020, you can deploy trained models on AWS simply by using the \*\*deploy\_model \*\*from \*\*\*\*your Notebook. In the recent release, we have added functionalities to support deployment on GCP as well as Microsoft Azure.

#### **Microsoft Azure**

To deploy a model on Microsoft Azure, environment variables for connection string must be set. The connection string can be obtained from the ‘Access Keys’ of your storage account in Azure.

![https:/portal.azure.com — Getting connection string from the storage account](https://cdn-images-1.medium.com/max/3832/1*XPH0ZtRmQkRxVHiqEMLaIw.png)

Once you have copied the connection string, you can set it as an environment variable. See example below:

```
**import os
**os.environ['AZURE_STORAGE_CONNECTION_STRING'] = 'your-conn-string'

**from pycaret.classification import load_model**
deploy_model(model = model, model_name = 'model-name', platform = 'azure', authentication = {'container' : 'container-name'})
```

BOOM! That’s it. Just by using one line of code\*\*, \*\*your entire machine learning pipeline is now shipped on the container in Microsoft Azure. You can access that using the **load\_model** function.

```
**import os
**os.environ['AZURE_STORAGE_CONNECTION_STRING'] = 'your-conn-string'

**from pycaret.classification import load_model
**loaded_model = load_model(model_name = 'model-name', platform = 'azure', authentication = {'container' : 'container-name'})

**from pycaret.classification import predict_model
**predictions = predict_model(loaded_model, data = new-dataframe)
```

#### Google Cloud Platform

To deploy a model on Google Cloud Platform (GCP), you must create a project first either using a command line or GCP console. Once the project is created, you must create a service account and download the service account key as a JSON file, which is then used to set the environment variable.

![Creating a new service account and downloading the JSON from GCP Console](https://cdn-images-1.medium.com/max/3834/1*nN6uslyOixxmYpFcVel8Bw.png)

To learn more about creating a service account, read the [official documentation](https://cloud.google.com/docs/authentication/production). Once you have created a service account and downloaded the JSON file from your GCP console you are ready for deployment.

```
**import os
**os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:/path-to-json-file.json'

**from pycaret.classification import deploy_model
**deploy_model(model = model, model_name = 'model-name', platform = 'gcp', authentication = {'project' : 'project-name', 'bucket' : 'bucket-name'})
```

Model uploaded. You can now access the model from the GCP bucket using the **load\_model** function.

```
**import os
**os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'c:/path-to-json-file.json'

**from pycaret.classification import load_model
**loaded_model = load_model(model_name = 'model-name', platform = 'gcp', authentication = {'project' : 'project-name', 'bucket' : 'bucket-name'})

**from pycaret.classification import predict_model
**predictions = predict_model(loaded_model, data = new-dataframe)
```

### 👉 MLFlow Deployment

In addition to using PyCaret’s native deployment functionalities, you can now also use all the MLFlow deployment capabilities. To use those, you must log your experiment using the **log\_experiment** parameter in the \*\*setup \*\*function.

```
**# init setup**
exp1 = setup(data, target = 'target-name', log_experiment = True, experiment_name = 'exp-name')

**# create xgboost model
**xgboost = create_model('xgboost')

..
..
..

# rest of your script

**# start mlflow server on localhost:5000**
!mlflow ui
```

Now open <https://localhost:5000> on your favorite browser.

![MLFlow UI on https://localhost:5000](https://cdn-images-1.medium.com/max/3838/1*y0nMOMuDeMS1sdFepDngKw.png)

You can see the details of run by clicking the **“Start Time”** shown on the left of **“Run Name”**. What you see inside is all the hyperparameters and scoring metrics of a trained model and if you scroll down a little, all the artifacts are shown as well (see below).

![MLFLow Artifacts](https://cdn-images-1.medium.com/max/3496/1*NS7ifCnHHKRpLHCWeYhNZg.png)

A trained model along with other metadata files are stored under the directory “/model”. MLFlow follows a standard format for packaging machine learning models that can be used in a variety of downstream tools — for example, real-time serving through a REST API or batch inference on Apache Spark. If you want you can serve this model locally you can do that by using MLFlow command line.

```
mlflow models serve -m local-path-to-model
```

You can then send the request to model using CURL to get the predictions.

```
curl [http://127.0.0.1:5000/invocations](http://127.0.0.1:5000/invocations) -H 'Content-Type: application/json' -d '{
    "columns": ["age", "sex", "bmi", "children", "smoker", "region"],
    "data": [[19, "female", 27.9, 0, "yes", "southwest"]]
}'
```

*(Note: This functionality of MLFlow is not supported on Windows OS yet).*

MLFlow also provide integration with AWS Sagemaker and Azure Machine Learning Service. You can train models locally in a Docker container with SageMaker compatible environment or remotely on SageMaker. To deploy remotely to SageMaker you need to set up your environment and AWS user account.

**Example workflow using the MLflow CLI**

```
mlflow sagemaker build-and-push-container 
mlflow sagemaker run-local -m <path-to-model>
mlflow sagemaker deploy <parameters>
```

To learn more about all deployment capabilities of MLFlow, [click here](https://www.mlflow.org/docs/latest/models.html).

### 👉 MLFlow Model Registry

The MLflow Model Registry component is a centralized model store, set of APIs, and UI, to collaboratively manage the full lifecycle of an MLflow Model. It provides model lineage (which MLflow experiment and run produced the model), model versioning, stage transitions (for example from staging to production), and annotations.

If running your own MLflow server, you must use a database-backed backend store in order to access the model registry. [Click here](https://www.mlflow.org/docs/latest/tracking.html#backend-stores) for more information. However, if you are using [Databricks](https://databricks.com/) or any of the managed Databricks services such as [Azure Databricks](https://azure.microsoft.com/en-ca/services/databricks/), you don’t need to worry about setting up anything. It comes with all the bells and whistles you would ever need.

![https://databricks.com/blog/2020/06/25/announcing-mlflow-model-serving-on-databricks.html](https://cdn-images-1.medium.com/max/2048/1*XlT58YrFuszGb-1PIXvKZw.gif)

### 👉 High-Resolution Plotting

This is not ground-breaking but indeed a very useful addition for people using PyCaret for research and publications. The **plot\_model** now has an additional parameter called “scale” through which you can control the resolution and generate high quality plot for your publications.

```
**# create linear regression model**
lr = create_model('lr')

**# plot in high-quality resolution
**plot_model(lr, scale = 5) # default is 1
```

![High-Resolution Residual Plot from PyCaret](https://cdn-images-1.medium.com/max/3456/1*O413K8IUvgYTgD3aTtcYjw.png)

### 👉 User-Defined Loss Function

This is one of the most requested feature ever since release of the first version. Allowing to tune hyperparameters of a model using custom / user-defined function gives immense flexibility to data scientists. It is now possible to use user-defined custom loss functions using \*\*custom\_scorer \*\*parameter in the \*\*tune\_model \*\*function.

```
**# define the loss function**
def my_function(y_true, y_pred):
...
...

**# create scorer using sklearn**
from sklearn.metrics import make_scorer**
**my_own_scorer = make_scorer(my_function, needs_proba=True)

**# train catboost model
**catboost = create_model('catboost')

**# tune catboost using custom scorer
**tuned_catboost = tune_model(catboost, custom_scorer = my_own_scorer)
```

### 👉 Feature Selection

Feature selection is a fundamental step in machine learning. You dispose of a bunch of features and you want to select only the relevant ones and to discard the others. The aim is simplifying the problem by removing unuseful features which would introduce unnecessary noise.

In PyCaret 2.1 we have introduced implementation of Boruta algorithm in Python (originally implemented in R). Boruta is a pretty smart algorithm dating back to 2010 designed to automatically perform feature selection on a dataset. To use this, you simply have to pass the \*\*feature\_selection\_method \*\*within the **setup** function.

```
exp1 = setup(data, target = 'target-var', feature_selection = True, feature_selection_method = 'boruta')
```

To read more about Boruta algorithm, [click here.](https://towardsdatascience.com/boruta-explained-the-way-i-wish-someone-explained-it-to-me-4489d70e154a)

### 👉 Other Changes

* blacklist and whitelist parameters in compare\_models function is now renamed to exclude and include with no change in functionality.
* To set the upper limit on training time in compare\_models function, new parameter budget\_time has been added.
* PyCaret is now compatible with Pandas categorical datatype. Internally they are converted into object and are treated as the same way as object or bool is treated.
* Numeric Imputation New method zero has been added in the numeric\_imputation in the setup function. When method is set to zero, missing values are replaced with constant 0.
* To make the output more human-readable, the Label column returned by predict\_model function now returns the original value instead of encoded value.

To learn more about all the updates in PyCaret 2.1, please see the [release notes](https://github.com/pycaret/pycaret/releases/tag/2.1).

There is no limit to what you can achieve using the lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret/).

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

### Important Links

[User Guide](https://www.pycaret.org/guide) [Documentation](https://pycaret.readthedocs.io/en/latest/) [Official Tutorials ](https://github.com/pycaret/pycaret/tree/master/tutorials)[Example Notebooks](https://github.com/pycaret/pycaret/tree/master/examples) [Other Resources](https://github.com/pycaret/pycaret/tree/master/resources)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)


# Ship ML Models to SQL Server using PyCaret

### Ship Machine Learning Model to Data Using PyCaret — Part II

#### Binary Classification

#### by Umar Farooque

![Photo by Joshua Sortino on Unsplash](https://cdn-images-1.medium.com/max/8390/0*3n2RWRuMocf7X67I)

My previous post [\*\*Machine Learning in SQL using PyCaret 1.0](https://towardsdatascience.com/machine-learning-in-sql-using-pycaret-87aff377d90c)\*\* provided details about integrating [\*\*PyCaret](https://pycaret.org/)\*\* with [\*\*SQL Server](https://www.microsoft.com/en-ca/sql-server/sql-server-downloads)**. In this article, I will provide step-by-step details on how to train and deploy a Supervised Machine Learning Classification model in SQL Server using** [**\*\*PyCaret 2.0**](https://pycaret.org/) **(PyCaret is a low-code ML library in Python).**

**Things to be covered in this article:**

1. How to load data into SQL Server table
2. How to create and save a model in SQL Server table
3. How to make model predictions using the saved model and store results in the table

### **I. Import/Load Data**

You will now have to import CSV file into a database using SQL Server Management Studio.

Create a table “**cancer**” in the database

![](https://cdn-images-1.medium.com/max/2000/0*js8AFIoUDjQZZSPa.png)

Right-click the database and select **Tasks** **->** **Import Data**

![](https://cdn-images-1.medium.com/max/2000/0*tZSAwhgQU9Oq8-uc.png)

For Data Source, select **Flat File Source**. Then use the **Browse** button to select the CSV file. Spend some time configuring the data import before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/1*F4b5xric6n9Mc5sjWT4tHg.png)

For Destination, select the correct database provider (e.g. SQL Server Native Client 11.0). Enter the **Server name**; check **Use SQL Server Authentication**, enter the **Username**, **Password**, and \*\*Database \*\*before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/0*c514MMvjt3DavCyI.png)

In the Select Source Tables and Views window, you can Edit Mappings before clicking the \*\*Next \*\*button.

![](https://cdn-images-1.medium.com/max/2000/0*I4VhN7PyYrQfipU5.png)

Check Run immediately and click the \*\*Next \*\*button

![](https://cdn-images-1.medium.com/max/2000/0*uBqcVcjEyaUQsKNq.png)

Click the Finish button to run the package

### **II. Create ML Model & Save in Database Table**

\*\*Classification **is a type of supervised machine learning to predict the categorical class labels which are discrete and unordered. The module available in the** [**\*\*PyCaret**](https://pycaret.org/) package can be used for **binary** or **multiclass** problems.

In this example, we will be using a ‘**Breast Cancer Dataset**’. Creating and saving a model in a database table is a multi-step process. Let’s go by them step by step:

i. Create a stored procedure to create a trained model in this case an Extra Trees Classifier algorithm. The procedure will read data from the cancer table created in the previous step.

Below is the code used to create the procedure:

```
*-- Stored procedure that generates a PyCaret model using the cancer data using Extra Trees Classifier Algorithm*

DROP PROCEDURE IF EXISTS generate_cancer_pycaret_model;

Go

CREATE PROCEDURE generate_cancer_pycaret_model (@trained_model varbinary(max) OUTPUT) AS

BEGIN

EXECUTE sp_execute_external_script

@language = N'Python'

, @script = N'

import pycaret.classification as cp

import pickle

trail1 = cp.setup(data = cancer_data, target = "Class", silent = True, n_jobs=None)

*# Create Model*
et = cp.create_model("et", verbose=False)


*#To improve our model further, we can tune hyper-parameters using tune_model function.
#We can also optimize tuning based on an evaluation metric. As our choice of metric is F1-score, lets optimize our algorithm!*

tuned_et = cp.tune_model(et, optimize = "F1", verbose=False)


*#The finalize_model() function fits the model onto the complete dataset.
#The purpose of this function is to train the model on the complete dataset before it is deployed in production*

final_model = cp.finalize_model(tuned_et)

*# Before saving the model to the DB table, convert it to a binary object*

trained_model = []
prep = cp.get_config("prep_pipe")
trained_model.append(prep)
trained_model.append(final_model)
trained_model = pickle.dumps(trained_model)'

, @input_data_1 = N'select "Class", "age", "menopause", "tumor_size", "inv_nodes", "node_caps", "deg_malig", "breast", "breast_quad", "irradiat" from dbo.cancer'

, @input_data_1_name = N'cancer_data'

, @params = N'@trained_model varbinary(max) OUTPUT'

, @trained_model = @trained_model OUTPUT;

END;

GO
```

ii. Create a table that is required to store the trained model object

```
DROP TABLE IF EXISTS dbo.pycaret_models;

GO

CREATE TABLE dbo.pycaret_models (
model_id  INT NOT NULL PRIMARY KEY,
dataset_name VARCHAR(100) NOT NULL DEFAULT('default dataset'),
model_name  VARCHAR(100) NOT NULL DEFAULT('default model'),
model   VARBINARY(MAX) NOT NULL
);

GO
```

iii. Invoke stored procedure to create a model object and save into a database table

```
DECLARE @model VARBINARY(MAX);
EXECUTE generate_cancer_pycaret_model @model OUTPUT;
INSERT INTO pycaret_models (model_id, dataset_name, model_name, model) VALUES(2, 'cancer', 'Extra Trees Classifier algorithm', @model);
```

The output of this execution is:

![Output from Console](https://cdn-images-1.medium.com/max/2000/1*rMPx1cdPMqxZ2xAZDpqzsA.png)

The view of table results after saving model

![SQL Server Table Results](https://cdn-images-1.medium.com/max/2000/1*8DcdhzXZupB_fqiO6SofhQ.png)

### **III. Running Predictions**

The next step is to run the prediction for the test dataset based on the saved model. This is again a multi-step process. Let’s go through all the steps again.

i. Create a stored procedure that will use the test dataset to detect cancer for a test datapoint

Below is the code to create a database procedure:

```
DROP PROCEDURE IF EXISTS pycaret_predict_cancer;
GO

CREATE PROCEDURE pycaret_predict_cancer (@id INT, @dataset varchar(100), @model varchar(100))
AS

BEGIN

DECLARE @py_model varbinary(max) = (select model

from pycaret_models

where model_name = @model

and dataset_name = @dataset

and model_id = @id

);

EXECUTE sp_execute_external_script

@language = N'Python',

@script = N'

# Import the scikit-learn function to compute error.

import pycaret.classification as cp

import pickle

cancer_model = pickle.loads(py_model)

*# Generate the predictions for the test set.*

predictions = cp.predict_model(cancer_model, data=cancer_score_data)

OutputDataSet = predictions

print(OutputDataSet)

'

, @input_data_1 = N'select "Class", "age", "menopause", "tumor_size", "inv_nodes", "node_caps", "deg_malig", "breast", "breast_quad", "irradiat" from dbo.cancer'

, @input_data_1_name = N'cancer_score_data'

, @params = N'@py_model varbinary(max)'

, @py_model = @py_model

with result sets (("Class" INT, "age" INT, "menopause" INT, "tumor_size" INT, "inv_nodes" INT,

"node_caps" INT, "deg_malig" INT, "breast" INT, "breast_quad" INT,

"irradiat" INT, "Class_Predict" INT, "Class_Score" float ));

END;

GO
```

ii. Create a table to save the predictions along with the dataset

```
DROP TABLE IF EXISTS [dbo].[pycaret_cancer_predictions];

GO

CREATE TABLE [dbo].[pycaret_cancer_predictions](

[Class_Actual] [nvarchar] (50) NULL,

[age] [nvarchar] (50) NULL,

[menopause] [nvarchar] (50) NULL,

[tumor_size] [nvarchar] (50) NULL,

[inv_nodes] [nvarchar] (50) NULL,

[node_caps] [nvarchar] (50) NULL,

[deg_malig] [nvarchar] (50) NULL,

[breast] [nvarchar] (50) NULL,

[breast_quad] [nvarchar] (50) NULL,

[irradiat] [nvarchar] (50) NULL,

[Class_Predicted] [nvarchar] (50) NULL,

[Class_Score] [float] NULL

) ON [PRIMARY]

GO
```

iii. Call pycaret\_predict\_cancer procedure to save predictions result into a table

```
*--Insert the results of the predictions for test set into a table*

INSERT INTO [pycaret_cancer_predictions]

EXEC pycaret_predict_cancer 2, 'cancer', 'Extra Trees Classifier algorithm';
```

iv. Execute the SQL below to view the result of the prediction

```
*-- Select contents of the table*

SELECT * FROM [pycaret_cancer_predictions];
```

![Predictions Result](https://cdn-images-1.medium.com/max/2000/1*kboWnjA4K41DV6a__l79wA.png)

### IV. Conclusion

In this post, we learnt how to build a classification model using a PyCaret in SQL Server. Similarly, you can build and run other types of supervised and unsupervised ML models depending on the need of your business problem.

![Photo by Tobias Fischer on Unsplash](https://cdn-images-1.medium.com/max/8064/0*45eSsUjDsCd_7_-J)

You can further check out the [\*\*PyCaret](http://pycaret.org/)\*\* website for documentation on other supervised and unsupervised experiments that can be implemented in a similar manner within SQL Server.

My future posts will be tutorials on exploring other supervised & unsupervised learning techniques using Python and **PyCaret** within a S**QL Server**.

### V. Important Links

[PyCaret](https://pycaret.org/)

[My LinkedIn Profile](https://www.linkedin.com/in/umarfarooque/)


# Supercharge Your ML with PyCaret and Gradio

### Supercharge Your Machine Learning Experiments with PyCaret and Gradio

#### A step-by-step tutorial to develop and interact with machine learning pipelines rapidly

![Photo by Hunter Harritt on Unsplash](https://cdn-images-1.medium.com/max/10944/0*izwo6BPsV7Ru4b6r)

### 👉 Introduction

This tutorial is a step-by-step, beginner-friendly explanation of how you can integrate [PyCaret](https://www.pycaret.org) and [Gradio](https://www.gradio.app/), the two powerful open-source libraries in Python, and supercharge your machine learning experimentation within minutes.

This tutorial is a “hello world” example, I have used [Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris) from UCI, which is a multiclassification problem where the goal is to predict the class of iris plants. The code given in this example can be reproduced on any other dataset, without any major modifications.

### 👉 PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is incredibly popular for its ease of use, simplicity, and ability to build and deploy end-to-end ML prototypes quickly and efficiently.

PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it’s imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it.

To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

### 👉 Gradio

Gradio is an open-source Python library for creating customizable UI components around your machine learning models. Gradio makes it easy for you to “play around” with your model in your browser by dragging and dropping in your own images, pasting your own text, recording your own voice, etc., and seeing what the model outputs.

Gradio is useful for:

* Creating quick demos around your trained ML pipelines
* Getting live feedback on model performance
* Debugging your model interactively during development

To learn more about Gradio, check out their [GitHub](https://github.com/gradio-app/gradio).

![The workflow for PyCaret and Gradio](https://cdn-images-1.medium.com/max/2000/1*CLPbvtAvxkI5MbnPFE59sQ.png)

### 👉 Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret which only installs hard dependencies that are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed.

### 👉 Installing Gradio

You can install gradio from pip.

```
pip install gradio
```

### 👉 Let’s get started

```
**# load the iris dataset from pycaret repo**
from pycaret.datasets import get_data
data = get_data('iris')
```

![Sample rows from iris dataset](https://cdn-images-1.medium.com/max/2000/1*qttXFQnZ3atRv_qb9FtVTw.png)

### 👉 Initialize Setup

```
**# initialize setup**
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)
```

![](https://cdn-images-1.medium.com/max/2444/1*m5Sgz4IGqGEKNjbar6hGfg.png)

Whenever you initialize the setup function in PyCaret, it profiles the dataset and infers the data types for all input features. In this case, you can see all the four features (*sepal\_length, sepal\_width, petal\_length, and petal\_width*) are identified correctly as Numeric datatype. You can press enter to continue.

![Output from setup — truncated for display](https://cdn-images-1.medium.com/max/2000/1*MNchQT8Y7E_Lsg-66CVSFg.png)

Common to all modules in PyCaret, the setup function is the first and the only mandatory step to start any machine learning experiment in PyCaret. Besides performing some basic processing tasks by default, PyCaret also offers a wide array of pre-processing features such as [scaling and transformation](https://pycaret.org/normalization/), [feature engineering](https://pycaret.org/feature-interaction/), [feature selection](https://pycaret.org/feature-importance/), and several key data preparatory steps such as [one-hot-encoding](https://pycaret.org/one-hot-encoding/), [missing values imputation](https://pycaret.org/missing-values/), [over-sampling/under-sampling](https://pycaret.org/fix-imbalance/), etc. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

![https://pycaret.org/preprocessing/](https://cdn-images-1.medium.com/max/2242/1*7AOrLPzJWLFH90asByQqsg.png)

### 👉 Compare Models

This is the first step we recommend in the workflow of *any* supervised experiment in PyCaret. This function trains all the available models in the model library using default hyperparameters and evaluates performance metrics using cross-validation.

The output of this function is a table showing the mean cross-validated scores for all the models. The number of folds can be defined using the foldparameter (default = 10 folds). The table is sorted (highest to lowest) by the metric of choice which can be defined using the sortparameter (default = ‘Accuracy’).

```
best = compare_models(n_select = 15)
compare_model_results = pull()
```

n\_select parameter in the setup function controls the return of trained models. In this case, I am setting it to 15, meaning return the top 15 models as a list. pull function in the second line stores the output of compare\_models as pd.DataFrame .

![Output from compare\_models](https://cdn-images-1.medium.com/max/2060/1*Qu62jca8TpZLkhZgUq1uFA.png)

```
len(best)
>>> 15

print(best[:5])
```

![Output from print(best\[:5\])](https://cdn-images-1.medium.com/max/2000/1*_H72UEY5AQlYnQswyZ0xhQ.png)

### 👉 Gradio

Now that we are done with the modeling process, let’s create a simple UI using Gradio to interact with our models. I will do it in two parts, first I will create a function that will use PyCaret’s predict\_model functionality to generate and return predictions and the second part will be feeding that function into Gradio and designing a simple input form for interactivity.

### **Part I — Creating an internal function**

The first two lines of the code take the input features and convert them into pandas DataFrame. Line 7 is creating a unique list of model names displayed in the compare\_models output (this will be used as a dropdown in the UI). Line 8 selects the best model based on the index value of the list (which will be passed in through UI) and Line 9 uses the predict\_model functionality of PyCaret to score the dataset.

### Part II — Creating a UI with Gradio

Line 3 in the code below creates a dropdown for model names, Line 4–7 creates a slider for each of the input features and I have set the default value to the mean of each feature. Line 9 initiates a UI (in the notebook as well as on your local host so you can view it in the browser).

![Output from running Gradio interface](https://cdn-images-1.medium.com/max/2910/1*zVe2L4L8fqDL4zIN75rFwQ.png)

You can see this quick video here to see how easy it is to interact with your pipelines and query your models without writing hundreds of lines of code or developing a full-fledged front-end.

I hope that you will appreciate the ease of use and simplicity in PyCaret and Gradio. In less than 25 lines of code and few minutes of experimentation, I have trained and evaluated multiple models using PyCaret and developed a lightweight UI to interact with models in the Notebook.

### Coming Soon!

Next week I will be writing a tutorial on unsupervised anomaly detection on time-series data using [PyCaret Anomaly Detection Module](https://pycaret.readthedocs.io/en/latest/api/anomaly.html). Please follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1) to get more updates.

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Time Series 101 - For beginners

### Time Series 101 — For beginners

#### A beginner-friendly introduction to Time Series Forecasting

![Photo by Chris Liverani on Unsplash](https://cdn-images-1.medium.com/max/7262/0*AfqHPFyS5tc-9Amn)

### 👉 What is Time Series Data?

Time series data is data collected on the same subject at different points in time, such as **GDP of a country by year, a stock price of a particular company over a period of time, or your own heartbeat recorded at each second**, as a matter of fact, anything that you can capture continuously at different time-intervals is a time series data.

See below as an example of time series data, the chart below is the daily stock price of Tesla Inc. (Ticker Symbol: TSLA) for last year. The y-axis on the right-hand side is the value in US$ (The last point on the chart i.e. $701.91 is the latest stock price as of the writing of this article on April 12, 2021).

![Example of Time Series Data — Tesla Inc. (ticker symbol: TSLA) daily stock price 1Y interval.](https://cdn-images-1.medium.com/max/2874/1*5lgEl2_2wx3b7YEiROYPtA.png)

On the other hand, more conventional datasets such as customer information, product information, company information, etc. which store information at a single point in time are known as cross-sectional data.

See the example below of a dataset that tracks America’s best-selling electric cars in the first half of 2020. Notice that instead of tracking the cars sold over a period of time, the chart below tracks different cars such as Tesla, Chevy, and Nissan in the same time period.

![Source: Forbes](https://cdn-images-1.medium.com/max/2000/1*pzKQuUCGJldCQcORZlLvXQ.jpeg)

It is not very hard to distinguish the difference between cross-sectional and time-series data as the objective of analysis for both datasets are widely different. For the first analysis, we were interested in tracking Tesla stock price over a period of time, whereas for the latter, we wanted to analyze different companies in the same time period i.e. first half of 2020.

However, a typical real-world dataset is likely to be a hybrid. Imagine a retailer like Walmart that sold thousand’s of products every day. If you analyze the sale by-product on a particular day, for example, if you want to find out what’s the number 1 selling item on Christmas eve, this will be a cross-sectional analysis. As opposed to, If you want to find out the sale of one particular item such as PS4 over a period of time (let’s say last 5 years), this now becomes a time-series analysis.

Precisely, the objective of the analysis for time-series and cross-sectional data is different and a real-world dataset is likely to be a hybrid of both time-series as well as cross-sectional data.

### 👉 What is Time Series Forecasting?

Time series forecasting is exactly what it sounds like i.e. predicting the future unknown values. However, unlike sci-fi movies, it’s a little less thrilling in the real world. It involves the collection of historical data, preparing it for algorithms to consume (the algorithm is simply put the maths that goes behind the scene), and then predict the future values based on patterns learned from the historical data.

Can you think of a reason why would companies or anybody be interested in forecasting future values for any time series (GDP, monthly sales, inventory, unemployment, global temperatures, etc.). Let me give you some business perspective:

* A retailer may be interested in predicting future sales at an SKU level for planning and budgeting.
* A small merchant may be interested in forecasting sales by store, so it can schedule the right resources (more people during busy periods and vice versa).
* A software giant like Google may be interested in knowing the busiest hour of the day or busiest day of the week so that it can schedule server resources accordingly.
* The health department may be interested in predicting the cumulative COVID vaccination administered so that it can know the point of consolidation where herd immunity is expected to kick in.

### 👉 Time Series Forecasting Methods

Time series forecasting can broadly be categorized into the following categories:

* **Classical / Statistical Models** — Moving Averages, Exponential smoothing, ARIMA, SARIMA, TBATS
* \*\*Machine Learning \*\*— Linear Regression, XGBoost, Random Forest, or any ML model with reduction methods
* \*\*Deep Learning \*\*— RNN, LSTM

This tutorial is focused on forecasting time series using ***Machine Learning***. For this tutorial, I will use the Regression Module of an open-source, low-code machine library in Python called [PyCaret](https://www.pycaret.org). If you haven’t used PyCaret before, you can get quickly started [here](https://www.pycaret.org/guide). Although, you don’t require any prior knowledge of PyCaret to follow along with this tutorial.

### 👉 PyCaret Regression Module

PyCaret **Regression Module** is a supervised machine learning module used for estimating the relationships between a **dependent variable** (often called the ‘outcome variable’, or ‘target’) and one or more **independent variables** (often called ‘features’, or ‘predictors’).

The objective of regression is to predict continuous values such as sales amount, quantity, temperature, number of customers, etc. All modules in PyCaret provide many [pre-processing](https://www.pycaret.org/preprocessing) features to prepare the data for modeling through the [setup ](https://www.pycaret.org/setup)function. It has over 25 ready-to-use algorithms and [several plots](https://www.pycaret.org/plot-model) to analyze the performance of trained models.

### 👉 Dataset

For this tutorial, I have used the US airline passengers dataset. You can download the dataset from [Kaggle](https://www.kaggle.com/chirag19/air-passengers). This dataset provides monthly totals of US airline passengers from 1949 to 1960.

```
**# read csv file
**import pandas as pd
data = pd.read_csv('AirPassengers.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.head()
```

![Sample rows](https://cdn-images-1.medium.com/max/2000/0*1-RkItCLsIyv3HpN.png)

```
**# create 12 month moving average
**data['MA12'] = data['Passengers'].rolling(12).mean()

**# plot the data and MA
**import plotly.express as px
fig = px.line(data, x="Date", y=["Passengers", "MA12"], template = 'plotly_dark')
fig.show()
```

![US Airline Passenger Dataset Time Series Plot with Moving Average = 12](https://cdn-images-1.medium.com/max/2618/0*iwkq5c6sZM63PU9u.png)

Since machine learning algorithms cannot directly deal with dates, let’s extract some simple features from dates such as month and year, and drop the original date column.

```
**# extract month and year from dates**
data['Month'] = [i.month for i in data['Date']]
data['Year'] = [i.year for i in data['Date']]

**# create a sequence of numbers
**data['Series'] = np.arange(1,len(data)+1)

**# drop unnecessary columns and re-arrange
**data.drop(['Date', 'MA12'], axis=1, inplace=True)
data = data[['Series', 'Year', 'Month', 'Passengers']] 

**# check the head of the dataset**
data.head()
```

![Sample rows after extracting features](https://cdn-images-1.medium.com/max/2000/0*h8TaSF1bi9-Y9Psa.png)

```
**# split data into train-test set
**train = data[data['Year'] < 1960]
test = data[data['Year'] >= 1960]

**# check shape
**train.shape, test.shape
>>> ((132, 4), (12, 4))
```

I have manually split the dataset before initializing the setup . An alternate would be to pass the entire dataset to PyCaret and let it handle the split, in which case you will have to pass data\_split\_shuffle = False in the setup function to avoid shuffling the dataset before the split.

### 👉 Initialize Setup

Now it’s time to initialize the setup function, where we will explicitly pass the training data, test data, and cross-validation strategy using the fold\_strategy parameter.

```
**# import the regression module**
from pycaret.regression import *

**# initialize setup**
s = setup(data = train, test_data = test, target = 'Passengers', fold_strategy = 'timeseries', numeric_features = ['Year', 'Series'], fold = 3, transform_target = True, session_id = 123)
```

### 👉 Train and Evaluate all Models

```
best = compare_models(sort = 'MAE')
```

![Results from compare\_models](https://cdn-images-1.medium.com/max/2000/1*Z7VBrEv1Sh5z532cNy6_qQ.png)

The best model based on cross-validated MAE is \*\*Least Angle Regression \*\*(MAE: 22.3). Let’s check the score on the test set.

```
prediction_holdout = predict_model(best);
```

![Results from predict\_model(best) function](https://cdn-images-1.medium.com/max/2000/0*O0gKIfX126Z0Ni-B.png)

MAE on the test set is 12% higher than the cross-validated MAE. Not so good, but we will work with it. Let’s plot the actual and predicted lines to visualize the fit.

```
**# generate predictions on the original dataset**
predictions = predict_model(best, data=data)

**# add a date column in the dataset**
predictions['Date'] = pd.date_range(start='1949-01-01', end = '1960-12-01', freq = 'MS')

**# line plot**
fig = px.line(predictions, x='Date', y=["Passengers", "Label"], template = 'plotly_dark')

**# add a vertical rectange for test-set separation**
fig.add_vrect(x0="1960-01-01", x1="1960-12-01", fillcolor="grey", opacity=0.25, line_width=0)fig.show()
```

![Actual and Predicted US airline passengers (1949–1960)](https://cdn-images-1.medium.com/max/2624/0*_1esCD8Bx6MZ14Mj.png)

The grey backdrop towards the end is the test period (i.e. 1960). Now let’s finalize the model i.e. train the best model i.e. *Least Angle Regression* on the entire dataset (this time, including the test set).

```
final_best = finalize_model(best)
```

### 👉 Create a future scoring dataset

Now that we have trained our model on the entire dataset (1949 to 1960), let’s predict five years out in the future through 1964. To use our final model to generate future predictions, we first need to create a dataset consisting of the Month, Year, Series column on the future dates.

```
future_dates = pd.date_range(start = '1961-01-01', end = '1965-01-01', freq = 'MS')

future_df = pd.DataFrame()

future_df['Month'] = [i.month for i in future_dates]
future_df['Year'] = [i.year for i in future_dates]    
future_df['Series'] = np.arange(145 (145+len(future_dates)))future_df.head()
```

![Sample rows from future\_df](https://cdn-images-1.medium.com/max/2000/0*N26BSbKSR9u3k7hv.png)

Now, let’s use the future\_df to score and generate predictions.

```
predictions_future = predict_model(final_best, data=future_df)
predictions_future.head()
```

![Sample rows from predictions\_future](https://cdn-images-1.medium.com/max/2000/0*c97sliOBqExx6Hs_.png)

### **👉 Plot the actual data and predictions**

```
concat_df = pd.concat([data,predictions_future], axis=0)
concat_df_i = pd.date_range(start='1949-01-01', end = '1965-01-01', freq = 'MS')
concat_df.set_index(concat_df_i, inplace=True)fig = 

px.line(concat_df, x=concat_df.index, y=["Passengers", "Label"], template = 'plotly_dark')
fig.show()
```

![Actual (1949–1960) and Predicted (1961–1964) US airline passengers](https://cdn-images-1.medium.com/max/2614/0*x8TJJUO--Unxheeg.png)

I hope you find this tutorial easy. If you think you are ready for the next level, you can check out my advanced time-series tutorial on [Multiple Time Series Forecasting with PyCaret](https://towardsdatascience.com/multiple-time-series-forecasting-with-pycaret-bc0a779a22fe).

### Coming Soon!

I will soon be writing a tutorial on unsupervised anomaly detection on time-series data using [PyCaret Anomaly Detection Module](https://pycaret.readthedocs.io/en/latest/api/anomaly.html). If you would like to get more updates, you can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1).

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give ⭐️ on our GitHub repository.

To learn more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Time Series Anomaly Detection with PyCaret

#### [Hands-on Tutorials](https://towardsdatascience.com/tagged/hands-on-tutorials)

### Time Series Anomaly Detection with PyCaret

#### A step-by-step tutorial on unsupervised anomaly detection for time series data using PyCaret

![PyCaret — An open-source, low-code machine learning library in Python](https://cdn-images-1.medium.com/max/2604/1*O-lbKPXdK7716BK8MLpTQA.png)

### 👉 Introduction

This is a step-by-step, beginner-friendly tutorial on detecting anomalies in time series data using PyCaret’s Unsupervised Anomaly Detection Module.

#### Learning Goals of this Tutorial

* What is Anomaly Detection? Types of Anomaly Detection.
* Anomaly Detection use-case in business.
* Training and evaluating anomaly detection model using PyCaret.
* Label anomalies and analyze the results.

### 👉 PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is incredibly popular for its ease of use, simplicity, and ability to build and deploy end-to-end ML prototypes quickly and efficiently.

PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it’s imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it.

To learn more about PyCaret, check out their [GitHub](https://www.github.com/pycaret/pycaret).

### 👉 Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret which only installs hard dependencies that are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed.

### 👉 What is Anomaly Detection

Anomaly Detection is a technique used for identifying **rare items, events, or observations** that raise suspicions by differing significantly from the majority of the data.

Typically, the anomalous items will translate to some kind of problem such as:

* bank fraud,
* structural defect,
* medical problem,
* Error, etc.

Anomaly detection algorithms can broadly be categorized into these groups:

\*\*(a) Supervised: \*\*Used when the data set has labels identifying which transactions are an anomaly and which are normal. *(this is similar to a supervised classification problem)*.

\*\*(b) Unsupervised: \*\*Unsupervised means no labels and a model is trained on the complete data and assumes that the majority of the instances are normal.

**(c) Semi-Supervised:** A model is trained on normal data only *(without any anomalies)*. When the trained model used on the new data points, it can predict whether the new data point is normal or not (based on the distribution of the data in the trained model).

![Anomaly Detection Business use-cases](https://cdn-images-1.medium.com/max/3200/0*viL5WxtnFLMCyFXo)

### 👉 PyCaret Anomaly Detection Module

PyCaret’s [\*\*Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html)\*\* Module is an unsupervised machine learning module that is used for identifying **rare items**, **events,** or \*\*observations. \*\*It provides over 15 algorithms and [several plots](https://www.pycaret.org/plot-model) to analyze the results of trained models.

### 👉 Dataset

I will be using the NYC taxi passengers dataset that contains the number of taxi passengers from July 2014 to January 2015 at half-hourly intervals. You can download the dataset from [here](https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/nyc_taxi.csv).

```
import pandas as pd
data = pd.read_csv('[https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/nyc_taxi.csv](https://raw.githubusercontent.com/numenta/NAB/master/data/realKnownCause/nyc_taxi.csv)')

data['timestamp'] = pd.to_datetime(data['timestamp'])

data.head()
```

![Sample raws from the data](https://cdn-images-1.medium.com/max/2000/1*PR6dPBsezOTlHg23y6HJLA.png)

```
**# create moving-averages
**data['MA48'] = data['value'].rolling(48).mean()
data['MA336'] = data['value'].rolling(336).mean()

# plot 
import plotly.express as px
fig = px.line(data, x="timestamp", y=['value', 'MA48', 'MA336'], title='NYC Taxi Trips', template = 'plotly_dark')
fig.show()
```

![value, moving\_average(48), and moving\_average(336)](https://cdn-images-1.medium.com/max/2626/1*7_u3piw7krj-g_hw98pYxA.png)

### 👉 Data Preparation

Since algorithms cannot directly consume date or timestamp data, we will extract the features from the timestamp and will drop the actual timestamp column before training models.

```
**# drop moving-average columns
**data.drop(['MA48', 'MA336'], axis=1, inplace=True)

**# set timestamp to index**
data.set_index('timestamp', drop=True, inplace=True)

**# resample timeseries to hourly **
data = data.resample('H').sum()

**# creature features from date**
data['day'] = [i.day for i in data.index]
data['day_name'] = [i.day_name() for i in data.index]
data['day_of_year'] = [i.dayofyear for i in data.index]
data['week_of_year'] = [i.weekofyear for i in data.index]
data['hour'] = [i.hour for i in data.index]
data['is_weekday'] = [i.isoweekday() for i in data.index]

data.head()
```

![Sample rows from data after transformations](https://cdn-images-1.medium.com/max/2000/1*tEOAoRNWE6Djjqw4TAzDrg.png)

### 👉 Experiment Setup

Common to all modules in PyCaret, the setup function is the first and the only mandatory step to start any machine learning experiment in PyCaret. Besides performing some basic processing tasks by default, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# init setup**
from pycaret.anomaly import *
s = setup(data, session_id = 123)
```

![setup function in pycaret.anomaly module](https://cdn-images-1.medium.com/max/2740/1*XtjlemIJlJzHWC_jdEuUxA.png)

Whenever you initialize the setup function in PyCaret, it profiles the dataset and infers the data types for all input features. In this case, you can see day\_name and is\_weekday is inferred as categorical and remaining as numeric. You can press enter to continue.

![Output from setup — truncated for display](https://cdn-images-1.medium.com/max/2000/1*Za0hBYrKkUCWIZOBwO6cYg.png)

### 👉 Model Training

To check the list of all available algorithms:

```
**# check list of available models**
models()
```

![Output from models() function](https://cdn-images-1.medium.com/max/2000/1*ukgNW9AQxGMQJp46ZVdQgQ.png)

In this tutorial, I am using Isolation Forest, but you can replace the ID ‘iforest’ in the code below with any other model ID to change the algorithm. If you want to learn more about the Isolation Forest algorithm, you can refer to [this](https://en.wikipedia.org/wiki/Isolation_forest).

```
**# train model
**iforest = create_model('iforest', fraction = 0.1)
iforest_results = assign_model(iforest)
iforest_results.head()
```

![Sample rows from iforest\_results](https://cdn-images-1.medium.com/max/2036/1*ZqqojxS5Ef99RFxXwV7m_w.png)

Notice that two new columns are appended i.e. \*\*Anomaly \*\*that contains value 1 for outlier and 0 for inlier and \*\*Anomaly\_Score \*\*which is a continuous value a.k.a as decision function (internally, the algorithm calculates the score based on which the anomaly is determined).

```
**# check anomalies
**iforest_results[iforest_results['Anomaly'] == 1].head()
```

![sample rows from iforest\_results (FILTER to Anomaly == 1)](https://cdn-images-1.medium.com/max/2016/1*HaOFOsWbixByVdRBK-FkfQ.png)

We can now plot anomalies on the graph to visualize.

```
import plotly.graph_objects as go

**# plot value on y-axis and date on x-axis**
fig = px.line(iforest_results, x=iforest_results.index, y="value", title='NYC TAXI TRIPS - UNSUPERVISED ANOMALY DETECTION', template = 'plotly_dark')

**# create list of outlier_dates**
outlier_dates = iforest_results[iforest_results['Anomaly'] == 1].index

**# obtain y value of anomalies to plot**
y_values = [iforest_results.loc[i]['value'] for i in outlier_dates]

fig.add_trace(go.Scatter(x=outlier_dates, y=y_values, mode = 'markers', 
                name = 'Anomaly', 
                marker=dict(color='red',size=10)))
        
fig.show()
```

![NYC Taxi Trips — Unsupervised Anomaly Detection](https://cdn-images-1.medium.com/max/2632/1*Xg78KCHEgSRVbY4lKOX3Kw.png)

Notice that the model has picked several anomalies around Jan 1st which is a new year eve. The model has also detected a couple of anomalies around Jan 18— Jan 22 which is when the *North American blizzard*\*\* \*\*(a \*\*\*\*fast-moving disruptive blizzard) moved through the Northeast dumping 30 cm in areas around the New York City area.

If you google the dates around the other red points on the graph, you will probably be able to find the leads on why those points were picked up as anomalous by the model *(hopefully)*.

I hope you will appreciate the ease of use and simplicity in PyCaret. In just a few lines of code and few minutes of experimentation, I have trained an unsupervised anomaly detection model and have labeled the dataset to detect anomalies on a time series data.

### Coming Soon!

Next week I will be writing a tutorial on training custom models in PyCaret using [PyCaret Regression Module](https://pycaret.readthedocs.io/en/latest/api/regression.html). You can follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1) to get instant notifications whenever a new tutorial is released.

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Time Series Forecasting with PyCaret Regression

### Time Series Forecasting with PyCaret Regression Module

![Photo by Lukas Blazek on Unsplash](https://cdn-images-1.medium.com/max/12288/0*6t7FzC-AdfDlA9LI)

### PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is incredibly popular for its ease of use, simplicity, and ability to build and deploy end-to-end ML prototypes quickly and efficiently.

PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it's imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it. To learn more about PyCaret, watch this 1-minute video.

This tutorial assumes that you have some prior knowledge and experience with PyCaret. If you haven’t used it before, no problem — you can get a quick headstart through these tutorials:

* [PyCaret 2.2 is here — what’s new](https://towardsdatascience.com/pycaret-2-2-is-here-whats-new-ad7612ca63b)
* [Announcing PyCaret 2.0](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e)
* [Five things you don’t know about PyCaret](https://towardsdatascience.com/5-things-you-dont-know-about-pycaret-528db0436eec)

### Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret which only installs hard dependencies that are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed.

### 👉 PyCaret Regression Module

PyCaret **Regression Module** is a supervised machine learning module used for estimating the relationships between a **dependent variable** (often called the ‘outcome variable’, or ‘target’) and one or more **independent variables** (often called ‘features’, or ‘predictors’).

The objective of regression is to predict continuous values such as sales amount, quantity, temperature, number of customers, etc. All modules in PyCaret provide many [pre-processing](https://www.pycaret.org/preprocessing) features to prepare the data for modeling through the [setup ](https://www.pycaret.org/setup)function. It has over 25 ready-to-use algorithms and [several plots](https://www.pycaret.org/plot-model) to analyze the performance of trained models.

### 👉 Time Series with PyCaret Regression Module

Time series forecasting can broadly be categorized into the following categories:

* **Classical / Statistical Models** — Moving Averages, Exponential smoothing, ARIMA, SARIMA, TBATS
* \*\*Machine Learning \*\*— Linear Regression, XGBoost, Random Forest, or any ML model with reduction methods
* \*\*Deep Learning \*\*— RNN, LSTM

This tutorial is focused on the second category i.e. *Machine Learning*.

PyCaret’s Regression module default settings are not ideal for time series data because it involves few data preparatory steps that are not valid for ordered data (*data with a sequence such as time series data*).

For example, the split of the dataset into train and test set is done randomly with shuffling. This wouldn’t make sense for time series data as you don’t want the recent dates to be included in the training set whereas historical dates are part of the test set.

Time-series data also requires a different kind of cross-validation since it needs to respect the order of dates. PyCaret regression module by default uses k-fold random cross-validation when evaluating models. The default cross-validation setting is not suitable for time-series data.

The following section in this tutorial will demonstrate how you can change default settings in PyCaret Regression Module easily to make it work for time series data.

### 👉 Dataset

For the purpose of this tutorial, I have used the US airline passengers dataset. You can download the dataset from [Kaggle](https://www.kaggle.com/chirag19/air-passengers).

```
**# read csv file
**import pandas as pd
data = pd.read_csv('AirPassengers.csv')
data['Date'] = pd.to_datetime(data['Date'])
data.head()
```

![Sample rows](https://cdn-images-1.medium.com/max/2000/1*9Gn9v-CWD3Eca3V92edtDw.png)

```
**# create 12 month moving average
**data['MA12'] = data['Passengers'].rolling(12).mean()

**# plot the data and MA
**import plotly.express as px
fig = px.line(data, x="Date", y=["Passengers", "MA12"], template = 'plotly_dark')
fig.show()
```

![US Airline Passenger Dataset Time Series Plot with Moving Average = 12](https://cdn-images-1.medium.com/max/2618/1*vXL7m7exxTid0kGcU9jGUA.png)

Since algorithms cannot directly deal with dates, let’s extract some simple features from dates such as month and year, and drop the original date column.

```
**# extract month and year from dates**
data['Month'] = [i.month for i in data['Date']]
data['Year'] = [i.year for i in data['Date']]

**# create a sequence of numbers
**data['Series'] = np.arange(1,len(data)+1)

**# drop unnecessary columns and re-arrange
**data.drop(['Date', 'MA12'], axis=1, inplace=True)
data = data[['Series', 'Year', 'Month', 'Passengers']] 

**# check the head of the dataset**
data.head()
```

![Sample rows after extracting features](https://cdn-images-1.medium.com/max/2000/1*T4xXVYhrfIyB35EDjl645A.png)

```
**# split data into train-test set
**train = data[data['Year'] < 1960]
test = data[data['Year'] >= 1960]

**# check shape
**train.shape, test.shape
>>> ((132, 4), (12, 4))
```

I have manually split the dataset before initializing the setup . An alternate would be to pass the entire dataset to PyCaret and let it handle the split, in which case you will have to pass data\_split\_shuffle = False in the setup function to avoid shuffling the dataset before the split.

### 👉 **Initialize Setup**

Now it’s time to initialize the setup function, where we will explicitly pass the training data, test data, and cross-validation strategy using the fold\_strategy parameter.

```
**# import the regression module**
from pycaret.regression import *

**# initialize setup**
s = setup(data = train, test_data = test, target = 'Passengers', fold_strategy = 'timeseries', numeric_features = ['Year', 'Series'], fold = 3, transform_target = True, session_id = 123)
```

### 👉 **Train and Evaluate all Models**

```
best = compare_models(sort = 'MAE')
```

![Results from compare\_models](https://cdn-images-1.medium.com/max/2000/1*Mnqplw1KbJYm9fxyH-46Tg.png)

The best model based on cross-validated MAE is \*\*Least Angle Regression \*\*(MAE: 22.3). Let’s check the score on the test set.

```
prediction_holdout = predict_model(best);
```

![Results from predict\_model(best) function](https://cdn-images-1.medium.com/max/2000/1*Us888u-jaVQzasN8Kn3z6A.png)

MAE on the test set is 12% higher than the cross-validated MAE. Not so good, but we will work with it. Let’s plot the actual and predicted lines to visualize the fit.

```
**# generate predictions on the original dataset**
predictions = predict_model(best, data=data)

**# add a date column in the dataset**
predictions['Date'] = pd.date_range(start='1949-01-01', end = '1960-12-01', freq = 'MS')

**# line plot**
fig = px.line(predictions, x='Date', y=["Passengers", "Label"], template = 'plotly_dark')

**# add a vertical rectange for test-set separation**
fig.add_vrect(x0="1960-01-01", x1="1960-12-01", fillcolor="grey", opacity=0.25, line_width=0)

fig.show()
```

![Actual and Predicted US airline passengers (1949–1960)](https://cdn-images-1.medium.com/max/2624/1*BlfRbXuxwcgvs-zrpK8C0Q.png)

The grey backdrop towards the end is the test period (i.e. 1960). Now let’s finalize the model i.e. train the best model i.e. *Least Angle Regression* on the entire dataset (this time, including the test set).

```
final_best = finalize_model(best)
```

### 👉 Create a future scoring dataset

Now that we have trained our model on the entire dataset (1949 to 1960), let’s predict five years out in the future through 1964. To use our final model to generate future predictions, we first need to create a dataset consisting of the Month, Year, Series column on the future dates.

```
future_dates = pd.date_range(start = '1961-01-01', end = '1965-01-01', freq = 'MS')

future_df = pd.DataFrame()

future_df['Month'] = [i.month for i in future_dates]
future_df['Year'] = [i.year for i in future_dates]    
future_df['Series'] = np.arange(145,(145+len(future_dates)))

future_df.head()
```

![Sample rows from future\_df](https://cdn-images-1.medium.com/max/2000/1*KD4G6VVmbuq-w_6088Vl8Q.png)

Now, let’s use the future\_df to score and generate predictions.

```
predictions_future = predict_model(final_best, data=future_df)
predictions_future.head()
```

![Sample rows from predictions\_future](https://cdn-images-1.medium.com/max/2000/1*5mqx2Qi2En2VPq9zNZG87g.png)

Let’s plot it.

```
concat_df = pd.concat([data,predictions_future], axis=0)
concat_df_i = pd.date_range(start='1949-01-01', end = '1965-01-01', freq = 'MS')
concat_df.set_index(concat_df_i, inplace=True)

fig = px.line(concat_df, x=concat_df.index, y=["Passengers", "Label"], template = 'plotly_dark')
fig.show()
```

![Actual (1949–1960) and Predicted (1961–1964) US airline passengers](https://cdn-images-1.medium.com/max/2614/1*IjglwJEeU2hZMsjxM8yPbg.png)

Wasn’t that easy?

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Topic Modeling in Power BI using PyCaret

### Topic Modeling in Power BI using PyCaret

#### by Moez Ali

![NLP Dashboard in Power BI](https://cdn-images-1.medium.com/max/2624/1*SyZczsDz5Pf-4Srfj_p8vQ.png)

In our [last post](https://towardsdatascience.com/how-to-implement-clustering-in-power-bi-using-pycaret-4b5e34b1405b), we demonstrated how to implement clustering analysis in Power BI by integrating it with PyCaret, thus allowing analysts and data scientists to add a layer of machine learning to their reports and dashboards without any additional license costs.

In this post, we will see how we can implement topic modeling in Power BI using PyCaret. If you haven’t heard about PyCaret before, please read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

### Learning Goals of this Tutorial

* What is Natural Language Processing?
* What is Topic Modeling?
* Train and implement a Latent Dirichlet Allocation model in Power BI.
* Analyze results and visualize information in a dashboard.

### Before we start

If you have used Python before, it is likely that you already have Anaconda Distribution installed on your computer. If not, [click here](https://www.anaconda.com/distribution/) to download Anaconda Distribution with Python 3.7 or greater.

![https://www.anaconda.com/products/individual](https://cdn-images-1.medium.com/max/2612/1*sMceDxpwFVHDtdFi528jEg.png)

### Setting up the Environment

Before we start using PyCaret’s machine learning capabilities in Power BI we have to create a virtual environment and install pycaret. It’s a four-step process:

[✅](https://fsymbols.com/signs/tick/) **Step 1 — Create an anaconda environment**

Open \*\*Anaconda Prompt \*\*from start menu and execute the following code:

```
conda create --name **powerbi **python=3.7
```

*“powerbi” is the name of environment we have chosen. You can keep whatever name you would like.*

[✅](https://fsymbols.com/signs/tick/) **Step 2 — Install PyCaret**

Execute the following code in Anaconda Prompt:

```
pip install **pycaret**
```

Installation may take 15–20 minutes. If you are having issues with installation, please see our [GitHub](https://www.github.com/pycaret/pycaret) page for known issues and resolutions.

[✅](https://fsymbols.com/signs/tick/)**Step 3 — Set Python Directory in Power BI**

The virtual environment created must be linked with Power BI. This can be done using Global Settings in Power BI Desktop (File → Options → Global → Python scripting). Anaconda Environment by default is installed under:

C:\Users\***username**\*\Anaconda3\envs\\

![File → Options → Global → Python scripting](https://cdn-images-1.medium.com/max/2000/1*3qTuOM-N6ekhoiQmDpHgXg.png)

[✅](https://fsymbols.com/signs/tick/)**Step 4 — Install Language Model**

In order to perform NLP tasks you must download language model by executing following code in your Anaconda Prompt.

First activate your conda environment in Anaconda Prompt:

```
conda activate **powerbi**
```

Download English Language Model:

```
python -m spacy download en_core_web_sm
python -m textblob.download_corpora
```

![python -m spacy download en\_core\_web\_sm](https://cdn-images-1.medium.com/max/3840/1*savPqt23x7nBcK76-0MBxw.png)

![python -m textblob.download\_corpora](https://cdn-images-1.medium.com/max/3838/1*NYaSehQvRp9ANsEpC_GPQw.png)

### What is Natural Language Processing?

Natural language processing (NLP) is a subfield of computer science and artificial intelligence that is concerned with the interactions between computers and human languages. In particular, NLP covers broad range of techniques on how to program computers to process and analyze large amounts of natural language data.

NLP-powered software helps us in our daily lives in various ways and it is likely that you have been using it without even knowing. Some examples are:

* **Personal assistants**: Siri, Cortana, Alexa.
* **Auto-complete**: In search engines (*e.g:* Google, Bing, Baidu, Yahoo).
* **Spell checking**: Almost everywhere, in your browser, your IDE (*e.g:* Visual Studio), desktop apps (*e.g:* Microsoft Word).
* **Machine Translation**: Google Translate.
* \*\*Document Summarization Software: \*\*Text compactor, Autosummarizer.

![Source: https://clevertap.com/blog/natural-language-processing](https://cdn-images-1.medium.com/max/2800/1*IEuGZY5vaWoVnTqQpoZUvQ.jpeg)

Topic Modeling is a type of statistical model used for discovering abstract topics in text data. It is one of many practical applications within NLP.

### What is Topic Modeling?

A topic model is a type of statistical model that falls under unsupervised machine learning and is used for discovering abstract topics in text data. The goal of topic modeling is to automatically find the topics / themes in a set of documents.

Some common use-cases for topic modeling are:

* **Summarizing** large text data by classifying documents into topics (*the idea is pretty similar to clustering*).
* \*\*Exploratory Data Analysis \*\*to gain understanding of data such as customer feedback forms, amazon reviews, survey results etc.
* \*\*Feature Engineering \*\*creating features for supervised machine learning experiments such as classification or regression

There are several algorithms used for topic modeling. Some common ones are Latent Dirichlet Allocation (LDA), Latent Semantic Analysis (LSA), and Non-Negative Matrix Factorization (NMF). Each algorithm has its own mathematical details which will not be covered in this tutorial. We will implement a Latent Dirichlet Allocation (LDA) model in Power BI using PyCaret’s NLP module.

If you are interested in learning the technical details of the LDA algorithm, you can read [this paper](http://www.jmlr.org/papers/volume3/blei03a/blei03a.pdf).

![Source : https://springerplus.springeropen.com/articles/10.1186/s40064-016-3252-8](https://cdn-images-1.medium.com/max/2000/1*DYbV9YMI94QsUeRiiJyrSg.png)

### **Text preprocessing for Topic Modeling**

In order to get meaningful results from topic modeling text data must be processed before feeding it to the algorithm. This is common with almost all NLP tasks. The preprocessing of text is different from the classical preprocessing techniques often used in machine learning when dealing with structured data (data in rows and columns).

PyCaret automatically preprocess text data by applying over 15 techniques such as **stop word removal**, **tokenization**, **lemmatization**, **bi-gram/tri-gram extraction etc**. If you would like to learn more about all the text preprocessing features available in PyCaret, [click here](https://www.pycaret.org/nlp).

### Setting the Business Context

Kiva is an international non-profit founded in 2005 in San Francisco. Its mission is to expand financial access to underserved communities in order to help them thrive.

![Source: https://www.kiva.org/about](https://cdn-images-1.medium.com/max/2124/1*U4zzTYo6MoCk6PxuZl3FBw.png)

In this tutorial we will use the open dataset from Kiva which contains loan information on 6,818 approved loan applicants. The dataset includes information such as loan amount, country, gender and some text data which is the application submitted by the borrower.

![Sample Data points](https://cdn-images-1.medium.com/max/3194/1*jnQvTmQHhWpOSAgSMqaspg.png)

Our objective is to analyze the text data in the ‘*en*’ column to find abstract topics and then use them to evaluate the effect of certain topics (or certain types of loans) on the default rate.

### 👉 Let’s get started

Now that you have set up the Anaconda Environment, understand topic modeling and have the business context for this tutorial, let’s get started.

### 1. Get Data

The first step is importing the dataset into Power BI Desktop. You can load the data using a web connector. (Power BI Desktop → Get Data → From Web).

![Power BI Desktop → Get Data → Other → Web](https://cdn-images-1.medium.com/max/3828/1*lGqJEUm2lVDcYNDdGNUfbw.png)

Link to csv file: <https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/kiva.csv>

### 2. Model Training

To train a topic model in Power BI we will have to execute a Python script in Power Query Editor (Power Query Editor → Transform → Run python script). Run the following code as a Python script:

```
from **pycaret.nlp **import *
dataset = **get_topics**(dataset, text='en')
```

![Power Query Editor (Transform → Run python script)](https://cdn-images-1.medium.com/max/2000/1*EwC-QI4m6DORCtdakOAPmQ.png)

There are 5 ready-to-use topic models available in PyCaret.

![](https://cdn-images-1.medium.com/max/2000/1*LszI1w45K6i5pOBJ0ZmndA.png)

By default, PyCaret trains a \*\*Latent Dirichlet Allocation (LDA) \*\*model with 4 topics. Default values can be changed easily:

* To change the model type use the \*\*\*model \*\*\*parameter within **get\_topics()**.
* To change the number of topics, use the \*\*\*num\_topics \*\*\*parameter.

See the example code for a **Non-Negative Matrix Factorization** model with 6 topics.

```
from **pycaret.nlp **import *
dataset = **get_topics**(dataset, text='en', model='nmf', num_topics=6)
```

**Output:**

![Topic Modeling Results (after execution of Python code)](https://cdn-images-1.medium.com/max/3834/1*DY70gtEWPMy5BPiuKwWPPA.png)

![Final Output (after clicking on Table)](https://cdn-images-1.medium.com/max/3840/1*lbTGdPoqZQkYejsl01D4dQ.png)

New columns containing topic weights are attached to the original dataset. Here’s how the final output looks like in Power BI once you apply the query.

![Results in Power BI Desktop (after applying query)](https://cdn-images-1.medium.com/max/3844/1*btTSFxgmmEV8e7-Nw133mw.png)

### 3. Dashboard

Once you have topic weights in Power BI, here’s an example of how you can visualize it in dashboard to generate insights:

![Summary page of Dashboard](https://cdn-images-1.medium.com/max/2624/1*SyZczsDz5Pf-4Srfj_p8vQ.png)

![Details page of Dashboard](https://cdn-images-1.medium.com/max/2660/1*SVY-1iq0qXmh_Dl8D3rl0w.png)

You can download the PBIX file and the data set from our [GitHub](https://github.com/pycaret/powerbi-nlp).

If you would like to learn more about implementing Topic Modeling in Jupyter notebook using PyCaret, watch this 2 minute video tutorial:

If you are Interested in learning more about Topic Modeling, you can also checkout our NLP 101 [Notebook Tutorial](https://www.pycaret.org/nlp101) for beginners.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Important Links

[User Guide / Documentation](https://www.pycaret.org/guide) [GitHub Repository ](https://www.github.com/pycaret/pycaret)[Install PyCaret](https://www.pycaret.org/install) [Notebook Tutorials](https://www.pycaret.org/tutorial) [Contribute in PyCaret](https://www.pycaret.org/contribute)

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium : [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn : <https://www.linkedin.com/in/profile-moez/>

Twitter : <https://twitter.com/moezpycaretorg1>


# Write and train custom ML models using PyCaret

### Write and train your own custom machine learning models using PyCaret

#### A step-by-step, beginner-friendly tutorial on how to write and train custom machine learning models in PyCaret

![Photo by Rob Lambert on Unsplash](https://cdn-images-1.medium.com/max/10368/0*dERI0tdhD_Yay4OU)

### PyCaret

PyCaret is an open-source, low-code machine learning library and end-to-end model management tool built-in Python for automating machine learning workflows. It is incredibly popular for its ease of use, simplicity, and ability to quickly and efficiently build and deploy end-to-end ML prototypes.

PyCaret is an alternate low-code library that can replace hundreds of code lines with few lines only. This makes the experiment cycle exponentially fast and efficient.

PyCaret is **simple and** **easy to use**. All the operations performed in PyCaret are sequentially stored in a **Pipeline** that is fully automated for \*\*deployment. \*\*Whether it’s imputing missing values, one-hot-encoding, transforming categorical data, feature engineering, or even hyperparameter tuning, PyCaret automates all of it.

This tutorial assumes that you have some prior knowledge and experience with PyCaret. If you haven’t used it before, no problem — you can get a quick headstart through these tutorials:

* [PyCaret 2.2 is here — what’s new](https://towardsdatascience.com/pycaret-2-2-is-here-whats-new-ad7612ca63b)
* [Announcing PyCaret 2.0](https://towardsdatascience.com/announcing-pycaret-2-0-39c11014540e)
* [Five things you don’t know about PyCaret](https://towardsdatascience.com/5-things-you-dont-know-about-pycaret-528db0436eec)

### Installing PyCaret

Installing PyCaret is very easy and takes only a few minutes. We strongly recommend using a virtual environment to avoid potential conflicts with other libraries.

PyCaret’s default installation is a slim version of pycaret that only installs hard dependencies [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).

```
**# install slim version (default)
**pip install pycaret

**# install the full version**
pip install pycaret[full]
```

When you install the full version of pycaret, all the optional dependencies as [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-optional.txt) are also installed.

### 👉 Let’s get started

Before we start talking about custom model training, let’s see a quick demo of how PyCaret works with out-of-the-box models. I will be using the ‘insurance’ dataset available on [PyCaret’s Repository](https://github.com/pycaret/pycaret/tree/master/datasets). The goal of this dataset is to predict patient charges based on some attributes.

### 👉 **Dataset**

```
**# read data from pycaret repo
**from pycaret.datasets import get_data
data = get_data('insurance')
```

![Sample rows from insurance dataset](https://cdn-images-1.medium.com/max/2000/1*h4UQIEtUUmsP2ybJlsFKPA.png)

### 👉 **Data Preparation**

Common to all modules in PyCaret, the setup is the first and the only mandatory step in any machine learning experiment performed in PyCaret. This function takes care of all the data preparation required before training models. Besides performing some basic default processing tasks, PyCaret also offers a wide array of pre-processing features. To learn more about all the preprocessing functionalities in PyCaret, you can see this [link](https://pycaret.org/preprocessing/).

```
**# initialize setup
**from pycaret.regression import *
s = setup(data, target = 'charges')
```

![setup function in pycaret.regression module](https://cdn-images-1.medium.com/max/2736/1*s5bhY1IN1jOM11JDuwFaZw.png)

Whenever you initialize the setup function in PyCaret, it profiles the dataset and infers the data types for all input features. If all data types are correctly inferred, you can press enter to continue.

![Output from setup — truncated for display](https://cdn-images-1.medium.com/max/2000/1*Y9kIg0BfRfzG1WdZm6MnbQ.png)

### 👉 Available Models

To check the list of all models available for training, you can use the function called models . It displays a table with model ID, name, and the reference of the actual estimator.

```
**# check all the available models
**models()
```

![Output from models() — Output truncated for display purpose](https://cdn-images-1.medium.com/max/2000/1*JVVVA2aUyVBJ9SyQjEC13A.png)

### 👉 Model Training & Selection

The most used function for training any model in PyCaret is create\_model . It takes an ID for the estimator you want to train.

```
**# train decision tree
**dt = create_model('dt')
```

![Output from create\_model(‘dt’)](https://cdn-images-1.medium.com/max/2000/1*-txdluhP3Jl27ZUvoMzdow.png)

The output shows the 10-fold cross-validated metrics with mean and standard deviation. The output from this function is a trained model object, which is essentially a scikit-learn object.

```
print(dt)
```

![Output from print(dt)](https://cdn-images-1.medium.com/max/2000/1*7z-sMZdcNVamc1U-PFzVXg.png)

To train multiple models in a loop, you can write a simple list comprehension:

```
**# train multiple models**
multiple_models = [create_model(i) for i in ['dt', 'lr', 'xgboost']]

**# check multiple_models
**type(multiple_models), len(multiple_models)
>>> (list, 3)

print(multiple_models)
```

![Output from print(multiple\_models)](https://cdn-images-1.medium.com/max/2734/1*OO_I-wbH7h4PseoHOQ36Vg.png)

If you want to train all the models available in the library instead of the few selected you can use PyCaret’s compare\_models function instead of writing your own loop (*the results will be the same though*).

```
**# compare all models**
best_model = compare_models()
```

![Output from the compare\_models function](https://cdn-images-1.medium.com/max/2000/1*9XtwGLvLDmJ5ro2fq67HLQ.png)

compare\_models returns the output which shows the cross-validated metrics for all models. According to this output, Gradient Boosting Regressor is the best model with $2,702 in Mean Absolute Error \*\*\*\*(MAE) \*\*\*\*using 10-fold cross-validation on the train set.

```
**# check the best model**
print(best_model)
```

![Output from the print(best\_model)](https://cdn-images-1.medium.com/max/2000/1*pQSXoclIKREi-2U2uG3jhQ.png)

The metrics shown in the above grid is cross-validation scores, to check the score of the best\_modelon hold-out set:

```
**# predict on hold-out
**pred_holdout = predict_model(best_model)
```

![Output from the predict\_model(best\_model) function](https://cdn-images-1.medium.com/max/2000/1*G1l1bG1f_Tzoeo7X_ieixw.png)

To generate predictions on the unseen dataset you can use the same predict\_model function but just pass an extra parameter data :

```
**# create copy of data drop target column**
data2 = data.copy()
data2.drop('charges', axis=1, inplace=True)

**# generate predictions
**predictions = predict_model(best_model, data = data2)
```

![Output from predict\_model(best\_model, data = data2)](https://cdn-images-1.medium.com/max/2000/1*jch_dJNscn_i2vNfgWpV5g.png)

### 👉 Writing and Training Custom Model

So far what we have seen is training and model selection for all the available models in PyCaret. However, the way PyCaret works for custom models is exactly the same. As long as, your estimator is compatible with sklearn API style, it will work the same way. Let’s see few examples.

Before I show you how to write your own custom class, I will first demonstrate how you can work with custom non-sklearn models (models that are not available in sklearn or pycaret’s base library).

#### 👉 **GPLearn Models**

While Genetic Programming (GP) can be used to perform a [very wide variety of tasks](http://www.genetic-programming.org/combined.php), gplearn is purposefully constrained to solving symbolic regression problems.

Symbolic regression is a machine learning technique that aims to identify an underlying mathematical expression that best describes a relationship. It begins by building a population of naive random formulas to represent a relationship between known independent variables and their dependent variable targets to predict new data. Each successive generation of programs is then evolved from the one that came before it by selecting the fittest individuals from the population to undergo genetic operations.

To use models from gplearn you will have to first install it:

```
**# install gplearn
**pip install gplearn
```

Now you can simply import the untrained model and pass it in the create\_model function:

```
**# import untrained estimator**
from gplearn.genetic import SymbolicRegressor
sc = SymbolicRegressor()

**# train using create_model
**sc_trained = create_model(sc)
```

![Output from create\_model(sc\_trained)](https://cdn-images-1.medium.com/max/2000/1*WjHjXcM_Q4w7zuM_nfzVng.png)

```
print(sc_trained)
```

![Output from print(sc\_trained)](https://cdn-images-1.medium.com/max/2000/1*1glIGPLohn6bxElYSmgtuQ.png)

You can also check the hold-out score for this:

```
**# check hold-out score
**pred_holdout_sc = predict_model(sc_trained)
```

![Output from predict\_model(sc\_trained)](https://cdn-images-1.medium.com/max/2000/1*EoTHf4G1wm8Zh0xqScS_Gg.png)

#### 👉 NGBoost Models

ngboost is a Python library that implements Natural Gradient Boosting, as described in [“NGBoost: Natural Gradient Boosting for Probabilistic Prediction”](https://stanfordmlgroup.github.io/projects/ngboost/). It is built on top of [Scikit-Learn](https://scikit-learn.org/stable/) and is designed to be scalable and modular with respect to the choice of proper scoring rule, distribution, and base learner. A didactic introduction to the methodology underlying NGBoost is available in this [slide deck](https://drive.google.com/file/d/183BWFAdFms81MKy6hSku8qI97OwS_JH_/view?usp=sharing).

To use models from ngboost, you will have to first install ngboost:

```
**# install ngboost**
pip install ngboost
```

Once installed, you can import the untrained estimator from the ngboost library and use create\_model to train and evaluate the model:

```
**# import untrained estimator**
from ngboost import NGBRegressor
ng = NGBRegressor()

**# train using create_model
**ng_trained = create_model(ng)
```

![Output from create\_model(ng)](https://cdn-images-1.medium.com/max/2000/1*6GjuFIPOBN4f19Qj7YPMlw.png)

```
print(ng_trained)
```

![Output from print(ng\_trained)](https://cdn-images-1.medium.com/max/2000/1*SSZoHUK4NnLE2Ri_Uy985Q.png)

#### 👉 Writing Custom Class

The above two examples gplearn and ngboost are custom models for pycaret as they are not available in the default library but you can use them just like you can use any other out-of-the-box models. However, there may be a use-case that involves writing your own algorithm (i.e. maths behind the algorithm), in which case you can inherit the base class from sklearn and write your own maths.

Let’s create a naive estimator which learns the mean value of target variable during fit stage and predicts the same mean value for all new data points, irrespective of X input (*probably not useful in real life, but just to make demonstrate the functionality*).

```
**# create custom estimator**
import numpy as np**
**from sklearn.base import BaseEstimator

class MyOwnModel(BaseEstimator):
    
    def __init__(self):
        self.mean = 0
        
    def fit(self, X, y):
        self.mean = y.mean()
        return self
    
    def predict(self, X):
        return np.array(X.shape[0]*[self.mean])
```

Now let’s use this estimator for training:

```
**# import MyOwnModel class**
mom = MyOwnModel()

**# train using create_model
**mom_trained = create_model(mom)
```

![Output from create\_model(mom)](https://cdn-images-1.medium.com/max/2000/1*ElBm8PRRTYgkCQ7J6tsf_g.png)

```
**# generate predictions on data**
predictions = predict_model(mom_trained, data=data)
```

![Output from predict\_model(mom, data=data)](https://cdn-images-1.medium.com/max/2000/1*SE8aSw-Rhj41PYzRQxHWQw.png)

Notice that Label column which is essentially the prediction is the same number $13,225 for all the rows, that’s because we created this algorithm in such a way, that learns from the mean of train set and predict the same value (just to keep things simple).

I hope that you will appreciate the ease of use and simplicity in PyCaret. In just a few lines, you can perform end-to-end machine learning experiments and write your own algorithms without adjusting any native code.

### Coming Soon!

Next week I will be writing a tutorial to advance this tutorial. We will write a more complex algorithm instead of just a mean prediction. I will introduce some complex concepts in the next tutorial. Please follow me on [Medium](https://medium.com/@moez-62905), [LinkedIn](https://www.linkedin.com/in/profile-moez/), and [Twitter](https://twitter.com/moezpycaretorg1) to get more updates.

There is no limit to what you can achieve using this lightweight workflow automation library in Python. If you find this useful, please do not forget to give us ⭐️ on our GitHub repository.

To hear more about PyCaret follow us on [LinkedIn](https://www.linkedin.com/company/pycaret/) and [Youtube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g).

Join us on our slack channel. Invite link [here](https://join.slack.com/t/pycaret/shared_invite/zt-p7aaexnl-EqdTfZ9U~mF0CwNcltffHg).

### You may also be interested in:

[Build your own AutoML in Power BI using PyCaret 2.0](https://towardsdatascience.com/build-your-own-automl-in-power-bi-using-pycaret-8291b64181d) [Deploy Machine Learning Pipeline on Azure using Docker](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01) [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b) [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) [Build and deploy your first machine learning web app](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99) [Deploy PyCaret and Streamlit app using AWS Fargate serverless](https://towardsdatascience.com/deploy-pycaret-and-streamlit-app-using-aws-fargate-serverless-infrastructure-8b7d7c0584c2) [Build and deploy machine learning web app using PyCaret and Streamlit](https://towardsdatascience.com/build-and-deploy-machine-learning-web-app-using-pycaret-and-streamlit-28883a569104) [Deploy Machine Learning App built using Streamlit and PyCaret on GKE](https://towardsdatascience.com/deploy-machine-learning-app-built-using-streamlit-and-pycaret-on-google-kubernetes-engine-fd7e393d99cb)

### Important Links

[Documentation](https://pycaret.readthedocs.io/en/latest/installation.html) [Blog](https://medium.com/@moez_62905) [GitHub](http://www.github.com/pycaret/pycaret) [StackOverflow](https://stackoverflow.com/questions/tagged/pycaret) [Install PyCaret ](https://pycaret.readthedocs.io/en/latest/installation.html)[Notebook Tutorials ](https://pycaret.readthedocs.io/en/latest/tutorials.html)[Contribute in PyCaret](https://pycaret.readthedocs.io/en/latest/contribute.html)

### Want to learn about a specific module?

Click on the links below to see the documentation and working examples.

[Classification ](https://pycaret.readthedocs.io/en/latest/api/classification.html)[Regression](https://pycaret.readthedocs.io/en/latest/api/regression.html) [Clustering](https://pycaret.readthedocs.io/en/latest/api/clustering.html) [Anomaly Detection](https://pycaret.readthedocs.io/en/latest/api/anomaly.html) [Natural Language Processing ](https://pycaret.readthedocs.io/en/latest/api/nlp.html)[Association Rule Mining](https://pycaret.readthedocs.io/en/latest/api/arules.html)


# Build and deploy ML app with PyCaret and Streamlit

### Build and deploy machine learning web app using PyCaret and Streamlit

#### A beginner’s guide to deploying a machine learning app on Heroku PaaS

#### by Moez Ali

![](https://cdn-images-1.medium.com/max/2000/1*HuGxT33q9tj7FQikC3EB_Q.png)

### RECAP

In our [last post](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507) on deploying a machine learning pipeline in the cloud, we demonstrated how to develop a machine learning pipeline in PyCaret, containerize Flask app with Docker and deploy serverless using AWS Fargate. If you haven’t heard about PyCaret before, you can read this [announcement](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more.

In this tutorial, we will train a machine learning pipeline using PyCaret and create a web app using a [Streamlit](https://www.streamlit.io/) open-source framework. This web app will be a simple interface for business users to generate predictions on a new dataset using a trained machine learning pipeline.

By the end of this tutorial, you will be able to build a fully functional web app to generate online predictions (one-by-one) and predictions by batch (by uploading a csv file) using trained machine learning model. The final app looks like this:

![https://pycaret-streamlit.herokuapp.com](https://cdn-images-1.medium.com/max/3826/1*-scVDUhBbOIWievCj0DYjw.png)

### 👉 What you will learn in this tutorial

* What is a deployment and why do we deploy machine learning models?
* Develop a machine learning pipeline and train models using PyCaret.
* Build a simple web app using a Streamlit open-source framework.
* Deploy a web app on ‘Heroku’ and see the model in action.

This tutorial will cover the entire workflow starting from training a machine learning model and developing a pipeline in Python, developing a simple web app using streamlit and deploying the app on the Heroku cloud platform.

In the past, we have covered containerization using docker and deployment on cloud platforms like Azure, GCP and AWS. If you are interested in learning more about those, you can read the following stories:

* [Deploy Machine Learning Pipeline on AWS Fargate](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507)
* [Deploy Machine Learning Pipeline on Google Kubernetes Engine](https://towardsdatascience.com/deploy-machine-learning-model-on-google-kubernetes-engine-94daac85108b)
* [Deploy Machine Learning Pipeline on AWS Web Service](https://towardsdatascience.com/deploy-machine-learning-pipeline-on-cloud-using-docker-container-bec64458dc01)
* [Build and deploy your first machine learning web app on Heroku PaaS](https://towardsdatascience.com/build-and-deploy-your-first-machine-learning-web-app-e020db344a99)

### 💻 Toolbox for this tutorial

### PyCaret

[PyCaret](https://www.pycaret.org/) is an open source, low-code machine learning library in Python that is used to train and deploy machine learning pipelines and models into production. PyCaret can be installed easily using pip.

```
pip install **pycaret**
```

### Streamlit

[Streamlit](https://www.streamlit.io/) is an open-source Python library that makes it easy to build beautiful custom web-apps for machine learning and data science. Streamlit can be installed easily using pip.

```
pip install **streamlit**
```

### GitHub

[GitHub](https://www.github.com/) is a cloud-based service that is used to host, manage and control code. Imagine you are working in a large team where multiple people (sometimes hundreds of them) are making changes. PyCaret is itself an example of an open-source project where hundreds of community developers are continuously contributing to source code. If you haven’t used GitHub before, you can [sign up](https://github.com/join) for a free account.

### Heroku

[Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables the deployment of web apps based on a managed container system, with integrated data services and a powerful ecosystem. In simple words, this will allow you to take the application from your local machine to the cloud so that anybody can access it using a Web URL. In this tutorial, we have chosen Heroku for deployment as it provides free resource hours when you [sign up](https://signup.heroku.com/) for a new account.

![Machine Learning Workflow (from Training to Deployment on PaaS)](https://cdn-images-1.medium.com/max/2000/1*XTizEjPOR4UKJphNsjbhBw.png)

### ✔️Let’s get started…..

### Why Deploy Machine Learning Models?

Deployment of machine learning models is the process of putting models into production so that web applications, enterprise software and APIs can consume a trained model and generate predictions with new data points.

Normally machine learning models are built so that they can be used to predict an outcome (binary value i.e. 1 or 0 for [Classification](https://www.pycaret.org/classification), continuous values for [Regression](https://www.pycaret.org/regression), labels for [Clustering](https://www.pycaret.org/clustering) etc. There are two broad ways to predict new data points:

### 👉 **Online Predictions**

Online prediction scenarios are for cases where you want to generate predictions on a one-by-one basis for each datapoint. For example, you could use predictions to make immediate decisions about whether a particular transaction is likely to be fraudulent.

### 👉 **Batch Predictions**

Batch prediction is useful when you want to generate predictions for a set of observations all at once. For example, if you want to decide which customers to target as part of an advertisement campaign for a product you would get prediction scores for all customers, sort these to identify which customers are most likely to purchase, and then target maybe the top 5% customers that are most likely to purchase.

> ## In this tutorial we will build an app that can do both; online prediction as well as batch prediction by uploading a csv file containing new data points.

### Setting the Business Context

An insurance company wants to improve its cash flow forecasting by better predicting patient charges using demographic and basic patient health risk metrics at the time of hospitalization.

![](https://cdn-images-1.medium.com/max/2000/1*qM1HiWZ_uigwdcZ0_ZL6yA.png)

*(*[*data source*](https://www.kaggle.com/mirichoi0218/insurance#insurance.csv)*)*

### Objective

To build a web application that supports online (one-by-one) as well as batch prediction using trained machine learning model and pipeline.

### Tasks

* Train, validate and develop a machine learning pipeline using PyCaret.
* Build a front-end web application with two functionalities: (i) online prediction and (ii) batch prediction.
* Deploy the web app on Heroku. Once deployed, it will become publicly available and can be accessed via Web URL.

### 👉 Task 1 — Model Training and Validation

Training and model validation are performed in an Integrated Development Environment (IDE) or Notebook either on your local machine or on cloud. If you haven’t used PyCaret before, [click here](https://towardsdatascience.com/announcing-pycaret-an-open-source-low-code-machine-learning-library-in-python-4a1f1aad8d46) to learn more about PyCaret or see [Getting Started Tutorials](https://www.pycaret.org/tutorial) on our [website](https://www.pycaret.org/).

In this tutorial, we have performed two experiments. The first experiment is performed with default preprocessing settings in PyCaret. The second experiment has some additional preprocessing tasks such as **scaling and normalization, automatic feature engineering and binning continuous data into intervals**. See the setup code for the second experiment:

```
**# Experiment No. 2**

from **pycaret.regression** import *****

r2 = **setup**(data, target = 'charges', session_id = 123,
           normalize = True,
           polynomial_features = True, trigonometry_features = True,
           feature_interaction=True, 
           bin_numeric_features= ['age', 'bmi'])
```

![Comparison of information grid for both experiments](https://cdn-images-1.medium.com/max/2000/1*TeqcOM-jBpkdeQu84c4Onw.png)

The magic happens with only a few lines of code. Notice that in **Experiment 2** the transformed dataset has 62 features for training derived from only 6 features in the original dataset. All of the new features are the result of transformations and automatic feature engineering in PyCaret.

![Columns in dataset after transformation](https://cdn-images-1.medium.com/max/2000/1*ju5RFYKGkAVEOvVjeoM5nQ.png)

Sample code for model training in PyCaret:

```
# Model Training and Validation 
lr = **create_model**('lr')
```

![10 Fold cross-validation of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2276/1*TX-IzWHBekZBRSQi2T_JTQ.png)

Notice the impact of transformations and automatic feature engineering. The R2 has increased by 10% with very little effort. We can compare the **residual plot** of linear regression model for both experiments and observe the impact of transformations and feature engineering on the \*\*heteroskedasticity \*\*of model.

```
# plot residuals of trained model**
plot_model**(lr, plot = 'residuals')
```

![Residual Plot of Linear Regression Model(s)](https://cdn-images-1.medium.com/max/2876/1*LxVMcK4hNvBvEj1tyqxfWQ.png)

Machine learning is an iterative process. The number of iterations and techniques used within are dependent on how critical the task is and what the impact will be if predictions are wrong. The severity and impact of a machine learning model to predict a patient outcome in real-time in the ICU of a hospital is far more than a model built to predict customer churn.

In this tutorial, we have performed only two iterations and the linear regression model from the second experiment will be used for deployment. At this stage, however, the model is still only an object within a Notebook / IDE. To save it as a file that can be transferred to and consumed by other applications, execute the following code:

```
# save transformation pipeline and model 
**save_model**(lr, model_name = 'deployment_28042020')
```

When you save a model in PyCaret, the entire transformation pipeline based on the configuration defined in the \*\*setup() \*\*function is created. All inter-dependencies are orchestrated automatically. See the pipeline and model stored in the ‘deployment\_28042020’ variable:

![Pipeline created using PyCaret](https://cdn-images-1.medium.com/max/2000/1*NWoHVWJzO7i7gIvrlBnIiQ.png)

We have finished training and model selection. The final machine learning pipeline and linear regression model is now saved as a pickle file (deployment\_28042020.pkl) that will be used in a web application to generate predictions on new datapoints.

### 👉 Task 2 — Building Web Application

Now that our machine learning pipeline and model are ready we will start building a front-end web application that can generate predictions on new datapoints. This application will support ‘Online’ as well as ‘Batch’ predictions through a csv file upload. Let’s breakdown the application code into three main parts:

### **Header / Layout**

This section imports libraries, loads the trained model and creates a basic layout with a logo on top, a jpg image and a dropdown menu on the sidebar to toggle between ‘Online’ and ‘Batch’ prediction.

![app.py — code snippet part 1](https://cdn-images-1.medium.com/max/2268/1*xAnCZ1N_BNoPW7FoA-NXrA.png)

### **Online Predictions**

This section deals with the first functionality of the app i.e. Online (one-by-one) prediction. We are using streamlit widgets such as *number input, text input, drop down menu and checkbox* to collect the datapoints used to train the model such as Age, Sex, BMI, Children, Smoker, Region.

![app.py — code snippet part 2](https://cdn-images-1.medium.com/max/2408/1*eFeq1wINsUUnvLJfuL-GOA.png)

### **Batch Predictions**

This part deals with the second functionality i.e. prediction by batch. We have used the **file\_uploader** widget of streamlit to upload a csv file and then called the native \*\*predict\_model() \*\*function from PyCaret to generate predictions that are displayed used streamlit’s write() function.

![app.py — code snippet part 3](https://cdn-images-1.medium.com/max/2410/1*u-g2iLy_gV7hom71PM3CEA.png)

If you remember from Task 1 above we finalized a linear regression model that was trained on 62 features that were extracted using 6 original features. However, the front-end of our web application has an input form that collects only the six features i.e. age, sex, bmi, children, smoker, region.

How do we transform the 6 features of a new data point into 62 used to train the model? We do not need to worry about this part as PyCaret automatically handles this by orchestrating the transformation pipeline. When you call the predict function on a model trained using PyCaret, all transformations are applied automatically (in sequence) before generating predictions from the trained model.

\*\*Testing App \*\*One final step before we publish the application on Heroku is to test the web app locally. Open Anaconda Prompt and navigate to your project folder and execute the following code:

```
**streamlit **run app.py
```

![Streamlit application testing — Online Prediction](https://cdn-images-1.medium.com/max/3832/1*GxVKpxijk0tlqk-bO5Q3JQ.png)

![Streamlit application testing — Batch Prediction](https://cdn-images-1.medium.com/max/3836/1*P5tit2pMf5qiQqU_wjQMVg.png)

### 👉 Task 3 — Deploy the Web App on Heroku

Now that the model is trained, the machine learning pipeline is ready, and the application is tested on our local machine, we are ready to start our deployment on Heroku. There are a couple of ways to upload your application source code onto Heroku. The simplest way is to link a GitHub repository to your Heroku account.

If you would like to follow along you can fork this [repository](https://www.github.com/pycaret/pycaret-deployment-streamlit) from GitHub. If you don’t know how to fork a repo, please [read this](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) official GitHub tutorial.

![https://www.github.com/pycaret/pycaret-deployment-streamlit](https://cdn-images-1.medium.com/max/2260/1*IxxUdaHpWu8qqRxakPzG3g.png)

By now you are familiar with all of the files in the repository except for three files: ‘requirements.txt’ , ‘setup.sh’ and ‘Procfile’. Let’s see what those are:

### requirements.txt

\*\*requirements.txt \*\*file is a text file containing the names of the python packages required to execute the application. If these packages are not installed in the environment where the application is running, it will fail.

![requirements.txt](https://cdn-images-1.medium.com/max/2222/1*BB7NOG_3GI4ue1J_TdtgYQ.png)

### setup.sh

setup.sh is a script programmed for bash. It contains instructions written in the Bash language and like requirements.txt, \*\*it is used for creating the necessary environment for our streamlit app to run on the cloud.

![setup.sh](https://cdn-images-1.medium.com/max/2226/1*Con6kr4kh0Ss_puX7l32_w.png)

### **Procfile**

Procfile is simply one line of code that provides startup instructions to the web server that indicate which file should be executed when an application is triggered. In this example, ‘Procfile’ is used for executing \*\*setup.sh \*\*which will create the necessary environment for the streamlit app and the second part “streamlit run app.py” is to execute the application (this is similar to how you would execute a streamlit application on your local computer).

![Procfile](https://cdn-images-1.medium.com/max/2226/1*b11lGrtlyNHpRcBmY1z4Bg.png)

Once all the files are uploaded onto the GitHub repository, we are now ready to start deployment on Heroku. Follow the steps below:

**Step 1 — Sign up on heroku.com and click on ‘Create new app’**

![Heroku Dashboard](https://cdn-images-1.medium.com/max/3108/1*5tVQzeF-9HZgajee_-2PZg.png)

**Step 2 — Enter App name and region**

![Heroku — Create new app](https://cdn-images-1.medium.com/max/2000/1*yFTEWk8izcuZQFQer96zOQ.png)

**Step 3 — Connect to your GitHub repository**

![Heroku — Connect to GitHub](https://cdn-images-1.medium.com/max/3054/1*wh45-7ZwbcM04OeV6nFgpw.png)

**Step 4 — Deploy branch**

![Heroku — Deploy Branch](https://cdn-images-1.medium.com/max/2990/1*jMrL-8R0-ZWm4WrDObERcw.png)

**Step 5 — Wait 10 minutes and BOOM**

App is published to URL: <https://pycaret-streamlit.herokuapp.com/>

![https://pycaret-streamlit.herokuapp.com/](https://cdn-images-1.medium.com/max/3826/1*-scVDUhBbOIWievCj0DYjw.png)

### PyCaret 2.0.0 is coming!

We have received overwhelming support and feedback from the community. We are actively working on improving PyCaret and preparing for our next release. **PyCaret 2.0.0 will be bigger and better**. If you would like to share your feedback and help us improve further, you may [fill this form](https://www.pycaret.org/feedback) on the website or leave a comment on our [GitHub ](https://www.github.com/pycaret/)or [LinkedIn](https://www.linkedin.com/company/pycaret/) page.

Follow our [LinkedIn](https://www.linkedin.com/company/pycaret/) and subscribe to our [YouTube](https://www.youtube.com/channel/UCxA1YTYJ9BEeo50lxyI_B3g) channel to learn more about PyCaret.

### Want to learn about a specific module?

As of the first release 1.0.0, PyCaret has the following modules available for use. Click on the links below to see the documentation and working examples in Python.

[Classification](https://www.pycaret.org/classification) [Regression ](https://www.pycaret.org/regression)[Clustering](https://www.pycaret.org/clustering) [Anomaly Detection ](https://www.pycaret.org/anomaly-detection)[Natural Language Processing](https://www.pycaret.org/nlp) [Association Rule Mining](https://www.pycaret.org/association-rules)

### Also see:

PyCaret getting started tutorials in Notebook:

[Clustering](https://www.pycaret.org/clu101) [Anomaly Detection](https://www.pycaret.org/anom101) [Natural Language Processing](https://www.pycaret.org/nlp101) [Association Rule Mining](https://www.pycaret.org/arul101) [Regression](https://www.pycaret.org/reg101) [Classification](https://www.pycaret.org/clf101)

### Would you like to contribute?

PyCaret is an open source project. Everybody is welcome to contribute. If you would like to contribute, please feel free to work on [open issues](https://github.com/pycaret/pycaret/issues). Pull requests are accepted with unit tests on dev-1.0.1 branch.

Please give us ⭐️ on our [GitHub repo](https://www.github.com/pycaret/pycaret) if you like PyCaret.

Medium: [https://medium.com/@moez\_62905/](https://medium.com/@moez_62905/machine-learning-in-power-bi-using-pycaret-34307f09394a)

LinkedIn: <https://www.linkedin.com/in/profile-moez/>

Twitter: <https://twitter.com/moezpycaretorg1>


# PyCaret 2.3.6 is Here! Learn What’s New?

PyCaret 2.3.6 is Here! Learn What’s New? From EDA to Deployment to AI Fairness — By far the biggest release of PyCaret

### 🚀 Introduction <a href="#id-261e" id="id-261e"></a>

PyCaret is an open-source, low-code machine learning library in Python that automates machine learning workflows. It is an end-to-end machine learning and model management tool that speeds up the experiment cycle exponentially and makes you more productive.

By far PyCaret 2.3.6 is the biggest release in terms of the new features and functionalities. This article demonstrates the use of new functionalities added in the recent release of [PyCaret 2.3.6](https://pycaret.gitbook.io/docs/get-started/release-notes#pycaret-2.3.6).

### 💻 Installation <a href="#id-90a4" id="id-90a4"></a>

Installation is easy and will only take a few minutes. PyCaret’s default installation from pip only installs hard dependencies as listed in the [requirements.txt](https://github.com/pycaret/pycaret/blob/master/requirements.txt) file.

```
pip install pycaret
```

To install the full version:

```
pip install pycaret[full]
```

### 📈 Dashboard <a href="#id-5b8f" id="id-5b8f"></a>

This function will generate the interactive dashboard for a trained model. The dashboard is implemented using the [ExplainerDashboard](http://explainerdashboard.readthedocs.io/).

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setupfrom pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# generate dashboard
dashboard(lr)
```

![](https://cdn-images-1.medium.com/max/800/1*MlXSTs8BmiICexLfcajJKA.png)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=FZ5-GtdYez0>" %}

### 📊 Exploratory Data Analysis (EDA) <a href="#id-3223" id="id-3223"></a>

This function will generate automated EDA using the [AutoViz](https://github.com/AutoViML/AutoViz) integration.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# generate EDA
eda()
```

![](https://cdn-images-1.medium.com/max/800/1*lByuyZL-pR2eZ0rPc1qsxA.png)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=Pm5VOuYqU4Q>" %}

### 🚊 Convert Model <a href="#id-2e61" id="id-2e61"></a>

This function will transpile trained machine learning models into native inference scripts in different programming languages (Python, C, Java, Go, JavaScript, Visual Basic, C#, PowerShell, R, PHP, Dart, Haskell, Ruby, F#). This functionality is very useful if you want to deploy models into environments where you can’t install your normal Python stack to support model inference.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# convert model
lr_java = convert_model(lr, language = 'java')
print(lr_java)
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FASs2JFGTUbMZtjuhxvPA%2Fimage.png?alt=media\&token=2334e780-7c9f-4c10-b213-29c72b153b64)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=xwQgfNC7808>" %}

### ☑️ Check Fairness <a href="#id-95da" id="id-95da"></a>

There are many approaches to conceptualizing fairness. This new function follows the approach known as [group fairness](https://github.com/fairlearn/fairlearn), which asks: Which groups of individuals are at risk for experiencing harm. This function provides fairness-related metrics between different groups (also called subpopulations).

```
# load dataset
from pycaret.datasets import get_data
data = get_data('income')

# init setup
from pycaret.classification import *
s = setup(data, target = 'income >50K', session_id = 123)

# train model
lr = create_model('lr')

# check fairness
check_fairness(lr, sensitive_features = ['race'])
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F71TtHSyeKNf3YTqhTUT8%2Fimage.png?alt=media\&token=3afe2b1d-a286-43d9-bac5-d1b77d59d415)

**Video Demo:**

{% embed url="<https://youtu.be/mjhDKuLRpM0>" %}

### 📩 Create Web API <a href="#ea0e" id="ea0e"></a>

This function will create a POST API for the ML pipeline for inference using [FastAPI](https://github.com/tiangolo/fastapi) framework. It only creates the API and doesn’t run it automatically.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# create API
create_api(lr, 'my_first_api')

# Run the API
!python my_first_api.py
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FzaXYtm5GmT69Gmod1e0X%2Fimage.png?alt=media\&token=f038bf02-1501-4dc0-88f0-060ae32a3799)

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FlrHG7o4s3XDpnw0YWIxW%2Fimage.png?alt=media\&token=905b4586-dfd2-41e8-a230-6e423ffbc774)

#### **Video Demo:** <a href="#id-4653" id="id-4653"></a>

{% embed url="<https://www.youtube.com/watch?t=1s&v=88M9c5Hc-k0>" %}

### 🚢 Create Docker <a href="#id-4653" id="id-4653"></a>

This function will create a `Dockerfile`and `requirements`file for your API end-point.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# create API
create_api(lr, 'my_first_api')

# create Docker
create_docker('my_first_api')
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FgzP3dd0GGX4YgyaZR02H%2Fimage.png?alt=media\&token=acbde7bc-97d0-4919-b295-b8cc71cdf7af)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=xMgwEJ57uxs>" %}

### 💻 Create Web Application <a href="#id-5897" id="id-5897"></a>

This function creates a basic [Gradio](https://github.com/gradio-app/gradio) web app for inference. It will later be expanded for other app types such as Streamlit.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F1GdZ0hFyOcWUMyuFSJU7%2Fimage.png?alt=media\&token=339a6a57-e96d-4570-adff-aff55ec30ae3)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=4JyYhbW6eCA>" %}

### 🎰 Monitor Drift of ML Models <a href="#b01d" id="b01d"></a>

A new parameter called `drift_report` is added to the `predict_model` function that generates the drift report using [Evidently AI](https://github.com/evidentlyai/evidently?) framework. At the moment this functionality is in experimental mode and will only work on test data. Later on, it will be expanded for production use.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# generate report
preds = predict_model(lr, drift_report = True)
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FGSMGrry9H6CEAO3Ny0It%2Fimage.png?alt=media\&token=1f353997-1758-4dee-b25d-12beb3663977)

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FvmEBEtLJ0RIic123lN0k%2Fimage.png?alt=media\&token=040b5b5d-5683-4dae-93e4-22333c254118)

**Video Demo:**

{% embed url="<https://www.youtube.com/watch?v=C9TNq1bndRI>" %}

### 🔨 Plot Model is now more configurable <a href="#ac70" id="ac70"></a>

`plot_model` function is PyCaret is now more configurable. For example, previously if you wanted to see percentages in Confusion Matrix instead of absolute numbers, it wasn’t possible, or if you want to change the color map of visuals, it wasn’t possible. Now it is possible with the new parameter `plot_kwargs` in the `plot_model` function. See example:

```
# load dataset
from pycaret.datasets import get_data
data = get_data('iris')

# init setup
from pycaret.classification import *
s = setup(data, target = 'species', session_id = 123)

# train model
lr = create_model('lr')

# plot model (without plot kwargs)
plot_model(lr, plot = 'confusion_matrix') 

# plot model (with plot kwargs)
plot_model(lr, plot = 'confusion_matrix', plot_kwargs = {'percent' : True})
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FaJTdSC0cmN0kMDehnNrk%2Fimage.png?alt=media\&token=2951c095-d78c-418d-894f-2e1036a8e95a)

### 🏆Optimize Threshold <a href="#bc52" id="bc52"></a>

This is not a new function but it was completely revamped in 2.3.6. This function is to optimize the probability threshold for binary classification problems. Previously you had to pass cost function as `true_positive` , `false_positive` , `true_negative` , `false_negative` in this function and now it automatically picks up all the metrics including the custom ones from your active experiment run.

```
# load dataset
from pycaret.datasets import get_data
data = get_data('blood')

# init setup
from pycaret.classification import *
s = setup(data, target = 'Class', session_id = 123)

# train model
lr = create_model('lr')

# optimize threshold
optimize_threshold(lr)
```

![](https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FGzWTJA0RuBzODLVwBrs5%2Fimage.png?alt=media\&token=ed9531ba-2798-49a7-a997-672b89c81da7)

### 📚 New Documentation <a href="#c5b7" id="c5b7"></a>

The biggest and hardest of all is the completely new documentation. This is a single source of truth for everything related to PyCaret, from official tutorials to release notes and from API ref to community contributions. Take a video tour:

{% embed url="<https://youtu.be/NpJiD5H0dJc>" %}

Finally, if you want to take the tour of all new functionalities added in 2.3.6, watch this 10 minutes video:

{% embed url="<https://www.youtube.com/watch?t=4s&v=Qr6Hu2t2gwY>" %}

To learn about all the other changes, bug fixes, and minor updates in PyCaret 2.3.6, check out the detailed [release notes](https://github.com/pycaret/pycaret/releases/tag/2.3.6).

Thank you for reading.

### :link: Important Links <a href="#b749" id="b749"></a>

* 📚 [Official Docs:](https://pycaret.gitbook.io/) The bible of PyCaret. Everything is here.
* 🌐 [Official Web:](https://www.pycaret.org/) Check out our official website
* 😺 [GitHub](https://www.github.com/pycaret/pycaret) Check out our Git
* ⭐ [Tutorials](https://pycaret.gitbook.io/docs/get-started/tutorials) New to PyCaret? Check out our official notebooks!
* 📋 [Example Notebooks](https://github.com/pycaret/pycaret/tree/master/examples) created by the community.
* 📙 [Blog](https://pycaret.gitbook.io/docs/learn-pycaret/official-blog) Tutorials and articles by contributors.
* ❓ [FAQs](https://pycaret.gitbook.io/docs/learn-pycaret/faqs) Check out frequently asked questions.
* 📺 [Video Tutorials](https://pycaret.gitbook.io/docs/learn-pycaret/videos) Our video tutorial from various events.
* 📢 [Discussions](https://github.com/pycaret/pycaret/discussions) Have questions? Engage with community and contributors.
* 🛠️ [Changelog](https://pycaret.gitbook.io/docs/get-started/release-notes) Changes and version history.
* 🙌 [User Group](https://www.meetup.com/pycaret-user-group/) Join our Meetup user group.


# Videos

Videos to learn more about PyCaret

### Moez Ali on AutoML at Goto Copenhagen 2022

{% embed url="<https://www.youtube.com/watch?v=nm6vt_olXdg>" %}

### Data Science Summit Poland November 2022

{% embed url="<https://www.youtube.com/watch?v=p-T2M-I5Wt4>" %}

### Deploy PyCaret model within Power BI

{% embed url="<https://www.youtube.com/watch?v=OB_30yKiPFI>" %}

### PyCaret Meet up 5 Feb 2022

{% embed url="<https://www.youtube.com/watch?v=cXrjLveN3IQ>" %}

### PyCaret and Gradio

{% embed url="<https://www.youtube.com/watch?v=4JyYhbW6eCA>" %}

### PyCaret and SageMaker

{% embed url="<https://www.youtube.com/watch?v=wK-Hztot8wc>" %}

### PyCaret and Docker

{% embed url="<https://www.youtube.com/watch?v=xMgwEJ57uxs>" %}

### Check ML Fairness

{% embed url="<https://www.youtube.com/watch?v=mjhDKuLRpM0>" %}

### EDA with PyCaret

{% embed url="<https://www.youtube.com/watch?v=Pm5VOuYqU4Q>" %}

### Transpile ML Models

{% embed url="<https://www.youtube.com/watch?v=xwQgfNC7808>" %}

### PyCaret and Streamlit

{% embed url="<https://www.youtube.com/watch?v=fQthJvYEqx8>" %}

### PyCaret Time Series Module

{% embed url="<https://www.youtube.com/watch?t=2s&v=lHBAHggc4Jg>" %}

### PyCaret and Gradio

{% embed url="<https://www.youtube.com/watch?v=RpOMTdEXFJc>" %}

### Data + AI Summit 2021

{% embed url="<https://www.youtube.com/watch?t=513s&v=yjhBDFBfkcA>" %}

### Deploying ML Pipelines by Moez Ali

{% embed url="<https://www.youtube.com/watch?v=MQCzehNPqes>" %}

### Machine Learning with PyCaret

{% embed url="<https://www.youtube.com/watch?v=Nt1gpaOuCHY>" %}

### PyCaret - talk by Moez Ali

{% embed url="<https://www.youtube.com/watch?t=3496s&v=jlW5kRBwcb0>" %}

### ML + PyCaret with Moez Ali

{% embed url="<https://www.youtube.com/watch?v=QDME8SDT7gc>" %}

### ML made simple by Antoni Baum

{% embed url="<https://www.youtube.com/watch?v=k-8hwQDCwoA>" %}

### PyCaret GUI by APAflow

{% embed url="<https://www.youtube.com/watch?v=1RG4zhjXs-s>" %}

### PyCaret in Power BI

{% embed url="<https://www.youtube.com/watch?v=3qZlF6lFa6o>" %}

### Clustering + PyCaret + Power BI

{% embed url="<https://www.youtube.com/watch?v=ewoA4suoi-U>" %}

### Moez Ali on PyCaret

{% embed url="<https://www.youtube.com/watch?v=iuhx54DrJAM>" %}

### Fraud Detection using PyCaret

{% embed url="<https://www.youtube.com/watch?t=97s&v=Z5pEuBV_lNA>" %}

### Quick Tour of PyCaret

{% embed url="<https://www.youtube.com/watch?t=1s&v=4Rn4YMLUjGc>" %}

### Discussion of PyCaret

{% embed url="<https://www.youtube.com/watch?v=BjcpOVQhNlc>" %}

### Automate  ML Lifecycle with PyCaret

{% embed url="<https://www.youtube.com/watch?v=o2bYvj3yTxg>" %}

### Model selection using PyCaret

{% embed url="<https://www.youtube.com/watch?v=VV1Wn34rdyg>" %}

### Create your first Kaggle Kernel

{% embed url="<https://www.youtube.com/watch?v=nqMM6rngNCA>" %}

### Binary Classification

{% embed url="<https://www.youtube.com/watch?t=2s&v=2xAgLKUN6Xs>" %}

### Clustering Analysis

{% embed url="<https://www.youtube.com/watch?t=2s&v=2oxLDir7foQ>" %}

### Anomaly Detection

{% embed url="<https://www.youtube.com/watch?v=q0dxYDq1A40>" %}

### Topic Modeling

{% embed url="<https://www.youtube.com/watch?t=17s&v=G6ShuoM3T1M>" %}

### Association Rules

{% embed url="<https://www.youtube.com/watch?t=20s&v=XYAGwts5qGw>" %}

### Official Announcement

{% embed url="<https://www.youtube.com/watch?t=1s&v=scd6KS03NiE>" %}

###


# Cheat sheet

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2FRCUHBlhD3BbYmwZNhALL%2Fimage.png?alt=media&#x26;token=b108b535-0328-41c6-9e56-ce2bd5584b2a" alt=""><figcaption><p>Page 1 of 2</p></figcaption></figure>

<figure><img src="https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2Fku9GckINqvjFvwdSY337%2Fimage.png?alt=media&#x26;token=0c81725a-fc16-4b87-a52a-2c06b1e3f16d" alt=""><figcaption><p>Page 2 of 2</p></figcaption></figure>

{% file src="<https://3811348345-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FjAq5m5T7Qtz03TnB0Wve%2Fuploads%2F5awbHjRUaE8w6jEJmL0Z%2FPyCaret%203.0%20cheat_sheet.pdf?alt=media&token=6c642562-0738-42c6-b0ec-fe1171d7d78e>" %}


# FAQs

Frequently Asked Questions!

<details>

<summary>Why PyCaret?</summary>

The short answer is it's an open-source, low-code machine learning library built on top of your favorite libraries and frameworks like *scikit-learn, xgboost, lightgbm, etc.* Machine Learning experments take a lot of iterations and the primary goal of PyCaret is to give you the ability to iterate with lightning speed. In comparison with the other awesome open-source machine learning libraries, PyCaret is an alternate low-code library that can be used to replace hundreds of lines of code with a few lines only. Give it a try!

</details>

<details>

<summary>Does PyCaret work with all OS and Python versions?</summary>

PyCaret is tested and supported on 64-bit systems:

* Python 3.7, 3.8, 3.9, and 3.10
* Ubuntu 16.04 or later
* Windows 7 or later

PyCaret also works on Mac OS but we do not guarantee the performance as the releases are not tested for Mac. To learn more about our testing workflows, [click here](https://github.com/pycaret/pycaret/blob/master/.github/workflows/test.yml).

</details>

<details>

<summary>Can  I use PyCaret on Google Colab or Kaggle Notebooks?</summary>

Absolutely. Just do `pip install pycaret`

</details>

<details>

<summary>Does PyCaret support model training on GPU?</summary>

Yes. We have integrated PyCaret with the amazing [Rapids.AI](https://rapids.ai/) project. To use GPU instead of CPU, just pass `use_gpu=True` in the `setup` function.&#x20;

**This will use CPU for model training:**

{% code lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name')
```

{% endcode %}

**This will use GPU for model training:**

{% code lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name', use_gpu = True)
```

{% endcode %}

There is no change in the use of the API, however, in some cases, additional libraries have to be installed as they are not installed with the default version or the full version of PyCaret. You can learn more about this [here](https://pycaret.gitbook.io/docs/get-started/installation#training-on-gpu).

</details>

<details>

<summary>Can I use PyCaret with parallel processing frameworks like Spark?</summary>

Absolutely Yes. PyCaret 3.0 has integration with [`Fugue`](https://github.com/fugue-project/fugue). You can now distribute `compare_models` function using the `parallel` parameter on your choice of framework. The current supported frameworks are `Ray`, `Dask`, and `Spark`. To learn more about this, check out [this link](https://pycaret.gitbook.io/docs/get-started/functions/train#distributed-training-on-a-cluster).

</details>

<details>

<summary>How can I contribute to PyCaret?</summary>

Thank you for choosing to contribute to PyCaret. There are a ton of great open-source projects out there, so we appreciate your interest in contributing to PyCaret. Please check out our [Contribution Guidelines](https://github.com/pycaret/pycaret/blob/master/CONTRIBUTING.md).

</details>

<details>

<summary>Does PyCaret support Deep Learning or Reinforcement Learning?</summary>

Not yet. In the future, maybe.

</details>

<details>

<summary>Can I integrate PyCaret with BI tools like Power BI, Tableau, Qlik, etc.?</summary>

Yes, any tool that supports the Python environment. You can use PyCaret within Power BI, Tableau, SQL, Alteryx, KNIME.&#x20;

</details>

<details>

<summary>How can I change verbosity in PyCaret?</summary>

Most functions in PyCaret has `verbose` parameter. Simply set `verbose=False` in the function.&#x20;

**Example:**

{% code lineNumbers="true" %}

```python
lr = create_model('lr', verbose = False)
```

{% endcode %}

</details>

<details>

<summary>How can can I silent the logger?</summary>

We have noticed in some situations that the logger of PyCaret can conflict with other libraries in the environment causing an abnormal behavior resulting in logs being printed on the screen (Notebook or CLI) as the code is running. While in the next major release (3.0), we are planning to make the logger more configurable, allowing you to totally disable it if you want. In the meantime, there is a way around using environment variables. Run the following code on the top of your Notebook:

{% code lineNumbers="true" %}

```python
import os
os.environ["PYCARET_CUSTOM_LOGGING_LEVEL"] = "CRITICAL"
```

{% endcode %}

**NOTE:** This command will set an environment variable that is used by PyCaret's logger. Setting it to `CRITICAL` means that only critical messages will be logged and there aren't many critical messages in PyCaret.&#x20;

</details>

<details>

<summary>I am having issues in installing PyCaret, what can I do?</summary>

Search on our [GitHub](https://github.com/pycaret/pycaret/issues) if others may have faced the same issue. If you are still stuck feel free to open a [new issue](https://github.com/pycaret/pycaret/issues).

</details>

<details>

<summary>Can I add my own custom models in PyCaret?</summary>

Absolutely. PyCaret's vision is to give you full control of your ML pipeline. To add custom models, there is only one rule. They must be compatible with standard `sklearn` API. To learn how to do it, you can read the following tutorials by Fahad Akbar:

* [Custom Estimator with PyCaret - Part I](https://towardsdatascience.com/custome-estimator-with-pycaret-part-1-by-fahad-akbar-839513315965)
* [Custom Estimator with PyCaret - Part II](https://towardsdatascience.com/custom-estimator-with-pycaret-part-2-by-fahad-akbar-aee4dbdacbf)

</details>

<details>

<summary>Can I add custom metrics for cross-validation in PyCaret?</summary>

Absolutely. PyCaret aim's to balance the abstraction with flexibility and so far we are doing a pretty good job. You can use PyCaret's `add_metric` and `remove_metric` functions to add or remove metrics used for cross-validation.  [Learn More](https://pycaret.gitbook.io/docs/get-started/functions/others#add_metric).

</details>

<details>

<summary>Can I just use PyCaret for data preprocessing?</summary>

Yes if you would like. You can run the `setup` function which handles all the data preprocessing and after that you can access the transformed train set and test set using the `get_config` function.&#x20;

**Example:**

{% code overflow="wrap" lineNumbers="true" %}

```python
from pycaret.classification import *
s = setup(data, target = 'target_name')

X_train, y_train = get_config('X_train_transformed'), get_config('y_train_transformed')
X_test, y_test = get_config('X_test_transformed'), get_config('y_test_transformed')
```

{% endcode %}

</details>

<details>

<summary>Can I export models from PyCaret and work on them outside of PyCaret?</summary>

Absolutely. You can use the `save_model` function of PyCaret to export the entire Pipeline as a `pkl` file. [Learn more](https://pycaret.gitbook.io/docs/get-started/functions/deploy#save_model) about this function.

</details>

<details>

<summary>Can I deploy ML pipelines on cloud using PyCaret?</summary>

Absolutely. PyCaret is an end-to-end library with a lot of deployment functionalities. There are many official tutorials on deployment on different cloud platforms such as Azure, AWS, and GCP. You can check out these [tutorials here](https://pycaret.gitbook.io/docs/official-blog#pycaret-add-ml-deployment).

</details>

<details>

<summary>Can I install and run PyCaret on an Apple M1 MacBook?</summary>

It's not straightforward due to some issues in the underlying dependencies of PyCaret. However, if you have tried everything and still can't find a solution, this [article](https://pareekshithkatti.medium.com/setting-up-python-for-data-science-on-m1-mac-ced8a0d05911) by Pareekshith Katti may help you.

</details>

<details>

<summary>Do I need a powerful computer to use PyCaret?</summary>

No, as long as your data can fit in the memory, you can use PyCaret. No super computer is needed.

</details>

<details>

<summary>Why is my pull request not getting any attention?</summary>

The review process may take some time. You should not be discouraged by delays in review on your pull request. We have many features that are requested by the community and only limited time from our maintainers to review and approve these pull requests. Since every feature comes at a cost of lifetime maintenance, we care a lot about getting things right the first time.&#x20;

</details>

<details>

<summary>Is PyCaret comparable to scikit-learn and ML libraries and framework?</summary>

Well, PyCaret is built on top of common ML libraries and frameworks such as scikit-learn, LightGBM, XGBoost, etc. The benefit of using PyCaret is that you don't have to write a lot of code. The underlying models and evaluation framework are the same as what you are used to.&#x20;

</details>


