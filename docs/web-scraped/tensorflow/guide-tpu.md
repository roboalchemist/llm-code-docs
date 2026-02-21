# Source: https://www.tensorflow.org/guide/tpu

Title: Use TPUs

URL Source: https://www.tensorflow.org/guide/tpu

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/tpu#main-content)

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

Use TPUs Stay organized with collections  Save and categorize content based on your preferences.
------------------------------------------------------------------------------------------------

*   On this page
*   [Setup](https://www.tensorflow.org/guide/tpu#setup)
*   [TPU initialization](https://www.tensorflow.org/guide/tpu#tpu_initialization)
*   [Manual device placement](https://www.tensorflow.org/guide/tpu#manual_device_placement)
*   [Distribution strategies](https://www.tensorflow.org/guide/tpu#distribution_strategies)
*   [Classification on TPUs](https://www.tensorflow.org/guide/tpu#classification_on_tpus)
    *   [Define a Keras model](https://www.tensorflow.org/guide/tpu#define_a_keras_model)
    *   [Load the dataset](https://www.tensorflow.org/guide/tpu#load_the_dataset)
    *   [Train the model using Keras high-level APIs](https://www.tensorflow.org/guide/tpu#train_the_model_using_keras_high-level_apis)
    *   [Train the model using a custom training loop](https://www.tensorflow.org/guide/tpu#train_the_model_using_a_custom_training_loop)
    *   [Improving performance with multiple steps inside tf.function](https://www.tensorflow.org/guide/tpu#improving_performance_with_multiple_steps_inside_tffunction)

*   [Next steps](https://www.tensorflow.org/guide/tpu#next_steps)

This guide demonstrates how to perform basic training on [Tensor Processing Units (TPUs)](https://cloud.google.com/tpu/) and TPU Pods, a collection of TPU devices connected by dedicated high-speed network interfaces, with [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) and custom training loops.

TPUs are Google's custom-developed application-specific integrated circuits (ASICs) used to accelerate machine learning workloads. They are available through [Google Colab](https://colab.research.google.com/), the [TPU Research Cloud](https://sites.research.google/trc/), and [Cloud TPU](https://cloud.google.com/tpu).

Setup
-----

Before you run this Colab notebook, make sure that your hardware accelerator is a TPU by checking your notebook settings: **Runtime**>**Change runtime type**>**Hardware accelerator**>**TPU**.

Import some necessary libraries, including TensorFlow Datasets:

```
import tensorflow as tf

import os
import tensorflow_datasets as tfds
```
2023-06-09 12:13:32.486552: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT

TPU initialization
------------------

TPUs are typically [Cloud TPU](https://cloud.google.com/tpu/docs/) workers, which are different from the local process running the user's Python program. Thus, you need to do some initialization work to connect to the remote cluster and initialize the TPUs. Note that the `tpu` argument to [`tf.distribute.cluster_resolver.TPUClusterResolver`](https://www.tensorflow.org/api_docs/python/tf/distribute/cluster_resolver/TPUClusterResolver) is a special address just for Colab. If you are running your code on Google Compute Engine (GCE), you should instead pass in the name of your Cloud TPU.

```
resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='')
tf.config.experimental_connect_to_cluster(resolver)
# This is the TPU initialization code that has to be at the beginning.
tf.tpu.experimental.initialize_tpu_system(resolver)
print("All devices: ", tf.config.list_logical_devices('TPU'))
```
INFO:tensorflow:Deallocate tpu buffers before initializing tpu system.
2023-06-09 12:13:34.011755: E tensorflow/compiler/xla/stream_executor/cuda/cuda_driver.cc:266] failed call to cuInit: CUDA_ERROR_NO_DEVICE: no CUDA-capable device is detected
INFO:tensorflow:Deallocate tpu buffers before initializing tpu system.
INFO:tensorflow:Initializing the TPU system: grpc://10.25.167.66:8470
INFO:tensorflow:Initializing the TPU system: grpc://10.25.167.66:8470
INFO:tensorflow:Finished initializing TPU system.
INFO:tensorflow:Finished initializing TPU system.
All devices:  [LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:0', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:1', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:2', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:3', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:4', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:5', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:6', device_type='TPU'), LogicalDevice(name='/job:worker/replica:0/task:0/device:TPU:7', device_type='TPU')]

Manual device placement
-----------------------

After the TPU is initialized, you can use manual device placement to place the computation on a single TPU device:

```
a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

with tf.device('/TPU:0'):
  c = tf.matmul(a, b)

print("c device: ", c.device)
print(c)
```
c device:  /job:worker/replica:0/task:0/device:TPU:0
tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)

Distribution strategies
-----------------------

Usually, you run your model on multiple TPUs in a data-parallel way. To distribute your model on multiple TPUs (as well as multiple GPUs or multiple machines), TensorFlow offers the [`tf.distribute.Strategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/Strategy) API. You can replace your distribution strategy and the model will run on any given (TPU) device. Learn more in the [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training) guide.

Using the [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) option implements synchronous distributed training. TPUs provide their own implementation of efficient all-reduce and other collective operations across multiple TPU cores, which are used in `TPUStrategy`.

To demonstrate this, create a [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy) object:

```
strategy = tf.distribute.TPUStrategy(resolver)
```
INFO:tensorflow:Found TPU system:
INFO:tensorflow:Found TPU system:
INFO:tensorflow:*** Num TPU Cores: 8
INFO:tensorflow:*** Num TPU Cores: 8
INFO:tensorflow:*** Num TPU Workers: 1
INFO:tensorflow:*** Num TPU Workers: 1
INFO:tensorflow:*** Num TPU Cores Per Worker: 8
INFO:tensorflow:*** Num TPU Cores Per Worker: 8
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:CPU:0, CPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:localhost/replica:0/task:0/device:CPU:0, CPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:CPU:0, CPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:CPU:0, CPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:0, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:0, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:1, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:1, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:2, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:2, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:3, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:3, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:4, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:4, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:5, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:5, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:6, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:6, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:7, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU:7, TPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU_SYSTEM:0, TPU_SYSTEM, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:TPU_SYSTEM:0, TPU_SYSTEM, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:XLA_CPU:0, XLA_CPU, 0, 0)
INFO:tensorflow:*** Available Device: _DeviceAttributes(/job:worker/replica:0/task:0/device:XLA_CPU:0, XLA_CPU, 0, 0)

To replicate a computation so it can run in all TPU cores, you can pass it into the [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run) API. Below is an example that shows all cores receiving the same inputs `(a, b)` and performing matrix multiplication on each core independently. The outputs will be the values from all the replicas.

```
@tf.function
def matmul_fn(x, y):
  z = tf.matmul(x, y)
  return z

z = strategy.run(matmul_fn, args=(a, b))
print(z)
```
PerReplica:{
  0: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  1: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  2: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  3: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  4: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  5: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  6: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32),
  7: tf.Tensor(
[[22. 28.]
 [49. 64.]], shape=(2, 2), dtype=float32)
}

Classification on TPUs
----------------------

Having covered the basic concepts, consider a more concrete example. This section demonstrates how to use the distribution strategy—[`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)—to train a Keras model on a Cloud TPU.

### Define a Keras model

Start with a definition of a [`Sequential` Keras model](https://www.tensorflow.org/guide/keras/sequential_model) for image classification on the MNIST dataset. It's no different than what you would use if you were training on CPUs or GPUs. Note that Keras model creation needs to be inside the [`Strategy.scope`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#scope), so the variables can be created on each TPU device. Other parts of the code are not necessary to be inside the `Strategy` scope.

```
def create_model():
  return tf.keras.Sequential(
      [tf.keras.layers.Conv2D(256, 3, activation='relu', input_shape=(28, 28, 1)),
       tf.keras.layers.Conv2D(256, 3, activation='relu'),
       tf.keras.layers.Flatten(),
       tf.keras.layers.Dense(256, activation='relu'),
       tf.keras.layers.Dense(128, activation='relu'),
       tf.keras.layers.Dense(10)])
```

### Load the dataset

Efficient use of the [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) API is critical when using a Cloud TPU. You can learn more about dataset performance in the [Input pipeline performance guide](https://www.tensorflow.org/guide/data_performance).

If you are using [TPU Nodes](https://cloud.google.com/tpu/docs/managing-tpus-tpu-vm), you need to store all data files read by the TensorFlow `Dataset` in [Google Cloud Storage (GCS) buckets](https://cloud.google.com/tpu/docs/storage-buckets). If you are using [TPU VMs](https://cloud.google.com/tpu/docs/users-guide-tpu-vm), you can store data wherever you like. For more information on TPU Nodes and TPU VMs, refer to the [TPU System Architecture](https://cloud.google.com/tpu/docs/system-architecture-tpu-vm) documentation.

For most use cases, it is recommended to convert your data into the `TFRecord` format and use a [`tf.data.TFRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset) to read it. Check the [TFRecord and tf.Example tutorial](https://www.tensorflow.org/tutorials/load_data/tfrecord) for details on how to do this. It is not a hard requirement and you can use other dataset readers, such as [`tf.data.FixedLengthRecordDataset`](https://www.tensorflow.org/api_docs/python/tf/data/FixedLengthRecordDataset) or [`tf.data.TextLineDataset`](https://www.tensorflow.org/api_docs/python/tf/data/TextLineDataset).

You can load entire small datasets into memory using [`tf.data.Dataset.cache`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#cache).

Regardless of the data format used, it is strongly recommended that you use large files on the order of 100MB. This is especially important in this networked setting, as the overhead of opening a file is significantly higher.

As shown in the code below, you should use the Tensorflow Datasets [`tfds.load`](https://www.tensorflow.org/datasets/api_docs/python/tfds/load) module to get a copy of the MNIST training and test data. Note that `try_gcs` is specified to use a copy that is available in a public GCS bucket. If you don't specify this, the TPU will not be able to access the downloaded data.

```
def get_dataset(batch_size, is_training=True):
  split = 'train' if is_training else 'test'
  dataset, info = tfds.load(name='mnist', split=split, with_info=True,
                            as_supervised=True, try_gcs=True)

  # Normalize the input data.
  def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.0
    return image, label

  dataset = dataset.map(scale)

  # Only shuffle and repeat the dataset in training. The advantage of having an
  # infinite dataset for training is to avoid the potential last partial batch
  # in each epoch, so that you don't need to think about scaling the gradients
  # based on the actual batch size.
  if is_training:
    dataset = dataset.shuffle(10000)
    dataset = dataset.repeat()

  dataset = dataset.batch(batch_size)

  return dataset
```

### Train the model using Keras high-level APIs

You can train your model with Keras [`Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) and [`Model.compile`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile) APIs. There is nothing TPU-specific in this step—you write the code as if you were using multiple GPUs and a `MirroredStrategy` instead of the `TPUStrategy`. You can learn more in the [Distributed training with Keras](https://www.tensorflow.org/tutorials/distribute/keras) tutorial.

```
with strategy.scope():
  model = create_model()
  model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['sparse_categorical_accuracy'])

batch_size = 200
steps_per_epoch = 60000 // batch_size
validation_steps = 10000 // batch_size

train_dataset = get_dataset(batch_size, is_training=True)
test_dataset = get_dataset(batch_size, is_training=False)

model.fit(train_dataset,
          epochs=5,
          steps_per_epoch=steps_per_epoch,
          validation_data=test_dataset,
          validation_steps=validation_steps)
```
Epoch 1/5
300/300 [==============================] - 17s 32ms/step - loss: 0.1235 - sparse_categorical_accuracy: 0.9620 - val_loss: 0.0462 - val_sparse_categorical_accuracy: 0.9856
Epoch 2/5
300/300 [==============================] - 7s 24ms/step - loss: 0.0333 - sparse_categorical_accuracy: 0.9894 - val_loss: 0.0401 - val_sparse_categorical_accuracy: 0.9878
Epoch 3/5
300/300 [==============================] - 7s 24ms/step - loss: 0.0186 - sparse_categorical_accuracy: 0.9938 - val_loss: 0.0352 - val_sparse_categorical_accuracy: 0.9900
Epoch 4/5
300/300 [==============================] - 7s 25ms/step - loss: 0.0127 - sparse_categorical_accuracy: 0.9957 - val_loss: 0.0482 - val_sparse_categorical_accuracy: 0.9879
Epoch 5/5
300/300 [==============================] - 7s 24ms/step - loss: 0.0111 - sparse_categorical_accuracy: 0.9962 - val_loss: 0.0448 - val_sparse_categorical_accuracy: 0.9894
<keras.callbacks.History at 0x7f79107c8d30>

To reduce Python overhead and maximize the performance of your TPU, pass in the `steps_per_execution` argument to Keras [`Model.compile`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#compile). In this example, it increases throughput by about 50%:

```
with strategy.scope():
  model = create_model()
  model.compile(optimizer='adam',
                # Anything between 2 and `steps_per_epoch` could help here.
                steps_per_execution = 50,
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['sparse_categorical_accuracy'])

model.fit(train_dataset,
          epochs=5,
          steps_per_epoch=steps_per_epoch,
          validation_data=test_dataset,
          validation_steps=validation_steps)
```
Epoch 1/5
300/300 [==============================] - 14s 45ms/step - loss: 0.1306 - sparse_categorical_accuracy: 0.9591 - val_loss: 0.0420 - val_sparse_categorical_accuracy: 0.9863
Epoch 2/5
300/300 [==============================] - 3s 10ms/step - loss: 0.0333 - sparse_categorical_accuracy: 0.9900 - val_loss: 0.0502 - val_sparse_categorical_accuracy: 0.9846
Epoch 3/5
300/300 [==============================] - 3s 10ms/step - loss: 0.0193 - sparse_categorical_accuracy: 0.9936 - val_loss: 0.0406 - val_sparse_categorical_accuracy: 0.9879
Epoch 4/5
300/300 [==============================] - 3s 10ms/step - loss: 0.0135 - sparse_categorical_accuracy: 0.9955 - val_loss: 0.0416 - val_sparse_categorical_accuracy: 0.9882
Epoch 5/5
300/300 [==============================] - 3s 10ms/step - loss: 0.0110 - sparse_categorical_accuracy: 0.9962 - val_loss: 0.0463 - val_sparse_categorical_accuracy: 0.9882
<keras.callbacks.History at 0x7f7898488e20>

### Train the model using a custom training loop

You can also create and train your model using [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) and [`tf.distribute`](https://www.tensorflow.org/api_docs/python/tf/distribute) APIs directly. You can use the `Strategy.experimental_distribute_datasets_from_function` API to distribute the [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset) given a dataset function. Note that in the example below the batch size passed into the `Dataset` is the per-replica batch size instead of the global batch size. To learn more, check out the [Custom training with `tf.distribute.Strategy`](https://www.tensorflow.org/tutorials/distribute/custom_training) tutorial.

First, create the model, datasets and [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)s:

```
# Create the model, optimizer and metrics inside the `tf.distribute.Strategy`
# scope, so that the variables can be mirrored on each device.
with strategy.scope():
  model = create_model()
  optimizer = tf.keras.optimizers.Adam()
  training_loss = tf.keras.metrics.Mean('training_loss', dtype=tf.float32)
  training_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(
      'training_accuracy', dtype=tf.float32)

# Calculate per replica batch size, and distribute the `tf.data.Dataset`s
# on each TPU worker.
per_replica_batch_size = batch_size // strategy.num_replicas_in_sync

train_dataset = strategy.experimental_distribute_datasets_from_function(
    lambda _: get_dataset(per_replica_batch_size, is_training=True))

@tf.function
def train_step(iterator):
  """The step function for one training step."""

  def step_fn(inputs):
    """The computation to run on each TPU device."""
    images, labels = inputs
    with tf.GradientTape() as tape:
      logits = model(images, training=True)
      loss = tf.keras.losses.sparse_categorical_crossentropy(
          labels, logits, from_logits=True)
      loss = tf.nn.compute_average_loss(loss, global_batch_size=batch_size)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(list(zip(grads, model.trainable_variables)))
    training_loss.update_state(loss * strategy.num_replicas_in_sync)
    training_accuracy.update_state(labels, logits)

  strategy.run(step_fn, args=(next(iterator),))
```
WARNING:tensorflow:From /tmpfs/tmp/ipykernel_9094/1509474074.py:14: StrategyBase.experimental_distribute_datasets_from_function (from tensorflow.python.distribute.distribute_lib) is deprecated and will be removed in a future version.
Instructions for updating:
rename to distribute_datasets_from_function
WARNING:tensorflow:From /tmpfs/tmp/ipykernel_9094/1509474074.py:14: StrategyBase.experimental_distribute_datasets_from_function (from tensorflow.python.distribute.distribute_lib) is deprecated and will be removed in a future version.
Instructions for updating:
rename to distribute_datasets_from_function

Then, run the training loop:

```
steps_per_eval = 10000 // batch_size

train_iterator = iter(train_dataset)
for epoch in range(5):
  print('Epoch: {}/5'.format(epoch))

  for step in range(steps_per_epoch):
    train_step(train_iterator)
  print('Current step: {}, training loss: {}, accuracy: {}%'.format(
      optimizer.iterations.numpy(),
      round(float(training_loss.result()), 4),
      round(float(training_accuracy.result()) * 100, 2)))
  training_loss.reset_states()
  training_accuracy.reset_states()
```
Epoch: 0/5
Current step: 300, training loss: 0.1465, accuracy: 95.4%
Epoch: 1/5
Current step: 600, training loss: 0.035, accuracy: 98.94%
Epoch: 2/5
Current step: 900, training loss: 0.0197, accuracy: 99.39%
Epoch: 3/5
Current step: 1200, training loss: 0.0126, accuracy: 99.59%
Epoch: 4/5
Current step: 1500, training loss: 0.0109, accuracy: 99.64%

### Improving performance with multiple steps inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

You can improve the performance by running multiple steps within a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). This is achieved by wrapping the [`Strategy.run`](https://www.tensorflow.org/api_docs/python/tf/distribute/MirroredStrategy#run) call with a [`tf.range`](https://www.tensorflow.org/api_docs/python/tf/range) inside [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function), and AutoGraph will convert it to a [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop) on the TPU worker. You can learn more about [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)s in the [Better performance with `tf.function`](https://www.tensorflow.org/guide/function) guide.

Despite the improved performance, there are tradeoffs with this method compared to running a single step inside a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function). Running multiple steps in a [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) is less flexible—you cannot run things eagerly or arbitrary Python code within the steps.

```
@tf.function
def train_multiple_steps(iterator, steps):
  """The step function for one training step."""

  def step_fn(inputs):
    """The computation to run on each TPU device."""
    images, labels = inputs
    with tf.GradientTape() as tape:
      logits = model(images, training=True)
      loss = tf.keras.losses.sparse_categorical_crossentropy(
          labels, logits, from_logits=True)
      loss = tf.nn.compute_average_loss(loss, global_batch_size=batch_size)
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(list(zip(grads, model.trainable_variables)))
    training_loss.update_state(loss * strategy.num_replicas_in_sync)
    training_accuracy.update_state(labels, logits)

  for _ in tf.range(steps):
    strategy.run(step_fn, args=(next(iterator),))

# Convert `steps_per_epoch` to `tf.Tensor` so the `tf.function` won't get
# retraced if the value changes.
train_multiple_steps(train_iterator, tf.convert_to_tensor(steps_per_epoch))

print('Current step: {}, training loss: {}, accuracy: {}%'.format(
      optimizer.iterations.numpy(),
      round(float(training_loss.result()), 4),
      round(float(training_accuracy.result()) * 100, 2)))
```
Current step: 1800, training loss: 0.009, accuracy: 99.72%

Next steps
----------

To learn more about Cloud TPUs and how to use them:

*   [Google Cloud TPU](https://cloud.google.com/tpu): The Google Cloud TPU homepage.
*   [Google Cloud TPU documentation](https://cloud.google.com/tpu/docs/): Google Cloud TPU documentation, which includes: 
    *   [Introduction to Cloud TPU](https://cloud.google.com/tpu/docs/intro-to-tpu): An overview of working with Cloud TPUs.
    *   [Cloud TPU quickstarts](https://cloud.google.com/tpu/docs/quick-starts): Quickstart introductions to working with Cloud TPU VMs using TensorFlow and other main machine learning frameworks.

*   [Google Cloud TPU Colab notebooks](https://cloud.google.com/tpu/docs/colabs): End-to-end training examples.
*   [Google Cloud TPU performance guide](https://cloud.google.com/tpu/docs/performance-guide): Enhance Cloud TPU performance further by adjusting Cloud TPU configuration parameters for your application
*   [Distributed training with TensorFlow](https://www.tensorflow.org/guide/distributed_training): How to use distribution strategies—including [`tf.distribute.TPUStrategy`](https://www.tensorflow.org/api_docs/python/tf/distribute/TPUStrategy)—with examples showing best practices.
*   TPU embeddings: TensorFlow includes specialized support for training embeddings on TPUs via [`tf.tpu.experimental.embedding`](https://www.tensorflow.org/api_docs/python/tf/tpu/experimental/embedding). In addition, [TensorFlow Recommenders](https://www.tensorflow.org/recommenders) has [`tfrs.layers.embedding.TPUEmbedding`](https://www.tensorflow.org/recommenders/api_docs/python/tfrs/layers/embedding/TPUEmbedding). Embeddings provide efficient and dense representations, capturing complex similarities and relationships between features. TensorFlow's TPU-specific embedding support allows you to train embeddings that are larger than the memory of a single TPU device, and to use sparse and ragged inputs on TPUs.
*   [TPU Research Cloud (TRC)](https://sites.research.google/trc/about/): TRC enables researchers to apply for access to a cluster of more than 1,000 Cloud TPU devices.

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-03-23 UTC.
