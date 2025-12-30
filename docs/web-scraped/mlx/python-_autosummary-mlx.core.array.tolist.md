# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.tolist.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.array.tolist.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.array.tolist

## Contents

- [[`array.tolist()`]](#mlx.core.array.tolist)

# mlx.core.array.tolist[\#](#mlx-core-array-tolist "Link to this heading")

[[array.]][[tolist]][(]*[[self]]*[)] [[→] [[list_or_scalar]]][\#](#mlx.core.array.tolist "Link to this definition")

:   Convert the array to a Python [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)").

    Returns[:]

    :   The Python list.

        If the array is a scalar then a standard Python scalar is returned.

        If the array has more than one dimension then the result is a nested list of lists.

        The value type of the list corresponding to the last dimension is either [`bool`], [`int`] or [`float`] depending on the [`dtype`] of the array.

    Return type[:]

    :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

[](mlx.core.array.item.html "previous page")

previous

mlx.core.array.item

[](mlx.core.array.dtype.html "next page")

next

mlx.core.array.dtype

Contents

- [[`array.tolist()`]](#mlx.core.array.tolist)

By MLX Contributors

© Copyright 2023, Apple.\