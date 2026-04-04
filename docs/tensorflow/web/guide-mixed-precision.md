# Source: https://www.tensorflow.org/guide/mixed_precision

Title: Mixed precision

URL Source: https://www.tensorflow.org/guide/mixed_precision

Markdown Content:
Overview
--------

Mixed precision is the use of both 16-bit and 32-bit floating-point types in a model during training to make it run faster and use less memory. By keeping certain parts of the model in the 32-bit types for numeric stability, the model will have a lower step time and train equally as well in terms of the evaluation metrics such as accuracy. This guide describes how to use the Keras mixed precision API to speed up your models. Using this API can improve performance by more than 3 times on modern GPUs, 60% on TPUs and more than 2 times on latest Intel CPUs.

Today, most models use the float32 dtype, which takes 32 bits of memory. However, there are two lower-precision dtypes, float16 and bfloat16, each which take 16 bits of memory instead. Modern accelerators can run operations faster in the 16-bit dtypes, as they have specialized hardware to run 16-bit computations and 16-bit dtypes can be read from memory faster.

NVIDIA GPUs can run operations in float16 faster than in float32, and TPUs and supporting Intel CPUs can run operations in bfloat16 faster than float32. Therefore, these lower-precision dtypes should be used whenever possible on those devices. However, variables and a few computations should still be in float32 for numeric reasons so that the model trains to the same quality. The Keras mixed precision API allows you to use a mix of either float16 or bfloat16 with float32, to get the performance benefits from float16/bfloat16 and the numeric stability benefits from float32.

Setup
-----

```
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import mixed_precision
```

Supported hardware
------------------

While mixed precision will run on most hardware, it will only speed up models on recent NVIDIA GPUs, Cloud TPUs and recent Intel CPUs. NVIDIA GPUs support using a mix of float16 and float32, while TPUs and Intel CPUs support a mix of bfloat16 and float32.

Among NVIDIA GPUs, those with compute capability 7.0 or higher will see the greatest performance benefit from mixed precision because they have special hardware units, called Tensor Cores, to accelerate float16 matrix multiplications and convolutions. Older GPUs offer no math performance benefit for using mixed precision, however memory and bandwidth savings can enable some speedups. You can look up the compute capability for your GPU at NVIDIA's [CUDA GPU web page](https://developer.nvidia.com/cuda-gpus). Examples of GPUs that will benefit most from mixed precision include RTX GPUs, the V100, and the A100.

Among Intel CPUs, starting with the 4th Gen Intel Xeon Processors (code name Sapphire Rapids), will see the greatest performance benefit from mixed precision as they can accelerate bfloat16 computations using AMX instructions (requires Tensorflow 2.12 or later).

You can check your GPU type with the following. The command only exists if the NVIDIA drivers are installed, so the following will raise an error otherwise.

`nvidia-smi -L`
All Cloud TPUs support bfloat16.

Even on older Intel CPUs, other x86 CPUs without AMX, and older GPUs, where no speedup is expected, mixed precision APIs can still be used for unit testing, debugging, or just to try out the API. However, mixed_bfloat16 on CPUs without AMX instructions and mixed_float16 on all x86 CPUs will run significantly slower.

Setting the dtype policy
------------------------

To use mixed precision in Keras, you need to create a [`tf.keras.mixed_precision.Policy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy), typically referred to as a _dtype policy_. Dtype policies specify the dtypes layers will run in. In this guide, you will construct a policy from the string `'mixed_float16'` and set it as the global policy. This will cause subsequently created layers to use mixed precision with a mix of float16 and float32.

```
policy = mixed_precision.Policy('mixed_float16')
mixed_precision.set_global_policy(policy)
```

For short, you can directly pass a string to `set_global_policy`, which is typically done in practice.

```
# Equivalent to the two lines above
mixed_precision.set_global_policy('mixed_float16')
```

The policy specifies two important aspects of a layer: the dtype the layer's computations are done in, and the dtype of a layer's variables. Above, you created a `mixed_float16` policy (i.e., a [`mixed_precision.Policy`](https://www.tensorflow.org/api_docs/python/tf/keras/DTypePolicy) created by passing the string `'mixed_float16'` to its constructor). With this policy, layers use float16 computations and float32 variables. Computations are done in float16 for performance, but variables must be kept in float32 for numeric stability. You can directly query these properties of the policy.

```
print('Compute dtype: %s' % policy.compute_dtype)
print('Variable dtype: %s' % policy.variable_dtype)
```

As mentioned before, the `mixed_float16` policy will most significantly improve performance on NVIDIA GPUs with compute capability of at least 7.0. The policy will run on other GPUs and CPUs but may not improve performance. For TPUs and CPUs, the `mixed_bfloat16` policy should be used instead.

Building the model
------------------

Next, let's start building a simple model. Very small toy models typically do not benefit from mixed precision, because overhead from the TensorFlow runtime typically dominates the execution time, making any performance improvement on the GPU negligible. Therefore, let's build two large `Dense` layers with 4096 units each if a GPU is used.

```
inputs = keras.Input(shape=(784,), name='digits')
if tf.config.list_physical_devices('GPU'):
  print('The model will run with 4096 units on a GPU')
  num_units = 4096
else:
  # Use fewer units on CPUs so the model finishes in a reasonable amount of time
  print('The model will run with 64 units on a CPU')
  num_units = 64
dense1 = layers.Dense(num_units, activation='relu', name='dense_1')
x = dense1(inputs)
dense2 = layers.Dense(num_units, activation='relu', name='dense_2')
x = dense2(x)
```

Each layer has a policy and uses the global policy by default. Each of the `Dense` layers therefore have the `mixed_float16` policy because you set the global policy to `mixed_float16` previously. This will cause the dense layers to do float16 computations and have float32 variables. They cast their inputs to float16 in order to do float16 computations, which causes their outputs to be float16 as a result. Their variables are float32 and will be cast to float16 when the layers are called to avoid errors from dtype mismatches.

```
print(dense1.dtype_policy)
print('x.dtype: %s' % x.dtype.name)
# 'kernel' is dense1's variable
print('dense1.kernel.dtype: %s' % dense1.kernel.dtype.name)
```

Next, create the output predictions. Normally, you can create the output predictions as follows, but this is not always numerically stable with float16.

```
# INCORRECT: softmax and model output will be float16, when it should be float32
outputs = layers.Dense(10, activation='softmax', name='predictions')(x)
print('Outputs dtype: %s' % outputs.dtype.name)
```

A softmax activation at the end of the model should be float32. Because the dtype policy is `mixed_float16`, the softmax activation would normally have a float16 compute dtype and output float16 tensors.

This can be fixed by separating the Dense and softmax layers, and by passing `dtype='float32'` to the softmax layer:

```
# CORRECT: softmax and model output are float32
x = layers.Dense(10, name='dense_logits')(x)
outputs = layers.Activation('softmax', dtype='float32', name='predictions')(x)
print('Outputs dtype: %s' % outputs.dtype.name)
```

Passing `dtype='float32'` to the softmax layer constructor overrides the layer's dtype policy to be the `float32` policy, which does computations and keeps variables in float32. Equivalently, you could have instead passed `dtype=mixed_precision.Policy('float32')`; layers always convert the dtype argument to a policy. Because the `Activation` layer has no variables, the policy's variable dtype is ignored, but the policy's compute dtype of float32 causes softmax and the model output to be float32.

Adding a float16 softmax in the middle of a model is fine, but a softmax at the end of the model should be in float32. The reason is that if the intermediate tensor flowing from the softmax to the loss is float16 or bfloat16, numeric issues may occur.

You can override the dtype of any layer to be float32 by passing `dtype='float32'` if you think it will not be numerically stable with float16 computations. But typically, this is only necessary on the last layer of the model, as most layers have sufficient precision with `mixed_float16` and `mixed_bfloat16`.

Even if the model does not end in a softmax, the outputs should still be float32. While unnecessary for this specific model, the model outputs can be cast to float32 with the following:

```
# The linear activation is an identity function. So this simply casts 'outputs'
# to float32. In this particular case, 'outputs' is already float32 so this is a
# no-op.
outputs = layers.Activation('linear', dtype='float32')(outputs)
```

Next, finish and compile the model, and generate input data:

```
model = keras.Model(inputs=inputs, outputs=outputs)
model.compile(loss='sparse_categorical_crossentropy',
              optimizer=keras.optimizers.RMSprop(),
              metrics=['accuracy'])

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train = x_train.reshape(60000, 784).astype('float32') / 255
x_test = x_test.reshape(10000, 784).astype('float32') / 255
```

This example casts the input data from int8 to float32. You don't cast to float16 since the division by 255 is on the CPU, which runs float16 operations slower than float32 operations. In this case, the performance difference is negligible, but in general you should run input processing math in float32 if it runs on the CPU. The first layer of the model will cast the inputs to float16, as each layer casts floating-point inputs to its compute dtype.

The initial weights of the model are retrieved. This will allow training from scratch again by loading the weights.

```
initial_weights = model.get_weights()
```

Training the model with Model.fit
---------------------------------

Next, train the model:

```
history = model.fit(x_train, y_train,
                    batch_size=8192,
                    epochs=5,
                    validation_split=0.2)
test_scores = model.evaluate(x_test, y_test, verbose=2)
print('Test loss:', test_scores[0])
print('Test accuracy:', test_scores[1])
```

Notice the model prints the time per step in the logs: for example, "25ms/step". The first epoch may be slower as TensorFlow spends some time optimizing the model, but afterwards the time per step should stabilize.

If you are running this guide in Colab, you can compare the performance of mixed precision with float32. To do so, change the policy from `mixed_float16` to `float32` in the "Setting the dtype policy" section, then rerun all the cells up to this point. On GPUs with compute capability 7.X, you should see the time per step significantly increase, indicating mixed precision sped up the model. Make sure to change the policy back to `mixed_float16` and rerun the cells before continuing with the guide.

On GPUs with compute capability of at least 8.0 (Ampere GPUs and above), you likely will see no performance improvement in the toy model in this guide when using mixed precision compared to float32. This is due to the use of [TensorFloat-32](https://www.tensorflow.org/api_docs/python/tf/config/experimental/enable_tensor_float_32_execution), which automatically uses lower precision math in certain float32 ops such as [`tf.linalg.matmul`](https://www.tensorflow.org/api_docs/python/tf/linalg/matmul). TensorFloat-32 gives some of the performance advantages of mixed precision when using float32. However, in real-world models, you will still typically experience significant performance improvements from mixed precision due to memory bandwidth savings and ops which TensorFloat-32 does not support.

If running mixed precision on a TPU, you will not see as much of a performance gain compared to running mixed precision on GPUs, especially pre-Ampere GPUs. This is because TPUs do certain ops in bfloat16 under the hood even with the default dtype policy of float32. This is similar to how Ampere GPUs use TensorFloat-32 by default. Compared to Ampere GPUs, TPUs typically see less performance gains with mixed precision on real-world models.

For many real-world models, mixed precision also allows you to double the batch size without running out of memory, as float16 tensors take half the memory. This does not apply however to this toy model, as you can likely run the model in any dtype where each batch consists of the entire MNIST dataset of 60,000 images.

Loss scaling
------------

Loss scaling is a technique which [`tf.keras.Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit) automatically performs with the `mixed_float16` policy to avoid numeric underflow. This section describes what loss scaling is and the next section describes how to use it with a custom training loop.

### Underflow and Overflow

The float16 data type has a narrow dynamic range compared to float32. This means values above \(65504\) will overflow to infinity and values below \(6.0 \times 10^{-8}\) will underflow to zero. float32 and bfloat16 have a much higher dynamic range so that overflow and underflow are not a problem.

For example:

```
x = tf.constant(256, dtype='float16')
(x ** 2).numpy()  # Overflow
```

```
x = tf.constant(1e-5, dtype='float16')
(x ** 2).numpy()  # Underflow
```

In practice, overflow with float16 rarely occurs. Additionally, underflow also rarely occurs during the forward pass. However, during the backward pass, gradients can underflow to zero. Loss scaling is a technique to prevent this underflow.

### Loss scaling overview

The basic concept of loss scaling is simple: simply multiply the loss by some large number, say \(1024\), and you get the _loss scale_ value. This will cause the gradients to scale by \(1024\) as well, greatly reducing the chance of underflow. Once the final gradients are computed, divide them by \(1024\) to bring them back to their correct values.

The pseudocode for this process is:

```
loss_scale = 1024
loss = model(inputs)
loss *= loss_scale
# Assume `grads` are float32. You do not want to divide float16 gradients.
grads = compute_gradient(loss, model.trainable_variables)
grads /= loss_scale
```

Choosing a loss scale can be tricky. If the loss scale is too low, gradients may still underflow to zero. If too high, the opposite the problem occurs: the gradients may overflow to infinity.

To solve this, TensorFlow dynamically determines the loss scale so you do not have to choose one manually. If you use [`tf.keras.Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit), loss scaling is done for you so you do not have to do any extra work. If you use a custom training loop, you must explicitly use the special optimizer wrapper [`tf.keras.mixed_precision.LossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer) in order to use loss scaling. This is described in the next section.

Training the model with a custom training loop
----------------------------------------------

So far, you have trained a Keras model with mixed precision using [`tf.keras.Model.fit`](https://www.tensorflow.org/api_docs/python/tf/keras/Model#fit). Next, you will use mixed precision with a custom training loop. If you do not already know what a custom training loop is, please read the [Custom training guide](https://www.tensorflow.org/tutorials/customization/custom_training_walkthrough) first.

Running a custom training loop with mixed precision requires two changes over running it in float32:

1.   Build the model with mixed precision (you already did this)
2.   Explicitly use loss scaling if `mixed_float16` is used.

For step (2), you will use the [`tf.keras.mixed_precision.LossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer) class, which wraps an optimizer and applies loss scaling. By default, it dynamically determines the loss scale so you do not have to choose one. Construct a `LossScaleOptimizer` as follows.

```
optimizer = keras.optimizers.RMSprop()
optimizer = mixed_precision.LossScaleOptimizer(optimizer)
```

If you want, it is possible choose an explicit loss scale or otherwise customize the loss scaling behavior, but it is highly recommended to keep the default loss scaling behavior, as it has been found to work well on all known models. See the [`tf.keras.mixed_precision.LossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer) documentation if you want to customize the loss scaling behavior.

Next, define the loss object and the [`tf.data.Dataset`](https://www.tensorflow.org/api_docs/python/tf/data/Dataset)s:

```
loss_object = tf.keras.losses.SparseCategoricalCrossentropy()
train_dataset = (tf.data.Dataset.from_tensor_slices((x_train, y_train))
                 .shuffle(10000).batch(8192))
test_dataset = tf.data.Dataset.from_tensor_slices((x_test, y_test)).batch(8192)
```

Next, define the training step function. You will use two new methods from the loss scale optimizer to scale the loss and unscale the gradients:

*   `get_scaled_loss(loss)`: Multiplies the loss by the loss scale
*   `get_unscaled_gradients(gradients)`: Takes in a list of scaled gradients as inputs, and divides each one by the loss scale to unscale them

These functions must be used in order to prevent underflow in the gradients. [`LossScaleOptimizer.apply_gradients`](https://www.tensorflow.org/api_docs/python/tf/keras/Optimizer#apply_gradients) will then apply gradients if none of them have `Inf`s or `NaN`s. It will also update the loss scale, halving it if the gradients had `Inf`s or `NaN`s and potentially increasing it otherwise.

```
@tf.function
def train_step(x, y):
  with tf.GradientTape() as tape:
    predictions = model(x)
    loss = loss_object(y, predictions)
    scaled_loss = optimizer.get_scaled_loss(loss)
  scaled_gradients = tape.gradient(scaled_loss, model.trainable_variables)
  gradients = optimizer.get_unscaled_gradients(scaled_gradients)
  optimizer.apply_gradients(zip(gradients, model.trainable_variables))
  return loss
```

The `LossScaleOptimizer` will likely skip the first few steps at the start of training. The loss scale starts out high so that the optimal loss scale can quickly be determined. After a few steps, the loss scale will stabilize and very few steps will be skipped. This process happens automatically and does not affect training quality.

Now, define the test step:

```
@tf.function
def test_step(x):
  return model(x, training=False)
```

Load the initial weights of the model, so you can retrain from scratch:

```
model.set_weights(initial_weights)
```

Finally, run the custom training loop:

```
for epoch in range(5):
  epoch_loss_avg = tf.keras.metrics.Mean()
  test_accuracy = tf.keras.metrics.SparseCategoricalAccuracy(
      name='test_accuracy')
  for x, y in train_dataset:
    loss = train_step(x, y)
    epoch_loss_avg(loss)
  for x, y in test_dataset:
    predictions = test_step(x)
    test_accuracy.update_state(y, predictions)
  print('Epoch {}: loss={}, test accuracy={}'.format(epoch, epoch_loss_avg.result(), test_accuracy.result()))
```

GPU performance tips
--------------------

Here are some performance tips when using mixed precision on GPUs.

### Increasing your batch size

If it doesn't affect model quality, try running with double the batch size when using mixed precision. As float16 tensors use half the memory, this often allows you to double your batch size without running out of memory. Increasing batch size typically increases training throughput, i.e. the training elements per second your model can run on.

### Ensuring GPU Tensor Cores are used

As mentioned previously, modern NVIDIA GPUs use a special hardware unit called Tensor Cores that can multiply float16 matrices very quickly. However, Tensor Cores requires certain dimensions of tensors to be a multiple of 8. In the examples below, an argument is bold if and only if it needs to be a multiple of 8 for Tensor Cores to be used.

*   tf.keras.layers.Dense(**units=64**)
*   tf.keras.layers.Conv2d(**filters=48**, kernel_size=7, stride=3) 
    *   And similarly for other convolutional layers, such as tf.keras.layers.Conv3d

*   tf.keras.layers.LSTM(**units=64**) 
    *   And similar for other RNNs, such as tf.keras.layers.GRU

*   tf.keras.Model.fit(epochs=2, **batch_size=128**)

You should try to use Tensor Cores when possible. If you want to learn more, [NVIDIA deep learning performance guide](https://docs.nvidia.com/deeplearning/sdk/dl-performance-guide/index.html) describes the exact requirements for using Tensor Cores as well as other Tensor Core-related performance information.

### XLA

XLA is a compiler that can further increase mixed precision performance, as well as float32 performance to a lesser extent. Refer to the [XLA guide](https://www.tensorflow.org/xla) for details.

Cloud TPU performance tips
--------------------------

As with GPUs, you should try doubling your batch size when using Cloud TPUs because bfloat16 tensors use half the memory. Doubling batch size may increase training throughput.

TPUs do not require any other mixed precision-specific tuning to get optimal performance. They already require the use of XLA. TPUs benefit from having certain dimensions being multiples of \(128\), but this applies equally to the float32 type as it does for mixed precision. Check the [Cloud TPU performance guide](https://cloud.google.com/tpu/docs/performance-guide) for general TPU performance tips, which apply to mixed precision as well as float32 tensors.

Summary
-------

*   You should use mixed precision if you use TPUs, NVIDIA GPUs with at least compute capability 7.0, or Intel CPUs with support for AMX instructions, as it will improve performance by up to 3x.
*   You can use mixed precision with the following lines:

```
# On TPUs and CPUs, use 'mixed_bfloat16' instead
mixed_precision.set_global_policy('mixed_float16')
```
*   If your model ends in softmax, make sure it is float32. And regardless of what your model ends in, make sure the output is float32.

*   If you use a custom training loop with `mixed_float16`, in addition to the above lines, you need to wrap your optimizer with a [`tf.keras.mixed_precision.LossScaleOptimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision/LossScaleOptimizer). Then call `optimizer.get_scaled_loss` to scale the loss, and `optimizer.get_unscaled_gradients` to unscale the gradients.

*   If you use a custom training loop with `mixed_bfloat16`, setting the global_policy mentioned above is sufficient.

*   Double the training batch size if it does not reduce evaluation accuracy

*   On GPUs, ensure most tensor dimensions are a multiple of \(8\) to maximize performance

For an example of mixed precision using the [`tf.keras.mixed_precision`](https://www.tensorflow.org/api_docs/python/tf/keras/mixed_precision) API, check [functions and classes related to training performance](https://github.com/tensorflow/models/blob/master/official/modeling/performance.py). Check out the official models, such as [Transformer](https://github.com/tensorflow/models/blob/master/official/nlp/modeling/layers/transformer_encoder_block.py), for details.
