# Source: https://keras.io/api/optimizers/sgd

Title: Keras documentation: SGD

URL Source: https://keras.io/api/optimizers/sgd

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/optimizers/sgd.py#L6)

### `SGD` class

```
keras.optimizers.SGD(
    learning_rate=0.01,
    momentum=0.0,
    nesterov=False,
    weight_decay=None,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="SGD",
    **kwargs
)
```

Gradient descent (with momentum) optimizer.

Update rule for parameter `w` with gradient `g` when `momentum` is 0:

```
w = w - learning_rate * g
```

Update rule when `momentum` is larger than 0:

```
velocity = momentum * velocity - learning_rate * g
w = w + velocity
```

When `nesterov=True`, this rule becomes:

```
velocity = momentum * velocity - learning_rate * g
w = w + momentum * velocity - learning_rate * g
```

**Arguments**

*   **learning_rate**: A float, a [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class) instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.01`.
*   **momentum**: float hyperparameter >= 0 that accelerates gradient descent in the relevant direction and dampens oscillations. 0 is vanilla gradient descent. Defaults to `0.0`.
*   **nesterov**: boolean. Whether to apply Nesterov momentum. Defaults to `False`.
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

**Guides and examples using `SGD`**

*   [How to use Keras with NNX backend](https://keras.io/guides/keras_nnx_guide/)
*   [Image Classification](https://keras.io/keras_hub/guides/classification_with_keras_hub/)
*   [Semantic Segmentation](https://keras.io/keras_hub/guides/semantic_segmentation_deeplab_v3/)
*   [Few-Shot learning with Reptile](https://keras.io/examples/vision/reptile/)
*   [Monocular depth estimation](https://keras.io/examples/vision/depth_estimation/)
*   [Self-supervised contrastive learning with SimSiam](https://keras.io/examples/vision/simsiam/)
*   [Image Classification using BigTransfer (BiT)](https://keras.io/examples/vision/bit/)
*   [Masked image modeling with Autoencoders](https://keras.io/examples/vision/masked_image_modeling/)

* * *
