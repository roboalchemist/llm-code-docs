# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.split.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.split.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.split

## Contents

- [[`split()`]](#mlx.core.split)

# mlx.core.split[\#](#mlx-core-split "Link to this heading")

[[split]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[indices_or_sections]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.split "Link to this definition")

:   Split an array along a given axis.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **indices_or_sections** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- If [`indices_or_sections`] is an integer the array is split into that many sections of equal size. An error is raised if this is not possible. If [`indices_or_sections`] is a list, then the indices are the split points, and the array is divided into [`len(indices_or_sections)`]` `[`+`]` `[`1`] sub-arrays.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis to split along, defaults to 0.

    Returns[:]

    :   A list of split arrays.

    Return type[:]

    :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

    Example

    :::: 
    ::: highlight
        >>> a = mx.array([1, 2, 3, 4], dtype=mx.int32)
        >>> mx.split(a, 2)
        [array([1, 2], dtype=int32), array([3, 4], dtype=int32)]
        >>> mx.split(a, [1, 3])
        [array([1], dtype=int32), array([2, 3], dtype=int32), array([4], dtype=int32)]
    :::
    ::::

[](mlx.core.sort.html "previous page")

previous

mlx.core.sort

[](mlx.core.sqrt.html "next page")

next

mlx.core.sqrt

Contents

- [[`split()`]](#mlx.core.split)

By MLX Contributors

© Copyright 2023, Apple.\