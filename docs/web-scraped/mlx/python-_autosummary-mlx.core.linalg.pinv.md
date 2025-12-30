# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.pinv.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.pinv.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.pinv

## Contents

- [[`pinv()`]](#mlx.core.linalg.pinv)

# mlx.core.linalg.pinv[\#](#mlx-core-linalg-pinv "Link to this heading")

[[pinv]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.pinv "Link to this definition")

:   Compute the (Moore-Penrose) pseudo-inverse of a matrix.

    This function calculates a generalized inverse of a matrix using its singular-value decomposition. This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of [`a`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   [`aplus`] such that [`a`]` `[`@`]` `[`aplus`]` `[`@`]` `[`a`]` `[`=`]` `[`a`]

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.lu_factor.html "previous page")

previous

mlx.core.linalg.lu_factor

[](mlx.core.linalg.solve.html "next page")

next

mlx.core.linalg.solve

Contents

- [[`pinv()`]](#mlx.core.linalg.pinv)

By MLX Contributors

© Copyright 2023, Apple.\