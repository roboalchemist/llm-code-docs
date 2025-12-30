# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.pad.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.pad.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.pad

## Contents

- [[`pad()`]](#mlx.core.pad)

# mlx.core.pad[\#](#mlx-core-pad "Link to this heading")

[[pad]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[pad_width]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][[\]]]]*, *[[mode]][[:]][ ][[Literal][[\[]][[\'constant\']][[,]][ ][[\'edge\']][[\]]]][ ][[=]][ ][[\'constant\']]*, *[[constant_values]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.pad "Link to this definition")

:   Pad an array with a constant value

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **pad_width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*))*) -- Number of padded values to add to the edges of each axis:[`((before_1,`]` `[`after_1),`]` `[`(before_2,`]` `[`after_2),`]` `[`...,`]` `[`(before_N,`]` `[`after_N))`]. If a single pair of integers is passed then [`(before_i,`]` `[`after_i)`] are all the same. If a single integer or tuple with a single integer is passed then all axes are extended by the same number on each side.

        - **mode** -- Padding mode. One of the following strings: "constant" (default): Pads with a constant value. "edge": Pads with the edge values of array.

        - **constant_value** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array") *or* *scalar,* *optional*) -- Optional constant value to pad the edges of the array with.

    Returns[:]

    :   The padded array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.partition.html "previous page")

previous

mlx.core.partition

[](mlx.core.power.html "next page")

next

mlx.core.power

Contents

- [[`pad()`]](#mlx.core.pad)

By MLX Contributors

© Copyright 2023, Apple.\