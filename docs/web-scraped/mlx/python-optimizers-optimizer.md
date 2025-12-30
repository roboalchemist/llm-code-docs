# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/optimizer.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/optimizers/optimizer.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Optimizer

## Contents

- [[`Optimizer`]](#mlx.optimizers.Optimizer)

# Optimizer[\#](#optimizer "Link to this heading")

*[class][ ]*[[Optimizer]][(]*[[schedulers]][[=]][[None]]*[)][\#](#mlx.optimizers.Optimizer "Link to this definition")

:   The base class for all optimizers. It allows us to implement an optimizer on a per-parameter basis and apply it to a parameter tree.

    Attributes

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------
      [[`Optimizer.state`]](_autosummary/mlx.optimizers.Optimizer.state.html#mlx.optimizers.Optimizer.state "mlx.optimizers.Optimizer.state")   The optimizer\'s state dictionary.
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------
    :::

    Methods

    ::: pst-scrollable-table-container
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
      [[`Optimizer.apply_gradients`]](_autosummary/mlx.optimizers.Optimizer.apply_gradients.html#mlx.optimizers.Optimizer.apply_gradients "mlx.optimizers.Optimizer.apply_gradients")(gradients, parameters)   Apply the gradients to the parameters and return the updated parameters.
      [[`Optimizer.init`]](_autosummary/mlx.optimizers.Optimizer.init.html#mlx.optimizers.Optimizer.init "mlx.optimizers.Optimizer.init")(parameters)                                                          Initialize the optimizer\'s state
      [[`Optimizer.update`]](_autosummary/mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update "mlx.optimizers.Optimizer.update")(model, gradients)                                            Apply the gradients to the parameters of the model and update the model with the new parameters.
      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------
    :::

[](../optimizers.html "previous page")

previous

Optimizers

[](_autosummary/mlx.optimizers.Optimizer.state.html "next page")

next

mlx.optimizers.Optimizer.state

Contents

- [[`Optimizer`]](#mlx.optimizers.Optimizer)

By MLX Contributors

© Copyright 2023, Apple.\