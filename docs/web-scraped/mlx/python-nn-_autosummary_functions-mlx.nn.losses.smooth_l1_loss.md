# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.smooth_l1_loss

## Contents

- [[`smooth_l1_loss`]](#mlx.nn.losses.smooth_l1_loss)

# mlx.nn.losses.smooth_l1_loss[\#](#mlx-nn-losses-smooth-l1-loss "Link to this heading")

*[class][ ]*[[smooth_l1_loss]][(]*[[predictions]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[beta]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'mean\']]*[)][\#](#mlx.nn.losses.smooth_l1_loss "Link to this definition")

:   Computes the smooth L1 loss.

    The smooth L1 loss is a variant of the L1 loss which replaces the absolute difference with a squared difference when the absolute difference is less than [`beta`].

    The formula for the smooth L1 Loss is:

    ::: 
    \\\[\\beginl = \\begin 0.5 (x - y)\^2 / \\beta, & \\text \|x - y\| \< \\beta \\\\ \|x - y\| - 0.5 \\beta, & \\text \\end\\end\\\]
    :::

    Parameters[:]

    :   - **predictions** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Predicted values.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Ground truth values.

        - **beta** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The threshold after which the loss changes from the squared to the absolute difference. Default: [`1.0`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'mean'`].

    Returns[:]

    :   The computed smooth L1 loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.nll_loss.html "previous page")

previous

mlx.nn.losses.nll_loss

[](mlx.nn.losses.triplet_loss.html "next page")

next

mlx.nn.losses.triplet_loss

Contents

- [[`smooth_l1_loss`]](#mlx.nn.losses.smooth_l1_loss)

By MLX Contributors

© Copyright 2023, Apple.\