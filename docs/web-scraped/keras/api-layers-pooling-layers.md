# Source: https://keras.io/api/layers/pooling_layers/

Title: Keras documentation: Pooling layers

URL Source: https://keras.io/api/layers/pooling_layers/

Markdown Content:
Pooling layers
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[The base Layer class](https://keras.io/api/layers/base_layer/)[Layer activations](https://keras.io/api/layers/activations/)[Layer weight initializers](https://keras.io/api/layers/initializers/)[Layer weight regularizers](https://keras.io/api/layers/regularizers/)[Layer weight constraints](https://keras.io/api/layers/constraints/)[Core layers](https://keras.io/api/layers/core_layers/)[Convolution layers](https://keras.io/api/layers/convolution_layers/)[Pooling layers](https://keras.io/api/layers/pooling_layers/)[Recurrent layers](https://keras.io/api/layers/recurrent_layers/)[Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)[Normalization layers](https://keras.io/api/layers/normalization_layers/)[Regularization layers](https://keras.io/api/layers/regularization_layers/)[Attention layers](https://keras.io/api/layers/attention_layers/)[Reshaping layers](https://keras.io/api/layers/reshaping_layers/)[Merging layers](https://keras.io/api/layers/merging_layers/)[Activation layers](https://keras.io/api/layers/activation_layers/)[Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[The base Layer class](https://keras.io/api/layers/base_layer/)[Layer activations](https://keras.io/api/layers/activations/)[Layer weight initializers](https://keras.io/api/layers/initializers/)[Layer weight regularizers](https://keras.io/api/layers/regularizers/)[Layer weight constraints](https://keras.io/api/layers/constraints/)[Core layers](https://keras.io/api/layers/core_layers/)[Convolution layers](https://keras.io/api/layers/convolution_layers/)[Pooling layers](https://keras.io/api/layers/pooling_layers/)[Recurrent layers](https://keras.io/api/layers/recurrent_layers/)[Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/)[Normalization layers](https://keras.io/api/layers/normalization_layers/)[Regularization layers](https://keras.io/api/layers/regularization_layers/)[Attention layers](https://keras.io/api/layers/attention_layers/)[Reshaping layers](https://keras.io/api/layers/reshaping_layers/)[Merging layers](https://keras.io/api/layers/merging_layers/)[Activation layers](https://keras.io/api/layers/activation_layers/)[Backend-specific layers](https://keras.io/api/layers/backend_specific_layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Layers API](https://keras.io/api/layers/) / Pooling layers 

Pooling layers
==============

*   [MaxPooling1D layer](https://keras.io/api/layers/pooling_layers/max_pooling1d/)
*   [MaxPooling2D layer](https://keras.io/api/layers/pooling_layers/max_pooling2d/)
*   [MaxPooling3D layer](https://keras.io/api/layers/pooling_layers/max_pooling3d/)
*   [AveragePooling1D layer](https://keras.io/api/layers/pooling_layers/average_pooling1d/)
*   [AveragePooling2D layer](https://keras.io/api/layers/pooling_layers/average_pooling2d/)
*   [AveragePooling3D layer](https://keras.io/api/layers/pooling_layers/average_pooling3d/)
*   [GlobalMaxPooling1D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling1d/)
*   [GlobalMaxPooling2D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling2d/)
*   [GlobalMaxPooling3D layer](https://keras.io/api/layers/pooling_layers/global_max_pooling3d/)
*   [GlobalAveragePooling1D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling1d/)
*   [GlobalAveragePooling2D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling2d/)
*   [GlobalAveragePooling3D layer](https://keras.io/api/layers/pooling_layers/global_average_pooling3d/)
*   [AdaptiveAveragePooling1D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling1d/)
*   [AdaptiveAveragePooling2D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling2d/)
*   [AdaptiveAveragePooling3D layer](https://keras.io/api/layers/pooling_layers/adaptive_average_pooling3d/)
*   [AdaptiveMaxPooling1D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling1d/)
*   [AdaptiveMaxPooling2D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling2d/)
*   [AdaptiveMaxPooling3D layer](https://keras.io/api/layers/pooling_layers/adaptive_max_pooling3d/)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
