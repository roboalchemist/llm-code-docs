# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.topk.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.topk.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.topk

## Contents

- [[`topk()`]](#mlx.core.topk)

# mlx.core.topk[\#](#mlx-core-topk "Link to this heading")

[[topk]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[k]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.topk "Link to this definition")

:   Returns the [`k`] largest elements from the input along a given axis.

    The elements will not necessarily be in sorted order.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **k** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- [`k`] top elements to be returned

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None,* *optional*) -- Optional axis to select over. If [`None`], this selects the top [`k`] elements over the flattened array. If unspecified, it defaults to [`-1`].

    Returns[:]

    :   The top [`k`] elements from the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.tile.html "previous page")

previous

mlx.core.tile

[](mlx.core.trace.html "next page")

next

mlx.core.trace

Contents

- [[`topk()`]](#mlx.core.topk)

By MLX Contributors

© Copyright 2023, Apple.\