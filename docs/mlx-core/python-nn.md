:::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

::::::::::::::::::::::::::::::::::::::::::::: bd-content
:::::::::::::::::::::::::::::::::::::::: bd-article-container
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
  [.rst]{.btn__text-container}](../_sources/python/nn.rst "Download source file"){.btn
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
# Neural Networks

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Quick Start with Neural
  Networks](#quick-start-with-neural-networks){.reference .internal
  .nav-link}
- [The Module Class](#the-module-class){.reference .internal .nav-link}
  - [Parameters](#parameters){.reference .internal .nav-link}
  - [Updating the Parameters](#updating-the-parameters){.reference
    .internal .nav-link}
  - [Inspecting Modules](#inspecting-modules){.reference .internal
    .nav-link}
- [Value and Grad](#value-and-grad){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

::::::::::::::::::::::: {#neural-networks .section}
[]{#nn}

# Neural Networks[\#](#neural-networks "Link to this heading"){.headerlink}

Writing arbitrarily complex neural networks in MLX can be done using
only [[`mlx.core.array`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} and [[`mlx.core.value_and_grad()`{.xref .py .py-meth
.docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
.internal}. However, this requires the user to write again and again the
same simple neural network operations as well as handle all the
parameter state and initialization manually and explicitly.

The module [`mlx.nn`{.xref .py .py-mod .docutils .literal
.notranslate}]{.pre} solves this problem by providing an intuitive way
of composing neural network layers, initializing their parameters,
freezing them for finetuning and more.

::::: {#quick-start-with-neural-networks .section}
## Quick Start with Neural Networks[\#](#quick-start-with-neural-networks "Link to this heading"){.headerlink}

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx
    import mlx.nn as nn

    class MLP(nn.Module):
        def __init__(self, in_dims: int, out_dims: int):
            super().__init__()

            self.layers = [
                nn.Linear(in_dims, 128),
                nn.Linear(128, 128),
                nn.Linear(128, out_dims),
            ]

        def __call__(self, x):
            for i, l in enumerate(self.layers):
                x = mx.maximum(x, 0) if i > 0 else x
                x = l(x)
            return x

    # The model is created with all its parameters but nothing is initialized
    # yet because MLX is lazily evaluated
    mlp = MLP(2, 10)

    # We can access its parameters by calling mlp.parameters()
    params = mlp.parameters()
    print(params["layers"][0]["weight"].shape)

    # Printing a parameter will cause it to be evaluated and thus initialized
    print(params["layers"][0])

    # We can also force evaluate all parameters to initialize the model
    mx.eval(mlp.parameters())

    # A simple loss function.
    # NOTE: It doesn't matter how it uses the mlp model. It currently captures
    #       it from the local scope. It could be a positional argument or a
    #       keyword argument.
    def l2_loss(x, y):
        y_hat = mlp(x)
        return (y_hat - y).square().mean()

    # Calling `nn.value_and_grad` instead of `mx.value_and_grad` returns the
    # gradient with respect to `mlp.trainable_parameters()`
    loss_and_grad = nn.value_and_grad(mlp, l2_loss)
:::
::::
:::::

:::::::::::::: {#the-module-class .section}
[]{#module-class}

## The Module Class[\#](#the-module-class "Link to this heading"){.headerlink}

The workhorse of any neural network library is the [[`Module`{.xref .py
.py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} class. In MLX the [[`Module`{.xref .py .py-class .docutils
.literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} class is a container of [[`mlx.core.array`{.xref .py
.py-class .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} or [[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} instances. Its main function is to provide a way to
recursively **access** and **update** its parameters and those of its
submodules.

::: {#parameters .section}
### Parameters[\#](#parameters "Link to this heading"){.headerlink}

A parameter of a module is any public member of type
[[`mlx.core.array`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"){.reference
.internal} (its name should not start with [`_`{.docutils .literal
.notranslate}]{.pre}). It can be arbitrarily nested in other
[[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} instances or lists and dictionaries.

[[`Module.parameters()`{.xref .py .py-meth .docutils .literal
.notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.parameters.html#mlx.nn.Module.parameters "mlx.nn.Module.parameters"){.reference
.internal} can be used to extract a nested dictionary with all the
parameters of a module and its submodules.

A [[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} can also keep track of "frozen" parameters. See the
[[`Module.freeze()`{.xref .py .py-meth .docutils .literal
.notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.freeze.html#mlx.nn.Module.freeze "mlx.nn.Module.freeze"){.reference
.internal} method for more details. [[`mlx.nn.value_and_grad()`{.xref
.py .py-meth .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad "mlx.nn.value_and_grad"){.reference
.internal} the gradients returned will be with respect to these
trainable parameters.
:::

::: {#updating-the-parameters .section}
### Updating the Parameters[\#](#updating-the-parameters "Link to this heading"){.headerlink}

MLX modules allow accessing and updating individual parameters. However,
most times we need to update large subsets of a module's parameters.
This action is performed by [[`Module.update()`{.xref .py .py-meth
.docutils .literal
.notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.update.html#mlx.nn.Module.update "mlx.nn.Module.update"){.reference
.internal}.
:::

::::::::::: {#inspecting-modules .section}
### Inspecting Modules[\#](#inspecting-modules "Link to this heading"){.headerlink}

The simplest way to see the model architecture is to print it. Following
along with the above example, you can print the [`MLP`{.docutils
.literal .notranslate}]{.pre} with:

:::: {.highlight-python .notranslate}
::: highlight
    print(mlp)
:::
::::

This will display:

:::: {.highlight-shell .notranslate}
::: highlight
    MLP(
      (layers.0): Linear(input_dims=2, output_dims=128, bias=True)
      (layers.1): Linear(input_dims=128, output_dims=128, bias=True)
      (layers.2): Linear(input_dims=128, output_dims=10, bias=True)
    )
:::
::::

To get more detailed information on the arrays in a [[`Module`{.xref .py
.py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} you can use [[`mlx.utils.tree_map()`{.xref .py .py-func
.docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.utils.tree_map.html#mlx.utils.tree_map "mlx.utils.tree_map"){.reference
.internal} on the parameters. For example, to see the shapes of all the
parameters in a [[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} do:

:::: {.highlight-python .notranslate}
::: highlight
    from mlx.utils import tree_map
    shapes = tree_map(lambda p: p.shape, mlp.parameters())
:::
::::

As another example, you can count the number of parameters in a
[[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} with:

:::: {.highlight-python .notranslate}
::: highlight
    from mlx.utils import tree_flatten
    num_params = sum(v.size for _, v in tree_flatten(mlp.parameters()))
:::
::::
:::::::::::
::::::::::::::

::::::: {#value-and-grad .section}
## Value and Grad[\#](#value-and-grad "Link to this heading"){.headerlink}

Using a [[`Module`{.xref .py .py-class .docutils .literal
.notranslate}]{.pre}](nn/module.html#mlx.nn.Module "mlx.nn.Module"){.reference
.internal} does not preclude using MLX's high order function
transformations ([[`mlx.core.value_and_grad()`{.xref .py .py-meth
.docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
.internal}, [[`mlx.core.grad()`{.xref .py .py-meth .docutils .literal
.notranslate}]{.pre}](_autosummary/mlx.core.grad.html#mlx.core.grad "mlx.core.grad"){.reference
.internal}, etc.). However, these function transformations assume pure
functions, namely the parameters should be passed as an argument to the
function being transformed.

There is an easy pattern to achieve that with MLX modules

:::: {.highlight-python .notranslate}
::: highlight
    model = ...

    def f(params, other_inputs):
        model.update(params)  # <---- Necessary to make the model use the passed parameters
        return model(other_inputs)

    f(model.trainable_parameters(), mx.zeros((10,)))
:::
::::

However, [[`mlx.nn.value_and_grad()`{.xref .py .py-meth .docutils
.literal
.notranslate}]{.pre}](_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad "mlx.nn.value_and_grad"){.reference
.internal} provides precisely this pattern and only computes the
gradients with respect to the trainable parameters of the model.

In detail:

- it wraps the passed function with a function that calls
  [[`Module.update()`{.xref .py .py-meth .docutils .literal
  .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.update.html#mlx.nn.Module.update "mlx.nn.Module.update"){.reference
  .internal} to make sure the model is using the provided parameters.

- it calls [[`mlx.core.value_and_grad()`{.xref .py .py-meth .docutils
  .literal
  .notranslate}]{.pre}](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
  .internal} to transform the function into a function that also
  computes the gradients with respect to the passed parameters.

- it wraps the returned function with a function that passes the
  trainable parameters as the first argument to the function returned by
  [[`mlx.core.value_and_grad()`{.xref .py .py-meth .docutils .literal
  .notranslate}]{.pre}](_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad "mlx.core.value_and_grad"){.reference
  .internal}

::: pst-scrollable-table-container
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [[`value_and_grad`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad "mlx.nn.value_and_grad"){.reference .internal}(model, fn)                                             Transform the passed function [`fn`{.docutils .literal .notranslate}]{.pre} to a function that computes the gradients of [`fn`{.docutils .literal .notranslate}]{.pre} wrt the model\'s trainable parameters and also its value.
  [[`quantize`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.nn.quantize.html#mlx.nn.quantize "mlx.nn.quantize"){.reference .internal}(model\[, group_size, bits, mode, \...\])                                       Quantize the sub-modules of a module according to a predicate.
  [[`average_gradients`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.nn.average_gradients.html#mlx.nn.average_gradients "mlx.nn.average_gradients"){.reference .internal}(gradients\[, group, \...\])                Average the gradients across the distributed processes in the passed group.
  [[`fsdp_apply_gradients`{.xref .py .py-obj .docutils .literal .notranslate}]{.pre}](_autosummary/mlx.nn.fsdp_apply_gradients.html#mlx.nn.fsdp_apply_gradients "mlx.nn.fsdp_apply_gradients"){.reference .internal}(gradients, parameters, \...)   Perform a distributed optimizer step by sharding gradients and optimizer states across ranks.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::

::: {.toctree-wrapper .compound}
- [Module](nn/module.html){.reference .internal}
  - [[`Module`{.docutils .literal
    .notranslate}]{.pre}](nn/module.html#mlx.nn.Module){.reference
    .internal}
  - [mlx.nn.Module.training](nn/_autosummary/mlx.nn.Module.training.html){.reference
    .internal}
    - [[`Module.training`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.training.html#mlx.nn.Module.training){.reference
      .internal}
  - [mlx.nn.Module.state](nn/_autosummary/mlx.nn.Module.state.html){.reference
    .internal}
    - [[`Module.state`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.state.html#mlx.nn.Module.state){.reference
      .internal}
  - [mlx.nn.Module.apply](nn/_autosummary/mlx.nn.Module.apply.html){.reference
    .internal}
    - [[`Module.apply()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.apply.html#mlx.nn.Module.apply){.reference
      .internal}
  - [mlx.nn.Module.apply_to_modules](nn/_autosummary/mlx.nn.Module.apply_to_modules.html){.reference
    .internal}
    - [[`Module.apply_to_modules()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.apply_to_modules.html#mlx.nn.Module.apply_to_modules){.reference
      .internal}
  - [mlx.nn.Module.children](nn/_autosummary/mlx.nn.Module.children.html){.reference
    .internal}
    - [[`Module.children()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.children.html#mlx.nn.Module.children){.reference
      .internal}
  - [mlx.nn.Module.eval](nn/_autosummary/mlx.nn.Module.eval.html){.reference
    .internal}
    - [[`Module.eval()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.eval.html#mlx.nn.Module.eval){.reference
      .internal}
  - [mlx.nn.Module.filter_and_map](nn/_autosummary/mlx.nn.Module.filter_and_map.html){.reference
    .internal}
    - [[`Module.filter_and_map()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.filter_and_map.html#mlx.nn.Module.filter_and_map){.reference
      .internal}
  - [mlx.nn.Module.freeze](nn/_autosummary/mlx.nn.Module.freeze.html){.reference
    .internal}
    - [[`Module.freeze()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.freeze.html#mlx.nn.Module.freeze){.reference
      .internal}
  - [mlx.nn.Module.leaf_modules](nn/_autosummary/mlx.nn.Module.leaf_modules.html){.reference
    .internal}
    - [[`Module.leaf_modules()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.leaf_modules.html#mlx.nn.Module.leaf_modules){.reference
      .internal}
  - [mlx.nn.Module.load_weights](nn/_autosummary/mlx.nn.Module.load_weights.html){.reference
    .internal}
    - [[`Module.load_weights()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.load_weights.html#mlx.nn.Module.load_weights){.reference
      .internal}
  - [mlx.nn.Module.modules](nn/_autosummary/mlx.nn.Module.modules.html){.reference
    .internal}
    - [[`Module.modules()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.modules.html#mlx.nn.Module.modules){.reference
      .internal}
  - [mlx.nn.Module.named_modules](nn/_autosummary/mlx.nn.Module.named_modules.html){.reference
    .internal}
    - [[`Module.named_modules()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.named_modules.html#mlx.nn.Module.named_modules){.reference
      .internal}
  - [mlx.nn.Module.parameters](nn/_autosummary/mlx.nn.Module.parameters.html){.reference
    .internal}
    - [[`Module.parameters()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.parameters.html#mlx.nn.Module.parameters){.reference
      .internal}
  - [mlx.nn.Module.save_weights](nn/_autosummary/mlx.nn.Module.save_weights.html){.reference
    .internal}
    - [[`Module.save_weights()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.save_weights.html#mlx.nn.Module.save_weights){.reference
      .internal}
  - [mlx.nn.Module.set_dtype](nn/_autosummary/mlx.nn.Module.set_dtype.html){.reference
    .internal}
    - [[`Module.set_dtype()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.set_dtype.html#mlx.nn.Module.set_dtype){.reference
      .internal}
  - [mlx.nn.Module.train](nn/_autosummary/mlx.nn.Module.train.html){.reference
    .internal}
    - [[`Module.train()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.train.html#mlx.nn.Module.train){.reference
      .internal}
  - [mlx.nn.Module.trainable_parameters](nn/_autosummary/mlx.nn.Module.trainable_parameters.html){.reference
    .internal}
    - [[`Module.trainable_parameters()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.trainable_parameters.html#mlx.nn.Module.trainable_parameters){.reference
      .internal}
  - [mlx.nn.Module.unfreeze](nn/_autosummary/mlx.nn.Module.unfreeze.html){.reference
    .internal}
    - [[`Module.unfreeze()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.unfreeze.html#mlx.nn.Module.unfreeze){.reference
      .internal}
  - [mlx.nn.Module.update](nn/_autosummary/mlx.nn.Module.update.html){.reference
    .internal}
    - [[`Module.update()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.update.html#mlx.nn.Module.update){.reference
      .internal}
  - [mlx.nn.Module.update_modules](nn/_autosummary/mlx.nn.Module.update_modules.html){.reference
    .internal}
    - [[`Module.update_modules()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Module.update_modules.html#mlx.nn.Module.update_modules){.reference
      .internal}
- [Layers](nn/layers.html){.reference .internal}
  - [mlx.nn.ALiBi](nn/_autosummary/mlx.nn.ALiBi.html){.reference
    .internal}
    - [[`ALiBi`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ALiBi.html#mlx.nn.ALiBi){.reference
      .internal}
  - [mlx.nn.AllToShardedLinear](nn/_autosummary/mlx.nn.AllToShardedLinear.html){.reference
    .internal}
    - [[`AllToShardedLinear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.AllToShardedLinear.html#mlx.nn.AllToShardedLinear){.reference
      .internal}
  - [mlx.nn.AvgPool1d](nn/_autosummary/mlx.nn.AvgPool1d.html){.reference
    .internal}
    - [[`AvgPool1d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.AvgPool1d.html#mlx.nn.AvgPool1d){.reference
      .internal}
  - [mlx.nn.AvgPool2d](nn/_autosummary/mlx.nn.AvgPool2d.html){.reference
    .internal}
    - [[`AvgPool2d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.AvgPool2d.html#mlx.nn.AvgPool2d){.reference
      .internal}
  - [mlx.nn.AvgPool3d](nn/_autosummary/mlx.nn.AvgPool3d.html){.reference
    .internal}
    - [[`AvgPool3d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.AvgPool3d.html#mlx.nn.AvgPool3d){.reference
      .internal}
  - [mlx.nn.BatchNorm](nn/_autosummary/mlx.nn.BatchNorm.html){.reference
    .internal}
    - [[`BatchNorm`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.BatchNorm.html#mlx.nn.BatchNorm){.reference
      .internal}
  - [mlx.nn.CELU](nn/_autosummary/mlx.nn.CELU.html){.reference
    .internal}
    - [[`CELU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.CELU.html#mlx.nn.CELU){.reference
      .internal}
  - [mlx.nn.Conv1d](nn/_autosummary/mlx.nn.Conv1d.html){.reference
    .internal}
    - [[`Conv1d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Conv1d.html#mlx.nn.Conv1d){.reference
      .internal}
  - [mlx.nn.Conv2d](nn/_autosummary/mlx.nn.Conv2d.html){.reference
    .internal}
    - [[`Conv2d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Conv2d.html#mlx.nn.Conv2d){.reference
      .internal}
  - [mlx.nn.Conv3d](nn/_autosummary/mlx.nn.Conv3d.html){.reference
    .internal}
    - [[`Conv3d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Conv3d.html#mlx.nn.Conv3d){.reference
      .internal}
  - [mlx.nn.ConvTranspose1d](nn/_autosummary/mlx.nn.ConvTranspose1d.html){.reference
    .internal}
    - [[`ConvTranspose1d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ConvTranspose1d.html#mlx.nn.ConvTranspose1d){.reference
      .internal}
  - [mlx.nn.ConvTranspose2d](nn/_autosummary/mlx.nn.ConvTranspose2d.html){.reference
    .internal}
    - [[`ConvTranspose2d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ConvTranspose2d.html#mlx.nn.ConvTranspose2d){.reference
      .internal}
  - [mlx.nn.ConvTranspose3d](nn/_autosummary/mlx.nn.ConvTranspose3d.html){.reference
    .internal}
    - [[`ConvTranspose3d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ConvTranspose3d.html#mlx.nn.ConvTranspose3d){.reference
      .internal}
  - [mlx.nn.Dropout](nn/_autosummary/mlx.nn.Dropout.html){.reference
    .internal}
    - [[`Dropout`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Dropout.html#mlx.nn.Dropout){.reference
      .internal}
  - [mlx.nn.Dropout2d](nn/_autosummary/mlx.nn.Dropout2d.html){.reference
    .internal}
    - [[`Dropout2d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Dropout2d.html#mlx.nn.Dropout2d){.reference
      .internal}
  - [mlx.nn.Dropout3d](nn/_autosummary/mlx.nn.Dropout3d.html){.reference
    .internal}
    - [[`Dropout3d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Dropout3d.html#mlx.nn.Dropout3d){.reference
      .internal}
  - [mlx.nn.Embedding](nn/_autosummary/mlx.nn.Embedding.html){.reference
    .internal}
    - [[`Embedding`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Embedding.html#mlx.nn.Embedding){.reference
      .internal}
  - [mlx.nn.ELU](nn/_autosummary/mlx.nn.ELU.html){.reference .internal}
    - [[`ELU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ELU.html#mlx.nn.ELU){.reference
      .internal}
  - [mlx.nn.GELU](nn/_autosummary/mlx.nn.GELU.html){.reference
    .internal}
    - [[`GELU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.GELU.html#mlx.nn.GELU){.reference
      .internal}
  - [mlx.nn.GLU](nn/_autosummary/mlx.nn.GLU.html){.reference .internal}
    - [[`GLU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.GLU.html#mlx.nn.GLU){.reference
      .internal}
  - [mlx.nn.GroupNorm](nn/_autosummary/mlx.nn.GroupNorm.html){.reference
    .internal}
    - [[`GroupNorm`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.GroupNorm.html#mlx.nn.GroupNorm){.reference
      .internal}
  - [mlx.nn.GRU](nn/_autosummary/mlx.nn.GRU.html){.reference .internal}
    - [[`GRU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.GRU.html#mlx.nn.GRU){.reference
      .internal}
  - [mlx.nn.HardShrink](nn/_autosummary/mlx.nn.HardShrink.html){.reference
    .internal}
    - [[`HardShrink`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.HardShrink.html#mlx.nn.HardShrink){.reference
      .internal}
  - [mlx.nn.HardTanh](nn/_autosummary/mlx.nn.HardTanh.html){.reference
    .internal}
    - [[`HardTanh`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.HardTanh.html#mlx.nn.HardTanh){.reference
      .internal}
  - [mlx.nn.Hardswish](nn/_autosummary/mlx.nn.Hardswish.html){.reference
    .internal}
    - [[`Hardswish`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Hardswish.html#mlx.nn.Hardswish){.reference
      .internal}
  - [mlx.nn.InstanceNorm](nn/_autosummary/mlx.nn.InstanceNorm.html){.reference
    .internal}
    - [[`InstanceNorm`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.InstanceNorm.html#mlx.nn.InstanceNorm){.reference
      .internal}
  - [mlx.nn.LayerNorm](nn/_autosummary/mlx.nn.LayerNorm.html){.reference
    .internal}
    - [[`LayerNorm`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.LayerNorm.html#mlx.nn.LayerNorm){.reference
      .internal}
  - [mlx.nn.LeakyReLU](nn/_autosummary/mlx.nn.LeakyReLU.html){.reference
    .internal}
    - [[`LeakyReLU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.LeakyReLU.html#mlx.nn.LeakyReLU){.reference
      .internal}
  - [mlx.nn.Linear](nn/_autosummary/mlx.nn.Linear.html){.reference
    .internal}
    - [[`Linear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Linear.html#mlx.nn.Linear){.reference
      .internal}
  - [mlx.nn.LogSigmoid](nn/_autosummary/mlx.nn.LogSigmoid.html){.reference
    .internal}
    - [[`LogSigmoid`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.LogSigmoid.html#mlx.nn.LogSigmoid){.reference
      .internal}
  - [mlx.nn.LogSoftmax](nn/_autosummary/mlx.nn.LogSoftmax.html){.reference
    .internal}
    - [[`LogSoftmax`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.LogSoftmax.html#mlx.nn.LogSoftmax){.reference
      .internal}
  - [mlx.nn.LSTM](nn/_autosummary/mlx.nn.LSTM.html){.reference
    .internal}
    - [[`LSTM`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.LSTM.html#mlx.nn.LSTM){.reference
      .internal}
  - [mlx.nn.MaxPool1d](nn/_autosummary/mlx.nn.MaxPool1d.html){.reference
    .internal}
    - [[`MaxPool1d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.MaxPool1d.html#mlx.nn.MaxPool1d){.reference
      .internal}
  - [mlx.nn.MaxPool2d](nn/_autosummary/mlx.nn.MaxPool2d.html){.reference
    .internal}
    - [[`MaxPool2d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.MaxPool2d.html#mlx.nn.MaxPool2d){.reference
      .internal}
  - [mlx.nn.MaxPool3d](nn/_autosummary/mlx.nn.MaxPool3d.html){.reference
    .internal}
    - [[`MaxPool3d`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.MaxPool3d.html#mlx.nn.MaxPool3d){.reference
      .internal}
  - [mlx.nn.Mish](nn/_autosummary/mlx.nn.Mish.html){.reference
    .internal}
    - [[`Mish`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Mish.html#mlx.nn.Mish){.reference
      .internal}
  - [mlx.nn.MultiHeadAttention](nn/_autosummary/mlx.nn.MultiHeadAttention.html){.reference
    .internal}
    - [[`MultiHeadAttention`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.MultiHeadAttention.html#mlx.nn.MultiHeadAttention){.reference
      .internal}
  - [mlx.nn.PReLU](nn/_autosummary/mlx.nn.PReLU.html){.reference
    .internal}
    - [[`PReLU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.PReLU.html#mlx.nn.PReLU){.reference
      .internal}
  - [mlx.nn.QuantizedAllToShardedLinear](nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.html){.reference
    .internal}
    - [[`QuantizedAllToShardedLinear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.html#mlx.nn.QuantizedAllToShardedLinear){.reference
      .internal}
  - [mlx.nn.QuantizedEmbedding](nn/_autosummary/mlx.nn.QuantizedEmbedding.html){.reference
    .internal}
    - [[`QuantizedEmbedding`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedEmbedding.html#mlx.nn.QuantizedEmbedding){.reference
      .internal}
  - [mlx.nn.QuantizedLinear](nn/_autosummary/mlx.nn.QuantizedLinear.html){.reference
    .internal}
    - [[`QuantizedLinear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedLinear.html#mlx.nn.QuantizedLinear){.reference
      .internal}
  - [mlx.nn.QuantizedShardedToAllLinear](nn/_autosummary/mlx.nn.QuantizedShardedToAllLinear.html){.reference
    .internal}
    - [[`QuantizedShardedToAllLinear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedShardedToAllLinear.html#mlx.nn.QuantizedShardedToAllLinear){.reference
      .internal}
  - [mlx.nn.RMSNorm](nn/_autosummary/mlx.nn.RMSNorm.html){.reference
    .internal}
    - [[`RMSNorm`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.RMSNorm.html#mlx.nn.RMSNorm){.reference
      .internal}
  - [mlx.nn.ReLU](nn/_autosummary/mlx.nn.ReLU.html){.reference
    .internal}
    - [[`ReLU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ReLU.html#mlx.nn.ReLU){.reference
      .internal}
  - [mlx.nn.ReLU2](nn/_autosummary/mlx.nn.ReLU2.html){.reference
    .internal}
    - [[`ReLU2`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ReLU2.html#mlx.nn.ReLU2){.reference
      .internal}
  - [mlx.nn.ReLU6](nn/_autosummary/mlx.nn.ReLU6.html){.reference
    .internal}
    - [[`ReLU6`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ReLU6.html#mlx.nn.ReLU6){.reference
      .internal}
  - [mlx.nn.RNN](nn/_autosummary/mlx.nn.RNN.html){.reference .internal}
    - [[`RNN`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.RNN.html#mlx.nn.RNN){.reference
      .internal}
  - [mlx.nn.RoPE](nn/_autosummary/mlx.nn.RoPE.html){.reference
    .internal}
    - [[`RoPE`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.RoPE.html#mlx.nn.RoPE){.reference
      .internal}
  - [mlx.nn.SELU](nn/_autosummary/mlx.nn.SELU.html){.reference
    .internal}
    - [[`SELU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.SELU.html#mlx.nn.SELU){.reference
      .internal}
  - [mlx.nn.Sequential](nn/_autosummary/mlx.nn.Sequential.html){.reference
    .internal}
    - [[`Sequential`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Sequential.html#mlx.nn.Sequential){.reference
      .internal}
  - [mlx.nn.ShardedToAllLinear](nn/_autosummary/mlx.nn.ShardedToAllLinear.html){.reference
    .internal}
    - [[`ShardedToAllLinear`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ShardedToAllLinear.html#mlx.nn.ShardedToAllLinear){.reference
      .internal}
  - [mlx.nn.Sigmoid](nn/_autosummary/mlx.nn.Sigmoid.html){.reference
    .internal}
    - [[`Sigmoid`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Sigmoid.html#mlx.nn.Sigmoid){.reference
      .internal}
  - [mlx.nn.SiLU](nn/_autosummary/mlx.nn.SiLU.html){.reference
    .internal}
    - [[`SiLU`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.SiLU.html#mlx.nn.SiLU){.reference
      .internal}
  - [mlx.nn.SinusoidalPositionalEncoding](nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.html){.reference
    .internal}
    - [[`SinusoidalPositionalEncoding`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.html#mlx.nn.SinusoidalPositionalEncoding){.reference
      .internal}
  - [mlx.nn.Softmin](nn/_autosummary/mlx.nn.Softmin.html){.reference
    .internal}
    - [[`Softmin`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Softmin.html#mlx.nn.Softmin){.reference
      .internal}
  - [mlx.nn.Softshrink](nn/_autosummary/mlx.nn.Softshrink.html){.reference
    .internal}
    - [[`Softshrink`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Softshrink.html#mlx.nn.Softshrink){.reference
      .internal}
  - [mlx.nn.Softsign](nn/_autosummary/mlx.nn.Softsign.html){.reference
    .internal}
    - [[`Softsign`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Softsign.html#mlx.nn.Softsign){.reference
      .internal}
  - [mlx.nn.Softmax](nn/_autosummary/mlx.nn.Softmax.html){.reference
    .internal}
    - [[`Softmax`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Softmax.html#mlx.nn.Softmax){.reference
      .internal}
  - [mlx.nn.Softplus](nn/_autosummary/mlx.nn.Softplus.html){.reference
    .internal}
    - [[`Softplus`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Softplus.html#mlx.nn.Softplus){.reference
      .internal}
  - [mlx.nn.Step](nn/_autosummary/mlx.nn.Step.html){.reference
    .internal}
    - [[`Step`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Step.html#mlx.nn.Step){.reference
      .internal}
  - [mlx.nn.Tanh](nn/_autosummary/mlx.nn.Tanh.html){.reference
    .internal}
    - [[`Tanh`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Tanh.html#mlx.nn.Tanh){.reference
      .internal}
  - [mlx.nn.Transformer](nn/_autosummary/mlx.nn.Transformer.html){.reference
    .internal}
    - [[`Transformer`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Transformer.html#mlx.nn.Transformer){.reference
      .internal}
  - [mlx.nn.Upsample](nn/_autosummary/mlx.nn.Upsample.html){.reference
    .internal}
    - [[`Upsample`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.Upsample.html#mlx.nn.Upsample){.reference
      .internal}
- [Functions](nn/functions.html){.reference .internal}
  - [mlx.nn.elu](nn/_autosummary_functions/mlx.nn.elu.html){.reference
    .internal}
    - [[`elu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.elu.html#mlx.nn.elu){.reference
      .internal}
  - [mlx.nn.celu](nn/_autosummary_functions/mlx.nn.celu.html){.reference
    .internal}
    - [[`celu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.celu.html#mlx.nn.celu){.reference
      .internal}
  - [mlx.nn.gelu](nn/_autosummary_functions/mlx.nn.gelu.html){.reference
    .internal}
    - [[`gelu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.gelu.html#mlx.nn.gelu){.reference
      .internal}
  - [mlx.nn.gelu_approx](nn/_autosummary_functions/mlx.nn.gelu_approx.html){.reference
    .internal}
    - [[`gelu_approx`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.gelu_approx.html#mlx.nn.gelu_approx){.reference
      .internal}
  - [mlx.nn.gelu_fast_approx](nn/_autosummary_functions/mlx.nn.gelu_fast_approx.html){.reference
    .internal}
    - [[`gelu_fast_approx`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.gelu_fast_approx.html#mlx.nn.gelu_fast_approx){.reference
      .internal}
  - [mlx.nn.glu](nn/_autosummary_functions/mlx.nn.glu.html){.reference
    .internal}
    - [[`glu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.glu.html#mlx.nn.glu){.reference
      .internal}
  - [mlx.nn.hard_shrink](nn/_autosummary_functions/mlx.nn.hard_shrink.html){.reference
    .internal}
    - [[`hard_shrink`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.hard_shrink.html#mlx.nn.hard_shrink){.reference
      .internal}
  - [mlx.nn.hard_tanh](nn/_autosummary_functions/mlx.nn.hard_tanh.html){.reference
    .internal}
    - [[`hard_tanh`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.hard_tanh.html#mlx.nn.hard_tanh){.reference
      .internal}
  - [mlx.nn.hardswish](nn/_autosummary_functions/mlx.nn.hardswish.html){.reference
    .internal}
    - [[`hardswish`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.hardswish.html#mlx.nn.hardswish){.reference
      .internal}
  - [mlx.nn.leaky_relu](nn/_autosummary_functions/mlx.nn.leaky_relu.html){.reference
    .internal}
    - [[`leaky_relu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.leaky_relu.html#mlx.nn.leaky_relu){.reference
      .internal}
  - [mlx.nn.log_sigmoid](nn/_autosummary_functions/mlx.nn.log_sigmoid.html){.reference
    .internal}
    - [[`log_sigmoid`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.log_sigmoid.html#mlx.nn.log_sigmoid){.reference
      .internal}
  - [mlx.nn.log_softmax](nn/_autosummary_functions/mlx.nn.log_softmax.html){.reference
    .internal}
    - [[`log_softmax`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.log_softmax.html#mlx.nn.log_softmax){.reference
      .internal}
  - [mlx.nn.mish](nn/_autosummary_functions/mlx.nn.mish.html){.reference
    .internal}
    - [[`mish`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.mish.html#mlx.nn.mish){.reference
      .internal}
  - [mlx.nn.prelu](nn/_autosummary_functions/mlx.nn.prelu.html){.reference
    .internal}
    - [[`prelu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.prelu.html#mlx.nn.prelu){.reference
      .internal}
  - [mlx.nn.relu](nn/_autosummary_functions/mlx.nn.relu.html){.reference
    .internal}
    - [[`relu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.relu.html#mlx.nn.relu){.reference
      .internal}
  - [mlx.nn.relu2](nn/_autosummary_functions/mlx.nn.relu2.html){.reference
    .internal}
    - [[`relu2`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.relu2.html#mlx.nn.relu2){.reference
      .internal}
  - [mlx.nn.relu6](nn/_autosummary_functions/mlx.nn.relu6.html){.reference
    .internal}
    - [[`relu6`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.relu6.html#mlx.nn.relu6){.reference
      .internal}
  - [mlx.nn.selu](nn/_autosummary_functions/mlx.nn.selu.html){.reference
    .internal}
    - [[`selu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.selu.html#mlx.nn.selu){.reference
      .internal}
  - [mlx.nn.sigmoid](nn/_autosummary_functions/mlx.nn.sigmoid.html){.reference
    .internal}
    - [[`sigmoid`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.sigmoid.html#mlx.nn.sigmoid){.reference
      .internal}
  - [mlx.nn.silu](nn/_autosummary_functions/mlx.nn.silu.html){.reference
    .internal}
    - [[`silu`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.silu.html#mlx.nn.silu){.reference
      .internal}
  - [mlx.nn.softmax](nn/_autosummary_functions/mlx.nn.softmax.html){.reference
    .internal}
    - [[`softmax`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.softmax.html#mlx.nn.softmax){.reference
      .internal}
  - [mlx.nn.softmin](nn/_autosummary_functions/mlx.nn.softmin.html){.reference
    .internal}
    - [[`softmin`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.softmin.html#mlx.nn.softmin){.reference
      .internal}
  - [mlx.nn.softplus](nn/_autosummary_functions/mlx.nn.softplus.html){.reference
    .internal}
    - [[`softplus`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.softplus.html#mlx.nn.softplus){.reference
      .internal}
  - [mlx.nn.softshrink](nn/_autosummary_functions/mlx.nn.softshrink.html){.reference
    .internal}
    - [[`softshrink`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.softshrink.html#mlx.nn.softshrink){.reference
      .internal}
  - [mlx.nn.step](nn/_autosummary_functions/mlx.nn.step.html){.reference
    .internal}
    - [[`step`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.step.html#mlx.nn.step){.reference
      .internal}
  - [mlx.nn.tanh](nn/_autosummary_functions/mlx.nn.tanh.html){.reference
    .internal}
    - [[`tanh`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.tanh.html#mlx.nn.tanh){.reference
      .internal}
- [Loss Functions](nn/losses.html){.reference .internal}
  - [mlx.nn.losses.binary_cross_entropy](nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html){.reference
    .internal}
    - [[`binary_cross_entropy`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html#mlx.nn.losses.binary_cross_entropy){.reference
      .internal}
  - [mlx.nn.losses.cosine_similarity_loss](nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.html){.reference
    .internal}
    - [[`cosine_similarity_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.html#mlx.nn.losses.cosine_similarity_loss){.reference
      .internal}
  - [mlx.nn.losses.cross_entropy](nn/_autosummary_functions/mlx.nn.losses.cross_entropy.html){.reference
    .internal}
    - [[`cross_entropy`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.cross_entropy.html#mlx.nn.losses.cross_entropy){.reference
      .internal}
  - [mlx.nn.losses.gaussian_nll_loss](nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.html){.reference
    .internal}
    - [[`gaussian_nll_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.html#mlx.nn.losses.gaussian_nll_loss){.reference
      .internal}
  - [mlx.nn.losses.hinge_loss](nn/_autosummary_functions/mlx.nn.losses.hinge_loss.html){.reference
    .internal}
    - [[`hinge_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.hinge_loss.html#mlx.nn.losses.hinge_loss){.reference
      .internal}
  - [mlx.nn.losses.huber_loss](nn/_autosummary_functions/mlx.nn.losses.huber_loss.html){.reference
    .internal}
    - [[`huber_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.huber_loss.html#mlx.nn.losses.huber_loss){.reference
      .internal}
  - [mlx.nn.losses.kl_div_loss](nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.html){.reference
    .internal}
    - [[`kl_div_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.html#mlx.nn.losses.kl_div_loss){.reference
      .internal}
  - [mlx.nn.losses.l1_loss](nn/_autosummary_functions/mlx.nn.losses.l1_loss.html){.reference
    .internal}
    - [[`l1_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.l1_loss.html#mlx.nn.losses.l1_loss){.reference
      .internal}
  - [mlx.nn.losses.log_cosh_loss](nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.html){.reference
    .internal}
    - [[`log_cosh_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.html#mlx.nn.losses.log_cosh_loss){.reference
      .internal}
  - [mlx.nn.losses.margin_ranking_loss](nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.html){.reference
    .internal}
    - [[`margin_ranking_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.html#mlx.nn.losses.margin_ranking_loss){.reference
      .internal}
  - [mlx.nn.losses.mse_loss](nn/_autosummary_functions/mlx.nn.losses.mse_loss.html){.reference
    .internal}
    - [[`mse_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.mse_loss.html#mlx.nn.losses.mse_loss){.reference
      .internal}
  - [mlx.nn.losses.nll_loss](nn/_autosummary_functions/mlx.nn.losses.nll_loss.html){.reference
    .internal}
    - [[`nll_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.nll_loss.html#mlx.nn.losses.nll_loss){.reference
      .internal}
  - [mlx.nn.losses.smooth_l1_loss](nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.html){.reference
    .internal}
    - [[`smooth_l1_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.html#mlx.nn.losses.smooth_l1_loss){.reference
      .internal}
  - [mlx.nn.losses.triplet_loss](nn/_autosummary_functions/mlx.nn.losses.triplet_loss.html){.reference
    .internal}
    - [[`triplet_loss`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary_functions/mlx.nn.losses.triplet_loss.html#mlx.nn.losses.triplet_loss){.reference
      .internal}
- [Initializers](nn/init.html){.reference .internal}
  - [mlx.nn.init.constant](nn/_autosummary/mlx.nn.init.constant.html){.reference
    .internal}
    - [[`constant()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.constant.html#mlx.nn.init.constant){.reference
      .internal}
  - [mlx.nn.init.normal](nn/_autosummary/mlx.nn.init.normal.html){.reference
    .internal}
    - [[`normal()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.normal.html#mlx.nn.init.normal){.reference
      .internal}
  - [mlx.nn.init.uniform](nn/_autosummary/mlx.nn.init.uniform.html){.reference
    .internal}
    - [[`uniform()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.uniform.html#mlx.nn.init.uniform){.reference
      .internal}
  - [mlx.nn.init.identity](nn/_autosummary/mlx.nn.init.identity.html){.reference
    .internal}
    - [[`identity()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.identity.html#mlx.nn.init.identity){.reference
      .internal}
  - [mlx.nn.init.glorot_normal](nn/_autosummary/mlx.nn.init.glorot_normal.html){.reference
    .internal}
    - [[`glorot_normal()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.glorot_normal.html#mlx.nn.init.glorot_normal){.reference
      .internal}
  - [mlx.nn.init.glorot_uniform](nn/_autosummary/mlx.nn.init.glorot_uniform.html){.reference
    .internal}
    - [[`glorot_uniform()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.glorot_uniform.html#mlx.nn.init.glorot_uniform){.reference
      .internal}
  - [mlx.nn.init.he_normal](nn/_autosummary/mlx.nn.init.he_normal.html){.reference
    .internal}
    - [[`he_normal()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.he_normal.html#mlx.nn.init.he_normal){.reference
      .internal}
  - [mlx.nn.init.he_uniform](nn/_autosummary/mlx.nn.init.he_uniform.html){.reference
    .internal}
    - [[`he_uniform()`{.docutils .literal
      .notranslate}]{.pre}](nn/_autosummary/mlx.nn.init.he_uniform.html#mlx.nn.init.he_uniform){.reference
      .internal}
- [Distributed](nn/distributed.html){.reference .internal}
  - [Helper Routines](nn/distributed.html#helper-routines){.reference
    .internal}
    - [mlx.nn.layers.distributed.shard_linear](nn/_autosummary/mlx.nn.layers.distributed.shard_linear.html){.reference
      .internal}
      - [[`shard_linear()`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.layers.distributed.shard_linear.html#mlx.nn.layers.distributed.shard_linear){.reference
        .internal}
    - [mlx.nn.layers.distributed.shard_inplace](nn/_autosummary/mlx.nn.layers.distributed.shard_inplace.html){.reference
      .internal}
      - [[`shard_inplace()`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.layers.distributed.shard_inplace.html#mlx.nn.layers.distributed.shard_inplace){.reference
        .internal}
  - [Layers](nn/distributed.html#layers){.reference .internal}
    - [mlx.nn.AllToShardedLinear](nn/_autosummary/mlx.nn.AllToShardedLinear.html){.reference
      .internal}
      - [[`AllToShardedLinear`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.AllToShardedLinear.html#mlx.nn.AllToShardedLinear){.reference
        .internal}
    - [mlx.nn.ShardedToAllLinear](nn/_autosummary/mlx.nn.ShardedToAllLinear.html){.reference
      .internal}
      - [[`ShardedToAllLinear`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.ShardedToAllLinear.html#mlx.nn.ShardedToAllLinear){.reference
        .internal}
    - [mlx.nn.QuantizedAllToShardedLinear](nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.html){.reference
      .internal}
      - [[`QuantizedAllToShardedLinear`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.html#mlx.nn.QuantizedAllToShardedLinear){.reference
        .internal}
    - [mlx.nn.QuantizedShardedToAllLinear](nn/_autosummary/mlx.nn.QuantizedShardedToAllLinear.html){.reference
      .internal}
      - [[`QuantizedShardedToAllLinear`{.docutils .literal
        .notranslate}]{.pre}](nn/_autosummary/mlx.nn.QuantizedShardedToAllLinear.html#mlx.nn.QuantizedShardedToAllLinear){.reference
        .internal}
:::
:::::::
:::::::::::::::::::::::

::::: prev-next-area
[](_autosummary/mlx.core.clear_cache.html "previous page"){.left-prev}

::: prev-next-info
previous

mlx.core.clear_cache
:::

[](_autosummary/mlx.nn.value_and_grad.html "next page"){.right-next}

::: prev-next-info
next

mlx.nn.value_and_grad
:::
:::::
::::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Quick Start with Neural
  Networks](#quick-start-with-neural-networks){.reference .internal
  .nav-link}
- [The Module Class](#the-module-class){.reference .internal .nav-link}
  - [Parameters](#parameters){.reference .internal .nav-link}
  - [Updating the Parameters](#updating-the-parameters){.reference
    .internal .nav-link}
  - [Inspecting Modules](#inspecting-modules){.reference .internal
    .nav-link}
- [Value and Grad](#value-and-grad){.reference .internal .nav-link}
::::
:::::
::::::
:::::::::::::::::::::::::::::::::::::::::::::

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
::::::::::::::::::::::::::::::::::::::::::::::::::::
