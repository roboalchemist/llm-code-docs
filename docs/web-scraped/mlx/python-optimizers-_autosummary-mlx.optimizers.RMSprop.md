# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.RMSprop.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.RMSprop.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.RMSprop

## Contents

- [[`RMSprop`]](#mlx.optimizers.RMSprop)

# mlx.optimizers.RMSprop[\#](#mlx-optimizers-rmsprop "Link to this heading")

*[class][ ]*[[RMSprop]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[alpha]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.99]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*[)][\#](#mlx.optimizers.RMSprop "Link to this definition")

:   The RMSprop optimizer \[1\].

    \[1\]: Tieleman, T. and Hinton, G. 2012. Lecture 6.5-rmsprop, coursera: Neural networks for machine learning

    ::: 
    \\\[\\beginv\_ &= \\alpha v_t + (1 - \\alpha) g_t\^2 \\\\ w\_ &= w_t - \\lambda \\frac} + \\epsilon}\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The smoothing constant [\\(\\alpha\\)]. Default: [`0.99`]

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: [`1e-8`]

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, alpha, eps\])    
      [`apply_single`](gradient, parameter, state)   Performs the RMSprop parameter update and stores [\\(v\\)] in the optimizer state.
      [`init_single`](parameter, state)              Initialize optimizer state
      ------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.SGD.html "previous page")

previous

mlx.optimizers.SGD

[](mlx.optimizers.Adagrad.html "next page")

next

mlx.optimizers.Adagrad

Contents

- [[`RMSprop`]](#mlx.optimizers.RMSprop)

By MLX Contributors

© Copyright 2023, Apple.\