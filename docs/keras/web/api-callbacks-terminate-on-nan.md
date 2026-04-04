# Source: https://keras.io/api/callbacks/terminate_on_nan

Title: Keras documentation: TerminateOnNaN

URL Source: https://keras.io/api/callbacks/terminate_on_nan

Markdown Content:
TerminateOnNaN
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

►[Keras 3 API documentation](https://keras.io/api/) / [Callbacks API](https://keras.io/api/callbacks/) / TerminateOnNaN 

TerminateOnNaN
==============

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/terminate_on_nan.py#L8)

### `TerminateOnNaN` class

```
keras.callbacks.TerminateOnNaN(raise_error: bool = False)
```

Callback that terminates training when a NaN loss is encountered.

This callback monitors the loss value during training and terminates training when a NaN or Inf loss is detected. By default, training is stopped gracefully by setting `model.stop_training = True`, which triggers all callback cleanup methods including `on_train_end()`.

Alternatively, you can use `raise_error=True` to immediately raise a RuntimeError when NaN/Inf is detected. This raise_error termination prevents `on_train_end()` from being called on other callbacks, which is useful for preserving backup states or preventing unintended cleanup when training fails.

**Arguments**

*   **raise_error**: Boolean, default False. If False, uses graceful stop via `model.stop_training = True`. If True, immediately raises RuntimeError on NaN/Inf loss, bypassing callback cleanup methods.

**Example**

```
# Graceful termination (default)
callback = keras.callbacks.TerminateOnNaN()
model.fit(x, y, callbacks=[callback])

# raise_error termination (strict failure)
callback = keras.callbacks.TerminateOnNaN(raise_error=True)
model.fit(x, y, callbacks=[callback])
```

* * *

[TerminateOnNaN](https://keras.io/api/callbacks/terminate_on_nan#terminateonnan)

[`TerminateOnNaN` class](https://keras.io/api/callbacks/terminate_on_nan#terminateonnan-class)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
