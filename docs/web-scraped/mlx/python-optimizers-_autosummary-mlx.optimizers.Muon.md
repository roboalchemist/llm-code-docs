# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Muon.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Muon.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Muon

## Contents

- [[`Muon`]](#mlx.optimizers.Muon)

# mlx.optimizers.Muon[\#](#mlx-optimizers-muon "Link to this heading")

*[class][ ]*[[Muon]][(]*[[learning_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[momentum]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.95]]*, *[[weight_decay]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.01]]*, *[[nesterov]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[ns_steps]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[5]]*[)][\#](#mlx.optimizers.Muon "Link to this definition")

:   The Muon optimizer.

    Our Muon (MomentUm Orthogonalized by Newton-schulz) optimizer follows the original implementation: [Muon: An optimizer for hidden layers in neural networks](https://kellerjordan.github.io/posts/muon/)

    ::: 
    Note

    - Muon may be sub-optimal for the embedding layer, the final fully connected layer, or any 0D/1D parameters. Those should be optimized by a different method (e.g., [[`AdamW`]](mlx.optimizers.AdamW.html#mlx.optimizers.AdamW "mlx.optimizers.AdamW")).

    - For 4D convolutional filters, it works by flattening their last dimensions.
    :::

    Parameters[:]

    :   - **learning_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* *callable*) -- The learning rate.

        - **momentum** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The momentum strength. Default: [`0.95`]

        - **weight_decay** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The weight decay (L2 penalty). Default: [`0.01`]

        - **nesterov** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Enables Nesterov momentum. Recommended for better performance. Default: [`True`]

        - **ns_steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Number of Newton-Schulz iteration steps for orthogonalization. Default: [`5`]

    Methods

    ::: pst-scrollable-table-container
      ---------------------------------------------------------------------------------------------------------- ------------------------------------
      [`__init__`](learning_rate\[, momentum, \...\])   
      [`apply_single`](gradient, parameter, state)      Performs the Muon parameter update
      [`init_single`](parameter, state)                 Initialize optimizer state
      ---------------------------------------------------------------------------------------------------------- ------------------------------------
    :::

[](mlx.optimizers.MultiOptimizer.html "previous page")

previous

mlx.optimizers.MultiOptimizer

[](../schedulers.html "next page")

next

Schedulers

Contents

- [[`Muon`]](#mlx.optimizers.Muon)

By MLX Contributors

© Copyright 2023, Apple.\