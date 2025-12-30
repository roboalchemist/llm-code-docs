# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.solve.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.solve.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.solve

## Contents

- [[`solve()`]](#mlx.core.linalg.solve)

# mlx.core.linalg.solve[\#](#mlx-core-linalg-solve "Link to this heading")

[[solve]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.solve "Link to this definition")

:   Compute the solution to a system of linear equations [`AX`]` `[`=`]` `[`B`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The unique solution to the system [`AX`]` `[`=`]` `[`B`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.pinv.html "previous page")

previous

mlx.core.linalg.pinv

[](mlx.core.linalg.solve_triangular.html "next page")

next

mlx.core.linalg.solve_triangular

Contents

- [[`solve()`]](#mlx.core.linalg.solve)

By MLX Contributors

© Copyright 2023, Apple.\