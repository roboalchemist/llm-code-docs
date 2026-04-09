::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-bars}
:::
::::

:::::: header-article-items__end
::::: header-article-item
:::: article-header-buttons
[[
]{.btn__icon-container}](https://github.com/ml-explore/mlx "Source repository"){.btn
.btn-sm .btn-source-repository-button target="_blank"
bs-placement="bottom" bs-toggle="tooltip"}

::: {.dropdown .dropdown-download-buttons}

- [[ ]{.btn__icon-container}
  [.rst]{.btn__text-container}](../_sources/python/optimizers.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}

[]{.fa-solid .fa-list}
::::
:::::
::::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Optimizers

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Saving and Loading](#saving-and-loading){.reference .internal
  .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::: {#optimizers .section}
[]{#id1}

# Optimizers[\#](#optimizers "Link to this heading"){.headerlink}

The optimizers in MLX can be used both with [`mlx.nn`{.xref .py .py-mod
.docutils .literal .notranslate}]{.pre} but also with pure
[`mlx.core`{.xref .py .py-mod .docutils .literal .notranslate}]{.pre}
functions. A typical example involves calling
[[`Optimizer.update()`{.xref .py .py-meth .docutils .literal
.notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update "mlx.optimizers.Optimizer.update"){.reference
.internal} to update a model's parameters based on the loss gradients
and subsequently calling [[`mlx.core.eval()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.eval.html#mlx.core.eval "mlx.core.eval"){.reference
.internal} to evaluate both the model's parameters and the **optimizer
state**.

:::: {.highlight-python .notranslate}
::: highlight
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
:::
::::

::::::: {#saving-and-loading .section}
## Saving and Loading[\#](#saving-and-loading "Link to this heading"){.headerlink}

To serialize an optimizer, save its state. To load an optimizer, load
and set the saved state. Here's a simple example:

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    from mlx.utils import tree_flatten, tree_unflatten
    import mlx.optimizers as optim

    optimizer = optim.Adam(learning_rate=1e-2)

    # Perform some updates with the optimizer
    model = {"w" : mx.zeros((5, 5))}
    grads = {"w" : mx.ones((5, 5))}
    optimizer.update(model, grads)

    # Save the state
    state = tree_flatten(optimizer.state, destination={})
    mx.save_safetensors("optimizer.safetensors", state)

    # Later on, for example when loading from a checkpoint,
    # recreate the optimizer and load the state
    optimizer = optim.Adam(learning_rate=1e-2)

    state = tree_unflatten(mx.load("optimizer.safetensors"))
    optimizer.state = state
:::
::::

Note, not every optimizer configuation parameter is saved in the state.
For example, for Adam the learning rate is saved but the
[`betas`{.docutils .literal .notranslate}]{.pre} and [`eps`{.docutils
.literal .notranslate}]{.pre} parameters are not. A good rule of thumb
is if the parameter can be scheduled then it will be included in the
optimizer state.

::: {.toctree-wrapper .compound}
- [Optimizer](optimizers/optimizer.html){.reference .internal}
  - [[`Optimizer`{.docutils .literal
    .notranslate}]{.pre}](optimizers/optimizer.html#mlx.optimizers.Optimizer){.reference
    .internal}
  - [mlx.optimizers.Optimizer.state](optimizers/_autosummary/mlx.optimizers.Optimizer.state.html){.reference
    .internal}
    - [[`Optimizer.state`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Optimizer.state.html#mlx.optimizers.Optimizer.state){.reference
      .internal}
  - [mlx.optimizers.Optimizer.apply_gradients](optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html){.reference
    .internal}
    - [[`Optimizer.apply_gradients()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html#mlx.optimizers.Optimizer.apply_gradients){.reference
      .internal}
  - [mlx.optimizers.Optimizer.init](optimizers/_autosummary/mlx.optimizers.Optimizer.init.html){.reference
    .internal}
    - [[`Optimizer.init()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Optimizer.init.html#mlx.optimizers.Optimizer.init){.reference
      .internal}
  - [mlx.optimizers.Optimizer.update](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html){.reference
    .internal}
    - [[`Optimizer.update()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update){.reference
      .internal}
- [Common Optimizers](optimizers/common_optimizers.html){.reference
  .internal}
  - [mlx.optimizers.SGD](optimizers/_autosummary/mlx.optimizers.SGD.html){.reference
    .internal}
    - [[`SGD`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.SGD.html#mlx.optimizers.SGD){.reference
      .internal}
  - [mlx.optimizers.RMSprop](optimizers/_autosummary/mlx.optimizers.RMSprop.html){.reference
    .internal}
    - [[`RMSprop`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.RMSprop.html#mlx.optimizers.RMSprop){.reference
      .internal}
  - [mlx.optimizers.Adagrad](optimizers/_autosummary/mlx.optimizers.Adagrad.html){.reference
    .internal}
    - [[`Adagrad`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Adagrad.html#mlx.optimizers.Adagrad){.reference
      .internal}
  - [mlx.optimizers.Adafactor](optimizers/_autosummary/mlx.optimizers.Adafactor.html){.reference
    .internal}
    - [[`Adafactor`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Adafactor.html#mlx.optimizers.Adafactor){.reference
      .internal}
  - [mlx.optimizers.AdaDelta](optimizers/_autosummary/mlx.optimizers.AdaDelta.html){.reference
    .internal}
    - [[`AdaDelta`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.AdaDelta.html#mlx.optimizers.AdaDelta){.reference
      .internal}
  - [mlx.optimizers.Adam](optimizers/_autosummary/mlx.optimizers.Adam.html){.reference
    .internal}
    - [[`Adam`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Adam.html#mlx.optimizers.Adam){.reference
      .internal}
  - [mlx.optimizers.AdamW](optimizers/_autosummary/mlx.optimizers.AdamW.html){.reference
    .internal}
    - [[`AdamW`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.AdamW.html#mlx.optimizers.AdamW){.reference
      .internal}
  - [mlx.optimizers.Adamax](optimizers/_autosummary/mlx.optimizers.Adamax.html){.reference
    .internal}
    - [[`Adamax`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Adamax.html#mlx.optimizers.Adamax){.reference
      .internal}
  - [mlx.optimizers.Lion](optimizers/_autosummary/mlx.optimizers.Lion.html){.reference
    .internal}
    - [[`Lion`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Lion.html#mlx.optimizers.Lion){.reference
      .internal}
  - [mlx.optimizers.MultiOptimizer](optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html){.reference
    .internal}
    - [[`MultiOptimizer`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.MultiOptimizer.html#mlx.optimizers.MultiOptimizer){.reference
      .internal}
  - [mlx.optimizers.Muon](optimizers/_autosummary/mlx.optimizers.Muon.html){.reference
    .internal}
    - [[`Muon`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.Muon.html#mlx.optimizers.Muon){.reference
      .internal}
- [Schedulers](optimizers/schedulers.html){.reference .internal}
  - [mlx.optimizers.cosine_decay](optimizers/_autosummary/mlx.optimizers.cosine_decay.html){.reference
    .internal}
    - [[`cosine_decay()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.cosine_decay.html#mlx.optimizers.cosine_decay){.reference
      .internal}
  - [mlx.optimizers.exponential_decay](optimizers/_autosummary/mlx.optimizers.exponential_decay.html){.reference
    .internal}
    - [[`exponential_decay()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.exponential_decay.html#mlx.optimizers.exponential_decay){.reference
      .internal}
  - [mlx.optimizers.join_schedules](optimizers/_autosummary/mlx.optimizers.join_schedules.html){.reference
    .internal}
    - [[`join_schedules()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.join_schedules.html#mlx.optimizers.join_schedules){.reference
      .internal}
  - [mlx.optimizers.linear_schedule](optimizers/_autosummary/mlx.optimizers.linear_schedule.html){.reference
    .internal}
    - [[`linear_schedule()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.linear_schedule.html#mlx.optimizers.linear_schedule){.reference
      .internal}
  - [mlx.optimizers.step_decay](optimizers/_autosummary/mlx.optimizers.step_decay.html){.reference
    .internal}
    - [[`step_decay()`{.docutils .literal
      .notranslate}]{.pre}](optimizers/_autosummary/mlx.optimizers.step_decay.html#mlx.optimizers.step_decay){.reference
      .internal}
:::

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------
  [[`clip_grad_norm`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.optimizers.clip_grad_norm.html#mlx.optimizers.clip_grad_norm "mlx.optimizers.clip_grad_norm"){.reference .internal}(grads, max_norm)   Clips the global norm of the gradients.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -----------------------------------------
:::
:::::::
::::::::::

::::: prev-next-area
[](nn/_autosummary/mlx.nn.layers.distributed.shard_inplace.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.nn.layers.distributed.shard_inplace
:::

[](optimizers/optimizer.html "next page"){.right-next}

::: prev-next-info
next

Optimizer
:::
:::::
:::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Saving and Loading](#saving-and-loading){.reference .internal
  .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::

::::::: {.bd-footer-content__inner .container}
::: footer-item
By MLX Contributors
:::

::: footer-item
© Copyright 2023, Apple.\
:::

::: footer-item
:::

::: footer-item
:::
:::::::
:::::::::::::::::::::::::::::::::::::::
