# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array_equal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.array_equal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.array_equal

## Contents

- [[`array_equal()`]](#mlx.core.array_equal)

# mlx.core.array_equal[\#](#mlx-core-array-equal "Link to this heading")

[[array_equal]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[equal_nan]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.array_equal "Link to this definition")

:   Array equality check.

    Compare two arrays for equality. Returns [`True`] if and only if the arrays have the same shape and their values are equal. The arrays need not have the same type to be considered equal.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **equal_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`], NaNs are considered equal. Defaults to [`False`].

    Returns[:]

    :   A scalar boolean array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.argsort.html "previous page")

previous

mlx.core.argsort

[](mlx.core.as_strided.html "next page")

next

mlx.core.as_strided

Contents

- [[`array_equal()`]](#mlx.core.array_equal)

By MLX Contributors

© Copyright 2023, Apple.\