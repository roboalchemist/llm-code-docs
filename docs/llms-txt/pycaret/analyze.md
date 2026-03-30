# Source: https://pycaret.gitbook.io/docs/get-started/functions/analyze.md

# Analyze

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
