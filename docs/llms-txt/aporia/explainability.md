# Source: https://docs.aporia.com/v1/core-concepts/explainability.md

# Explainability

**"My model is working perfectly! But why?"**

This is what explainability is all about - the ability to tell *why* your model predicted what it actually predicted. Or, in other words, what is the impact of each feature on the final prediction?

<figure><img src="https://1009457926-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FCiBXs570GNM7Jbx4EBQ9%2Fuploads%2FJpd6CVMqWMXubCkZMyPt%2Ftabular-explainability.gif?alt=media" alt=""><figcaption><p>Explainability in Action</p></figcaption></figure>

### Why Explainability?

There are many reasons why you would need explainability for your models, some examples:

* **Trust:** Models can be viewed as a black box that generates predictions; the ability to explain these predictions increases trust in the model.
* **Debugging:** Being able to explain predictions based on different inputs is a powerful debugging tool for identifying errors.
* **Bias and Fairness:** The ability to see the effect of each feature can aid in identifying unintentional biases that may affect the model's fairness.

For further reading on the subject, check out [our blog about explainability](https://www.aporia.com/blog/explainable-ai/).

### Integrating Explainability in Aporia

Aporia lets you explain each prediction by visualizing the impact of each feature on the final prediction. This can be done by clicking on the **Explain** button near each prediction in the "Data Points" page of your model.

You can also interactively change any feature value, click **Re-Explain** and see the impact on a theoretical prediction.&#x20;

**Make sure your feature schema in the model version is&#x20;*****ordered***

When creating your model version, you'll need to make sure that the order of the features is identical to your model artifact features.

Instead of passing a normal `dict` as features schema, you'll need to pass `OrderedDict`. For example:

```python
# Build feature schema by order - you can use model.columns for this of course :)
features = OrderedDict()
features["sepal_length"] = "numeric"
features["sepal_width"] = "numeric"
features["petal_length"] = "numeric"
features["petal_width"] = "numeric"

apr_model = aporia.create_model_version(
    model_id="<MODEL_ID>",
    model_version="v1",
    model_type="multiclass",
    features=features,
    predictions={
          "variety": "categorical"
    }
)
```

**Log Training + Serving data**

Training data is required for Explainability. Please check out   [Data Sources - Overview](https://docs.aporia.com/v1/data-sources) for more information.

**Upload Model Artifact in ONNX format**

[ONNX](https://onnx.ai/) is an open format for Machine Learning models. Models from all popular ML libraries (XGBoost, Sklearn, Tensorflow, Pytorch, etc.) can be converted to ONNX

To upload your model artifact, you'll need to execute:

```python
apr_model.upload_model_artifact(
    artifact_type="onnx",
    model_artifact=onnx_model.SerializeToString()
)
```

Here are quick snippets and references that may help you with converting your model.

#### XGBoost

```python
import onnxmltools
from onnxmltools.convert.common.data_types import FloatTensorType

initial_types = [('features', FloatTensorType([None, X_train.shape[1]]))]

onnx_model = onnxmltools.convert_xgboost(xgb_model, initial_types=initial_types, target_opset=9)
```

#### LightGBM

```python
import onnxmltools
from onnxmltools.convert.common.data_types import FloatTensorType

initial_types = [('features', FloatTensorType([None, X_train.shape[1]]))]

onnx_model = onnxmltools.convert_lightgbm(lgb_model, initial_types=initial_types, target_opset=9)
```

#### Catboost

```python
import onnxmltools
from onnxmltools.convert.common.data_types import FloatTensorType

initial_types = [('features', FloatTensorType([None, X_train.shape[1]]))]

onnx_model = onnxmltools.covnert_catboost(catboost_model, initial_types=initial_types, target_opset=9)
```

#### Scikit Learn

```python
import onnxmltools
from onnxmltools.convert.common.data_types import FloatTensorType

initial_types = [('features', FloatTensorType([None, X_train.shape[1]]))]

onnx_model = onnxmltools.convert_sklearn(skl_model, initial_types=initial_types, target_opset=9)
```

#### Keras

```python
import onnxmltools

onnx_model = onnxmltools.convert_keras(keras_model, target_opset=9)
```

#### Tensorflow

```python
import onnxmltools

onnx_model = onnxmltools.convert_tensorflow(keras_model, target_opset=9)
```

#### Pytorch

```python
# Please see https://pytorch.org/tutorials/advanced/super_resolution_with_onnxruntime.html
```
