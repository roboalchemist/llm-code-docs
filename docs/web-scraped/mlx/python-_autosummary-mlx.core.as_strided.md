# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.as_strided.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.as_strided.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.as_strided

## Contents

- [[`as_strided()`]](#mlx.core.as_strided)

# mlx.core.as_strided[\#](#mlx-core-as-strided "Link to this heading")

[[as_strided]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[strides]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[offset]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.as_strided "Link to this definition")

:   Create a view into the array with the given shape and strides.

    The resulting array will always be as if the provided array was row contiguous regardless of the provided arrays storage order and current strides.

    ::: 
    Note

    Note that this function should be used with caution as it changes the shape and strides of the array directly. This can lead to the resulting array pointing to invalid memory locations which can result into crashes.
    :::

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The shape of the resulting array. If None it defaults to [`a.shape()`].

        - **strides** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The strides of the resulting array. If None it defaults to the reverse exclusive cumulative product of [`a.shape()`].

        - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Skip that many elements from the beginning of the input array.

    Returns[:]

    :   The output array which is the strided view of the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.array_equal.html "previous page")

previous

mlx.core.array_equal

[](mlx.core.atleast_1d.html "next page")

next

mlx.core.atleast_1d

Contents

- [[`as_strided()`]](#mlx.core.as_strided)

By MLX Contributors

© Copyright 2023, Apple.\