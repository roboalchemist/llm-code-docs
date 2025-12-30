# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.concatenate.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.concatenate.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.concatenate

## Contents

- [[`concatenate()`]](#mlx.core.concatenate)

# mlx.core.concatenate[\#](#mlx-core-concatenate "Link to this heading")

[[concatenate]][(]*[[arrays]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.concatenate "Link to this definition")

:   Concatenate the arrays along the given axis.

    Parameters[:]

    :   - **arrays** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- Input [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") or [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of arrays.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Optional axis to concatenate along. If unspecified defaults to [`0`].

    Returns[:]

    :   The concatenated array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.clip.html "previous page")

previous

mlx.core.clip

[](mlx.core.contiguous.html "next page")

next

mlx.core.contiguous

Contents

- [[`concatenate()`]](#mlx.core.concatenate)

By MLX Contributors

© Copyright 2023, Apple.\