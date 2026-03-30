# Source: https://keras.io/api/callbacks/reduce_lr_on_plateau

Title: Keras documentation: ReduceLROnPlateau

URL Source: https://keras.io/api/callbacks/reduce_lr_on_plateau

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/reduce_lr_on_plateau.py#L11)

### `ReduceLROnPlateau` class

```
keras.callbacks.ReduceLROnPlateau(
    monitor="val_loss",
    factor=0.1,
    patience=10,
    verbose=0,
    mode="auto",
    min_delta=0.0001,
    cooldown=0,
    min_lr=0.0,
    **kwargs
)
```

Reduce learning rate when a metric has stopped improving.

Models often benefit from reducing the learning rate by a factor of 2-10 once learning stagnates. This callback monitors a quantity and if no improvement is seen for a 'patience' number of epochs, the learning rate is reduced.

**Example**

```
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.001)
model.fit(x_train, y_train, callbacks=[reduce_lr])
```

**Arguments**

*   **monitor**: String. Quantity to be monitored.
*   **factor**: Float. Factor by which the learning rate will be reduced. `new_lr = lr * factor`.
*   **patience**: Integer. Number of epochs with no improvement after which learning rate will be reduced.
*   **verbose**: Integer. 0: quiet, 1: update messages.
*   **mode**: String. One of `{'auto', 'min', 'max'}`. In `'min'` mode, the learning rate will be reduced when the quantity monitored has stopped decreasing; in `'max'` mode it will be reduced when the quantity monitored has stopped increasing; in `'auto'` mode, the direction is automatically inferred from the name of the monitored quantity.
*   **min_delta**: Float. Threshold for measuring the new optimum, to only focus on significant changes.
*   **cooldown**: Integer. Number of epochs to wait before resuming normal operation after the learning rate has been reduced.
*   **min_lr**: Float. Lower bound on the learning rate.

**Guides and examples using `ReduceLROnPlateau`**

*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)
*   [Image classification with Perceiver](https://keras.io/examples/vision/perceiver_image_classification/)
*   [Low-light image enhancement using MIRNet](https://keras.io/examples/vision/mirnet/)
*   [Next-Frame Video Prediction with Convolutional LSTMs](https://keras.io/examples/vision/conv_lstm/)
*   [Timeseries classification from scratch](https://keras.io/examples/timeseries/timeseries_classification_from_scratch/)
*   [Electroencephalogram Signal Classification for action identification](https://keras.io/examples/timeseries/eeg_signal_classification/)

* * *
