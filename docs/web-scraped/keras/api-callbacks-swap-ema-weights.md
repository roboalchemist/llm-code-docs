# Source: https://keras.io/api/callbacks/swap_ema_weights

Title: Keras documentation: SwapEMAWeights

URL Source: https://keras.io/api/callbacks/swap_ema_weights

Markdown Content:
SwapEMAWeights
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Base Callback class](https://keras.io/api/callbacks/base_callback/)[ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/)[BackupAndRestore](https://keras.io/api/callbacks/backup_and_restore/)[TensorBoard](https://keras.io/api/callbacks/tensorboard/)[EarlyStopping](https://keras.io/api/callbacks/early_stopping/)[LearningRateScheduler](https://keras.io/api/callbacks/learning_rate_scheduler/)[ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/)[RemoteMonitor](https://keras.io/api/callbacks/remote_monitor/)[LambdaCallback](https://keras.io/api/callbacks/lambda_callback/)[TerminateOnNaN](https://keras.io/api/callbacks/terminate_on_nan/)[CSVLogger](https://keras.io/api/callbacks/csv_logger/)[ProgbarLogger](https://keras.io/api/callbacks/progbar_logger/)[SwapEMAWeights](https://keras.io/api/callbacks/swap_ema_weights/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Base Callback class](https://keras.io/api/callbacks/base_callback/)[ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/)[BackupAndRestore](https://keras.io/api/callbacks/backup_and_restore/)[TensorBoard](https://keras.io/api/callbacks/tensorboard/)[EarlyStopping](https://keras.io/api/callbacks/early_stopping/)[LearningRateScheduler](https://keras.io/api/callbacks/learning_rate_scheduler/)[ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/)[RemoteMonitor](https://keras.io/api/callbacks/remote_monitor/)[LambdaCallback](https://keras.io/api/callbacks/lambda_callback/)[TerminateOnNaN](https://keras.io/api/callbacks/terminate_on_nan/)[CSVLogger](https://keras.io/api/callbacks/csv_logger/)[ProgbarLogger](https://keras.io/api/callbacks/progbar_logger/)[SwapEMAWeights](https://keras.io/api/callbacks/swap_ema_weights/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Callbacks API](https://keras.io/api/callbacks/) / SwapEMAWeights 

SwapEMAWeights
==============

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/swap_ema_weights.py#L7)

### `SwapEMAWeights` class

```
keras.callbacks.SwapEMAWeights(swap_on_epoch=False)
```

Swaps model weights and EMA weights before and after evaluation.

This callbacks replaces the model's weight values with the values of the optimizer's EMA weights (the exponential moving average of the past model weights values, implementing "Polyak averaging") before model evaluation, and restores the previous weights after evaluation.

The `SwapEMAWeights` callback is to be used in conjunction with an optimizer that sets `use_ema=True`.

Note that the weights are swapped in-place in order to save memory. The behavior is undefined if you modify the EMA weights or model weights in other callbacks.

**Example**

```
# Remember to set `use_ema=True` in the optimizer
optimizer = SGD(use_ema=True)
model.compile(optimizer=optimizer, loss=..., metrics=...)

# Metrics will be computed with EMA weights
model.fit(X_train, Y_train, callbacks=[SwapEMAWeights()])

# If you want to save model checkpoint with EMA weights, you can set
# `swap_on_epoch=True` and place ModelCheckpoint after SwapEMAWeights.
model.fit(
    X_train,
    Y_train,
    callbacks=[SwapEMAWeights(swap_on_epoch=True), ModelCheckpoint(...)]
)
```

**Arguments**

*   **swap_on_epoch**: whether to perform swapping at `on_epoch_begin()` and `on_epoch_end()`. This is useful if you want to use EMA weights for other callbacks such as `ModelCheckpoint`. Defaults to `False`.

* * *

[SwapEMAWeights](https://keras.io/api/callbacks/swap_ema_weights#swapemaweights)

[`SwapEMAWeights` class](https://keras.io/api/callbacks/swap_ema_weights#swapemaweights-class)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
