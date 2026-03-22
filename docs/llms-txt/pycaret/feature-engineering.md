# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing/feature-engineering.md

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
