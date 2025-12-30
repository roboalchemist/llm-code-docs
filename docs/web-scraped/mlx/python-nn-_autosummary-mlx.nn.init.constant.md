# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.constant.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.constant.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.constant

## Contents

- [[`constant()`]](#mlx.nn.init.constant)

# mlx.nn.init.constant[\#](#mlx-nn-init-constant "Link to this heading")

[[constant]][(]*[[value]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.constant "Link to this definition")

:   An initializer that returns an array filled with [`value`].

    Parameters[:]

    :   - **value** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- The value to fill the array with.

        - **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Default: [`float32`].

    Returns[:]

    :   An initializer that returns an array with the same shape as the input, filled with [`value`].

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.constant(0.5)
        >>> init_fn(mx.zeros((2, 2)))
        array([[0.5, 0.5],
               [0.5, 0.5]], dtype=float32)
    :::
    ::::

[](../init.html "previous page")

previous

Initializers

[](mlx.nn.init.normal.html "next page")

next

mlx.nn.init.normal

Contents

- [[`constant()`]](#mlx.nn.init.constant)

By MLX Contributors

© Copyright 2023, Apple.\