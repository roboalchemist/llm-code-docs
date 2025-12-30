# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.losses.gaussian_nll_loss

## Contents

- [[`gaussian_nll_loss`]](#mlx.nn.losses.gaussian_nll_loss)

# mlx.nn.losses.gaussian_nll_loss[\#](#mlx-nn-losses-gaussian-nll-loss "Link to this heading")

*[class][ ]*[[gaussian_nll_loss]][(]*[[inputs]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[targets]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[vars]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[full]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-06]]*, *[[reduction]][[:]][ ][[[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'none\']][[,]][ ][[\'mean\']][[,]][ ][[\'sum\']][[\]]]][ ][[=]][ ][[\'mean\']]*[)][\#](#mlx.nn.losses.gaussian_nll_loss "Link to this definition")

:   Computes the negative log likelihood loss for a Gaussian distribution.

    The loss is given by:

    ::: 
    \\\[\\frac\\left(\\log\\left(\\max\\left(\\text, \\ \\epsilon\\right)\\right) + \\frac - \\text \\right)\^2} , \\ \\epsilon \\right)}\\right) + \\text\\\]
    :::

    where [`inputs`] are the predicted means and [`vars`] are the the predicted variances.

    Parameters[:]

    :   - **inputs** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted expectation of the Gaussian distribution.

        - **targets** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The target values (samples from the Gaussian distribution).

        - **vars** ([*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The predicted variance of the Gaussian distribution.

        - **full** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether to include the constant term in the loss calculation. Default: [`False`].

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Small positive constant for numerical stability. Default: [`1e-6`].

        - **reduction** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Specifies the reduction to apply to the output: [`'none'`] \| [`'mean'`] \| [`'sum'`]. Default: [`'none'`].

    Returns[:]

    :   The Gaussian NLL loss.

    Return type[:]

    :   [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.nn.losses.cross_entropy.html "previous page")

previous

mlx.nn.losses.cross_entropy

[](mlx.nn.losses.hinge_loss.html "next page")

next

mlx.nn.losses.hinge_loss

Contents

- [[`gaussian_nll_loss`]](#mlx.nn.losses.gaussian_nll_loss)

By MLX Contributors

© Copyright 2023, Apple.\