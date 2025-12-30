# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.log_cosh_loss

## Contents

- [[`log_cosh_loss`]](#mlx.nn.losses.log_cosh_loss)

# mlx.nn.losses.log_cosh_loss[\#](#mlx-nn-losses-log-cosh-loss "Link to this heading")

*[class][ ]*[[log_cosh_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.log_cosh_loss "Link to this definition")

:   Computes the log cosh loss between inputs and targets.

    Logcosh acts like L2 loss for small errors, ensuring stable gradients, and like the L1 loss for large errors, reducing sensitivity to outliers. This dual behavior offers a balanced, robust approach for regression tasks.

    ::: 
    \\\[\\text(y\_}, y\_}) = \\frac \\sum\_\^ \\log(\\cosh(y\_}\^ - y\_}\^))\\\]
    :::

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted values.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The target values.

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed log cosh loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.l1_loss.html "previous page")

previous

mlx.nn.losses.l1_loss

[](mlx.nn.losses.margin_ranking_loss.html "next page")

next

mlx.nn.losses.margin_ranking_loss

Contents

- [[`log_cosh_loss`]](#mlx.nn.losses.log_cosh_loss)

By MLX Contributors

© Copyright 2023, Apple.\