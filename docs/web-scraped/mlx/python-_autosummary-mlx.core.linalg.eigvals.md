# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigvals.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.eigvals.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.eigvals

## Contents

- [[`eigvals()`]](#mlx.core.linalg.eigvals)

# mlx.core.linalg.eigvals[\#](#mlx-core-linalg-eigvals "Link to this heading")

[[eigvals]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.eigvals "Link to this definition")

:   Compute the eigenvalues of a square matrix.

    This function differs from [[`numpy.linalg.eigvals()`]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals "(in NumPy v2.3)") in that the return type is always complex even if the eigenvalues are all real.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues are computed for each matrix in the last two dimensions.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The eigenvalues (not necessarily in order).

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Example

    :::: 
    ::: highlight
        >>> A = mx.array([[1., -2.], [-2., 1.]])
        >>> eigenvalues = mx.linalg.eigvals(A, stream=mx.cpu)
        >>> eigenvalues
        array([3+0j, -1+0j], dtype=complex64)
    :::
    ::::

[](mlx.core.linalg.svd.html "previous page")

previous

mlx.core.linalg.svd

[](mlx.core.linalg.eig.html "next page")

next

mlx.core.linalg.eig

Contents

- [[`eigvals()`]](#mlx.core.linalg.eigvals)

By MLX Contributors

© Copyright 2023, Apple.\