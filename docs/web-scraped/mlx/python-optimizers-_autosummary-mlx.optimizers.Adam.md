# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adam.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adam.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Adam

## Contents

- [[`Adam`]](#mlx.optimizers.Adam)

# mlx.optimizers.Adam[\#](#mlx-optimizers-adam "Link to this heading")

*[class][ ]*[[Adam]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[betas]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[0.9,] [0.999\]]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*, *[[bias_correction]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.optimizers.Adam "Link to this definition")

:   The Adam optimizer \[1\]. In detail,

    \[1\]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic optimization. ICLR 2015.

    ::: 
    \\\[\\beginm\_ &= \\beta_1 m_t + (1 - \\beta_1) g_t \\\\ v\_ &= \\beta_2 v_t + (1 - \\beta_2) g_t\^2 \\\\ w\_ &= w_t - \\lambda \\frac}} + \\epsilon}\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **betas** (*Tuple\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*\],* *optional*) -- The coefficients [\\((\\beta_1, \\beta_2)\\)] used for computing running averages of the gradient and its square. Default: [`(0.9,`]` `[`0.999)`]

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: [`1e-8`]

        - **bias_correction** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`], bias correction is applied. Default: [`False`]

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, betas, eps, \...\])   
      [`apply_single`](gradient, parameter, state)        Performs the Adam parameter update and stores [\\(v\\)] and [\\(m\\)] in the optimizer state.
      [`init_single`](parameter, state)                   Initialize optimizer state
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.AdaDelta.html "previous page")

previous

mlx.optimizers.AdaDelta

[](mlx.optimizers.AdamW.html "next page")

next

mlx.optimizers.AdamW

Contents

- [[`Adam`]](#mlx.optimizers.Adam)

By MLX Contributors

© Copyright 2023, Apple.\