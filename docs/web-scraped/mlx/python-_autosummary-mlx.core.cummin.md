# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cummin.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.cummin.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.cummin

## Contents

- [[`cummin()`]](#mlx.core.cummin)

# mlx.core.cummin[\#](#mlx-core-cummin "Link to this heading")

[[cummin]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[reverse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[inclusive]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.cummin "Link to this definition")

:   Return the cumulative minimum of the elements along the given axis.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Optional axis to compute the cumulative minimum over. If unspecified the cumulative minimum of the flattened array is returned.

        - **reverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Perform the cumulative minimum in reverse.

        - **inclusive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- The i-th element of the output includes the i-th element of the input.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.cummax.html "previous page")

previous

mlx.core.cummax

[](mlx.core.cumprod.html "next page")

next

mlx.core.cumprod

Contents

- [[`cummin()`]](#mlx.core.cummin)

By MLX Contributors

© Copyright 2023, Apple.\