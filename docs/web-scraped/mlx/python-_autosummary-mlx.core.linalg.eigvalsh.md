# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigvalsh.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.eigvalsh.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.eigvalsh

## Contents

- [[`eigvalsh()`]](#mlx.core.linalg.eigvalsh)

# mlx.core.linalg.eigvalsh[\#](#mlx-core-linalg-eigvalsh "Link to this heading")

[[eigvalsh]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[UPLO]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'L\']]*, *[[\*]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.eigvalsh "Link to this definition")

:   Compute the eigenvalues of a complex Hermitian or real symmetric matrix.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues are computed for each matrix in the last two dimensions.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array. Must be a real symmetric or complex Hermitian matrix.

        - **UPLO** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Whether to use the upper ([`"U"`]) or lower ([`"L"`]) triangle of the matrix. Default: [`"L"`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The eigenvalues in ascending order.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    ::: 
    Note

    The input matrix is assumed to be symmetric (or Hermitian). Only the selected triangle is used. No checks for symmetry are performed.
    :::

    Example

    :::: 
    ::: highlight
        >>> A = mx.array([[1., -2.], [-2., 1.]])
        >>> eigenvalues = mx.linalg.eigvalsh(A, stream=mx.cpu)
        >>> eigenvalues
        array([-1., 3.], dtype=float32)
    :::
    ::::

[](mlx.core.linalg.eig.html "previous page")

previous

mlx.core.linalg.eig

[](mlx.core.linalg.eigh.html "next page")

next

mlx.core.linalg.eigh

Contents

- [[`eigvalsh()`]](#mlx.core.linalg.eigvalsh)

By MLX Contributors

© Copyright 2023, Apple.\