# Source: https://keras.io/api/models/model_saving_apis/

Title: Keras documentation: Saving & serialization

URL Source: https://keras.io/api/models/model_saving_apis/

Markdown Content:
Saving & serialization
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[The Model class](https://keras.io/api/models/model/)[The Sequential class](https://keras.io/api/models/sequential/)[Model training APIs](https://keras.io/api/models/model_training_apis/)[Saving & serialization](https://keras.io/api/models/model_saving_apis/)[Knowledge distillation](https://keras.io/api/models/distillation/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[The Model class](https://keras.io/api/models/model/)[The Sequential class](https://keras.io/api/models/sequential/)[Model training APIs](https://keras.io/api/models/model_training_apis/)[Saving & serialization](https://keras.io/api/models/model_saving_apis/)[Knowledge distillation](https://keras.io/api/models/distillation/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Models API](https://keras.io/api/models/) / Saving & serialization 

Saving & serialization
======================

### [Whole model saving & loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/)

*   [save method](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#save-method)
*   [save_model function](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#save_model-function)
*   [load_model function](https://keras.io/api/models/model_saving_apis/model_saving_and_loading/#load_model-function)

### [Weights-only saving & loading](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/)

*   [save_weights method](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/#save_weights-method)
*   [load_weights method](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading/#load_weights-method)

### [Model config serialization](https://keras.io/api/models/model_saving_apis/model_config_serialization/)

*   [get_config method](https://keras.io/api/models/model_saving_apis/model_config_serialization/#get_config-method)
*   [from_config method](https://keras.io/api/models/model_saving_apis/model_config_serialization/#from_config-method)
*   [clone_model function](https://keras.io/api/models/model_saving_apis/model_config_serialization/#clone_model-function)
*   [model_from_json function](https://keras.io/api/models/model_saving_apis/model_config_serialization/#model_from_json-function)

### [Model export for inference](https://keras.io/api/models/model_saving_apis/export/)

*   [export method](https://keras.io/api/models/model_saving_apis/export/#export-method)
*   [ExportArchive class](https://keras.io/api/models/model_saving_apis/export/#exportarchive-class)
*   [add_endpoint method](https://keras.io/api/models/model_saving_apis/export/#add_endpoint-method)
*   [add_variable_collection method](https://keras.io/api/models/model_saving_apis/export/#add_variable_collection-method)
*   [track method](https://keras.io/api/models/model_saving_apis/export/#track-method)
*   [write_out method](https://keras.io/api/models/model_saving_apis/export/#write_out-method)

### [Serialization utilities](https://keras.io/api/models/model_saving_apis/serialization_utils/)

*   [serialize_keras_object function](https://keras.io/api/models/model_saving_apis/serialization_utils/#serialize_keras_object-function)
*   [deserialize_keras_object function](https://keras.io/api/models/model_saving_apis/serialization_utils/#deserialize_keras_object-function)
*   [custom_object_scope class](https://keras.io/api/models/model_saving_apis/serialization_utils/#customobjectscope-class)
*   [get_custom_objects function](https://keras.io/api/models/model_saving_apis/serialization_utils/#get_custom_objects-function)
*   [register_keras_serializable function](https://keras.io/api/models/model_saving_apis/serialization_utils/#register_keras_serializable-function)

### [Keras weights file editor](https://keras.io/api/models/model_saving_apis/keras_file_editor/)

*   [KerasFileEditor class](https://keras.io/api/models/model_saving_apis/keras_file_editor/#kerasfileeditor-class)
*   [summary method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#summary-method)
*   [compare method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#compare-method)
*   [save method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#save-method)
*   [rename_object method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#rename_object-method)
*   [delete_object method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#delete_object-method)
*   [add_object method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#add_object-method)
*   [delete_weight method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#delete_weight-method)
*   [add_weights method](https://keras.io/api/models/model_saving_apis/keras_file_editor/#add_weights-method)

[Saving & serialization](https://keras.io/api/models/model_saving_apis/#saving-amp-serialization)

[Whole model saving & loading](https://keras.io/api/models/model_saving_apis/#whole-model-saving-amp-loading)

[Weights-only saving & loading](https://keras.io/api/models/model_saving_apis/#weightsonly-saving-amp-loading)

[Model config serialization](https://keras.io/api/models/model_saving_apis/#model-config-serialization)

[Model export for inference](https://keras.io/api/models/model_saving_apis/#model-export-for-inference)

[Serialization utilities](https://keras.io/api/models/model_saving_apis/#serialization-utilities)

[Keras weights file editor](https://keras.io/api/models/model_saving_apis/#keras-weights-file-editor)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
