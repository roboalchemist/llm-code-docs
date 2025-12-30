# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.slice_update.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.slice_update.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.slice_update

## Contents

- [[`slice_update()`]](#mlx.core.slice_update)

# mlx.core.slice_update[\#](#mlx-core-slice-update "Link to this heading")

[[slice_update]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[update]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[start_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axes]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.slice_update "Link to this definition")

:   Update a sub-array of the input array.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array to update

        - **update** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The update array.

        - **start_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The index location to start the slice at.

        - **axes** ([*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The axes corresponding to the indices in [`start_indices`].

    Returns[:]

    :   The output array with the same shape and type as the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Example

    :::: 
    ::: highlight
        >>> a = mx.zeros((3, 3))
        >>> mx.slice_update(a, mx.ones((1, 2)), start_indices=mx.array(1, 1), axes=(0, 1))
        array([[0, 0, 0],
               [0, 1, 0],
               [0, 1, 0]], dtype=float32)
    :::
    ::::

[](mlx.core.slice.html "previous page")

previous

mlx.core.slice

[](mlx.core.softmax.html "next page")

next

mlx.core.softmax

Contents

- [[`slice_update()`]](#mlx.core.slice_update)

By MLX Contributors

© Copyright 2023, Apple.\