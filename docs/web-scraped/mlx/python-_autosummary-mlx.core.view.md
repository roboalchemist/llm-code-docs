# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.view.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.view.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.view

## Contents

- [[`view()`]](#mlx.core.view)

# mlx.core.view[\#](#mlx-core-view "Link to this heading")

[[view]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.view "Link to this definition")

:   View the array as a different type.

    The output shape changes along the last axis if the input array's type and the input [`dtype`] do not have the same size.

    Note: the view op does not imply that the input and output arrays share their underlying data. The view only gaurantees that the binary representation of each element (or group of elements) is the same.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")) -- The data type to change to.

    Returns[:]

    :   The array with the new type.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.var.html "previous page")

previous

mlx.core.var

[](mlx.core.where.html "next page")

next

mlx.core.where

Contents

- [[`view()`]](#mlx.core.view)

By MLX Contributors

© Copyright 2023, Apple.\