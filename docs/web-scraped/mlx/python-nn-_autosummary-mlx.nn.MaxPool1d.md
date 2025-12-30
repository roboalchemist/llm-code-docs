# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.MaxPool1d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.MaxPool1d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.MaxPool1d

## Contents

- [[`MaxPool1d`]](#mlx.nn.MaxPool1d)

# mlx.nn.MaxPool1d[\#](#mlx-nn-maxpool1d "Link to this heading")

*[class][ ]*[[MaxPool1d]][(]*[[kernel_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[Tuple]](https://docs.python.org/3/library/typing.html#typing.Tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[0]]*[)][\#](#mlx.nn.MaxPool1d "Link to this definition")

:   Applies 1-dimensional max pooling.

    Spatially downsamples the input by taking the maximum of a sliding window of size [`kernel_size`] and sliding stride [`stride`].

    Parameters[:]

    :   - **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The size of the pooling window kernel.

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The stride of the pooling window. Default: [`kernel_size`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- How much negative infinity padding to apply to the input. The padding amount is applied to both sides of the spatial axis. Default: [`0`].

    Examples

    :::: 
    ::: highlight
        >>> import mlx.core as mx
        >>> import mlx.nn.layers as nn
        >>> x = mx.random.normal(shape=(4, 16, 5))
        >>> pool = nn.MaxPool1d(kernel_size=2, stride=2)
        >>> pool(x)
    :::
    ::::

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.LSTM.html "previous page")

previous

mlx.nn.LSTM

[](mlx.nn.MaxPool2d.html "next page")

next

mlx.nn.MaxPool2d

Contents

- [[`MaxPool1d`]](#mlx.nn.MaxPool1d)

By MLX Contributors

© Copyright 2023, Apple.\