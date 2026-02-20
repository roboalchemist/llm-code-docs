# Source: https://keras.io/api/layers/constraints

Title: Keras documentation: Layer weight constraints

URL Source: https://keras.io/api/layers/constraints

Markdown Content:
Usage of constraints
--------------------

Classes from the `keras.constraints` module allow setting constraints (eg. non-negativity) on model parameters during training. They are per-variable projection functions applied to the target variable after each gradient update (when using `fit()`).

The exact API will depend on the layer, but the layers `Dense`, `Conv1D`, `Conv2D` and `Conv3D` have a unified API.

These layers expose two keyword arguments:

*   `kernel_constraint` for the main weights matrix
*   `bias_constraint` for the bias.

```
from keras.constraints import max_norm
model.add(Dense(64, kernel_constraint=max_norm(2.)))
```

* * *

Available weight constraints
----------------------------

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/constraints/constraints.py#L80)

### `MaxNorm` class

```
keras.constraints.MaxNorm(max_value=2, axis=0)
```

MaxNorm weight constraint.

Constrains the weights incident to each hidden unit to have a norm less than or equal to a desired value.

Also available via the shortcut function `keras.constraints.max_norm`.

**Arguments**

*   **max_value**: the maximum norm value for the incoming weights.
*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/constraints/constraints.py#L160)

### `MinMaxNorm` class

```
keras.constraints.MinMaxNorm(min_value=0.0, max_value=1.0, rate=1.0, axis=0)
```

MinMaxNorm weight constraint.

Constrains the weights incident to each hidden unit to have the norm between a lower bound and an upper bound.

**Arguments**

*   **min_value**: the minimum norm for the incoming weights.
*   **max_value**: the maximum norm for the incoming weights.
*   **rate**: rate for enforcing the constraint: weights will be rescaled to yield `(1 - rate) * norm + rate * norm.clip(min_value, max_value)`. Effectively, this means that rate=1.0 stands for strict enforcement of the constraint, while rate<1.0 means that weights will be rescaled at each step to slowly move towards a value inside the desired interval.
*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/constraints/constraints.py#L121)

### `NonNeg` class

```
keras.constraints.NonNeg()
```

Constrains the weights to be non-negative.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/constraints/constraints.py#L130)

### `UnitNorm` class

```
keras.constraints.UnitNorm(axis=0)
```

Constrains the weights incident to each hidden unit to have unit norm.

**Arguments**

*   **axis**: integer, axis along which to calculate weight norms. For instance, in a `Dense` layer the weight matrix has shape `(input_dim, output_dim)`, set `axis` to `0` to constrain each weight vector of length `(input_dim,)`. In a `Conv2D` layer with `data_format="channels_last"`, the weight tensor has shape `(rows, cols, input_depth, output_depth)`, set `axis` to `[0, 1, 2]` to constrain the weights of each filter tensor of size `(rows, cols, input_depth)`.

* * *

Creating custom weight constraints
----------------------------------

A weight constraint can be any callable that takes a tensor and returns a tensor with the same shape and dtype. You would typically implement your constraints as subclasses of `keras.constraints.Constraint`.

Here's a simple example: a constraint that forces weight tensors to be centered around a specific value on average.

```
from keras import ops

class CenterAround(keras.constraints.Constraint):
  """Constrains weight tensors to be centered around `ref_value`."""

  def __init__(self, ref_value):
    self.ref_value = ref_value

  def __call__(self, w):
    mean = ops.mean(w)
    return w - mean + self.ref_value

  def get_config(self):
    return {'ref_value': self.ref_value}
```

Optionally, you an also implement the method `get_config` and the class method `from_config` in order to support serialization – just like with any Keras object. Note that we don't have to implement `from_config` in the example above since the constructor arguments of the class the keys in the config returned by `get_config` are the same. In this case, the default `from_config` works fine.
