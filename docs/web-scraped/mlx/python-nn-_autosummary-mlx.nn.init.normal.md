# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.normal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.normal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.normal

## Contents

- [[`normal()`]](#mlx.nn.init.normal)

# mlx.nn.init.normal[\#](#mlx-nn-init-normal "Link to this heading")

[[normal]][(]*[[mean]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[std]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.normal "Link to this definition")

:   An initializer that returns samples from a normal distribution.

    Parameters[:]

    :   - **mean** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Mean of the normal distribution. Default: [`0.0`].

        - **std** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Standard deviation of the normal distribution. Default: [`1.0`].

        - **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Default: [`float32`].

    Returns[:]

    :   An initializer that returns an array with the same shape as the input, filled with samples from a normal distribution.

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.normal()
        >>> init_fn(mx.zeros((2, 2)))
        array([[-0.982273, -0.534422],
               [0.380709, 0.0645099]], dtype=float32)
    :::
    ::::

[](mlx.nn.init.constant.html "previous page")

previous

mlx.nn.init.constant

[](mlx.nn.init.uniform.html "next page")

next

mlx.nn.init.uniform

Contents

- [[`normal()`]](#mlx.nn.init.normal)

By MLX Contributors

© Copyright 2023, Apple.\