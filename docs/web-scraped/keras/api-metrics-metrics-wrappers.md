# Source: https://keras.io/api/metrics/metrics_wrappers

Title: Keras documentation: Metric wrappers and reduction metrics

URL Source: https://keras.io/api/metrics/metrics_wrappers

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/reduction_metrics.py#L161)

### `MeanMetricWrapper` class

```
keras.metrics.MeanMetricWrapper(fn, name=None, dtype=None, **kwargs)
```

Wrap a stateless metric function with the `Mean` metric.

You could use this class to quickly build a mean metric from a function. The function needs to have the signature `fn(y_true, y_pred)` and return a per-sample loss array. `MeanMetricWrapper.result()` will return the average metric value across all samples seen so far.

For example:

```
def mse(y_true, y_pred):
    return (y_true - y_pred) ** 2

mse_metric = MeanMetricWrapper(fn=mse)
```

**Arguments**

*   **fn**: The metric function to wrap, with signature `fn(y_true, y_pred, **kwargs)`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   ****kwargs**: Keyword arguments to pass on to `fn`.

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/reduction_metrics.py#L96)

### `Mean` class

```
keras.metrics.Mean(name="mean", dtype=None)
```

Compute the (weighted) mean of the given values.

For example, if values is `[1, 3, 5, 7]` then the mean is 4. If `sample_weight` was specified as `[1, 1, 0, 0]` then the mean would be 2.

This metric creates two variables, `total` and `count`. The mean value returned is simply `total` divided by `count`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = Mean()
>>> m.update_state([1, 3, 5, 7])
>>> m.result()
4.0
```

```
>>> m.reset_state()
>>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
>>> m.result()
2.0
```

**Guides and examples using `Mean`**

*   [Customizing `fit()` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
*   [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
*   [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
*   [Tune hyperparameters in your custom training loop](https://keras.io/keras_tuner/guides/custom_tuner/)
*   [Semi-supervised image classification using contrastive pretraining with SimCLR](https://keras.io/examples/vision/semisupervised_simclr/)
*   [Using the Forward-Forward Algorithm for Image Classification](https://keras.io/examples/vision/forwardforward/)
*   [Monocular depth estimation](https://keras.io/examples/vision/depth_estimation/)
*   [3D volumetric rendering with NeRF](https://keras.io/examples/vision/nerf/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/reduction_metrics.py#L47)

### `Sum` class

```
keras.metrics.Sum(name="sum", dtype=None)
```

Compute the (weighted) sum of the given values.

For example, if `values` is `[1, 3, 5, 7]` then their sum is 16. If `sample_weight` was specified as `[1, 1, 0, 0]` then the sum would be 4.

This metric creates one variable, `total`. This is ultimately returned as the sum value.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = metrics.Sum()
>>> m.update_state([1, 3, 5, 7])
>>> m.result()
16.0
```

```
>>> m = metrics.Sum()
>>> m.update_state([1, 3, 5, 7], sample_weight=[1, 1, 0, 0])
>>> m.result()
4.0
```

* * *
