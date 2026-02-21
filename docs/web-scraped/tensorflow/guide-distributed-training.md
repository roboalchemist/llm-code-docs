# Source: https://www.tensorflow.org/guide/distributed_training

Title: Distributed training with TensorFlow

URL Source: https://www.tensorflow.org/guide/distributed_training

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/distributed_training#main-content)

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

Distributed training with Tensor Flow Stay organized with collections  Save and categorize content based on your preferences.
-----------------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Overview](https://www.tensorflow.org/guide/distributed_training#overview)
*   [Set up TensorFlow](https://www.tensorflow.org/guide/distributed_training#set_up_tensorflow)
*   [Types of strategies](https://www.tensorflow.org/guide/distributed_training#types_of_strategies)
    *   [MirroredStrategy](https://www.tensorflow.org/guide/distributed_training#mirroredstrategy)
    *   [TPUStrategy](https://www.tensorflow.org/guide/distributed_training#tpustrategy)
    *   [MultiWorkerMirroredStrategy](https://www.tensorflow.org/guide/distributed_training#multiworkermirroredstrategy)
    *   [ParameterServerStrategy](https://www.tensorflow.org/guide/distributed_training#parameterserverstrategy)
    *   [CentralStorageStrategy](https://www.tensorflow.org/guide/distributed_training#centralstoragestrategy)
    *   [Other strategies](https://www.tensorflow.org/guide/distributed_training#other_strategies)

*   [Use tf.distribute.Strategy with Keras Model.fit](https://www.tensorflow.org/guide/distributed_training#use_tfdistributestrategy_with_keras_modelfit)
    *   [What's supported now?](https://www.tensorflow.org/guide/distributed_training#whats_supported_now)
    *   [Examples and tutorials](https://www.tensorflow.org/guide/distributed_training#examples_and_tutorials)

*   [Use tf.distribute.Strategy with custom training loops](https://www.tensorflow.org/guide/distributed_training#use_tfdistributestrategy_with_custom_training_loops)
    *   [What's supported now?](https://www.tensorflow.org/guide/distributed_training#whats_supported_now_2)
    *   [Examples and tutorials](https://www.tensorflow.org/guide/distributed_training#examples_and_tutorials_2)

*   [Other topics](https://www.tensorflow.org/guide/distributed_training#other_topics)
    *   [Setting up the TF_CONFIG environment variable](https://www.tensorflow.org/guide/distributed_training#setting_up_the_tf_config_environment_variable)

*   [What's next?](https://www.tensorflow.org/guide/distributed_training#whats_next)

Overview
--------

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) is a TensorFlow API to distribute training across multiple GPUs, multiple machines, or TPUs. Using this API, you can distribute your existing models and training code with minimal code changes.

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) has been designed with these key goals in mind:

*   Easy to use and support multiple user segments, including researchers, machine learning engineers, etc.
*   Provide good performance out of the box.
*   Easy switching between strategies.

You can distribute training using [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) with a high-level API like Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit), as well as [custom training loops](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch) (and, in general, any computation using TensorFlow).

In TensorFlow 2.x, you can execute your programs eagerly, or in a graph using [`tf.function`](https://www.tensorflow.org/guide/function). [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) intends to support both these modes of execution, but works best with [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). Eager mode is only recommended for debugging purposes and not supported for [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy). Although training is the focus of this guide, this API can also be used for distributing evaluation and prediction on different platforms.

You can use [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) with very few changes to your code, because the underlying components of TensorFlow have been changed to become strategy-aware. This includes variables, layers, models, optimizers, metrics, summaries, and checkpoints.

In this guide, you will learn about various types of strategies and how you can use them in different situations. To learn how to debug performance issues, check out the [Optimize TensorFlow GPU performance](https://www.tensorflow.org/guide/gpu_performance_analysis) guide.

Set up Tensor Flow
------------------

```
import tensorflow as tf
```
2024-10-25 03:10:09.809713: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1729825809.832772  192915 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1729825809.839425  192915 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

Types of strategies
-------------------

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) intends to cover a number of use cases along different axes. Some of these combinations are currently supported and others will be added in the future. Some of these axes are:

*   _Synchronous vs asynchronous training:_ These are two common ways of distributing training with data parallelism. In sync training, all workers train over different slices of input data in sync, and aggregating gradients at each step. In async training, all workers are independently training over the input data and updating variables asynchronously. Typically sync training is supported via all-reduce and async through parameter server architecture.
*   _Hardware platform:_ You may want to scale your training onto multiple GPUs on one machine, or multiple machines in a network (with 0 or more GPUs each), or on Cloud TPUs.

In order to support these use cases, TensorFlow has `MirroredStrategy`, `TPUStrategy`, `MultiWorkerMirroredStrategy`, `ParameterServerStrategy`, `CentralStorageStrategy`, as well as other strategies available. The next section explains which of these are supported in which scenarios in TensorFlow. Here is a quick overview:

| Training API | `MirroredStrategy` | `TPUStrategy` | `MultiWorkerMirroredStrategy` | `CentralStorageStrategy` | `ParameterServerStrategy` |
| --- | --- | --- | --- | --- | --- |
| **Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit)** | Supported | Supported | Supported | Experimental support | Experimental support |
| **Custom training loop** | Supported | Supported | Supported | Experimental support | Experimental support |
| **Estimator API** | Limited Support | Not supported | Limited Support | Limited Support | Limited Support |

### MirroredStrategy

[`tf.distribute.MirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy) supports synchronous distributed training on multiple GPUs on one machine. It creates one replica per GPU device. Each variable in the model is mirrored across all the replicas. Together, these variables form a single conceptual variable called `MirroredVariable`. These variables are kept in sync with each other by applying identical updates.

Efficient all-reduce algorithms are used to communicate the variable updates across the devices. All-reduce aggregates tensors across all the devices by adding them up, and makes them available on each device. It’s a fused algorithm that is very efficient and can reduce the overhead of synchronization significantly. There are many all-reduce algorithms and implementations available, depending on the type of communication available between devices. By default, it uses the NVIDIA Collective Communication Library ([NCCL](https://developer.nvidia.com/nccl)) as the all-reduce implementation. You can choose from a few other options or write your own.

Here is the simplest way of creating `MirroredStrategy`:

```
mirrored_strategy = tf.distribute.MirroredStrategy()
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',)
W0000 00:00:1729825812.490898  192915 gpu_device.cc:2344] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...

This will create a `MirroredStrategy` instance, which will use all the GPUs that are visible to TensorFlow, and NCCL—as the cross-device communication.

If you wish to use only some of the GPUs on your machine, you can do so like this:

```
mirrored_strategy = tf.distribute.MirroredStrategy(devices=["/gpu:0", "/gpu:1"])
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:GPU:0', '/job:localhost/replica:0/task:0/device:GPU:1')

If you wish to override the cross device communication, you can do so using the `cross_device_ops` argument by supplying an instance of [`tf.distribute.CrossDeviceOps`](https://www.tensorflow.org/api_docs/python/tf/distribute/CrossDeviceOps). Currently, [`tf.distribute.HierarchicalCopyAllReduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/HierarchicalCopyAllReduce) and [`tf.distribute.ReductionToOneDevice`](https://www.tensorflow.org/api_docs/python/tf/distribute/ReductionToOneDevice) are two options other than [`tf.distribute.NcclAllReduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/NcclAllReduce), which is the default.

```
mirrored_strategy = tf.distribute.MirroredStrategy(
    cross_device_ops=tf.distribute.HierarchicalCopyAllReduce())
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',)

### TPUStrategy

[`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) lets you run your TensorFlow training on [Tensor Processing Units (TPUs)](https://www.tensorflow.org/guide/tpu). TPUs are Google's specialized ASICs designed to dramatically accelerate machine learning workloads. They are available on [Google Colab](https://colab.research.google.com/), the [TPU Research Cloud](https://sites.research.google/trc/), and [Cloud TPU](https://cloud.google.com/tpu).

In terms of distributed training architecture, `TPUStrategy` is the same `MirroredStrategy`—it implements synchronous distributed training. TPUs provide their own implementation of efficient all-reduce and other collective operations across multiple TPU cores, which are used in `TPUStrategy`.

Here is how you would instantiate `TPUStrategy`:

```
cluster_resolver = tf.distribute.cluster_resolver.TPUClusterResolver(
    tpu=tpu_address)
tf.config.experimental_connect_to_cluster(cluster_resolver)
tf.tpu.experimental.initialize_tpu_system(cluster_resolver)
tpu_strategy = tf.distribute.TPUStrategy(cluster_resolver)
```

The `TPUClusterResolver` instance helps locate the TPUs. In Colab, you don't need to specify any arguments to it.

If you want to use this for Cloud TPUs:

*   You must specify the name of your TPU resource in the `tpu` argument.
*   You must initialize the TPU system explicitly at the _start_ of the program. This is required before TPUs can be used for computation. Initializing the TPU system also wipes out the TPU memory, so it's important to complete this step first in order to avoid losing state.

### MultiWorkerMirroredStrategy

[`tf.distribute.MultiWorkerMirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy) is very similar to `MirroredStrategy`. It implements synchronous distributed training across multiple workers, each with potentially multiple GPUs. Similar to [`tf.distribute.MirroredStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy), it creates copies of all variables in the model on each device across all workers.

Here is the simplest way of creating `MultiWorkerMirroredStrategy`:

```
strategy = tf.distribute.MultiWorkerMirroredStrategy()
```
WARNING:tensorflow:Collective ops is not configured at program startup. Some performance features may not be enabled.
INFO:tensorflow:Using MirroredStrategy with devices ('/device:CPU:0',)
INFO:tensorflow:Single-worker MultiWorkerMirroredStrategy with local_devices = ('/device:CPU:0',), communication = CommunicationImplementation.AUTO

`MultiWorkerMirroredStrategy` has two implementations for cross-device communications. [`CommunicationImplementation.RING`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#RING) is [RPC](https://en.wikipedia.org/wiki/Remote_procedure_call)-based and supports both CPUs and GPUs. [`CommunicationImplementation.NCCL`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#NCCL) uses NCCL and provides state-of-art performance on GPUs but it doesn't support CPUs. [`CollectiveCommunication.AUTO`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CommunicationImplementation#AUTO) defers the choice to Tensorflow. You can specify them in the following way:

```
communication_options = tf.distribute.experimental.CommunicationOptions(
    implementation=tf.distribute.experimental.CommunicationImplementation.NCCL)
strategy = tf.distribute.MultiWorkerMirroredStrategy(
    communication_options=communication_options)
```
WARNING:tensorflow:Collective ops is not configured at program startup. Some performance features may not be enabled.
INFO:tensorflow:Using MirroredStrategy with devices ('/device:CPU:0',)
WARNING:tensorflow:Enabled NCCL communication but no GPUs detected/specified.
INFO:tensorflow:Single-worker MultiWorkerMirroredStrategy with local_devices = ('/device:CPU:0',), communication = CommunicationImplementation.NCCL

One of the key differences to get multi worker training going, as compared to multi-GPU training, is the multi-worker setup. The `'TF_CONFIG'` environment variable is the standard way in TensorFlow to specify the cluster configuration to each worker that is part of the cluster. Learn more in the [setting up TF_CONFIG section](https://www.tensorflow.org/guide/distributed_training#TF_CONFIG) of this document.

For more details about `MultiWorkerMirroredStrategy`, consider the following tutorials:

*   [Multi-worker training with Keras Model.fit](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras)
*   [Multi-worker training with a custom training loop](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl)

### ParameterServerStrategy

Parameter server training is a common data-parallel method to scale up model training on multiple machines. A parameter server training cluster consists of workers and parameter servers. Variables are created on parameter servers and they are read and updated by workers in each step. Check out the [Parameter server training](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) tutorial for details.

In TensorFlow 2, parameter server training uses a central coordinator-based architecture via the [`tf.distribute.experimental.coordinator.ClusterCoordinator`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/coordinator/ClusterCoordinator) class.

In this implementation, the `worker` and `parameter server` tasks run [`tf.distribute.Server`](https://www.tensorflow.org/api_docs/python/tf/distribute/Server)s that listen for tasks from the coordinator. The coordinator creates resources, dispatches training tasks, writes checkpoints, and deals with task failures.

In the programming running on the coordinator, you will use a `ParameterServerStrategy` object to define a training step and use a `ClusterCoordinator` to dispatch training steps to remote workers. Here is the simplest way to create them:

```
strategy = tf.distribute.experimental.ParameterServerStrategy(
    tf.distribute.cluster_resolver.TFConfigClusterResolver(),
    variable_partitioner=variable_partitioner)
coordinator = tf.distribute.experimental.coordinator.ClusterCoordinator(
    strategy)
```

To learn more about `ParameterServerStrategy`, check out the [Parameter server training with Keras Model.fit and a custom training loop](https://www.tensorflow.org/tutorials/distribute/parameter_server_training) tutorial.

In TensorFlow 1, `ParameterServerStrategy` is available only with an Estimator via [`tf.compat.v1.distribute.experimental.ParameterServerStrategy`](https://www.tensorflow.org/api_docs/python/tf/compat/v1/distribute/experimental/ParameterServerStrategy) symbol.

### CentralStorageStrategy

[`tf.distribute.experimental.CentralStorageStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/experimental/CentralStorageStrategy) does synchronous training as well. Variables are not mirrored, instead they are placed on the CPU and operations are replicated across all local GPUs. If there is only one GPU, all variables and operations will be placed on that GPU.

Create an instance of `CentralStorageStrategy` by:

```
central_storage_strategy = tf.distribute.experimental.CentralStorageStrategy()
```
INFO:tensorflow:ParameterServerStrategy (CentralStorageStrategy if you are using a single machine) with compute_devices = ['/job:localhost/replica:0/task:0/device:CPU:0'], variable_device = '/job:localhost/replica:0/task:0/device:CPU:0'

This will create a `CentralStorageStrategy` instance which will use all visible GPUs and CPU. Update to variables on replicas will be aggregated before being applied to variables.

### Other strategies

In addition to the above strategies, there are two other strategies which might be useful for prototyping and debugging when using [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute) APIs.

#### Default Strategy

The Default Strategy is a distribution strategy which is present when no explicit distribution strategy is in scope. It implements the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) interface but is a pass-through and provides no actual distribution. For instance, [`Strategy.run(fn)`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run) will simply call `fn`. Code written using this strategy should behave exactly as code written without any strategy. You can think of it as a "no-op" strategy.

The Default Strategy is a singleton—and one cannot create more instances of it. It can be obtained using [`tf.distribute.get_strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy) outside any explicit strategy's scope (the same API that can be used to get the current strategy inside an explicit strategy's scope).

```
default_strategy = tf.distribute.get_strategy()
```

This strategy serves two main purposes:

*   It allows writing distribution-aware library code unconditionally. For example, in [`tf.keras.optimizers`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers) you can use [`tf.distribute.get_strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/get_strategy) and use that strategy for reducing gradients—it will always return a strategy object on which you can call the [`Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#reduce) API.

```
# In optimizer or other library code
# Get currently active strategy
strategy = tf.distribute.get_strategy()
strategy.reduce("SUM", 1., axis=None)  # reduce some values
```
1.0

*   Similar to library code, it can be used to write end users' programs to work with and without distribution strategy, without requiring conditional logic. Here's a sample code snippet illustrating this:

```
if tf.config.list_physical_devices('GPU'):
  strategy = tf.distribute.MirroredStrategy()
else:  # Use the Default Strategy
  strategy = tf.distribute.get_strategy()

with strategy.scope():
  # Do something interesting
  print(tf.Variable(1.))
```
<tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.0>

#### OneDeviceStrategy

[`tf.distribute.OneDeviceStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy) is a strategy to place all variables and computation on a single specified device.

```
strategy = tf.distribute.OneDeviceStrategy(device="/gpu:0")
```

This strategy is distinct from the Default Strategy in a number of ways. In the Default Strategy, the variable placement logic remains unchanged when compared to running TensorFlow without any distribution strategy. But when using `OneDeviceStrategy`, all variables created in its scope are explicitly placed on the specified device. Moreover, any functions called via [`OneDeviceStrategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/OneDeviceStrategy#run) will also be placed on the specified device.

Input distributed through this strategy will be prefetched to the specified device. In the Default Strategy, there is no input distribution.

Similar to the Default Strategy, this strategy could also be used to test your code before switching to other strategies which actually distribute to multiple devices/machines. This will exercise the distribution strategy machinery somewhat more than the Default Strategy, but not to the full extent of using, for example, `MirroredStrategy` or `TPUStrategy`. If you want code that behaves as if there is no strategy, then use the Default Strategy.

So far you've learned about different strategies and how you can instantiate them. The next few sections show the different ways in which you can use them to distribute your training.

Use tf.distribute.Strategy with Keras Model.fit
-----------------------------------------------

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) is integrated into [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras), which is TensorFlow's implementation of the [Keras API specification](https://keras.io/api/). [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) is a high-level API to build and train models. By integrating into the [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) backend, it's seamless for you to distribute your training written in the Keras training framework [using Model.fit](https://www.tensorflow.org/guide/keras/customizing_what_happens_in_fit).

Here's what you need to change in your code:

1.   Create an instance of the appropriate [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy).
2.   Move the creation of Keras model, optimizer and metrics inside `strategy.scope`. Thus the code in the model's `call()`, `train_step()`, and `test_step()` methods will all be distributed and executed on the accelerator(s).

TensorFlow distribution strategies support all types of Keras models—[Sequential](https://www.tensorflow.org/guide/keras/sequential_model), [Functional](https://www.tensorflow.org/guide/keras/functional), and [subclassed](https://www.tensorflow.org/guide/keras/custom_layers_and_models)

Here is a snippet of code to do this for a very simple Keras model with one `Dense` layer:

```
mirrored_strategy = tf.distribute.MirroredStrategy()

with mirrored_strategy.scope():
  model = tf.keras.Sequential([
      tf.keras.layers.Dense(1, input_shape=(1,),
                            kernel_regularizer=tf.keras.regularizers.L2(1e-4))])
  model.compile(loss='mse', optimizer='sgd')
```
INFO:tensorflow:Using MirroredStrategy with devices ('/job:localhost/replica:0/task:0/device:CPU:0',)
/tmpfs/src/tf_docs_env/lib/python3.9/site-packages/keras/src/layers/core/dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.
  super().__init__(activity_regularizer=activity_regularizer, **kwargs)

This example uses `MirroredStrategy`, so you can run this on a machine with multiple GPUs. `strategy.scope()` indicates to Keras which strategy to use to distribute the training. Creating models/optimizers/metrics inside this scope allows you to create distributed variables instead of regular variables. Once this is set up, you can fit your model like you would normally. `MirroredStrategy` takes care of replicating the model's training on the available GPUs, aggregating gradients, and more.

```
dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(100).batch(10)
model.fit(dataset, epochs=2)
model.evaluate(dataset)
```
2024-10-25 03:10:12.686928: W tensorflow/core/framework/dataset.cc:993] Input of GeneratorDatasetOp::Dataset will not be optimized because the dataset does not implement the AsGraphDefInternal() method needed to apply optimizations.
Epoch 1/2
 1/10 ━━━━━━━━━━━━━━━━━━━━ 2s 287ms/step - loss: 0.649210/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.5412
Epoch 2/2
 1/10 ━━━━━━━━━━━━━━━━━━━━ 0s 61ms/step - loss: 0.286910/10 ━━━━━━━━━━━━━━━━━━━━ 0s 1ms/step - loss: 0.2392
 1/10 ━━━━━━━━━━━━━━━━━━━━ 1s 168ms/step - loss: 0.126810/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.1268
0.1268472820520401

Here a [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) provides the training and eval input. You can also use NumPy arrays:

```
import numpy as np

inputs, targets = np.ones((100, 1)), np.ones((100, 1))
model.fit(inputs, targets, epochs=2, batch_size=10)
```
Epoch 1/2
 2/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.124410/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.1058
Epoch 2/2
 3/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.0539 10/10 ━━━━━━━━━━━━━━━━━━━━ 0s 2ms/step - loss: 0.0468
<keras.src.callbacks.history.History at 0x7fab904bcfa0>

In both cases—with `Dataset` or NumPy—each batch of the given input is divided equally among the multiple replicas. For instance, if you are using the `MirroredStrategy` with 2 GPUs, each batch of size 10 will be divided among the 2 GPUs, with each receiving 5 input examples in each step. Each epoch will then train faster as you add more GPUs. Typically, you would want to increase your batch size as you add more accelerators, so as to make effective use of the extra computing power. You will also need to re-tune your learning rate, depending on the model. You can use `strategy.num_replicas_in_sync` to get the number of replicas.

```
mirrored_strategy.num_replicas_in_sync
```
1

```
# Compute a global batch size using a number of replicas.
BATCH_SIZE_PER_REPLICA = 5
global_batch_size = (BATCH_SIZE_PER_REPLICA *
                     mirrored_strategy.num_replicas_in_sync)
dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(100)
dataset = dataset.batch(global_batch_size)

LEARNING_RATES_BY_BATCH_SIZE = {5: 0.1, 10: 0.15, 20:0.175}
learning_rate = LEARNING_RATES_BY_BATCH_SIZE[global_batch_size]
```

### What's supported now?

| Training API | `MirroredStrategy` | `TPUStrategy` | `MultiWorkerMirroredStrategy` | `ParameterServerStrategy` | `CentralStorageStrategy` |
| --- | --- | --- | --- | --- | --- |
| Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) | Supported | Supported | Supported | Experimental support | Experimental support |

### Examples and tutorials

Here is a list of tutorials and examples that illustrate the above integration end-to-end with Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit):

1.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/keras): Training with [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and `MirroredStrategy`.
2.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras): Training with [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and `MultiWorkerMirroredStrategy`.
3.   [Guide](https://www.tensorflow.org/guide/tpu): Contains an example of using [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and `TPUStrategy`.
4.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/parameter_server_training): Parameter server training with [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and `ParameterServerStrategy`.
5.   [Tutorial](https://www.tensorflow.org/text/tutorials/bert_glue): Fine-tuning BERT for many tasks from the GLUE benchmark with [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and `TPUStrategy`.
6.   TensorFlow Model Garden [repository](https://github.com/tensorflow/models/tree/master/official) containing collections of state-of-the-art models implemented using various strategies.

Use tf.distribute.Strategy with custom training loops
-----------------------------------------------------

As demonstrated above, using [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) with Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) requires changing only a couple lines of your code. With a little more effort, you can also use [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy)[with custom training loops](https://www.tensorflow.org/guide/keras/writing_a_training_loop_from_scratch).

If you need more flexibility and control over your training loops than is possible with Estimator or Keras, you can write custom training loops. For instance, when using a GAN, you may want to take a different number of generator or discriminator steps each round. Similarly, the high level frameworks are not very suitable for Reinforcement Learning training.

The [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) classes provide a core set of methods to support custom training loops. Using these may require minor restructuring of the code initially, but once that is done, you should be able to switch between GPUs, TPUs, and multiple machines simply by changing the strategy instance.

Below is a brief snippet illustrating this use case for a simple training example using the same Keras model as before.

First, create the model and optimizer inside the strategy's scope. This ensures that any variables created with the model and optimizer are mirrored variables.

```
with mirrored_strategy.scope():
  model = tf.keras.Sequential([
      tf.keras.layers.Dense(1, input_shape=(1,),
                            kernel_regularizer=tf.keras.regularizers.L2(1e-4))])
  optimizer = tf.keras.optimizers.SGD()
```

Next, create the input dataset and call [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset) to distribute the dataset based on the strategy.

```
dataset = tf.data.Dataset.from_tensors(([1.], [1.])).repeat(1000).batch(
    global_batch_size)
dist_dataset = mirrored_strategy.experimental_distribute_dataset(dataset)
```

Then, define one step of the training. Use [`tf.GradientTape`](https://www.tensorflow.org/api_docs/python/tf/GradientTape) to compute gradients and optimizer to apply those gradients to update your model's variables. To distribute this training step, put it in a function `train_step` and pass it to [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run) along with the dataset inputs you got from the `dist_dataset` created before:

```
# Sets `reduction=NONE` to leave it to tf.nn.compute_average_loss() below.
loss_object = tf.keras.losses.BinaryCrossentropy(
  from_logits=True,
  reduction=tf.keras.losses.Reduction.NONE)

def train_step(inputs):
  features, labels = inputs

  with tf.GradientTape() as tape:
    predictions = model(features, training=True)
    per_example_loss = loss_object(labels, predictions)
    loss = tf.nn.compute_average_loss(per_example_loss)
    model_losses = model.losses
    if model_losses:
      loss += tf.nn.scale_regularization_loss(tf.add_n(model_losses))

  gradients = tape.gradient(loss, model.trainable_variables)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))
  return loss

@tf.function
def distributed_train_step(dist_inputs):
  per_replica_losses = mirrored_strategy.run(train_step, args=(dist_inputs,))
  return mirrored_strategy.reduce(tf.distribute.ReduceOp.SUM, per_replica_losses,
                         axis=None)
```

A few other things to note in the code above:

1.   You used [`tf.nn.compute_average_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss) to reduce the per-example prediction losses to a scalar. [`tf.nn.compute_average_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/compute_average_loss) sums the per example loss and divides the sum by the global batch size. This is important because later after the gradients are calculated on each replica, they are aggregated across the replicas by **summing** them.

By default, the global batch size is taken to be `tf.get_strategy().num_replicas_in_sync * tf.shape(per_example_loss)[0]`. It can also be specified explicitly as a keyword argument `global_batch_size=`. Without short batches, the default is equivalent to `tf.nn.compute_average_loss(..., global_batch_size=global_batch_size)` with the `global_batch_size` defined above. (For more on short batches and how to avoid or handle them, see the [Custom Training tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training).)

2.   You used [`tf.nn.scale_regularization_loss`](https://www.tensorflow.org/api_docs/python/tf/nn/scale_regularization_loss) to scale regularization losses registered with the `Model` object, if any, by `1/num_replicas_in_sync` as well. For those regularization losses that are input-dependent, it falls on the modeling code, not the custom training loop, to perform the averaging over the per-replica(!) batch size; that way the modeling code can remain agnostic of replication while the training loop remains agnostic of how regularization losses are computed.

3.   When you call `apply_gradients` within a distribution strategy scope, its behavior is modified. Specifically, before applying gradients on each parallel instance during synchronous training, it performs a sum-over-all-replicas of the gradients.

4.   You also used the [`tf.distribute.Strategy.reduce`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#reduce) API to aggregate the results returned by [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run) for reporting. [`tf.distribute.Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#run) returns results from each local replica in the strategy, and there are multiple ways to consume this result. You can `reduce` them to get an aggregated value. You can also do [`tf.distribute.Strategy.experimental_local_results`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_local_results) to get the list of values contained in the result, one per local replica.

Finally, once you have defined the training step, you can iterate over `dist_dataset` and run the training in a loop:

```
for dist_inputs in dist_dataset:
  print(distributed_train_step(dist_inputs))
```
tf.Tensor(0.9024367, shape=(), dtype=float32)
tf.Tensor(0.8953863, shape=(), dtype=float32)
tf.Tensor(0.8884038, shape=(), dtype=float32)
tf.Tensor(0.88148874, shape=(), dtype=float32)
tf.Tensor(0.87464076, shape=(), dtype=float32)
tf.Tensor(0.86785895, shape=(), dtype=float32)
tf.Tensor(0.86114323, shape=(), dtype=float32)
tf.Tensor(0.8544927, shape=(), dtype=float32)
tf.Tensor(0.84790725, shape=(), dtype=float32)
tf.Tensor(0.841386, shape=(), dtype=float32)
tf.Tensor(0.83492863, shape=(), dtype=float32)
tf.Tensor(0.8285344, shape=(), dtype=float32)
tf.Tensor(0.82220304, shape=(), dtype=float32)
tf.Tensor(0.8159339, shape=(), dtype=float32)
tf.Tensor(0.8097264, shape=(), dtype=float32)
tf.Tensor(0.8035801, shape=(), dtype=float32)
tf.Tensor(0.79749453, shape=(), dtype=float32)
tf.Tensor(0.79146886, shape=(), dtype=float32)
tf.Tensor(0.785503, shape=(), dtype=float32)
tf.Tensor(0.779596, shape=(), dtype=float32)
tf.Tensor(0.77374756, shape=(), dtype=float32)
tf.Tensor(0.7679571, shape=(), dtype=float32)
tf.Tensor(0.7622242, shape=(), dtype=float32)
tf.Tensor(0.7565481, shape=(), dtype=float32)
tf.Tensor(0.75092846, shape=(), dtype=float32)
tf.Tensor(0.7453647, shape=(), dtype=float32)
tf.Tensor(0.73985624, shape=(), dtype=float32)
tf.Tensor(0.7344028, shape=(), dtype=float32)
tf.Tensor(0.7290035, shape=(), dtype=float32)
tf.Tensor(0.723658, shape=(), dtype=float32)
tf.Tensor(0.7183659, shape=(), dtype=float32)
tf.Tensor(0.71312654, shape=(), dtype=float32)
tf.Tensor(0.7079393, shape=(), dtype=float32)
tf.Tensor(0.70280397, shape=(), dtype=float32)
tf.Tensor(0.6977197, shape=(), dtype=float32)
tf.Tensor(0.69268626, shape=(), dtype=float32)
tf.Tensor(0.687703, shape=(), dtype=float32)
tf.Tensor(0.68276954, shape=(), dtype=float32)
tf.Tensor(0.67788523, shape=(), dtype=float32)
tf.Tensor(0.6730496, shape=(), dtype=float32)
tf.Tensor(0.66826224, shape=(), dtype=float32)
tf.Tensor(0.66352266, shape=(), dtype=float32)
tf.Tensor(0.6588302, shape=(), dtype=float32)
tf.Tensor(0.6541846, shape=(), dtype=float32)
tf.Tensor(0.6495853, shape=(), dtype=float32)
tf.Tensor(0.64503175, shape=(), dtype=float32)
tf.Tensor(0.6405235, shape=(), dtype=float32)
tf.Tensor(0.6360602, shape=(), dtype=float32)
tf.Tensor(0.6316412, shape=(), dtype=float32)
tf.Tensor(0.62726617, shape=(), dtype=float32)
tf.Tensor(0.6229345, shape=(), dtype=float32)
tf.Tensor(0.61864597, shape=(), dtype=float32)
tf.Tensor(0.6143999, shape=(), dtype=float32)
tf.Tensor(0.6101959, shape=(), dtype=float32)
tf.Tensor(0.60603356, shape=(), dtype=float32)
tf.Tensor(0.60191244, shape=(), dtype=float32)
tf.Tensor(0.597832, shape=(), dtype=float32)
tf.Tensor(0.5937919, shape=(), dtype=float32)
tf.Tensor(0.5897917, shape=(), dtype=float32)
tf.Tensor(0.585831, shape=(), dtype=float32)
tf.Tensor(0.58190924, shape=(), dtype=float32)
tf.Tensor(0.5780261, shape=(), dtype=float32)
tf.Tensor(0.57418114, shape=(), dtype=float32)
tf.Tensor(0.57037395, shape=(), dtype=float32)
tf.Tensor(0.5666041, shape=(), dtype=float32)
tf.Tensor(0.56287116, shape=(), dtype=float32)
tf.Tensor(0.55917484, shape=(), dtype=float32)
tf.Tensor(0.5555145, shape=(), dtype=float32)
tf.Tensor(0.55189, shape=(), dtype=float32)
tf.Tensor(0.54830086, shape=(), dtype=float32)
tf.Tensor(0.54474664, shape=(), dtype=float32)
tf.Tensor(0.54122704, shape=(), dtype=float32)
tf.Tensor(0.5377416, shape=(), dtype=float32)
tf.Tensor(0.5342899, shape=(), dtype=float32)
tf.Tensor(0.5308717, shape=(), dtype=float32)
tf.Tensor(0.5274865, shape=(), dtype=float32)
tf.Tensor(0.52413404, shape=(), dtype=float32)
tf.Tensor(0.52081394, shape=(), dtype=float32)
tf.Tensor(0.51752573, shape=(), dtype=float32)
tf.Tensor(0.5142692, shape=(), dtype=float32)
tf.Tensor(0.51104385, shape=(), dtype=float32)
tf.Tensor(0.50784945, shape=(), dtype=float32)
tf.Tensor(0.50468564, shape=(), dtype=float32)
tf.Tensor(0.50155205, shape=(), dtype=float32)
tf.Tensor(0.49844825, shape=(), dtype=float32)
tf.Tensor(0.4953741, shape=(), dtype=float32)
tf.Tensor(0.49232918, shape=(), dtype=float32)
tf.Tensor(0.4893132, shape=(), dtype=float32)
tf.Tensor(0.48632562, shape=(), dtype=float32)
tf.Tensor(0.4833664, shape=(), dtype=float32)
tf.Tensor(0.4804351, shape=(), dtype=float32)
tf.Tensor(0.47753143, shape=(), dtype=float32)
tf.Tensor(0.47465506, shape=(), dtype=float32)
tf.Tensor(0.47180572, shape=(), dtype=float32)
tf.Tensor(0.46898302, shape=(), dtype=float32)
tf.Tensor(0.4661867, shape=(), dtype=float32)
tf.Tensor(0.46341658, shape=(), dtype=float32)
tf.Tensor(0.4606722, shape=(), dtype=float32)
tf.Tensor(0.4579534, shape=(), dtype=float32)
tf.Tensor(0.4552598, shape=(), dtype=float32)
tf.Tensor(0.45259115, shape=(), dtype=float32)
tf.Tensor(0.44994718, shape=(), dtype=float32)
tf.Tensor(0.44732755, shape=(), dtype=float32)
tf.Tensor(0.44473216, shape=(), dtype=float32)
tf.Tensor(0.44216052, shape=(), dtype=float32)
tf.Tensor(0.4396125, shape=(), dtype=float32)
tf.Tensor(0.43708783, shape=(), dtype=float32)
tf.Tensor(0.4345862, shape=(), dtype=float32)
tf.Tensor(0.4321074, shape=(), dtype=float32)
tf.Tensor(0.42965108, shape=(), dtype=float32)
tf.Tensor(0.4272171, shape=(), dtype=float32)
tf.Tensor(0.42480516, shape=(), dtype=float32)
tf.Tensor(0.42241505, shape=(), dtype=float32)
tf.Tensor(0.42004645, shape=(), dtype=float32)
tf.Tensor(0.41769922, shape=(), dtype=float32)
tf.Tensor(0.41537297, shape=(), dtype=float32)
tf.Tensor(0.41306767, shape=(), dtype=float32)
tf.Tensor(0.41078293, shape=(), dtype=float32)
tf.Tensor(0.4085186, shape=(), dtype=float32)
tf.Tensor(0.4062744, shape=(), dtype=float32)
tf.Tensor(0.4040502, shape=(), dtype=float32)
tf.Tensor(0.40184572, shape=(), dtype=float32)
tf.Tensor(0.39966068, shape=(), dtype=float32)
tf.Tensor(0.3974949, shape=(), dtype=float32)
tf.Tensor(0.39534825, shape=(), dtype=float32)
tf.Tensor(0.39322042, shape=(), dtype=float32)
tf.Tensor(0.39111122, shape=(), dtype=float32)
tf.Tensor(0.3890205, shape=(), dtype=float32)
tf.Tensor(0.38694802, shape=(), dtype=float32)
tf.Tensor(0.38489357, shape=(), dtype=float32)
tf.Tensor(0.38285697, shape=(), dtype=float32)
tf.Tensor(0.38083804, shape=(), dtype=float32)
tf.Tensor(0.3788365, shape=(), dtype=float32)
tf.Tensor(0.37685227, shape=(), dtype=float32)
tf.Tensor(0.3748851, shape=(), dtype=float32)
tf.Tensor(0.37293482, shape=(), dtype=float32)
tf.Tensor(0.37100127, shape=(), dtype=float32)
tf.Tensor(0.36908418, shape=(), dtype=float32)
tf.Tensor(0.36718345, shape=(), dtype=float32)
tf.Tensor(0.3652989, shape=(), dtype=float32)
tf.Tensor(0.36343032, shape=(), dtype=float32)
tf.Tensor(0.36157757, shape=(), dtype=float32)
tf.Tensor(0.35974047, shape=(), dtype=float32)
tf.Tensor(0.3579188, shape=(), dtype=float32)
tf.Tensor(0.35611248, shape=(), dtype=float32)
tf.Tensor(0.3543213, shape=(), dtype=float32)
tf.Tensor(0.35254508, shape=(), dtype=float32)
tf.Tensor(0.3507837, shape=(), dtype=float32)
tf.Tensor(0.34903696, shape=(), dtype=float32)
tf.Tensor(0.34730473, shape=(), dtype=float32)
tf.Tensor(0.3455869, shape=(), dtype=float32)
tf.Tensor(0.3438832, shape=(), dtype=float32)
tf.Tensor(0.34219357, shape=(), dtype=float32)
tf.Tensor(0.3405178, shape=(), dtype=float32)
tf.Tensor(0.3388558, shape=(), dtype=float32)
tf.Tensor(0.3372074, shape=(), dtype=float32)
tf.Tensor(0.33557245, shape=(), dtype=float32)
tf.Tensor(0.33395082, shape=(), dtype=float32)
tf.Tensor(0.33234236, shape=(), dtype=float32)
tf.Tensor(0.33074695, shape=(), dtype=float32)
tf.Tensor(0.32916442, shape=(), dtype=float32)
tf.Tensor(0.3275946, shape=(), dtype=float32)
tf.Tensor(0.3260375, shape=(), dtype=float32)
tf.Tensor(0.3244928, shape=(), dtype=float32)
tf.Tensor(0.3229605, shape=(), dtype=float32)
tf.Tensor(0.32144046, shape=(), dtype=float32)
tf.Tensor(0.31993246, shape=(), dtype=float32)
tf.Tensor(0.3184365, shape=(), dtype=float32)
tf.Tensor(0.31695238, shape=(), dtype=float32)
tf.Tensor(0.31548, shape=(), dtype=float32)
tf.Tensor(0.31401917, shape=(), dtype=float32)
tf.Tensor(0.3125699, shape=(), dtype=float32)
tf.Tensor(0.31113195, shape=(), dtype=float32)
tf.Tensor(0.30970532, shape=(), dtype=float32)
tf.Tensor(0.3082898, shape=(), dtype=float32)
tf.Tensor(0.30688527, shape=(), dtype=float32)
tf.Tensor(0.3054917, shape=(), dtype=float32)
tf.Tensor(0.30410892, shape=(), dtype=float32)
tf.Tensor(0.3027368, shape=(), dtype=float32)
tf.Tensor(0.30137527, shape=(), dtype=float32)
tf.Tensor(0.3000242, shape=(), dtype=float32)
tf.Tensor(0.29868355, shape=(), dtype=float32)
tf.Tensor(0.29735315, shape=(), dtype=float32)
tf.Tensor(0.29603288, shape=(), dtype=float32)
tf.Tensor(0.29472268, shape=(), dtype=float32)
tf.Tensor(0.2934224, shape=(), dtype=float32)
tf.Tensor(0.29213202, shape=(), dtype=float32)
tf.Tensor(0.29085135, shape=(), dtype=float32)
tf.Tensor(0.28958035, shape=(), dtype=float32)
tf.Tensor(0.2883189, shape=(), dtype=float32)
tf.Tensor(0.28706694, shape=(), dtype=float32)
tf.Tensor(0.28582436, shape=(), dtype=float32)
tf.Tensor(0.28459102, shape=(), dtype=float32)
tf.Tensor(0.28336692, shape=(), dtype=float32)
tf.Tensor(0.2821518, shape=(), dtype=float32)
tf.Tensor(0.28094578, shape=(), dtype=float32)
tf.Tensor(0.27974862, shape=(), dtype=float32)
tf.Tensor(0.2785603, shape=(), dtype=float32)
tf.Tensor(0.27738073, shape=(), dtype=float32)
tf.Tensor(0.2762098, shape=(), dtype=float32)

In the example above, you iterated over the `dist_dataset` to provide input to your training. You are also provided with the `tf.distribute.Strategy.make_experimental_numpy_dataset` to support NumPy inputs. You can use this API to create a dataset before calling [`tf.distribute.Strategy.experimental_distribute_dataset`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy#experimental_distribute_dataset).

Another way of iterating over your data is to explicitly use iterators. You may want to do this when you want to run for a given number of steps as opposed to iterating over the entire dataset. The above iteration would now be modified to first create an iterator and then explicitly call `next` on it to get the input data.

```
iterator = iter(dist_dataset)
for _ in range(10):
  print(distributed_train_step(next(iterator)))
```
tf.Tensor(0.27504745, shape=(), dtype=float32)
tf.Tensor(0.2738936, shape=(), dtype=float32)
tf.Tensor(0.2727481, shape=(), dtype=float32)
tf.Tensor(0.27161098, shape=(), dtype=float32)
tf.Tensor(0.27048206, shape=(), dtype=float32)
tf.Tensor(0.26936132, shape=(), dtype=float32)
tf.Tensor(0.26824862, shape=(), dtype=float32)
tf.Tensor(0.26714393, shape=(), dtype=float32)
tf.Tensor(0.26604718, shape=(), dtype=float32)
tf.Tensor(0.26495826, shape=(), dtype=float32)

This covers the simplest case of using [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) API to distribute custom training loops.

### What's supported now?

| Training API | `MirroredStrategy` | `TPUStrategy` | `MultiWorkerMirroredStrategy` | `ParameterServerStrategy` | `CentralStorageStrategy` |
| --- | --- | --- | --- | --- | --- |
| Custom training loop | Supported | Supported | Supported | Experimental support | Experimental support |

### Examples and tutorials

Here are some examples for using distribution strategies with custom training loops:

1.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/custom_training): Training with a custom training loop and `MirroredStrategy`.
2.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/multi_worker_with_ctl): Training with a custom training loop and `MultiWorkerMirroredStrategy`.
3.   [Guide](https://www.tensorflow.org/guide/tpu): Contains an example of a custom training loop with `TPUStrategy`.
4.   [Tutorial](https://www.tensorflow.org/tutorials/distribute/parameter_server_training): Parameter server training with a custom training loop and `ParameterServerStrategy`.
5.   TensorFlow Model Garden [repository](https://github.com/tensorflow/models/tree/master/official) containing collections of state-of-the-art models implemented using various strategies.

Other topics
------------

This section covers some topics that are relevant to multiple use cases.

### Setting up the TF_CONFIG environment variable

For multi-worker training, as mentioned before, you need to set up the `'TF_CONFIG'` environment variable for each binary running in your cluster. The `'TF_CONFIG'` environment variable is a JSON string which specifies what tasks constitute a cluster, their addresses and each task's role in the cluster. The [`tensorflow/ecosystem`](https://github.com/tensorflow/ecosystem) repo provides a Kubernetes template, which sets up `'TF_CONFIG'` for your training tasks.

There are two components of `'TF_CONFIG'`: a cluster and a task.

*   A cluster provides information about the training cluster, which is a dict consisting of different types of jobs such as workers. In multi-worker training, there is usually one worker that takes on a little more responsibility like saving checkpoint and writing summary file for TensorBoard in addition to what a regular worker does. Such worker is referred to as the "chief" worker, and it is customary that the worker with index `0` is appointed as the chief worker (in fact this is how [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) is implemented).
*   A task on the other hand provides information about the current task. The first component cluster is the same for all workers, and the second component task is different on each worker and specifies the type and index of that worker.

One example of `'TF_CONFIG'` is:

```
os.environ["TF_CONFIG"] = json.dumps({
    "cluster": {
        "worker": ["host1:port", "host2:port", "host3:port"],
        "ps": ["host4:port", "host5:port"]
    },
   "task": {"type": "worker", "index": 1}
})
```

This `'TF_CONFIG'` specifies that there are three workers and two `"ps"` tasks in the `"cluster"` along with their hosts and ports. The `"task"` part specifies the role of the current task in the `"cluster"`—worker `1` (the second worker). Valid roles in a cluster are `"chief"`, `"worker"`, `"ps"`, and `"evaluator"`. There should be no `"ps"` job except when using `tf.distribute.experimental.ParameterServerStrategy`.

What's next?
------------

[`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) is actively under development. Try it out and provide your feedback using [GitHub issues](https://github.com/tensorflow/tensorflow/issues/new).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-25 UTC.
