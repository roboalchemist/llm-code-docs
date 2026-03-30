# Source: https://keras.io/api/models/

Title: Keras documentation: Models API

URL Source: https://keras.io/api/models/

Markdown Content:
►[Keras 3 API documentation](https://keras.io/api/) / Models API

There are three ways to create Keras models:

*   The [Sequential model](https://keras.io/guides/sequential_model), which is very straightforward (a simple list of layers), but is limited to single-input, single-output stacks of layers (as the name gives away).
*   The [Functional API](https://keras.io/guides/functional_api), which is an easy-to-use, fully-featured API that supports arbitrary model architectures. For most people and most use cases, this is what you should be using. This is the Keras "industry strength" model.
*   [Model subclassing](https://keras.io/guides/making_new_layers_and_models_via_subclassing), where you implement everything from scratch on your own. Use this if you have complex, out-of-the-box research use cases.

Models API overview
-------------------

### [The Model class](https://keras.io/api/models/model/)

*   [Model class](https://keras.io/api/models/model/#model-class)
*   [summary method](https://keras.io/api/models/model/#summary-method)
*   [get_layer method](https://keras.io/api/models/model/#get_layer-method)
*   [get_quantization_layer_structure method](https://keras.io/api/models/model/#get_quantization_layer_structure-method)
*   [get_state_tree method](https://keras.io/api/models/model/#get_state_tree-method)
*   [set_state_tree method](https://keras.io/api/models/model/#set_state_tree-method)
*   [quantize method](https://keras.io/api/models/model/#quantize-method)

### [The Sequential class](https://keras.io/api/models/sequential/)

*   [Sequential class](https://keras.io/api/models/sequential/#sequential-class)
*   [add method](https://keras.io/api/models/sequential/#add-method)
*   [pop method](https://keras.io/api/models/sequential/#pop-method)

### [Model training APIs](https://keras.io/api/models/model_training_apis/)

*   [compile method](https://keras.io/api/models/model_training_apis/#compile-method)
*   [fit method](https://keras.io/api/models/model_training_apis/#fit-method)
*   [evaluate method](https://keras.io/api/models/model_training_apis/#evaluate-method)
*   [predict method](https://keras.io/api/models/model_training_apis/#predict-method)
*   [train_on_batch method](https://keras.io/api/models/model_training_apis/#train_on_batch-method)
*   [test_on_batch method](https://keras.io/api/models/model_training_apis/#test_on_batch-method)
*   [predict_on_batch method](https://keras.io/api/models/model_training_apis/#predict_on_batch-method)

### [Saving & serialization](https://keras.io/api/models/model_saving_apis/)

*   [Whole model saving & loading](https://keras.io/api/models/model_saving_apis/model_saving_and_loading)
*   [Weights-only saving & loading](https://keras.io/api/models/model_saving_apis/weights_saving_and_loading)
*   [Model config serialization](https://keras.io/api/models/model_saving_apis/model_config_serialization)
*   [Model export for inference](https://keras.io/api/models/model_saving_apis/export)
*   [Serialization utilities](https://keras.io/api/models/model_saving_apis/serialization_utils)
*   [Keras weights file editor](https://keras.io/api/models/model_saving_apis/keras_file_editor)

### [Knowledge distillation](https://keras.io/api/models/distillation/)

*   [Distiller model](https://keras.io/api/models/distillation/distiller)
*   [Base distillation loss](https://keras.io/api/models/distillation/distillation_loss)
*   [Logits distillation loss](https://keras.io/api/models/distillation/logits_distillation)
*   [Feature distillation loss](https://keras.io/api/models/distillation/feature_distillation)
