# Source: https://keras.io/api/optimizers/muon

Title: Keras documentation: Muon

URL Source: https://keras.io/api/optimizers/muon

Markdown Content:
[[source]](https://github.com/keras-team/keras/tree/v3.13.2/keras/src/optimizers/muon.py#L8)

### `Muon` class

```
keras.optimizers.Muon(
    learning_rate=0.001,
    adam_beta_1=0.9,
    adam_beta_2=0.999,
    adam_weight_decay=0.004,
    epsilon=1e-07,
    weight_decay=0.004,
    clipnorm=None,
    clipvalue=None,
    global_clipnorm=None,
    use_ema=False,
    ema_momentum=0.99,
    ema_overwrite_frequency=None,
    loss_scale_factor=None,
    gradient_accumulation_steps=None,
    name="muon",
    exclude_layers=None,
    exclude_embeddings=True,
    muon_a=3.4445,
    muon_b=-4.775,
    muon_c=2.0315,
    adam_lr_ratio=1,
    momentum=0.95,
    ns_steps=5,
    nesterov=True,
    rms_rate=0.2,
    **kwargs
)
```

Optimizer that implements the Muon algorithm.

Note that this optimizer should not be used in the following layers:

1.   Embedding layer
2.   Final output fully connected layer
3.   Any {0,1}-D variables

These should all be optimized using AdamW.

The Muon optimizer can use both the Muon update step or the AdamW update step based on the following:

*   For any variable that isn't 2D, the AdamW step will be used. This is not configurable.
*   If the argument `exclude_embeddings` (defaults to `True`) is set to `True`, the AdamW step will be used.
*   For any variablewith a name that matches an expression listed in the argument `exclude_layers` (a list), the AdamW step will be used.
*   Any other variable uses the Muon step.

Typically, you only need to pass the name of your densely-connected output layer to `exclude_layers`, e.g. `exclude_layers=["output_dense"]`.

**References**

*   [Original implementation](https://github.com/KellerJordan/Muon) - [Liu et al, 2025](https://arxiv.org/abs/2502.16982)

**Arguments**

*   **learning_rate**: A float, [`keras.optimizers.schedules.LearningRateSchedule`](https://keras.io/api/optimizers/learning_rate_schedules/learning_rate_schedule#learningrateschedule-class) instance, or a callable that takes no arguments and returns the actual value to use. The learning rate. Defaults to `0.001`.
*   **adam_beta_1**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 1st moment estimates. Defaults to `0.9`.
*   **adam_beta_2**: A float value or a constant float tensor, or a callable that takes no arguments and returns the actual value to use. The exponential decay rate for the 2nd moment estimates. Defaults to `0.999`.
*   **adam_weight_decay**: Float. If set, weight decay is applied when using the Adam optimizer.
*   **epsilon**: A small constant for numerical stability. This is "epsilon hat" in the Kingma and Ba paper (in the formula just before Section 2.1), not the epsilon in Algorithm 1 of the paper. It be used at Adamw.Defaults to `1e-7`.
*   **exclude_layers**: List of strings, keywords of layer names to exclude. All layers with keywords in their path will use adamw.
*   **exclude_embeddings**: Boolean value If True, embedding layers will use adamw.
*   **muon_a**: Float, parameter a of the muon algorithm. It is recommended to use the default value
*   **muon_b**: Float, parameter b of the muon algorithm. It is recommended to use the default value
*   **muon_c**: Float, parameter c of the muon algorithm. It is recommended to use the default value
*   **adam_lr_ratio**: Float, the ratio of the learning rate when using Adam to the main learning rate. It is recommended to set it to 1
*   **momentum**: Float, momentum used by internal SGD.
*   **ns_steps**: Integer, number of Newton-Schulz iterations to run.
*   **nesterov**: Boolean, whether to use Nesterov-style momentum {{base_optimizer_keyword_args}}
*   **rms_rate**: Float. A parameter from https://arxiv.org/abs/2502.16982 that can enhance the stability of Muon, allowing it to use the same learning rate and weight decay as Adam. Defaults to `0.2`. Set to `None` to disable this feature.

* * *
