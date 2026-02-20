# Source: https://keras.io/api/metrics/hinge_metrics

Title: Keras documentation: Hinge metrics for

URL Source: https://keras.io/api/metrics/hinge_metrics

Markdown Content:
Hinge metrics for "maximum-margin" classification
-------------------------------------------------

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/hinge_metrics.py#L8)

### `Hinge` class

```
keras.metrics.Hinge(name="hinge", dtype=None)
```

Computes the hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.Hinge()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
>>> m.result()
1.3
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
...                sample_weight=[1, 0])
>>> m.result()
1.1
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/hinge_metrics.py#L41)

### `SquaredHinge` class

```
keras.metrics.SquaredHinge(name="squared_hinge", dtype=None)
```

Computes the hinge metric between `y_true` and `y_pred`.

`y_true` values are expected to be -1 or 1. If binary (0 or 1) labels are provided we will convert them to -1 or 1.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.SquaredHinge()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
>>> m.result()
1.86
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
...                sample_weight=[1, 0])
>>> m.result()
1.46
```

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/hinge_metrics.py#L74)

### `CategoricalHinge` class

```
keras.metrics.CategoricalHinge(name="categorical_hinge", dtype=None)
```

Computes the categorical hinge metric between `y_true` and `y_pred`.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.CategoricalHinge()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]])
>>> m.result().numpy()
1.4000001
>>> m.reset_state()
>>> m.update_state([[0, 1], [0, 0]], [[0.6, 0.4], [0.4, 0.6]],
...                sample_weight=[1, 0])
>>> m.result()
1.2
```

* * *
