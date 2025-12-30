# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cholesky.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.cholesky.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.cholesky

## Contents

- [[`cholesky()`]](#mlx.core.linalg.cholesky)

# mlx.core.linalg.cholesky[\#](#mlx-core-linalg-cholesky "Link to this heading")

[[cholesky]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[upper]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linalg.cholesky "Link to this definition")

:   Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the Cholesky decomposition is computed for each matrix in the last two dimensions of [`a`].

    If the input matrix is not symmetric positive semi-definite, behaviour is undefined.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **upper** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`], return the upper triangular Cholesky factor. If [`False`], return the lower triangular Cholesky factor. Default: [`False`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   If [`upper`]` `[`=`]` `[`False`], it returns a lower triangular [`L`] matrix such that [`L`]` `[`@`]` `[`L.T`]` `[`=`]` `[`a`]. If [`upper`]` `[`=`]` `[`True`], it returns an upper triangular [`U`] matrix such that [`U.T`]` `[`@`]` `[`U`]` `[`=`]` `[`a`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.linalg.norm.html "previous page")

previous

mlx.core.linalg.norm

[](mlx.core.linalg.cholesky_inv.html "next page")

next

mlx.core.linalg.cholesky_inv

Contents

- [[`cholesky()`]](#mlx.core.linalg.cholesky)

By MLX Contributors

© Copyright 2023, Apple.\