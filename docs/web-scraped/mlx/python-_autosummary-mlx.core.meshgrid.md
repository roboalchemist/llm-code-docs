# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.meshgrid.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.meshgrid.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.meshgrid

## Contents

- [[`meshgrid()`]](#mlx.core.meshgrid)

# mlx.core.meshgrid[\#](#mlx-core-meshgrid "Link to this heading")

[[meshgrid]][(]*[[\*]][[arrays]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[sparse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[indexing]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[\'xy\']]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.meshgrid "Link to this definition")

:   Generate multidimensional coordinate grids from 1-D coordinate arrays

    Parameters[:]

    :   - **\*arrays** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input arrays.

        - **sparse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`], a sparse grid is returned in which each output array has a single non-zero element. If [`False`], a dense grid is returned. Defaults to [`False`].

        - **indexing** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- Cartesian ('xy') or matrix ('ij') indexing of the output arrays. Defaults to [`'xy'`].

    Returns[:]

    :   The output arrays.

    Return type[:]

    :   [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

[](mlx.core.median.html "previous page")

previous

mlx.core.median

[](mlx.core.min.html "next page")

next

mlx.core.min

Contents

- [[`meshgrid()`]](#mlx.core.meshgrid)

By MLX Contributors

© Copyright 2023, Apple.\