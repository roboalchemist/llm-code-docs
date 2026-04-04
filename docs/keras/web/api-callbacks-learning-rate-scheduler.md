# Source: https://keras.io/api/callbacks/learning_rate_scheduler

Title: Keras documentation: LearningRateScheduler

URL Source: https://keras.io/api/callbacks/learning_rate_scheduler

Markdown Content:
LearningRateScheduler
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

►[Keras 3 API documentation](https://keras.io/api/) / [Callbacks API](https://keras.io/api/callbacks/) / LearningRateScheduler 

LearningRateScheduler
=====================

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/learning_rate_scheduler.py#L9)

### `LearningRateScheduler` class

```
keras.callbacks.LearningRateScheduler(schedule, verbose=0)
```

Learning rate scheduler.

At the beginning of every epoch, this callback gets the updated learning rate value from `schedule` function provided at `__init__`, with the current epoch and current learning rate, and applies the updated learning rate on the optimizer.

**Arguments**

*   **schedule**: A function that takes an epoch index (integer, indexed from 0) and current learning rate (float) as inputs and returns a new learning rate as output (float).
*   **verbose**: Integer. 0: quiet, 1: log update messages.

**Example**

```
>>> # This function keeps the initial learning rate for the first ten epochs
>>> # and decreases it exponentially after that.
>>> def scheduler(epoch, lr):
...     if epoch < 10:
...         return lr
...     else:
...         return lr * ops.exp(-0.1)
>>>
>>> model = keras.models.Sequential([keras.layers.Dense(10)])
>>> model.compile(keras.optimizers.SGD(), loss='mse')
>>> round(model.optimizer.learning_rate, 5)
0.01
```

```
>>> callback = keras.callbacks.LearningRateScheduler(scheduler)
>>> history = model.fit(np.arange(100).reshape(5, 20), np.zeros(5),
...                     epochs=15, callbacks=[callback], verbose=0)
>>> round(model.optimizer.learning_rate, 5)
0.00607
```

**Guides and examples using `LearningRateScheduler`**

*   [MultipleChoice Task with Transfer Learning](https://keras.io/examples/nlp/multiple_choice_task_with_transfer_learning/)

* * *

[LearningRateScheduler](https://keras.io/api/callbacks/learning_rate_scheduler#learningratescheduler)

[`LearningRateScheduler` class](https://keras.io/api/callbacks/learning_rate_scheduler#learningratescheduler-class)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
