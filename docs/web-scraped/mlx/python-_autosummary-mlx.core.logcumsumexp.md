# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.logcumsumexp.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.logcumsumexp.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.logcumsumexp

## Contents

- [[`logcumsumexp()`]](#mlx.core.logcumsumexp)

# mlx.core.logcumsumexp[\#](#mlx-core-logcumsumexp "Link to this heading")

[[logcumsumexp]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[reverse]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[inclusive]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.logcumsumexp "Link to this definition")

:   Return the cumulative logsumexp of the elements along the given axis.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Optional axis to compute the cumulative logsumexp over. If unspecified the cumulative logsumexp of the flattened array is returned.

        - **reverse** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Perform the cumulative logsumexp in reverse.

        - **inclusive** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- The i-th element of the output includes the i-th element of the input.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.logaddexp.html "previous page")

previous

mlx.core.logaddexp

[](mlx.core.logical_not.html "next page")

next

mlx.core.logical_not

Contents

- [[`logcumsumexp()`]](#mlx.core.logcumsumexp)

By MLX Contributors

© Copyright 2023, Apple.\