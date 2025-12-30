# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eig.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.eig.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.eig

## Contents

- [[`eig()`]](#mlx.core.linalg.eig)

# mlx.core.linalg.eig[\#](#mlx-core-linalg-eig "Link to this heading")

[[eig]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.eig "Link to this definition")

:   Compute the eigenvalues and eigenvectors of a square matrix.

    This function differs from [[`numpy.linalg.eig()`]](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig "(in NumPy v2.3)") in that the return type is always complex even if the eigenvalues are all real.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues and eigenvectors are computed for each matrix in the last two dimensions.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   A tuple containing the eigenvalues and the normalized right eigenvectors. The column [`v[:,`]` `[`i]`] is the eigenvector corresponding to the i-th eigenvalue.

    Return type[:]

    :   *Tuple*\[[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    Example

    :::: 
    ::: highlight
        >>> A = mx.array([[1., -2.], [-2., 1.]])
        >>> w, v = mx.linalg.eig(A, stream=mx.cpu)
        >>> w
        array([3+0j, -1+0j], dtype=complex64)
        >>> v
        array([[0.707107+0j, 0.707107+0j],
               [-0.707107+0j, 0.707107+0j]], dtype=complex64)
    :::
    ::::

[](mlx.core.linalg.eigvals.html "previous page")

previous

mlx.core.linalg.eigvals

[](mlx.core.linalg.eigvalsh.html "next page")

next

mlx.core.linalg.eigvalsh

Contents

- [[`eig()`]](#mlx.core.linalg.eig)

By MLX Contributors

© Copyright 2023, Apple.\