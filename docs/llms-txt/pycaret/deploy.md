# Source: https://pycaret.gitbook.io/docs/get-started/functions/deploy.md

# Deploy

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
