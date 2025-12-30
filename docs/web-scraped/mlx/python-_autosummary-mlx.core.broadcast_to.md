# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.broadcast_to.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.broadcast_to.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.broadcast_to

## Contents

- [[`broadcast_to()`]](#mlx.core.broadcast_to)

# mlx.core.broadcast_to[\#](#mlx-core-broadcast-to "Link to this heading")

[[broadcast_to]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.broadcast_to "Link to this definition")

:   Broadcast an array to the given shape.

    The broadcasting semantics are the same as Numpy.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The shape to broadcast to.

    Returns[:]

    :   The output array with the new shape.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.broadcast_arrays.html "previous page")

previous

mlx.core.broadcast_arrays

[](mlx.core.ceil.html "next page")

next

mlx.core.ceil

Contents

- [[`broadcast_to()`]](#mlx.core.broadcast_to)

By MLX Contributors

© Copyright 2023, Apple.\