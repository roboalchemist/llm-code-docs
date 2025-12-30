# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.isclose.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.isclose.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.isclose

## Contents

- [[`isclose()`]](#mlx.core.isclose)

# mlx.core.isclose[\#](#mlx-core-isclose "Link to this heading")

[[isclose]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[rtol]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-05]]*, *[[atol]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-08]]*, *[[\*]]*, *[[equal_nan]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.isclose "Link to this definition")

:   Returns a boolean array where two arrays are element-wise equal within a tolerance.

    Infinite values are considered equal if they have the same sign, NaN values are not equal unless [`equal_nan`] is [`True`].

    Two values are considered equal if:

    :::: 
    ::: highlight
        abs(a - b) <= (atol + rtol * abs(b))
    :::
    ::::

    Note unlike [[`array_equal()`]](mlx.core.array_equal.html#mlx.core.array_equal "mlx.core.array_equal"), this function supports numpy-style broadcasting.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **rtol** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Relative tolerance.

        - **atol** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Absolute tolerance.

        - **equal_nan** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If [`True`], NaNs are considered equal. Defaults to [`False`].

    Returns[:]

    :   The boolean output scalar indicating if the arrays are close.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.isfinite.html "previous page")

previous

mlx.core.isfinite

[](mlx.core.isinf.html "next page")

next

mlx.core.isinf

Contents

- [[`isclose()`]](#mlx.core.isclose)

By MLX Contributors

© Copyright 2023, Apple.\