# Source: https://keras.io/api/callbacks/remote_monitor

Title: Keras documentation: RemoteMonitor

URL Source: https://keras.io/api/callbacks/remote_monitor

Markdown Content:
RemoteMonitor
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

►[Keras 3 API documentation](https://keras.io/api/) / [Callbacks API](https://keras.io/api/callbacks/) / RemoteMonitor 

RemoteMonitor
=============

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/remote_monitor.py#L15)

### `RemoteMonitor` class

```
keras.callbacks.RemoteMonitor(
    root="http://localhost:9000",
    path="/publish/epoch/end/",
    field="data",
    headers=None,
    send_as_json=False,
)
```

Callback used to stream events to a server.

Requires the `requests` library. Events are sent to `root + '/publish/epoch/end/'` by default. Calls are HTTP POST, with a `data` argument which is a JSON-encoded dictionary of event data. If `send_as_json=True`, the content type of the request will be `"application/json"`. Otherwise the serialized JSON will be sent within a form.

**Arguments**

*   **root**: String; root url of the target server.
*   **path**: String; path relative to `root` to which the events will be sent.
*   **field**: String; JSON field under which the data will be stored. The field is used only if the payload is sent within a form (i.e. when `send_as_json=False`).
*   **headers**: Dictionary; optional custom HTTP headers.
*   **send_as_json**: Boolean; whether the request should be sent as `"application/json"`.

* * *

[RemoteMonitor](https://keras.io/api/callbacks/remote_monitor#remotemonitor)

[`RemoteMonitor` class](https://keras.io/api/callbacks/remote_monitor#remotemonitor-class)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
