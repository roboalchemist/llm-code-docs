# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.average_gradients.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.nn.average_gradients.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.average_gradients

## Contents

- [[`average_gradients()`]](#mlx.nn.average_gradients)

# mlx.nn.average_gradients[\#](#mlx-nn-average-gradients "Link to this heading")

[[average_gradients]][(]*[[gradients]][[:]][ ][[[Any]](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *[[group]][[:]][ ][[[Group]](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[all_reduce_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[33554432]]*, *[[communication_type]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[communication_stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)][\#](#mlx.nn.average_gradients "Link to this definition")

:   Average the gradients across the distributed processes in the passed group.

    This helper enables concatenating several gradients of small arrays to one big all reduce call for better networking performance.

    Parameters[:]

    :   - **gradients** (*Any*) -- The Python tree containing the gradients (it should have the same structure across processes)

        - **group** (*Optional\[*[*Group*](mlx.core.distributed.Group.html#mlx.core.distributed.Group "mlx.core.distributed.Group")*\]*) -- The group of processes to average the gradients. If set to [`None`] the global group is used. Default: [`None`].

        - **all_reduce_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Group arrays until their size in bytes exceeds this number. Perform one communication step per group of arrays. If less or equal to 0 array grouping is disabled. Default: [`32MiB`].

        - **communication_type** (*Optional\[*[*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*\]*) -- If provided cast to this type before performing the communication. Typically cast to a smaller float to reduce the communication size. Default: [`None`].

        - **communication_stream** (*Optional\[*[*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*\]*) -- The stream to usse for the communication. If unspecified the default communication stream is used which can vary by back-end. Default: [`None`].

[](mlx.nn.quantize.html "previous page")

previous

mlx.nn.quantize

[](../nn/module.html "next page")

next

Module

Contents

- [[`average_gradients()`]](#mlx.nn.average_gradients)

By MLX Contributors

© Copyright 2023, Apple.\