# Source: https://keras.io/api/layers/core_layers/

Title: Keras documentation: Core layers

URL Source: https://keras.io/api/layers/core_layers/

Markdown Content:
Core layers
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

►[Keras 3 API documentation](https://keras.io/api/) / [Layers API](https://keras.io/api/layers/) / Core layers 

Core layers
===========

### [Input object](https://keras.io/api/layers/core_layers/input/)

*   [Input function](https://keras.io/api/layers/core_layers/input/#input-function)

### [InputSpec object](https://keras.io/api/layers/core_layers/input_spec/)

*   [InputSpec class](https://keras.io/api/layers/core_layers/input_spec/#inputspec-class)

### [Dense layer](https://keras.io/api/layers/core_layers/dense/)

*   [Dense class](https://keras.io/api/layers/core_layers/dense/#dense-class)

### [EinsumDense layer](https://keras.io/api/layers/core_layers/einsum_dense/)

*   [EinsumDense class](https://keras.io/api/layers/core_layers/einsum_dense/#einsumdense-class)

### [Activation layer](https://keras.io/api/layers/core_layers/activation/)

*   [Activation class](https://keras.io/api/layers/core_layers/activation/#activation-class)

### [Embedding layer](https://keras.io/api/layers/core_layers/embedding/)

*   [Embedding class](https://keras.io/api/layers/core_layers/embedding/#embedding-class)
*   [ReversibleEmbedding class](https://keras.io/api/layers/core_layers/embedding/#reversibleembedding-class)

### [Masking layer](https://keras.io/api/layers/core_layers/masking/)

*   [Masking class](https://keras.io/api/layers/core_layers/masking/#masking-class)

### [Lambda layer](https://keras.io/api/layers/core_layers/lambda/)

*   [Lambda class](https://keras.io/api/layers/core_layers/lambda/#lambda-class)

### [Identity layer](https://keras.io/api/layers/core_layers/identity/)

*   [Identity class](https://keras.io/api/layers/core_layers/identity/#identity-class)

[Core layers](https://keras.io/api/layers/core_layers/#core-layers)

[Input object](https://keras.io/api/layers/core_layers/#input-object)

[InputSpec object](https://keras.io/api/layers/core_layers/#inputspec-object)

[Dense layer](https://keras.io/api/layers/core_layers/#dense-layer)

[EinsumDense layer](https://keras.io/api/layers/core_layers/#einsumdense-layer)

[Activation layer](https://keras.io/api/layers/core_layers/#activation-layer)

[Embedding layer](https://keras.io/api/layers/core_layers/#embedding-layer)

[Masking layer](https://keras.io/api/layers/core_layers/#masking-layer)

[Lambda layer](https://keras.io/api/layers/core_layers/#lambda-layer)

[Identity layer](https://keras.io/api/layers/core_layers/#identity-layer)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
