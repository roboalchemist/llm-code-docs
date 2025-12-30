# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.partition.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.partition.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.partition

## Contents

- [[`partition()`]](#mlx.core.partition)

# mlx.core.partition[\#](#mlx-core-partition "Link to this heading")

[[partition]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[kth]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.partition "Link to this definition")

:   Returns a partitioned copy of the array such that the smaller [`kth`] elements are first.

    The ordering of the elements in partitions is undefined.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **kth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Element at the [`kth`] index will be in its sorted position in the output. All elements before the kth index will be less or equal to the [`kth`] element and all elements after will be greater or equal to the [`kth`] element in the output.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None,* *optional*) -- Optional axis to partition over. If [`None`], this partitions over the flattened array. If unspecified, it defaults to [`-1`].

    Returns[:]

    :   The partitioned array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.outer.html "previous page")

previous

mlx.core.outer

[](mlx.core.pad.html "next page")

next

mlx.core.pad

Contents

- [[`partition()`]](#mlx.core.partition)

By MLX Contributors

© Copyright 2023, Apple.\