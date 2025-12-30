# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.round.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.round.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.round

## Contents

- [[`round()`]](#mlx.core.round)

# mlx.core.round[\#](#mlx-core-round "Link to this heading")

[[round]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[decimals]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.round "Link to this definition")

:   Round to the given number of decimals.

    Basically performs:

    :::: 
    ::: highlight
        s = 10**decimals
        x = round(x * s) / s
    :::
    ::::

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **decimals** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Number of decimal places to round to. (default: 0)

    Returns[:]

    :   An array of the same type as [`a`] rounded to the given number of decimals.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.roll.html "previous page")

previous

mlx.core.roll

[](mlx.core.rsqrt.html "next page")

next

mlx.core.rsqrt

Contents

- [[`round()`]](#mlx.core.round)

By MLX Contributors

© Copyright 2023, Apple.\