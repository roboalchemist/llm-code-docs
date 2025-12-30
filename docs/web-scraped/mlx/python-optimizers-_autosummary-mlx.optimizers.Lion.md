# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Lion.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Lion.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Lion

## Contents

- [[`Lion`]](#mlx.optimizers.Lion)

# mlx.optimizers.Lion[\#](#mlx-optimizers-lion "Link to this heading")

*[class][ ]*[[Lion]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[betas]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[0.9,] [0.99\]]]*, *[[weight_decay]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*[)][\#](#mlx.optimizers.Lion "Link to this definition")

:   The Lion optimizer \[1\].

    Since updates are computed through the sign operation, they tend to have larger norm than for other optimizers such as SGD and Adam. We recommend a learning rate that is 3-10x smaller than AdamW and a weight decay 3-10x larger than AdamW to maintain the strength (lr \* wd). Our Lion implementation follows the original paper. In detail,

    \[1\]: Chen, X. Symbolic Discovery of Optimization Algorithms. arXiv preprint arXiv:2302.06675.

    ::: 
    \\\[\\beginc\_ &= \\beta_1 m_t + (1 - \\beta_1) g_t \\\\ m\_ &= \\beta_2 m_t + (1 - \\beta_2) g_t \\\\ w\_ &= w_t - \\eta (\\text(c_t) + \\lambda w_t)\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\eta\\)].

        - **betas** (*Tuple\[*[*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*\],* *optional*) -- The coefficients [\\((\\beta_1, \\beta_2)\\)] used for computing the gradient momentum and update direction. Default: [`(0.9,`]` `[`0.99)`]

        - **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The weight decay [\\(\\lambda\\)]. Default: [`0.0`]

    Methods

    ::: pst-scrollable-table-container
      --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, betas, weight_decay\])   
      [`apply_single`](gradient, parameter, state)           Performs the Lion parameter update and stores [\\(m\\)] in the optimizer state.
      [`init_single`](parameter, state)                      Initialize optimizer state
      --------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.optimizers.Adamax.html "previous page")

previous

mlx.optimizers.Adamax

[](mlx.optimizers.MultiOptimizer.html "next page")

next

mlx.optimizers.MultiOptimizer

Contents

- [[`Lion`]](#mlx.optimizers.Lion)

By MLX Contributors

© Copyright 2023, Apple.\