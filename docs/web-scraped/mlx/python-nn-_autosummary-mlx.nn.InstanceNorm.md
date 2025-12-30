# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.InstanceNorm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.InstanceNorm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.InstanceNorm

## Contents

- [[`InstanceNorm`]](#mlx.nn.InstanceNorm)

# mlx.nn.InstanceNorm[\#](#mlx-nn-instancenorm "Link to this heading")

*[class][ ]*[[InstanceNorm]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-05]]*, *[[affine]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.nn.InstanceNorm "Link to this definition")

:   Applies instance normalization \[1\] on the inputs.

    Computes

    ::: 
    \\\[y = \\frac\[x\]}\[x\] + \\epsilon}} \* \\gamma + \\beta,\\\]
    :::

    where [\\(\\gamma\\)] and [\\(\\beta\\)] are learned per feature dimension parameters initialized at 1 and 0 respectively. Both are of size [`dims`], if [`affine`] is [`True`].

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of features of the input.

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- A value added to the denominator for numerical stability. Default: [`1e-5`].

        - **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Default: [`False`].

    Shape:

    :   - Input: [\\((\..., C)\\)] where [\\(C\\)] is equal to [`dims`].

        - Output: Same shape as the input.

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn as nn
        >>> x = mx.random.normal((8, 4, 4, 16))
        >>> inorm = nn.InstanceNorm(dims=16)
        >>> output = inorm(x)
    :::
    ::::

    References

    \[1\]: [https://arxiv.org/abs/1607.08022](https://arxiv.org/abs/1607.08022)

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.Hardswish.html "previous page")

previous

mlx.nn.Hardswish

[](mlx.nn.LayerNorm.html "next page")

next

mlx.nn.LayerNorm

Contents

- [[`InstanceNorm`]](#mlx.nn.InstanceNorm)

By MLX Contributors

© Copyright 2023, Apple.\