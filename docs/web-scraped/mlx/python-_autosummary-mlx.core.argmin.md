# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argmin.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.argmin.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.argmin

## Contents

- [[`argmin()`]](#mlx.core.argmin)

# mlx.core.argmin[\#](#mlx-core-argmin "Link to this heading")

[[argmin]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[keepdims]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.argmin "Link to this definition")

:   Indices of the minimum values along the axis.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Optional axis to reduce over. If unspecified this defaults to reducing over the entire array.

        - **keepdims** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Keep reduced axes as singleton dimensions, defaults to False.

    Returns[:]

    :   The [`uint32`] array with the indices of the minimum values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.argmax.html "previous page")

previous

mlx.core.argmax

[](mlx.core.argpartition.html "next page")

next

mlx.core.argpartition

Contents

- [[`argmin()`]](#mlx.core.argmin)

By MLX Contributors

© Copyright 2023, Apple.\