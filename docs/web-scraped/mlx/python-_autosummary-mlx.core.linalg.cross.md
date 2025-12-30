# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cross.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.cross.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.cross

## Contents

- [[`cross()`]](#mlx.core.linalg.cross)

# mlx.core.linalg.cross[\#](#mlx-core-linalg-cross "Link to this heading")

[[cross]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.cross "Link to this definition")

:   Compute the cross product of two arrays along a specified axis.

    The cross product is defined for arrays with size 2 or 3 in the specified axis. If the size is 2 then the third value is assumed to be zero.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis along which to compute the cross product. Default: [`-1`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The cross product of [`a`] and [`b`] along the specified axis.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.cholesky_inv.html "previous page")

previous

mlx.core.linalg.cholesky_inv

[](mlx.core.linalg.qr.html "next page")

next

mlx.core.linalg.qr

Contents

- [[`cross()`]](#mlx.core.linalg.cross)

By MLX Contributors

© Copyright 2023, Apple.\