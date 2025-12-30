# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.issubdtype.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.issubdtype.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.issubdtype

## Contents

- [[`issubdtype()`]](#mlx.core.issubdtype)

# mlx.core.issubdtype[\#](#mlx-core-issubdtype "Link to this heading")

[[issubdtype]][(]*[[arg1]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[DtypeCategory]](mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory")]*, *[[arg2]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[DtypeCategory]](mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory")]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][\#](#mlx.core.issubdtype "Link to this definition")

:   Check if a [[`Dtype`]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype") or [[`DtypeCategory`]](mlx.core.DtypeCategory.html#mlx.core.DtypeCategory "mlx.core.DtypeCategory") is a subtype of another.

    Parameters[:]

    :   - **(Union\[Dtype** (*arg2*) -- First dtype or category.

        - **DtypeCategory\]** -- First dtype or category.

        - **(Union\[Dtype** -- Second dtype or category.

        - **DtypeCategory\]** -- Second dtype or category.

    Returns[:]

    :   A boolean indicating if the first input is a subtype of the second input.

    Return type[:]

    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    Example

    :::: 
    ::: highlight
        >>> ints = mx.array([1, 2, 3], dtype=mx.int32)
        >>> mx.issubdtype(ints.dtype, mx.integer)
        True
        >>> mx.issubdtype(ints.dtype, mx.floating)
        False
    :::
    ::::

    :::: 
    ::: highlight
        >>> floats = mx.array([1, 2, 3], dtype=mx.float32)
        >>> mx.issubdtype(floats.dtype, mx.integer)
        False
        >>> mx.issubdtype(floats.dtype, mx.floating)
        True
    :::
    ::::

    Similar types of different sizes are not subdtypes of each other:

    :::: 
    ::: highlight
        >>> mx.issubdtype(mx.float64, mx.float32)
        False
        >>> mx.issubdtype(mx.float32, mx.float64)
        False
    :::
    ::::

    but both are subtypes of floating:

    :::: 
    ::: highlight
        >>> mx.issubdtype(mx.float64, mx.floating)
        True
        >>> mx.issubdtype(mx.float32, mx.floating)
        True
    :::
    ::::

    For convenience, dtype-like objects are allowed too:

    :::: 
    ::: highlight
        >>> mx.issubdtype(mx.float32, mx.inexact)
        True
        >>> mx.issubdtype(mx.signedinteger, mx.floating)
        False
    :::
    ::::

[](mlx.core.DtypeCategory.html "previous page")

previous

mlx.core.DtypeCategory

[](mlx.core.finfo.html "next page")

next

mlx.core.finfo

Contents

- [[`issubdtype()`]](#mlx.core.issubdtype)

By MLX Contributors

© Copyright 2023, Apple.\