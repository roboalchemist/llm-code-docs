# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.identity.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.identity.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.identity

## Contents

- [[`identity()`]](#mlx.nn.init.identity)

# mlx.nn.init.identity[\#](#mlx-nn-init-identity "Link to this heading")

[[identity]][(]*[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.identity "Link to this definition")

:   An initializer that returns an identity matrix.

    Parameters[:]

    :   **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Defaults: [`float32`].

    Returns[:]

    :   An initializer that returns an identity matrix with the same shape as the input.

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.identity()
        >>> init_fn(mx.zeros((2, 2)))
        array([[1, 0],
               [0, 1]], dtype=float32)
    :::
    ::::

[](mlx.nn.init.uniform.html "previous page")

previous

mlx.nn.init.uniform

[](mlx.nn.init.glorot_normal.html "next page")

next

mlx.nn.init.glorot_normal

Contents

- [[`identity()`]](#mlx.nn.init.identity)

By MLX Contributors

© Copyright 2023, Apple.\