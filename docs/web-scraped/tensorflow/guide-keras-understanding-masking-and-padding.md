# Source: https://www.tensorflow.org/guide/keras/understanding_masking_and_padding

Title: Understanding masking & padding

URL Source: https://www.tensorflow.org/guide/keras/understanding_masking_and_padding

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#main-content)

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

*   [Tensor Flow guide](https://www.tensorflow.org/guide)
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
*   [NumPy API Type Promotion](https://www.tensorflow.org/guide/tf_numpy_type_promotion)
*   [DTensor concepts](https://www.tensorflow.org/guide/dtensor_overview)
*   [Thinking in TensorFlow 2](https://www.tensorflow.org/guide/effective_tf2)
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

Understanding masking & padding Stay organized with collections  Save and categorize content based on your preferences.
-----------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#setup)
*   [Introduction](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#introduction)
*   [Padding sequence data](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#padding_sequence_data)
*   [Masking](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#masking)
*   [Mask-generating layers: Embedding and Masking](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#mask-generating_layers_embedding_and_masking)
*   [Mask propagation in the Functional API and Sequential API](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#mask_propagation_in_the_functional_api_and_sequential_api)
*   [Passing mask tensors directly to layers](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#passing_mask_tensors_directly_to_layers)
*   [Supporting masking in your custom layers](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#supporting_masking_in_your_custom_layers)
*   [Opting-in to mask propagation on compatible layers](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#opting-in_to_mask_propagation_on_compatible_layers)
*   [Writing layers that need mask information](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#writing_layers_that_need_mask_information)
*   [Summary](https://www.tensorflow.org/guide/keras/understanding_masking_and_padding#summary)

**Authors:** Scott Zhu, Francois Chollet

Setup
-----

```
import numpy as np
import tensorflow as tf
import keras
from keras import layers
```

Introduction
------------

**Masking** is a way to tell sequence-processing layers that certain timesteps in an input are missing, and thus should be skipped when processing the data.

**Padding** is a special form of masking where the masked steps are at the start or the end of a sequence. Padding comes from the need to encode sequence data into contiguous batches: in order to make all sequences in a batch fit a given standard length, it is necessary to pad or truncate some sequences.

Let's take a close look.

Padding sequence data
---------------------

When processing sequence data, it is very common for individual samples to have different lengths. Consider the following example (text tokenized as words):

```
[
  ["Hello", "world", "!"],
  ["How", "are", "you", "doing", "today"],
  ["The", "weather", "will", "be", "nice", "tomorrow"],
]
```

After vocabulary lookup, the data might be vectorized as integers, e.g.:

```
[
  [71, 1331, 4231]
  [73, 8, 3215, 55, 927],
  [83, 91, 1, 645, 1253, 927],
]
```

The data is a nested list where individual samples have length 3, 5, and 6, respectively. Since the input data for a deep learning model must be a single tensor (of shape e.g. `(batch_size, 6, vocab_size)` in this case), samples that are shorter than the longest item need to be padded with some placeholder value (alternatively, one might also truncate long samples before padding short samples).

Keras provides a utility function to truncate and pad Python lists to a common length: [`tf.keras.utils.pad_sequences`](https://www.tensorflow.org/api_docs/python/tf/keras/utils/pad_sequences).

```
raw_inputs = [
    [711, 632, 71],
    [73, 8, 3215, 55, 927],
    [83, 91, 1, 645, 1253, 927],
]

# By default, this will pad using 0s; it is configurable via the
# "value" parameter.
# Note that you could use "pre" padding (at the beginning) or
# "post" padding (at the end).
# We recommend using "post" padding when working with RNN layers
# (in order to be able to use the
# CuDNN implementation of the layers).
padded_inputs = tf.keras.utils.pad_sequences(raw_inputs, padding="post")
print(padded_inputs)
```
[[ 711  632   71    0    0    0]
 [  73    8 3215   55  927    0]
 [  83   91    1  645 1253  927]]

Now that all samples have a uniform length, the model must be informed that some part of the data is actually padding and should be ignored. That mechanism is **masking**.

There are three ways to introduce input masks in Keras models:

*   Add a [`keras.layers.Masking`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Masking) layer.
*   Configure a [`keras.layers.Embedding`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding) layer with `mask_zero=True`.
*   Pass a `mask` argument manually when calling layers that support this argument (e.g. RNN layers).

Mask-generating layers: `Embedding` and `Masking`
-------------------------------------------------

Under the hood, these layers will create a mask tensor (2D tensor with shape 
```
(batch,
sequence_length)
```
), and attach it to the tensor output returned by the `Masking` or `Embedding` layer.

```
embedding = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)
masked_output = embedding(padded_inputs)

print(masked_output._keras_mask)

masking_layer = layers.Masking()
# Simulate the embedding lookup by expanding the 2D input to 3D,
# with embedding dimension of 10.
unmasked_embedding = tf.cast(
    tf.tile(tf.expand_dims(padded_inputs, axis=-1), [1, 1, 10]), tf.float32
)

masked_embedding = masking_layer(unmasked_embedding)
print(masked_embedding._keras_mask)
```
tf.Tensor(
[[ True  True  True False False False]
 [ True  True  True  True  True False]
 [ True  True  True  True  True  True]], shape=(3, 6), dtype=bool)
tf.Tensor(
[[ True  True  True False False False]
 [ True  True  True  True  True False]
 [ True  True  True  True  True  True]], shape=(3, 6), dtype=bool)

As you can see from the printed result, the mask is a 2D boolean tensor with shape `(batch_size, sequence_length)`, where each individual `False` entry indicates that the corresponding timestep should be ignored during processing.

Mask propagation in the Functional API and Sequential API
---------------------------------------------------------

When using the Functional API or the Sequential API, a mask generated by an `Embedding` or `Masking` layer will be propagated through the network for any layer that is capable of using them (for example, RNN layers). Keras will automatically fetch the mask corresponding to an input and pass it to any layer that knows how to use it.

For instance, in the following Sequential model, the `LSTM` layer will automatically receive a mask, which means it will ignore padded values:

```
model = keras.Sequential(
    [
        layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True),
        layers.LSTM(32),
    ]
)
```

This is also the case for the following Functional API model:

```
inputs = keras.Input(shape=(None,), dtype="int32")
x = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)(inputs)
outputs = layers.LSTM(32)(x)

model = keras.Model(inputs, outputs)
```

Passing mask tensors directly to layers
---------------------------------------

Layers that can handle masks (such as the `LSTM` layer) have a `mask` argument in their `__call__` method.

Meanwhile, layers that produce a mask (e.g. `Embedding`) expose a 
```
compute_mask(input,
previous_mask)
```
 method which you can call.

Thus, you can pass the output of the `compute_mask()` method of a mask-producing layer to the `__call__` method of a mask-consuming layer, like this:

```
class MyLayer(layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.embedding = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)
        self.lstm = layers.LSTM(32)

    def call(self, inputs):
        x = self.embedding(inputs)
        # Note that you could also prepare a `mask` tensor manually.
        # It only needs to be a boolean tensor
        # with the right shape, i.e. (batch_size, timesteps).
        mask = self.embedding.compute_mask(inputs)
        output = self.lstm(x, mask=mask)  # The layer will ignore the masked values
        return output

layer = MyLayer()
x = np.random.random((32, 10)) * 100
x = x.astype("int32")
layer(x)
```
<tf.Tensor: shape=(32, 32), dtype=float32, numpy=
array([[ 1.1063378e-04, -5.7033719e-03,  3.0645048e-03, ...,
         3.6328615e-04, -2.8766368e-03, -1.3289017e-03],
       [-9.2790304e-03, -1.5139847e-02,  5.7660388e-03, ...,
         3.5337124e-03,  4.0699611e-03, -3.9524431e-04],
       [-3.4190060e-03,  7.9529232e-04,  3.7830453e-03, ...,
        -6.8300538e-04,  4.7965860e-03,  4.4357078e-03],
       ...,
       [-4.3796434e-04,  3.5149506e-03,  5.0854073e-03, ...,
         6.3023632e-03, -4.6664057e-03, -2.1111544e-03],
       [ 1.2171637e-03, -1.8671650e-03,  8.6708134e-03, ...,
        -2.6730294e-03, -1.6238958e-03,  5.9354519e-03],
       [-7.1832030e-03, -6.0863695e-03,  4.3814078e-05, ...,
         3.8765911e-03, -1.7828923e-03, -2.3530782e-03]], dtype=float32)>

Supporting masking in your custom layers
----------------------------------------

Sometimes, you may need to write layers that generate a mask (like `Embedding`), or layers that need to modify the current mask.

For instance, any layer that produces a tensor with a different time dimension than its input, such as a `Concatenate` layer that concatenates on the time dimension, will need to modify the current mask so that downstream layers will be able to properly take masked timesteps into account.

To do this, your layer should implement the `layer.compute_mask()` method, which produces a new mask given the input and the current mask.

Here is an example of a `TemporalSplit` layer that needs to modify the current mask.

```
class TemporalSplit(keras.layers.Layer):
    """Split the input tensor into 2 tensors along the time dimension."""

    def call(self, inputs):
        # Expect the input to be 3D and mask to be 2D, split the input tensor into 2
        # subtensors along the time axis (axis 1).
        return tf.split(inputs, 2, axis=1)

    def compute_mask(self, inputs, mask=None):
        # Also split the mask into 2 if it presents.
        if mask is None:
            return None
        return tf.split(mask, 2, axis=1)

first_half, second_half = TemporalSplit()(masked_embedding)
print(first_half._keras_mask)
print(second_half._keras_mask)
```
tf.Tensor(
[[ True  True  True]
 [ True  True  True]
 [ True  True  True]], shape=(3, 3), dtype=bool)
tf.Tensor(
[[False False False]
 [ True  True False]
 [ True  True  True]], shape=(3, 3), dtype=bool)

Here is another example of a `CustomEmbedding` layer that is capable of generating a mask from input values:

```
class CustomEmbedding(keras.layers.Layer):
    def __init__(self, input_dim, output_dim, mask_zero=False, **kwargs):
        super().__init__(**kwargs)
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.mask_zero = mask_zero

    def build(self, input_shape):
        self.embeddings = self.add_weight(
            shape=(self.input_dim, self.output_dim),
            initializer="random_normal",
            dtype="float32",
        )

    def call(self, inputs):
        return tf.nn.embedding_lookup(self.embeddings, inputs)

    def compute_mask(self, inputs, mask=None):
        if not self.mask_zero:
            return None
        return tf.not_equal(inputs, 0)

layer = CustomEmbedding(10, 32, mask_zero=True)
x = np.random.random((3, 10)) * 9
x = x.astype("int32")

y = layer(x)
mask = layer.compute_mask(x)

print(mask)
```
tf.Tensor(
[[ True  True  True  True  True  True  True  True  True  True]
 [ True  True  True  True False  True False  True  True  True]
 [ True False  True False  True  True  True  True  True  True]], shape=(3, 10), dtype=bool)

Opting-in to mask propagation on compatible layers
--------------------------------------------------

Most layers don't modify the time dimension, so don't need to modify the current mask. However, they may still want to be able to **propagate** the current mask, unchanged, to the next layer. **This is an opt-in behavior.** By default, a custom layer will destroy the current mask (since the framework has no way to tell whether propagating the mask is safe to do).

If you have a custom layer that does not modify the time dimension, and if you want it to be able to propagate the current input mask, you should set 
```
self.supports_masking
= True
```
 in the layer constructor. In this case, the default behavior of `compute_mask()` is to just pass the current mask through.

Here's an example of a layer that is whitelisted for mask propagation:

```
@keras.saving.register_keras_serializable()
class MyActivation(keras.layers.Layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Signal that the layer is safe for mask propagation
        self.supports_masking = True

    def call(self, inputs):
        return tf.nn.relu(inputs)
```

You can now use this custom layer in-between a mask-generating layer (like `Embedding`) and a mask-consuming layer (like `LSTM`), and it will pass the mask along so that it reaches the mask-consuming layer.

```
inputs = keras.Input(shape=(None,), dtype="int32")
x = layers.Embedding(input_dim=5000, output_dim=16, mask_zero=True)(inputs)
x = MyActivation()(x)  # Will pass the mask along
print("Mask found:", x._keras_mask)
outputs = layers.LSTM(32)(x)  # Will receive the mask

model = keras.Model(inputs, outputs)
```
Mask found: KerasTensor(type_spec=TensorSpec(shape=(None, None), dtype=tf.bool, name=None), name='Placeholder_1:0')

Writing layers that need mask information
-----------------------------------------

Some layers are mask _consumers_: they accept a `mask` argument in `call` and use it to determine whether to skip certain time steps.

To write such a layer, you can simply add a `mask=None` argument in your `call` signature. The mask associated with the inputs will be passed to your layer whenever it is available.

Here's a simple example below: a layer that computes a softmax over the time dimension (axis 1) of an input sequence, while discarding masked timesteps.

```
@keras.saving.register_keras_serializable()
class TemporalSoftmax(keras.layers.Layer):
    def call(self, inputs, mask=None):
        broadcast_float_mask = tf.expand_dims(tf.cast(mask, "float32"), -1)
        inputs_exp = tf.exp(inputs) * broadcast_float_mask
        inputs_sum = tf.reduce_sum(
            inputs_exp * broadcast_float_mask, axis=-1, keepdims=True
        )
        return inputs_exp / inputs_sum

inputs = keras.Input(shape=(None,), dtype="int32")
x = layers.Embedding(input_dim=10, output_dim=32, mask_zero=True)(inputs)
x = layers.Dense(1)(x)
outputs = TemporalSoftmax()(x)

model = keras.Model(inputs, outputs)
y = model(np.random.randint(0, 10, size=(32, 100)), np.random.random((32, 100, 1)))
```

Summary
-------

That is all you need to know about padding & masking in Keras. To recap:

*   "Masking" is how layers are able to know when to skip / ignore certain timesteps in sequence inputs.
*   Some layers are mask-generators: `Embedding` can generate a mask from input values (if `mask_zero=True`), and so can the `Masking` layer.
*   Some layers are mask-consumers: they expose a `mask` argument in their `__call__` method. This is the case for RNN layers.
*   In the Functional API and Sequential API, mask information is propagated automatically.
*   When using layers in a standalone way, you can pass the `mask` arguments to layers manually.
*   You can easily write layers that modify the current mask, that generate a new mask, or that consume the mask associated with the inputs.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-07-24 UTC.
