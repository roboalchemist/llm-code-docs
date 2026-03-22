# Source: https://pycaret.gitbook.io/docs/get-started/preprocessing.md

# Data Preprocessing

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
