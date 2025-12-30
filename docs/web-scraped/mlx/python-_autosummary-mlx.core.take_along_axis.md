# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.take_along_axis.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.take_along_axis.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.take_along_axis

## Contents

- [[`take_along_axis()`]](#mlx.core.take_along_axis)

# mlx.core.take_along_axis[\#](#mlx-core-take-along-axis "Link to this heading")

[[take_along_axis]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.take_along_axis "Link to this definition")

:   Take values along an axis at the specified indices.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Indices array. These should be broadcastable with the input array excluding the axis dimension.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None*) -- Axis in the input to take the values from. If [`axis`]` `[`==`]` `[`None`] the array is flattened to 1D prior to the indexing operation.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.take.html "previous page")

previous

mlx.core.take

[](mlx.core.tan.html "next page")

next

mlx.core.tan

Contents

- [[`take_along_axis()`]](#mlx.core.take_along_axis)

By MLX Contributors

© Copyright 2023, Apple.\