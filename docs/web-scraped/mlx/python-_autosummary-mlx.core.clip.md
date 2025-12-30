# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.clip.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.clip.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.clip

## Contents

- [[`clip()`]](#mlx.core.clip)

# mlx.core.clip[\#](#mlx-core-clip "Link to this heading")

[[clip]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[a_min]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[a_max]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.clip "Link to this definition")

:   Clip the values of the array between the given minimum and maximum.

    If either [`a_min`] or [`a_max`] are [`None`], then corresponding edge is ignored. At least one of [`a_min`] and [`a_max`] cannot be [`None`]. The input [`a`] and the limits must broadcast with one another.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **a_min** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array") *or* *None*) -- Minimum value to clip to.

        - **a_max** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array") *or* *None*) -- Maximum value to clip to.

    Returns[:]

    :   The clipped array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.ceil.html "previous page")

previous

mlx.core.ceil

[](mlx.core.concatenate.html "next page")

next

mlx.core.concatenate

Contents

- [[`clip()`]](#mlx.core.clip)

By MLX Contributors

© Copyright 2023, Apple.\