# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.margin_ranking_loss

## Contents

- [[`margin_ranking_loss`]](#mlx.nn.losses.margin_ranking_loss)

# mlx.nn.losses.margin_ranking_loss[\#](#mlx-nn-losses-margin-ranking-loss "Link to this heading")

*[class][ ]*[[margin_ranking_loss]][(]*[[inputs1]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[inputs2]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[margin]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.margin_ranking_loss "Link to this definition")

:   Calculate the margin ranking loss that loss given inputs [\\(x_1\\)], [\\(x_2\\)] and a label [\\(y\\)] (containing 1 or -1).

    The loss is given by:

    ::: 
    \\\[\\text = \\max (0, -y \* (x_1 - x_2) + \\text)\\\]
    :::

    Where [\\(y\\)] represents [`targets`], [\\(x_1\\)] represents [`inputs1`] and [\\(x_2\\)] represents [`inputs2`].

    Parameters[:]

    :   - **inputs1** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Scores for the first input.

        - **inputs2** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Scores for the second input.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Labels indicating whether samples in [`inputs1`] should be ranked higher than samples in [`inputs2`]. Values should be 1 or -1.

        - **margin** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The margin by which the scores should be separated. Default: [`0.0`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed margin ranking loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn as nn
        >>> targets = mx.array([1, 1, -1])
        >>> inputs1 = mx.array([-0.573409, -0.765166, -0.0638])
        >>> inputs2 = mx.array([0.75596, 0.225763, 0.256995])
        >>> loss = nn.losses.margin_ranking_loss(inputs1, inputs2, targets)
        >>> loss
        array(0.773433, dtype=float32)
    :::
    ::::

[](mlx.nn.losses.log_cosh_loss.html "previous page")

previous

mlx.nn.losses.log_cosh_loss

[](mlx.nn.losses.mse_loss.html "next page")

next

mlx.nn.losses.mse_loss

Contents

- [[`margin_ranking_loss`]](#mlx.nn.losses.margin_ranking_loss)

By MLX Contributors

© Copyright 2023, Apple.\