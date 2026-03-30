# Source: https://keras.io/api/optimizers/adamw

Title: Keras documentation: AdamW

URL Source: https://keras.io/api/optimizers/adamw

Published Time: Thu, 19 Feb 2026 23:04:40 GMT

Markdown Content:
AdamW
===============

 None 

[![Image 1](https://keras.io/img/k-logo.png)](https://keras.io/)

[Getting started](https://keras.io/getting_started/)[Developer guides](https://keras.io/guides/)[Code examples](https://keras.io/examples/)[Keras 3 API documentation](https://keras.io/api/)[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[SGD](https://keras.io/api/optimizers/sgd/)[RMSprop](https://keras.io/api/optimizers/rmsprop/)[Adam](https://keras.io/api/optimizers/adam/)[AdamW](https://keras.io/api/optimizers/adamw/)[Adadelta](https://keras.io/api/optimizers/adadelta/)[Adagrad](https://keras.io/api/optimizers/adagrad/)[Adamax](https://keras.io/api/optimizers/adamax/)[Adafactor](https://keras.io/api/optimizers/adafactor/)[Nadam](https://keras.io/api/optimizers/Nadam/)[Ftrl](https://keras.io/api/optimizers/ftrl/)[Lion](https://keras.io/api/optimizers/lion/)[Lamb](https://keras.io/api/optimizers/lamb/)[Loss Scale Optimizer](https://keras.io/api/optimizers/loss_scale_optimizer/)[Learning rate schedules API](https://keras.io/api/optimizers/learning_rate_schedules/)[Muon](https://keras.io/api/optimizers/muon/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)[Keras 2 API documentation](https://keras.io/2/api/)[KerasTuner: Hyperparam Tuning](https://keras.io/keras_tuner/)[KerasHub: Pretrained Models](https://keras.io/keras_hub/)[KerasRS](https://keras.io/keras_rs/)

[![Image 2: keras.io logo](https://keras.io/img/logo.png)](https://keras.io/)

*   [Get started](https://keras.io/getting_started/)
*   [Guides](https://keras.io/guides/)
*   [API](https://keras.io/api/)
*   [Examples](https://keras.io/examples/)
*   [Keras Hub](https://keras.io/keras_hub/)
*   [Keras RS](https://keras.io/keras_rs/)
*   [Keras Tuner](https://keras.io/keras_tuner/)

[Keras 3 API documentation](https://keras.io/api/)

[Models API](https://keras.io/api/models/)[Layers API](https://keras.io/api/layers/)[Callbacks API](https://keras.io/api/callbacks/)[Ops API](https://keras.io/api/ops/)[Optimizers](https://keras.io/api/optimizers/)[SGD](https://keras.io/api/optimizers/sgd/)[RMSprop](https://keras.io/api/optimizers/rmsprop/)[Adam](https://keras.io/api/optimizers/adam/)[AdamW](https://keras.io/api/optimizers/adamw/)[Adadelta](https://keras.io/api/optimizers/adadelta/)[Adagrad](https://keras.io/api/optimizers/adagrad/)[Adamax](https://keras.io/api/optimizers/adamax/)[Adafactor](https://keras.io/api/optimizers/adafactor/)[Nadam](https://keras.io/api/optimizers/Nadam/)[Ftrl](https://keras.io/api/optimizers/ftrl/)[Lion](https://keras.io/api/optimizers/lion/)[Lamb](https://keras.io/api/optimizers/lamb/)[Loss Scale Optimizer](https://keras.io/api/optimizers/loss_scale_optimizer/)[Learning rate schedules API](https://keras.io/api/optimizers/learning_rate_schedules/)[Muon](https://keras.io/api/optimizers/muon/)[Metrics](https://keras.io/api/metrics/)[Losses](https://keras.io/api/losses/)[Data loading](https://keras.io/api/data_loading/)[Tree API](https://keras.io/api/tree/)[Built-in small datasets](https://keras.io/api/datasets/)[Keras Applications](https://keras.io/api/applications/)[Mixed precision](https://keras.io/api/mixed_precision/)[Multi-device distribution](https://keras.io/api/distribution/)[RNG API](https://keras.io/api/random/)[Quantizers](https://keras.io/api/quantizers/)[Scope](https://keras.io/api/scope/)[Rematerialization](https://keras.io/api/rematerialization/)[Utilities](https://keras.io/api/utils/)

[Keras 2 API documentation](https://keras.io/2/api/)

►[Keras 3 API documentation](https://keras.io/api/) / [Optimizers](https://keras.io/api/optimizers/) / AdamW 

AdamW
=====

[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/optimizers/adamw.py#L6)

### `AdamW` class

```
keras.optimizers.AdamW(
    learning_rate=0.001,
    weight_decay=0.004,
    beta_1=0.9,
    beta_2=0.999,
    epsilon=1e-07,
    amsgrad=False,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="adamw",
    **kwargs
)
```

Optimizer that implements the AdamW algorithm.

AdamW optimization is a stochastic gradient descent method that is based on adaptive estimation of first-order and second-order moments with an added method to decay weights per the techniques discussed in the paper, 'Decoupled Weight Decay Regularization' by [Loshchilov, Hutter et al., 2019](https://arxiv.org/abs/1711.05101).

According to [Kingma et al., 2014](http://arxiv.org/abs/1412.6980), the underlying Adam method is "_computationally efficient, has little memory requirement, invariant to diagonal rescaling of gradients, and is well suited for problems that are large in terms of data/parameters_".

**Arguments**

*   **learning_rate**: A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class) instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`.
*   **beta_1**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 1st moment estimates. Defaults to `0.9`.
*   **beta_2**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 2nd moment estimates. Defaults to `0.999`.
*   **epsilon**: A small constant for numerical stability. This epsilon is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1), not the epsilon in Algorithm 1 of the paper. Defaults to 1e-7.
*   **amsgrad**: Boolean. Whether to apply AMSGrad variant of this algorithm from the paper "On the Convergence of Adam and beyond". Defaults to `False`.
*   **name**: String. The name to use for momentum accumulator weights created by the optimizer.
*   **weight_decay**: Float. If set, weight decay is applied.
*   **clipnorm**: Float. If set, the gradient of each weight is individually clipped so that its norm is no higher than this value.
*   **clipvalue**: Float. If set, the gradient of each weight is clipped to be no higher than this value.
*   **global_clipnorm**: Float. If set, the gradient of all weights is clipped so that their global norm is no higher than this value.
*   **use_ema**: Boolean, defaults to `False`. If `True`, exponential moving average (EMA) is applied. EMA consists of computing an exponential moving average of the weights of the model (as the weight values change after each training batch), and periodically overwriting the weights with their moving average.
*   **ema_momentum**: Float, defaults to 0.99. Only used if `use_ema=True`. This is the momentum to use when computing the EMA of the model's weights: 
```
new_average = ema_momentum * old_average + (1 - ema_momentum) *
  current_variable_value
```
.
*   **ema_overwrite_frequency**: Int or None, defaults to None. Only used if `use_ema=True`. Every `ema_overwrite_frequency` steps of iterations, we overwrite the model variable by its moving average. If None, the optimizer does not overwrite model variables in the middle of training, and you need to explicitly overwrite the variables at the end of training by calling `optimizer.finalize_variable_values()` (which updates the model variables in-place). When using the built-in `fit()` training loop, this happens automatically after the last epoch, and you don't need to do anything.
*   **loss_scale_factor**: Float or `None`. If a float, the scale factor will be multiplied the loss before computing gradients, and the inverse of the scale factor will be multiplied by the gradients before updating variables. Useful for preventing underflow during mixed precision training. Alternately, [`keras.optimizers.LossScaleOptimizer`](https://keras.io/api/optimizers/loss_scale_optimizer#lossscaleoptimizer-class) will automatically set a loss scale factor.
*   **gradient_accumulation_steps**: Int or `None`. If an int, model & optimizer variables will not be updated at every step; instead they will be updated every `gradient_accumulation_steps` steps, using the average value of the gradients since the last update. This is known as "gradient accumulation". This can be useful when your batch size is very small, in order to reduce gradient noise at each update step. EMA frequency will look at "accumulated" iterations value (optimizer steps // gradient_accumulation_steps). Learning rate schedules will look at "real" iterations value (optimizer steps).

**References**

*   [Loshchilov et al., 2019](https://arxiv.org/abs/1711.05101)
*   [Kingma et al., 2014](http://arxiv.org/abs/1412.6980) for `adam`
*   [Reddi et al., 2018](https://openreview.net/pdf?id=ryQu7f-RZ) for `amsgrad`.

**Guides and examples using `AdamW`**

*   [Pretraining a Transformer from scratch](https://keras.io/keras_hub/guides/transformer_pretraining/)
*   [Image classification with Vision Transformer](https://keras.io/examples/vision/image_classification_with_vision_transformer/)
*   [Image classification with modern MLP models](https://keras.io/examples/vision/mlp_image_classification/)
*   [Compact Convolutional Transformers](https://keras.io/examples/vision/cct/)
*   [Image classification with ConvMixer](https://keras.io/examples/vision/convmixer/)
*   [Image classification with EANet (External Attention Transformer)](https://keras.io/examples/vision/eanet/)
*   [Image classification with Swin Transformers](https://keras.io/examples/vision/swin_transformers/)
*   [Train a Vision Transformer on small datasets](https://keras.io/examples/vision/vit_small_ds/)

* * *

[AdamW](https://keras.io/api/optimizers/adamw#adamw)

[`AdamW` class](https://keras.io/api/optimizers/adamw#adamw-class)

[Terms](https://policies.google.com/terms)

|

[Privacy](https://policies.google.com/privacy)
