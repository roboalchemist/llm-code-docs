# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adamax.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adamax.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Adamax

## Contents

- [[`Adamax`]](#mlx.optimizers.Adamax)

# mlx.optimizers.Adamax[\#](#mlx-optimizers-adamax "Link to this heading")

*[class][ ]*[[Adamax]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[betas]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[0.9,] [0.999\]]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*[)][\#](#mlx.optimizers.Adamax "Link to this definition")

:   The Adamax optimizer, a variant of Adam based on the infinity norm \[1\].

    Our Adam implementation follows the original paper and omits the bias correction in the first and second moment estimates. In detail,

    \[1\]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic optimization. ICLR 2015.

    ::: 
    \\\[\\beginm\_ &= \\beta_1 m_t + (1 - \\beta_1) g_t \\\\ v\_ &= \\max(\\beta_2 v_t, \|g_t\|) \\\\ w\_ &= w_t - \\lambda \\frac} + \\epsilon}\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **betas** (*Tuple\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*\],* *optional*) -- The coefficients [\\((\\beta_1, \\beta_2)\\)] used for computing running averages of the gradient and its square. Default: [`(0.9,`]` `[`0.999)`]

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: [`1e-8`]

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, betas, eps\])    
      [`apply_single`](gradient, parameter, state)   Performs the Adamax parameter update and stores [\\(v\\)] and [\\(m\\)] in the optimizer state.
      [`init_single`](parameter, state)              Initialize optimizer state
      ------------------------------------------------------------------------------------------------------- -------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.AdamW.html "previous page")

previous

mlx.optimizers.AdamW

[](mlx.optimizers.Lion.html "next page")

next

mlx.optimizers.Lion

Contents

- [[`Adamax`]](#mlx.optimizers.Adamax)

By MLX Contributors

© Copyright 2023, Apple.\