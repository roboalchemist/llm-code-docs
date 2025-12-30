# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.triplet_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.triplet_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.triplet_loss

## Contents

- [[`triplet_loss`]](#mlx.nn.losses.triplet_loss)

# mlx.nn.losses.triplet_loss[\#](#mlx-nn-losses-triplet-loss "Link to this heading")

*[class][ ]*[[triplet_loss]][(]*[[anchors]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[positives]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[negatives]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[p]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[2]]*, *[[margin]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-06]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.triplet_loss "Link to this definition")

:   Computes the triplet loss for a set of anchor, positive, and negative samples. Margin is represented with alpha in the math section.

    ::: 
    \\\[\\max\\left(\\\|A - P\\\|\_p - \\\|A - N\\\|\_p + \\alpha, 0\\right)\\\]
    :::

    Parameters[:]

    :   - **anchors** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The anchor samples.

        - **positives** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The positive samples.

        - **negatives** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The negative samples.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The distribution axis. Default: [`-1`].

        - **p** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The norm degree for pairwise distance. Default: [`2`].

        - **margin** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Margin for the triplet loss. Defaults to [`1.0`].

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Small positive constant to prevent numerical instability. Defaults to [`1e-6`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   

        Computed triplet loss. If reduction is "none", returns a tensor of the same shape as input;

        :   if reduction is "mean" or "sum", returns a scalar tensor.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.smooth_l1_loss.html "previous page")

previous

mlx.nn.losses.smooth_l1_loss

[](../init.html "next page")

next

Initializers

Contents

- [[`triplet_loss`]](#mlx.nn.losses.triplet_loss)

By MLX Contributors

© Copyright 2023, Apple.\