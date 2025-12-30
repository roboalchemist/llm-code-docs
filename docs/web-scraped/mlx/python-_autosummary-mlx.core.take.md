# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.take.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.take.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.take

## Contents

- [[`take()`]](#mlx.core.take)

# mlx.core.take[\#](#mlx-core-take "Link to this heading")

[[take]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[indices]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.take "Link to this definition")

:   Take elements along an axis.

    The elements are taken from [`indices`] along the specified axis. If the axis is not specified the array is treated as a flattened 1-D array prior to performing the take.

    As an example, if the [`axis=1`] this is equivalent to [`a[:,`]` `[`indices,`]` `[`...]`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **indices** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Integer index or input array with integral type.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis along which to perform the take. If unspecified the array is treated as a flattened 1-D vector.

    Returns[:]

    :   The indexed values of [`a`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.swapaxes.html "previous page")

previous

mlx.core.swapaxes

[](mlx.core.take_along_axis.html "next page")

next

mlx.core.take_along_axis

Contents

- [[`take()`]](#mlx.core.take)

By MLX Contributors

© Copyright 2023, Apple.\