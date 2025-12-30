# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.floor_divide.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.floor_divide.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.floor_divide

## Contents

- [[`floor_divide()`]](#mlx.core.floor_divide)

# mlx.core.floor_divide[\#](#mlx-core-floor-divide "Link to this heading")

[[floor_divide]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.floor_divide "Link to this definition")

:   Element-wise integer division.

    If either array is a floating point type then it is equivalent to calling [[`floor()`]](mlx.core.floor.html#mlx.core.floor "mlx.core.floor") after [[`divide()`]](mlx.core.divide.html#mlx.core.divide "mlx.core.divide").

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

    Returns[:]

    :   The quotient [`a`]` `[`//`]` `[`b`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.floor.html "previous page")

previous

mlx.core.floor

[](mlx.core.full.html "next page")

next

mlx.core.full

Contents

- [[`floor_divide()`]](#mlx.core.floor_divide)

By MLX Contributors

© Copyright 2023, Apple.\