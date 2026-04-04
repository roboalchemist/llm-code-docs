# Source: https://keras.io/api/layers/activations

Title: Keras documentation: Layer activation functions

URL Source: https://keras.io/api/layers/activations

Markdown Content:
Usage of activations
--------------------

Activations can either be used through an `Activation` layer, or through the `activation` argument supported by all forward layers:

```
model.add(layers.Dense(64, activation=activations.relu))
```

This is equivalent to:

```
from keras import layers
from keras import activations

model.add(layers.Dense(64))
model.add(layers.Activation(activations.relu))
```

All built-in activations may also be passed via their string identifier:

```
model.add(layers.Dense(64, activation='relu'))
```

* * *

Available activations
---------------------

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L362)

### `celu` function

```
keras.activations.celu(x, alpha=1.0)
```

Continuously Differentiable Exponential Linear Unit.

The CeLU activation function is defined as:

`celu(x) = alpha * (exp(x / alpha) - 1) for x < 0`,`celu(x) = x for x >= 0`.

where `alpha` is a scaling parameter that controls the activation's shape.

**Arguments**

*   **x**: Input tensor.
*   **alpha**: The α value for the CeLU formulation. Defaults to `1.0`.

**Reference**

*   [Barron, J. T., 2017](https://arxiv.org/abs/1704.07483)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L170)

### `elu` function

```
keras.activations.elu(x, alpha=1.0)
```

Exponential Linear Unit.

The exponential linear unit (ELU) with `alpha > 0` is defined as:

*   `x` if `x > 0`
*   alpha * `exp(x) - 1` if `x < 0`

ELUs have negative values which pushes the mean of the activations closer to zero.

Mean activations that are closer to zero enable faster learning as they bring the gradient closer to the natural gradient. ELUs saturate to a negative value when the argument gets smaller. Saturation means a small derivative which decreases the variation and the information that is propagated to the next layer.

**Arguments**

*   **x**: Input tensor.
*   **alpha**: A scalar, slope of positive section. Defaults to `1.0`.

**Reference**

*   [Clevert et al., 2016](https://arxiv.org/abs/1511.07289)

**Guides and examples using `elu`**

*   [Approximating non-Function Mappings with Mixture Density Networks](https://keras.io/examples/keras_recipes/approximating_non_function_mappings/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L509)

### `exponential` function

```
keras.activations.exponential(x)
```

Exponential activation function.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L339)

### `gelu` function

```
keras.activations.gelu(x, approximate=False)
```

Gaussian error linear unit (GELU) activation function.

The Gaussian error linear unit (GELU) is defined as:

`gelu(x) = x * P(X <= x)` where `P(X) ~ N(0, 1)`, i.e. `gelu(x) = 0.5 * x * (1 + erf(x / sqrt(2)))`.

GELU weights inputs by their value, rather than gating inputs by their sign as in ReLU.

**Arguments**

*   **x**: Input tensor.
*   **approximate**: A `bool`, whether to enable approximation.

**Reference**

*   [Hendrycks et al., 2016](https://arxiv.org/abs/1606.08415)

**Guides and examples using `gelu`**

*   [Image classification with Vision Transformer](https://keras.io/examples/vision/image_classification_with_vision_transformer/)
*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
*   [Object detection with Vision Transformers](https://keras.io/examples/vision/object_detection_using_vision_transformer/)
*   [Video Classification with Transformers](https://keras.io/examples/vision/video_transformers/)
*   [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L383)

### `glu` function

```
keras.activations.glu(x, axis=-1)
```

Gated Linear Unit (GLU) activation function.

The GLU activation function is defined as:

`glu(x) = a * sigmoid(b)`,

where `x` is split into two equal parts `a` and `b` along the given axis.

**Arguments**

*   **x**: Input tensor.
*   **axis**: The axis along which to split the input tensor. Defaults to `-1`.

**Reference**

*   [Dauphin et al., 2017](https://arxiv.org/abs/1612.08083)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L447)

### `hard_shrink` function

```
keras.activations.hard_shrink(x, threshold=0.5)
```

Hard Shrink activation function.

It is defined as:

`hard_shrink(x) = x` if `|x| > threshold`, `hard_shrink(x) = 0` otherwise.

**Arguments**

*   **x**: Input tensor.
*   **threshold**: Threshold value. Defaults to 0.5.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L519)

### `hard_sigmoid` function

```
keras.activations.hard_sigmoid(x)
```

Hard sigmoid activation function.

The hard sigmoid activation is defined as:

*   `0` if `if x <= -3`
*   `1` if `x >= 3`
*   `(x/6) + 0.5` if `-3 < x < 3`

It's a faster, piecewise linear approximation of the sigmoid activation.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [Wikipedia "Hard sigmoid"](https://en.wikipedia.org/wiki/Hard_sigmoid)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L576)

### `hard_silu` function

```
keras.activations.hard_silu(x)
```

Hard SiLU activation function, also known as Hard Swish.

It is defined as:

*   `0` if `if x < -3`
*   `x` if `x > 3`
*   `x * (x + 3) / 6` if `-3 <= x <= 3`

It's a faster, piecewise linear approximation of the silu activation.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [A Howard, 2019](https://arxiv.org/abs/1905.02244)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L576)

### `hard_silu` function

```
keras.activations.hard_swish(x)
```

Hard SiLU activation function, also known as Hard Swish.

It is defined as:

*   `0` if `if x < -3`
*   `x` if `x > 3`
*   `x * (x + 3) / 6` if `-3 <= x <= 3`

It's a faster, piecewise linear approximation of the silu activation.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [A Howard, 2019](https://arxiv.org/abs/1905.02244)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L432)

### `hard_tanh` function

```
keras.activations.hard_tanh(x)
```

HardTanh activation function.

It is defined as: `hard_tanh(x) = -1 for x < -1`, `hard_tanh(x) = x for -1 <= x <= 1`, `hard_tanh(x) = 1 for x > 1`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L113)

### `leaky_relu` function

```
keras.activations.leaky_relu(x, negative_slope=0.2)
```

Leaky relu activation function.

**Arguments**

*   **x**: Input tensor.
*   **negative_slope**: A `float` that controls the slope for values lower than the threshold.

**Guides and examples using `leaky_relu`**

*   [GauGAN for conditional image generation](https://keras.io/examples/generative/gaugan/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L599)

### `linear` function

```
keras.activations.linear(x)
```

Linear activation function (pass-through).

A "linear" activation is an identity function: it returns the input, unmodified.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L542)

### `log_sigmoid` function

```
keras.activations.log_sigmoid(x)
```

Logarithm of the sigmoid activation function.

It is defined as `f(x) = log(1 / (1 + exp(-x)))`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L647)

### `log_softmax` function

```
keras.activations.log_softmax(x, axis=-1)
```

Log-Softmax activation function.

Each input vector is handled independently. The `axis` argument sets which axis of the input the function is applied along.

**Arguments**

*   **x**: Input tensor.
*   **axis**: Integer, axis along which the softmax is applied.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L624)

### `mish` function

```
keras.activations.mish(x)
```

Mish activation function.

It is defined as:

`mish(x) = x * tanh(softplus(x))`

where `softplus` is defined as:

`softplus(x) = log(exp(x) + 1)`

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [Misra, 2019](https://arxiv.org/abs/1908.08681)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L6)

### `relu` function

```
keras.activations.relu(x, negative_slope=0.0, max_value=None, threshold=0.0)
```

Applies the rectified linear unit activation function.

With default values, this returns the standard ReLU activation: `max(x, 0)`, the element-wise maximum of 0 and the input tensor.

Modifying default parameters allows you to use non-zero thresholds, change the max value of the activation, and to use a non-zero multiple of the input for values below the threshold.

**Examples**

```
>>> x = [-10, -5, 0.0, 5, 10]
>>> keras.activations.relu(x)
[ 0.,  0.,  0.,  5., 10.]
>>> keras.activations.relu(x, negative_slope=0.5)
[-5. , -2.5,  0. ,  5. , 10. ]
>>> keras.activations.relu(x, max_value=5.)
[0., 0., 0., 5., 5.]
>>> keras.activations.relu(x, threshold=5.)
[-0., -0.,  0.,  0., 10.]
```

**Arguments**

*   **x**: Input tensor.
*   **negative_slope**: A `float` that controls the slope for values lower than the threshold.
*   **max_value**: A `float` that sets the saturation threshold (the largest value the function will return).
*   **threshold**: A `float` giving the threshold value of the activation function below which values will be damped or set to zero.

**Returns**

A tensor with the same shape and dtype as input `x`.

**Guides and examples using `relu`**

*   [Making new layers & models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L125)

### `relu6` function

```
keras.activations.relu6(x)
```

Relu6 activation function.

It's the ReLU function, but truncated to a maximum value of 6.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L199)

### `selu` function

```
keras.activations.selu(x)
```

Scaled Exponential Linear Unit (SELU).

The Scaled Exponential Linear Unit (SELU) activation function is defined as:

*   `scale * x` if `x > 0`
*   `scale * alpha * (exp(x) - 1)` if `x < 0`

where `alpha` and `scale` are pre-defined constants (`alpha=1.67326324` and `scale=1.05070098`).

Basically, the SELU activation function multiplies `scale` (> 1) with the output of the [`keras.activations.elu`](https://keras.io/api/layers/activations#elu-function) function to ensure a slope larger than one for positive inputs.

The values of `alpha` and `scale` are chosen so that the mean and variance of the inputs are preserved between two consecutive layers as long as the weights are initialized correctly (see [`keras.initializers.LecunNormal`](https://keras.io/api/layers/initializers#lecunnormal-class) initializer) and the number of input units is "large enough" (see reference paper for more information).

**Arguments**

*   **x**: Input tensor.

Notes:

*   To be used together with the [`keras.initializers.LecunNormal`](https://keras.io/api/layers/initializers#lecunnormal-class) initializer.
*   To be used together with the dropout variant [`keras.layers.AlphaDropout`](https://keras.io/api/layers/regularization_layers/alpha_dropout#alphadropout-class) (rather than regular dropout).

**Reference**

*   [Klambauer et al., 2017](https://arxiv.org/abs/1706.02515)

**Guides and examples using `selu`**

*   [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L482)

### `sigmoid` function

```
keras.activations.sigmoid(x)
```

Sigmoid activation function.

It is defined as: `sigmoid(x) = 1 / (1 + exp(-x))`.

For small values (<-5), `sigmoid` returns a value close to zero, and for large values (>5) the result of the function gets close to 1.

Sigmoid is equivalent to a 2-element softmax, where the second element is assumed to be zero. The sigmoid function always returns a value between 0 and 1.

**Arguments**

*   **x**: Input tensor.

**Guides and examples using `sigmoid`**

*   [Low-light image enhancement using MIRNet](https://keras.io/examples/vision/mirnet/)
*   [Memory-efficient embeddings for recommendation systems](https://keras.io/examples/keras_recipes/memory_efficient_embeddings/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L298)

### `silu` function

```
keras.activations.silu(x)
```

Swish (or Silu) activation function.

It is defined as: `swish(x) = x * sigmoid(x)`.

The Swish (or Silu) activation function is a smooth, non-monotonic function that is unbounded above and bounded below.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [Ramachandran et al., 2017](https://arxiv.org/abs/1710.05941)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L137)

### `softmax` function

```
keras.activations.softmax(x, axis=-1)
```

Softmax converts a vector of values to a probability distribution.

The elements of the output vector are in range `[0, 1]` and sum to 1.

Each input vector is handled independently. The `axis` argument sets which axis of the input the function is applied along.

Softmax is often used as the activation for the last layer of a classification network because the result could be interpreted as a probability distribution.

The softmax of each vector x is computed as `exp(x) / sum(exp(x))`.

The input values in are the log-odds of the resulting probability.

**Arguments**

*   **x**: Input tensor.
*   **axis**: Integer, axis along which the softmax is applied.

**Guides and examples using `softmax`**

*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
*   [Text classification with Switch Transformer](https://keras.io/examples/nlp/text_classification_with_switch_transformer/)
*   [Classification with Neural Decision Forests](https://keras.io/examples/structured_data/deep_neural_decision_forests/)
*   [Text generation with a miniature GPT](https://keras.io/examples/generative/text_generation_with_miniature_gpt/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L263)

### `soft_shrink` function

```
keras.activations.soft_shrink(x, threshold=0.5)
```

Soft Shrink activation function.

It is defined as:

`soft_shrink(x) = x - threshold` if `x > threshold`, `soft_shrink(x) = x + threshold` if `x < -threshold`, `soft_shrink(x) = 0` otherwise.

**Arguments**

*   **x**: Input tensor.
*   **threshold**: Threshold value. Defaults to 0.5.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L239)

### `softplus` function

```
keras.activations.softplus(x)
```

Softplus activation function.

It is defined as: `softplus(x) = log(exp(x) + 1)`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L251)

### `softsign` function

```
keras.activations.softsign(x)
```

Softsign activation function.

Softsign is defined as: `softsign(x) = x / (abs(x) + 1)`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L281)

### `sparse_plus` function

```
keras.activations.sparse_plus(x)
```

SparsePlus activation function.

SparsePlus is defined as:

`sparse_plus(x) = 0` for `x <= -1`. `sparse_plus(x) = (1/4) * (x + 1)^2` for `-1 < x < 1`. `sparse_plus(x) = x` for `x >= 1`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L555)

### `sparse_sigmoid` function

```
keras.activations.sparse_sigmoid(x)
```

Sparse sigmoid activation function.

It is defined as

`f(x) = 0` for `x <= -1`, `f(x) = 0.5 * (x + 1)` for `-1 < x < 1`, `f(x) = 1` for `x >= 1`.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [M. Blondel, A. F. T. Martins, V. Niculae, 2019](https://arxiv.org/pdf/1901.02324)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L662)

### `sparsemax` function

```
keras.activations.sparsemax(x, axis=-1)
```

Sparsemax activation function.

For each batch `i`, and class `j`, sparsemax activation function is defined as:

`sparsemax(x)[i, j] = max(x[i, j] - τ(x[i, :]), 0).`

**Arguments**

*   **x**: Input tensor.
*   **axis**: `int`, axis along which the sparsemax operation is applied.

**Returns**

A tensor, output of sparsemax transformation. Has the same type and shape as `x`.

**Reference**

*   [Martins et.al., 2016](https://arxiv.org/abs/1602.02068)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L318)

### `squareplus` function

```
keras.activations.squareplus(x, b=4)
```

Squareplus activation function.

The Squareplus activation function is defined as:

`f(x) = (x + sqrt(x^2 + b)) / 2`

Where `b` is a smoothness parameter.

**Arguments**

*   **x**: Input tensor.
*   **b**: Smoothness parameter. Defaults to 4.

**Reference**

*   [Ramachandran et al., 2021](https://arxiv.org/abs/2112.11687)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L298)

### `silu` function

```
keras.activations.swish(x)
```

Swish (or Silu) activation function.

It is defined as: `swish(x) = x * sigmoid(x)`.

The Swish (or Silu) activation function is a smooth, non-monotonic function that is unbounded above and bounded below.

**Arguments**

*   **x**: Input tensor.

**Reference**

*   [Ramachandran et al., 2017](https://arxiv.org/abs/1710.05941)

**Guides and examples using `swish`**

*   [A mobile-friendly Transformer-based model for image classification](https://keras.io/examples/vision/mobilevit/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L404)

### `tanh` function

```
keras.activations.tanh(x)
```

Hyperbolic tangent activation function.

It is defined as: `tanh(x) = sinh(x) / cosh(x)`, i.e. `tanh(x) = ((exp(x) - exp(-x)) / (exp(x) + exp(-x)))`.

**Arguments**

*   **x**: Input tensor.

**Guides and examples using `tanh`**

*   [GauGAN for conditional image generation](https://keras.io/examples/generative/gaugan/)
*   [Proximal Policy Optimization](https://keras.io/examples/rl/ppo_cartpole/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L418)

### `tanh_shrink` function

```
keras.activations.tanh_shrink(x)
```

Tanh shrink activation function.

It is defined as:

`f(x) = x - tanh(x)`.

**Arguments**

*   **x**: Input tensor.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/activations/activations.py#L464)

### `threshold` function

```
keras.activations.threshold(x, threshold, default_value)
```

Threshold activation function.

It is defined as:

`threshold(x) = x` if `x > threshold`, `threshold(x) = default_value` otherwise.

**Arguments**

*   **x**: Input tensor.
*   **threshold**: The value that decides when to retain or replace x.
*   **default_value**: Value to assign when `x <= threshold`.

* * *

* * *

Creating custom activations
---------------------------

You can also use a callable as an activation (in this case it should take a tensor and return a tensor of the same shape and dtype):

```
model.add(layers.Dense(64, activation=keras.ops.tanh))
```

* * *

About "advanced activation" layers
----------------------------------

Activations that are more complex than a simple function (eg. learnable activations, which maintain a state) are available as [Advanced Activation layers](https://keras.io/api/layers/activation_layers/).
