# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stop_gradient.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.stop_gradient.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.stop_gradient

## Contents

- [[`stop_gradient()`]](#mlx.core.stop_gradient)

# mlx.core.stop_gradient[\#](#mlx-core-stop-gradient "Link to this heading")

[[stop_gradient]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.stop_gradient "Link to this definition")

:   Stop gradients from being computed.

    The operation is the identity but it prevents gradients from flowing through the array.

    Parameters[:]

    :   **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

    Returns[:]

    :   The unchanged input [`a`] but without gradient flowing through it.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.std.html "previous page")

previous

mlx.core.std

[](mlx.core.subtract.html "next page")

next

mlx.core.subtract

Contents

- [[`stop_gradient()`]](#mlx.core.stop_gradient)

By MLX Contributors

© Copyright 2023, Apple.\