# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing/data-preparation.md

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
