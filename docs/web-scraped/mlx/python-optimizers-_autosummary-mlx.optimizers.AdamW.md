# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.AdamW.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.AdamW.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.AdamW

## Contents

- [[`AdamW`]](#mlx.optimizers.AdamW)

# mlx.optimizers.AdamW[\#](#mlx-optimizers-adamw "Link to this heading")

*[class][ ]*[[AdamW]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[betas]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[0.9,] [0.999\]]]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*, *[[weight_decay]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.01]]*, *[[bias_correction]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.optimizers.AdamW "Link to this definition")

:   The AdamW optimizer \[1\]. We update the weights with a weight_decay ([\\(\\lambda\\)]) value:

    \[1\]: Loshchilov, I. and Hutter, F., 2019. Decoupled weight decay regularization. ICLR 2019.

    ::: 
    \\\[\\beginm\_ &= \\beta_1 m_t + (1 - \\beta_1) g_t \\\\ v\_ &= \\beta_2 v_t + (1 - \\beta_2) g_t\^2 \\\\ w\_ &= w_t - \\alpha (\\frac}} + \\epsilon} + \\lambda w_t)\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\alpha\\)].

        - **betas** (*Tuple\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*\],* *optional*) -- The coefficients [\\((\\beta_1, \\beta_2)\\)] used for computing running averages of the gradient and its square. Default: [`(0.9,`]` `[`0.999)`]

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The term [\\(\\epsilon\\)] added to the denominator to improve numerical stability. Default: [`1e-8`]

        - **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The weight decay [\\(\\lambda\\)]. Default: [`0.01`].

        - **bias_correction** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`], bias correction is applied. Default: [`False`]

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, betas, eps, \...\])   
      [`apply_single`](gradient, parameter, state)        Performs the AdamW parameter update by modifying the parameters passed into Adam.
      ------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------
    :::

[](mlx.optimizers.Adam.html "previous page")

previous

mlx.optimizers.Adam

[](mlx.optimizers.Adamax.html "next page")

next

mlx.optimizers.Adamax

Contents

- [[`AdamW`]](#mlx.optimizers.AdamW)

By MLX Contributors

© Copyright 2023, Apple.\