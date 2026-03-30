# Source: https://keras.io/api/layers/preprocessing_layers/

Title: Keras documentation: Preprocessing layers

URL Source: https://keras.io/api/layers/preprocessing_layers/

Markdown Content:
Preprocessing layers
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

►[Keras 3 API documentation](https://keras.io/api/) / [Layers API](https://keras.io/api/layers/) / Preprocessing layers 

Preprocessing layers
====================

### [Text preprocessing](https://keras.io/api/layers/preprocessing_layers/text/)

*   [TextVectorization layer](https://keras.io/api/layers/preprocessing_layers/text/text_vectorization)

### [Numerical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/numerical/)

*   [Normalization layer](https://keras.io/api/layers/preprocessing_layers/numerical/normalization)
*   [Spectral Normalization layer](https://keras.io/api/layers/preprocessing_layers/numerical/spectral_normalization)
*   [Discretization layer](https://keras.io/api/layers/preprocessing_layers/numerical/discretization)

### [Categorical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/categorical/)

*   [CategoryEncoding layer](https://keras.io/api/layers/preprocessing_layers/categorical/category_encoding)
*   [Hashing layer](https://keras.io/api/layers/preprocessing_layers/categorical/hashing)
*   [HashedCrossing layer](https://keras.io/api/layers/preprocessing_layers/categorical/hashed_crossing)
*   [StringLookup layer](https://keras.io/api/layers/preprocessing_layers/categorical/string_lookup)
*   [IntegerLookup layer](https://keras.io/api/layers/preprocessing_layers/categorical/integer_lookup)

### [Image preprocessing layers](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/)

*   [Resizing layer](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/resizing)
*   [Rescaling layer](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/rescaling)
*   [CenterCrop layer](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/center_crop)
*   [AutoContrast layer](https://keras.io/api/layers/preprocessing_layers/image_preprocessing/auto_constrast)

### [Image augmentation layers](https://keras.io/api/layers/preprocessing_layers/image_augmentation/)

*   [AugMix layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/aug_mix)
*   [CutMix layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/cut_mix)
*   [Equalization layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/equalization)
*   [MaxNumBoundingBoxes layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/max_num_bounding_boxes)
*   [MixUp layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/mix_up)
*   [Pipeline layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/pipeline)
*   [RandAugment layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/rand_augment)
*   [RandomBrightness layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_brightness)
*   [RandomColorDegeneration layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_degeneration)
*   [RandomColorJitter layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_color_jitter)
*   [RandomContrast layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_contrast)
*   [RandomCrop layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_crop)
*   [RandomElasticTransform layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_elastic_transform)
*   [RandomErasing layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_erasing)
*   [RandomFlip layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_flip)
*   [RandomGaussianBlur layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_gaussian_blur)
*   [RandomGrayscale layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_grayscale)
*   [RandomHue layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_hue)
*   [RandomInvert layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_invert)
*   [RandomPerspective layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_perspective)
*   [RandomPosterization layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_posterization)
*   [RandomRotation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_rotation)
*   [RandomSaturation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_saturation)
*   [RandomSharpness layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_sharpness)
*   [RandomShear layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_shear)
*   [RandomTranslation layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_translation)
*   [RandomZoom layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/random_zoom)
*   [Solarization layer](https://keras.io/api/layers/preprocessing_layers/image_augmentation/solarization)

### [Audio preprocessing layers](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/)

*   [MelSpectrogram layer](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/mel_spectrogram)
*   [STFTSpectrogram layer](https://keras.io/api/layers/preprocessing_layers/audio_preprocessing/stft_spectrogram)

[Preprocessing layers](https://keras.io/api/layers/preprocessing_layers/#preprocessing-layers)

[Text preprocessing](https://keras.io/api/layers/preprocessing_layers/#text-preprocessing)

[Numerical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/#numerical-features-preprocessing-layers)

[Categorical features preprocessing layers](https://keras.io/api/layers/preprocessing_layers/#categorical-features-preprocessing-layers)

[Image preprocessing layers](https://keras.io/api/layers/preprocessing_layers/#image-preprocessing-layers)

[Image augmentation layers](https://keras.io/api/layers/preprocessing_layers/#image-augmentation-layers)

[Audio preprocessing layers](https://keras.io/api/layers/preprocessing_layers/#audio-preprocessing-layers)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
