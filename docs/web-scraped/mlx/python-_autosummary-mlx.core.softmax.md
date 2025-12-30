# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.softmax.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.softmax.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.softmax

## Contents

- [[`softmax()`]](#mlx.core.softmax)

# mlx.core.softmax[\#](#mlx-core-softmax "Link to this heading")

[[softmax]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.softmax "Link to this definition")

:   Perform the softmax along the given axis.

    This operation is a numerically stable version of:

    :::: 
    ::: highlight
        exp(a) / sum(exp(a), axis, keepdims=True)
    :::
    ::::

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Optional axis or axes to compute the softmax over. If unspecified this performs the softmax over the full array.

    Returns[:]

    :   The output of the softmax.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.slice_update.html "previous page")

previous

mlx.core.slice_update

[](mlx.core.sort.html "next page")

next

mlx.core.sort

Contents

- [[`softmax()`]](#mlx.core.softmax)

By MLX Contributors

© Copyright 2023, Apple.\