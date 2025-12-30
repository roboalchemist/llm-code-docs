# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.SGD.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.SGD.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.SGD

## Contents

- [[`SGD`]](#mlx.optimizers.SGD)

# mlx.optimizers.SGD[\#](#mlx-optimizers-sgd "Link to this heading")

*[class][ ]*[[SGD]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[momentum]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[weight_decay]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[dampening]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[nesterov]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.optimizers.SGD "Link to this definition")

:   The stochastic gradient descent optimizer.

    Updates a parameter [\\(w\\)] with a gradient [\\(g\\)] as follows

    ::: 
    \\\[\\beginv\_ &= \\mu v_t + (1 - \\tau) g_t \\\\ w\_ &= w_t - \\lambda v\_\\end\\\]
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate [\\(\\lambda\\)].

        - **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The momentum strength [\\(\\mu\\)]. Default: [`0`]

        - **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The weight decay (L2 penalty). Default: [`0`]

        - **dampening** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Dampening for momentum [\\(\\tau\\)]. Default: [`0`]

        - **nesterov** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Enables Nesterov momentum. Default: [`False`]

    Methods

    ::: pst-scrollable-table-container
      ---------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
      [`__init__`](learning_rate\[, momentum, \...\])   
      [`apply_single`](gradient, parameter, state)      Performs the SGD parameter update and stores [\\(v\\)] in the optimizer state.
      [`init_single`](parameter, state)                 Initialize optimizer state
      ---------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------
    :::

[](../common_optimizers.html "previous page")

previous

Common Optimizers

[](mlx.optimizers.RMSprop.html "next page")

next

mlx.optimizers.RMSprop

Contents

- [[`SGD`]](#mlx.optimizers.SGD)

By MLX Contributors

© Copyright 2023, Apple.\