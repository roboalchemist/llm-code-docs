# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.svd.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.svd.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.svd

## Contents

- [[`svd()`]](#mlx.core.linalg.svd)

# mlx.core.linalg.svd[\#](#mlx-core-linalg-svd "Link to this heading")

[[svd]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[compute_uv]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.svd "Link to this definition")

:   The Singular Value Decomposition (SVD) of the input matrix.

    This function supports arrays with at least 2 dimensions. When the input has more than two dimensions, the function iterates over all indices of the first a.ndim - 2 dimensions and for each combination SVD is applied to the last two indices.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **compute_uv** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`], return the [`U`], [`S`], and [`Vt`] components. If [`False`], return only the [`S`] array. Default: [`True`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   If compute_uv is [`True`] returns the [`U`], [`S`], and [`Vt`] matrices, such that [`A`]` `[`=`]` `[`U`]` `[`@`]` `[`diag(S)`]` `[`@`]` `[`Vt`]. If compute_uv is [`False`] returns singular values array [`S`].

    Return type[:]

    :   *Union*\[[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), ...), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")\]

[](mlx.core.linalg.qr.html "previous page")

previous

mlx.core.linalg.qr

[](mlx.core.linalg.eigvals.html "next page")

next

mlx.core.linalg.eigvals

Contents

- [[`svd()`]](#mlx.core.linalg.svd)

By MLX Contributors

© Copyright 2023, Apple.\