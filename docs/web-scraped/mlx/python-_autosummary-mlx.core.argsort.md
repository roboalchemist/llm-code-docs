# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argsort.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.argsort.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.argsort

## Contents

- [[`argsort()`]](#mlx.core.argsort)

# mlx.core.argsort[\#](#mlx-core-argsort "Link to this heading")

[[argsort]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.argsort "Link to this definition")

:   Returns the indices that sort the array.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None,* *optional*) -- Optional axis to sort over. If [`None`], this sorts over the flattened array. If unspecified, it defaults to -1 (sorting over the last axis).

    Returns[:]

    :   The [`uint32`] array containing indices that sort the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.argpartition.html "previous page")

previous

mlx.core.argpartition

[](mlx.core.array_equal.html "next page")

next

mlx.core.array_equal

Contents

- [[`argsort()`]](#mlx.core.argsort)

By MLX Contributors

© Copyright 2023, Apple.\