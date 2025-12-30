# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.AvgPool3d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.AvgPool3d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.AvgPool3d

## Contents

- [[`AvgPool3d`]](#mlx.nn.AvgPool3d)

# mlx.nn.AvgPool3d[\#](#mlx-nn-avgpool3d "Link to this heading")

*[class][ ]*[[AvgPool3d]][(]*[[kernel_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[0]]*[)][\#](#mlx.nn.AvgPool3d "Link to this definition")

:   Applies 3-dimensional average pooling.

    Spatially downsamples the input by taking the average of a sliding window of size [`kernel_size`] and sliding stride [`stride`].

    The parameters [`kernel_size`], [`stride`], and [`padding`] can either be:

    - a single [`int`] -- in which case the same value is used for the depth, height, and width axis.

    - a [`tuple`] of three [`int`] s -- in which case, the first [`int`] is used for the depth axis, the second [`int`] for the height axis, and the third [`int`] for the width axis.

    Parameters[:]

    :   - **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The size of the pooling window.

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The stride of the pooling window. Default: [`kernel_size`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- How much zero padding to apply to the input. The padding is applied on both sides of the depth, height and width axis. Default: [`0`].

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn.layers as nn
        >>> x = mx.random.normal(shape=(8, 16, 32, 32, 4))
        >>> pool = nn.AvgPool3d(kernel_size=2, stride=2)
        >>> pool(x)
    :::
    ::::

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.AvgPool2d.html "previous page")

previous

mlx.nn.AvgPool2d

[](mlx.nn.BatchNorm.html "next page")

next

mlx.nn.BatchNorm

Contents

- [[`AvgPool3d`]](#mlx.nn.AvgPool3d)

By MLX Contributors

© Copyright 2023, Apple.\