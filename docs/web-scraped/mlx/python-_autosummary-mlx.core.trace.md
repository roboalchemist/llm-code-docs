# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.trace.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.trace.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.trace

## Contents

- [[`trace()`]](#mlx.core.trace)

# mlx.core.trace[\#](#mlx-core-trace "Link to this heading")

[[trace]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[offset]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[axis1]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[axis2]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.trace "Link to this definition")

:   Return the sum along a specified diagonal in the given array.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **offset** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Offset of the diagonal from the main diagonal. Can be positive or negative. Default: [`0`].

        - **axis1** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The first axis of the 2-D sub-arrays from which the diagonals should be taken. Default: [`0`].

        - **axis2** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The second axis of the 2-D sub-arrays from which the diagonals should be taken. Default: [`1`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Data type of the output array. If unspecified the output type is inferred from the input array.

    Returns[:]

    :   Sum of specified diagonal.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.topk.html "previous page")

previous

mlx.core.topk

[](mlx.core.transpose.html "next page")

next

mlx.core.transpose

Contents

- [[`trace()`]](#mlx.core.trace)

By MLX Contributors

© Copyright 2023, Apple.\