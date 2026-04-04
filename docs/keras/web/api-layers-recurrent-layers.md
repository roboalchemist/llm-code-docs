# Source: https://keras.io/api/layers/recurrent_layers/

Title: Keras documentation: Recurrent layers

URL Source: https://keras.io/api/layers/recurrent_layers/

Markdown Content:
Recurrent layers
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[The base Layer class](https://keras.io/api/layers/base_layer/)[Layer activations](https://keras.io/api/layers/activations/)[Layer weight initializers](https://keras.io/api/layers/initializers/)[Layer weight regularizers](https://keras.io/api/layers/regularizers/)[Layer weight constraints](https://keras.io/api/layers/constraints/)[Core layers](https://keras.io/api/layers/core_layers/)[Convolution layers](https://keras.io/api/layers/convolution_layers/)[Pooling layers](https://keras.io/api/layers/pooling_layers/)[Recurrent layers](https://keras.io/api/layers/recurrent_layers/)[Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)[Normalization layers](https://keras.io/api/layers/normalization_layers/)[Regularization layers](https://keras.io/api/layers/regularization_layers/)[Attention layers](https://keras.io/api/layers/attention_layers/)[Reshaping layers](https://keras.io/api/layers/reshaping_layers/)[Merging layers](https://keras.io/api/layers/merging_layers/)[Activation layers](https://keras.io/api/layers/activation_layers/)[Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[The base Layer class](https://keras.io/api/layers/base_layer/)[Layer activations](https://keras.io/api/layers/activations/)[Layer weight initializers](https://keras.io/api/layers/initializers/)[Layer weight regularizers](https://keras.io/api/layers/regularizers/)[Layer weight constraints](https://keras.io/api/layers/constraints/)[Core layers](https://keras.io/api/layers/core_layers/)[Convolution layers](https://keras.io/api/layers/convolution_layers/)[Pooling layers](https://keras.io/api/layers/pooling_layers/)[Recurrent layers](https://keras.io/api/layers/recurrent_layers/)[Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)[Normalization layers](https://keras.io/api/layers/normalization_layers/)[Regularization layers](https://keras.io/api/layers/regularization_layers/)[Attention layers](https://keras.io/api/layers/attention_layers/)[Reshaping layers](https://keras.io/api/layers/reshaping_layers/)[Merging layers](https://keras.io/api/layers/merging_layers/)[Activation layers](https://keras.io/api/layers/activation_layers/)[Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Layers API](https://keras.io/api/layers/) / Recurrent layers 

Recurrent layers
================

*   [LSTM layer](https://keras.io/api/layers/recurrent_layers/lstm/)
*   [LSTM cell layer](https://keras.io/api/layers/recurrent_layers/lstm_cell/)
*   [GRU layer](https://keras.io/api/layers/recurrent_layers/gru/)
*   [GRU Cell layer](https://keras.io/api/layers/recurrent_layers/gru_cell/)
*   [SimpleRNN layer](https://keras.io/api/layers/recurrent_layers/simple_rnn/)
*   [TimeDistributed layer](https://keras.io/api/layers/recurrent_layers/time_distributed/)
*   [Bidirectional layer](https://keras.io/api/layers/recurrent_layers/bidirectional/)
*   [ConvLSTM1D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm1d/)
*   [ConvLSTM2D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm2d/)
*   [ConvLSTM3D layer](https://keras.io/api/layers/recurrent_layers/conv_lstm3d/)
*   [Base RNN layer](https://keras.io/api/layers/recurrent_layers/rnn/)
*   [Simple RNN cell layer](https://keras.io/api/layers/recurrent_layers/simple_rnn_cell/)
*   [Stacked RNN cell layer](https://keras.io/api/layers/recurrent_layers/stacked_rnn_cell/)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
