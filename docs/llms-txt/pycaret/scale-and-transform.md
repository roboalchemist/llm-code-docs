# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing/scale-and-transform.md

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
