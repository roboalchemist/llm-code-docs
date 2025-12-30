# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.qr.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.qr.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.qr

## Contents

- [[`qr()`]](#mlx.core.linalg.qr)

# mlx.core.linalg.qr[\#](#mlx-core-linalg-qr "Link to this heading")

[[qr]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.qr "Link to this definition")

:   The QR factorization of the input matrix.

    This function supports arrays with at least 2 dimensions. The matrices which are factorized are assumed to be in the last two dimensions of the input.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   [`Q`] and [`R`] matrices such that [`Q`]` `[`@`]` `[`R`]` `[`=`]` `[`a`].

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

    Example

    :::: 
    ::: highlight
        >>> A = mx.array([[2., 3.], [1., 2.]])
        >>> Q, R = mx.linalg.qr(A, stream=mx.cpu)
        >>> Q
        array([[-0.894427, -0.447214],
               [-0.447214, 0.894427]], dtype=float32)
        >>> R
        array([[-2.23607, -3.57771],
               [0, 0.447214]], dtype=float32)
    :::
    ::::

[](mlx.core.linalg.cross.html "previous page")

previous

mlx.core.linalg.cross

[](mlx.core.linalg.svd.html "next page")

next

mlx.core.linalg.svd

Contents

- [[`qr()`]](#mlx.core.linalg.qr)

By MLX Contributors

© Copyright 2023, Apple.\