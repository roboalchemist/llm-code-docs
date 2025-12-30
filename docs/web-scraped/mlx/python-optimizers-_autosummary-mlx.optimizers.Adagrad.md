# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adagrad.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adagrad.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Adagrad

## Contents

- [[`Adagrad`]](#mlx.optimizers.Adagrad)

# mlx.optimizers.Adagrad[\#](#mlx-optimizers-adagrad "Link to this heading")

*[class][ ]*[[Adagrad]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*[)][\#](#mlx.optimizers.Adagrad "Link to this definition")

:   The Adagrad optimizer \[1\].

    Our Adagrad implementation follows the original paper. In detail,

    \[1\]: Duchi, J., Hazan, E. and Singer, Y., 2011. Adaptive subgradient methods for online learning and stochastic optimization. JMLR 2011.

    ::: 
    \\\[\\beginv\_ &= v_t + g_t\^2 \\\\ w\_ &= w_t - \\lambda \\frac} + \\epsilon}\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: [`1e-8`]

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, eps\])           
      [`apply_single`](gradient, parameter, state)   Performs the Adagrad parameter update and stores [\\(v\\)] in the optimizer state.
      [`init_single`](parameter, state)              Initialize optimizer state
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.RMSprop.html "previous page")

previous

mlx.optimizers.RMSprop

[](mlx.optimizers.Adafactor.html "next page")

next

mlx.optimizers.Adafactor

Contents

- [[`Adagrad`]](#mlx.optimizers.Adagrad)

By MLX Contributors

© Copyright 2023, Apple.\