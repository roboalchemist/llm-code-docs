# Source: https://ml-explore.github.io/mlx/build/html/python/nn/init.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/nn/init.rst "Download source file")
- [ ] [.pdf]

[ ]

# Initializers

[]

# Initializers[\#](#initializers "Link to this heading")

The [`mlx.nn.init`] package contains commonly used initializers for neural network parameters. Initializers return a function which can be applied to any input [[`mlx.core.array`]](../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array") to produce an initialized output.

For example:

    import mlx.core as mx
    import mlx.nn as nn

    init_fn = nn.init.uniform()

    # Produces a [2, 2] uniform matrix
    param = init_fn(mx.zeros((2, 2)))

To re-initialize all the parameter in an [[`mlx.nn.Module`]](module.html#mlx.nn.Module "mlx.nn.Module") from say a uniform distribution, you can do:

    import mlx.nn as nn
    model = nn.Sequential(nn.Linear(5, 10), nn.ReLU(), nn.Linear(10, 5))
    init_fn = nn.init.uniform(low=-0.1, high=0.1)
    model.apply(init_fn)

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------
  [[`constant`]](_autosummary/mlx.nn.init.constant.html#mlx.nn.init.constant "mlx.nn.init.constant")(value\[, dtype\])                    An initializer that returns an array filled with [`value`].
  [[`normal`]](_autosummary/mlx.nn.init.normal.html#mlx.nn.init.normal "mlx.nn.init.normal")(\[mean, std, dtype\])                        An initializer that returns samples from a normal distribution.
  [[`uniform`]](_autosummary/mlx.nn.init.uniform.html#mlx.nn.init.uniform "mlx.nn.init.uniform")(\[low, high, dtype\])                    An initializer that returns samples from a uniform distribution.
  [[`identity`]](_autosummary/mlx.nn.init.identity.html#mlx.nn.init.identity "mlx.nn.init.identity")(\[dtype\])                           An initializer that returns an identity matrix.
  [[`glorot_normal`]](_autosummary/mlx.nn.init.glorot_normal.html#mlx.nn.init.glorot_normal "mlx.nn.init.glorot_normal")(\[dtype\])       A Glorot normal initializer.
  [[`glorot_uniform`]](_autosummary/mlx.nn.init.glorot_uniform.html#mlx.nn.init.glorot_uniform "mlx.nn.init.glorot_uniform")(\[dtype\])   A Glorot uniform initializer.
  [[`he_normal`]](_autosummary/mlx.nn.init.he_normal.html#mlx.nn.init.he_normal "mlx.nn.init.he_normal")(\[dtype\])                       Build a He normal initializer.
  [[`he_uniform`]](_autosummary/mlx.nn.init.he_uniform.html#mlx.nn.init.he_uniform "mlx.nn.init.he_uniform")(\[dtype\])                   A He uniform (Kaiming uniform) initializer.
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------

[](_autosummary_functions/mlx.nn.losses.triplet_loss.html "previous page")

previous

mlx.nn.losses.triplet_loss

[](_autosummary/mlx.nn.init.constant.html "next page")

next

mlx.nn.init.constant

By MLX Contributors

© Copyright 2023, Apple.\