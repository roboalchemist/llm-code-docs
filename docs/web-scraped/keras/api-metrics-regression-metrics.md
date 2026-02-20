# Source: https://keras.io/api/metrics/regression_metrics

Title: Keras documentation: Regression metrics

URL Source: https://keras.io/api/metrics/regression_metrics

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L16)

### `MeanSquaredError` class

```
keras.metrics.MeanSquaredError(name="mean_squared_error", dtype=None)
```

Computes the mean squared error between `y_true` and `y_pred`.

Formula:

```
loss = mean(square(y_true - y_pred))
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.MeanSquaredError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.25
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L183)

### `RootMeanSquaredError` class

```
keras.metrics.RootMeanSquaredError(name="root_mean_squared_error", dtype=None)
```

Computes root mean squared error metric between `y_true` and `y_pred`.

Formula:

```
loss = sqrt(mean((y_pred - y_true) ** 2))
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.RootMeanSquaredError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
0.70710677
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.RootMeanSquaredError()])
```

**Guides and examples using `RootMeanSquaredError`**

*   [Recommending movies: ranking](https://keras.io/keras_rs/examples/basic_ranking/)
*   [Multi-task recommenders: retrieval + ranking](https://keras.io/keras_rs/examples/multi_task/)
*   [Ranking with Deep and Cross Networks](https://keras.io/keras_rs/examples/dcn/)
*   [Rank movies with DLRM using KerasRS](https://keras.io/keras_rs/examples/dlrm/)
*   [DistributedEmbedding using TPU SparseCore and JAX](https://keras.io/keras_rs/examples/distributed_embedding_jax/)
*   [DistributedEmbedding using TPU SparseCore and TensorFlow](https://keras.io/keras_rs/examples/distributed_embedding_tf/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L46)

### `MeanAbsoluteError` class

```
keras.metrics.MeanAbsoluteError(name="mean_absolute_error", dtype=None)
```

Computes the mean absolute error between the labels and predictions.

Formula:

```
loss = mean(abs(y_true - y_pred))
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.MeanAbsoluteError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.25
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.MeanAbsoluteError()])
```

**Guides and examples using `MeanAbsoluteError`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Customizing `fit()` with JAX](https://keras.io/guides/custom_train_step_in_jax/)
*   [Customizing `fit()` with TensorFlow](https://keras.io/guides/custom_train_step_in_tensorflow/)
*   [Customizing `fit()` with PyTorch](https://keras.io/guides/custom_train_step_in_torch/)
*   [Highly accurate boundaries segmentation using BASNet](https://keras.io/examples/vision/basnet_segmentation/)
*   [A Transformer-based recommendation system](https://keras.io/examples/structured_data/movielens_recommendations_transformers/)
*   [Memory-efficient embeddings for recommendation systems](https://keras.io/examples/keras_recipes/memory_efficient_embeddings/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L92)

### `MeanAbsolutePercentageError` class

```
keras.metrics.MeanAbsolutePercentageError(
    name="mean_absolute_percentage_error", dtype=None
)
```

Computes mean absolute percentage error between `y_true` and `y_pred`.

Formula:

```
loss = 100 * mean(abs((y_true - y_pred) / y_true))
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.MeanAbsolutePercentageError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
250000000.0
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
500000000.0
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.MeanAbsolutePercentageError()])
```

**Guides and examples using `MeanAbsolutePercentageError`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Writing Keras Models With TensorFlow NumPy](https://keras.io/examples/keras_recipes/tensorflow_numpy_models/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L137)

### `MeanSquaredLogarithmicError` class

```
keras.metrics.MeanSquaredLogarithmicError(
    name="mean_squared_logarithmic_error", dtype=None
)
```

Computes mean squared logarithmic error between `y_true` and `y_pred`.

Formula:

```
loss = mean(square(log(y_true + 1) - log(y_pred + 1)))
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.MeanSquaredLogarithmicError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.12011322
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
0.24022643
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.MeanSquaredLogarithmicError()])
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L249)

### `CosineSimilarity` class

```
keras.metrics.CosineSimilarity(name="cosine_similarity", dtype=None, axis=-1)
```

Computes the cosine similarity between the labels and predictions.

Formula:

```
loss = sum(l2_norm(y_true) * l2_norm(y_pred))
```

See: [Cosine Similarity](https://en.wikipedia.org/wiki/Cosine_similarity). This metric keeps the average cosine similarity between `predictions` and `labels` over a stream of data.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **axis**: (Optional) Defaults to `-1`. The dimension along which the cosine similarity is computed.

**Examples**

```
>>> # l2_norm(y_true) = [[0., 1.], [1./1.414, 1./1.414]]
>>> # l2_norm(y_pred) = [[1., 0.], [1./1.414, 1./1.414]]
>>> # l2_norm(y_true) . l2_norm(y_pred) = [[0., 0.], [0.5, 0.5]]
>>> # result = mean(sum(l2_norm(y_true) . l2_norm(y_pred), axis=1))
>>> #        = ((0. + 0.) +  (0.5 + 0.5)) / 2
>>> m = keras.metrics.CosineSimilarity(axis=1)
>>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]])
>>> m.result()
0.49999997
```

```
>>> m.reset_state()
>>> m.update_state([[0., 1.], [1., 1.]], [[1., 0.], [1., 1.]],
...                sample_weight=[0.3, 0.7])
>>> m.result()
0.6999999
```

Usage with `compile()` API:

```
model.compile(
    optimizer='sgd',
    loss='mse',
    metrics=[keras.metrics.CosineSimilarity(axis=1)])
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L305)

### `LogCoshError` class

```
keras.metrics.LogCoshError(name="logcosh", dtype=None)
```

Computes the logarithm of the hyperbolic cosine of the prediction error.

Formula:

```
error = y_pred - y_true
logcosh = mean(log((exp(error) + exp(-error))/2), axis=-1)
```

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.LogCoshError()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]])
>>> m.result()
0.10844523
```

```
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[1, 1], [0, 0]],
...                sample_weight=[1, 0])
>>> m.result()
0.21689045
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='mse',
              metrics=[keras.metrics.LogCoshError()])
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/regression_metrics.py#L352)

### `R2Score` class

```
keras.metrics.R2Score(
    class_aggregation="uniform_average", num_regressors=0, name="r2_score", dtype=None
)
```

Computes R2 score.

Formula:

```
sum_squares_residuals = sum((y_true - y_pred) ** 2)
sum_squares = sum((y_true - mean(y_true)) ** 2)
R2 = 1 - sum_squares_residuals / sum_squares
```

This is also called the [coefficient of determination](https://en.wikipedia.org/wiki/Coefficient_of_determination).

It indicates how close the fitted regression line is to ground-truth data.

*   The highest score possible is 1.0. It indicates that the predictors perfectly accounts for variation in the target.
*   A score of 0.0 indicates that the predictors do not account for variation in the target.
*   It can also be negative if the model is worse than random.

This metric can also compute the "Adjusted R2" score.

**Arguments**

*   **class_aggregation**: Specifies how to aggregate scores corresponding to different output classes (or target dimensions), i.e. different dimensions on the last axis of the predictions. Equivalent to `multioutput` argument in Scikit-Learn. Should be one of `None` (no aggregation), `"uniform_average"`, `"variance_weighted_average"`.
*   **num_regressors**: Number of independent regressors used ("Adjusted R2" score). 0 is the standard R2 score. Defaults to `0`.
*   **name**: Optional. string name of the metric instance.
*   **dtype**: Optional. data type of the metric result.

**Example**

```
>>> y_true = np.array([[1], [4], [3]], dtype=np.float32)
>>> y_pred = np.array([[2], [4], [4]], dtype=np.float32)
>>> metric = keras.metrics.R2Score()
>>> metric.update_state(y_true, y_pred)
>>> result = metric.result()
>>> result
0.57142854
```

* * *
