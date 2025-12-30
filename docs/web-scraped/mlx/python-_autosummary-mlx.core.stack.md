# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stack.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.stack.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.stack

## Contents

- [[`stack()`]](#mlx.core.stack)

# mlx.core.stack[\#](#mlx-core-stack "Link to this heading")

[[stack]][(]*[[arrays]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.stack "Link to this definition")

:   Stacks the arrays along a new axis.

    Parameters[:]

    :   - **arrays** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- A list of arrays to stack.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The axis in the result array along which the input arrays are stacked. Defaults to [`0`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`].

    Returns[:]

    :   The resulting stacked array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.squeeze.html "previous page")

previous

mlx.core.squeeze

[](mlx.core.std.html "next page")

next

mlx.core.std

Contents

- [[`stack()`]](#mlx.core.stack)

By MLX Contributors

© Copyright 2023, Apple.\