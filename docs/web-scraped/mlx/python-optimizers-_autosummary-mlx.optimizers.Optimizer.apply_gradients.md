# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.Optimizer.apply_gradients

## Contents

- [[`Optimizer.apply_gradients()`]](#mlx.optimizers.Optimizer.apply_gradients)

# mlx.optimizers.Optimizer.apply_gradients[\#](#mlx-optimizers-optimizer-apply-gradients "Link to this heading")

[[Optimizer.]][[apply_gradients]][(]*[[gradients]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*, *[[parameters]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")]*[)][\#](#mlx.optimizers.Optimizer.apply_gradients "Link to this definition")

:   Apply the gradients to the parameters and return the updated parameters.

    Can be used to update a model via [`model.update(opt.apply_gradients(grads,`]` `[`model))`] which is precisely how [[`Optimizer.update()`]](mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update "mlx.optimizers.Optimizer.update") is implemented.

    Parameters[:]

    :   - **gradients** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A Python tree of gradients.

        - **parameters** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A Python tree of parameters. It can be a superset of the gradients. In that case the returned python tree will be of the same structure as the gradients.

[](mlx.optimizers.Optimizer.state.html "previous page")

previous

mlx.optimizers.Optimizer.state

[](mlx.optimizers.Optimizer.init.html "next page")

next

mlx.optimizers.Optimizer.init

Contents

- [[`Optimizer.apply_gradients()`]](#mlx.optimizers.Optimizer.apply_gradients)

By MLX Contributors

© Copyright 2023, Apple.\