# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.all_gather.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.distributed.all_gather.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.distributed.all_gather

## Contents

- [[`all_gather()`]](#mlx.core.distributed.all_gather)

# mlx.core.distributed.all_gather[\#](#mlx-core-distributed-all-gather "Link to this heading")

[[all_gather]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[group]][[:]][ ][[[Group]](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.distributed.all_gather "Link to this definition")

:   Gather arrays from all processes.

    Gather the [`x`] arrays from all processes in the group and concatenate them along the first axis. The arrays should all have the same shape.

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **group** ([*Group*](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")) -- The group of processes that will participate in the gather. If set to [`None`] the global group is used. Default: [`None`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`] in which case the default stream of the default device is used.

    Returns[:]

    :   The concatenation of all [`x`] arrays.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.distributed.all_sum.html "previous page")

previous

mlx.core.distributed.all_sum

[](mlx.core.distributed.send.html "next page")

next

mlx.core.distributed.send

Contents

- [[`all_gather()`]](#mlx.core.distributed.all_gather)

By MLX Contributors

© Copyright 2023, Apple.\