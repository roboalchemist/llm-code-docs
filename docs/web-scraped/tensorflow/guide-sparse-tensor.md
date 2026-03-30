# Source: https://www.tensorflow.org/guide/sparse_tensor

Title: Working with sparse tensors

URL Source: https://www.tensorflow.org/guide/sparse_tensor

Markdown Content:
[Skip to main content](https://www.tensorflow.org/guide/sparse_tensor#main-content)

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

Working with sparse tensors Stay organized with collections  Save and categorize content based on your preferences.
-------------------------------------------------------------------------------------------------------------------

*   On this page
*   [Sparse tensors in TensorFlow](https://www.tensorflow.org/guide/sparse_tensor#sparse_tensors_in_tensorflow)
*   [Creating a tf.sparse.SparseTensor](https://www.tensorflow.org/guide/sparse_tensor#creating_a_tfsparsesparsetensor)
*   [Manipulating sparse tensors](https://www.tensorflow.org/guide/sparse_tensor#manipulating_sparse_tensors)
*   [Using tf.sparse.SparseTensor with other TensorFlow APIs](https://www.tensorflow.org/guide/sparse_tensor#using_tfsparsesparsetensor_with_other_tensorflow_apis)
    *   [tf.keras](https://www.tensorflow.org/guide/sparse_tensor#tfkeras)
    *   [tf.data](https://www.tensorflow.org/guide/sparse_tensor#tfdata)
    *   [tf.train.Example](https://www.tensorflow.org/guide/sparse_tensor#tftrainexample)
    *   [tf.function](https://www.tensorflow.org/guide/sparse_tensor#tffunction)

*   [Distinguishing missing values from zero values](https://www.tensorflow.org/guide/sparse_tensor#distinguishing_missing_values_from_zero_values)
*   [Further reading and resources](https://www.tensorflow.org/guide/sparse_tensor#further_reading_and_resources)

When working with tensors that contain a lot of zero values, it is important to store them in a space- and time-efficient manner. Sparse tensors enable efficient storage and processing of tensors that contain a lot of zero values. Sparse tensors are used extensively in encoding schemes like [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) as part of data pre-processing in NLP applications and for pre-processing images with a lot of dark pixels in computer vision applications.

Sparse tensors in Tensor Flow
-----------------------------

TensorFlow represents sparse tensors through the [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) object. Currently, sparse tensors in TensorFlow are encoded using the coordinate list (COO) format. This encoding format is optimized for hyper-sparse matrices such as embeddings.

The COO encoding for sparse tensors is comprised of:

*   `values`: A 1D tensor with shape `[N]` containing all nonzero values.
*   `indices`: A 2D tensor with shape `[N, rank]`, containing the indices of the nonzero values.
*   `dense_shape`: A 1D tensor with shape `[rank]`, specifying the shape of the tensor.

A **_nonzero_** value in the context of a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) is a value that's not explicitly encoded. It is possible to explicitly include zero values in the `values` of a COO sparse matrix, but these "explicit zeros" are generally not included when referring to nonzero values in a sparse tensor.

Creating a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)
--------------------------------------------------------------------------------------------------------

Construct sparse tensors by directly specifying their `values`, `indices`, and `dense_shape`.

```
import tensorflow as tf
```
2024-10-25 01:24:09.202320: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1729819449.223893   16549 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered
E0000 00:00:1729819449.230517   16549 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered

```
st1 = tf.sparse.SparseTensor(indices=[[0, 3], [2, 4]],
                      values=[10, 20],
                      dense_shape=[3, 10])
```
W0000 00:00:1729819451.911465   16549 gpu_device.cc:2344] Cannot dlopen some GPU libraries. Please make sure the missing libraries mentioned above are installed properly if you would like to use GPU. Follow the guide at https://www.tensorflow.org/install/gpu for how to download and setup the required libraries for your platform.
Skipping registering GPU devices...

![Image 1](https://www.tensorflow.org/static/guide/images/sparse_tensor.png)

When you use the `print()` function to print a sparse tensor, it shows the contents of the three component tensors:

```
print(st1)
```
SparseTensor(indices=tf.Tensor(
[[0 3]
 [2 4]], shape=(2, 2), dtype=int64), values=tf.Tensor([10 20], shape=(2,), dtype=int32), dense_shape=tf.Tensor([ 3 10], shape=(2,), dtype=int64))

It is easier to understand the contents of a sparse tensor if the nonzero `values` are aligned with their corresponding `indices`. Define a helper function to pretty-print sparse tensors such that each nonzero value is shown on its own line.

```
def pprint_sparse_tensor(st):
  s = "<SparseTensor shape=%s \n values={" % (st.dense_shape.numpy().tolist(),)
  for (index, value) in zip(st.indices, st.values):
    s += f"\n  %s: %s" % (index.numpy().tolist(), value.numpy().tolist())
  return s + "}>"
```

```
print(pprint_sparse_tensor(st1))
```
<SparseTensor shape=[3, 10] 
 values={
  [0, 3]: 10
  [2, 4]: 20}>

You can also construct sparse tensors from dense tensors by using [`tf.sparse.from_dense`](https://www.tensorflow.org/api_docs/python/tf/sparse/from_dense), and convert them back to dense tensors by using [`tf.sparse.to_dense`](https://www.tensorflow.org/api_docs/python/tf/sparse/to_dense).

```
st2 = tf.sparse.from_dense([[1, 0, 0, 8], [0, 0, 0, 0], [0, 0, 3, 0]])
print(pprint_sparse_tensor(st2))
```
<SparseTensor shape=[3, 4] 
 values={
  [0, 0]: 1
  [0, 3]: 8
  [2, 2]: 3}>

```
st3 = tf.sparse.to_dense(st2)
print(st3)
```
tf.Tensor(
[[1 0 0 8]
 [0 0 0 0]
 [0 0 3 0]], shape=(3, 4), dtype=int32)

Manipulating sparse tensors
---------------------------

Use the utilities in the [`tf.sparse`](https://www.tensorflow.org/api_docs/python/tf/sparse) package to manipulate sparse tensors. Ops like [`tf.math.add`](https://www.tensorflow.org/api_docs/python/tf/math/add) that you can use for arithmetic manipulation of dense tensors do not work with sparse tensors.

Add sparse tensors of the same shape by using [`tf.sparse.add`](https://www.tensorflow.org/api_docs/python/tf/sparse/add).

```
st_a = tf.sparse.SparseTensor(indices=[[0, 2], [3, 4]],
                       values=[31, 2], 
                       dense_shape=[4, 10])

st_b = tf.sparse.SparseTensor(indices=[[0, 2], [3, 0]],
                       values=[56, 38],
                       dense_shape=[4, 10])

st_sum = tf.sparse.add(st_a, st_b)

print(pprint_sparse_tensor(st_sum))
```
<SparseTensor shape=[4, 10] 
 values={
  [0, 2]: 87
  [3, 0]: 38
  [3, 4]: 2}>

Use [`tf.sparse.sparse_dense_matmul`](https://www.tensorflow.org/api_docs/python/tf/sparse/sparse_dense_matmul) to multiply sparse tensors with dense matrices.

```
st_c = tf.sparse.SparseTensor(indices=([0, 1], [1, 0], [1, 1]),
                       values=[13, 15, 17],
                       dense_shape=(2,2))

mb = tf.constant([[4], [6]])
product = tf.sparse.sparse_dense_matmul(st_c, mb)

print(product)
```
tf.Tensor(
[[ 78]
 [162]], shape=(2, 1), dtype=int32)

Put sparse tensors together by using [`tf.sparse.concat`](https://www.tensorflow.org/api_docs/python/tf/sparse/concat) and take them apart by using [`tf.sparse.slice`](https://www.tensorflow.org/api_docs/python/tf/sparse/slice).

```
sparse_pattern_A = tf.sparse.SparseTensor(indices = [[2,4], [3,3], [3,4], [4,3], [4,4], [5,4]],
                         values = [1,1,1,1,1,1],
                         dense_shape = [8,5])
sparse_pattern_B = tf.sparse.SparseTensor(indices = [[0,2], [1,1], [1,3], [2,0], [2,4], [2,5], [3,5], 
                                              [4,5], [5,0], [5,4], [5,5], [6,1], [6,3], [7,2]],
                         values = [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                         dense_shape = [8,6])
sparse_pattern_C = tf.sparse.SparseTensor(indices = [[3,0], [4,0]],
                         values = [1,1],
                         dense_shape = [8,6])

sparse_patterns_list = [sparse_pattern_A, sparse_pattern_B, sparse_pattern_C]
sparse_pattern = tf.sparse.concat(axis=1, sp_inputs=sparse_patterns_list)
print(tf.sparse.to_dense(sparse_pattern))
```
tf.Tensor(
[[0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 0 0]
 [0 0 0 1 1 0 0 0 0 0 1 1 0 0 0 0 0]
 [0 0 0 1 1 0 0 0 0 0 1 1 0 0 0 0 0]
 [0 0 0 0 1 1 0 0 0 1 1 0 0 0 0 0 0]
 [0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0]], shape=(8, 17), dtype=int32)

```
sparse_slice_A = tf.sparse.slice(sparse_pattern_A, start = [0,0], size = [8,5])
sparse_slice_B = tf.sparse.slice(sparse_pattern_B, start = [0,5], size = [8,6])
sparse_slice_C = tf.sparse.slice(sparse_pattern_C, start = [0,10], size = [8,6])
print(tf.sparse.to_dense(sparse_slice_A))
print(tf.sparse.to_dense(sparse_slice_B))
print(tf.sparse.to_dense(sparse_slice_C))
```
tf.Tensor(
[[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 1]
 [0 0 0 1 1]
 [0 0 0 1 1]
 [0 0 0 0 1]
 [0 0 0 0 0]
 [0 0 0 0 0]], shape=(8, 5), dtype=int32)
tf.Tensor(
[[0]
 [0]
 [1]
 [1]
 [1]
 [1]
 [0]
 [0]], shape=(8, 1), dtype=int32)
tf.Tensor([], shape=(8, 0), dtype=int32)

If you're using TensorFlow 2.4 or above, use [`tf.sparse.map_values`](https://www.tensorflow.org/api_docs/python/tf/sparse/map_values) for elementwise operations on nonzero values in sparse tensors.

```
st2_plus_5 = tf.sparse.map_values(tf.add, st2, 5)
print(tf.sparse.to_dense(st2_plus_5))
```
tf.Tensor(
[[ 6  0  0 13]
 [ 0  0  0  0]
 [ 0  0  8  0]], shape=(3, 4), dtype=int32)

Note that only the nonzero values were modified – the zero values stay zero.

Equivalently, you can follow the design pattern below for earlier versions of TensorFlow:

```
st2_plus_5 = tf.sparse.SparseTensor(
    st2.indices,
    st2.values + 5,
    st2.dense_shape)
print(tf.sparse.to_dense(st2_plus_5))
```
tf.Tensor(
[[ 6  0  0 13]
 [ 0  0  0  0]
 [ 0  0  8  0]], shape=(3, 4), dtype=int32)

Using [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) with other TensorFlow APIs
------------------------------------------------------------------------------------------------------------------------------

Sparse tensors work transparently with these TensorFlow APIs:

*   [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)
*   [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)
*   `tf.Train.Example` protobuf
*   [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)
*   [`tf.while_loop`](https://www.tensorflow.org/api_docs/python/tf/while_loop)
*   [`tf.cond`](https://www.tensorflow.org/api_docs/python/tf/cond)
*   [`tf.identity`](https://www.tensorflow.org/api_docs/python/tf/identity)
*   [`tf.cast`](https://www.tensorflow.org/api_docs/python/tf/cast)
*   [`tf.print`](https://www.tensorflow.org/api_docs/python/tf/print)
*   [`tf.saved_model`](https://www.tensorflow.org/api_docs/python/tf/saved_model)
*   [`tf.io.serialize_sparse`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_sparse)
*   [`tf.io.serialize_many_sparse`](https://www.tensorflow.org/api_docs/python/tf/io/serialize_many_sparse)
*   [`tf.io.deserialize_many_sparse`](https://www.tensorflow.org/api_docs/python/tf/io/deserialize_many_sparse)
*   [`tf.math.abs`](https://www.tensorflow.org/api_docs/python/tf/math/abs)
*   [`tf.math.negative`](https://www.tensorflow.org/api_docs/python/tf/math/negative)
*   [`tf.math.sign`](https://www.tensorflow.org/api_docs/python/tf/math/sign)
*   [`tf.math.square`](https://www.tensorflow.org/api_docs/python/tf/math/square)
*   [`tf.math.sqrt`](https://www.tensorflow.org/api_docs/python/tf/math/sqrt)
*   [`tf.math.erf`](https://www.tensorflow.org/api_docs/python/tf/math/erf)
*   [`tf.math.tanh`](https://www.tensorflow.org/api_docs/python/tf/math/tanh)
*   [`tf.math.bessel_i0e`](https://www.tensorflow.org/api_docs/python/tf/math/bessel_i0e)
*   [`tf.math.bessel_i1e`](https://www.tensorflow.org/api_docs/python/tf/math/bessel_i1e)

Examples are shown below for a few of the above APIs.

### [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras)

A subset of the [`tf.keras`](https://www.tensorflow.org/api_docs/python/tf/keras) API supports sparse tensors without expensive casting or conversion ops. The Keras API lets you pass sparse tensors as inputs to a Keras model. Set `sparse=True` when calling [`tf.keras.Input`](https://www.tensorflow.org/api_docs/python/tf/keras/Input) or [`tf.keras.layers.InputLayer`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/InputLayer). You can pass sparse tensors between Keras layers, and also have Keras models return them as outputs. If you use sparse tensors in [`tf.keras.layers.Dense`](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Dense) layers in your model, they will output dense tensors.

The example below shows you how to pass a sparse tensor as an input to a Keras model if you use only layers that support sparse inputs.

```
x = tf.keras.Input(shape=(4,), sparse=True)
y = tf.keras.layers.Dense(4)(x)
model = tf.keras.Model(x, y)

sparse_data = tf.sparse.SparseTensor(
    indices = [(0,0),(0,1),(0,2),
               (4,3),(5,0),(5,1)],
    values = [1,1,1,1,1,1],
    dense_shape = (6,4)
)

model(sparse_data)

model.predict(sparse_data)
```
1/1 ━━━━━━━━━━━━━━━━━━━━ 0s 87ms/step
array([[ 1.8707037e-02,  7.7025330e-01,  2.2425324e-01, -1.9139588e+00],
       [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
       [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
       [ 0.0000000e+00,  0.0000000e+00,  0.0000000e+00,  0.0000000e+00],
       [-6.2435389e-02, -4.5783034e-01,  1.2970567e-03, -1.8046319e-01],
       [-8.0019468e-01,  9.0452707e-01,  2.1884918e-02, -1.3622781e+00]],
      dtype=float32)

### [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data)

The [`tf.data`](https://www.tensorflow.org/api_docs/python/tf/data) API enables you to build complex input pipelines from simple, reusable pieces. Its core data structure is [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset), which represents a sequence of elements in which each element consists of one or more components.

#### Building datasets with sparse tensors

Build datasets from sparse tensors using the same methods that are used to build them from [`tf.Tensor`](https://www.tensorflow.org/api_docs/python/tf/Tensor)s or NumPy arrays, such as [`tf.data.Dataset.from_tensor_slices`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#from_tensor_slices). This op preserves the sparsity (or sparse nature) of the data.

```
dataset = tf.data.Dataset.from_tensor_slices(sparse_data)
for element in dataset: 
  print(pprint_sparse_tensor(element))
```
<SparseTensor shape=[4] 
 values={
  [0]: 1
  [1]: 1
  [2]: 1}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={
  [3]: 1}>
<SparseTensor shape=[4] 
 values={
  [0]: 1
  [1]: 1}>

#### Batching and unbatching datasets with sparse tensors

You can batch (combine consecutive elements into a single element) and unbatch datasets with sparse tensors using the [`Dataset.batch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#batch) and [`Dataset.unbatch`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#unbatch) methods respectively.

```
batched_dataset = dataset.batch(2)
for element in batched_dataset:
  print (pprint_sparse_tensor(element))
```
<SparseTensor shape=[2, 4] 
 values={
  [0, 0]: 1
  [0, 1]: 1
  [0, 2]: 1}>
<SparseTensor shape=[2, 4] 
 values={}>
<SparseTensor shape=[2, 4] 
 values={
  [0, 3]: 1
  [1, 0]: 1
  [1, 1]: 1}>

```
unbatched_dataset = batched_dataset.unbatch()
for element in unbatched_dataset:
  print (pprint_sparse_tensor(element))
```
<SparseTensor shape=[4] 
 values={
  [0]: 1
  [1]: 1
  [2]: 1}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={
  [3]: 1}>
<SparseTensor shape=[4] 
 values={
  [0]: 1
  [1]: 1}>

You can also use [`tf.data.experimental.dense_to_sparse_batch`](https://www.tensorflow.org/api_docs/python/tf/data/experimental/dense_to_sparse_batch) to batch dataset elements of varying shapes into sparse tensors.

#### Transforming Datasets with sparse tensors

Transform and create sparse tensors in Datasets using [`Dataset.map`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset#map).

```
transform_dataset = dataset.map(lambda x: x*2)
for i in transform_dataset:
  print(pprint_sparse_tensor(i))
```
<SparseTensor shape=[4] 
 values={
  [0]: 2
  [1]: 2
  [2]: 2}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={}>
<SparseTensor shape=[4] 
 values={
  [3]: 2}>
<SparseTensor shape=[4] 
 values={
  [0]: 2
  [1]: 2}>

### tf.train.Example

[`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example) is a standard protobuf encoding for TensorFlow data. When using sparse tensors with [`tf.train.Example`](https://www.tensorflow.org/api_docs/python/tf/train/Example), you can:

*   Read variable-length data into a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) using [`tf.io.VarLenFeature`](https://www.tensorflow.org/api_docs/python/tf/io/VarLenFeature). However, you should consider using [`tf.io.RaggedFeature`](https://www.tensorflow.org/api_docs/python/tf/io/RaggedFeature) instead.

*   Read arbitrary sparse data into a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) using [`tf.io.SparseFeature`](https://www.tensorflow.org/api_docs/python/tf/io/SparseFeature), which uses three separate feature keys to store the `indices`, `values`, and `dense_shape`.

### [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function)

The [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) decorator precomputes TensorFlow graphs for Python functions, which can substantially improve the performance of your TensorFlow code. Sparse tensors work transparently with both [`tf.function`](https://www.tensorflow.org/api_docs/python/tf/function) and [concrete functions](https://www.tensorflow.org/guide/function#obtaining_concrete_functions).

```
@tf.function
def f(x,y):
  return tf.sparse.sparse_dense_matmul(x,y)

a = tf.sparse.SparseTensor(indices=[[0, 3], [2, 4]],
                    values=[15, 25],
                    dense_shape=[3, 10])

b = tf.sparse.to_dense(tf.sparse.transpose(a))

c = f(a,b)

print(c)
```
tf.Tensor(
[[225   0   0]
 [  0   0   0]
 [  0   0 625]], shape=(3, 3), dtype=int32)

Distinguishing missing values from zero values
----------------------------------------------

Most ops on [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor)s treat missing values and explicit zero values identically. This is by design — a [`tf.sparse.SparseTensor`](https://www.tensorflow.org/api_docs/python/tf/sparse/SparseTensor) is supposed to act just like a dense tensor.

However, there are a few cases where it can be useful to distinguish zero values from missing values. In particular, this allows for one way to encode missing/unknown data in your training data. For example, consider a use case where you have a tensor of scores (that can have any floating point value from -Inf to +Inf), with some missing scores. You can encode this tensor using a sparse tensor where the explicit zeros are known zero scores but the implicit zero values actually represent missing data and not zero.

Note that some ops like [`tf.sparse.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/sparse/reduce_max) do not treat missing values as if they were zero. For example, when you run the code block below, the expected output is `0`. However, because of this exception, the output is `-3`.

```
print(tf.sparse.reduce_max(tf.sparse.from_dense([-5, 0, -3])))
```
tf.Tensor(-3, shape=(), dtype=int32)

In contrast, when you apply [`tf.math.reduce_max`](https://www.tensorflow.org/api_docs/python/tf/math/reduce_max) to a dense tensor, the output is 0 as expected.

```
print(tf.math.reduce_max([-5, 0, -3]))
```
tf.Tensor(0, shape=(), dtype=int32)

Further reading and resources
-----------------------------

*   Refer to the [tensor guide](https://www.tensorflow.org/guide/tensor) to learn about tensors.
*   Read the [ragged tensor guide](https://www.tensorflow.org/guide/ragged_tensor) to learn how to work with ragged tensors, a type of tensor that lets you work with non-uniform data.
*   Check out this object detection model in the [TensorFlow Model Garden](https://github.com/tensorflow/models) that uses sparse tensors in a [`tf.Example` data decoder](https://github.com/tensorflow/models/blob/9139a7b90112562aec1d7e328593681bd410e1e7/research/object_detection/data_decoders/tf_example_decoder.py).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-10-25 UTC.
