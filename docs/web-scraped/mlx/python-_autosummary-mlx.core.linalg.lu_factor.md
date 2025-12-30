# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.lu_factor.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.lu_factor.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.lu_factor

## Contents

- [[`lu_factor()`]](#mlx.core.linalg.lu_factor)

# mlx.core.linalg.lu_factor[\#](#mlx-core-linalg-lu-factor "Link to this heading")

[[lu_factor]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.lu_factor "Link to this definition")

:   Computes a compact representation of the LU factorization.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The [`LU`] matrix and [`pivots`] array.

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

[](mlx.core.linalg.lu.html "previous page")

previous

mlx.core.linalg.lu

[](mlx.core.linalg.pinv.html "next page")

next

mlx.core.linalg.pinv

Contents

- [[`lu_factor()`]](#mlx.core.linalg.lu_factor)

By MLX Contributors

© Copyright 2023, Apple.\