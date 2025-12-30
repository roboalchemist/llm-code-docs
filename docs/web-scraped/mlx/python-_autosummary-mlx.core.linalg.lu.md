# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.lu.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linalg.lu.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linalg.lu

## Contents

- [[`lu()`]](#mlx.core.linalg.lu)

# mlx.core.linalg.lu[\#](#mlx-core-linalg-lu "Link to this heading")

[[lu]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[Tuple][[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.linalg.lu "Link to this definition")

:   Compute the LU factorization of the given matrix [`A`].

    Note, unlike the default behavior of [`scipy.linalg.lu`], the pivots are indices. To reconstruct the input use [`L[P,`]` `[`:]`]` `[`@`]` `[`U`] for 2 dimensions or [`mx.take_along_axis(L,`]` `[`P[...,`]` `[`None],`]` `[`axis=-2)`]` `[`@`]` `[`U`] for more than 2 dimensions.

    To construct the full permuation matrix do:

    :::: 
    ::: highlight
        P = mx.put_along_axis(mx.zeros_like(L), p[..., None], mx.array(1.0), axis=-1)
    :::
    ::::

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The [`p`], [`L`], and [`U`] arrays, such that [`A`]` `[`=`]` `[`L[P,`]` `[`:]`]` `[`@`]` `[`U`]

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

[](mlx.core.linalg.eigh.html "previous page")

previous

mlx.core.linalg.eigh

[](mlx.core.linalg.lu_factor.html "next page")

next

mlx.core.linalg.lu_factor

Contents

- [[`lu()`]](#mlx.core.linalg.lu)

By MLX Contributors

© Copyright 2023, Apple.\