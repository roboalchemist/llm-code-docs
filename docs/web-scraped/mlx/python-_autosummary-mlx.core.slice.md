# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.slice.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.slice.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.slice

## Contents

- [[`slice()`]](#mlx.core.slice)

# mlx.core.slice[\#](#mlx-core-slice "Link to this heading")

[[slice]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[start_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axes]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[slice_size]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.slice "Link to this definition")

:   Extract a sub-array from the input array.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **start_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The index location to start the slice at.

        - **axes** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The axes corresponding to the indices in [`start_indices`].

        - **slice_size** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The size of the slice.

    Returns[:]

    :   The sliced output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Example

    :::: 
    ::: highlight
        >>> a = mx.array([[1, 2, 3], [4, 5, 6]])
        >>> mx.slice(a, start_indices=mx.array(1), axes=(0,), slice_size=(1, 2))
        array([[4, 5]], dtype=int32)
        >>>
        >>> mx.slice(a, start_indices=mx.array(1), axes=(1,), slice_size=(2, 1))
        array([[2],
               [5]], dtype=int32)
    :::
    ::::

[](mlx.core.sinh.html "previous page")

previous

mlx.core.sinh

[](mlx.core.slice_update.html "next page")

next

mlx.core.slice_update

Contents

- [[`slice()`]](#mlx.core.slice)

By MLX Contributors

© Copyright 2023, Apple.\