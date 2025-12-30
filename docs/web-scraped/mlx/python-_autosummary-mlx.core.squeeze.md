# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.squeeze.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.squeeze.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.squeeze

## Contents

- [[`squeeze()`]](#mlx.core.squeeze)

# mlx.core.squeeze[\#](#mlx-core-squeeze "Link to this heading")

[[squeeze]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.squeeze "Link to this definition")

:   Remove length one axes from an array.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Axes to remove. Defaults to [`None`] in which case all size one axes are removed.

    Returns[:]

    :   The output array with size one axes removed.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.square.html "previous page")

previous

mlx.core.square

[](mlx.core.stack.html "next page")

next

mlx.core.stack

Contents

- [[`squeeze()`]](#mlx.core.squeeze)

By MLX Contributors

© Copyright 2023, Apple.\