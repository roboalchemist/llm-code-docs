# Source: https://keras.io/api/ops/math/

Title: Keras documentation: Math ops

URL Source: https://keras.io/api/ops/math/

Markdown Content:
Math ops
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[The Operation class](https://keras.io/api/ops/operation/)[NumPy ops](https://keras.io/api/ops/numpy/)[NN ops](https://keras.io/api/ops/nn/)[Linear algebra ops](https://keras.io/api/ops/linalg/)[Core ops](https://keras.io/api/ops/core/)[Image ops](https://keras.io/api/ops/image/)[FFT ops](https://keras.io/api/ops/fft/)[Einops ops](https://keras.io/api/ops/einops/)[Math ops](https://keras.io/api/ops/math/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[The Operation class](https://keras.io/api/ops/operation/)[NumPy ops](https://keras.io/api/ops/numpy/)[NN ops](https://keras.io/api/ops/nn/)[Linear algebra ops](https://keras.io/api/ops/linalg/)[Core ops](https://keras.io/api/ops/core/)[Image ops](https://keras.io/api/ops/image/)[FFT ops](https://keras.io/api/ops/fft/)[Einops ops](https://keras.io/api/ops/einops/)[Math ops](https://keras.io/api/ops/math/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Ops API](https://keras.io/api/ops/) / Math ops 

Math ops
========

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/math.py#L1064)

### `view_as_complex` function

Copied!

```
keras.ops.view_as_complex(x)
```

Converts a real tensor with shape `(..., 2)` to a complex tensor, where the last dimension represents the real and imaginary components of a complex tensor.

**Arguments**

*   **x**: A real tensor with last dimension of size 2.

**Returns**

*   __A complex tensor with shape `x.shape[__:-1]`.

**Example**

Copied!

```
```python
>>> import numpy as np
>>> from keras import ops
```

Copied!

```
>>> real_imag = np.array([[1.0, 2.0], [3.0, 4.0]])
>>> complex_tensor = ops.view_as_complex(real_imag)
>>> complex_tensor
array([1.+2.j, 3.+4.j])
```

Copied!

```
----

<span style="float:right;">[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/ops/math.py#L1105)</span>

### `view_as_real` function

```python
keras.ops.view_as_real(x)
```

Converts a complex tensor to a real tensor with shape `(..., 2)`, where the last dimension represents the real and imaginary components.

**Arguments**

*   **x**: A complex tensor.

**Returns**

A real tensor where the last dimension contains the real and imaginary parts.

**Example**

Copied!

```
```python
>>> import numpy as np
>>> from keras import ops
```

Copied!

```
>>> complex_tensor = np.array([1 + 2j, 3 + 4j])
>>> real = ops.view_as_real(complex_tensor)
>>> real
array([[1., 2.],
       [3., 4.]])
```

```

* * *

[Math ops](https://keras.io/api/ops/math/#math-ops)

[`view_as_complex` function](https://keras.io/api/ops/math/#viewascomplex-function)

[`view_as_real` function](https://keras.io/api/ops/math/#viewasreal-function)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
