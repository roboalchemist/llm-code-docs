# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.where.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.where.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.where

## Contents

- [[`where()`]](#mlx.core.where)

# mlx.core.where[\#](#mlx-core-where "Link to this heading")

[[where]][(]*[[condition]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[x]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[y]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.where "Link to this definition")

:   Select from [`x`] or [`y`] according to [`condition`].

    The condition and input arrays must be the same shape or broadcastable with each another.

    Parameters[:]

    :   - **condition** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The condition array.

        - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input selected from where condition is [`True`].

        - **y** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input selected from where condition is [`False`].

    Returns[:]

    :   The output containing elements selected from [`x`] and [`y`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.view.html "previous page")

previous

mlx.core.view

[](mlx.core.zeros.html "next page")

next

mlx.core.zeros

Contents

- [[`where()`]](#mlx.core.where)

By MLX Contributors

© Copyright 2023, Apple.\