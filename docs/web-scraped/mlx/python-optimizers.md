# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/python/optimizers.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Optimizers

## Contents

- [Saving and Loading](#saving-and-loading)

[]

# Optimizers[\#](#optimizers "Link to this heading")

The optimizers in MLX can be used both with [`mlx.nn`] but also with pure [`mlx.core`] functions. A typical example involves calling [[`Optimizer.update()`]](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update "mlx.optimizers.Optimizer.update") to update a model's parameters based on the loss gradients and subsequently calling [[`mlx.core.eval()`]](_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval") to evaluate both the model's parameters and the **optimizer state**.

    # Create a model
    model = MLP(num_layers, train_images.shape[-1], hidden_dim, num_classes)
    mx.eval(model.parameters())

    # Create the gradient function and the optimizer
    loss_and_grad_fn = nn.value_and_grad(model, loss_fn)
    optimizer = optim.SGD(learning_rate=learning_rate)

    for e in range(num_epochs):
        for X, y in batch_iterate(batch_size, train_images, train_labels):
            loss, grads = loss_and_grad_fn(model, X, y)

            # Update the model with the gradients. So far no computation has happened.
            optimizer.update(model, grads)

            # Compute the new parameters but also the optimizer state.
            mx.eval(model.parameters(), optimizer.state)

## Saving and Loading[\#](#saving-and-loading "Link to this heading")

To serialize an optimizer, save its state. To load an optimizer, load and set the saved state. Here's a simple example:

    import mlx.core as mx
    from mlx.utils import tree_flatten, tree_unflatten
    import mlx.optimizers as optim

    optimizer = optim.Adam(learning_rate=1e-2)

    # Perform some updates with the optimizer
    model = 
    grads = 
    optimizer.update(model, grads)

    # Save the state
    state = tree_flatten(optimizer.state, destination=)
    mx.save_safetensors("optimizer.safetensors", state)

    # Later on, for example when loading from a checkpoint,
    # recreate the optimizer and load the state
    optimizer = optim.Adam(learning_rate=1e-2)

    state = tree_unflatten(mx.load("optimizer.safetensors"))
    optimizer.state = state

Note, not every optimizer configuation parameter is saved in the state. For example, for Adam the learning rate is saved but the [`betas`] and [`eps`] parameters are not. A good rule of thumb is if the parameter can be scheduled then it will be included in the optimizer state.

- [Optimizer](optimizers/optimizer.html)
  - [[`Optimizer`]](optimizers/optimizer.html#mlx.optimizers.Optimizer)
  - [mlx.optimizers.Optimizer.state](optimizers/_autosummary/mlx.optimizers.Optimizer.state.html)
    - [[`Optimizer.state`]](optimizers/_autosummary/mlx.optimizers.Optimizer.state.html#mlx.optimizers.Optimizer.state)
  - [mlx.optimizers.Optimizer.apply_gradients](optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html)
    - [[`Optimizer.apply_gradients()`]](optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html#mlx.optimizers.Optimizer.apply_gradients)
  - [mlx.optimizers.Optimizer.init](optimizers/_autosummary/mlx.optimizers.Optimizer.init.html)
    - [[`Optimizer.init()`]](optimizers/_autosummary/mlx.optimizers.Optimizer.init.html#mlx.optimizers.Optimizer.init)
  - [mlx.optimizers.Optimizer.update](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html)
    - [[`Optimizer.update()`]](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update)
- [Common Optimizers](optimizers/common_optimizers.html)
  - [mlx.optimizers.SGD](optimizers/_autosummary/mlx.optimizers.SGD.html)
    - [[`SGD`]](optimizers/_autosummary/mlx.optimizers.SGD.html#mlx.optimizers.SGD)
  - [mlx.optimizers.RMSprop](optimizers/_autosummary/mlx.optimizers.RMSprop.html)
    - [[`RMSprop`]](optimizers/_autosummary/mlx.optimizers.RMSprop.html#mlx.optimizers.RMSprop)
  - [mlx.optimizers.Adagrad](optimizers/_autosummary/mlx.optimizers.Adagrad.html)
    - [[`Adagrad`]](optimizers/_autosummary/mlx.optimizers.Adagrad.html#mlx.optimizers.Adagrad)
  - [mlx.optimizers.Adafactor](optimizers/_autosummary/mlx.optimizers.Adafactor.html)
    - [[`Adafactor`]](optimizers/_autosummary/mlx.optimizers.Adafactor.html#mlx.optimizers.Adafactor)
  - [mlx.optimizers.AdaDelta](optimizers/_autosummary/mlx.optimizers.AdaDelta.html)
    - [[`AdaDelta`]](optimizers/_autosummary/mlx.optimizers.AdaDelta.html#mlx.optimizers.AdaDelta)
  - [mlx.optimizers.Adam](optimizers/_autosummary/mlx.optimizers.Adam.html)
    - [[`Adam`]](optimizers/_autosummary/mlx.optimizers.Adam.html#mlx.optimizers.Adam)
  - [mlx.optimizers.AdamW](optimizers/_autosummary/mlx.optimizers.AdamW.html)
    - [[`AdamW`]](optimizers/_autosummary/mlx.optimizers.AdamW.html#mlx.optimizers.AdamW)
  - [mlx.optimizers.Adamax](optimizers/_autosummary/mlx.optimizers.Adamax.html)
    - [[`Adamax`]](optimizers/_autosummary/mlx.optimizers.Adamax.html#mlx.optimizers.Adamax)
  - [mlx.optimizers.Lion](optimizers/_autosummary/mlx.optimizers.Lion.html)
    - [[`Lion`]](optimizers/_autosummary/mlx.optimizers.Lion.html#mlx.optimizers.Lion)
  - [mlx.optimizers.MultiOptimizer](optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html)
    - [[`MultiOptimizer`]](optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html#mlx.optimizers.MultiOptimizer)
  - [mlx.optimizers.Muon](optimizers/_autosummary/mlx.optimizers.Muon.html)
    - [[`Muon`]](optimizers/_autosummary/mlx.optimizers.Muon.html#mlx.optimizers.Muon)
- [Schedulers](optimizers/schedulers.html)
  - [mlx.optimizers.cosine_decay](optimizers/_autosummary/mlx.optimizers.cosine_decay.html)
    - [[`cosine_decay()`]](optimizers/_autosummary/mlx.optimizers.cosine_decay.html#mlx.optimizers.cosine_decay)
  - [mlx.optimizers.exponential_decay](optimizers/_autosummary/mlx.optimizers.exponential_decay.html)
    - [[`exponential_decay()`]](optimizers/_autosummary/mlx.optimizers.exponential_decay.html#mlx.optimizers.exponential_decay)
  - [mlx.optimizers.join_schedules](optimizers/_autosummary/mlx.optimizers.join_schedules.html)
    - [[`join_schedules()`]](optimizers/_autosummary/mlx.optimizers.join_schedules.html#mlx.optimizers.join_schedules)
  - [mlx.optimizers.linear_schedule](optimizers/_autosummary/mlx.optimizers.linear_schedule.html)
    - [[`linear_schedule()`]](optimizers/_autosummary/mlx.optimizers.linear_schedule.html#mlx.optimizers.linear_schedule)
  - [mlx.optimizers.step_decay](optimizers/_autosummary/mlx.optimizers.step_decay.html)
    - [[`step_decay()`]](optimizers/_autosummary/mlx.optimizers.step_decay.html#mlx.optimizers.step_decay)

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------
  [[`clip_grad_norm`]](_autosummary/mlx.optimizers.clip_grad_norm.html#mlx.optimizers.clip_grad_norm "mlx.optimizers.clip_grad_norm")(grads, max_norm)   Clips the global norm of the gradients.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------

[](nn/_autosummary/mlx.nn.init.he_uniform.html "previous page")

previous

mlx.nn.init.he_uniform

[](optimizers/optimizer.html "next page")

next

Optimizer

Contents

- [Saving and Loading](#saving-and-loading)

By MLX Contributors

© Copyright 2023, Apple.\