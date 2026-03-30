# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing/feature-selection.md

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
