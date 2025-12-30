# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.he_uniform.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.init.he_uniform.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.init.he_uniform

## Contents

- [[`he_uniform()`]](#mlx.nn.init.he_uniform)

# mlx.nn.init.he_uniform[\#](#mlx-nn-init-he-uniform "Link to this heading")

[[he_uniform]][(]*[[dtype]][[:]][ ][[[Dtype]](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")][ ][[=]][ ][[mlx.core.float32]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\[]][[\[]][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[Literal]](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")[[\[]][[\'fan_in\']][[,]][ ][[\'fan_out\']][[\]]][[,]][ ][[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[\]]][[,]][ ][[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.nn.init.he_uniform "Link to this definition")

:   A He uniform (Kaiming uniform) initializer.

    This initializer samples from a uniform distribution with a range computed from the number of input ([`fan_in`]) or output ([`fan_out`]) units according to:

    ::: 
    \\\[\\sigma = \\gamma \\sqrt}}\\\]
    :::

    where [\\(\\text\\)] is either the number of input units when the [`mode`] is [`"fan_in"`] or output units when the [`mode`] is [`"fan_out"`].

    For more details see the original reference: [Delving Deep into Rectifiers: Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852)

    Parameters[:]

    :   **dtype** ([*Dtype*](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the array. Default: [`float32`].

    Returns[:]

    :   An initializer that returns an array with the same shape as the input, filled with samples from the He uniform distribution.

    Return type[:]

    :   *Callable*\[\[[*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array"), [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")\], [*array*](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> init_fn = nn.init.he_uniform()
        >>> init_fn(mx.zeros((2, 2)))  # uses fan_in
        array([[0.0300242, -0.0184009],
               [0.793615, 0.666329]], dtype=float32)
        >>> init_fn(mx.zeros((2, 2)), mode="fan_out", gain=5)
        array([[-1.64331, -2.16506],
               [1.08619, 5.79854]], dtype=float32)
    :::
    ::::

[](mlx.nn.init.he_normal.html "previous page")

previous

mlx.nn.init.he_normal

[](../../optimizers.html "next page")

next

Optimizers

Contents

- [[`he_uniform()`]](#mlx.nn.init.he_uniform)

By MLX Contributors

© Copyright 2023, Apple.\