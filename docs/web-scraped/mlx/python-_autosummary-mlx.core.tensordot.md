# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.tensordot.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.tensordot.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.tensordot

## Contents

- [[`tensordot()`]](#mlx.core.tensordot)

# mlx.core.tensordot[\#](#mlx-core-tensordot "Link to this heading")

[[tensordot]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axes]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][[\]]]][ ][[=]][ ][[2]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.tensordot "Link to this definition")

:   Compute the tensor dot product along the specified axes.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **axes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)),* *optional*) -- The number of dimensions to sum over. If an integer is provided, then sum over the last [`axes`] dimensions of [`a`] and the first [`axes`] dimensions of [`b`]. If a list of lists is provided, then sum over the corresponding dimensions of [`a`] and [`b`]. Default: 2.

    Returns[:]

    :   The tensor dot product.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.tanh.html "previous page")

previous

mlx.core.tanh

[](mlx.core.tile.html "next page")

next

mlx.core.tile

Contents

- [[`tensordot()`]](#mlx.core.tensordot)

By MLX Contributors

© Copyright 2023, Apple.\