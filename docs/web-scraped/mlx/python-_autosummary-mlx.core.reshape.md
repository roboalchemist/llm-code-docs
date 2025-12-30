# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.reshape.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.reshape.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.reshape

## Contents

- [[`reshape()`]](#mlx.core.reshape)

# mlx.core.reshape[\#](#mlx-core-reshape "Link to this heading")

[[reshape]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.reshape "Link to this definition")

:   Reshape an array while preserving the size.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **shape** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- New shape.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The reshaped array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.repeat.html "previous page")

previous

mlx.core.repeat

[](mlx.core.right_shift.html "next page")

next

mlx.core.right_shift

Contents

- [[`reshape()`]](#mlx.core.reshape)

By MLX Contributors

© Copyright 2023, Apple.\