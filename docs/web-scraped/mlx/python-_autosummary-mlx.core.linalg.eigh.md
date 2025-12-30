# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigh.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.eigh.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.eigh

## Contents

- [[`eigh()`]](#mlx.core.linalg.eigh)

# mlx.core.linalg.eigh[\#](#mlx-core-linalg-eigh "Link to this heading")

[[eigh]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[UPLO]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'L\']]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.eigh "Link to this definition")

:   Compute the eigenvalues and eigenvectors of a complex Hermitian or real symmetric matrix.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the eigenvalues and eigenvectors are computed for each matrix in the last two dimensions.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array. Must be a real symmetric or complex Hermitian matrix.

        - **UPLO** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Whether to use the upper ([`"U"`]) or lower ([`"L"`]) triangle of the matrix. Default: [`"L"`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   A tuple containing the eigenvalues in ascending order and the normalized eigenvectors. The column [`v[:,`]` `[`i]`] is the eigenvector corresponding to the i-th eigenvalue.

    Return type[:]

    :   *Tuple*\[[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")\]

    ::: 
    Note

    The input matrix is assumed to be symmetric (or Hermitian). Only the selected triangle is used. No checks for symmetry are performed.
    :::

    Example

    :::: 
    ::: highlight
        >>> A = mx.array([[1., -2.], [-2., 1.]])
        >>> w, v = mx.linalg.eigh(A, stream=mx.cpu)
        >>> w
        array([-1., 3.], dtype=float32)
        >>> v
        array([[ 0.707107, -0.707107],
              [ 0.707107,  0.707107]], dtype=float32)
    :::
    ::::

[](mlx.core.linalg.eigvalsh.html "previous page")

previous

mlx.core.linalg.eigvalsh

[](mlx.core.linalg.lu.html "next page")

next

mlx.core.linalg.lu

Contents

- [[`eigh()`]](#mlx.core.linalg.eigh)

By MLX Contributors

© Copyright 2023, Apple.\