# Source: https://ml-explore.github.io/mlx/build/html/usage/using_streams.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/usage/using_streams.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Using Streams

## Contents

- [Specifying the [`Stream`]](#specifying-the-stream)

[]

# Using Streams[\#](#using-streams "Link to this heading")

## Specifying the [[`Stream`]](../python/_autosummary/stream_class.html#mlx.core.Stream "mlx.core.Stream")[\#](#specifying-the-stream "Link to this heading")

All operations (including random number generation) take an optional keyword argument [`stream`]. The [`stream`] kwarg specifies which [[`Stream`]](../python/_autosummary/stream_class.html#mlx.core.Stream "mlx.core.Stream") the operation should run on. If the stream is unspecified then the operation is run on the default stream of the default device: [`mx.default_stream(mx.default_device())`]. The [`stream`] kwarg can also be a [[`Device`]](../python/_autosummary/mlx.core.Device.html#mlx.core.Device "mlx.core.Device") (e.g. [`stream=my_device`]) in which case the operation is run on the default stream of the provided device [`mx.default_stream(my_device)`].

[](distributed.html "previous page")

previous

Distributed Communication

[](export.html "next page")

next

Exporting Functions

Contents

- [Specifying the [`Stream`]](#specifying-the-stream)

By MLX Contributors

© Copyright 2023, Apple.\