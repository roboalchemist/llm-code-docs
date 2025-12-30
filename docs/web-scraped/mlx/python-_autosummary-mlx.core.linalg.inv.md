# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.inv.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.inv.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.inv

## Contents

- [[`inv()`]](#mlx.core.linalg.inv)

# mlx.core.linalg.inv[\#](#mlx-core-linalg-inv "Link to this heading")

[[inv]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.inv "Link to this definition")

:   Compute the inverse of a square matrix.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the inverse is computed for each matrix in the last two dimensions of [`a`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   [`ainv`] such that [`dot(a,`]` `[`ainv)`]` `[`=`]` `[`dot(ainv,`]` `[`a)`]` `[`=`]` `[`eye(a.shape[0])`]

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](../linalg.html "previous page")

previous

Linear Algebra

[](mlx.core.linalg.tri_inv.html "next page")

next

mlx.core.linalg.tri_inv

Contents

- [[`inv()`]](#mlx.core.linalg.inv)

By MLX Contributors

© Copyright 2023, Apple.\