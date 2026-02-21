# Source: https://www.tensorflow.org/guide/ragged_tensor

Title: Ragged tensors

URL Source: https://www.tensorflow.org/guide/ragged_tensor

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/ragged_tensor#main-content)

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
*   TensorFlow basics

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
*   [Saved Model](https://www.tensorflow.org/guide/saved_model)
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

Ragged tensors Stay organized with collections  Save and categorize content based on your preferences.
------------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/ragged_tensor#setup)
*   [Overview](https://www.tensorflow.org/guide/ragged_tensor#overview)
    *   [What you can do with a ragged tensor](https://www.tensorflow.org/guide/ragged_tensor#what_you_can_do_with_a_ragged_tensor)
    *   [Constructing a ragged tensor](https://www.tensorflow.org/guide/ragged_tensor#constructing_a_ragged_tensor)
    *   [What you can store in a ragged tensor](https://www.tensorflow.org/guide/ragged_tensor#what_you_can_store_in_a_ragged_tensor)

*   [Example use case](https://www.tensorflow.org/guide/ragged_tensor#example_use_case)
*   [Ragged and uniform dimensions](https://www.tensorflow.org/guide/ragged_tensor#ragged_and_uniform_dimensions)
*   [Ragged vs sparse](https://www.tensorflow.org/guide/ragged_tensor#ragged_vs_sparse)
*   [TensorFlow APIs](https://www.tensorflow.org/guide/ragged_tensor#tensorflow_apis)
    *   [Keras](https://www.tensorflow.org/guide/ragged_tensor#keras)
    *   [tf.Example](https://www.tensorflow.org/guide/ragged_tensor#tfexample)
    *   [Datasets](https://www.tensorflow.org/guide/ragged_tensor#datasets)
    *   [tf.function](https://www.tensorflow.org/guide/ragged_tensor#tffunction)
    *   [SavedModels](https://www.tensorflow.org/guide/ragged_tensor#savedmodels)

*   [Overloaded operators](https://www.tensorflow.org/guide/ragged_tensor#overloaded_operators)
*   [Indexing](https://www.tensorflow.org/guide/ragged_tensor#indexing)
    *   [Indexing examples: 2D ragged tensor](https://www.tensorflow.org/guide/ragged_tensor#indexing_examples_2d_ragged_tensor)
    *   [Indexing examples: 3D ragged tensor](https://www.tensorflow.org/guide/ragged_tensor#indexing_examples_3d_ragged_tensor)

*   [Tensor type conversion](https://www.tensorflow.org/guide/ragged_tensor#tensor_type_conversion)
*   [Evaluating ragged tensors](https://www.tensorflow.org/guide/ragged_tensor#evaluating_ragged_tensors)
*   [Ragged Shapes](https://www.tensorflow.org/guide/ragged_tensor#ragged_shapes)
    *   [Static shape](https://www.tensorflow.org/guide/ragged_tensor#static_shape)
    *   [Dynamic shape](https://www.tensorflow.org/guide/ragged_tensor#dynamic_shape)
    *   [Broadcasting](https://www.tensorflow.org/guide/ragged_tensor#broadcasting)

*   [RaggedTensor encoding](https://www.tensorflow.org/guide/ragged_tensor#raggedtensor_encoding)
    *   [Multiple ragged dimensions](https://www.tensorflow.org/guide/ragged_tensor#multiple_ragged_dimensions)
    *   [Ragged rank and flat values](https://www.tensorflow.org/guide/ragged_tensor#ragged_rank_and_flat_values)
    *   [Uniform inner dimensions](https://www.tensorflow.org/guide/ragged_tensor#uniform_inner_dimensions)
    *   [Uniform non-inner dimensions](https://www.tensorflow.org/guide/ragged_tensor#uniform_non-inner_dimensions)

**API Documentation:**[`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor)[`tf.ragged`](https://www.tensorflow.org/api_docs/python/tf/ragged)

Setup
-----

```
!pip install --pre -U tensorflow
import math
import tensorflow as tf
```
2024-08-27 01:20:40.536630: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-27 01:20:40.557820: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-27 01:20:40.563984: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

Overview
--------

Your data comes in many shapes; your tensors should too. _Ragged tensors_ are the TensorFlow equivalent of nested variable-length lists. They make it easy to store and process data with non-uniform shapes, including:

*   Variable-length features, such as the set of actors in a movie.
*   Batches of variable-length sequential inputs, such as sentences or video clips.
*   Hierarchical inputs, such as text documents that are subdivided into sections, paragraphs, sentences, and words.
*   Individual fields in structured inputs, such as protocol buffers.

### What you can do with a ragged tensor

Ragged tensors are supported by more than a hundred TensorFlow operations, including math operations (such as [`tf.add`](https://www.tensorflow.org/api_docs/python/tf/math/add) and [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean)), array operations (such as [`tf.concat`](https://www.tensorflow.org/api_docs/python/tf/concat) and [`tf.tile`](https://www.tensorflow.org/api_docs/python/tf/tile)), string manipulation ops (such as [`tf.strings.substr`](https://www.tensorflow.org/api_docs/python/tf/strings/substr)), control flow operations (such as [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop) and [`tf.map_fn`](https://www.tensorflow.org/api_docs/python/tf/map_fn)), and many others:

```
digits = tf.ragged.constant([[3, 1, 4, 1], [], [5, 9, 2], [6], []])
words = tf.ragged.constant([["So", "long"], ["thanks", "for", "all", "the", "fish"]])
print(tf.add(digits, 3))
print(tf.reduce_mean(digits, axis=1))
print(tf.concat([digits, [[5, 3]]], axis=0))
print(tf.tile(digits, [1, 2]))
print(tf.strings.substr(words, 0, 2))
print(tf.map_fn(tf.math.square, digits))
```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724721643.161122   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.164924   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.168750   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.172328   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.183636   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.187178   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.190668   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.194028   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.197422   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.201089   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.204485   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721643.207934   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.469725   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.471772   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.473847   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.475930   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.477949   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.479867   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.481845   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.483831   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.486309   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.488220   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.490205   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.492181   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.532055   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.534019   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.536012   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.538150   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.540140   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.542032   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.543963   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.545991   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.547989   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.551435   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.553772   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1724721644.556197   10064 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
<tf.RaggedTensor [[6, 4, 7, 4], [], [8, 12, 5], [9], []]>
tf.Tensor([2.25              nan 5.33333333 6.                nan], shape=(5,), dtype=float64)
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9, 2], [6], [], [5, 3]]>
<tf.RaggedTensor [[3, 1, 4, 1, 3, 1, 4, 1], [], [5, 9, 2, 5, 9, 2], [6, 6], []]>
<tf.RaggedTensor [[b'So', b'lo'], [b'th', b'fo', b'al', b'th', b'fi']]>
<tf.RaggedTensor [[9, 1, 16, 1], [], [25, 81, 4], [36], []]>

There are also a number of methods and operations that are specific to ragged tensors, including factory methods, conversion methods, and value-mapping operations. For a list of supported ops, see the **[`tf.ragged`](https://www.tensorflow.org/api_docs/python/tf/ragged) package documentation**.

Ragged tensors are supported by many TensorFlow APIs, including [Keras](https://www.tensorflow.org/guide/keras), [Datasets](https://www.tensorflow.org/guide/data), [tf.function](https://www.tensorflow.org/guide/function), [SavedModels](https://www.tensorflow.org/guide/saved_model), and [tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord). For more information, check the section on **TensorFlow APIs** below.

As with normal tensors, you can use Python-style indexing to access specific slices of a ragged tensor. For more information, refer to the section on **Indexing** below.

```
print(digits[0])       # First row
```
tf.Tensor([3 1 4 1], shape=(4,), dtype=int32)

```
print(digits[:, :2])   # First two values in each row.
```
<tf.RaggedTensor [[3, 1], [], [5, 9], [6], []]>

```
print(digits[:, -2:])  # Last two values in each row.
```
<tf.RaggedTensor [[4, 1], [], [9, 2], [6], []]>

And just like normal tensors, you can use Python arithmetic and comparison operators to perform elementwise operations. For more information, check the section on **Overloaded operators** below.

```
print(digits + 3)
```
<tf.RaggedTensor [[6, 4, 7, 4], [], [8, 12, 5], [9], []]>

```
print(digits + tf.ragged.constant([[1, 2, 3, 4], [], [5, 6, 7], [8], []]))
```
<tf.RaggedTensor [[4, 3, 7, 5], [], [10, 15, 9], [14], []]>

If you need to perform an elementwise transformation to the values of a `RaggedTensor`, you can use [`tf.ragged.map_flat_values`](https://www.tensorflow.org/api_docs/python/tf/ragged/map_flat_values), which takes a function plus one or more arguments, and applies the function to transform the `RaggedTensor`'s values.

```
times_two_plus_one = lambda x: x * 2 + 1
print(tf.ragged.map_flat_values(times_two_plus_one, digits))
```
<tf.RaggedTensor [[7, 3, 9, 3], [], [11, 19, 5], [13], []]>

Ragged tensors can be converted to nested Python `list`s and NumPy `array`s:

```
digits.to_list()
```
[[3, 1, 4, 1], [], [5, 9, 2], [6], []]

```
digits.numpy()
```
array([array([3, 1, 4, 1], dtype=int32), array([], dtype=int32),
       array([5, 9, 2], dtype=int32), array([6], dtype=int32),
       array([], dtype=int32)], dtype=object)

### Constructing a ragged tensor

The simplest way to construct a ragged tensor is using [`tf.ragged.constant`](https://www.tensorflow.org/api_docs/python/tf/ragged/constant), which builds the `RaggedTensor` corresponding to a given nested Python `list` or NumPy `array`:

```
sentences = tf.ragged.constant([
    ["Let's", "build", "some", "ragged", "tensors", "!"],
    ["We", "can", "use", "tf.ragged.constant", "."]])
print(sentences)
```
<tf.RaggedTensor [[b"Let's", b'build', b'some', b'ragged', b'tensors', b'!'],
 [b'We', b'can', b'use', b'tf.ragged.constant', b'.']]>

```
paragraphs = tf.ragged.constant([
    [['I', 'have', 'a', 'cat'], ['His', 'name', 'is', 'Mat']],
    [['Do', 'you', 'want', 'to', 'come', 'visit'], ["I'm", 'free', 'tomorrow']],
])
print(paragraphs)
```
<tf.RaggedTensor [[[b'I', b'have', b'a', b'cat'], [b'His', b'name', b'is', b'Mat']],
 [[b'Do', b'you', b'want', b'to', b'come', b'visit'],
  [b"I'm", b'free', b'tomorrow']]]>

Ragged tensors can also be constructed by pairing flat _values_ tensors with _row-partitioning_ tensors indicating how those values should be divided into rows, using factory classmethods such as [`tf.RaggedTensor.from_value_rowids`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_value_rowids), [`tf.RaggedTensor.from_row_lengths`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_lengths), and [`tf.RaggedTensor.from_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_splits).

#### [`tf.RaggedTensor.from_value_rowids`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_value_rowids)

If you know which row each value belongs to, then you can build a `RaggedTensor` using a `value_rowids` row-partitioning tensor:

![Image 1: value_rowids row-partitioning tensor](https://www.tensorflow.org/images/ragged_tensors/value_rowids.png)

```
print(tf.RaggedTensor.from_value_rowids(
    values=[3, 1, 4, 1, 5, 9, 2],
    value_rowids=[0, 0, 0, 0, 2, 2, 3]))
```
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9], [2]]>

#### [`tf.RaggedTensor.from_row_lengths`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_lengths)

If you know how long each row is, then you can use a `row_lengths` row-partitioning tensor:

![Image 2: row_lengths row-partitioning tensor](https://www.tensorflow.org/images/ragged_tensors/row_lengths.png)

```
print(tf.RaggedTensor.from_row_lengths(
    values=[3, 1, 4, 1, 5, 9, 2],
    row_lengths=[4, 0, 2, 1]))
```
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9], [2]]>

#### [`tf.RaggedTensor.from_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_row_splits)

If you know the index where each row starts and ends, then you can use a `row_splits` row-partitioning tensor:

![Image 3: row_splits row-partitioning tensor](https://www.tensorflow.org/images/ragged_tensors/row_splits.png)

```
print(tf.RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2],
    row_splits=[0, 4, 4, 6, 7]))
```
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9], [2]]>

See the [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor) class documentation for a full list of factory methods.

### What you can store in a ragged tensor

As with normal `Tensor`s, the values in a `RaggedTensor` must all have the same type; and the values must all be at the same nesting depth (the _rank_ of the tensor):

```
print(tf.ragged.constant([["Hi"], ["How", "are", "you"]]))  # ok: type=string, rank=2
```
<tf.RaggedTensor [[b'Hi'], [b'How', b'are', b'you']]>

```
print(tf.ragged.constant([[[1, 2], [3]], [[4, 5]]]))        # ok: type=int32, rank=3
```
<tf.RaggedTensor [[[1, 2], [3]], [[4, 5]]]>

```
try:
  tf.ragged.constant([["one", "two"], [3, 4]])              # bad: multiple types
except ValueError as exception:
  print(exception)
```
Can't convert Python sequence with mixed types to Tensor.

```
try:
  tf.ragged.constant(["A", ["B", "C"]])                     # bad: multiple nesting depths
except ValueError as exception:
  print(exception)
```
all scalar values must have the same nesting depth

Example use case
----------------

The following example demonstrates how `RaggedTensor`s can be used to construct and combine unigram and bigram embeddings for a batch of variable-length queries, using special markers for the beginning and end of each sentence. For more details on the ops used in this example, check the [`tf.ragged`](https://www.tensorflow.org/api_docs/python/tf/ragged) package documentation.

```
queries = tf.ragged.constant([['Who', 'is', 'Dan', 'Smith'],
                              ['Pause'],
                              ['Will', 'it', 'rain', 'later', 'today']])

# Create an embedding table.
num_buckets = 1024
embedding_size = 4
embedding_table = tf.Variable(
    tf.random.truncated_normal([num_buckets, embedding_size],
                       stddev=1.0 / math.sqrt(embedding_size)))

# Look up the embedding for each word.
word_buckets = tf.strings.to_hash_bucket_fast(queries, num_buckets)
word_embeddings = tf.nn.embedding_lookup(embedding_table, word_buckets)     # ①

# Add markers to the beginning and end of each sentence.
marker = tf.fill([queries.nrows(), 1], '#')
padded = tf.concat([marker, queries, marker], axis=1)                       # ②

# Build word bigrams and look up embeddings.
bigrams = tf.strings.join([padded[:, :-1], padded[:, 1:]], separator='+')   # ③

bigram_buckets = tf.strings.to_hash_bucket_fast(bigrams, num_buckets)
bigram_embeddings = tf.nn.embedding_lookup(embedding_table, bigram_buckets) # ④

# Find the average embedding for each sentence
all_embeddings = tf.concat([word_embeddings, bigram_embeddings], axis=1)    # ⑤
avg_embedding = tf.reduce_mean(all_embeddings, axis=1)                      # ⑥
print(avg_embedding)
```
tf.Tensor(
[[-0.07189021  0.23444025 -0.04020268 -0.27113184]
 [ 0.10560822  0.00976487 -0.17885399  0.5371701 ]
 [-0.23479678 -0.15996003  0.07078557  0.24388357]], shape=(3, 4), dtype=float32)

![Image 4: Ragged tensor example](https://www.tensorflow.org/images/ragged_tensors/ragged_example.png)

Ragged and uniform dimensions
-----------------------------

A **_ragged dimension_** is a dimension whose slices may have different lengths. For example, the inner (column) dimension of `rt=[[3, 1, 4, 1], [], [5, 9, 2], [6], []]` is ragged, since the column slices (`rt[0, :]`, ..., `rt[4, :]`) have different lengths. Dimensions whose slices all have the same length are called _uniform dimensions_.

The outermost dimension of a ragged tensor is always uniform, since it consists of a single slice (and, therefore, there is no possibility for differing slice lengths). The remaining dimensions may be either ragged or uniform. For example, you may store the word embeddings for each word in a batch of sentences using a ragged tensor with shape `[num_sentences, (num_words), embedding_size]`, where the parentheses around `(num_words)` indicate that the dimension is ragged.

![Image 5: Word embeddings using a ragged tensor](https://www.tensorflow.org/images/ragged_tensors/sent_word_embed.png)

Ragged tensors may have multiple ragged dimensions. For example, you could store a batch of structured text documents using a tensor with shape `[num_documents, (num_paragraphs), (num_sentences), (num_words)]` (where again parentheses are used to indicate ragged dimensions).

As with [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor), the **_rank_** of a ragged tensor is its total number of dimensions (including both ragged and uniform dimensions). A **_potentially ragged tensor_** is a value that might be either a [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) or a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor).

When describing the shape of a RaggedTensor, ragged dimensions are conventionally indicated by enclosing them in parentheses. For example, as you saw above, the shape of a 3D RaggedTensor that stores word embeddings for each word in a batch of sentences can be written as `[num_sentences, (num_words), embedding_size]`.

The [`RaggedTensor.shape`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#shape) attribute returns a [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape) for a ragged tensor where ragged dimensions have size `None`:

```
tf.ragged.constant([["Hi"], ["How", "are", "you"]]).shape
```
TensorShape([2, None])

The method [`tf.RaggedTensor.bounding_shape`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#bounding_shape) can be used to find a tight bounding shape for a given `RaggedTensor`:

```
print(tf.ragged.constant([["Hi"], ["How", "are", "you"]]).bounding_shape())
```
tf.Tensor([2 3], shape=(2,), dtype=int64)

Ragged vs sparse
----------------

A ragged tensor should _not_ be thought of as a type of sparse tensor. In particular, sparse tensors are _efficient encodings for [`tf.Tensor`](https://www.tensorflow.org/api\_docs/python/tf/Tensor)_ that model the same data in a compact format; but ragged tensor is an _extension to [`tf.Tensor`](https://www.tensorflow.org/api\_docs/python/tf/Tensor)_ that models an expanded class of data. This difference is crucial when defining operations:

*   Applying an op to a sparse or dense tensor should always give the same result.
*   Applying an op to a ragged or sparse tensor may give different results.

As an illustrative example, consider how array operations such as `concat`, `stack`, and `tile` are defined for ragged vs. sparse tensors. Concatenating ragged tensors joins each row to form a single row with the combined length:

![Image 6: Concatenating ragged tensors](https://www.tensorflow.org/images/ragged_tensors/ragged_concat.png)

```
ragged_x = tf.ragged.constant([["John"], ["a", "big", "dog"], ["my", "cat"]])
ragged_y = tf.ragged.constant([["fell", "asleep"], ["barked"], ["is", "fuzzy"]])
print(tf.concat([ragged_x, ragged_y], axis=1))
```
<tf.RaggedTensor [[b'John', b'fell', b'asleep'], [b'a', b'big', b'dog', b'barked'],
 [b'my', b'cat', b'is', b'fuzzy']]>

However, concatenating sparse tensors is equivalent to concatenating the corresponding dense tensors, as illustrated by the following example (where Ø indicates missing values):

![Image 7: Concatenating sparse tensors](https://www.tensorflow.org/images/ragged_tensors/sparse_concat.png)

```
sparse_x = ragged_x.to_sparse()
sparse_y = ragged_y.to_sparse()
sparse_result = tf.sparse.concat(sp_inputs=[sparse_x, sparse_y], axis=1)
print(tf.sparse.to_dense(sparse_result, ''))
```
tf.Tensor(
[[b'John' b'' b'' b'fell' b'asleep']
 [b'a' b'big' b'dog' b'barked' b'']
 [b'my' b'cat' b'' b'is' b'fuzzy']], shape=(3, 5), dtype=string)

For another example of why this distinction is important, consider the definition of “the mean value of each row” for an op such as [`tf.reduce_mean`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean). For a ragged tensor, the mean value for a row is the sum of the row’s values divided by the row’s width. But for a sparse tensor, the mean value for a row is the sum of the row’s values divided by the sparse tensor’s overall width (which is greater than or equal to the width of the longest row).

TensorFlow APIs
---------------

### Keras

[tf.keras](https://www.tensorflow.org/guide/keras) is TensorFlow's high-level API for building and training deep learning models. It doesn't have ragged support. But it does support masked tensors. So the easiest way to use a ragged tensor in a Keras model is to convert the ragged tensor to a dense tensor, using `.to_tensor()` and then using Keras's builtin masking:

```
# Task: predict whether each sentence is a question or not.
sentences = tf.constant(
    ['What makes you think she is a witch?',
     'She turned me into a newt.',
     'A newt?',
     'Well, I got better.'])
is_question = tf.constant([True, False, True, False])
```

```
# Preprocess the input strings.
hash_buckets = 1000
words = tf.strings.split(sentences, ' ')
hashed_words = tf.strings.to_hash_bucket_fast(words, hash_buckets)
hashed_words.to_list()
```
[[940, 203, 668, 387, 790, 320, 939, 185],
 [315, 515, 791, 181, 939, 787],
 [564, 205],
 [820, 180, 993, 739]]

```
hashed_words.to_tensor()
```
<tf.Tensor: shape=(4, 8), dtype=int64, numpy=
array([[940, 203, 668, 387, 790, 320, 939, 185],
       [315, 515, 791, 181, 939, 787,   0,   0],
       [564, 205,   0,   0,   0,   0,   0,   0],
       [820, 180, 993, 739,   0,   0,   0,   0]])>

```
tf.keras.Input?
```

```
# Build the Keras model.
keras_model = tf.keras.Sequential([
    tf.keras.layers.Embedding(hash_buckets, 16, mask_zero=True),
    tf.keras.layers.LSTM(32, return_sequences=True, use_bias=False),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(32),
    tf.keras.layers.Activation(tf.nn.relu),
    tf.keras.layers.Dense(1)
])

keras_model.compile(loss='binary_crossentropy', optimizer='rmsprop')
keras_model.fit(hashed_words.to_tensor(), is_question, epochs=5)
```
Epoch 1/5
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1724721648.311913   10235 service.cc:146] XLA service 0x7f82d4008680 initialized for platform CUDA (this does not guarantee that XLA will be used). Devices:
I0000 00:00:1724721648.311945   10235 service.cc:154]   StreamExecutor device (0): Tesla T4, Compute Capability 7.5
I0000 00:00:1724721648.311949   10235 service.cc:154]   StreamExecutor device (1): Tesla T4, Compute Capability 7.5
I0000 00:00:1724721648.311952   10235 service.cc:154]   StreamExecutor device (2): Tesla T4, Compute Capability 7.5
I0000 00:00:1724721648.311955   10235 service.cc:154]   StreamExecutor device (3): Tesla T4, Compute Capability 7.5
1/1 ━━━━━━━━━━━━━━━━━━━━ 4s 4s/step - loss: 8.0590
Epoch 2/5
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 47ms/step - loss: 8.0590
Epoch 3/5
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 44ms/step - loss: 8.0590
Epoch 4/5
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 44ms/step - loss: 8.0590
Epoch 5/5
I0000 00:00:1724721650.626376   10235 device_compiler.h:188] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 43ms/step - loss: 8.0590
<keras.src.callbacks.history.History at 0x7f8444309fd0>

```
print(keras_model.predict(hashed_words.to_tensor()))
```
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 407ms/step
[[-0.00517703]
 [-0.00227403]
 [-0.00706224]
 [-0.00354813]]

### tf.Example

[tf.Example](https://www.tensorflow.org/tutorials/load_data/tfrecord) is a standard [protobuf](https://developers.google.com/protocol-buffers/) encoding for TensorFlow data. Data encoded with `tf.Example`s often includes variable-length features. For example, the following code defines a batch of four `tf.Example` messages with different feature lengths:

```
import google.protobuf.text_format as pbtext

def build_tf_example(s):
  return pbtext.Merge(s, tf.train.Example()).SerializeToString()

example_batch = [
  build_tf_example(r'''
    features {
      feature {key: "colors" value {bytes_list {value: ["red", "blue"]} } }
      feature {key: "lengths" value {int64_list {value: [7]} } } }'''),
  build_tf_example(r'''
    features {
      feature {key: "colors" value {bytes_list {value: ["orange"]} } }
      feature {key: "lengths" value {int64_list {value: []} } } }'''),
  build_tf_example(r'''
    features {
      feature {key: "colors" value {bytes_list {value: ["black", "yellow"]} } }
      feature {key: "lengths" value {int64_list {value: [1, 3]} } } }'''),
  build_tf_example(r'''
    features {
      feature {key: "colors" value {bytes_list {value: ["green"]} } }
      feature {key: "lengths" value {int64_list {value: [3, 5, 2]} } } }''')]
```

You can parse this encoded data using [`tf.io.parse_example`](https://www.tensorflow.org/api_docs/python/tf/io/parse_example), which takes a tensor of serialized strings and a feature specification dictionary, and returns a dictionary mapping feature names to tensors. To read the variable-length features into ragged tensors, you simply use [`tf.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature) in the feature specification dictionary:

```
feature_specification = {
    'colors': tf.io.RaggedFeature(tf.string),
    'lengths': tf.io.RaggedFeature(tf.int64),
}
feature_tensors = tf.io.parse_example(example_batch, feature_specification)
for name, value in feature_tensors.items():
  print("{}={}".format(name, value))
```
colors=<tf.RaggedTensor [[b'red', b'blue'], [b'orange'], [b'black', b'yellow'], [b'green']]>
lengths=<tf.RaggedTensor [[7], [], [1, 3], [3, 5, 2]]>

[`tf.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature) can also be used to read features with multiple ragged dimensions. For details, refer to the [API documentation](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature).

### Datasets

[tf.data](https://www.tensorflow.org/guide/data) is an API that enables you to build complex input pipelines from simple, reusable pieces. Its core data structure is [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset), which represents a sequence of elements, in which each element consists of one or more components.

```
# Helper function used to print datasets in the examples below.
def print_dictionary_dataset(dataset):
  for i, element in enumerate(dataset):
    print("Element {}:".format(i))
    for (feature_name, feature_value) in element.items():
      print('{:>14} = {}'.format(feature_name, feature_value))
```

#### Building Datasets with ragged tensors

Datasets can be built from ragged tensors using the same methods that are used to build them from [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)s or NumPy `array`s, such as [`Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices):

```
dataset = tf.data.Dataset.from_tensor_slices(feature_tensors)
print_dictionary_dataset(dataset)
```
Element 0:
        colors = [b'red' b'blue']
       lengths = [7]
Element 1:
        colors = [b'orange']
       lengths = []
Element 2:
        colors = [b'black' b'yellow']
       lengths = [1 3]
Element 3:
        colors = [b'green']
       lengths = [3 5 2]

#### Batching and unbatching Datasets with ragged tensors

Datasets with ragged tensors can be batched (which combines _n_ consecutive elements into a single elements) using the [`Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch) method.

```
batched_dataset = dataset.batch(2)
print_dictionary_dataset(batched_dataset)
```
Element 0:
        colors = <tf.RaggedTensor [[b'red', b'blue'], [b'orange']]>
       lengths = <tf.RaggedTensor [[7], []]>
Element 1:
        colors = <tf.RaggedTensor [[b'black', b'yellow'], [b'green']]>
       lengths = <tf.RaggedTensor [[1, 3], [3, 5, 2]]>

Conversely, a batched dataset can be transformed into a flat dataset using [`Dataset.unbatch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#unbatch).

```
unbatched_dataset = batched_dataset.unbatch()
print_dictionary_dataset(unbatched_dataset)
```
Element 0:
        colors = [b'red' b'blue']
       lengths = [7]
Element 1:
        colors = [b'orange']
       lengths = []
Element 2:
        colors = [b'black' b'yellow']
       lengths = [1 3]
Element 3:
        colors = [b'green']
       lengths = [3 5 2]

#### Batching Datasets with variable-length non-ragged tensors

If you have a Dataset that contains non-ragged tensors, and tensor lengths vary across elements, then you can batch those non-ragged tensors into ragged tensors by applying the `dense_to_ragged_batch` transformation:

```
non_ragged_dataset = tf.data.Dataset.from_tensor_slices([1, 5, 3, 2, 8])
non_ragged_dataset = non_ragged_dataset.map(tf.range)
batched_non_ragged_dataset = non_ragged_dataset.apply(
    tf.data.experimental.dense_to_ragged_batch(2))
for element in batched_non_ragged_dataset:
  print(element)
```
WARNING:tensorflow:From /tmpfs/tmp/ipykernel_10064/1427668168.py:4: dense_to_ragged_batch (from tensorflow.python.data.experimental.ops.batching) is deprecated and will be removed in a future version.
Instructions for updating:
Use `tf.data.Dataset.ragged_batch` instead.
<tf.RaggedTensor [[0], [0, 1, 2, 3, 4]]>
<tf.RaggedTensor [[0, 1, 2], [0, 1]]>
<tf.RaggedTensor [[0, 1, 2, 3, 4, 5, 6, 7]]>

#### Transforming Datasets with ragged tensors

You can also create or transform ragged tensors in Datasets using [`Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map):

```
def transform_lengths(features):
  return {
      'mean_length': tf.math.reduce_mean(features['lengths']),
      'length_ranges': tf.ragged.range(features['lengths'])}
transformed_dataset = dataset.map(transform_lengths)
print_dictionary_dataset(transformed_dataset)
```
Element 0:
   mean_length = 7
 length_ranges = <tf.RaggedTensor [[0, 1, 2, 3, 4, 5, 6]]>
Element 1:
   mean_length = 0
 length_ranges = <tf.RaggedTensor []>
Element 2:
   mean_length = 2
 length_ranges = <tf.RaggedTensor [[0], [0, 1, 2]]>
Element 3:
   mean_length = 3
 length_ranges = <tf.RaggedTensor [[0, 1, 2], [0, 1, 2, 3, 4], [0, 1]]>

### tf.function

[tf.function](https://www.tensorflow.org/guide/function) is a decorator that precomputes TensorFlow graphs for Python functions, which can substantially improve the performance of your TensorFlow code. Ragged tensors can be used transparently with [`@tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)-decorated functions. For example, the following function works with both ragged and non-ragged tensors:

```
@tf.function
def make_palindrome(x, axis):
  return tf.concat([x, tf.reverse(x, [axis])], axis)
```

```
make_palindrome(tf.constant([[1, 2], [3, 4], [5, 6]]), axis=1)
```
<tf.Tensor: shape=(3, 4), dtype=int32, numpy=
array([[1, 2, 2, 1],
       [3, 4, 4, 3],
       [5, 6, 6, 5]], dtype=int32)>

```
make_palindrome(tf.ragged.constant([[1, 2], [3], [4, 5, 6]]), axis=1)
```
2024-08-27 01:20:51.662289: W tensorflow/core/grappler/optimizers/loop_optimizer.cc:933] Skipping loop optimization for Merge node with control input: RaggedConcat/assert_equal_1/Assert/AssertGuard/branch_executed/_9
<tf.RaggedTensor [[1, 2, 2, 1], [3, 3], [4, 5, 6, 6, 5, 4]]>

If you wish to explicitly specify the `input_signature` for the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function), then you can do so using [`tf.RaggedTensorSpec`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensorSpec).

```
@tf.function(
    input_signature=[tf.RaggedTensorSpec(shape=[None, None], dtype=tf.int32)])
def max_and_min(rt):
  return (tf.math.reduce_max(rt, axis=-1), tf.math.reduce_min(rt, axis=-1))

max_and_min(tf.ragged.constant([[1, 2], [3], [4, 5, 6]]))
```
(<tf.Tensor: shape=(3,), dtype=int32, numpy=array([2, 3, 6], dtype=int32)>,
 <tf.Tensor: shape=(3,), dtype=int32, numpy=array([1, 3, 4], dtype=int32)>)

#### Concrete functions

[Concrete functions](https://www.tensorflow.org/guide/function#obtaining_concrete_functions) encapsulate individual traced graphs that are built by [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). Ragged tensors can be used transparently with concrete functions.

```
@tf.function
def increment(x):
  return x + 1

rt = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
cf = increment.get_concrete_function(rt)
print(cf(rt))
```
<tf.RaggedTensor [[2, 3], [4], [5, 6, 7]]>

### SavedModels

A [SavedModel](https://www.tensorflow.org/guide/saved_model) is a serialized TensorFlow program, including both weights and computation. It can be built from a Keras model or from a custom model. In either case, ragged tensors can be used transparently with the functions and methods defined by a SavedModel.

#### Example: saving a Keras model

```
import tempfile

keras_module_path = tempfile.mkdtemp()
keras_model.save(keras_module_path+"/my_model.keras")

imported_model = tf.keras.models.load_model(keras_module_path+"/my_model.keras")

imported_model(hashed_words.to_tensor())
```
<tf.Tensor: shape=(4, 1), dtype=float32, numpy=
array([[-0.00517703],
       [-0.00227403],
       [-0.00706224],
       [-0.00354813]], dtype=float32)>

#### Example: saving a custom model

```
class CustomModule(tf.Module):
  def __init__(self, variable_value):
    super(CustomModule, self).__init__()
    self.v = tf.Variable(variable_value)

  @tf.function
  def grow(self, x):
    return x * self.v

module = CustomModule(100.0)

# Before saving a custom model, you must ensure that concrete functions are
# built for each input signature that you will need.
module.grow.get_concrete_function(tf.RaggedTensorSpec(shape=[None, None],
                                                      dtype=tf.float32))

custom_module_path = tempfile.mkdtemp()
tf.saved_model.save(module, custom_module_path)
imported_model = tf.saved_model.load(custom_module_path)
imported_model.grow(tf.ragged.constant([[1.0, 4.0, 3.0], [2.0]]))
```
INFO:tensorflow:Assets written to: /tmpfs/tmp/tmpkmr703wo/assets
INFO:tensorflow:Assets written to: /tmpfs/tmp/tmpkmr703wo/assets
<tf.RaggedTensor [[100.0, 400.0, 300.0], [200.0]]>

Overloaded operators
--------------------

The `RaggedTensor` class overloads the standard Python arithmetic and comparison operators, making it easy to perform basic elementwise math:

```
x = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
y = tf.ragged.constant([[1, 1], [2], [3, 3, 3]])
print(x + y)
```
<tf.RaggedTensor [[2, 3], [5], [7, 8, 9]]>

Since the overloaded operators perform elementwise computations, the inputs to all binary operations must have the same shape or be broadcastable to the same shape. In the simplest broadcasting case, a single scalar is combined elementwise with each value in a ragged tensor:

```
x = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
print(x + 3)
```
<tf.RaggedTensor [[4, 5], [6], [7, 8, 9]]>

For a discussion of more advanced cases, check the section on **Broadcasting**.

Ragged tensors overload the same set of operators as normal `Tensor`s: the unary operators `-`, `~`, and `abs()`; and the binary operators `+`, `-`, `*`, `/`, `//`, `%`, `**`, `&`, `|`, `^`, `==`, `<`, `<=`, `>`, and `>=`.

Indexing
--------

Ragged tensors support Python-style indexing, including multidimensional indexing and slicing. The following examples demonstrate ragged tensor indexing with a 2D and a 3D ragged tensor.

### Indexing examples: 2D ragged tensor

```
queries = tf.ragged.constant(
    [['Who', 'is', 'George', 'Washington'],
     ['What', 'is', 'the', 'weather', 'tomorrow'],
     ['Goodnight']])
```

```
print(queries[1])                   # A single query
```
tf.Tensor([b'What' b'is' b'the' b'weather' b'tomorrow'], shape=(5,), dtype=string)

```
print(queries[1, 2])                # A single word
```
tf.Tensor(b'the', shape=(), dtype=string)

```
print(queries[1:])                  # Everything but the first row
```
<tf.RaggedTensor [[b'What', b'is', b'the', b'weather', b'tomorrow'], [b'Goodnight']]>

```
print(queries[:, :3])               # The first 3 words of each query
```
<tf.RaggedTensor [[b'Who', b'is', b'George'], [b'What', b'is', b'the'], [b'Goodnight']]>

```
print(queries[:, -2:])              # The last 2 words of each query
```
<tf.RaggedTensor [[b'George', b'Washington'], [b'weather', b'tomorrow'], [b'Goodnight']]>

### Indexing examples: 3D ragged tensor

```
rt = tf.ragged.constant([[[1, 2, 3], [4]],
                         [[5], [], [6]],
                         [[7]],
                         [[8, 9], [10]]])
```

```
print(rt[1])                        # Second row (2D RaggedTensor)
```
<tf.RaggedTensor [[5], [], [6]]>

```
print(rt[3, 0])                     # First element of fourth row (1D Tensor)
```
tf.Tensor([8 9], shape=(2,), dtype=int32)

```
print(rt[:, 1:3])                   # Items 1-3 of each row (3D RaggedTensor)
```
<tf.RaggedTensor [[[4]], [[], [6]], [], [[10]]]>

```
print(rt[:, -1:])                   # Last item of each row (3D RaggedTensor)
```
<tf.RaggedTensor [[[4]],

 [[6]],

 [[7]],

 [[10]]]>

`RaggedTensor`s support multidimensional indexing and slicing with one restriction: indexing into a ragged dimension is not allowed. This case is problematic because the indicated value may exist in some rows but not others. In such cases, it's not obvious whether you should (1) raise an `IndexError`; (2) use a default value; or (3) skip that value and return a tensor with fewer rows than you started with. Following the [guiding principles of Python](https://www.python.org/dev/peps/pep-0020/) ("In the face of ambiguity, refuse the temptation to guess"), this operation is currently disallowed.

Tensor type conversion
----------------------

The `RaggedTensor` class defines methods that can be used to convert between `RaggedTensor`s and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)s or `tf.SparseTensors`:

```
ragged_sentences = tf.ragged.constant([
    ['Hi'], ['Welcome', 'to', 'the', 'fair'], ['Have', 'fun']])
```

```
# RaggedTensor -> Tensor
print(ragged_sentences.to_tensor(default_value='', shape=[None, 10]))
```
tf.Tensor(
[[b'Hi' b'' b'' b'' b'' b'' b'' b'' b'' b'']
 [b'Welcome' b'to' b'the' b'fair' b'' b'' b'' b'' b'' b'']
 [b'Have' b'fun' b'' b'' b'' b'' b'' b'' b'' b'']], shape=(3, 10), dtype=string)

```
# Tensor -> RaggedTensor
x = [[1, 3, -1, -1], [2, -1, -1, -1], [4, 5, 8, 9]]
print(tf.RaggedTensor.from_tensor(x, padding=-1))
```
<tf.RaggedTensor [[1, 3], [2], [4, 5, 8, 9]]>

```
#RaggedTensor -> SparseTensor
print(ragged_sentences.to_sparse())
```
SparseTensor(indices=tf.Tensor(
[[0 0]
 [1 0]
 [1 1]
 [1 2]
 [1 3]
 [2 0]
 [2 1]], shape=(7, 2), dtype=int64), values=tf.Tensor([b'Hi' b'Welcome' b'to' b'the' b'fair' b'Have' b'fun'], shape=(7,), dtype=string), dense_shape=tf.Tensor([3 4], shape=(2,), dtype=int64))

```
# SparseTensor -> RaggedTensor
st = tf.SparseTensor(indices=[[0, 0], [2, 0], [2, 1]],
                     values=['a', 'b', 'c'],
                     dense_shape=[3, 3])
print(tf.RaggedTensor.from_sparse(st))
```
<tf.RaggedTensor [[b'a'], [], [b'b', b'c']]>

Evaluating ragged tensors
-------------------------

To access the values in a ragged tensor, you can:

1.   Use [`tf.RaggedTensor.to_list`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#to_list) to convert the ragged tensor to a nested Python list.
2.   Use [`tf.RaggedTensor.numpy`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#numpy) to convert the ragged tensor to a NumPy array whose values are nested NumPy arrays.
3.   Decompose the ragged tensor into its components, using the [`tf.RaggedTensor.values`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#values) and [`tf.RaggedTensor.row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#row_splits) properties, or row-partitioning methods such as [`tf.RaggedTensor.row_lengths`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#row_lengths) and [`tf.RaggedTensor.value_rowids`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#value_rowids).
4.   Use Python indexing to select values from the ragged tensor.

```
rt = tf.ragged.constant([[1, 2], [3, 4, 5], [6], [], [7]])
print("Python list:", rt.to_list())
print("NumPy array:", rt.numpy())
print("Values:", rt.values.numpy())
print("Splits:", rt.row_splits.numpy())
print("Indexed value:", rt[1].numpy())
```
Python list: [[1, 2], [3, 4, 5], [6], [], [7]]
NumPy array: [array([1, 2], dtype=int32) array([3, 4, 5], dtype=int32)
 array([6], dtype=int32) array([], dtype=int32) array([7], dtype=int32)]
Values: [1 2 3 4 5 6 7]
Splits: [0 2 5 6 6 7]
Indexed value: [3 4 5]

Ragged Shapes
-------------

The shape of a tensor specifies the size of each axis. For example, the shape of `[[1, 2], [3, 4], [5, 6]]` is `[3, 2]`, since there are 3 rows and 2 columns. TensorFlow has two separate but related ways to describe shapes:

*   **_static shape_**: Information about axis sizes that is known statically (e.g., while tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)). May be partially specified.

*   **_dynamic shape_**: Runtime information about the axis sizes.

### Static shape

A Tensor's static shape contains information about its axis sizes that is known at graph-construction time. For both [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) and [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor), it is available using the `.shape` property, and is encoded using [`tf.TensorShape`](https://www.tensorflow.org/api_docs/python/tf/TensorShape):

```
x = tf.constant([[1, 2], [3, 4], [5, 6]])
x.shape  # shape of a tf.tensor
```
TensorShape([3, 2])

```
rt = tf.ragged.constant([[1], [2, 3], [], [4]])
rt.shape  # shape of a tf.RaggedTensor
```
TensorShape([4, None])

The static shape of a ragged dimension is always `None` (i.e., unspecified). However, the inverse is not true -- if a `TensorShape` dimension is `None`, then that could indicate that the dimension is ragged, _or_ it could indicate that the dimension is uniform but that its size is not statically known.

### Dynamic shape

A tensor's dynamic shape contains information about its axis sizes that is known when the graph is run. It is constructed using the [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape) operation. For [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor), [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape) returns the shape as a 1D integer `Tensor`, where `tf.shape(x)[i]` is the size of axis `i`.

```
x = tf.constant([['a', 'b'], ['c', 'd'], ['e', 'f']])
tf.shape(x)
```
<tf.Tensor: shape=(2,), dtype=int32, numpy=array([3, 2], dtype=int32)>

However, a 1D `Tensor` is not expressive enough to describe the shape of a [`tf.RaggedTensor`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor). Instead, the dynamic shape for ragged tensors is encoded using a dedicated type, [`tf.experimental.DynamicRaggedShape`](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape). In the following example, the `DynamicRaggedShape` returned by [`tf.shape(rt)`](https://www.tensorflow.org/api_docs/python/tf/shape) indicates that the ragged tensor has 4 rows, with lengths 1, 3, 0, and 2:

```
rt = tf.ragged.constant([[1], [2, 3, 4], [], [5, 6]])
rt_shape = tf.shape(rt)
print(rt_shape)
```
<DynamicRaggedShape lengths=[4, (1, 3, 0, 2)] num_row_partitions=1>

#### Dynamic shape: operations

`DynamicRaggedShape`s can be used with most TensorFlow ops that expect shapes, including [`tf.reshape`](https://www.tensorflow.org/api_docs/python/tf/reshape), [`tf.zeros`](https://www.tensorflow.org/api_docs/python/tf/zeros), [`tf.ones`](https://www.tensorflow.org/api_docs/python/tf/ones). [`tf.fill`](https://www.tensorflow.org/api_docs/python/tf/fill), [`tf.broadcast_dynamic_shape`](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape), and [`tf.broadcast_to`](https://www.tensorflow.org/api_docs/python/tf/broadcast_to).

```
print(f"tf.reshape(x, rt_shape) = {tf.reshape(x, rt_shape)}")
print(f"tf.zeros(rt_shape) = {tf.zeros(rt_shape)}")
print(f"tf.ones(rt_shape) = {tf.ones(rt_shape)}")
print(f"tf.fill(rt_shape, 9) = {tf.fill(rt_shape, 'x')}")
```
tf.reshape(x, rt_shape) = <tf.RaggedTensor [[b'a'], [b'b', b'c', b'd'], [], [b'e', b'f']]>
tf.zeros(rt_shape) = <tf.RaggedTensor [[0.0], [0.0, 0.0, 0.0], [], [0.0, 0.0]]>
tf.ones(rt_shape) = <tf.RaggedTensor [[1.0], [1.0, 1.0, 1.0], [], [1.0, 1.0]]>
tf.fill(rt_shape, 9) = <tf.RaggedTensor [[b'x'], [b'x', b'x', b'x'], [], [b'x', b'x']]>

#### Dynamic shape: indexing and slicing

`DynamicRaggedShape` can be also be indexed to get the sizes of uniform dimensions. For example, we can find the number of rows in a raggedtensor using `tf.shape(rt)[0]` (just as we would for a non-ragged tensor):

```
rt_shape[0]
```
<tf.Tensor: shape=(), dtype=int32, numpy=4>

However, it is an error to use indexing to try to retrieve the size of a ragged dimension, since it doesn't have a single size. (Since `RaggedTensor` keeps track of which axes are ragged, this error is only thrown during eager execution or when tracing a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function); it will never be thrown when executing a concrete function.)

```
try:
  rt_shape[1]
except ValueError as e:
  print("Got expected ValueError:", e)
```
Got expected ValueError: Index 1 is not uniform

`DynamicRaggedShape`s can also be sliced, as long as the slice either begins with axis `0`, or contains only dense dimensions.

```
rt_shape[:1]
```
<DynamicRaggedShape lengths=[4] num_row_partitions=0>

#### Dynamic shape: encoding

`DynamicRaggedShape` is encoded using two fields:

*   `inner_shape`: An integer vector giving the shape of a dense [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor).
*   `row_partitions`: A list of [`tf.experimental.RowPartition`](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition) objects, describing how the outermost dimension of that inner shape should be partitioned to add ragged axes.

For more information about row partitions, see the "RaggedTensor encoding" section below, and the API docs for [`tf.experimental.RowPartition`](https://www.tensorflow.org/api_docs/python/tf/experimental/RowPartition).

#### Dynamic shape: construction

`DynamicRaggedShape` is most often constructed by applying [`tf.shape`](https://www.tensorflow.org/api_docs/python/tf/shape) to a `RaggedTensor`, but it can also be constructed directly:

```
tf.experimental.DynamicRaggedShape(
    row_partitions=[tf.experimental.RowPartition.from_row_lengths([5, 3, 2])],
    inner_shape=[10, 8])
```
<DynamicRaggedShape lengths=[3, (5, 3, 2), 8] num_row_partitions=1>

If the lengths of all rows are known statically, [`DynamicRaggedShape.from_lengths`](https://www.tensorflow.org/api_docs/python/tf/experimental/DynamicRaggedShape#from_lengths) can also be used to construct a dynamic ragged shape. (This is mostly useful for testing and demonstration code, since it's rare for the lengths of ragged dimensions to be known statically).

```
tf.experimental.DynamicRaggedShape.from_lengths([4, (2, 1, 0, 8), 12])
```
<DynamicRaggedShape lengths=[4, (2, 1, 0, 8), 12] num_row_partitions=1>

### Broadcasting

Broadcasting is the process of making tensors with different shapes have compatible shapes for elementwise operations. For more background on broadcasting, refer to:

*   [NumPy: Broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)
*   [`tf.broadcast_dynamic_shape`](https://www.tensorflow.org/api_docs/python/tf/broadcast_dynamic_shape)
*   [`tf.broadcast_to`](https://www.tensorflow.org/api_docs/python/tf/broadcast_to)

The basic steps for broadcasting two inputs `x` and `y` to have compatible shapes are:

1.   If `x` and `y` do not have the same number of dimensions, then add outer dimensions (with size 1) until they do.

2.   For each dimension where `x` and `y` have different sizes:

*   If `x` or `y` have size `1` in dimension `d`, then repeat its values across dimension `d` to match the other input's size.
*   Otherwise, raise an exception (`x` and `y` are not broadcast compatible).

Where the size of a tensor in a uniform dimension is a single number (the size of slices across that dimension); and the size of a tensor in a ragged dimension is a list of slice lengths (for all slices across that dimension).

#### Broadcasting examples

```
# x       (2D ragged):  2 x (num_rows)
# y       (scalar)
# result  (2D ragged):  2 x (num_rows)
x = tf.ragged.constant([[1, 2], [3]])
y = 3
print(x + y)
```
<tf.RaggedTensor [[4, 5], [6]]>

```
# x         (2d ragged):  3 x (num_rows)
# y         (2d tensor):  3 x          1
# Result    (2d ragged):  3 x (num_rows)
x = tf.ragged.constant(
   [[10, 87, 12],
    [19, 53],
    [12, 32]])
y = [[1000], [2000], [3000]]
print(x + y)
```
<tf.RaggedTensor [[1010, 1087, 1012], [2019, 2053], [3012, 3032]]>

```
# x      (3d ragged):  2 x (r1) x 2
# y      (2d ragged):         1 x 1
# Result (3d ragged):  2 x (r1) x 2
x = tf.ragged.constant(
    [[[1, 2], [3, 4], [5, 6]],
     [[7, 8]]],
    ragged_rank=1)
y = tf.constant([[10]])
print(x + y)
```
<tf.RaggedTensor [[[11, 12],
  [13, 14],
  [15, 16]], [[17, 18]]]>

```
# x      (3d ragged):  2 x (r1) x (r2) x 1
# y      (1d tensor):                    3
# Result (3d ragged):  2 x (r1) x (r2) x 3
x = tf.ragged.constant(
    [
        [
            [[1], [2]],
            [],
            [[3]],
            [[4]],
        ],
        [
            [[5], [6]],
            [[7]]
        ]
    ],
    ragged_rank=2)
y = tf.constant([10, 20, 30])
print(x + y)
```
<tf.RaggedTensor [[[[11, 21, 31],
   [12, 22, 32]], [], [[13, 23, 33]], [[14, 24, 34]]],
 [[[15, 25, 35],
   [16, 26, 36]], [[17, 27, 37]]]]>

Here are some examples of shapes that do not broadcast:

```
# x      (2d ragged): 3 x (r1)
# y      (2d tensor): 3 x    4  # trailing dimensions do not match
x = tf.ragged.constant([[1, 2], [3, 4, 5, 6], [7]])
y = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
try:
  x + y
except tf.errors.InvalidArgumentError as exception:
  print(exception)
```
Condition x == y did not hold.
Indices of first 3 different values:
[[1]
 [2]
 [3]]
Corresponding x values:
[ 4  8 12]
Corresponding y values:
[2 6 7]
First 3 elements of x:
[0 4 8]
First 3 elements of y:
[0 2 6]

```
# x      (2d ragged): 3 x (r1)
# y      (2d ragged): 3 x (r2)  # ragged dimensions do not match.
x = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
y = tf.ragged.constant([[10, 20], [30, 40], [50]])
try:
  x + y
except tf.errors.InvalidArgumentError as exception:
  print(exception)
```
Condition x == y did not hold.
Indices of first 2 different values:
[[1]
 [3]]
Corresponding x values:
[3 6]
Corresponding y values:
[2 5]
First 3 elements of x:
[0 3 4]
First 3 elements of y:
[0 2 4]

```
# x      (3d ragged): 3 x (r1) x 2
# y      (3d ragged): 3 x (r1) x 3  # trailing dimensions do not match
x = tf.ragged.constant([[[1, 2], [3, 4], [5, 6]],
                        [[7, 8], [9, 10]]])
y = tf.ragged.constant([[[1, 2, 0], [3, 4, 0], [5, 6, 0]],
                        [[7, 8, 0], [9, 10, 0]]])
try:
  x + y
except tf.errors.InvalidArgumentError as exception:
  print(exception)
```
Condition x == y did not hold.
Indices of first 3 different values:
[[1]
 [2]
 [3]]
Corresponding x values:
[2 4 6]
Corresponding y values:
[3 6 9]
First 3 elements of x:
[0 2 4]
First 3 elements of y:
[0 3 6]

RaggedTensor encoding
---------------------

Ragged tensors are encoded using the `RaggedTensor` class. Internally, each `RaggedTensor` consists of:

*   A `values` tensor, which concatenates the variable-length rows into a flattened list.
*   A `row_partition`, which indicates how those flattened values are divided into rows.

![Image 8: RaggedTensor encoding](https://www.tensorflow.org/images/ragged_tensors/ragged_encoding_2.png)

The `row_partition` can be stored using four different encodings:

*   `row_splits` is an integer vector specifying the split points between rows.
*   `value_rowids` is an integer vector specifying the row index for each value.
*   `row_lengths` is an integer vector specifying the length of each row.
*   `uniform_row_length` is an integer scalar specifying a single length for all rows.

![Image 9: row_partition encodings](https://www.tensorflow.org/images/ragged_tensors/partition_encodings.png)

An integer scalar `nrows` can also be included in the `row_partition` encoding to account for empty trailing rows with `value_rowids` or empty rows with `uniform_row_length`.

```
rt = tf.RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2],
    row_splits=[0, 4, 4, 6, 7])
print(rt)
```
<tf.RaggedTensor [[3, 1, 4, 1], [], [5, 9], [2]]>

The choice of which encoding to use for row partitions is managed internally by ragged tensors to improve efficiency in some contexts. In particular, some of the advantages and disadvantages of the different row-partitioning schemes are:

*   **Efficient indexing**: The `row_splits` encoding enables constant-time indexing and slicing into ragged tensors.
*   **Efficient concatenation**: The `row_lengths` encoding is more efficient when concatenating ragged tensors, since row lengths do not change when two tensors are concatenated together.
*   **Small encoding size**: The `value_rowids` encoding is more efficient when storing ragged tensors that have a large number of empty rows, since the size of the tensor depends only on the total number of values. On the other hand, the `row_splits` and `row_lengths` encodings are more efficient when storing ragged tensors with longer rows, since they require only one scalar value for each row.
*   **Compatibility**: The `value_rowids` scheme matches the [segmentation](https://www.tensorflow.org/api_docs/python/tf/math#about_segmentation) format used by operations, such as `tf.segment_sum`. The `row_limits` scheme matches the format used by ops such as [`tf.sequence_mask`](https://www.tensorflow.org/api_docs/python/tf/sequence_mask).
*   **Uniform dimensions**: As discussed below, the `uniform_row_length` encoding is used to encode ragged tensors with uniform dimensions.

### Multiple ragged dimensions

A ragged tensor with multiple ragged dimensions is encoded by using a nested `RaggedTensor` for the `values` tensor. Each nested `RaggedTensor` adds a single ragged dimension.

![Image 10: Encoding of a ragged tensor with multiple ragged dimensions (rank 2)](https://www.tensorflow.org/images/ragged_tensors/ragged_rank_2.png)

```
rt = tf.RaggedTensor.from_row_splits(
    values=tf.RaggedTensor.from_row_splits(
        values=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        row_splits=[0, 3, 3, 5, 9, 10]),
    row_splits=[0, 1, 1, 5])
print(rt)
print("Shape: {}".format(rt.shape))
print("Number of partitioned dimensions: {}".format(rt.ragged_rank))
```
<tf.RaggedTensor [[[10, 11, 12]], [], [[], [13, 14], [15, 16, 17, 18], [19]]]>
Shape: (3, None, None)
Number of partitioned dimensions: 2

The factory function [`tf.RaggedTensor.from_nested_row_splits`](https://www.tensorflow.org/api_docs/python/tf/RaggedTensor#from_nested_row_splits) may be used to construct a RaggedTensor with multiple ragged dimensions directly by providing a list of `row_splits` tensors:

```
rt = tf.RaggedTensor.from_nested_row_splits(
    flat_values=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
    nested_row_splits=([0, 1, 1, 5], [0, 3, 3, 5, 9, 10]))
print(rt)
```
<tf.RaggedTensor [[[10, 11, 12]], [], [[], [13, 14], [15, 16, 17, 18], [19]]]>

### Ragged rank and flat values

A ragged tensor's **_ragged rank_** is the number of times that the underlying `values` tensor has been partitioned (i.e. the nesting depth of `RaggedTensor` objects). The innermost `values` tensor is known as its **_flat\_values_**. In the following example, `conversations` has ragged_rank=3, and its `flat_values` is a 1D `Tensor` with 24 strings:

```
# shape = [batch, (paragraph), (sentence), (word)]
conversations = tf.ragged.constant(
    [[[["I", "like", "ragged", "tensors."]],
      [["Oh", "yeah?"], ["What", "can", "you", "use", "them", "for?"]],
      [["Processing", "variable", "length", "data!"]]],
     [[["I", "like", "cheese."], ["Do", "you?"]],
      [["Yes."], ["I", "do."]]]])
conversations.shape
```
TensorShape([2, None, None, None])

```
assert conversations.ragged_rank == len(conversations.nested_row_splits)
conversations.ragged_rank  # Number of partitioned dimensions.
```
3

```
conversations.flat_values.numpy()
```
array([b'I', b'like', b'ragged', b'tensors.', b'Oh', b'yeah?', b'What',
       b'can', b'you', b'use', b'them', b'for?', b'Processing',
       b'variable', b'length', b'data!', b'I', b'like', b'cheese.', b'Do',
       b'you?', b'Yes.', b'I', b'do.'], dtype=object)

### Uniform inner dimensions

Ragged tensors with uniform inner dimensions are encoded by using a multidimensional [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) for the flat_values (i.e., the innermost `values`).

![Image 11: Encoding of ragged tensors with uniform inner dimensions](https://www.tensorflow.org/images/ragged_tensors/uniform_inner.png)

```
rt = tf.RaggedTensor.from_row_splits(
    values=[[1, 3], [0, 0], [1, 3], [5, 3], [3, 3], [1, 2]],
    row_splits=[0, 3, 4, 6])
print(rt)
print("Shape: {}".format(rt.shape))
print("Number of partitioned dimensions: {}".format(rt.ragged_rank))
print("Flat values shape: {}".format(rt.flat_values.shape))
print("Flat values:\n{}".format(rt.flat_values))
```
<tf.RaggedTensor [[[1, 3],
  [0, 0],
  [1, 3]], [[5, 3]], [[3, 3],
                      [1, 2]]]>
Shape: (3, None, 2)
Number of partitioned dimensions: 1
Flat values shape: (6, 2)
Flat values:
[[1 3]
 [0 0]
 [1 3]
 [5 3]
 [3 3]
 [1 2]]

### Uniform non-inner dimensions

Ragged tensors with uniform non-inner dimensions are encoded by partitioning rows with `uniform_row_length`.

![Image 12: Encoding of ragged tensors with uniform non-inner dimensions](https://www.tensorflow.org/images/ragged_tensors/uniform_outer.png)

```
rt = tf.RaggedTensor.from_uniform_row_length(
    values=tf.RaggedTensor.from_row_splits(
        values=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
        row_splits=[0, 3, 5, 9, 10]),
    uniform_row_length=2)
print(rt)
print("Shape: {}".format(rt.shape))
print("Number of partitioned dimensions: {}".format(rt.ragged_rank))
```
<tf.RaggedTensor [[[10, 11, 12], [13, 14]],
 [[15, 16, 17, 18], [19]]]>
Shape: (2, 2, None)
Number of partitioned dimensions: 2

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-27 UTC.
