# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adafactor.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adafactor.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Adafactor

## Contents

- [[`Adafactor`]](#mlx.optimizers.Adafactor)

# mlx.optimizers.Adafactor[\#](#mlx-optimizers-adafactor "Link to this heading")

*[class][ ]*[[Adafactor]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[eps]][[:]][ ][[[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[,]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]]][ ][[=]][ ][[(1e-30,] [0.001)]]*, *[[clip_threshold]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[decay_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[-0.8]]*, *[[beta_1]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[weight_decay]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[scale_parameter]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[relative_step]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[warmup_init]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.optimizers.Adafactor "Link to this definition")

:   The Adafactor optimizer.

    Our Adafactor implementation follows the original paper: [Adafactor: Adaptive Learning Rates with Sublinear Memory Cost](https://arxiv.org/abs/1804.04235)

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable,* *optional*) -- The learning rate. Default: [`None`].

        - **eps** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*),* *optional*) -- The first term [\\(\\epsilon_1\\)] added to the square of the gradients to improve numerical stability and the second term [\\(\\epsilon_2\\)] is used for parameter scaling if [`parameter_scale`] is set to [`True`]. Default: [`(1e-30,`]` `[`1e-3)`].

        - **clip_threshold** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Clips the unscaled update at [`clip_threshold`]. Default: [`1.0`].

        - **decay_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Coefficient for the running average of the squared gradient. Default: [`-0.8`].

        - **beta_1** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- If set to a value bigger than zero then first moment will be used. Default: [`None`].

        - **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The weight decay [\\(\\lambda\\)]. Default: [`0.0`].

        - **scale_parameter** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] the learning rate will be scaled by [\\(\\max(\\epsilon_1, \\text(w\_))\\)]. Default: [`True`].

        - **relative_step** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] the [`learning_rate`] will be ignored and relative step size will be computed. Default: [`True`].

        - **warmup_init** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] then the relative step size will be calculated by the current step. Default: [`False`].

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- ----------------------------------------------------
      [`__init__`](\[learning_rate, eps, \...\])     
      [`apply_single`](gradient, parameter, state)   Performs the Adafactor parameter and state update.
      [`init_single`](parameter, state)              Initialize optimizer state
      ------------------------------------------------------------------------------------------------------- ----------------------------------------------------
    :::

[](mlx.optimizers.Adagrad.html "previous page")

previous

mlx.optimizers.Adagrad

[](mlx.optimizers.AdaDelta.html "next page")

next

mlx.optimizers.AdaDelta

Contents

- [[`Adafactor`]](#mlx.optimizers.Adafactor)

By MLX Contributors

© Copyright 2023, Apple.\