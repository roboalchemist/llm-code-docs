# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.hinge_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.hinge_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.hinge_loss

## Contents

- [[`hinge_loss`]](#mlx.nn.losses.hinge_loss)

# mlx.nn.losses.hinge_loss[\#](#mlx-nn-losses-hinge-loss "Link to this heading")

*[class][ ]*[[hinge_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.hinge_loss "Link to this definition")

:   Computes the hinge loss between inputs and targets.

    ::: 
    \\\[\\text(y, y\_}) = \\max(0, 1 - y \\cdot y\_})\\\]
    :::

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted values.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The target values. They should be -1 or 1.

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed hinge loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.gaussian_nll_loss.html "previous page")

previous

mlx.nn.losses.gaussian_nll_loss

[](mlx.nn.losses.huber_loss.html "next page")

next

mlx.nn.losses.huber_loss

Contents

- [[`hinge_loss`]](#mlx.nn.losses.hinge_loss)

By MLX Contributors

© Copyright 2023, Apple.\