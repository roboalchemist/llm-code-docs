# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.solve_triangular.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.solve_triangular.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.solve_triangular

## Contents

- [[`solve_triangular()`]](#mlx.core.linalg.solve_triangular)

# mlx.core.linalg.solve_triangular[\#](#mlx-core-linalg-solve-triangular "Link to this heading")

[[solve_triangular]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[upper]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.solve_triangular "Link to this definition")

:   Computes the solution of a triangular system of linear equations [`AX`]` `[`=`]` `[`B`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether the array is upper or lower triangular. Default: [`False`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The unique solution to the system [`AX`]` `[`=`]` `[`B`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.solve.html "previous page")

previous

mlx.core.linalg.solve

[](../metal.html "next page")

next

Metal

Contents

- [[`solve_triangular()`]](#mlx.core.linalg.solve_triangular)

By MLX Contributors

© Copyright 2023, Apple.\