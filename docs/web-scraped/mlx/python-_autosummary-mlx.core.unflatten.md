# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.unflatten.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.unflatten.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.unflatten

## Contents

- [[`unflatten()`]](#mlx.core.unflatten)

# mlx.core.unflatten[\#](#mlx-core-unflatten "Link to this heading")

[[unflatten]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.unflatten "Link to this definition")

:   Unflatten an axis of an array to a shape.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The axis to unflatten.

        - **shape** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The shape to unflatten to. At most one entry can be [`-1`] in which case the corresponding size will be inferred.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The unflattened array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Example

    :::: 
    ::: highlight
        >>> a = mx.array([1, 2, 3, 4])
        >>> mx.unflatten(a, 0, (2, -1))
        array([[1, 2], [3, 4]], dtype=int32)
    :::
    ::::

[](mlx.core.triu.html "previous page")

previous

mlx.core.triu

[](mlx.core.var.html "next page")

next

mlx.core.var

Contents

- [[`unflatten()`]](#mlx.core.unflatten)

By MLX Contributors

© Copyright 2023, Apple.\