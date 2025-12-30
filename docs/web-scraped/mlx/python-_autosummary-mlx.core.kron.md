# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.kron.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.kron.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.kron

## Contents

- [[`kron()`]](#mlx.core.kron)

# mlx.core.kron[\#](#mlx-core-kron "Link to this heading")

[[kron]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.kron "Link to this definition")

:   Compute the Kronecker product of two arrays [`a`] and [`b`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The first input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The second input array.

        - **stream** (*Union\[None,* [*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* [*Device*](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")*\],* *optional*) -- Optional stream or device for execution. Default: [`None`].

    Returns[:]

    :   The Kronecker product of [`a`] and [`b`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Examples

    :::: 
    ::: highlight
        >>> a = mx.array([[1, 2], [3, 4]])
        >>> b = mx.array([[0, 5], [6, 7]])
        >>> result = mx.kron(a, b)
        >>> print(result)
        array([[0, 5, 0, 10],
               [6, 7, 12, 14],
               [0, 15, 0, 20],
               [18, 21, 24, 28]], dtype=int32)
    :::
    ::::

[](mlx.core.isposinf.html "previous page")

previous

mlx.core.isposinf

[](mlx.core.left_shift.html "next page")

next

mlx.core.left_shift

Contents

- [[`kron()`]](#mlx.core.kron)

By MLX Contributors

© Copyright 2023, Apple.\