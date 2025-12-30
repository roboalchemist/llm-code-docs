# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.send.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.distributed.send.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.distributed.send

## Contents

- [[`send()`]](#mlx.core.distributed.send)

# mlx.core.distributed.send[\#](#mlx-core-distributed-send "Link to this heading")

[[send]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[dst]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[\*]]*, *[[group]][[:]][ ][[[Group]](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.distributed.send "Link to this definition")

:   Send an array from the current process to the process that has rank [`dst`] in the group.

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **dst** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Rank of the destination process in the group.

        - **group** ([*Group*](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")) -- The group of processes that will participate in the send. If set to [`None`] the global group is used. Default: [`None`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   An array identical to [`x`] which when evaluated the send is performed.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.distributed.all_gather.html "previous page")

previous

mlx.core.distributed.all_gather

[](mlx.core.distributed.recv.html "next page")

next

mlx.core.distributed.recv

Contents

- [[`send()`]](#mlx.core.distributed.send)

By MLX Contributors

© Copyright 2023, Apple.\