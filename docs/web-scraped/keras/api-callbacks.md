# Source: https://keras.io/api/callbacks/

Title: Keras documentation: Callbacks API

URL Source: https://keras.io/api/callbacks/

Markdown Content:
A callback is an object that can perform actions at various stages of training (e.g. at the start or end of an epoch, before or after a single batch, etc).

You can use callbacks to:

*   Write TensorBoard logs after every batch of training to monitor your metrics
*   Periodically save your model to disk
*   Do early stopping
*   Get a view on internal states and statistics of a model during training
*   ...and more

* * *

Available callbacks
-------------------

*   [Base Callback class](https://keras.io/api/callbacks/base_callback/)
*   [ModelCheckpoint](https://keras.io/api/callbacks/model_checkpoint/)
*   [BackupAndRestore](https://keras.io/api/callbacks/backup_and_restore/)
*   [TensorBoard](https://keras.io/api/callbacks/tensorboard/)
*   [EarlyStopping](https://keras.io/api/callbacks/early_stopping/)
*   [LearningRateScheduler](https://keras.io/api/callbacks/learning_rate_scheduler/)
*   [ReduceLROnPlateau](https://keras.io/api/callbacks/reduce_lr_on_plateau/)
*   [RemoteMonitor](https://keras.io/api/callbacks/remote_monitor/)
*   [LambdaCallback](https://keras.io/api/callbacks/lambda_callback/)
*   [TerminateOnNaN](https://keras.io/api/callbacks/terminate_on_nan/)
*   [CSVLogger](https://keras.io/api/callbacks/csv_logger/)
*   [ProgbarLogger](https://keras.io/api/callbacks/progbar_logger/)
*   [SwapEMAWeights](https://keras.io/api/callbacks/swap_ema_weights/)

* * *

Usage of callbacks via the built-in `fit()` loop
------------------------------------------------

You can pass a list of callbacks (as the keyword argument `callbacks`) to the `.fit()` method of a model:

```
my_callbacks = [
    keras.callbacks.EarlyStopping(patience=2),
    keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
    keras.callbacks.TensorBoard(log_dir='./logs'),
]
model.fit(dataset, epochs=10, callbacks=my_callbacks)
```

The relevant methods of the callbacks will then be called at each stage of the training.

* * *

Using custom callbacks
----------------------

Creating new callbacks is a simple and powerful way to customize a training loop. Learn more about creating new callbacks in the guide [Writing your own Callbacks](https://keras.io/guides/writing_your_own_callbacks), and refer to the documentation for [the base `Callback` class](https://keras.io/api/callbacks/base_callback).
