# Source: https://keras.io/api/models/model

Title: Keras documentation: The Model class

URL Source: https://keras.io/api/models/model

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L37)

### `Model` class

```
keras.Model()
```

A model grouping layers into an object with training/inference features.

There are three ways to instantiate a `Model`:

With the "Functional API"
-------------------------

You start from `Input`, you chain layer calls to specify the model's forward pass, and finally, you create your model from inputs and outputs:

```
inputs = keras.Input(shape=(37,))
x = keras.layers.Dense(32, activation="relu")(inputs)
outputs = keras.layers.Dense(5, activation="softmax")(x)
model = keras.Model(inputs=inputs, outputs=outputs)
```

Note: Only dicts, lists, and tuples of input tensors are supported. Nested inputs are not supported (e.g. lists of list or dicts of dict).

A new Functional API model can also be created by using the intermediate tensors. This enables you to quickly extract sub-components of the model.

**Example**

```
inputs = keras.Input(shape=(None, None, 3))
processed = keras.layers.RandomCrop(width=128, height=128)(inputs)
conv = keras.layers.Conv2D(filters=32, kernel_size=3)(processed)
pooling = keras.layers.GlobalAveragePooling2D()(conv)
feature = keras.layers.Dense(10)(pooling)

full_model = keras.Model(inputs, feature)
backbone = keras.Model(processed, conv)
activations = keras.Model(conv, feature)
```

Note that the `backbone` and `activations` models are not created with [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function) objects, but with the tensors that originate from [`keras.Input`](https://keras.io/api/layers/core_layers/input#input-function) objects. Under the hood, the layers and weights will be shared across these models, so that user can train the `full_model`, and use `backbone` or `activations` to do feature extraction. The inputs and outputs of the model can be nested structures of tensors as well, and the created models are standard Functional API models that support all the existing APIs.

By subclassing the `Model` class
--------------------------------

In that case, you should define your layers in `__init__()` and you should implement the model's forward pass in `call()`.

```
class MyModel(keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = keras.layers.Dense(32, activation="relu")
        self.dense2 = keras.layers.Dense(5, activation="softmax")

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)

model = MyModel()
```

If you subclass `Model`, you can optionally have a `training` argument (boolean) in `call()`, which you can use to specify a different behavior in training and inference:

```
class MyModel(keras.Model):
    def __init__(self):
        super().__init__()
        self.dense1 = keras.layers.Dense(32, activation="relu")
        self.dense2 = keras.layers.Dense(5, activation="softmax")
        self.dropout = keras.layers.Dropout(0.5)

    def call(self, inputs, training=False):
        x = self.dense1(inputs)
        x = self.dropout(x, training=training)
        return self.dense2(x)

model = MyModel()
```

Once the model is created, you can config the model with losses and metrics with `model.compile()`, train the model with `model.fit()`, or use the model to do prediction with `model.predict()`.

With the `Sequential` class
---------------------------

In addition, [`keras.Sequential`](https://keras.io/api/models/sequential#sequential-class) is a special case of model where the model is purely a stack of single-input, single-output layers.

```
model = keras.Sequential([
    keras.Input(shape=(None, None, 3)),
    keras.layers.Conv2D(filters=32, kernel_size=3),
])
```

**Guides and examples using `Model`**

*   [The Functional API](https://keras.io/guides/functional_api/)
*   [The Sequential model](https://keras.io/guides/sequential_model/)
*   [Making new layers & models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)
*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Customizing `fit()` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
*   [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
*   [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
*   [Writing a custom training loop in JAX](https://keras.io/guides/writing_a_custom_training_loop_in_jax/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/backend/common/keras_tensor.py#L6)

### `KerasTensor` class

```
keras.KerasTensor(
    shape,
    dtype="float32",
    sparse=False,
    ragged=False,
    record_history=True,
    name=None,
    **kwargs
)
```

Symbolic tensor – encapsulates a shape and a dtype.

You can use `KerasTensor` instances to build computation graphs of Keras operations, such as `keras.Function` objects or Functional `keras.models.Model` objects.

**Example**

```
>>> x = keras.KerasTensor(shape=(3, 4), dtype="float32")
>>> x.shape
(3, 4)
>>> x.dtype
float32
```

Calling a Keras operation (including a layer or a model) on a `KerasTensor` instance will return another `KerasTensor` instance with the appropriate shape and dtype. This is called a "symbolic call" (since there is no actual data involved). The computation of the correct output shape and dtype is called "static shape inference".

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L221)

### `summary` method

```
Model.summary(
    line_length=None,
    positions=None,
    print_fn=None,
    expand_nested=False,
    show_trainable=False,
    layer_range=None,
)
```

Prints a string summary of the network.

**Arguments**

*   **line_length**: Total length of printed lines (e.g. set this to adapt the display to different terminal window sizes).
*   **positions**: Relative or absolute positions of log elements in each line. If not provided, becomes `[0.3, 0.6, 0.70, 1.]`. Defaults to `None`.
*   **print_fn**: Print function to use. By default, prints to `stdout`. If `stdout` doesn't work in your environment, change to `print`. It will be called on each line of the summary. You can set it to a custom function in order to capture the string summary.
*   **expand_nested**: Whether to expand the nested models. Defaults to `False`.
*   **show_trainable**: Whether to show if a layer is trainable. Defaults to `False`.
*   **layer_range**: a list or tuple of 2 strings, which is the starting layer name and ending layer name (both inclusive) indicating the range of layers to be printed in summary. It also accepts regex patterns instead of exact names. In this case, the start predicate will be the first element that matches `layer_range[0]` and the end predicate will be the last element that matches `layer_range[1]`. By default `None` considers all layers of the model.

**Raises**

*   **ValueError**: if `summary()` is called before the model is built.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L180)

### `get_layer` method

```
Model.get_layer(name=None, index=None)
```

Retrieves a layer based on either its name (unique) or index.

If `name` and `index` are both provided, `index` will take precedence. Indices are based on order of horizontal graph traversal (bottom-up).

**Arguments**

*   **name**: String, name of layer.
*   **index**: Integer, index of layer.

**Returns**

A layer instance.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L426)

### `get_quantization_layer_structure` method

```
Model.get_quantization_layer_structure(mode=None)
```

Returns the quantization structure for the model.

This method is intended to be overridden by model authors to provide topology information required for structure-aware quantization modes like 'gptq'.

**Arguments**

*   **mode**: The quantization mode.

**Returns**

*   **A dictionary describing the topology, e.g.**:
*    __ `{'pre_block_layers'__: [list], 'sequential_blocks': [list]}` or `None` if the mode does not require structure or is not supported. `'pre_block_layers'` is a list of layers that the inputs should be passed through, before being passed to the sequential blocks. For example, inputs to an LLM must first be passed through an embedding layer, followed by the transformer.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L856)

### `get_state_tree` method

```
Model.get_state_tree(value_format="backend_tensor")
```

Retrieves tree-like structure of model variables.

This method allows retrieval of different model variables (trainable, non-trainable, optimizer, and metrics). The variables are returned in a nested dictionary format, where the keys correspond to the variable names and the values are the nested representations of the variables.

**Returns**

*   **dict**: A dictionary containing the nested representations of the requested variables. The keys are the variable names, and the values are the corresponding nested dictionaries.
*   **value_format**: One of `"backend_tensor"`, `"numpy_array"`. The kind of array to return as the leaves of the nested state tree.

**Example**

```
model = keras.Sequential([
    keras.Input(shape=(1,), name="my_input"),
    keras.layers.Dense(1, activation="sigmoid", name="my_dense"),
], name="my_sequential")
model.compile(optimizer="adam", loss="mse", metrics=["mae"])
model.fit(np.array([[1.0]]), np.array([[1.0]]))
state_tree = model.get_state_tree()
```

The `state_tree` dictionary returned looks like:

```
{
    'metrics_variables': {
        'loss': {
            'count': ...,
            'total': ...,
        },
        'mean_absolute_error': {
            'count': ...,
            'total': ...,
        }
    },
    'trainable_variables': {
        'my_sequential': {
            'my_dense': {
                'bias': ...,
                'kernel': ...,
            }
        }
    },
    'non_trainable_variables': {},
    'optimizer_variables': {
        'adam': {
                'iteration': ...,
                'learning_rate': ...,
                'my_sequential_my_dense_bias_momentum': ...,
                'my_sequential_my_dense_bias_velocity': ...,
                'my_sequential_my_dense_kernel_momentum': ...,
                'my_sequential_my_dense_kernel_velocity': ...,
            }
        }
    }
}
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L969)

### `set_state_tree` method

```
Model.set_state_tree(state_tree)
```

Assigns values to variables of the model.

This method takes a dictionary of nested variable values, which represents the state tree of the model, and assigns them to the corresponding variables of the model. The dictionary keys represent the variable names (e.g., `'trainable_variables'`, `'optimizer_variables'`), and the values are nested dictionaries containing the variable paths and their corresponding values.

**Arguments**

*   **state_tree**: A dictionary representing the state tree of the model. The keys are the variable names, and the values are nested dictionaries representing the variable paths and their values.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/models/model.py#L449)

### `quantize` method

```
Model.quantize(mode=None, config=None, filters=None, **kwargs)
```

Quantize the weights of the model.

Note that the model must be built first before calling this method. `quantize` will recursively call `quantize(...)` in all layers and will be skipped if the layer doesn't implement the function.

This method can be called by passing a `mode` string, which uses the default configuration for that mode. Alternatively, a `config` object can be passed to customize the behavior of the quantization (e.g. to use specific quantizers for weights or activations).

**Arguments**

*   **mode**: The mode of the quantization. Supported modes are: `"int8"`, `"int4"`, `"float8"`, `"gptq"`. This is optional if `config` is provided.
*   **config**: The configuration object specifying additional quantization options. This argument allows to configure the weight and activation quantizers. be an instance of [`keras.quantizers.QuantizationConfig`](https://keras.io/api/quantizers/quantizer_classes#quantizationconfig-class).
*   **filters**: Optional filters to apply to the quantization. Can be a regex string, a list of regex strings, or a callable. Only the layers which match the filter conditions will be quantized.
*   ****kwargs**: Additional keyword arguments.

**Example**

Quantize a model to int8 with default configuration:

```
# Build the model
model = keras.Sequential([
    keras.Input(shape=(10,)),
    keras.layers.Dense(10),
])
model.build((None, 10))

# Quantize with default int8 config
model.quantize("int8")
```

Quantize a model to int8 with a custom configuration:

```
from keras.quantizers import Int8QuantizationConfig
from keras.quantizers import AbsMaxQuantizer

# Build the model
model = keras.Sequential([
    keras.Input(shape=(10,)),
    keras.layers.Dense(10),
])
model.build((None, 10))

# Create a custom config
config = Int8QuantizationConfig(
    weight_quantizer=AbsMaxQuantizer(
        axis=0,
        value_range=(-127, 127)
    ),
    activation_quantizer=AbsMaxQuantizer(
        axis=-1,
        value_range=(-127, 127)
    ),
)

# Quantize with custom config
model.quantize(config=config)
```

* * *
