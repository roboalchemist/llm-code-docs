# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.set_dtype.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Module.set_dtype.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Module.set_dtype

## Contents

- [[`Module.set_dtype()`]](#mlx.nn.Module.set_dtype)

# mlx.nn.Module.set_dtype[\#](#mlx-nn-module-set-dtype "Link to this heading")

[[Module.]][[set_dtype]][(]*[dtype:] [\~mlx.core.Dtype,] [predicate:] [\~typing.Callable\[\[\~mlx.core.Dtype\],] [bool\]] [\|] [None] [=] [\<function] [Module.\<lambda\>\>]*[)][\#](#mlx.nn.Module.set_dtype "Link to this definition")

:   Set the dtype of the module's parameters.

    Parameters[:]

    :   - **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")) -- The new dtype.

        - **predicate** ([*Callable*](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")*,* *optional*) -- A predicate to select parameters to cast. By default, only parameters of type [`floating`] will be updated to avoid casting integer parameters to the new dtype.

[](mlx.nn.Module.save_weights.html "previous page")

previous

mlx.nn.Module.save_weights

[](mlx.nn.Module.train.html "next page")

next

mlx.nn.Module.train

Contents

- [[`Module.set_dtype()`]](#mlx.nn.Module.set_dtype)

By MLX Contributors

© Copyright 2023, Apple.\