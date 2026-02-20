# Source: https://keras.io/api/layers/

Title: Keras documentation: Keras layers API

URL Source: https://keras.io/api/layers/

Markdown Content:
Layers are the basic building blocks of neural networks in Keras. A layer consists of a tensor-in tensor-out computation function (the layer's `call` method) and some state, held in TensorFlow variables (the layer's _weights_).

A Layer instance is callable, much like a function:

```
import keras
from keras import layers

layer = layers.Dense(32, activation='relu')
inputs = keras.random.uniform(shape=(10, 20))
outputs = layer(inputs)
```

Unlike a function, though, layers maintain a state, updated when the layer receives data during training, and stored in `layer.weights`:

```
>>> layer.weights
[<KerasVariable shape=(20, 32), dtype=float32, path=dense/kernel>,
 <KerasVariable shape=(32,), dtype=float32, path=dense/bias>]
```

* * *

Creating custom layers
----------------------

While Keras offers a wide range of built-in layers, they don't cover ever possible use case. Creating custom layers is very common, and very easy.

See the guide [Making new layers and models via subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing) for an extensive overview, and refer to the documentation for [the base `Layer` class](https://keras.io/api/layers/base_layer).

* * *

Layers API overview
-------------------

### [The base Layer class](https://keras.io/api/layers/base_layer/)

*   [Layer class](https://keras.io/api/layers/base_layer/#layer-class)
*   [weights property](https://keras.io/api/layers/base_layer/#weights-property)
*   [trainable_weights property](https://keras.io/api/layers/base_layer/#trainable_weights-property)
*   [non_trainable_weights property](https://keras.io/api/layers/base_layer/#non_trainable_weights-property)
*   [add_weight method](https://keras.io/api/layers/base_layer/#add_weight-method)
*   [trainable property](https://keras.io/api/layers/base_layer/#trainable-property)
*   [get_weights method](https://keras.io/api/layers/base_layer/#get_weights-method)
*   [set_weights method](https://keras.io/api/layers/base_layer/#set_weights-method)
*   [get_config method](https://keras.io/api/layers/base_layer/#get_config-method)
*   [add_loss method](https://keras.io/api/layers/base_layer/#add_loss-method)
*   [losses property](https://keras.io/api/layers/base_layer/#losses-property)

### [Layer activations](https://keras.io/api/layers/activations/)

*   [celu function](https://keras.io/api/layers/activations/#celu-function)
*   [elu function](https://keras.io/api/layers/activations/#elu-function)
*   [exponential function](https://keras.io/api/layers/activations/#exponential-function)
*   [gelu function](https://keras.io/api/layers/activations/#gelu-function)
*   [glu function](https://keras.io/api/layers/activations/#glu-function)
*   [hard_shrink function](https://keras.io/api/layers/activations/#hard_shrink-function)
*   [hard_sigmoid function](https://keras.io/api/layers/activations/#hard_sigmoid-function)
*   [hard_silu function](https://keras.io/api/layers/activations/#hard_silu-function)
*   [hard_tanh function](https://keras.io/api/layers/activations/#hard_tanh-function)
*   [leaky_relu function](https://keras.io/api/layers/activations/#leaky_relu-function)
*   [linear function](https://keras.io/api/layers/activations/#linear-function)
*   [log_sigmoid function](https://keras.io/api/layers/activations/#log_sigmoid-function)
*   [log_softmax function](https://keras.io/api/layers/activations/#log_softmax-function)
*   [mish function](https://keras.io/api/layers/activations/#mish-function)
*   [relu function](https://keras.io/api/layers/activations/#relu-function)
*   [relu6 function](https://keras.io/api/layers/activations/#relu6-function)
*   [selu function](https://keras.io/api/layers/activations/#selu-function)
*   [sigmoid function](https://keras.io/api/layers/activations/#sigmoid-function)
*   [silu function](https://keras.io/api/layers/activations/#silu-function)
*   [softmax function](https://keras.io/api/layers/activations/#softmax-function)
*   [soft_shrink function](https://keras.io/api/layers/activations/#soft_shrink-function)
*   [softplus function](https://keras.io/api/layers/activations/#softplus-function)
*   [softsign function](https://keras.io/api/layers/activations/#softsign-function)
*   [sparse_plus function](https://keras.io/api/layers/activations/#sparse_plus-function)
*   [sparsemax function](https://keras.io/api/layers/activations/#sparsemax-function)
*   [squareplus function](https://keras.io/api/layers/activations/#squareplus-function)
*   [tanh function](https://keras.io/api/layers/activations/#tanh-function)
*   [tanh_shrink function](https://keras.io/api/layers/activations/#tanh_shrink-function)
*   [threshold function](https://keras.io/api/layers/activations/#threshold-function)

### [Layer weight initializers](https://keras.io/api/layers/initializers/)

*   [RandomNormal class](https://keras.io/api/layers/initializers/#randomnormal-class)
*   [RandomUniform class](https://keras.io/api/layers/initializers/#randomuniform-class)
*   [TruncatedNormal class](https://keras.io/api/layers/initializers/#truncatednormal-class)
*   [Zeros class](https://keras.io/api/layers/initializers/#zeros-class)
*   [Ones class](https://keras.io/api/layers/initializers/#ones-class)
*   [GlorotNormal class](https://keras.io/api/layers/initializers/#glorotnormal-class)
*   [GlorotUniform class](https://keras.io/api/layers/initializers/#glorotuniform-class)
*   [HeNormal class](https://keras.io/api/layers/initializers/#henormal-class)
*   [HeUniform class](https://keras.io/api/layers/initializers/#heuniform-class)
*   [Orthogonal class](https://keras.io/api/layers/initializers/#orthogonal-class)
*   [Constant class](https://keras.io/api/layers/initializers/#constant-class)
*   [VarianceScaling class](https://keras.io/api/layers/initializers/#variancescaling-class)
*   [LecunNormal class](https://keras.io/api/layers/initializers/#lecunnormal-class)
*   [LecunUniform class](https://keras.io/api/layers/initializers/#lecununiform-class)
*   [IdentityInitializer class](https://keras.io/api/layers/initializers/#identity-class)

### [Layer weight regularizers](https://keras.io/api/layers/regularizers/)

*   [Regularizer class](https://keras.io/api/layers/regularizers/#regularizer-class)
*   [L1 class](https://keras.io/api/layers/regularizers/#l1-class)
*   [L2 class](https://keras.io/api/layers/regularizers/#l2-class)
*   [L1L2 class](https://keras.io/api/layers/regularizers/#l1l2-class)
*   [OrthogonalRegularizer class](https://keras.io/api/layers/regularizers/#orthogonalregularizer-class)

### [Layer weight constraints](https://keras.io/api/layers/constraints/)

*   [Constraint class](https://keras.io/api/layers/constraints/#constraint-class)
*   [MaxNorm class](https://keras.io/api/layers/constraints/#maxnorm-class)
*   [MinMaxNorm class](https://keras.io/api/layers/constraints/#minmaxnorm-class)
*   [NonNeg class](https://keras.io/api/layers/constraints/#nonneg-class)
*   [UnitNorm class](https://keras.io/api/layers/constraints/#unitnorm-class)

### [Core layers](https://keras.io/api/layers/core_layers/)

*   [Input object](https://keras.io/api/layers/core_layers/input)
*   [InputSpec object](https://keras.io/api/layers/core_layers/input_spec)
*   [Dense layer](https://keras.io/api/layers/core_layers/dense)
*   [EinsumDense layer](https://keras.io/api/layers/core_layers/einsum_dense)
*   [Activation layer](https://keras.io/api/layers/core_layers/activation)
*   [Embedding layer](https://keras.io/api/layers/core_layers/embedding)
*   [Masking layer](https://keras.io/api/layers/core_layers/masking)
*   [Lambda layer](https://keras.io/api/layers/core_layers/lambda)
*   [Identity layer](https://keras.io/api/layers/core_layers/identity)

### [Convolution layers](https://keras.io/api/layers/convolution_layers/)

*   [Conv1D layer](https://keras.io/api/layers/convolution_layers/convolution1d)
*   [Conv2D layer](https://keras.io/api/layers/convolution_layers/convolution2d)
*   [Conv3D layer](https://keras.io/api/layers/convolution_layers/convolution3d)
*   [SeparableConv1D layer](https://keras.io/api/layers/convolution_layers/separable_convolution1d)
*   [SeparableConv2D layer](https://keras.io/api/layers/convolution_layers/separable_convolution2d)
*   [DepthwiseConv1D layer](https://keras.io/api/layers/convolution_layers/depthwise_convolution1d)
*   [DepthwiseConv2D layer](https://keras.io/api/layers/convolution_layers/depthwise_convolution2d)
*   [Conv1DTranspose layer](https://keras.io/api/layers/convolution_layers/convolution1d_transpose)
*   [Conv2DTranspose layer](https://keras.io/api/layers/convolution_layers/convolution2d_transpose)
*   [Conv3DTranspose layer](https://keras.io/api/layers/convolution_layers/convolution3d_transpose)

### [Pooling layers](https://keras.io/api/layers/pooling_layers/)

*   [MaxPooling1D layer](https://keras.io/api/layers/pooling_layers/max_pooling1d)
*   [MaxPooling2D layer](https://keras.io/api/layers/pooling_layers/max_pooling2d)
*   [MaxPooling3D layer](https://keras.io/api/layers/pooling_layers/max_pooling3d)
*   [AveragePooling1D layer](https://keras.io/api/layers/pooling_layers/average_pooling1d)
*   [AveragePooling2D layer](https://keras.io/api/layers/pooling_layers/average_pooling2d)
*   [AveragePooling3D layer](https://keras.io/api/layers/pooling_layers/average_pooling3d)
*   [GlobalMaxPooling1D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling1d)
*   [GlobalMaxPooling2D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling2d)
*   [GlobalMaxPooling3D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling3d)
*   [GlobalAveragePooling1D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling1d)
*   [GlobalAveragePooling2D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling2d)
*   [GlobalAveragePooling3D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling3d)
*   [AdaptiveAveragePooling1D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling1d)
*   [AdaptiveAveragePooling2D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling2d)
*   [AdaptiveAveragePooling3D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling3d)
*   [AdaptiveMaxPooling1D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling1d)
*   [AdaptiveMaxPooling2D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling2d)
*   [AdaptiveMaxPooling3D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling3d)

### [Recurrent layers](https://keras.io/api/layers/recurrent_layers/)

*   [LSTM layer](https://keras.io/api/layers/recurrent_layers/lstm)
*   [LSTM cell layer](https://keras.io/api/layers/recurrent_layers/lstm_cell)
*   [GRU layer](https://keras.io/api/layers/recurrent_layers/gru)
*   [GRU Cell layer](https://keras.io/api/layers/recurrent_layers/gru_cell)
*   [SimpleRNN layer](https://keras.io/api/layers/recurrent_layers/simple_rnn)
*   [TimeDistributed layer](https://keras.io/api/layers/recurrent_layers/time_distributed)
*   [Bidirectional layer](https://keras.io/api/layers/recurrent_layers/bidirectional)
*   [ConvLSTM1D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm1d)
*   [ConvLSTM2D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm2d)
*   [ConvLSTM3D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm3d)
*   [Base RNN layer](https://keras.io/api/layers/recurrent_layers/rnn)
*   [Simple RNN cell layer](https://keras.io/api/layers/recurrent_layers/simple_rnn_cell)
*   [Stacked RNN cell layer](https://keras.io/api/layers/recurrent_layers/stacked_rnn_cell)

### [Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)

*   [Text preprocessing](https://keras.io/api/layers/preprocessing_layers/text/)
*   [Numerical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/numerical/)
*   [Categorical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/categorical/)
*   [Image preprocessing layers](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/)
*   [Image augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/)
*   [Audio preprocessing layers](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/)

### [Normalization layers](https://keras.io/api/layers/normalization_layers/)

*   [BatchNormalization layer](https://keras.io/api/layers/normalization_layers/batch_normalization)
*   [LayerNormalization layer](https://keras.io/api/layers/normalization_layers/layer_normalization)
*   [UnitNormalization layer](https://keras.io/api/layers/normalization_layers/unit_normalization)
*   [GroupNormalization layer](https://keras.io/api/layers/normalization_layers/group_normalization)
*   [RMSNormalization layer](https://keras.io/api/layers/normalization_layers/rms_normalization)

### [Regularization layers](https://keras.io/api/layers/regularization_layers/)

*   [Dropout layer](https://keras.io/api/layers/regularization_layers/dropout)
*   [SpatialDropout1D layer](https://keras.io/api/layers/regularization_layers/spatial_dropout1d)
*   [SpatialDropout2D layer](https://keras.io/api/layers/regularization_layers/spatial_dropout2d)
*   [SpatialDropout3D layer](https://keras.io/api/layers/regularization_layers/spatial_dropout3d)
*   [GaussianDropout layer](https://keras.io/api/layers/regularization_layers/gaussian_dropout)
*   [AlphaDropout layer](https://keras.io/api/layers/regularization_layers/alpha_dropout)
*   [GaussianNoise layer](https://keras.io/api/layers/regularization_layers/gaussian_noise)
*   [ActivityRegularization layer](https://keras.io/api/layers/regularization_layers/activity_regularization)

### [Attention layers](https://keras.io/api/layers/attention_layers/)

*   [GroupQueryAttention](https://keras.io/api/layers/attention_layers/group_query_attention)
*   [MultiHeadAttention layer](https://keras.io/api/layers/attention_layers/multi_head_attention)
*   [Attention layer](https://keras.io/api/layers/attention_layers/attention)
*   [AdditiveAttention layer](https://keras.io/api/layers/attention_layers/additive_attention)

### [Reshaping layers](https://keras.io/api/layers/reshaping_layers/)

*   [Reshape layer](https://keras.io/api/layers/reshaping_layers/reshape)
*   [Flatten layer](https://keras.io/api/layers/reshaping_layers/flatten)
*   [RepeatVector layer](https://keras.io/api/layers/reshaping_layers/repeat_vector)
*   [Permute layer](https://keras.io/api/layers/reshaping_layers/permute)
*   [Cropping1D layer](https://keras.io/api/layers/reshaping_layers/cropping1d)
*   [Cropping2D layer](https://keras.io/api/layers/reshaping_layers/cropping2d)
*   [Cropping3D layer](https://keras.io/api/layers/reshaping_layers/cropping3d)
*   [UpSampling1D layer](https://keras.io/api/layers/reshaping_layers/up_sampling1d)
*   [UpSampling2D layer](https://keras.io/api/layers/reshaping_layers/up_sampling2d)
*   [UpSampling3D layer](https://keras.io/api/layers/reshaping_layers/up_sampling3d)
*   [ZeroPadding1D layer](https://keras.io/api/layers/reshaping_layers/zero_padding1d)
*   [ZeroPadding2D layer](https://keras.io/api/layers/reshaping_layers/zero_padding2d)
*   [ZeroPadding3D layer](https://keras.io/api/layers/reshaping_layers/zero_padding3d)

### [Merging layers](https://keras.io/api/layers/merging_layers/)

*   [Concatenate layer](https://keras.io/api/layers/merging_layers/concatenate)
*   [Average layer](https://keras.io/api/layers/merging_layers/average)
*   [Maximum layer](https://keras.io/api/layers/merging_layers/maximum)
*   [Minimum layer](https://keras.io/api/layers/merging_layers/minimum)
*   [Add layer](https://keras.io/api/layers/merging_layers/add)
*   [Subtract layer](https://keras.io/api/layers/merging_layers/subtract)
*   [Multiply layer](https://keras.io/api/layers/merging_layers/multiply)
*   [Dot layer](https://keras.io/api/layers/merging_layers/dot)

### [Activation layers](https://keras.io/api/layers/activation_layers/)

*   [ReLU layer](https://keras.io/api/layers/activation_layers/relu)
*   [Softmax layer](https://keras.io/api/layers/activation_layers/softmax)
*   [LeakyReLU layer](https://keras.io/api/layers/activation_layers/leaky_relu)
*   [PReLU layer](https://keras.io/api/layers/activation_layers/prelu)
*   [ELU layer](https://keras.io/api/layers/activation_layers/elu)

### [Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)

*   [TorchModuleWrapper layer](https://keras.io/api/layers/backend_specific_layers/torch_module_wrapper)
*   [Tensorflow SavedModel layer](https://keras.io/api/layers/backend_specific_layers/tfsm_layer)
*   [JaxLayer](https://keras.io/api/layers/backend_specific_layers/jax_layer)
*   [FlaxLayer](https://keras.io/api/layers/backend_specific_layers/flax_layer)
