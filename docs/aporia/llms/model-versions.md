# Source: https://docs.aporia.com/core-concepts/model-versions.md

# Source: https://docs.aporia.com/v1/core-concepts/model-versions.md

# Models & Versions

### Model

In Aporia, a `model` is any system that can make predictions and can be improved through the use of data.

We use this broad definition in order to support a large number of use cases. Some examples of a model include:

* a simple Pytorch model
* an ensemble of 15 XGBoost models, 37 LightGBM models, and a few deterministic algorithms
* or even an evolutionary algorithm

Aporia models usually serve specific business use cases: Fraud Detection, Credit Risk, Patient Diagnosis, Churn Prediction, LTV, etc.

### Model Version

Each `model` in Aporia can have different `version`. When you (re)train your `model` or update a model's `schema` you should create a new model version in Aporia (via the **Versions page** or **SDK**).

When creating a new model version in Aporia, you'll be able to specify the model version's `schema` - a definition of the inputs and outputs of the model.
