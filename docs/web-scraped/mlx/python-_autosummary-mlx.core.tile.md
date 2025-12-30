# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.tile.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.tile.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.tile

## Contents

- [[`tile()`]](#mlx.core.tile)

# mlx.core.tile[\#](#mlx-core-tile "Link to this heading")

[[tile]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[reps]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.tile "Link to this definition")

:   Construct an array by repeating [`a`] the number of times given by [`reps`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **reps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The number of times to repeat [`a`] along each axis.

    Returns[:]

    :   The tiled array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.tensordot.html "previous page")

previous

mlx.core.tensordot

[](mlx.core.topk.html "next page")

next

mlx.core.topk

Contents

- [[`tile()`]](#mlx.core.tile)

By MLX Contributors

© Copyright 2023, Apple.\