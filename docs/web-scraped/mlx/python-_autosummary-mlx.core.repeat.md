# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.repeat.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.repeat.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.repeat

## Contents

- [[`repeat()`]](#mlx.core.repeat)

# mlx.core.repeat[\#](#mlx-core-repeat "Link to this heading")

[[repeat]][(]*[[array]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[repeats]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.repeat "Link to this definition")

:   Repeat an array along a specified axis.

    Parameters[:]

    :   - **array** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **repeats** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of repetitions for each element.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The axis in which to repeat the array along. If unspecified it uses the flattened array of the input and repeats along axis 0.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`].

    Returns[:]

    :   The resulting repeated array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.remainder.html "previous page")

previous

mlx.core.remainder

[](mlx.core.reshape.html "next page")

next

mlx.core.reshape

Contents

- [[`repeat()`]](#mlx.core.repeat)

By MLX Contributors

© Copyright 2023, Apple.\