# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.kl_div_loss

## Contents

- [[`kl_div_loss`]](#mlx.nn.losses.kl_div_loss)

# mlx.nn.losses.kl_div_loss[\#](#mlx-nn-losses-kl-div-loss "Link to this heading")

*[class][ ]*[[kl_div_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'none\']]*[)][\#](#mlx.nn.losses.kl_div_loss "Link to this definition")

:   Computes the Kullback-Leibler divergence loss.

    Computes the following when [`reduction`]` `[`==`]` `[`'none'`]:

    :::: 
    ::: highlight
        mx.exp(targets) * (targets - inputs).sum(axis)
    :::
    ::::

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Log probabilities for the predicted distribution.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Log probabilities for the target distribution.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The distribution axis. Default: [`-1`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The computed Kullback-Leibler divergence loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.huber_loss.html "previous page")

previous

mlx.nn.losses.huber_loss

[](mlx.nn.losses.l1_loss.html "next page")

next

mlx.nn.losses.l1_loss

Contents

- [[`kl_div_loss`]](#mlx.nn.losses.kl_div_loss)

By MLX Contributors

© Copyright 2023, Apple.\