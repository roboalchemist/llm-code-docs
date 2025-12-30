# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.nll_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.nll_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.nll_loss

## Contents

- [[`nll_loss`]](#mlx.nn.losses.nll_loss)

# mlx.nn.losses.nll_loss[\#](#mlx-nn-losses-nll-loss "Link to this heading")

*[class][ ]*[[nll_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.nll_loss "Link to this definition")

:   Computes the negative log likelihood loss.

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted distribution in log space.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The target values.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The distribution axis. Default: [`-1`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed NLL loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.mse_loss.html "previous page")

previous

mlx.nn.losses.mse_loss

[](mlx.nn.losses.smooth_l1_loss.html "next page")

next

mlx.nn.losses.smooth_l1_loss

Contents

- [[`nll_loss`]](#mlx.nn.losses.nll_loss)

By MLX Contributors

© Copyright 2023, Apple.\