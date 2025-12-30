# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.he_normal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.he_normal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.he_normal

## Contents

- [[`he_normal()`]](#mlx.nn.init.he_normal)

# mlx.nn.init.he_normal[\#](#mlx-nn-init-he-normal "Link to this heading")

[[he_normal]][(]*[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'fan_in\']][[,]][ ][[\'fan_out\']][[\]]][[,]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.he_normal "Link to this definition")

:   Build a He normal initializer.

    This initializer samples from a normal distribution with a standard deviation computed from the number of input ([`fan_in`]) or output ([`fan_out`]) units according to:

    ::: 
    \\\[\\sigma = \\gamma \\frac}}\\\]
    :::

    where [\\(\\text\\)] is either the number of input units when the [`mode`] is [`"fan_in"`] or output units when the [`mode`] is [`"fan_out"`].

    For more details see the original reference: [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852)

    Parameters[:]

    :   **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Defaults to mx.float32.

    Returns[:]

    :   An initializer that returns an array with the same shape as the input, filled with samples from the He normal distribution.

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.he_normal()
        >>> init_fn(mx.zeros((2, 2)))  # uses fan_in
        array([[-1.25211, 0.458835],
               [-0.177208, -0.0137595]], dtype=float32)
        >>> init_fn(mx.zeros((2, 2)), mode="fan_out", gain=5)
        array([[5.6967, 4.02765],
               [-4.15268, -2.75787]], dtype=float32)
    :::
    ::::

[](mlx.nn.init.glorot_uniform.html "previous page")

previous

mlx.nn.init.glorot_uniform

[](mlx.nn.init.he_uniform.html "next page")

next

mlx.nn.init.he_uniform

Contents

- [[`he_normal()`]](#mlx.nn.init.he_normal)

By MLX Contributors

© Copyright 2023, Apple.\