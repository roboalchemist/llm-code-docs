# Source: https://www.tensorflow.org/guide/random_numbers

Title: Random number generation

URL Source: https://www.tensorflow.org/guide/random_numbers

Published Time: Thu, 15 Aug 2024 03:17:08 GMT

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/random_numbers#main-content)

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

Random number generation Stay organized with collections  Save and categorize content based on your preferences.
----------------------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/random_numbers#setup)
*   [The tf.random.Generator class](https://www.tensorflow.org/guide/random_numbers#the_tfrandomgenerator_class)
    *   [Creating independent random-number streams](https://www.tensorflow.org/guide/random_numbers#creating_independent_random-number_streams)
    *   [Interaction with tf.function](https://www.tensorflow.org/guide/random_numbers#interaction_with_tffunction)
    *   [Interaction with distribution strategies](https://www.tensorflow.org/guide/random_numbers#interaction_with_distribution_strategies)
    *   [Saving generators](https://www.tensorflow.org/guide/random_numbers#saving_generators)

*   [Stateless RNGs](https://www.tensorflow.org/guide/random_numbers#stateless_rngs)
*   [Algorithms](https://www.tensorflow.org/guide/random_numbers#algorithms)
    *   [General](https://www.tensorflow.org/guide/random_numbers#general)
    *   [XLA devices](https://www.tensorflow.org/guide/random_numbers#xla_devices)

TensorFlow provides a set of pseudo-random number generators (RNG), in the [`tf.random`](https://www.tensorflow.org/api_docs/python/tf/random) module. This document describes how you can control the random number generators, and how these generators interact with other tensorflow sub-systems.

TensorFlow provides two approaches for controlling the random number generation process:

1.   Through the explicit use of [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) objects. Each such object maintains a state (in [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable)) that will be changed after each number generation.

2.   Through the purely-functional stateless random functions like [`tf.random.stateless_uniform`](https://www.tensorflow.org/api_docs/python/tf/random/stateless_uniform). Calling these functions with the same arguments (which include the seed) and on the same device will always produce the same results.

Setup
-----

```
import tensorflow as tf

# Creates some virtual devices (cpu:0, cpu:1, etc.) for using distribution strategy
physical_devices = tf.config.list_physical_devices("CPU")
tf.config.experimental.set_virtual_device_configuration(
    physical_devices[0], [
        tf.config.experimental.VirtualDeviceConfiguration(),
        tf.config.experimental.VirtualDeviceConfiguration(),
        tf.config.experimental.VirtualDeviceConfiguration()
    ])
```
2024-08-15 01:43:41.157432: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-08-15 01:43:41.178819: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-08-15 01:43:41.185039: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1723686223.758551   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.762466   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.765643   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.769228   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.780976   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.784469   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.787369   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.790779   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.794250   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.797851   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.800627   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686223.804177   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355

The [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) class
-------------------------------------------------------------------------------------------------

The [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) class is used in cases where you want each RNG call to produce different results. It maintains an internal state (managed by a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable) object) which will be updated every time random numbers are generated. Because the state is managed by [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable), it enjoys all facilities provided by [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable) such as easy checkpointing, automatic control-dependency and thread safety.

You can get a [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) by manually creating an object of the class or call [`tf.random.get_global_generator()`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator) to get the default global generator:

```
g1 = tf.random.Generator.from_seed(1)
print(g1.normal(shape=[2, 3]))
g2 = tf.random.get_global_generator()
print(g2.normal(shape=[2, 3]))
```
I0000 00:00:1723686225.040869   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.043016   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.045041   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.047115   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.049184   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.051188   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.053162   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.055160   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.057105   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.059113   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.061029   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
tf.Tensor(
[[ 0.43842277 -0.53439844 -0.07710262]
 [ 1.5658045  -0.1012345  -0.2744976 ]], shape=(2, 3), dtype=float32)
tf.Tensor(
[[ 1.3061213   0.6299361   0.52625704]
 [ 1.3733886   0.29277426 -0.7945693 ]], shape=(2, 3), dtype=float32)
I0000 00:00:1723686225.063243   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.101904   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.103956   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.105919   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.107957   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.109922   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.111909   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.113815   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.115823   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.117783   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.120279   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.122678   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1723686225.125117   55391 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355

There are multiple ways to create a generator object. The easiest is [`Generator.from_seed`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#from_seed), as shown above, that creates a generator from a seed. A seed is any non-negative integer. `from_seed` also takes an optional argument `alg` which is the RNG algorithm that will be used by this generator:

```
g1 = tf.random.Generator.from_seed(1, alg='philox')
print(g1.normal(shape=[2, 3]))
```
tf.Tensor(
[[ 0.43842277 -0.53439844 -0.07710262]
 [ 1.5658045  -0.1012345  -0.2744976 ]], shape=(2, 3), dtype=float32)

See the _Algorithms_ section below for more information about it.

Another way to create a generator is with [`Generator.from_non_deterministic_state`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#from_non_deterministic_state). A generator created this way will start from a non-deterministic state, depending on e.g., time and OS.

```
g = tf.random.Generator.from_non_deterministic_state()
print(g.normal(shape=[2, 3]))
```
tf.Tensor(
[[ 0.9104948  -0.23143363 -0.09841432]
 [-0.91448975  0.1579936   1.3923475 ]], shape=(2, 3), dtype=float32)

There are yet other ways to create generators, such as from explicit states, which are not covered by this guide.

When using [`tf.random.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator) to get the global generator, you need to be careful about device placement. The global generator is created (from a non-deterministic state) at the first time [`tf.random.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator) is called, and placed on the default device at that call. So, for example, if the first site you call [`tf.random.get_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/get_global_generator) is within a `tf.device("gpu")` scope, the global generator will be placed on the GPU, and using the global generator later on from the CPU will incur a GPU-to-CPU copy.

There is also a function [`tf.random.set_global_generator`](https://www.tensorflow.org/api_docs/python/tf/random/set_global_generator) for replacing the global generator with another generator object. This function should be used with caution though, because the old global generator may have been captured by a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) (as a weak reference), and replacing it will cause it to be garbage collected, breaking the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). A better way to reset the global generator is to use one of the "reset" functions such as [`Generator.reset_from_seed`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#reset_from_seed), which won't create new generator objects.

```
g = tf.random.Generator.from_seed(1)
print(g.normal([]))
print(g.normal([]))
g.reset_from_seed(1)
print(g.normal([]))
```
tf.Tensor(0.43842277, shape=(), dtype=float32)
tf.Tensor(1.6272374, shape=(), dtype=float32)
tf.Tensor(0.43842277, shape=(), dtype=float32)

### Creating independent random-number streams

In many applications one needs multiple independent random-number streams, independent in the sense that they won't overlap and won't have any statistically detectable correlations. This is achieved by using [`Generator.split`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#split) to create multiple generators that are guaranteed to be independent of each other (i.e. generating independent streams).

```
g = tf.random.Generator.from_seed(1)
print(g.normal([]))
new_gs = g.split(3)
for new_g in new_gs:
  print(new_g.normal([]))
print(g.normal([]))
```
tf.Tensor(0.43842277, shape=(), dtype=float32)
tf.Tensor(2.536413, shape=(), dtype=float32)
tf.Tensor(0.33186463, shape=(), dtype=float32)
tf.Tensor(-0.07144657, shape=(), dtype=float32)
tf.Tensor(-0.79253083, shape=(), dtype=float32)

`split` will change the state of the generator on which it is called (`g` in the above example), similar to an RNG method such as `normal`. In addition to being independent of each other, the new generators (`new_gs`) are also guaranteed to be independent of the old one (`g`).

Spawning new generators is also useful when you want to make sure the generator you use is on the same device as other computations, to avoid the overhead of cross-device copy. For example:

```
with tf.device("cpu"):  # change "cpu" to the device you want
  g = tf.random.get_global_generator().split(1)[0]  
  print(g.normal([]))  # use of g won't cause cross-device copy, unlike the global generator
```
tf.Tensor(-0.66787744, shape=(), dtype=float32)

You can do splitting recursively, calling `split` on split generators. There are no limits (barring integer overflow) on the depth of recursions.

### Interaction with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

[`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) obeys the same rules as [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable) when used with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). This includes three aspects.

#### Creating generators outside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

[`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) can use a generator created outside of it.

```
g = tf.random.Generator.from_seed(1)
@tf.function
def foo():
  return g.normal([])
print(foo())
```
tf.Tensor(0.43842277, shape=(), dtype=float32)

The user needs to make sure that the generator object is still alive (not garbage-collected) when the function is called.

#### Creating generators inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

Creation of generators inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) can only happened during the first run of the function.

```
g = None
@tf.function
def foo():
  global g
  if g is None:
    g = tf.random.Generator.from_seed(1)
  return g.normal([])
print(foo())
print(foo())
```
tf.Tensor(0.43842277, shape=(), dtype=float32)
tf.Tensor(1.6272374, shape=(), dtype=float32)

#### Passing generators as arguments to [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

When used as an argument to a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function), different generator objects will cause retracing of the [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function).

```
num_traces = 0
@tf.function
def foo(g):
  global num_traces
  num_traces += 1
  return g.normal([])
foo(tf.random.Generator.from_seed(1))
foo(tf.random.Generator.from_seed(2))
print(num_traces)
```
2

Note that this retracing behavior is consistent with [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable):

```
num_traces = 0
@tf.function
def foo(v):
  global num_traces
  num_traces += 1
  return v.read_value()
foo(tf.Variable(1))
foo(tf.Variable(2))
print(num_traces)
```
1

### Interaction with distribution strategies

There are two ways in which `Generator` interacts with distribution strategies.

#### Creating generators outside distribution strategies

If a generator is created outside strategy scopes, all replicas’ access to the generator will be serialized, and hence the replicas will get different random numbers.

```
g = tf.random.Generator.from_seed(1)
strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():
  def f():
    print(g.normal([]))
  results = strat.run(f)
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
WARNING:tensorflow:Using MirroredStrategy eagerly has significant overhead currently. We will be working on improving this in the future, but for now please wrap `call_for_each_replica` or `experimental_run` or `run` inside a tf.function to get the best performance.
tf.Tensor(0.43842274, shape=(), dtype=float32)
tf.Tensor(1.6272374, shape=(), dtype=float32)

Note that this usage may have performance issues because the generator's device is different from the replicas.

#### Creating generators inside distribution strategies

If a generator is created inside a strategy scope, each replica will get a different and independent stream of random numbers.

```
strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():
  g = tf.random.Generator.from_seed(1)
  print(strat.run(lambda: g.normal([])))
  print(strat.run(lambda: g.normal([])))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
WARNING:tensorflow:Using MirroredStrategy eagerly has significant overhead currently. We will be working on improving this in the future, but for now please wrap `call_for_each_replica` or `experimental_run` or `run` inside a tf.function to get the best performance.
PerReplica:{
  0: tf.Tensor(-0.87930447, shape=(), dtype=float32),
  1: tf.Tensor(0.020661574, shape=(), dtype=float32)
}
WARNING:tensorflow:Using MirroredStrategy eagerly has significant overhead currently. We will be working on improving this in the future, but for now please wrap `call_for_each_replica` or `experimental_run` or `run` inside a tf.function to get the best performance.
PerReplica:{
  0: tf.Tensor(-1.5822568, shape=(), dtype=float32),
  1: tf.Tensor(0.77539235, shape=(), dtype=float32)
}

If the generator is seeded (e.g. created by [`Generator.from_seed`](https://www.tensorflow.org/api_docs/python/tf/random/Generator#from_seed)), the random numbers are determined by the seed, even though different replicas get different and uncorrelated numbers. One can think of a random number generated on a replica as a hash of the replica ID and a "primary" random number that is common to all replicas. Hence, the whole system is still deterministic.

[`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) can also be created inside [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run):

```
strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():
  def f():
    g = tf.random.Generator.from_seed(1)
    a = g.normal([])
    b = g.normal([])
    return tf.stack([a, b])
  print(strat.run(f))
  print(strat.run(f))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
WARNING:tensorflow:Using MirroredStrategy eagerly has significant overhead currently. We will be working on improving this in the future, but for now please wrap `call_for_each_replica` or `experimental_run` or `run` inside a tf.function to get the best performance.
PerReplica:{
  0: tf.Tensor([-0.87930447 -1.5822568 ], shape=(2,), dtype=float32),
  1: tf.Tensor([0.02066157 0.77539235], shape=(2,), dtype=float32)
}
WARNING:tensorflow:Using MirroredStrategy eagerly has significant overhead currently. We will be working on improving this in the future, but for now please wrap `call_for_each_replica` or `experimental_run` or `run` inside a tf.function to get the best performance.
PerReplica:{
  0: tf.Tensor([-0.87930447 -1.5822568 ], shape=(2,), dtype=float32),
  1: tf.Tensor([0.02066157 0.77539235], shape=(2,), dtype=float32)
}

We no longer recommend passing [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) as arguments to [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run), because [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run) generally expects the arguments to be tensors, not generators.

### Saving generators

Generally for saving or serializing you can handle a [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) the same way you would handle a [`tf.Variable`](https://www.tensorflow.org/api_docs/python/tf/Variable) or a [`tf.Module`](https://www.tensorflow.org/api_docs/python/tf/Module) (or its subclasses). In TF there are two mechanisms for serialization: [Checkpoint](https://www.tensorflow.org/guide/checkpoint) and [SavedModel](https://www.tensorflow.org/guide/saved_model).

#### Checkpoint

Generators can be freely saved and restored using [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint). The random-number stream from the restoring point will be the same as that from the saving point.

```
filename = "./checkpoint"
g = tf.random.Generator.from_seed(1)
cp = tf.train.Checkpoint(generator=g)
print(g.normal([]))
```
tf.Tensor(0.43842277, shape=(), dtype=float32)

```
cp.write(filename)
print("RNG stream from saving point:")
print(g.normal([]))
print(g.normal([]))
```
RNG stream from saving point:
tf.Tensor(1.6272374, shape=(), dtype=float32)
tf.Tensor(1.6307176, shape=(), dtype=float32)

```
cp.restore(filename)
print("RNG stream from restoring point:")
print(g.normal([]))
print(g.normal([]))
```
RNG stream from restoring point:
tf.Tensor(1.6272374, shape=(), dtype=float32)
tf.Tensor(1.6307176, shape=(), dtype=float32)

You can also save and restore within a distribution strategy:

```
filename = "./checkpoint"
strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():
  g = tf.random.Generator.from_seed(1)
  cp = tf.train.Checkpoint(my_generator=g)
  print(strat.run(lambda: g.normal([])))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
PerReplica:{
  0: tf.Tensor(-0.87930447, shape=(), dtype=float32),
  1: tf.Tensor(0.020661574, shape=(), dtype=float32)
}

```
with strat.scope():
  cp.write(filename)
  print("RNG stream from saving point:")
  print(strat.run(lambda: g.normal([])))
  print(strat.run(lambda: g.normal([])))
```
RNG stream from saving point:
PerReplica:{
  0: tf.Tensor(-1.5822568, shape=(), dtype=float32),
  1: tf.Tensor(0.77539235, shape=(), dtype=float32)
}
PerReplica:{
  0: tf.Tensor(-0.5039703, shape=(), dtype=float32),
  1: tf.Tensor(0.1251838, shape=(), dtype=float32)
}

```
with strat.scope():
  cp.restore(filename)
  print("RNG stream from restoring point:")
  print(strat.run(lambda: g.normal([])))
  print(strat.run(lambda: g.normal([])))
```
RNG stream from restoring point:
PerReplica:{
  0: tf.Tensor(-1.5822568, shape=(), dtype=float32),
  1: tf.Tensor(0.77539235, shape=(), dtype=float32)
}
PerReplica:{
  0: tf.Tensor(-0.5039703, shape=(), dtype=float32),
  1: tf.Tensor(0.1251838, shape=(), dtype=float32)
}

You should make sure that the replicas don't diverge in their RNG call history (e.g. one replica makes one RNG call while another makes two RNG calls) before saving. Otherwise, their internal RNG states will diverge and [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint) (which only saves the first replica's state) won't properly restore all the replicas.

You can also restore a saved checkpoint to a different distribution strategy with a different number of replicas. Because a [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) object created in a strategy can only be used in the same strategy, to restore to a different strategy, you have to create a new [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) in the target strategy and a new [`tf.train.Checkpoint`](https://www.tensorflow.org/api_docs/python/tf/train/Checkpoint) for it, as shown in this example:

```
filename = "./checkpoint"
strat1 = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat1.scope():
  g1 = tf.random.Generator.from_seed(1)
  cp1 = tf.train.Checkpoint(my_generator=g1)
  print(strat1.run(lambda: g1.normal([])))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
PerReplica:{
  0: tf.Tensor(-0.87930447, shape=(), dtype=float32),
  1: tf.Tensor(0.020661574, shape=(), dtype=float32)
}

```
with strat1.scope():
  cp1.write(filename)
  print("RNG stream from saving point:")
  print(strat1.run(lambda: g1.normal([])))
  print(strat1.run(lambda: g1.normal([])))
```
RNG stream from saving point:
PerReplica:{
  0: tf.Tensor(-1.5822568, shape=(), dtype=float32),
  1: tf.Tensor(0.77539235, shape=(), dtype=float32)
}
PerReplica:{
  0: tf.Tensor(-0.5039703, shape=(), dtype=float32),
  1: tf.Tensor(0.1251838, shape=(), dtype=float32)
}

```
strat2 = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1", "cpu:2"])
with strat2.scope():
  g2 = tf.random.Generator.from_seed(1)
  cp2 = tf.train.Checkpoint(my_generator=g2)
  cp2.restore(filename)
  print("RNG stream from restoring point:")
  print(strat2.run(lambda: g2.normal([])))
  print(strat2.run(lambda: g2.normal([])))
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1', '/job:localhost/replica:0/task:0/device:CPU:2')
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1', '/job:localhost/replica:0/task:0/device:CPU:2')
RNG stream from restoring point:
PerReplica:{
  0: tf.Tensor(-1.5822568, shape=(), dtype=float32),
  1: tf.Tensor(0.77539235, shape=(), dtype=float32),
  2: tf.Tensor(0.6851049, shape=(), dtype=float32)
}
PerReplica:{
  0: tf.Tensor(-0.5039703, shape=(), dtype=float32),
  1: tf.Tensor(0.1251838, shape=(), dtype=float32),
  2: tf.Tensor(-0.58519536, shape=(), dtype=float32)
}

Although `g1` and `cp1` are different objects from `g2` and `cp2`, they are linked via the common checkpoint file `filename` and object name `my_generator`. Overlapping replicas between strategies (e.g. `cpu:0` and `cpu:1` above) will have their RNG streams properly restored like in previous examples. This guarantee doesn't cover the case when a generator is saved in a strategy scope and restored outside of any strategy scope or vice versa, because a device outside strategies is treated as different from any replica in a strategy.

#### SavedModel

[`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) can be saved to a SavedModel. The generator can be created within a strategy scope. The saving can also happen within a strategy scope.

```
filename = "./saved_model"

class MyModule(tf.Module):

  def __init__(self):
    super(MyModule, self).__init__()
    self.g = tf.random.Generator.from_seed(0)

  @tf.function
  def __call__(self):
    return self.g.normal([])

  @tf.function
  def state(self):
    return self.g.state

strat = tf.distribute.MirroredStrategy(devices=["cpu:0", "cpu:1"])
with strat.scope():
  m = MyModule()
  print(strat.run(m))
  print("state:", m.state())
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0', '/job:localhost/replica:0/task:0/device:CPU:1')
PerReplica:{
  0: tf.Tensor(-1.4154755, shape=(), dtype=float32),
  1: tf.Tensor(-0.11388441, shape=(), dtype=float32)
}
state: tf.Tensor([256   0   0], shape=(3,), dtype=int64)

```
with strat.scope():
  tf.saved_model.save(m, filename)
  print("RNG stream from saving point:")
  print(strat.run(m))
  print("state:", m.state())
  print(strat.run(m))
  print("state:", m.state())
```
INFO:tensorflow:Assets written to: ./saved_model/assets
INFO:tensorflow:Assets written to: ./saved_model/assets
RNG stream from saving point:
PerReplica:{
  0: tf.Tensor(-0.68758255, shape=(), dtype=float32),
  1: tf.Tensor(0.8084062, shape=(), dtype=float32)
}
state: tf.Tensor([512   0   0], shape=(3,), dtype=int64)
PerReplica:{
  0: tf.Tensor(-0.27342677, shape=(), dtype=float32),
  1: tf.Tensor(-0.53093255, shape=(), dtype=float32)
}
state: tf.Tensor([768   0   0], shape=(3,), dtype=int64)

```
imported = tf.saved_model.load(filename)
print("RNG stream from loading point:")
print("state:", imported.state())
print(imported())
print("state:", imported.state())
print(imported())
print("state:", imported.state())
```
RNG stream from loading point:
state: tf.Tensor([256   0   0], shape=(3,), dtype=int64)
tf.Tensor(-1.0359411, shape=(), dtype=float32)
state: tf.Tensor([512   0   0], shape=(3,), dtype=int64)
tf.Tensor(-0.06425078, shape=(), dtype=float32)
state: tf.Tensor([768   0   0], shape=(3,), dtype=int64)

Loading a SavedModel containing [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) into a distribution strategy is not recommended because the replicas will all generate the same random-number stream (which is because replica ID is frozen in SavedModel's graph).

Loading a distributed [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) (a generator created within a distribution strategy) into a non-strategy environment, like the above example, also has a caveat. The RNG state will be properly restored, but the random numbers generated will be different from the original generator in its strategy (again because a device outside strategies is treated as different from any replica in a strategy).

Stateless RNGs
--------------

Usage of stateless RNGs is simple. Since they are just pure functions, there is no state or side effect involved.

```
print(tf.random.stateless_normal(shape=[2, 3], seed=[1, 2]))
print(tf.random.stateless_normal(shape=[2, 3], seed=[1, 2]))
```
tf.Tensor(
[[ 0.5441101   0.20738031  0.07356433]
 [ 0.04643455 -1.30159    -0.95385665]], shape=(2, 3), dtype=float32)
tf.Tensor(
[[ 0.5441101   0.20738031  0.07356433]
 [ 0.04643455 -1.30159    -0.95385665]], shape=(2, 3), dtype=float32)

Every stateless RNG requires a `seed` argument, which needs to be an integer Tensor of shape `[2]`. The results of the op are fully determined by this seed.

The RNG algorithm used by stateless RNGs is device-dependent, meaning the same op running on a different device may produce different outputs.

Algorithms
----------

### General

Both the [`tf.random.Generator`](https://www.tensorflow.org/api_docs/python/tf/random/Generator) class and the `stateless` functions support the Philox algorithm (written as `"philox"` or `tf.random.Algorithm.PHILOX`) on all devices.

Different devices will generate the same integer numbers, if using the same algorithm and starting from the same state. They will also generate "almost the same" float-point numbers, though there may be small numerical discrepancies caused by the different ways the devices carry out the float-point computation (e.g. reduction order).

### XLA devices

On XLA-driven devices (such as TPU, and also CPU/GPU when XLA is enabled) the ThreeFry algorithm (written as `"threefry"` or `tf.random.Algorithm.THREEFRY`) is also supported. This algorithm is fast on TPU but slow on CPU/GPU compared to Philox.

See paper ['Parallel Random Numbers: As Easy as 1, 2, 3'](https://www.thesalmons.org/john/random123/papers/random123sc11.pdf) for more details about these algorithms.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-15 UTC.
