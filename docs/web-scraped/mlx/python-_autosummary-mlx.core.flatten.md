# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.flatten.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.flatten.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.flatten

## Contents

- [[`flatten()`]](#mlx.core.flatten)

# mlx.core.flatten[\#](#mlx-core-flatten "Link to this heading")

[[flatten]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[start_axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[end_axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.flatten "Link to this definition")

:   Flatten an array.

    The axes flattened will be between [`start_axis`] and [`end_axis`], inclusive. Negative axes are supported. After converting negative axis to positive, axes outside the valid range will be clamped to a valid value, [`start_axis`] to [`0`] and [`end_axis`] to [`ndim`]` `[`-`]` `[`1`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **start_axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The first dimension to flatten. Defaults to [`0`].

        - **end_axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The last dimension to flatten. Defaults to [`-1`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The flattened array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Example

    :::: 
    ::: highlight
        >>> a = mx.array([[1, 2], [3, 4]])
        >>> mx.flatten(a)
        array([1, 2, 3, 4], dtype=int32)
        >>>
        >>> mx.flatten(a, start_axis=0, end_axis=-1)
        array([1, 2, 3, 4], dtype=int32)
    :::
    ::::

[](mlx.core.eye.html "previous page")

previous

mlx.core.eye

[](mlx.core.floor.html "next page")

next

mlx.core.floor

Contents

- [[`flatten()`]](#mlx.core.flatten)

By MLX Contributors

© Copyright 2023, Apple.\