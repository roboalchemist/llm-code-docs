# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cummax.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.cummax.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.cummax

## Contents

- [[`cummax()`]](#mlx.core.cummax)

# mlx.core.cummax[\#](#mlx-core-cummax "Link to this heading")

[[cummax]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[reverse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[inclusive]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.cummax "Link to this definition")

:   Return the cumulative maximum of the elements along the given axis.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Optional axis to compute the cumulative maximum over. If unspecified the cumulative maximum of the flattened array is returned.

        - **reverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Perform the cumulative maximum in reverse.

        - **inclusive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- The i-th element of the output includes the i-th element of the input.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.cosh.html "previous page")

previous

mlx.core.cosh

[](mlx.core.cummin.html "next page")

next

mlx.core.cummin

Contents

- [[`cummax()`]](#mlx.core.cummax)

By MLX Contributors

© Copyright 2023, Apple.\