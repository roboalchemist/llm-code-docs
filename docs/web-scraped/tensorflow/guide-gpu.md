# Source: https://www.tensorflow.org/guide/gpu

Title: Use a GPU

URL Source: https://www.tensorflow.org/guide/gpu

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/gpu#main-content)

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
*   TensorFlow in depth

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
*   [Profile Tensor Flow performance](https://www.tensorflow.org/guide/profiler)
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

Use a GPU Stay organized with collections  Save and categorize content based on your preferences.
-------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/gpu#setup)
*   [Overview](https://www.tensorflow.org/guide/gpu#overview)
*   [Logging device placement](https://www.tensorflow.org/guide/gpu#logging_device_placement)
*   [Manual device placement](https://www.tensorflow.org/guide/gpu#manual_device_placement)
*   [Limiting GPU memory growth](https://www.tensorflow.org/guide/gpu#limiting_gpu_memory_growth)
*   [Using a single GPU on a multi-GPU system](https://www.tensorflow.org/guide/gpu#using_a_single_gpu_on_a_multi-gpu_system)
*   [Using multiple GPUs](https://www.tensorflow.org/guide/gpu#using_multiple_gpus)

TensorFlow code, and [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) models will transparently run on a single GPU with no code changes required.

The simplest way to run on multiple GPUs, on one or many machines, is using [Distribution Strategies](https://www.tensorflow.org/guide/distributed_training).

This guide is for users who have tried these approaches and found that they need fine-grained control of how TensorFlow uses the GPU. To learn how to debug performance issues for single and multi-GPU scenarios, see the [Optimize TensorFlow GPU Performance](https://www.tensorflow.org/guide/gpu_performance_analysis) guide.

Setup
-----

Ensure you have the latest TensorFlow gpu release installed.

```
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```
2024-08-15 02:53:40.344028: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-15 02:53:40.365851: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-15 02:53:40.372242: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
Num GPUs Available:  4
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1723690422.944962  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.948934  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.952655  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.955880  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.967120  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.970596  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.973980  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.976984  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.979869  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.983344  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.986754  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690422.989690  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355

Overview
--------

TensorFlow supports running computations on a variety of types of devices, including CPU and GPU. They are represented with string identifiers for example:

*   `"/device:CPU:0"`: The CPU of your machine.
*   `"/GPU:0"`: Short-hand notation for the first GPU of your machine that is visible to TensorFlow.
*   `"/job:localhost/replica:0/task:0/device:GPU:1"`: Fully qualified name of the second GPU of your machine that is visible to TensorFlow.

If a TensorFlow operation has both CPU and GPU implementations, by default, the GPU device is prioritized when the operation is assigned. For example, [`tf.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul) has both CPU and GPU kernels and on a system with devices `CPU:0` and `GPU:0`, the `GPU:0` device is selected to run `tf.matmul` unless you explicitly request to run it on another device.

If a TensorFlow operation has no corresponding GPU implementation, then the operation falls back to the CPU device. For example, since [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast) only has a CPU kernel, on a system with devices `CPU:0` and `GPU:0`, the `CPU:0` device is selected to run `tf.cast`, even if requested to run on the `GPU:0` device.

Logging device placement
------------------------

To find out which devices your operations and tensors are assigned to, put [`tf.debugging.set_log_device_placement(True)`](https://www.tensorflow.org/api_docs/python/tf/debugging/set_log_device_placement) as the first statement of your program. Enabling device placement logging causes any Tensor allocations or operations to be printed.

```
tf.debugging.set_log_device_placement(True)

# Create some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)
```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
I0000 00:00:1723690424.215487  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.217630  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.219585  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.221664  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.223723  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.225666  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.227528  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.229544  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.231494  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.233433  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.235295  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.237325  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.276919  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.278939  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.280845  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.282884  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.284977  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.286923  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.288779  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.290783  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.292741  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.295170  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.297460  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723690424.299854  162671 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

The above code will print an indication the `MatMul` op was executed on `GPU:0`.

Manual device placement
-----------------------

If you would like a particular operation to run on a device of your choice instead of what's automatically selected for you, you can use `with tf.device` to create a device context, and all the operations within that context will run on the same designated device.

```
tf.debugging.set_log_device_placement(True)

# Place tensors on the CPU
with tf.device('/CPU:0'):
  a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
  b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Run on the GPU
c = tf.matmul(a, b)
print(c)
```
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

You will see that now `a` and `b` are assigned to `CPU:0`. Since a device was not explicitly specified for the `MatMul` operation, the TensorFlow runtime will choose one based on the operation and available devices (`GPU:0` in this example) and automatically copy tensors between devices if required.

Limiting GPU memory growth
--------------------------

By default, TensorFlow maps nearly all of the GPU memory of all GPUs (subject to [`CUDA_VISIBLE_DEVICES`](https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars)) visible to the process. This is done to more efficiently use the relatively precious GPU memory resources on the devices by reducing memory fragmentation. To limit TensorFlow to a specific set of GPUs, use the [`tf.config.set_visible_devices`](https://www.tensorflow.org/api_docs/python/tf/config/set_visible_devices) method.

```
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only use the first GPU
  try:
    tf.config.set_visible_devices(gpus[0], 'GPU')
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPU")
  except RuntimeError as e:
    # Visible devices must be set before GPUs have been initialized
    print(e)
```
Visible devices cannot be modified after being initialized

In some cases it is desirable for the process to only allocate a subset of the available memory, or to only grow the memory usage as is needed by the process. TensorFlow provides two methods to control this.

The first option is to turn on memory growth by calling [`tf.config.experimental.set_memory_growth`](https://www.tensorflow.org/api_docs/python/tf/config/experimental/set_memory_growth), which attempts to allocate only as much GPU memory as needed for the runtime allocations: it starts out allocating very little memory, and as the program gets run and more GPU memory is needed, the GPU memory region is extended for the TensorFlow process. Memory is not released since it can lead to memory fragmentation. To turn on memory growth for a specific GPU, use the following code prior to allocating any tensors or executing any ops.

```
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)
```
Physical devices cannot be modified after being initialized

Another way to enable this option is to set the environmental variable `TF_FORCE_GPU_ALLOW_GROWTH` to `true`. This configuration is platform specific.

The second method is to configure a virtual GPU device with [`tf.config.set_logical_device_configuration`](https://www.tensorflow.org/api_docs/python/tf/config/set_logical_device_configuration) and set a hard limit on the total memory to allocate on the GPU.

```
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  # Restrict TensorFlow to only allocate 1GB of memory on the first GPU
  try:
    tf.config.set_logical_device_configuration(
        gpus[0],
        [tf.config.LogicalDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)
```
Virtual devices cannot be modified after being initialized

This is useful if you want to truly bound the amount of GPU memory available to the TensorFlow process. This is common practice for local development when the GPU is shared with other applications such as a workstation GUI.

Using a single GPU on a multi-GPU system
----------------------------------------

If you have more than one GPU in your system, the GPU with the lowest ID will be selected by default. If you would like to run on a different GPU, you will need to specify the preference explicitly:

```
tf.debugging.set_log_device_placement(True)

try:
  # Specify an invalid GPU device
  with tf.device('/device:GPU:2'):
    a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    c = tf.matmul(a, b)
except RuntimeError as e:
  print(e)
```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:2

If the device you have specified does not exist, you will get a `RuntimeError`: `.../device:GPU:2 unknown device`.

If you would like TensorFlow to automatically choose an existing and supported device to run the operations in case the specified one doesn't exist, you can call [`tf.config.set_soft_device_placement(True)`](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement).

```
tf.config.set_soft_device_placement(True)
tf.debugging.set_log_device_placement(True)

# Creates some tensors
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
c = tf.matmul(a, b)

print(c)
```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

Using multiple GPUs
-------------------

Developing for multiple GPUs will allow a model to scale with the additional resources. If developing on a system with a single GPU, you can simulate multiple GPUs with virtual devices. This enables easy testing of multi-GPU setups without requiring additional resources.

```
gpus = tf.config.list_physical_devices('GPU')
if gpus:
  # Create 2 virtual GPUs with 1GB memory each
  try:
    tf.config.set_logical_device_configuration(
        gpus[0],
        [tf.config.LogicalDeviceConfiguration(memory_limit=1024),
         tf.config.LogicalDeviceConfiguration(memory_limit=1024)])
    logical_gpus = tf.config.list_logical_devices('GPU')
    print(len(gpus), "Physical GPU,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Virtual devices must be set before GPUs have been initialized
    print(e)
```
Virtual devices cannot be modified after being initialized

Once there are multiple logical GPUs available to the runtime, you can utilize the multiple GPUs with [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) or with manual placement.

#### With [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)

The best practice for using multiple GPUs is to use [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy). Here is a simple example:

```
tf.debugging.set_log_device_placement(True)
gpus = tf.config.list_logical_devices('GPU')
strategy = tf.distribute.MirroredStrategy(gpus)
with strategy.scope():
  inputs = tf.keras.layers.Input(shape=(1,))
  predictions = tf.keras.layers.Dense(1)(inputs)
  model = tf.keras.models.Model(inputs=inputs, outputs=predictions)
  model.compile(loss='mse',
                optimizer=tf.keras.optimizers.SGD(learning_rate=0.2))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:GPU:0', '/job:localhost/replica:0/task:0/device:GPU:1', '/job:localhost/replica:0/task:0/device:GPU:2', '/job:localhost/replica:0/task:0/device:GPU:3')
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op FloorMod in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Cast in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op StatelessRandomGetKeyCounter in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
a: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
b: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
MatMul: (MatMul): /job:localhost/replica:0/task:0/device:GPU:0
product_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
a: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
b: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
MatMul: (MatMul): /job:localhost/replica:0/task:0/device:GPU:2
product_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
FloorMod: (FloorMod): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Cast: (Cast): /job:localhost/replica:0/task:0/device:GPU:0
y_RetVal: (_DeviceRetval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
_EagerConst: (_EagerConst): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
seed: (_Arg): /job:localhost/replica:0/task:0/device:CPU:0
StatelessRandomGetKeyCounter: (StatelessRandomGetKeyCounter): /job:localhost/replica:0/task:0/device:GPU:0
key_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
counter_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
shape: (_DeviceArg): /job:localhost/replica:0/task:0/device:CPU:0
key: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
counter: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
alg: (_DeviceArg): /job:localhost/replica:0/taExecuting op StatelessRandomUniformV2 in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Sub in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Mul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AddV2 in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
sk:0/device:CPU:0
StatelessRandomUniformV2: (StatelessRandomUniformV2): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Sub: (Sub): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Mul: (Mul): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
x: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
y: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AddV2: (AddV2): /job:localhost/replica:0/task:0/device:GPU:0
z_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
NoOp: (NoOp): /job:localhost/replica:0/task:0/device:GPU:0
dims: (_DeviceArg): /job:localhost/replica:0/task:0/device:CPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
Fill: (Fill): /job:localhost/replica:0/task:0/device:GPU:0
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:lExecuting op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
ocalhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:1
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:1
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:1
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:2
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:2
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:2
input: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
Identity: (Identity): /job:localhost/replica:0/task:0/device:GPU:3
output_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
value: (_Arg): /job:localhost/replica:0/task:0/device:GPU:3
AssignVariableOp: (AssignVariableOp): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:0
resource: (_Arg): /job:localhost/replica:0/task:0/device:GPU:0
ReadVariableOp: (ReadVariableOp): /job:localhost/replica:0/task:0/device:GPU:0
value_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:1
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:1
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:2
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:2
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:3
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/device:GPU:3
resource_RetVal: (_Retval): /job:localhost/replica:0/task:0/device:GPU:0
VarHandleOp: (VarHandleOp): /job:localhost/replica:0/task:0/deviExecuting op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Fill in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op ReadVariableOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op Identity in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op VarHandleOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AssignVariableOp in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op NoOp in device /job:localhost/replica:0/task:0/device:GPU:0

This program will run a copy of your model on each GPU, splitting the input data between them, also known as "[data parallelism](https://en.wikipedia.org/wiki/Data_parallelism)".

For more information about distribution strategies, check out the guide [here](https://www.tensorflow.org/guide/distributed_training).

#### Manual placement

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) works under the hood by replicating computation across devices. You can manually implement replication by constructing your model on each GPU. For example:

```
tf.debugging.set_log_device_placement(True)

gpus = tf.config.list_logical_devices('GPU')
if gpus:
  # Replicate your computation on multiple GPUs
  c = []
  for gpu in gpus:
    with tf.device(gpu.name):
      a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
      b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
      c.append(tf.matmul(a, b))

  with tf.device('/CPU:0'):
    matmul_sum = tf.add_n(c)

  print(matmul_sum)
```
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:0
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:1
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:2
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op _EagerConst in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op MatMul in device /job:localhost/replica:0/task:0/device:GPU:3
Executing op AddN in device /job:localhost/replica:0/task:0/device:CPU:0
tf.Tensor(
[[ 88. 112.]
 [196. 256.]], shape=(2, 2), dtype=float32)

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-15 UTC.
