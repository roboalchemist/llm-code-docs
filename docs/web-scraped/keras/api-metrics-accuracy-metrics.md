# Source: https://keras.io/api/metrics/accuracy_metrics

Title: Keras documentation: Accuracy metrics

URL Source: https://keras.io/api/metrics/accuracy_metrics

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L15)

### `Accuracy` class

```
keras.metrics.Accuracy(name="accuracy", dtype=None)
```

Calculates how often predictions equal labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Examples**

```
>>> m = keras.metrics.Accuracy()
>>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]])
>>> m.result()
0.75
```

```
>>> m.reset_state()
>>> m.update_state([[1], [2], [3], [4]], [[0], [2], [3], [4]],
...                sample_weight=[1, 1, 0, 0])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=[keras.metrics.Accuracy()])
```

**Guides and examples using `Accuracy`**

*   [Event classification for payment card fraud detection](https://keras.io/examples/timeseries/event_classification_for_payment_card_fraud_detection/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L72)

### `BinaryAccuracy` class

```
keras.metrics.BinaryAccuracy(name="binary_accuracy", dtype=None, threshold=0.5)
```

Calculates how often predictions match binary labels.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `binary accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **threshold**: (Optional) Float representing the threshold for deciding whether prediction values are 1 or 0.

**Example**

```
>>> m = keras.metrics.BinaryAccuracy()
>>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]])
>>> m.result()
0.75
```

```
>>> m.reset_state()
>>> m.update_state([[1], [1], [0], [0]], [[0.98], [1], [0], [0.6]],
...                sample_weight=[1, 0, 0, 1])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='binary_crossentropy',
              metrics=[keras.metrics.BinaryAccuracy()])
```

**Guides and examples using `BinaryAccuracy`**

*   [Transfer learning & fine-tuning](https://keras.io/guides/transfer_learning/)
*   [Image classification from scratch](https://keras.io/examples/vision/image_classification_from_scratch/)
*   [Pneumonia Classification on TPU](https://keras.io/examples/vision/xray_classification_with_tpus/)
*   [Review Classification using Active Learning](https://keras.io/examples/nlp/active_learning_review_classification/)
*   [Classification with Gated Residual and Variable Selection Networks](https://keras.io/examples/structured_data/classification_with_grn_and_vsn/)
*   [Structured data learning with TabTransformer](https://keras.io/examples/structured_data/tabtransformer/)
*   [Data-efficient GANs with Adaptive Discriminator Augmentation](https://keras.io/examples/generative/gan_ada/)
*   [Endpoint layer pattern](https://keras.io/examples/keras_recipes/endpoint_layer_pattern/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L160)

### `CategoricalAccuracy` class

```
keras.metrics.CategoricalAccuracy(name="categorical_accuracy", dtype=None)
```

Calculates how often predictions match one-hot labels.

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

`y_pred` and `y_true` should be passed in as vectors of probabilities, rather than as labels. If necessary, use `ops.one_hot` to expand `y_true` as a vector.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.CategoricalAccuracy()
>>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8],
...                 [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[0, 0, 1], [0, 1, 0]], [[0.1, 0.9, 0.8],
...                 [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=[keras.metrics.CategoricalAccuracy()])
```

**Guides and examples using `CategoricalAccuracy`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Writing a custom training loop in JAX](https://keras.io/guides/writing_a_custom_training_loop_in_jax/)
*   [Writing a custom training loop in PyTorch](https://keras.io/guides/writing_a_custom_training_loop_in_torch/)
*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)
*   [Image classification with EANet (External Attention Transformer)](https://keras.io/examples/vision/eanet/)
*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
*   [Distilling Vision Transformers](https://keras.io/examples/vision/deit/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L249)

### `SparseCategoricalAccuracy` class

```
keras.metrics.SparseCategoricalAccuracy(
    name="sparse_categorical_accuracy", dtype=None
)
```

Calculates how often predictions match integer labels.

```
acc = np.dot(sample_weight, np.equal(y_true, np.argmax(y_pred, axis=1))
```

You can provide logits of classes as `y_pred`, since argmax of logits and probabilities are same.

This metric creates two local variables, `total` and `count` that are used to compute the frequency with which `y_pred` matches `y_true`. This frequency is ultimately returned as `sparse categorical accuracy`: an idempotent operation that simply divides `total` by `count`.

If `sample_weight` is `None`, weights default to 1. Use `sample_weight` of 0 to mask values.

**Arguments**

*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.SparseCategoricalAccuracy()
>>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[2], [1]], [[0.1, 0.6, 0.3], [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=[keras.metrics.SparseCategoricalAccuracy()])
```

**Guides and examples using `SparseCategoricalAccuracy`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Writing a custom training loop in TensorFlow](https://keras.io/guides/writing_a_custom_training_loop_in_tensorflow/)
*   [Distributed training with TensorFlow](https://keras.io/guides/distributed_training_with_tensorflow/)
*   [Image classification with Vision Transformer](https://keras.io/examples/vision/image_classification_with_vision_transformer/)
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)
*   [Image classification with Perceiver](https://keras.io/examples/vision/perceiver_image_classification/)
*   [Semi-supervised image classification using contrastive pretraining with SimCLR](https://keras.io/examples/vision/semisupervised_simclr/)
*   [Train a Vision Transformer on small datasets](https://keras.io/examples/vision/vit_small_ds/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L333)

### `TopKCategoricalAccuracy` class

```
keras.metrics.TopKCategoricalAccuracy(
    k=5, name="top_k_categorical_accuracy", dtype=None
)
```

Computes how often targets are in the top `K` predictions.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.

**Example**

```
>>> m = keras.metrics.TopKCategoricalAccuracy(k=1)
>>> m.update_state([[0, 0, 1], [0, 1, 0]],
...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([[0, 0, 1], [0, 1, 0]],
...                [[0.1, 0.9, 0.8], [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='categorical_crossentropy',
              metrics=[keras.metrics.TopKCategoricalAccuracy()])
```

**Guides and examples using `TopKCategoricalAccuracy`**

*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)
*   [Image classification with EANet (External Attention Transformer)](https://keras.io/examples/vision/eanet/)
*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
*   [Electroencephalogram Signal Classification for action identification](https://keras.io/examples/timeseries/eeg_signal_classification/)

* * *

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/metrics/accuracy_metrics.py#L439)

### `SparseTopKCategoricalAccuracy` class

```
keras.metrics.SparseTopKCategoricalAccuracy(
    k=5, name="sparse_top_k_categorical_accuracy", dtype=None, from_sorted_ids=False
)
```

Computes how often integer targets are in the top `K` predictions.

By default, the arguments expected by `update_state()` are: - `y_true`: a tensor of shape `(batch_size)` representing indices of true categories. - `y_pred`: a tensor of shape `(batch_size, num_categories)` containing the scores for each sample for all possible categories.

With `from_sorted_ids=True`, the arguments expected by `update_state` are: - `y_true`: a tensor of shape `(batch_size)` representing indices or IDs of true categories. - `y_pred`: a tensor of shape `(batch_size, N)` containing the indices or IDs of the top `N` categories sorted in order from highest score to lowest score. `N` must be greater or equal to `k`.

The `from_sorted_ids=True` option can be more efficient when the set of categories is very large and the model has an optimized way to retrieve the top ones either without scoring or without maintaining the scores for all the possible categories.

**Arguments**

*   **k**: (Optional) Number of top elements to look at for computing accuracy. Defaults to `5`.
*   **name**: (Optional) string name of the metric instance.
*   **dtype**: (Optional) data type of the metric result.
*   **from_sorted_ids**: (Optional) When `False`, the default, the tensor passed in `y_pred` contains the unsorted scores of all possible categories. When `True`, `y_pred` contains a the indices or IDs for the top categories.

**Example**

```
>>> m = keras.metrics.SparseTopKCategoricalAccuracy(k=1)
>>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]])
>>> m.result()
0.5
```

```
>>> m.reset_state()
>>> m.update_state([2, 1], [[0.1, 0.9, 0.8], [0.05, 0.95, 0]],
...                sample_weight=[0.7, 0.3])
>>> m.result()
0.3
```

```
>>> m = keras.metrics.SparseTopKCategoricalAccuracy(k=1,
...                                                from_sorted_ids=True)
>>> m.update_state([2, 1], [[1, 0, 3], [1, 2, 3]])
>>> m.result()
0.5
```

Usage with `compile()` API:

```
model.compile(optimizer='sgd',
              loss='sparse_categorical_crossentropy',
              metrics=[keras.metrics.SparseTopKCategoricalAccuracy()])
```

**Guides and examples using `SparseTopKCategoricalAccuracy`**

*   [Image classification with Vision Transformer](https://keras.io/examples/vision/image_classification_with_vision_transformer/)
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)
*   [Image classification with Perceiver](https://keras.io/examples/vision/perceiver_image_classification/)
*   [Train a Vision Transformer on small datasets](https://keras.io/examples/vision/vit_small_ds/)
*   [A Vision Transformer without Attention](https://keras.io/examples/vision/shiftvit/)
*   [Video Vision Transformer](https://keras.io/examples/vision/vivit/)
*   [Learning to tokenize in Vision Transformers](https://keras.io/examples/vision/token_learner/)
*   [Augmenting convnets with aggregated attention](https://keras.io/examples/vision/patch_convnet/)

* * *
