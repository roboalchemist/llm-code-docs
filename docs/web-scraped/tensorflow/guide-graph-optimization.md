# Source: https://www.tensorflow.org/guide/graph_optimization

Title: TensorFlow graph optimization with Grappler

URL Source: https://www.tensorflow.org/guide/graph_optimization

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/graph_optimization#main-content)

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

Tensor Flow graph optimization with Grappler Stay organized with collections  Save and categorize content based on your preferences.
------------------------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Overview](https://www.tensorflow.org/guide/graph_optimization#overview)
*   [Available graph optimizers](https://www.tensorflow.org/guide/graph_optimization#available_graph_optimizers)
*   [Setup](https://www.tensorflow.org/guide/graph_optimization#setup)
*   [Compare execution performance with and without Grappler](https://www.tensorflow.org/guide/graph_optimization#compare_execution_performance_with_and_without_grappler)
    *   [Constant folding optimizer](https://www.tensorflow.org/guide/graph_optimization#constant_folding_optimizer)
    *   [Debug stripper optimizer](https://www.tensorflow.org/guide/graph_optimization#debug_stripper_optimizer)

*   [Summary](https://www.tensorflow.org/guide/graph_optimization#summary)

Overview
--------

TensorFlow uses both graph and eager executions to execute computations. A [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph) contains a set of [`tf.Operation`](https://www.tensorflow.org/api_docs/python/tf/Operation) objects (ops) which represent units of computation and [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor) objects which represent the units of data that flow between ops.

Grappler is the default graph optimization system in the TensorFlow runtime. Grappler applies optimizations in graph mode (within [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)) to improve the performance of your TensorFlow computations through graph simplifications and other high-level optimizations such as inlining function bodies to enable inter-procedural optimizations. Optimizing the [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph) also reduces the device peak memory usage and improves hardware utilization by optimizing the mapping of graph nodes to compute resources.

Use [`tf.config.optimizer.set_experimental_options()`](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options) for finer control over your [`tf.Graph`](https://www.tensorflow.org/api_docs/python/tf/Graph) optimizations.

Available graph optimizers
--------------------------

Grappler performs graph optimizations through a top-level driver called the `MetaOptimizer`. The following graph optimizers are available with TensorFlow:

*   _Constant folding optimizer -_ Statically infers the value of tensors when possible by folding constant nodes in the graph and materializes the result using constants.
*   _Arithmetic optimizer -_ Simplifies arithmetic operations by eliminating common subexpressions and simplifying arithmetic statements. 
*   _Layout optimizer -_ Optimizes tensor layouts to execute data format dependent operations such as convolutions more efficiently.
*   _Remapper optimizer -_ Remaps subgraphs onto more efficient implementations by replacing commonly occurring subgraphs with optimized fused monolithic kernels.
*   _Memory optimizer -_ Analyzes the graph to inspect the peak memory usage for each operation and inserts CPU-GPU memory copy operations for swapping GPU memory to CPU to reduce the peak memory usage.
*   _Dependency optimizer -_ Removes or rearranges control dependencies to shorten the critical path for a model step or enables other optimizations. Also removes nodes that are effectively no-ops such as Identity.
*   _Pruning optimizer -_ Prunes nodes that have no effect on the output from the graph. It is usually run first to reduce the size of the graph and speed up processing in other Grappler passes.
*   _Function optimizer -_ Optimizes the function library of a TensorFlow program and inlines function bodies to enable other inter-procedural optimizations.
*   _Shape optimizer -_ Optimizes subgraphs that operate on shape and shape related information.
*   _Autoparallel optimizer -_ Automatically parallelizes graphs by splitting along the batch dimension. This optimizer is turned OFF by default.
*   _Loop optimizer -_ Optimizes the graph control flow by hoisting loop-invariant subgraphs out of loops and by removing redundant stack operations in loops. Also optimizes loops with statically known trip counts and removes statically known dead branches in conditionals.
*   _Scoped allocator optimizer -_ Introduces scoped allocators to reduce data movement and to consolidate some operations.
*   _Pin to host optimizer -_ Swaps small operations onto the CPU. This optimizer is turned OFF by default. 
*   _Auto mixed precision optimizer -_ Converts data types to float16 where applicable to improve performance. Currently applies to GPUs and the latest Intel Xeon CPUs.
*   _Debug stripper -_ Strips nodes related to debugging operations such as [`tf.debugging.Assert`](https://www.tensorflow.org/api_docs/python/tf/debugging/Assert), [`tf.debugging.check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics), and [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print) from the graph. This optimizer is turned OFF by default.

Setup
-----

```
import numpy as np
import timeit
import traceback
import contextlib

import tensorflow as tf
```
2024-10-22 01:21:40.497936: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:485] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
2024-10-22 01:21:40.518495: E external/local_xla/xla/stream_executor/cuda/cuda_dnn.cc:8454] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
2024-10-22 01:21:40.524546: E external/local_xla/xla/stream_executor/cuda/cuda_blas.cc:1452] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

Create a context manager to easily toggle optimizer states.

```
@contextlib.contextmanager
def options(options):
  old_opts = tf.config.optimizer.get_experimental_options()
  tf.config.optimizer.set_experimental_options(options)
  try:
    yield
  finally:
    tf.config.optimizer.set_experimental_options(old_opts)
```

Compare execution performance with and without Grappler
-------------------------------------------------------

TensorFlow 2 and beyond executes eagerly by default. Use [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) to switch the default execution to Graph mode. Grappler runs automatically in the background to apply the graph optimizations above and improve execution performance.

### Constant folding optimizer

As a preliminary example, consider a function which performs operations on constants and returns an output.

```
def test_function_1():
  @tf.function
  def simple_function(input_arg):
    print('Tracing!')
    a = tf.constant(np.random.randn(2000,2000), dtype = tf.float32)
    c = a
    for n in range(50):
      c = c@a
    return tf.reduce_mean(c+input_arg)

  return simple_function
```

Turn off the constant folding optimizer and execute the function:

```
with options({'constant_folding': False}):
  print(tf.config.optimizer.get_experimental_options())
  simple_function = test_function_1()
  # Trace once
  x = tf.constant(2.2)
  simple_function(x)
  print("Vanilla execution:", timeit.timeit(lambda: simple_function(x), number = 1), "s")
```
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1729560103.034816   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.038481   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.042253   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.046045   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.057719   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.061186   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.064513   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.068051   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.071607   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.075025   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.078392   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560103.081893   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.352532   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.354590   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.356672   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.358683   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.360804   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.362737   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.364643   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.366576   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.368663   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.370608   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.372559   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.374467   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.414463   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.416494   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.418461   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.420413   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.422446   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.424357   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.426261   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.428204   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.430256   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.433836   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.436197   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
I0000 00:00:1729560104.438538   10375 cuda_executor.cc:1015] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero. See more at https://github.com/torvalds/linux/blob/v6.0/Documentation/ABI/testing/sysfs-bus-pci#L344-L355
{'constant_folding': False, 'disable_model_pruning': False, 'disable_meta_optimizer': False}
Tracing!
Vanilla execution: 0.002112719000024299 s

Enable the constant folding optimizer and execute the function again to observe a speed-up in function execution.

```
with options({'constant_folding': True}):
  print(tf.config.optimizer.get_experimental_options())
  simple_function = test_function_1()
  # Trace once
  x = tf.constant(2.2)
  simple_function(x)
  print("Constant folded execution:", timeit.timeit(lambda: simple_function(x), number = 1), "s")
```
{'constant_folding': True, 'disable_model_pruning': False, 'disable_meta_optimizer': False}
Tracing!
Constant folded execution: 0.0007726810000576734 s

### Debug stripper optimizer

Consider a simple function that checks the numeric value of its input argument and returns it.

```
def test_function_2():
  @tf.function
  def simple_func(input_arg):
    output = input_arg
    tf.debugging.check_numerics(output, "Bad!")
    return output
  return simple_func
```

First, execute the function with the debug stripper optimizer turned off.

```
test_func = test_function_2()
p1 = tf.constant(float('inf'))
try:
  test_func(p1)
except tf.errors.InvalidArgumentError as e:
  traceback.print_exc(limit=2)
```
2024-10-22 01:22:00.656591: E tensorflow/core/kernels/check_numerics_op.cc:299] abnormal_detected_host @0x7f5f72c00100 = {0, 1} Bad!
Traceback (most recent call last):
  File "/tmpfs/tmp/ipykernel_10375/3616845043.py", line 4, in <module>
    test_func(p1)
  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/tensorflow/python/util/traceback_utils.py", line 153, in error_handler
    raise e.with_traceback(filtered_tb) from None
tensorflow.python.framework.errors_impl.InvalidArgumentError: Graph execution error:

Detected at node CheckNumerics defined at (most recent call last):
  File "/usr/lib/python3.9/runpy.py", line 197, in _run_module_as_main

  File "/usr/lib/python3.9/runpy.py", line 87, in _run_code

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel_launcher.py", line 18, in <module>

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/traitlets/config/application.py", line 1075, in launch_instance

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/kernelapp.py", line 739, in start

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/tornado/platform/asyncio.py", line 205, in start

  File "/usr/lib/python3.9/asyncio/base_events.py", line 601, in run_forever

  File "/usr/lib/python3.9/asyncio/base_events.py", line 1905, in _run_once

  File "/usr/lib/python3.9/asyncio/events.py", line 80, in _run

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/kernelbase.py", line 545, in dispatch_queue

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/kernelbase.py", line 534, in process_one

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/kernelbase.py", line 437, in dispatch_shell

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/ipkernel.py", line 362, in execute_request

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/kernelbase.py", line 778, in execute_request

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/ipkernel.py", line 449, in do_execute

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/ipykernel/zmqshell.py", line 549, in run_cell

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3048, in run_cell

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3103, in _run_cell

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/async_helpers.py", line 129, in _pseudo_sync_runner

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3308, in run_cell_async

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3490, in run_ast_nodes

  File "/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/IPython/core/interactiveshell.py", line 3550, in run_code

  File "/tmpfs/tmp/ipykernel_10375/3616845043.py", line 4, in <module>

  File "/tmpfs/tmp/ipykernel_10375/2241890286.py", line 5, in simple_func

Bad! : Tensor had Inf values
     [[{ {node CheckNumerics} }]] [Op:__inference_simple_func_128]

[`tf.debugging.check_numerics`](https://www.tensorflow.org/api_docs/python/tf/debugging/check_numerics) raises an invalid argument error because of the `Inf` argument to `test_func`.

Enable the debug stripper optimizer and execute the function again.

```
with options({'debug_stripper': True}):
  test_func2 = test_function_2()
  p1 = tf.constant(float('inf'))
  try:
    test_func2(p1)
  except tf.errors.InvalidArgumentError as e:
    traceback.print_exc(limit=2)
```

The debug stripper optimizer strips the `tf.debug.check_numerics` node from the graph and executes the function without raising any errors.

Summary
-------

The TensorFlow runtime uses Grappler to optimize graphs automatically before execution. Use [`tf.config.optimizer.set_experimental_options`](https://www.tensorflow.org/api_docs/python/tf/config/optimizer/set_experimental_options) to enable or disable the various graph optimizers.

For more information on Grappler, see [TensorFlow Graph Optimizations](http://web.stanford.edu/class/cs245/slides/TFGraphOptimizationsStanford.pdf).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-22 UTC.
