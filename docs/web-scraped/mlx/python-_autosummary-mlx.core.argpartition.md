# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argpartition.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.argpartition.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.argpartition

## Contents

- [[`argpartition()`]](#mlx.core.argpartition)

# mlx.core.argpartition[\#](#mlx-core-argpartition "Link to this heading")

[[argpartition]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[kth]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.argpartition "Link to this definition")

:   Returns the indices that partition the array.

    The ordering of the elements within a partition in given by the indices is undefined.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **kth** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Element index at the [`kth`] position in the output will give the sorted position. All indices before the [`kth`] position will be of elements less or equal to the element at the [`kth`] index and all indices after will be of elements greater or equal to the element at the [`kth`] index.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* *None,* *optional*) -- Optional axis to partition over. If [`None`], this partitions over the flattened array. If unspecified, it defaults to [`-1`].

    Returns[:]

    :   The [`uint32`] array containing indices that partition the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.argmin.html "previous page")

previous

mlx.core.argmin

[](mlx.core.argsort.html "next page")

next

mlx.core.argsort

Contents

- [[`argpartition()`]](#mlx.core.argpartition)

By MLX Contributors

© Copyright 2023, Apple.\