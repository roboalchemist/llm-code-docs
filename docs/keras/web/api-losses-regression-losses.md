# Source: https://keras.io/api/losses/regression_losses

Title: Keras documentation: Regression losses

URL Source: https://keras.io/api/losses/regression_losses

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L51)

### `MeanSquaredError` class

```
keras.losses.MeanSquaredError(
    reduction="sum_over_batch_size", name="mean_squared_error", dtype=None
)
```

Computes the mean of squares of errors between labels and predictions.

Formula:

```
loss = mean(square(y_true - y_pred))
```

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Guides and examples using `MeanSquaredError`**

*   [Making new layers & models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing/)
*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Customizing `fit()` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
*   [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
*   [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
*   [Object detection with Vision Transformers](https://keras.io/examples/vision/object_detection_using_vision_transformer/)
*   [3D volumetric rendering with NeRF](https://keras.io/examples/vision/nerf/)
*   [Image Super-Resolution using an Efficient Sub-Pixel CNN](https://keras.io/examples/vision/super_resolution_sub_pixel/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L92)

### `MeanAbsoluteError` class

```
keras.losses.MeanAbsoluteError(
    reduction="sum_over_batch_size", name="mean_absolute_error", dtype=None
)
```

Computes the mean of absolute difference between labels and predictions.

Formula:

```
loss = mean(abs(y_true - y_pred))
```

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Guides and examples using `MeanAbsoluteError`**

*   [CycleGAN](https://keras.io/examples/generative/cyclegan/)
*   [GauGAN for conditional image generation](https://keras.io/examples/generative/gaugan/)
*   [Estimating required sample size for model training](https://keras.io/examples/keras_recipes/sample_size_estimate/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L133)

### `MeanAbsolutePercentageError` class

```
keras.losses.MeanAbsolutePercentageError(
    reduction="sum_over_batch_size", name="mean_absolute_percentage_error", dtype=None
)
```

Computes the mean absolute percentage error between `y_true`&`y_pred`.

Formula:

```
loss = 100 * mean(abs((y_true - y_pred) / y_true))
```

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L177)

### `MeanSquaredLogarithmicError` class

```
keras.losses.MeanSquaredLogarithmicError(
    reduction="sum_over_batch_size", name="mean_squared_logarithmic_error", dtype=None
)
```

Computes the mean squared logarithmic error between `y_true`&`y_pred`.

Formula:

```
loss = mean(square(log(y_true + 1) - log(y_pred + 1)))
```

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L221)

### `CosineSimilarity` class

```
keras.losses.CosineSimilarity(
    axis=-1, reduction="sum_over_batch_size", name="cosine_similarity", dtype=None
)
```

Computes the cosine similarity between `y_true`&`y_pred`.

Note that it is a number between -1 and 1. When it is a negative number between -1 and 0, 0 indicates orthogonality and values closer to -1 indicate greater similarity. This makes it usable as a loss function in a setting where you try to maximize the proximity between predictions and targets. If either `y_true` or `y_pred` is a zero vector, cosine similarity will be 0 regardless of the proximity between predictions and targets.

Formula:

```
loss = -sum(l2_norm(y_true) * l2_norm(y_pred))
```

**Arguments**

*   **axis**: The axis along which the cosine similarity is computed (the features axis). Defaults to `-1`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L276)

### `Huber` class

```
keras.losses.Huber(
    delta=1.0, reduction="sum_over_batch_size", name="huber_loss", dtype=None
)
```

Computes the Huber loss between `y_true`&`y_pred`.

Formula:

```
for x in error:
    if abs(x) <= delta:
        loss.append(0.5 * x^2)
    elif abs(x) > delta:
        loss.append(delta * abs(x) - 0.5 * delta^2)

loss = mean(loss, axis=-1)
```

See: [Huber loss](https://en.wikipedia.org/wiki/Huber_loss).

**Arguments**

*   **delta**: A float, the point where the Huber loss function changes from a quadratic to linear.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Guides and examples using `Huber`**

*   [Actor Critic Method](https://keras.io/examples/rl/actor_critic_cartpole/)
*   [Deep Q-Learning for Atari Breakout](https://keras.io/examples/rl/deep_q_network_breakout/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L331)

### `LogCosh` class

```
keras.losses.LogCosh(reduction="sum_over_batch_size", name="log_cosh", dtype=None)
```

Computes the logarithm of the hyperbolic cosine of the prediction error.

Formula:

```
error = y_pred - y_true
logcosh = mean(log((exp(error) + exp(-error))/2), axis=-1)`
```

where x is the error `y_pred - y_true`.

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L1351)

### `Tversky` class

```
keras.losses.Tversky(
    alpha=0.5,
    beta=0.5,
    reduction="sum_over_batch_size",
    name="tversky",
    axis=None,
    dtype=None,
)
```

Computes the Tversky loss value between `y_true` and `y_pred`.

This loss function is weighted by the alpha and beta coefficients that penalize false positives and false negatives.

With `alpha=0.5` and `beta=0.5`, the loss value becomes equivalent to Dice Loss.

**Arguments**

*   **alpha**: The coefficient controlling incidence of false positives. Defaults to `0.5`.
*   **beta**: The coefficient controlling incidence of false negatives. Defaults to `0.5`.
*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Returns**

Tversky loss value.

**Reference**

*   [Salehi et al., 2017](https://arxiv.org/abs/1706.05721)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/losses/losses.py#L1277)

### `Dice` class

```
keras.losses.Dice(
    reduction="sum_over_batch_size", name="dice", axis=None, dtype=None
)
```

Computes the Dice loss value between `y_true` and `y_pred`.

Formula:

```
loss = 1 - (2 * sum(y_true * y_pred)) / (sum(y_true) + sum(y_pred))
```

**Arguments**

*   **reduction**: Type of reduction to apply to the loss. In almost all cases this should be `"sum_over_batch_size"`. Supported options are `"sum"`, `"sum_over_batch_size"`, `"mean"`, `"mean_with_sample_weight"` or `None`. `"sum"` sums the loss, `"sum_over_batch_size"` and `"mean"` sum the loss and divide by the sample size, and `"mean_with_sample_weight"` sums the loss and divides by the sum of the sample weights. `"none"` and `None` perform no aggregation. Defaults to `"sum_over_batch_size"`.
*   **name**: Optional name for the loss instance.
*   **axis**: Tuple for which dimensions the loss is calculated. Defaults to `None`.
*   **dtype**: The dtype of the loss's computations. Defaults to `None`, which means using `keras.backend.floatx()`. `keras.backend.floatx()` is a `"float32"` unless set to different value (via `keras.backend.set_floatx()`). If a `keras.DTypePolicy` is provided, then the `compute_dtype` will be utilized.

**Returns**

Dice loss value.

**Example**

```
>>> y_true = [[[[1.0], [1.0]], [[0.0], [0.0]]],
...           [[[1.0], [1.0]], [[0.0], [0.0]]]]
>>> y_pred = [[[[0.0], [1.0]], [[0.0], [1.0]]],
...           [[[0.4], [0.0]], [[0.0], [0.9]]]]
>>> axis = (1, 2, 3)
>>> loss = keras.losses.Dice(axis=axis, reduction=None)(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> loss
array([0.5, 0.75757575], shape=(2,), dtype=float32)
```

```
>>> loss = keras.losses.Dice()(y_true, y_pred)
>>> assert loss.shape == ()
>>> loss
array(0.6164384, shape=(), dtype=float32)
```

```
>>> y_true = np.array(y_true)
>>> y_pred = np.array(y_pred)
>>> loss = keras.losses.Dice(axis=axis, reduction=None)(y_true, y_pred)
>>> assert loss.shape == (2,)
>>> loss
array([0.5, 0.75757575], shape=(2,), dtype=float32)
```

* * *
