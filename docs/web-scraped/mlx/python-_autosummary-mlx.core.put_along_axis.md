# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.put_along_axis.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.put_along_axis.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.put_along_axis

## Contents

- [[`put_along_axis()`]](#mlx.core.put_along_axis)

# mlx.core.put_along_axis[\#](#mlx-core-put-along-axis "Link to this heading")

[[put_along_axis]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[values]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.put_along_axis "Link to this definition")

:   Put values along an axis at the specified indices.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Destination array.

        - **indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Indices array. These should be broadcastable with the input array excluding the axis dimension.

        - **values** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Values array. These should be broadcastable with the indices.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None*) -- Axis in the destination to put the values to. If [`axis`]` `[`==`]` `[`None`] the destination is flattened prior to the put operation.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.prod.html "previous page")

previous

mlx.core.prod

[](mlx.core.quantize.html "next page")

next

mlx.core.quantize

Contents

- [[`put_along_axis()`]](#mlx.core.put_along_axis)

By MLX Contributors

© Copyright 2023, Apple.\