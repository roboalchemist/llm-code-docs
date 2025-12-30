# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.diag.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.diag.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.diag

## Contents

- [[`diag()`]](#mlx.core.diag)

# mlx.core.diag[\#](#mlx-core-diag "Link to this heading")

[[diag]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[k]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.diag "Link to this definition")

:   Extract a diagonal or construct a diagonal matrix. If [`a`] is 1-D then a diagonal matrix is constructed with [`a`] on the [\\(k\\)]-th diagonal. If [`a`] is 2-D then the [\\(k\\)]-th diagonal is returned.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- 1-D or 2-D input array.

        - **k** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The diagonal to extract or construct. Default: [`0`].

    Returns[:]

    :   The extracted diagonal or the constructed diagonal matrix.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.dequantize.html "previous page")

previous

mlx.core.dequantize

[](mlx.core.diagonal.html "next page")

next

mlx.core.diagonal

Contents

- [[`diag()`]](#mlx.core.diag)

By MLX Contributors

© Copyright 2023, Apple.\