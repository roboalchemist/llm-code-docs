# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.huber_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.huber_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.huber_loss

## Contents

- [[`huber_loss`]](#mlx.nn.losses.huber_loss)

# mlx.nn.losses.huber_loss[\#](#mlx-nn-losses-huber-loss "Link to this heading")

*[class][ ]*[[huber_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[delta]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.huber_loss "Link to this definition")

:   Computes the Huber loss between inputs and targets.

    ::: 
    \\\[\\beginl\_(a) = \\left\\ \\frac a\^2 & \\text \|a\| \\leq \\delta, \\\\ \\delta \\left( \|a\| - \\frac \\delta \\right) & \\text \\end \\right.\\end\\\]
    :::

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted values.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The target values.

        - **delta** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The threshold at which to change between L1 and L2 loss. Default: [`1.0`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed Huber loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.hinge_loss.html "previous page")

previous

mlx.nn.losses.hinge_loss

[](mlx.nn.losses.kl_div_loss.html "next page")

next

mlx.nn.losses.kl_div_loss

Contents

- [[`huber_loss`]](#mlx.nn.losses.huber_loss)

By MLX Contributors

© Copyright 2023, Apple.\