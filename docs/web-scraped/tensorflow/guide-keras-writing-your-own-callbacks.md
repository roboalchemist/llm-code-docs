# Source: https://www.tensorflow.org/guide/keras/writing_your_own_callbacks

Title: Writing your own callbacks

URL Source: https://www.tensorflow.org/guide/keras/writing_your_own_callbacks

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#main-content)

*   [Install](https://www.tensorflow.org/install)
*   [Learn](https://www.tensorflow.org/learn)
    *   [Tutorials](https://www.tensorflow.org/tutorials)
    *   [Guide](https://www.tensorflow.org/guide)
    *   [Migrate to TF2](https://www.tensorflow.org/guide/migrate)
    *   [TF 1 ↗](https://github.com/tensorflow/docs/tree/master/site/en/r1)

*   [API](https://www.tensorflow.org/api)
*   [Ecosystem](https://www.tensorflow.org/resources/models-datasets)
*   [Community](https://www.tensorflow.org/community)
*   [Why TensorFlow](https://www.tensorflow.org/about)
*   [GitHub](https://github.com/tensorflow)

*   [TensorFlow guide](https://www.tensorflow.org/guide)
*   Tensor Flow basics

*   [Overview](https://www.tensorflow.org/guide/basics)
*   [Tensors](https://www.tensorflow.org/guide/tensor)
*   [Variables](https://www.tensorflow.org/guide/variable)
*   [Automatic differentiation](https://www.tensorflow.org/guide/autodiff)
*   [Graphs and functions](https://www.tensorflow.org/guide/intro_to_graphs)
*   [Modules, layers, and models](https://www.tensorflow.org/guide/intro_to_modules)
*   [Training loops](https://www.tensorflow.org/guide/basic_training_loops)
*   Keras

*   [Overview](https://www.tensorflow.org/guide/keras)
*   [The Sequential model](https://www.tensorflow.org/guide/keras/sequential_model)
*   [The Functional API](https://www.tensorflow.org/guide/keras/functional_api)
*   [Training & evaluation with the built-in methods](https://www.tensorflow.org/guide/keras/training_with_built_in_methods)
*   [Making new layers and models via subclassing](https://www.tensorflow.org/guide/keras/making_new_layers_and_models_via_subclassing)
*   [Serialization and saving](https://www.tensorflow.org/guide/keras/serialization_and_saving)
*   [Customizing Saving](https://www.tensorflow.org/guide/keras/customizing_saving_and_serialization)
*   [Working with preprocessing layers](https://www.tensorflow.org/guide/keras/preprocessing_layers)
*   [Customizing what happens in fit()](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit)
*   [Writing a training loop from scratch](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch)
*   [Working with RNNs](https://www.tensorflow.org/guide/keras/working_with_rnns)
*   [Understanding masking & padding](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding)
*   [Writing your own callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks)
*   [Transfer learning & fine-tuning](https://www.tensorflow.org/guide/keras/transfer_learning)
*   [Multi-GPU and distributed training](https://www.tensorflow.org/guide/keras/distributed_training)
*   Build with Core

*   [Overview](https://www.tensorflow.org/guide/core)
*   [Quickstart for Core](https://www.tensorflow.org/guide/core/quickstart_core)
*   [Logistic regression](https://www.tensorflow.org/guide/core/logistic_regression_core)
*   [Multilayer perceptrons](https://www.tensorflow.org/guide/core/mlp_core)
*   [Matrix approximation](https://www.tensorflow.org/guide/core/matrix_core)
*   [Custom optimizers](https://www.tensorflow.org/guide/core/optimizers_core)
*   [DTensor with Core APIs](https://www.tensorflow.org/guide/core/distribution)
*   Tensor Flow in depth

*   [Tensor slicing](https://www.tensorflow.org/guide/tensor_slicing)
*   [Advanced autodiff](https://www.tensorflow.org/guide/advanced_autodiff)
*   [Ragged tensor](https://www.tensorflow.org/guide/ragged_tensor)
*   [Sparse tensor](https://www.tensorflow.org/guide/sparse_tensor)
*   [Random number generation](https://www.tensorflow.org/guide/random_numbers)
*   [Num Py API](https://www.tensorflow.org/guide/tf_numpy)
*   [Num Py API Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)
*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)
*   [Thinking in Tensor Flow 2](https://www.tensorflow.org/guide/effective_tf2)
*   Customization

*   [Create an op](https://www.tensorflow.org/guide/create_op)
*   [Extension types](https://www.tensorflow.org/guide/extension_type)
*   Data input pipelines

*   [tf.data](https://www.tensorflow.org/guide/data)
*   [Optimize pipeline performance](https://www.tensorflow.org/guide/data_performance)
*   [Analyze pipeline performance](https://www.tensorflow.org/guide/data_performance_analysis)
*   Import and export

*   [Checkpoint](https://www.tensorflow.org/guide/checkpoint)
*   [SavedModel](https://www.tensorflow.org/guide/saved_model)
*   [Import a JAX model using JAX2TF](https://www.tensorflow.org/guide/jax2tf)
*   Accelerators

*   [Distributed training](https://www.tensorflow.org/guide/distributed_training)
*   [GPU](https://www.tensorflow.org/guide/gpu)
*   [TPU](https://www.tensorflow.org/guide/tpu)
*   Performance

*   [Better performance with tf.function](https://www.tensorflow.org/guide/function)
*   [Profile TensorFlow performance](https://www.tensorflow.org/guide/profiler)
*   [Optimize GPU Performance](https://www.tensorflow.org/guide/gpu_performance_analysis)
*   [Graph optimization](https://www.tensorflow.org/guide/graph_optimization)
*   [Mixed precision](https://www.tensorflow.org/guide/mixed_precision)
*   Model Garden

*   [Overview](https://www.tensorflow.org/tfmodels)
*   [Training with Orbit](https://www.tensorflow.org/tfmodels/orbit)
*   [TFModels - NLP](https://www.tensorflow.org/tfmodels/nlp)
*   [Example: Image classification](https://www.tensorflow.org/tfmodels/vision/image_classification)
*   [Example: Object Detection](https://www.tensorflow.org/tfmodels/vision/object_detection)
*   [Example: Semantic Segmentation](https://www.tensorflow.org/tfmodels/vision/semantic_segmentation)
*   [Example: Instance Segmentation](https://www.tensorflow.org/tfmodels/vision/instance_segmentation)
*   Estimators

*   [Estimator overview](https://www.tensorflow.org/guide/estimator)
*   Appendix

*   [Version compatibility](https://www.tensorflow.org/guide/versions)

Writing your own callbacks Stay organized with collections  Save and categorize content based on your preferences.
------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Introduction](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#introduction)
*   [Setup](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#setup)
*   [Keras callbacks overview](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#keras_callbacks_overview)
*   [An overview of callback methods](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#an_overview_of_callback_methods)
    *   [Global methods](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#global_methods)
    *   [Batch-level methods for training/testing/predicting](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#batch-level_methods_for_trainingtestingpredicting)
    *   [Epoch-level methods (training only)](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#epoch-level_methods_training_only)

*   [A basic example](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#a_basic_example)
    *   [Usage of logs dict](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#usage_of_logs_dict)

*   [Usage of self.model attribute](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#usage_of_selfmodel_attribute)
*   [Examples of Keras callback applications](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#examples_of_keras_callback_applications)
    *   [Early stopping at minimum loss](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#early_stopping_at_minimum_loss)
    *   [Learning rate scheduling](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#learning_rate_scheduling)
    *   [Built-in Keras callbacks](https://www.tensorflow.org/guide/keras/writing_your_own_callbacks#built-in_keras_callbacks)

**Authors:** Rick Chao, Francois Chollet

Introduction
------------

A callback is a powerful tool to customize the behavior of a Keras model during training, evaluation, or inference. Examples include [`tf.keras.callbacks.TensorBoard`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/TensorBoard) to visualize training progress and results with TensorBoard, or [`tf.keras.callbacks.ModelCheckpoint`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/ModelCheckpoint) to periodically save your model during training.

In this guide, you will learn what a Keras callback is, what it can do, and how you can build your own. We provide a few demos of simple callback applications to get you started.

Setup
-----

```
import tensorflow as tf
from tensorflow import keras
```

Keras callbacks overview
------------------------

All callbacks subclass the [`keras.callbacks.Callback`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/Callback) class, and override a set of methods called at various stages of training, testing, and predicting. Callbacks are useful to get a view on internal states and statistics of the model during training.

You can pass a list of callbacks (as the keyword argument `callbacks`) to the following model methods:

*   [`keras.Model.fit()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)
*   [`keras.Model.evaluate()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#evaluate)
*   [`keras.Model.predict()`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#predict)

An overview of callback methods
-------------------------------

### Global methods

#### `on_(train|test|predict)_begin(self, logs=None)`

Called at the beginning of `fit`/`evaluate`/`predict`.

#### `on_(train|test|predict)_end(self, logs=None)`

Called at the end of `fit`/`evaluate`/`predict`.

### Batch-level methods for training/testing/predicting

#### `on_(train|test|predict)_batch_begin(self, batch, logs=None)`

Called right before processing a batch during training/testing/predicting.

#### `on_(train|test|predict)_batch_end(self, batch, logs=None)`

Called at the end of training/testing/predicting a batch. Within this method, `logs` is a dict containing the metrics results.

### Epoch-level methods (training only)

#### `on_epoch_begin(self, epoch, logs=None)`

Called at the beginning of an epoch during training.

#### `on_epoch_end(self, epoch, logs=None)`

Called at the end of an epoch during training.

A basic example
---------------

Let's take a look at a concrete example. To get started, let's import tensorflow and define a simple Sequential Keras model:

```
# Define the Keras model to add callbacks to
def get_model():
    model = keras.Sequential()
    model.add(keras.layers.Dense(1, input_dim=784))
    model.compile(
        optimizer=keras.optimizers.RMSprop(learning_rate=0.1),
        loss="mean_squared_error",
        metrics=["mean_absolute_error"],
    )
    return model
```

Then, load the MNIST data for training and testing from Keras datasets API:

```
# Load example MNIST data and pre-process it
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 784).astype("float32") / 255.0
x_test = x_test.reshape(-1, 784).astype("float32") / 255.0

# Limit the data to 1000 samples
x_train = x_train[:1000]
y_train = y_train[:1000]
x_test = x_test[:1000]
y_test = y_test[:1000]
```

Now, define a simple custom callback that logs:

*   When `fit`/`evaluate`/`predict` starts & ends
*   When each epoch starts & ends
*   When each training batch starts & ends
*   When each evaluation (test) batch starts & ends
*   When each inference (prediction) batch starts & ends

```
class CustomCallback(keras.callbacks.Callback):
    def on_train_begin(self, logs=None):
        keys = list(logs.keys())
        print("Starting training; got log keys: {}".format(keys))

    def on_train_end(self, logs=None):
        keys = list(logs.keys())
        print("Stop training; got log keys: {}".format(keys))

    def on_epoch_begin(self, epoch, logs=None):
        keys = list(logs.keys())
        print("Start epoch {} of training; got log keys: {}".format(epoch, keys))

    def on_epoch_end(self, epoch, logs=None):
        keys = list(logs.keys())
        print("End epoch {} of training; got log keys: {}".format(epoch, keys))

    def on_test_begin(self, logs=None):
        keys = list(logs.keys())
        print("Start testing; got log keys: {}".format(keys))

    def on_test_end(self, logs=None):
        keys = list(logs.keys())
        print("Stop testing; got log keys: {}".format(keys))

    def on_predict_begin(self, logs=None):
        keys = list(logs.keys())
        print("Start predicting; got log keys: {}".format(keys))

    def on_predict_end(self, logs=None):
        keys = list(logs.keys())
        print("Stop predicting; got log keys: {}".format(keys))

    def on_train_batch_begin(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Training: start of batch {}; got log keys: {}".format(batch, keys))

    def on_train_batch_end(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Training: end of batch {}; got log keys: {}".format(batch, keys))

    def on_test_batch_begin(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Evaluating: start of batch {}; got log keys: {}".format(batch, keys))

    def on_test_batch_end(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Evaluating: end of batch {}; got log keys: {}".format(batch, keys))

    def on_predict_batch_begin(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Predicting: start of batch {}; got log keys: {}".format(batch, keys))

    def on_predict_batch_end(self, batch, logs=None):
        keys = list(logs.keys())
        print("...Predicting: end of batch {}; got log keys: {}".format(batch, keys))
```

Let's try it out:

```
model = get_model()
model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=1,
    verbose=0,
    validation_split=0.5,
    callbacks=[CustomCallback()],
)

res = model.evaluate(
    x_test, y_test, batch_size=128, verbose=0, callbacks=[CustomCallback()]
)

res = model.predict(x_test, batch_size=128, callbacks=[CustomCallback()])
```
Starting training; got log keys: []
Start epoch 0 of training; got log keys: []
...Training: start of batch 0; got log keys: []
...Training: end of batch 0; got log keys: ['loss', 'mean_absolute_error']
...Training: start of batch 1; got log keys: []
...Training: end of batch 1; got log keys: ['loss', 'mean_absolute_error']
...Training: start of batch 2; got log keys: []
...Training: end of batch 2; got log keys: ['loss', 'mean_absolute_error']
...Training: start of batch 3; got log keys: []
...Training: end of batch 3; got log keys: ['loss', 'mean_absolute_error']
Start testing; got log keys: []
...Evaluating: start of batch 0; got log keys: []
...Evaluating: end of batch 0; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 1; got log keys: []
...Evaluating: end of batch 1; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 2; got log keys: []
...Evaluating: end of batch 2; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 3; got log keys: []
...Evaluating: end of batch 3; got log keys: ['loss', 'mean_absolute_error']
Stop testing; got log keys: ['loss', 'mean_absolute_error']
End epoch 0 of training; got log keys: ['loss', 'mean_absolute_error', 'val_loss', 'val_mean_absolute_error']
Stop training; got log keys: ['loss', 'mean_absolute_error', 'val_loss', 'val_mean_absolute_error']
Start testing; got log keys: []
...Evaluating: start of batch 0; got log keys: []
...Evaluating: end of batch 0; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 1; got log keys: []
...Evaluating: end of batch 1; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 2; got log keys: []
...Evaluating: end of batch 2; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 3; got log keys: []
...Evaluating: end of batch 3; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 4; got log keys: []
...Evaluating: end of batch 4; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 5; got log keys: []
...Evaluating: end of batch 5; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 6; got log keys: []
...Evaluating: end of batch 6; got log keys: ['loss', 'mean_absolute_error']
...Evaluating: start of batch 7; got log keys: []
...Evaluating: end of batch 7; got log keys: ['loss', 'mean_absolute_error']
Stop testing; got log keys: ['loss', 'mean_absolute_error']
Start predicting; got log keys: []
...Predicting: start of batch 0; got log keys: []
...Predicting: end of batch 0; got log keys: ['outputs']
1/8 [==>...........................] - ETA: 0s...Predicting: start of batch 1; got log keys: []
...Predicting: end of batch 1; got log keys: ['outputs']
...Predicting: start of batch 2; got log keys: []
...Predicting: end of batch 2; got log keys: ['outputs']
...Predicting: start of batch 3; got log keys: []
...Predicting: end of batch 3; got log keys: ['outputs']
...Predicting: start of batch 4; got log keys: []
...Predicting: end of batch 4; got log keys: ['outputs']
...Predicting: start of batch 5; got log keys: []
...Predicting: end of batch 5; got log keys: ['outputs']
...Predicting: start of batch 6; got log keys: []
...Predicting: end of batch 6; got log keys: ['outputs']
...Predicting: start of batch 7; got log keys: []
...Predicting: end of batch 7; got log keys: ['outputs']
Stop predicting; got log keys: []
8/8 [==============================] - 0s 2ms/step

### Usage of `logs` dict

The `logs` dict contains the loss value, and all the metrics at the end of a batch or epoch. Example includes the loss and mean absolute error.

```
class LossAndErrorPrintingCallback(keras.callbacks.Callback):
    def on_train_batch_end(self, batch, logs=None):
        print(
            "Up to batch {}, the average loss is {:7.2f}.".format(batch, logs["loss"])
        )

    def on_test_batch_end(self, batch, logs=None):
        print(
            "Up to batch {}, the average loss is {:7.2f}.".format(batch, logs["loss"])
        )

    def on_epoch_end(self, epoch, logs=None):
        print(
            "The average loss for epoch {} is {:7.2f} "
            "and mean absolute error is {:7.2f}.".format(
                epoch, logs["loss"], logs["mean_absolute_error"]
            )
        )

model = get_model()
model.fit(
    x_train,
    y_train,
    batch_size=128,
    epochs=2,
    verbose=0,
    callbacks=[LossAndErrorPrintingCallback()],
)

res = model.evaluate(
    x_test,
    y_test,
    batch_size=128,
    verbose=0,
    callbacks=[LossAndErrorPrintingCallback()],
)
```
Up to batch 0, the average loss is   33.08.
Up to batch 1, the average loss is  429.70.
Up to batch 2, the average loss is  293.82.
Up to batch 3, the average loss is  222.52.
Up to batch 4, the average loss is  179.47.
Up to batch 5, the average loss is  150.49.
Up to batch 6, the average loss is  129.87.
Up to batch 7, the average loss is  116.92.
The average loss for epoch 0 is  116.92 and mean absolute error is    5.88.
Up to batch 0, the average loss is    5.29.
Up to batch 1, the average loss is    4.86.
Up to batch 2, the average loss is    4.66.
Up to batch 3, the average loss is    4.54.
Up to batch 4, the average loss is    4.50.
Up to batch 5, the average loss is    4.38.
Up to batch 6, the average loss is    4.39.
Up to batch 7, the average loss is    4.33.
The average loss for epoch 1 is    4.33 and mean absolute error is    1.68.
Up to batch 0, the average loss is    5.21.
Up to batch 1, the average loss is    4.73.
Up to batch 2, the average loss is    4.68.
Up to batch 3, the average loss is    4.57.
Up to batch 4, the average loss is    4.70.
Up to batch 5, the average loss is    4.71.
Up to batch 6, the average loss is    4.63.
Up to batch 7, the average loss is    4.56.

Usage of `self.model` attribute
-------------------------------

In addition to receiving log information when one of their methods is called, callbacks have access to the model associated with the current round of training/evaluation/inference: `self.model`.

Here are a few of the things you can do with `self.model` in a callback:

*   Set `self.model.stop_training = True` to immediately interrupt training.
*   Mutate hyperparameters of the optimizer (available as `self.model.optimizer`), such as `self.model.optimizer.learning_rate`.
*   Save the model at period intervals.
*   Record the output of `model.predict()` on a few test samples at the end of each epoch, to use as a sanity check during training.
*   Extract visualizations of intermediate features at the end of each epoch, to monitor what the model is learning over time.
*   etc.

Let's see this in action in a couple of examples.

Examples of Keras callback applications
---------------------------------------

### Early stopping at minimum loss

This first example shows the creation of a `Callback` that stops training when the minimum of loss has been reached, by setting the attribute `self.model.stop_training` (boolean). Optionally, you can provide an argument `patience` to specify how many epochs we should wait before stopping after having reached a local minimum.

[`tf.keras.callbacks.EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping) provides a more complete and general implementation.

```
import numpy as np

class EarlyStoppingAtMinLoss(keras.callbacks.Callback):
    """Stop training when the loss is at its min, i.e. the loss stops decreasing.

    Arguments:
        patience: Number of epochs to wait after min has been hit. After this
        number of no improvement, training stops.
    """

    def __init__(self, patience=0):
        super().__init__()
        self.patience = patience
        # best_weights to store the weights at which the minimum loss occurs.
        self.best_weights = None

    def on_train_begin(self, logs=None):
        # The number of epoch it has waited when loss is no longer minimum.
        self.wait = 0
        # The epoch the training stops at.
        self.stopped_epoch = 0
        # Initialize the best as infinity.
        self.best = np.inf

    def on_epoch_end(self, epoch, logs=None):
        current = logs.get("loss")
        if np.less(current, self.best):
            self.best = current
            self.wait = 0
            # Record the best weights if current results is better (less).
            self.best_weights = self.model.get_weights()
        else:
            self.wait += 1
            if self.wait >= self.patience:
                self.stopped_epoch = epoch
                self.model.stop_training = True
                print("Restoring model weights from the end of the best epoch.")
                self.model.set_weights(self.best_weights)

    def on_train_end(self, logs=None):
        if self.stopped_epoch > 0:
            print("Epoch %05d: early stopping" % (self.stopped_epoch + 1))

model = get_model()
model.fit(
    x_train,
    y_train,
    batch_size=64,
    steps_per_epoch=5,
    epochs=30,
    verbose=0,
    callbacks=[LossAndErrorPrintingCallback(), EarlyStoppingAtMinLoss()],
)
```
Up to batch 0, the average loss is   23.53.
Up to batch 1, the average loss is  480.92.
Up to batch 2, the average loss is  328.49.
Up to batch 3, the average loss is  248.52.
Up to batch 4, the average loss is  200.53.
The average loss for epoch 0 is  200.53 and mean absolute error is    8.30.
Up to batch 0, the average loss is    5.02.
Up to batch 1, the average loss is    5.80.
Up to batch 2, the average loss is    5.51.
Up to batch 3, the average loss is    5.38.
Up to batch 4, the average loss is    5.42.
The average loss for epoch 1 is    5.42 and mean absolute error is    1.90.
Up to batch 0, the average loss is    5.80.
Up to batch 1, the average loss is    6.89.
Up to batch 2, the average loss is    6.68.
Up to batch 3, the average loss is    6.35.
Up to batch 4, the average loss is    6.57.
The average loss for epoch 2 is    6.57 and mean absolute error is    2.07.
Restoring model weights from the end of the best epoch.
Epoch 00003: early stopping
<keras.src.callbacks.History at 0x7fd3802cbb80>

### Learning rate scheduling

In this example, we show how a custom Callback can be used to dynamically change the learning rate of the optimizer during the course of training.

See [`callbacks.LearningRateScheduler`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/LearningRateScheduler) for a more general implementations.

```
class CustomLearningRateScheduler(keras.callbacks.Callback):
    """Learning rate scheduler which sets the learning rate according to schedule.

    Arguments:
        schedule: a function that takes an epoch index
            (integer, indexed from 0) and current learning rate
            as inputs and returns a new learning rate as output (float).
    """

    def __init__(self, schedule):
        super().__init__()
        self.schedule = schedule

    def on_epoch_begin(self, epoch, logs=None):
        if not hasattr(self.model.optimizer, "lr"):
            raise ValueError('Optimizer must have a "lr" attribute.')
        # Get the current learning rate from model's optimizer.
        lr = float(tf.keras.backend.get_value(self.model.optimizer.learning_rate))
        # Call schedule function to get the scheduled learning rate.
        scheduled_lr = self.schedule(epoch, lr)
        # Set the value back to the optimizer before this epoch starts
        tf.keras.backend.set_value(self.model.optimizer.lr, scheduled_lr)
        print("\nEpoch %05d: Learning rate is %6.4f." % (epoch, scheduled_lr))

LR_SCHEDULE = [
    # (epoch to start, learning rate) tuples
    (3, 0.05),
    (6, 0.01),
    (9, 0.005),
    (12, 0.001),
]

def lr_schedule(epoch, lr):
    """Helper function to retrieve the scheduled learning rate based on epoch."""
    if epoch < LR_SCHEDULE[0][0] or epoch > LR_SCHEDULE[-1][0]:
        return lr
    for i in range(len(LR_SCHEDULE)):
        if epoch == LR_SCHEDULE[i][0]:
            return LR_SCHEDULE[i][1]
    return lr

model = get_model()
model.fit(
    x_train,
    y_train,
    batch_size=64,
    steps_per_epoch=5,
    epochs=15,
    verbose=0,
    callbacks=[
        LossAndErrorPrintingCallback(),
        CustomLearningRateScheduler(lr_schedule),
    ],
)
```
Epoch 00000: Learning rate is 0.1000.
Up to batch 0, the average loss is   25.33.
Up to batch 1, the average loss is  434.31.
Up to batch 2, the average loss is  298.47.
Up to batch 3, the average loss is  226.43.
Up to batch 4, the average loss is  182.22.
The average loss for epoch 0 is  182.22 and mean absolute error is    8.09.

Epoch 00001: Learning rate is 0.1000.
Up to batch 0, the average loss is    5.55.
Up to batch 1, the average loss is    5.56.
Up to batch 2, the average loss is    6.20.
Up to batch 3, the average loss is    6.24.
Up to batch 4, the average loss is    6.34.
The average loss for epoch 1 is    6.34 and mean absolute error is    2.09.

Epoch 00002: Learning rate is 0.1000.
Up to batch 0, the average loss is    7.28.
Up to batch 1, the average loss is    7.82.
Up to batch 2, the average loss is    7.52.
Up to batch 3, the average loss is    7.33.
Up to batch 4, the average loss is    7.52.
The average loss for epoch 2 is    7.52 and mean absolute error is    2.27.

Epoch 00003: Learning rate is 0.0500.
Up to batch 0, the average loss is   10.56.
Up to batch 1, the average loss is    7.01.
Up to batch 2, the average loss is    6.36.
Up to batch 3, the average loss is    6.18.
Up to batch 4, the average loss is    5.55.
The average loss for epoch 3 is    5.55 and mean absolute error is    1.90.

Epoch 00004: Learning rate is 0.0500.
Up to batch 0, the average loss is    3.26.
Up to batch 1, the average loss is    3.70.
Up to batch 2, the average loss is    3.75.
Up to batch 3, the average loss is    3.73.
Up to batch 4, the average loss is    3.79.
The average loss for epoch 4 is    3.79 and mean absolute error is    1.56.

Epoch 00005: Learning rate is 0.0500.
Up to batch 0, the average loss is    5.90.
Up to batch 1, the average loss is    5.09.
Up to batch 2, the average loss is    4.59.
Up to batch 3, the average loss is    4.39.
Up to batch 4, the average loss is    4.50.
The average loss for epoch 5 is    4.50 and mean absolute error is    1.66.

Epoch 00006: Learning rate is 0.0100.
Up to batch 0, the average loss is    6.34.
Up to batch 1, the average loss is    6.46.
Up to batch 2, the average loss is    5.29.
Up to batch 3, the average loss is    4.89.
Up to batch 4, the average loss is    4.68.
The average loss for epoch 6 is    4.68 and mean absolute error is    1.74.

Epoch 00007: Learning rate is 0.0100.
Up to batch 0, the average loss is    3.67.
Up to batch 1, the average loss is    3.06.
Up to batch 2, the average loss is    3.25.
Up to batch 3, the average loss is    3.45.
Up to batch 4, the average loss is    3.34.
The average loss for epoch 7 is    3.34 and mean absolute error is    1.43.

Epoch 00008: Learning rate is 0.0100.
Up to batch 0, the average loss is    3.35.
Up to batch 1, the average loss is    3.74.
Up to batch 2, the average loss is    3.50.
Up to batch 3, the average loss is    3.38.
Up to batch 4, the average loss is    3.58.
The average loss for epoch 8 is    3.58 and mean absolute error is    1.52.

Epoch 00009: Learning rate is 0.0050.
Up to batch 0, the average loss is    2.08.
Up to batch 1, the average loss is    2.52.
Up to batch 2, the average loss is    2.76.
Up to batch 3, the average loss is    2.72.
Up to batch 4, the average loss is    2.85.
The average loss for epoch 9 is    2.85 and mean absolute error is    1.31.

Epoch 00010: Learning rate is 0.0050.
Up to batch 0, the average loss is    3.64.
Up to batch 1, the average loss is    3.39.
Up to batch 2, the average loss is    3.42.
Up to batch 3, the average loss is    3.83.
Up to batch 4, the average loss is    3.85.
The average loss for epoch 10 is    3.85 and mean absolute error is    1.56.

Epoch 00011: Learning rate is 0.0050.
Up to batch 0, the average loss is    3.33.
Up to batch 1, the average loss is    3.18.
Up to batch 2, the average loss is    2.98.
Up to batch 3, the average loss is    3.02.
Up to batch 4, the average loss is    2.85.
The average loss for epoch 11 is    2.85 and mean absolute error is    1.31.

Epoch 00012: Learning rate is 0.0010.
Up to batch 0, the average loss is    3.58.
Up to batch 1, the average loss is    3.22.
Up to batch 2, the average loss is    3.27.
Up to batch 3, the average loss is    3.24.
Up to batch 4, the average loss is    3.02.
The average loss for epoch 12 is    3.02 and mean absolute error is    1.32.

Epoch 00013: Learning rate is 0.0010.
Up to batch 0, the average loss is    3.37.
Up to batch 1, the average loss is    3.55.
Up to batch 2, the average loss is    3.31.
Up to batch 3, the average loss is    3.28.
Up to batch 4, the average loss is    3.27.
The average loss for epoch 13 is    3.27 and mean absolute error is    1.43.

Epoch 00014: Learning rate is 0.0010.
Up to batch 0, the average loss is    2.02.
Up to batch 1, the average loss is    2.66.
Up to batch 2, the average loss is    2.61.
Up to batch 3, the average loss is    2.56.
Up to batch 4, the average loss is    2.82.
The average loss for epoch 14 is    2.82 and mean absolute error is    1.27.
<keras.src.callbacks.History at 0x7fd3801da790>

### Built-in Keras callbacks

Be sure to check out the existing Keras callbacks by reading the [API docs](https://keras.io/api/callbacks/). Applications include logging to CSV, saving the model, visualizing metrics in TensorBoard, and a lot more!

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-07 UTC.
