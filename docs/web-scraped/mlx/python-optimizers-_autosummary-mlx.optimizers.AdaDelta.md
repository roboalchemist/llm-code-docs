# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.AdaDelta.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.AdaDelta.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.AdaDelta

## Contents

- [[`AdaDelta`]](#mlx.optimizers.AdaDelta)

# mlx.optimizers.AdaDelta[\#](#mlx-optimizers-adadelta "Link to this heading")

*[class][ ]*[[AdaDelta]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[rho]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.9]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-06]]*[)][\#](#mlx.optimizers.AdaDelta "Link to this definition")

:   The AdaDelta optimizer with a learning rate \[1\].

    Our AdaDelta implementation follows the original paper. In detail,

    \[1\]: Zeiler, M.D., 2012. ADADELTA: an adaptive learning rate method. arXiv preprint arXiv:1212.5701.

    ::: 
    \\\[\\beginv\_ &= \\rho v_t + (1 - \\rho) g_t\^2 \\\\ \\Delta w\_ &= \\frac} + \\epsilon}} g_t \\\\ u\_ &= \\rho u_t + (1 - \\rho) \\Delta w\_\^2 \\\\ w\_ &= w_t - \\lambda \\Delta w\_\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **rho** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The coefficient [\\(\\rho\\)] used for computing a running average of squared gradients. Default: [`0.9`]

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: 1e-8

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, rho, eps\])      
      [`apply_single`](gradient, parameter, state)   Performs the AdaDelta parameter update and stores [\\(v\\)] and [\\(u\\)] in the optimizer state.
      [`init_single`](parameter, state)              Initialize optimizer state
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.Adafactor.html "previous page")

previous

mlx.optimizers.Adafactor

[](mlx.optimizers.Adam.html "next page")

next

mlx.optimizers.Adam

Contents

- [[`AdaDelta`]](#mlx.optimizers.AdaDelta)

By MLX Contributors

© Copyright 2023, Apple.\