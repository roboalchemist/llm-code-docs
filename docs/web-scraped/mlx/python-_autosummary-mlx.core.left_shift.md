# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.left_shift.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.left_shift.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.left_shift

## Contents

- [[`left_shift()`]](#mlx.core.left_shift)

# mlx.core.left_shift[\#](#mlx-core-left-shift "Link to this heading")

[[left_shift]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.left_shift "Link to this definition")

:   Element-wise left shift.

    Shift the bits of the first input to the left by the second using numpy-style broadcasting semantics. Either or both input arrays can also be scalars.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

    Returns[:]

    :   The bitwise left shift [`a`]` `[`<<`]` `[`b`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.kron.html "previous page")

previous

mlx.core.kron

[](mlx.core.less.html "next page")

next

mlx.core.less

Contents

- [[`left_shift()`]](#mlx.core.left_shift)

By MLX Contributors

© Copyright 2023, Apple.\