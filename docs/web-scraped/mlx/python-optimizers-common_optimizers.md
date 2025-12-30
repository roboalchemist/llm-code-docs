# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/common_optimizers.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/optimizers/common_optimizers.rst "Download source file")
- [ ] [.pdf]

[ ]

# Common Optimizers

[]

# Common Optimizers[\#](#common-optimizers "Link to this heading")

  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------
  [[`SGD`]](_autosummary/mlx.optimizers.SGD.html#mlx.optimizers.SGD "mlx.optimizers.SGD")(learning_rate\[, momentum, weight_decay, \...\])                       The stochastic gradient descent optimizer.
  [[`RMSprop`]](_autosummary/mlx.optimizers.RMSprop.html#mlx.optimizers.RMSprop "mlx.optimizers.RMSprop")(learning_rate\[, alpha, eps\])                         The RMSprop optimizer \[1\].
  [[`Adagrad`]](_autosummary/mlx.optimizers.Adagrad.html#mlx.optimizers.Adagrad "mlx.optimizers.Adagrad")(learning_rate\[, eps\])                                The Adagrad optimizer \[1\].
  [[`Adafactor`]](_autosummary/mlx.optimizers.Adafactor.html#mlx.optimizers.Adafactor "mlx.optimizers.Adafactor")(\[learning_rate, eps, \...\])                  The Adafactor optimizer.
  [[`AdaDelta`]](_autosummary/mlx.optimizers.AdaDelta.html#mlx.optimizers.AdaDelta "mlx.optimizers.AdaDelta")(learning_rate\[, rho, eps\])                       The AdaDelta optimizer with a learning rate \[1\].
  [[`Adam`]](_autosummary/mlx.optimizers.Adam.html#mlx.optimizers.Adam "mlx.optimizers.Adam")(learning_rate\[, betas, eps, \...\])                               The Adam optimizer \[1\].
  [[`AdamW`]](_autosummary/mlx.optimizers.AdamW.html#mlx.optimizers.AdamW "mlx.optimizers.AdamW")(learning_rate\[, betas, eps, \...\])                           The AdamW optimizer \[1\].
  [[`Adamax`]](_autosummary/mlx.optimizers.Adamax.html#mlx.optimizers.Adamax "mlx.optimizers.Adamax")(learning_rate\[, betas, eps\])                             The Adamax optimizer, a variant of Adam based on the infinity norm \[1\].
  [[`Lion`]](_autosummary/mlx.optimizers.Lion.html#mlx.optimizers.Lion "mlx.optimizers.Lion")(learning_rate\[, betas, weight_decay\])                            The Lion optimizer \[1\].
  [[`MultiOptimizer`]](_autosummary/mlx.optimizers.MultiOptimizer.html#mlx.optimizers.MultiOptimizer "mlx.optimizers.MultiOptimizer")(optimizers\[, filters\])   Wraps a list of optimizers with corresponding weight predicates/filters to make it easy to use different optimizers for different weights.
  [[`Muon`]](_autosummary/mlx.optimizers.Muon.html#mlx.optimizers.Muon "mlx.optimizers.Muon")(learning_rate\[, momentum, \...\])                                 The Muon optimizer.
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------

[](_autosummary/mlx.optimizers.Optimizer.update.html "previous page")

previous

mlx.optimizers.Optimizer.update

[](_autosummary/mlx.optimizers.SGD.html "next page")

next

mlx.optimizers.SGD

By MLX Contributors

© Copyright 2023, Apple.\