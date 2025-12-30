# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.init.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Optimizer.init.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Optimizer.init

## Contents

- [[`Optimizer.init()`]](#mlx.optimizers.Optimizer.init)

# mlx.optimizers.Optimizer.init[\#](#mlx-optimizers-optimizer-init "Link to this heading")

[[Optimizer.]][[init]][(]*[[parameters]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*[)][\#](#mlx.optimizers.Optimizer.init "Link to this definition")

:   Initialize the optimizer's state

    This function can be used to initialize optimizers which have state (like momentum in [[`SGD`]](mlx.optimizers.SGD.html#mlx.optimizers.SGD "mlx.optimizers.SGD")). Using this method is optional as the optimizer will initialize itself if the state is not yet set. However, there are some cases where explicit initialization is useful in order to have access to the [[`Optimizer.state`]](mlx.optimizers.Optimizer.state.html#mlx.optimizers.Optimizer.state "mlx.optimizers.Optimizer.state") before the first call to [[`Optimizer.update()`]](mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update "mlx.optimizers.Optimizer.update").

    Parameters[:]

    :   **model** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A Python tree of parameters.

    Example

    :::: 
    ::: highlight
        >>> optimizer = optim.SGD(learning_rate=1e-1, momentum=0.9)
        >>> model = nn.Linear(2, 2)
        >>> optimizer.init(model.trainable_parameters())
        >>> optimizer.state.keys()
        dict_keys(['step', 'learning_rate', 'weight', 'bias'])
    :::
    ::::

[](mlx.optimizers.Optimizer.apply_gradients.html "previous page")

previous

mlx.optimizers.Optimizer.apply_gradients

[](mlx.optimizers.Optimizer.update.html "next page")

next

mlx.optimizers.Optimizer.update

Contents

- [[`Optimizer.init()`]](#mlx.optimizers.Optimizer.init)

By MLX Contributors

© Copyright 2023, Apple.\