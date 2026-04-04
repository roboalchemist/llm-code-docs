# Source: https://www.tensorflow.org/guide/tensor_slicing

Title: Introduction to tensor slicing

URL Source: https://www.tensorflow.org/guide/tensor_slicing

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/tensor_slicing#main-content)

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

Introduction to tensor slicing Stay organized with collections  Save and categorize content based on your preferences.
----------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/tensor_slicing#setup)
*   [Extract tensor slices](https://www.tensorflow.org/guide/tensor_slicing#extract_tensor_slices)
*   [Insert data into tensors](https://www.tensorflow.org/guide/tensor_slicing#insert_data_into_tensors)
*   [Further reading and resources](https://www.tensorflow.org/guide/tensor_slicing#further_reading_and_resources)

When working on ML applications such as object detection and NLP, it is sometimes necessary to work with sub-sections (slices) of tensors. For example, if your model architecture includes routing, where one layer might control which training example gets routed to the next layer. In this case, you could use tensor slicing ops to split the tensors up and put them back together in the right order.

In NLP applications, you can use tensor slicing to perform word masking while training. For example, you can generate training data from a list of sentences by choosing a word index to mask in each sentence, taking the word out as a label, and then replacing the chosen word with a mask token.

In this guide, you will learn how to use the TensorFlow APIs to:

*   Extract slices from a tensor
*   Insert data at specific indices in a tensor

This guide assumes familiarity with tensor indexing. Read the indexing sections of the [Tensor](https://www.tensorflow.org/guide/tensor#indexing) and [TensorFlow NumPy](https://www.tensorflow.org/guide/tf_numpy#indexing) guides before getting started with this guide.

Setup
-----

```
import tensorflow as tf
import numpy as np
```
2024-08-15 02:59:22.387959: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-15 02:59:22.409014: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-15 02:59:22.415391: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

Perform NumPy-like tensor slicing using [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice).

```
t1 = tf.constant([0, 1, 2, 3, 4, 5, 6, 7])

print(tf.slice(t1,
               begin=[1],
               size=[3]))
```
tf.Tensor([1 2 3], shape=(3,), dtype=int32)
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1723690765.029742  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.033507  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.037154  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.040869  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.052765  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.056359  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.059719  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.063138  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.066532  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.070040  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.073650  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690765.077235  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.300773  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.302797  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.304766  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.306851  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.308843  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.310723  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.312589  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.314574  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.316423  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.318291  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.320168  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.322150  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.360968  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.362946  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.364849  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.366867  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.368710  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.370591  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.372447  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.374435  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.376302  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.378677  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.380966  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690766.383365  169903 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355

Alternatively, you can use a more Pythonic syntax. Note that tensor slices are evenly spaced over a start-stop range.

```
print(t1[1:4])
```
tf.Tensor([1 2 3], shape=(3,), dtype=int32)

![Image 1](https://www.tensorflow.org/static/guide/images/tf_slicing/slice_1d_1.png)

```
print(t1[-3:])
```
tf.Tensor([5 6 7], shape=(3,), dtype=int32)

![Image 2](https://www.tensorflow.org/static/guide/images/tf_slicing/slice_1d_2.png)

For 2-dimensional tensors,you can use something like:

```
t2 = tf.constant([[0, 1, 2, 3, 4],
                  [5, 6, 7, 8, 9],
                  [10, 11, 12, 13, 14],
                  [15, 16, 17, 18, 19]])

print(t2[:-1, 1:3])
```
tf.Tensor(
[[ 1  2]
 [ 6  7]
 [11 12]], shape=(3, 2), dtype=int32)

![Image 3](https://www.tensorflow.org/static/guide/images/tf_slicing/slice_2d_1.png)

You can use [`tf.slice`](https://www.tensorflow.org/api_docs/python/tf/slice) on higher dimensional tensors as well.

```
t3 = tf.constant([[[1, 3, 5, 7],
                   [9, 11, 13, 15]],
                  [[17, 19, 21, 23],
                   [25, 27, 29, 31]]
                  ])

print(tf.slice(t3,
               begin=[1, 1, 0],
               size=[1, 1, 2]))
```
tf.Tensor([[[25 27]]], shape=(1, 1, 2), dtype=int32)

You can also use [`tf.strided_slice`](https://www.tensorflow.org/api_docs/python/tf/strided_slice) to extract slices of tensors by 'striding' over the tensor dimensions.

Use [`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather) to extract specific indices from a single axis of a tensor.

```
print(tf.gather(t1,
                indices=[0, 3, 6]))

# This is similar to doing

t1[::3]
```
tf.Tensor([0 3 6], shape=(3,), dtype=int32)
<tf.Tensor: shape=(3,), dtype=int32, numpy=array([0, 3, 6], dtype=int32)>

![Image 4](https://www.tensorflow.org/static/guide/images/tf_slicing/slice_1d_3.png)

[`tf.gather`](https://www.tensorflow.org/api_docs/python/tf/gather) does not require indices to be evenly spaced.

```
alphabet = tf.constant(list('abcdefghijklmnopqrstuvwxyz'))

print(tf.gather(alphabet,
                indices=[2, 0, 19, 18]))
```
tf.Tensor([b'c' b'a' b't' b's'], shape=(4,), dtype=string)

![Image 5](https://www.tensorflow.org/static/guide/images/tf_slicing/gather_1.png)

To extract slices from multiple axes of a tensor, use [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd). This is useful when you want to gather the elements of a matrix as opposed to just its rows or columns.

```
t4 = tf.constant([[0, 5],
                  [1, 6],
                  [2, 7],
                  [3, 8],
                  [4, 9]])

print(tf.gather_nd(t4,
                   indices=[[2], [3], [0]]))
```
tf.Tensor(
[[2 7]
 [3 8]
 [0 5]], shape=(3, 2), dtype=int32)

![Image 6](https://www.tensorflow.org/static/guide/images/tf_slicing/gather_2.png)

```
t5 = np.reshape(np.arange(18), [2, 3, 3])

print(tf.gather_nd(t5,
                   indices=[[0, 0, 0], [1, 2, 1]]))
```
tf.Tensor([ 0 16], shape=(2,), dtype=int64)

```
# Return a list of two matrices

print(tf.gather_nd(t5,
                   indices=[[[0, 0], [0, 2]], [[1, 0], [1, 2]]]))
```
tf.Tensor(
[[[ 0  1  2]
  [ 6  7  8]]

 [[ 9 10 11]
  [15 16 17]]], shape=(2, 2, 3), dtype=int64)

```
# Return one matrix

print(tf.gather_nd(t5,
                   indices=[[0, 0], [0, 2], [1, 0], [1, 2]]))
```
tf.Tensor(
[[ 0  1  2]
 [ 6  7  8]
 [ 9 10 11]
 [15 16 17]], shape=(4, 3), dtype=int64)

Insert data into tensors
------------------------

Use [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd) to insert data at specific slices/indices of a tensor. Note that the tensor into which you insert values is zero-initialized.

```
t6 = tf.constant([10])
indices = tf.constant([[1], [3], [5], [7], [9]])
data = tf.constant([2, 4, 6, 8, 10])

print(tf.scatter_nd(indices=indices,
                    updates=data,
                    shape=t6))
```
tf.Tensor([ 0  2  0  4  0  6  0  8  0 10], shape=(10,), dtype=int32)

Methods like [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd) which require zero-initialized tensors are similar to sparse tensor initializers. You can use [`tf.gather_nd`](https://www.tensorflow.org/api_docs/python/tf/gather_nd) and [`tf.scatter_nd`](https://www.tensorflow.org/api_docs/python/tf/scatter_nd) to mimic the behavior of sparse tensor ops.

Consider an example where you construct a sparse tensor using these two methods in conjunction.

```
# Gather values from one tensor by specifying indices

new_indices = tf.constant([[0, 2], [2, 1], [3, 3]])
t7 = tf.gather_nd(t2, indices=new_indices)
```

![Image 7](https://www.tensorflow.org/static/guide/images/tf_slicing/gather_nd_sparse.png)

```
# Add these values into a new tensor

t8 = tf.scatter_nd(indices=new_indices, updates=t7, shape=tf.constant([4, 5]))

print(t8)
```
tf.Tensor(
[[ 0  0  2  0  0]
 [ 0  0  0  0  0]
 [ 0 11  0  0  0]
 [ 0  0  0 18  0]], shape=(4, 5), dtype=int32)

This is similar to:

```
t9 = tf.SparseTensor(indices=[[0, 2], [2, 1], [3, 3]],
                     values=[2, 11, 18],
                     dense_shape=[4, 5])

print(t9)
```
SparseTensor(indices=tf.Tensor(
[[0 2]
 [2 1]
 [3 3]], shape=(3, 2), dtype=int64), values=tf.Tensor([ 2 11 18], shape=(3,), dtype=int32), dense_shape=tf.Tensor([4 5], shape=(2,), dtype=int64))

```
# Convert the sparse tensor into a dense tensor

t10 = tf.sparse.to_dense(t9)

print(t10)
```
tf.Tensor(
[[ 0  0  2  0  0]
 [ 0  0  0  0  0]
 [ 0 11  0  0  0]
 [ 0  0  0 18  0]], shape=(4, 5), dtype=int32)

To insert data into a tensor with pre-existing values, use [`tf.tensor_scatter_nd_add`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_add).

```
t11 = tf.constant([[2, 7, 0],
                   [9, 0, 1],
                   [0, 3, 8]])

# Convert the tensor into a magic square by inserting numbers at appropriate indices

t12 = tf.tensor_scatter_nd_add(t11,
                               indices=[[0, 2], [1, 1], [2, 0]],
                               updates=[6, 5, 4])

print(t12)
```
tf.Tensor(
[[2 7 6]
 [9 5 1]
 [4 3 8]], shape=(3, 3), dtype=int32)

Similarly, use [`tf.tensor_scatter_nd_sub`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_sub) to subtract values from a tensor with pre-existing values.

```
# Convert the tensor into an identity matrix

t13 = tf.tensor_scatter_nd_sub(t11,
                               indices=[[0, 0], [0, 1], [1, 0], [1, 1], [1, 2], [2, 1], [2, 2]],
                               updates=[1, 7, 9, -1, 1, 3, 7])

print(t13)
```
tf.Tensor(
[[1 0 0]
 [0 1 0]
 [0 0 1]], shape=(3, 3), dtype=int32)

Use [`tf.tensor_scatter_nd_min`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_min) to copy element-wise minimum values from one tensor to another.

```
t14 = tf.constant([[-2, -7, 0],
                   [-9, 0, 1],
                   [0, -3, -8]])

t15 = tf.tensor_scatter_nd_min(t14,
                               indices=[[0, 2], [1, 1], [2, 0]],
                               updates=[-6, -5, -4])

print(t15)
```
tf.Tensor(
[[-2 -7 -6]
 [-9 -5  1]
 [-4 -3 -8]], shape=(3, 3), dtype=int32)

Similarly, use [`tf.tensor_scatter_nd_max`](https://www.tensorflow.org/api_docs/python/tf/tensor_scatter_nd_max) to copy element-wise maximum values from one tensor to another.

```
t16 = tf.tensor_scatter_nd_max(t14,
                               indices=[[0, 2], [1, 1], [2, 0]],
                               updates=[6, 5, 4])

print(t16)
```
tf.Tensor(
[[-2 -7  6]
 [-9  5  1]
 [ 4 -3 -8]], shape=(3, 3), dtype=int32)

Further reading and resources
-----------------------------

In this guide, you learned how to use the tensor slicing ops available with TensorFlow to exert finer control over the elements in your tensors.

*   Check out the slicing ops available with TensorFlow NumPy such as [`tf.experimental.numpy.take_along_axis`](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/take_along_axis) and [`tf.experimental.numpy.take`](https://www.tensorflow.org/api_docs/python/tf/experimental/numpy/take).

*   Also check out the [Tensor guide](https://www.tensorflow.org/guide/tensor) and the [Variable guide](https://www.tensorflow.org/guide/variable).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-15 UTC.
