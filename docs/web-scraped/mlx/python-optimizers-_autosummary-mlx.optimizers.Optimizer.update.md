# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.update.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Optimizer.update.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Optimizer.update

## Contents

- [[`Optimizer.update()`]](#mlx.optimizers.Optimizer.update)

# mlx.optimizers.Optimizer.update[\#](#mlx-optimizers-optimizer-update "Link to this heading")

[[Optimizer.]][[update]][(]*[[model]][[:]][ ][[[Module]](../../nn/module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]*, *[[gradients]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*[)][\#](#mlx.optimizers.Optimizer.update "Link to this definition")

:   Apply the gradients to the parameters of the model and update the model with the new parameters.

    Parameters[:]

    :   - **model** ([*Module*](../../nn/module.html#mlx.nn.Module "mlx.nn.Module")) -- An mlx module to be updated.

        - **gradients** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A Python tree of gradients, most likely computed via [[`mlx.nn.value_and_grad()`]](../../_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad "mlx.nn.value_and_grad").

[](mlx.optimizers.Optimizer.init.html "previous page")

previous

mlx.optimizers.Optimizer.init

[](../common_optimizers.html "next page")

next

Common Optimizers

Contents

- [[`Optimizer.update()`]](#mlx.optimizers.Optimizer.update)

By MLX Contributors

© Copyright 2023, Apple.\