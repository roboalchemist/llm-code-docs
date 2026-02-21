# Source: https://www.tensorflow.org/guide/keras/serialization_and_saving

Title: Save, serialize, and export models

URL Source: https://www.tensorflow.org/guide/keras/serialization_and_saving

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/keras/serialization_and_saving#main-content)

*   [Install](https://www.tensorflow.org/install)
*   [Learn](https://www.tensorflow.org/learn)
    *   [Tutorials](https://www.tensorflow.org/tutorials)
    *   [Guide](https://www.tensorflow.org/guide)
    *   [Migrate to TF2](https://www.tensorflow.org/guide/migrate)
    *   [TF 1 ↗](https://github.com/tensorflow/docs/tree/master/site/en/r1)

*   [API](https://www.tensorflow.org/api)
*   [Ecosystem](https://www.tensorflow.org/resources/models-datasets)
*   [Community](https://www.tensorflow.org/community)
*   [Why TensorFlow](https://www.tensorflow.org/about)
*   [GitHub](https://github.com/tensorflow)

*   [TensorFlow guide](https://www.tensorflow.org/guide)
*   TensorFlow basics

*   [Overview](https://www.tensorflow.org/guide/basics)
*   [Tensors](https://www.tensorflow.org/guide/tensor)
*   [Variables](https://www.tensorflow.org/guide/variable)
*   [Automatic differentiation](https://www.tensorflow.org/guide/autodiff)
*   [Graphs and functions](https://www.tensorflow.org/guide/intro_to_graphs)
*   [Modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)
*   [Training loops](https://www.tensorflow.org/guide/basic_training_loops)
*   Keras

*   [Overview](https://www.tensorflow.org/guide/keras)
*   [The Sequential model](https://www.tensorflow.org/guide/keras/sequential_model)
*   [The Functional API](https://www.tensorflow.org/guide/keras/functional_api)
*   [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods)
*   [Making new layers and models via subclassing](https://www.tensorflow.org/guide/keras/making_new_layers_and_models_via_subclassing)
*   [Serialization and saving](https://www.tensorflow.org/guide/keras/serialization_and_saving)
*   [Customizing Saving](https://www.tensorflow.org/guide/keras/customizing_saving_and_serialization)
*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers)
*   [Customizing what happens in fit()](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit)
*   [Writing a training loop from scratch](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns)
*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding)
*   [Writing your own callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks)
*   [Transfer learning & fine-tuning](https://www.tensorflow.org/guide/keras/transfer_learning)
*   [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training)
*   Build with Core

*   [Overview](https://www.tensorflow.org/guide/core)
*   [Quickstart for Core](https://www.tensorflow.org/guide/core/quickstart_core)
*   [Logistic regression](https://www.tensorflow.org/guide/core/logistic_regression_core)
*   [Multilayer perceptrons](https://www.tensorflow.org/guide/core/mlp_core)
*   [Matrix approximation](https://www.tensorflow.org/guide/core/matrix_core)
*   [Custom optimizers](https://www.tensorflow.org/guide/core/optimizers_core)
*   [DTensor with Core APIs](https://www.tensorflow.org/guide/core/distribution)
*   TensorFlow in depth

*   [Tensor slicing](https://www.tensorflow.org/guide/tensor_slicing)
*   [Advanced autodiff](https://www.tensorflow.org/guide/advanced_autodiff)
*   [Ragged tensor](https://www.tensorflow.org/guide/ragged_tensor)
*   [Sparse tensor](https://www.tensorflow.org/guide/sparse_tensor)
*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)
*   [NumPy API](https://www.tensorflow.org/guide/tf_numpy)
*   [NumPy API Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)
*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)
*   [Thinking in TensorFlow 2](https://www.tensorflow.org/guide/effective_tf2)
*   Customization

*   [Create an op](https://www.tensorflow.org/guide/create_op)
*   [Extension types](https://www.tensorflow.org/guide/extension_type)
*   Data input pipelines

*   [tf.data](https://www.tensorflow.org/guide/data)
*   [Optimize pipeline performance](https://www.tensorflow.org/guide/data_performance)
*   [Analyze pipeline performance](https://www.tensorflow.org/guide/data_performance_analysis)
*   Import and export

*   [Checkpoint](https://www.tensorflow.org/guide/checkpoint)
*   [SavedModel](https://www.tensorflow.org/guide/saved_model)
*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)
*   Accelerators

*   [Distributed training](https://www.tensorflow.org/guide/distributed_training)
*   [GPU](https://www.tensorflow.org/guide/gpu)
*   [TPU](https://www.tensorflow.org/guide/tpu)
*   Performance

*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)
*   [Profile TensorFlow performance](https://www.tensorflow.org/guide/profiler)
*   [Optimize GPU Performance](https://www.tensorflow.org/guide/gpu_performance_analysis)
*   [Graph optimization](https://www.tensorflow.org/guide/graph_optimization)
*   [Mixed precision](https://www.tensorflow.org/guide/mixed_precision)
*   Model Garden

*   [Overview](https://www.tensorflow.org/tfmodels)
*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit)
*   [TFModels - NLP](https://www.tensorflow.org/tfmodels/nlp)
*   [Example: Image classification](https://www.tensorflow.org/tfmodels/vision/image_classification)
*   [Example: Object Detection](https://www.tensorflow.org/tfmodels/vision/object_detection)
*   [Example: Semantic Segmentation](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation)
*   [Example: Instance Segmentation](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)
*   Estimators

*   [Estimator overview](https://www.tensorflow.org/guide/estimator)
*   Appendix

*   [Version compatibility](https://www.tensorflow.org/guide/versions)

Save, serialize, and export models
----------------------------------

**Authors:** Neel Kovelamudi, Francois Chollet

Introduction
------------

A Keras model consists of multiple components:

*   The architecture, or configuration, which specifies what layers the model contain, and how they're connected.
*   A set of weights values (the "state of the model").
*   An optimizer (defined by compiling the model).
*   A set of losses and metrics (defined by compiling the model).

The Keras API saves all of these pieces together in a unified format, marked by the `.keras` extension. This is a zip archive consisting of the following:

*   A JSON-based configuration file (config.json): Records of model, layer, and other trackables' configuration.
*   A H5-based state file, such as `model.weights.h5` (for the whole model), with directory keys for layers and their weights.
*   A metadata file in JSON, storing things such as the current Keras version.

Let's take a look at how this works.

How to save and load a model
----------------------------

If you only have 10 seconds to read this guide, here's what you need to know.

**Saving a Keras model:**

```
model = ...  # Get model (Sequential, Functional Model, or Model subclass)
model.save('path/to/location.keras')  # The file needs to end with the .keras extension
```

**Loading the model back:**

```
model = keras.models.load_model('path/to/location.keras')
```

Now, let's look at the details.

Setup
-----

```
import numpy as np
import tensorflow as tf
import keras
```

Saving
------

This section is about saving an entire model to a single file. The file will include:

*   The model's architecture/config
*   The model's weight values (which were learned during training)
*   The model's compilation information (if `compile()` was called)
*   The optimizer and its state, if any (this enables you to restart training where you left)

#### APIs

You can save a model with `model.save()` or [`keras.models.save_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/save_model) (which is equivalent). You can load it back with [`keras.models.load_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/load_model).

The recommended format is the "Keras v3" format, which uses the `.keras` extension. There are, however, two legacy formats that are available: the **TensorFlow SavedModel format** and the older Keras **H5 format**.

You can switch to the SavedModel format by:

*   Passing `save_format='tf'` to `save()`
*   Passing a filename without an extension

You can switch to the H5 format by:

*   Passing `save_format='h5'` to `save()`
*   Passing a filename that ends in `.h5`

**Example:**

```
def get_model():
    # Create a simple model.
    inputs = keras.Input(shape=(32,))
    outputs = keras.layers.Dense(1)(inputs)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer=keras.optimizers.Adam(), loss="mean_squared_error")
    return model

model = get_model()

# Train the model.
test_input = np.random.random((128, 32))
test_target = np.random.random((128, 1))
model.fit(test_input, test_target)

# Calling `save('my_model.keras')` creates a zip archive `my_model.keras`.
model.save("my_model.keras")

# It can be used to reconstruct the model identically.
reconstructed_model = keras.models.load_model("my_model.keras")

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)
```
4/4 [==============================] - 2s 4ms/step - loss: 2.9952
4/4 [==============================] - 0s 2ms/step
4/4 [==============================] - 0s 1ms/step

### Custom objects

This section covers the basic workflows for handling custom layers, functions, and models in Keras saving and reloading.

When saving a model that includes custom objects, such as a subclassed Layer, you **must** define a `get_config()` method on the object class. If the arguments passed to the constructor (`__init__()` method) of the custom object aren't Python objects (anything other than base types like ints, strings, etc.), then you **must** serialize these arguments in `get_config()` method and also explicitly deserialize these arguments in the `from_config()` class method.

Like this:

```
class CustomLayer(keras.layers.Layer):
    def __init__(self, sublayer, **kwargs):
        super().__init__(**kwargs)
        self.sublayer = sublayer

    def call(self, x):
        return self.sublayer(x)

    def get_config(self):
        base_config = super().get_config()
        config = {
            "sublayer": keras.saving.serialize_keras_object(self.sublayer),
        }
        return {**base_config, **config}

    @classmethod
    def from_config(cls, config):
        sublayer_config = config.pop("sublayer")
        sublayer = keras.saving.deserialize_keras_object(sublayer_config)
        return cls(sublayer, **config)
```

Please see the [Defining the config methods section](https://www.tensorflow.org/guide/keras/serialization_and_saving#config_methods) for more details and examples.

The saved `.keras` file is lightweight and does not store the Python code for custom objects. Therefore, to reload the model, `load_model` requires access to the definition of any custom objects used through one of the following methods:

1.   Registering custom objects **(preferred)**,
2.   Passing custom objects directly when loading, or
3.   Using a custom object scope

Below are examples of each workflow:

#### Registering custom objects (**preferred**)

This is the preferred method, as custom object registration greatly simplifies saving and loading code. Adding the [`@keras.saving.register_keras_serializable`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/register_keras_serializable) decorator to the class definition of a custom object registers the object globally in a master list, allowing Keras to recognize the object when loading the model.

Let's create a custom model involving both a custom layer and a custom activation function to demonstrate this.

**Example:**

```
# Clear all previously registered custom objects
keras.saving.get_custom_objects().clear()

# Upon registration, you can optionally specify a package or a name.
# If left blank, the package defaults to `Custom` and the name defaults to
# the class name.
@keras.saving.register_keras_serializable(package="MyLayers")
class CustomLayer(keras.layers.Layer):
    def __init__(self, factor):
        super().__init__()
        self.factor = factor

    def call(self, x):
        return x * self.factor

    def get_config(self):
        return {"factor": self.factor}

@keras.saving.register_keras_serializable(package="my_package", name="custom_fn")
def custom_fn(x):
    return x**2

# Create the model.
def get_model():
    inputs = keras.Input(shape=(4,))
    mid = CustomLayer(0.5)(inputs)
    outputs = keras.layers.Dense(1, activation=custom_fn)(mid)
    model = keras.Model(inputs, outputs)
    model.compile(optimizer="rmsprop", loss="mean_squared_error")
    return model

# Train the model.
def train_model(model):
    input = np.random.random((4, 4))
    target = np.random.random((4, 1))
    model.fit(input, target)
    return model

test_input = np.random.random((4, 4))
test_target = np.random.random((4, 1))

model = get_model()
model = train_model(model)
model.save("custom_model.keras")

# Now, we can simply load without worrying about our custom objects.
reconstructed_model = keras.models.load_model("custom_model.keras")

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)
```
1/1 [==============================] - 0s 443ms/step - loss: 0.1362
1/1 [==============================] - 0s 62ms/step
1/1 [==============================] - 0s 59ms/step

#### Passing custom objects to `load_model()`

```
model = get_model()
model = train_model(model)

# Calling `save('my_model.keras')` creates a zip archive `my_model.keras`.
model.save("custom_model.keras")

# Upon loading, pass a dict containing the custom objects used in the
# `custom_objects` argument of `keras.models.load_model()`.
reconstructed_model = keras.models.load_model(
    "custom_model.keras",
    custom_objects={"CustomLayer": CustomLayer, "custom_fn": custom_fn},
)

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)
```
1/1 [==============================] - 0s 364ms/step - loss: 0.2342
WARNING:tensorflow:5 out of the last 11 calls to <function Model.make_predict_function.<locals>.predict_function at 0x7f834c0913a0> triggered tf.function retracing. Tracing is expensive and the excessive number of tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing tensors with different shapes, (3) passing Python objects instead of tensors. For (1), please define your @tf.function outside of the loop. For (2), @tf.function has reduce_retracing=True option that can avoid unnecessary retracing. For (3), please refer to https://www.tensorflow.org/guide/function#controlling_retracing and https://www.tensorflow.org/api_docs/python/tf/function for  more details.
1/1 [==============================] - 0s 62ms/step
WARNING:tensorflow:6 out of the last 12 calls to <function Model.make_predict_function.<locals>.predict_function at 0x7f82e07d1550> triggered tf.function retracing. Tracing is expensive and the excessive number of tracings could be due to (1) creating @tf.function repeatedly in a loop, (2) passing tensors with different shapes, (3) passing Python objects instead of tensors. For (1), please define your @tf.function outside of the loop. For (2), @tf.function has reduce_retracing=True option that can avoid unnecessary retracing. For (3), please refer to https://www.tensorflow.org/guide/function#controlling_retracing and https://www.tensorflow.org/api_docs/python/tf/function for  more details.
1/1 [==============================] - 0s 61ms/step

#### Using a custom object scope

Any code within the custom object scope will be able to recognize the custom objects passed to the scope argument. Therefore, loading the model within the scope will allow the loading of our custom objects.

**Example:**

```
model = get_model()
model = train_model(model)
model.save("custom_model.keras")

# Pass the custom objects dictionary to a custom object scope and place
# the `keras.models.load_model()` call within the scope.
custom_objects = {"CustomLayer": CustomLayer, "custom_fn": custom_fn}

with keras.saving.custom_object_scope(custom_objects):
    reconstructed_model = keras.models.load_model("custom_model.keras")

# Let's check:
np.testing.assert_allclose(
    model.predict(test_input), reconstructed_model.predict(test_input)
)
```
1/1 [==============================] - 0s 371ms/step - loss: 0.2904
1/1 [==============================] - 0s 59ms/step
1/1 [==============================] - 0s 60ms/step

### Model serialization

This section is about saving only the model's configuration, without its state. The model's configuration (or architecture) specifies what layers the model contains, and how these layers are connected. If you have the configuration of a model, then the model can be created with a freshly initialized state (no weights or compilation information).

#### APIs

The following serialization APIs are available:

*   [`keras.models.clone_model(model)`](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model): make a (randomly initialized) copy of a model.
*   `get_config()` and `cls.from_config()`: retrieve the configuration of a layer or model, and recreate a model instance from its config, respectively.
*   `keras.models.to_json()` and [`keras.models.model_from_json()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/model_from_json): similar, but as JSON strings.
*   [`keras.saving.serialize_keras_object()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/serialize_keras_object): retrieve the configuration any arbitrary Keras object.
*   [`keras.saving.deserialize_keras_object()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/deserialize_keras_object): recreate an object instance from its configuration.

#### In-memory model cloning

You can do in-memory cloning of a model via [`keras.models.clone_model()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/clone_model). This is equivalent to getting the config then recreating the model from its config (so it does not preserve compilation information or layer weights values).

**Example:**

```
new_model = keras.models.clone_model(model)
```

#### `get_config()` and `from_config()`

Calling `model.get_config()` or `layer.get_config()` will return a Python dict containing the configuration of the model or layer, respectively. You should define `get_config()` to contain arguments needed for the `__init__()` method of the model or layer. At loading time, the `from_config(config)` method will then call `__init__()` with these arguments to reconstruct the model or layer.

**Layer example:**

```
layer = keras.layers.Dense(3, activation="relu")
layer_config = layer.get_config()
print(layer_config)
```
{'name': 'dense_4', 'trainable': True, 'dtype': 'float32', 'units': 3, 'activation': 'relu', 'use_bias': True, 'kernel_initializer': {'module': 'keras.initializers', 'class_name': 'GlorotUniform', 'config': {'seed': None}, 'registered_name': None}, 'bias_initializer': {'module': 'keras.initializers', 'class_name': 'Zeros', 'config': {}, 'registered_name': None}, 'kernel_regularizer': None, 'bias_regularizer': None, 'activity_regularizer': None, 'kernel_constraint': None, 'bias_constraint': None}

Now let's reconstruct the layer using the `from_config()` method:

```
new_layer = keras.layers.Dense.from_config(layer_config)
```

**Sequential model example:**

```
model = keras.Sequential([keras.Input((32,)), keras.layers.Dense(1)])
config = model.get_config()
new_model = keras.Sequential.from_config(config)
```

**Functional model example:**

```
inputs = keras.Input((32,))
outputs = keras.layers.Dense(1)(inputs)
model = keras.Model(inputs, outputs)
config = model.get_config()
new_model = keras.Model.from_config(config)
```

#### `to_json()` and [`keras.models.model_from_json()`](https://www.tensorflow.org/api_docs/python/tf/keras/models/model_from_json)

This is similar to `get_config` / `from_config`, except it turns the model into a JSON string, which can then be loaded without the original model class. It is also specific to models, it isn't meant for layers.

**Example:**

```
model = keras.Sequential([keras.Input((32,)), keras.layers.Dense(1)])
json_config = model.to_json()
new_model = keras.models.model_from_json(json_config)
```

#### Arbitrary object serialization and deserialization

The [`keras.saving.serialize_keras_object()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/serialize_keras_object) and [`keras.saving.deserialize_keras_object()`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/deserialize_keras_object) APIs are general-purpose APIs that can be used to serialize or deserialize any Keras object and any custom object. It is at the foundation of saving model architecture and is behind all `serialize()`/`deserialize()` calls in keras.

**Example**:

```
my_reg = keras.regularizers.L1(0.005)
config = keras.saving.serialize_keras_object(my_reg)
print(config)
```
{'module': 'keras.regularizers', 'class_name': 'L1', 'config': {'l1': 0.004999999888241291}, 'registered_name': None}

Note the serialization format containing all the necessary information for proper reconstruction:

*   `module` containing the name of the Keras module or other identifying module the object comes from
*   `class_name` containing the name of the object's class.
*   `config` with all the information needed to reconstruct the object
*   `registered_name` for custom objects. See [here](https://www.tensorflow.org/guide/keras/serialization_and_saving#custom_object_serialization).

Now we can reconstruct the regularizer.

```
new_reg = keras.saving.deserialize_keras_object(config)
```

### Model weights saving

You can choose to only save & load a model's weights. This can be useful if:

*   You only need the model for inference: in this case you won't need to restart training, so you don't need the compilation information or optimizer state.
*   You are doing transfer learning: in this case you will be training a new model reusing the state of a prior model, so you don't need the compilation information of the prior model.

#### APIs for in-memory weight transfer

Weights can be copied between different objects by using `get_weights()` and `set_weights()`:

*   [`keras.layers.Layer.get_weights()`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#get_weights): Returns a list of NumPy arrays of weight values.
*   [`keras.layers.Layer.set_weights(weights)`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Layer#set_weights): Sets the model weights to the values provided (as NumPy arrays).

Examples:

**_Transfering weights from one layer to another, in memory_**

```
def create_layer():
    layer = keras.layers.Dense(64, activation="relu", name="dense_2")
    layer.build((None, 784))
    return layer

layer_1 = create_layer()
layer_2 = create_layer()

# Copy weights from layer 1 to layer 2
layer_2.set_weights(layer_1.get_weights())
```

**_Transfering weights from one model to another model with a compatible architecture, in memory_**

```
# Create a simple functional model
inputs = keras.Input(shape=(784,), name="digits")
x = keras.layers.Dense(64, activation="relu", name="dense_1")(inputs)
x = keras.layers.Dense(64, activation="relu", name="dense_2")(x)
outputs = keras.layers.Dense(10, name="predictions")(x)
functional_model = keras.Model(inputs=inputs, outputs=outputs, name="3_layer_mlp")

# Define a subclassed model with the same architecture
class SubclassedModel(keras.Model):
    def __init__(self, output_dim, name=None):
        super().__init__(name=name)
        self.output_dim = output_dim
        self.dense_1 = keras.layers.Dense(64, activation="relu", name="dense_1")
        self.dense_2 = keras.layers.Dense(64, activation="relu", name="dense_2")
        self.dense_3 = keras.layers.Dense(output_dim, name="predictions")

    def call(self, inputs):
        x = self.dense_1(inputs)
        x = self.dense_2(x)
        x = self.dense_3(x)
        return x

    def get_config(self):
        return {"output_dim": self.output_dim, "name": self.name}

subclassed_model = SubclassedModel(10)
# Call the subclassed model once to create the weights.
subclassed_model(tf.ones((1, 784)))

# Copy weights from functional_model to subclassed_model.
subclassed_model.set_weights(functional_model.get_weights())

assert len(functional_model.weights) == len(subclassed_model.weights)
for a, b in zip(functional_model.weights, subclassed_model.weights):
    np.testing.assert_allclose(a.numpy(), b.numpy())
```

**_The case of stateless layers_**

Because stateless layers do not change the order or number of weights, models can have compatible architectures even if there are extra/missing stateless layers.

```
inputs = keras.Input(shape=(784,), name="digits")
x = keras.layers.Dense(64, activation="relu", name="dense_1")(inputs)
x = keras.layers.Dense(64, activation="relu", name="dense_2")(x)
outputs = keras.layers.Dense(10, name="predictions")(x)
functional_model = keras.Model(inputs=inputs, outputs=outputs, name="3_layer_mlp")

inputs = keras.Input(shape=(784,), name="digits")
x = keras.layers.Dense(64, activation="relu", name="dense_1")(inputs)
x = keras.layers.Dense(64, activation="relu", name="dense_2")(x)

# Add a dropout layer, which does not contain any weights.
x = keras.layers.Dropout(0.5)(x)
outputs = keras.layers.Dense(10, name="predictions")(x)
functional_model_with_dropout = keras.Model(
    inputs=inputs, outputs=outputs, name="3_layer_mlp"
)

functional_model_with_dropout.set_weights(functional_model.get_weights())
```

#### APIs for saving weights to disk & loading them back

Weights can be saved to disk by calling `model.save_weights(filepath)`. The filename should end in `.weights.h5`.

**Example:**

```
# Runnable example
sequential_model = keras.Sequential(
    [
        keras.Input(shape=(784,), name="digits"),
        keras.layers.Dense(64, activation="relu", name="dense_1"),
        keras.layers.Dense(64, activation="relu", name="dense_2"),
        keras.layers.Dense(10, name="predictions"),
    ]
)
sequential_model.save_weights("my_model.weights.h5")
sequential_model.load_weights("my_model.weights.h5")
```

Note that changing `layer.trainable` may result in a different `layer.weights` ordering when the model contains nested layers.

```
class NestedDenseLayer(keras.layers.Layer):
    def __init__(self, units, name=None):
        super().__init__(name=name)
        self.dense_1 = keras.layers.Dense(units, name="dense_1")
        self.dense_2 = keras.layers.Dense(units, name="dense_2")

    def call(self, inputs):
        return self.dense_2(self.dense_1(inputs))

nested_model = keras.Sequential([keras.Input((784,)), NestedDenseLayer(10, "nested")])
variable_names = [v.name for v in nested_model.weights]
print("variables: {}".format(variable_names))

print("\nChanging trainable status of one of the nested layers...")
nested_model.get_layer("nested").dense_1.trainable = False

variable_names_2 = [v.name for v in nested_model.weights]
print("\nvariables: {}".format(variable_names_2))
print("variable ordering changed:", variable_names != variable_names_2)
```
variables: ['nested/dense_1/kernel:0', 'nested/dense_1/bias:0', 'nested/dense_2/kernel:0', 'nested/dense_2/bias:0']

Changing trainable status of one of the nested layers...

variables: ['nested/dense_2/kernel:0', 'nested/dense_2/bias:0', 'nested/dense_1/kernel:0', 'nested/dense_1/bias:0']
variable ordering changed: True

##### **Transfer learning example**

When loading pretrained weights from a weights file, it is recommended to load the weights into the original checkpointed model, and then extract the desired weights/layers into a new model.

**Example:**

```
def create_functional_model():
    inputs = keras.Input(shape=(784,), name="digits")
    x = keras.layers.Dense(64, activation="relu", name="dense_1")(inputs)
    x = keras.layers.Dense(64, activation="relu", name="dense_2")(x)
    outputs = keras.layers.Dense(10, name="predictions")(x)
    return keras.Model(inputs=inputs, outputs=outputs, name="3_layer_mlp")

functional_model = create_functional_model()
functional_model.save_weights("pretrained.weights.h5")

# In a separate program:
pretrained_model = create_functional_model()
pretrained_model.load_weights("pretrained.weights.h5")

# Create a new model by extracting layers from the original model:
extracted_layers = pretrained_model.layers[:-1]
extracted_layers.append(keras.layers.Dense(5, name="dense_3"))
model = keras.Sequential(extracted_layers)
model.summary()
```
Model: "sequential_4"
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 dense_1 (Dense)             (None, 64)                50240     
                                                                 
 dense_2 (Dense)             (None, 64)                4160      
                                                                 
 dense_3 (Dense)             (None, 5)                 325       
                                                                 
=================================================================
Total params: 54725 (213.77 KB)
Trainable params: 54725 (213.77 KB)
Non-trainable params: 0 (0.00 Byte)
_________________________________________________________________

Exporting
---------

Keras also lets you to create a lightweight version of your model for inferencing that contains the model's forward pass only (the `call()` method). This TensorFlow SavedModel artifact can then be served via TF-Serving, and all original code of the model (including custom layers) are no longer necessary to reload the artifact--it is entirely standalone.

#### APIs

*   `model.export()`, which exports the model to a lightweight SavedModel artifact for inference
*   `artifact.serve()`, which calls the exported artifact's forward pass

Lower level API for customization:

*   [`keras.export.ExportArchive`](https://www.tensorflow.org/api_docs/python/tf/keras/export/ExportArchive), which can be used to customize the serving endpoints. This is used internally by `model.export()`.

### Simple exporting with .export()

Let's go through a simple example of `model.export()` using a Functional model.

**Example:**

```
inputs = keras.Input(shape=(16,))
x = keras.layers.Dense(8, activation="relu")(inputs)
x = keras.layers.BatchNormalization()(x)
outputs = keras.layers.Dense(1, activation="sigmoid")(x)
model = keras.Model(inputs, outputs)

input_data = np.random.random((8, 16))
output_data = model(input_data)  # **NOTE**: Make sure your model is built!

# Export the model as a SavedModel artifact in a filepath.
model.export("exported_model")

# Reload the SavedModel artifact
reloaded_artifact = tf.saved_model.load("exported_model")

# Use the `.serve()` endpoint to call the forward pass on the input data
new_output_data = reloaded_artifact.serve(input_data)
```
INFO:tensorflow:Assets written to: exported_model/assets
INFO:tensorflow:Assets written to: exported_model/assets
Saved artifact at 'exported_model'. The following endpoints are available:

* Endpoint 'serve'
  Args:
    args_0: float32 Tensor, shape=(None, 16)
  Returns:
    float32 Tensor, shape=(None, 1)

### Customizing export artifacts with ExportArchive

The `ExportArchive` object allows you to customize exporting the model and add additional endpoints for serving. Here are its associated APIs:

*   `track()` to register the layer(s) or model(s) to be used,
*   `add_endpoint()` method to register a new serving endpoint.
*   `write_out()` method to save the artifact.
*   `add_variable_collection` method to register a set of variables to be retrieved after reloading.

By default, `model.export("path/to/location")` does the following:

```
export_archive = ExportArchive()
export_archive.track(model)
export_archive.add_endpoint(
    name="serve",
    fn=model.call,
input_signature=[tf.TensorSpec(shape=(None, 3), dtype=tf.float32)],  # `input_signature`
changes depending on model.
)
export_archive.write_out("path/to/location")
```

Let's look at an example customizing this for a MultiHeadAttention layer.

**Example:**

```
layer = keras.layers.MultiHeadAttention(2, 2)
x1 = tf.random.normal((3, 2, 2))
x2 = tf.random.normal((3, 2, 2))
ref_output = layer(x1, x2).numpy()  # **NOTE**: Make sure layer is built!

export_archive = keras.export.ExportArchive()  # Instantiate ExportArchive object
export_archive.track(layer)  # Register the layer to be used
export_archive.add_endpoint(  # New endpoint `call` corresponding to `model.call`
    "call",
    layer.call,
    input_signature=[  # input signature corresponding to 2 inputs
        tf.TensorSpec(
            shape=(None, 2, 2),
            dtype=tf.float32,
        ),
        tf.TensorSpec(
            shape=(None, 2, 2),
            dtype=tf.float32,
        ),
    ],
)

# Register the layer weights as a set of variables to be retrieved
export_archive.add_variable_collection("my_vars", layer.weights)
np.testing.assert_equal(len(export_archive.my_vars), 8)
# weights corresponding to 2 inputs, each of which are 2*2

# Save the artifact
export_archive.write_out("exported_mha_layer")

# Reload the artifact
revived_layer = tf.saved_model.load("exported_mha_layer")
np.testing.assert_allclose(
    ref_output,
    revived_layer.call(query=x1, value=x2).numpy(),
    atol=1e-6,
)
np.testing.assert_equal(len(revived_layer.my_vars), 8)
```
INFO:tensorflow:Assets written to: exported_mha_layer/assets
INFO:tensorflow:Assets written to: exported_mha_layer/assets
Saved artifact at 'exported_mha_layer'. The following endpoints are available:

* Endpoint 'call'
  Args:
    query: float32 Tensor, shape=(None, 2, 2)
    value: float32 Tensor, shape=(None, 2, 2)
  Returns:
    float32 Tensor, shape=(None, 2, 2)

### Appendix: Handling custom objects

#### Defining the config methods

Specifications:

*   `get_config()` should return a JSON-serializable dictionary in order to be compatible with the Keras architecture- and model-saving APIs.
*   `from_config(config)` (a `classmethod`) should return a new layer or model object that is created from the config. The default implementation returns `cls(**config)`.

**Example:**

```
@keras.saving.register_keras_serializable(package="MyLayers", name="KernelMult")
class MyDense(keras.layers.Layer):
    def __init__(
        self,
        units,
        *,
        kernel_regularizer=None,
        kernel_initializer=None,
        nested_model=None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.hidden_units = units
        self.kernel_regularizer = kernel_regularizer
        self.kernel_initializer = kernel_initializer
        self.nested_model = nested_model

    def get_config(self):
        config = super().get_config()
        # Update the config with the custom layer's parameters
        config.update(
            {
                "units": self.hidden_units,
                "kernel_regularizer": self.kernel_regularizer,
                "kernel_initializer": self.kernel_initializer,
                "nested_model": self.nested_model,
            }
        )
        return config

    def build(self, input_shape):
        input_units = input_shape[-1]
        self.kernel = self.add_weight(
            name="kernel",
            shape=(input_units, self.hidden_units),
            regularizer=self.kernel_regularizer,
            initializer=self.kernel_initializer,
        )

    def call(self, inputs):
        return tf.matmul(inputs, self.kernel)

layer = MyDense(units=16, kernel_regularizer="l1", kernel_initializer="ones")
layer3 = MyDense(units=64, nested_model=layer)

config = keras.layers.serialize(layer3)

print(config)

new_layer = keras.layers.deserialize(config)

print(new_layer)
```
{'module': None, 'class_name': 'MyDense', 'config': {'name': 'my_dense_1', 'trainable': True, 'dtype': 'float32', 'units': 64, 'kernel_regularizer': None, 'kernel_initializer': None, 'nested_model': {'module': None, 'class_name': 'MyDense', 'config': {'name': 'my_dense', 'trainable': True, 'dtype': 'float32', 'units': 16, 'kernel_regularizer': 'l1', 'kernel_initializer': 'ones', 'nested_model': None}, 'registered_name': 'MyLayers>KernelMult'} }, 'registered_name': 'MyLayers>KernelMult'}
<__main__.MyDense object at 0x7f82e060d460>

Note that overriding `from_config` is unnecessary above for `MyDense` because `hidden_units`, `kernel_initializer`, and `kernel_regularizer` are ints, strings, and a built-in Keras object, respectively. This means that the default `from_config` implementation of `cls(**config)` will work as intended.

For more complex objects, such as layers and models passed to `__init__`, for example, you must explicitly deserialize these objects. Let's take a look at an example of a model where a `from_config` override is necessary.

**Example:**[](https://www.tensorflow.org/guide/keras/serialization_and_saving)

```
@keras.saving.register_keras_serializable(package="ComplexModels")
class CustomModel(keras.layers.Layer):
    def __init__(self, first_layer, second_layer=None, **kwargs):
        super().__init__(**kwargs)
        self.first_layer = first_layer
        if second_layer is not None:
            self.second_layer = second_layer
        else:
            self.second_layer = keras.layers.Dense(8)

    def get_config(self):
        config = super().get_config()
        config.update(
            {
                "first_layer": self.first_layer,
                "second_layer": self.second_layer,
            }
        )
        return config

    @classmethod
    def from_config(cls, config):
        # Note that you can also use `keras.saving.deserialize_keras_object` here
        config["first_layer"] = keras.layers.deserialize(config["first_layer"])
        config["second_layer"] = keras.layers.deserialize(config["second_layer"])
        return cls(**config)

    def call(self, inputs):
        return self.first_layer(self.second_layer(inputs))

# Let's make our first layer the custom layer from the previous example (MyDense)
inputs = keras.Input((32,))
outputs = CustomModel(first_layer=layer)(inputs)
model = keras.Model(inputs, outputs)

config = model.get_config()
new_model = keras.Model.from_config(config)
```

#### How custom objects are serialized

The serialization format has a special key for custom objects registered via [`@keras.saving.register_keras_serializable`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/register_keras_serializable). This `registered_name` key allows for easy retrieval at loading/deserialization time while also allowing users to add custom naming.

Let's take a look at the config from serializing the custom layer `MyDense` we defined above.

**Example**:

```
layer = MyDense(
    units=16,
    kernel_regularizer=keras.regularizers.L1L2(l1=1e-5, l2=1e-4),
    kernel_initializer="ones",
)
config = keras.layers.serialize(layer)
print(config)
```
{'module': None, 'class_name': 'MyDense', 'config': {'name': 'my_dense_2', 'trainable': True, 'dtype': 'float32', 'units': 16, 'kernel_regularizer': {'module': 'keras.regularizers', 'class_name': 'L1L2', 'config': {'l1': 9.999999747378752e-06, 'l2': 9.999999747378752e-05}, 'registered_name': None}, 'kernel_initializer': 'ones', 'nested_model': None}, 'registered_name': 'MyLayers>KernelMult'}

As shown, the `registered_name` key contains the lookup information for the Keras master list, including the package `MyLayers` and the custom name `KernelMult` that we gave in the [`@keras.saving.register_keras_serializable`](https://www.tensorflow.org/api_docs/python/tf/keras/saving/register_keras_serializable) decorator. Take a look again at the custom class definition/registration [here](https://www.tensorflow.org/guide/keras/serialization_and_saving#registration_example).

Note that the `class_name` key contains the original name of the class, allowing for proper re-initialization in `from_config`.

Additionally, note that the `module` key is `None` since this is a custom object.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-08-05 UTC.
