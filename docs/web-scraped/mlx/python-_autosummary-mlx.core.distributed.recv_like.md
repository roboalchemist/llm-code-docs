# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.recv_like.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.distributed.recv_like.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.distributed.recv_like

## Contents

- [[`recv_like()`]](#mlx.core.distributed.recv_like)

# mlx.core.distributed.recv_like[\#](#mlx-core-distributed-recv-like "Link to this heading")

[[recv_like]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[src]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[\*]]*, *[[group]][[:]][ ][[[Group]](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.distributed.recv_like "Link to this definition")

:   Recv an array with shape and type like [`x`] from process with rank [`src`].

    It is equivalent to calling [`mx.distributed.recv(x.shape,`]` `[`x.dtype,`]` `[`src)`].

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- An array defining the shape and dtype of the array we are receiving.

        - **src** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Rank of the source process in the group.

        - **group** ([*Group*](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")) -- The group of processes that will participate in the recv. If set to [`None`] the global group is used. Default: [`None`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The array that was received from [`src`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.distributed.recv.html "previous page")

previous

mlx.core.distributed.recv

[](../tree_utils.html "next page")

next

Tree Utils

Contents

- [[`recv_like()`]](#mlx.core.distributed.recv_like)

By MLX Contributors

© Copyright 2023, Apple.\