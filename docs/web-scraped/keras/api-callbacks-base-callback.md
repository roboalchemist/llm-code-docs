# Source: https://keras.io/api/callbacks/base_callback

Title: Keras documentation: Base Callback class

URL Source: https://keras.io/api/callbacks/base_callback

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/callbacks/callback.py#L6)

### `Callback` class

```
keras.callbacks.Callback()
```

Base class used to build new callbacks.

Callbacks can be passed to keras methods such as `fit()`, `evaluate()`, and `predict()` in order to hook into the various stages of the model training, evaluation, and inference lifecycle.

To create a custom callback, subclass [`keras.callbacks.Callback`](https://keras.io/api/callbacks/base_callback#callback-class) and override the method associated with the stage of interest.

**Example**

```
>>> training_finished = False
>>> class MyCallback(Callback):
...   def on_train_end(self, logs=None):
...     global training_finished
...     training_finished = True
>>> model = Sequential([
...     layers.Dense(1, input_shape=(1,))])
>>> model.compile(loss='mean_squared_error')
>>> model.fit(np.array([[1.0]]), np.array([[1.0]]),
...           callbacks=[MyCallback()])
>>> assert training_finished == True
```

If you want to use `Callback` objects in a custom training loop:

1.   You should pack all your callbacks into a single `callbacks.CallbackList` so they can all be called together.
2.   You will need to manually call all the `on_*` methods at the appropriate locations in your loop. Like this:

**Example**

```
callbacks =  keras.callbacks.CallbackList([...])
callbacks.append(...)
callbacks.on_train_begin(...)
for epoch in range(EPOCHS):
    callbacks.on_epoch_begin(epoch)
    for i, data in dataset.enumerate():
    callbacks.on_train_batch_begin(i)
    batch_logs = model.train_step(data)
    callbacks.on_train_batch_end(i, batch_logs)
    epoch_logs = ...
    callbacks.on_epoch_end(epoch, epoch_logs)
final_logs=...
callbacks.on_train_end(final_logs)
```

**Attributes**

*   **params**: Dict. Training parameters (eg. verbosity, batch size, number of epochs...).
*   **model**: Instance of `Model`. Reference of the model being trained.

The `logs` dictionary that callback methods take as argument will contain keys for quantities relevant to the current batch or epoch (see method-specific docstrings).

**Guides and examples using `Callback`**

*   [Training & evaluation with the built-in methods](https://keras.io/guides/training_with_built_in_methods/)
*   [Writing your own callbacks](https://keras.io/guides/writing_your_own_callbacks/)
*   [Orbax Checkpointing in Keras](https://keras.io/guides/orbax_checkpoint/)
*   [3D volumetric rendering with NeRF](https://keras.io/examples/vision/nerf/)
*   [Handwriting recognition](https://keras.io/examples/vision/handwriting_recognition/)
*   [Image Super-Resolution using an Efficient Sub-Pixel CNN](https://keras.io/examples/vision/super_resolution_sub_pixel/)
*   [Gradient Centralization for Better Training Performance](https://keras.io/examples/vision/gradient_centralization/)
*   [Augmenting convnets with aggregated attention](https://keras.io/examples/vision/patch_convnet/)

* * *
