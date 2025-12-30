# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.uniform.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.uniform.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.uniform

## Contents

- [[`uniform()`]](#mlx.nn.init.uniform)

# mlx.nn.init.uniform[\#](#mlx-nn-init-uniform "Link to this heading")

[[uniform]][(]*[[low]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*, *[[high]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.uniform "Link to this definition")

:   An initializer that returns samples from a uniform distribution.

    Parameters[:]

    :   - **low** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The lower bound of the uniform distribution. Default: [`0.0`].

        - **high** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The upper bound of the uniform distribution. Default: [`1.0`]

        - **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Default: [`float32`].

    Returns[:]

    :   An initializer that returns an array with the same shape as the input, filled with samples from a uniform distribution

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.uniform(low=0, high=1)
        >>> init_fn(mx.zeros((2, 2)))
        array([[0.883935, 0.863726],
               [0.617261, 0.417497]], dtype=float32)
    :::
    ::::

[](mlx.nn.init.normal.html "previous page")

previous

mlx.nn.init.normal

[](mlx.nn.init.identity.html "next page")

next

mlx.nn.init.identity

Contents

- [[`uniform()`]](#mlx.nn.init.uniform)

By MLX Contributors

© Copyright 2023, Apple.\