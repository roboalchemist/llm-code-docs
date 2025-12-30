# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cholesky_inv.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.cholesky_inv.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.cholesky_inv

## Contents

- [[`cholesky_inv()`]](#mlx.core.linalg.cholesky_inv)

# mlx.core.linalg.cholesky_inv[\#](#mlx-core-linalg-cholesky-inv "Link to this heading")

[[cholesky_inv]][(]*[[L]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[upper]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.cholesky_inv "Link to this definition")

:   Compute the inverse of a real symmetric positive semi-definite matrix using it's Cholesky decomposition.

    Let [\\(\\mathbf\\)] be a real symmetric positive semi-definite matrix and [\\(\\mathbf\\)] its Cholesky decomposition such that:

    ::: 
    \\\[\\begin \\mathbf = \\mathbf\\mathbf\^T \\end\\\]
    :::

    This function computes [\\(\\mathbf\^\\)].

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the Cholesky inverse is computed for each matrix in the last two dimensions of [\\(\\mathbf\\)].

    If the input matrix is not a triangular matrix behaviour is undefined.

    Parameters[:]

    :   - **L** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`], return the upper triangular Cholesky factor. If [`False`], return the lower triangular Cholesky factor. Default: [`False`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   [\\(\\mathbf}\\)] where [\\(\\mathbf = \\mathbf\\mathbf\^T\\)].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.cholesky.html "previous page")

previous

mlx.core.linalg.cholesky

[](mlx.core.linalg.cross.html "next page")

next

mlx.core.linalg.cross

Contents

- [[`cholesky_inv()`]](#mlx.core.linalg.cholesky_inv)

By MLX Contributors

© Copyright 2023, Apple.\