# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.logaddexp.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.logaddexp.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.logaddexp

## Contents

- [[`logaddexp()`]](#mlx.core.logaddexp)

# mlx.core.logaddexp[\#](#mlx-core-logaddexp "Link to this heading")

[[logaddexp]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.logaddexp "Link to this definition")

:   Element-wise log-add-exp.

    This is a numerically stable log-add-exp of two arrays with numpy-style broadcasting semantics. Either or both input arrays can also be scalars.

    The computation is is a numerically stable version of [`log(exp(a)`]` `[`+`]` `[`exp(b))`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

    Returns[:]

    :   The log-add-exp of [`a`] and [`b`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.log1p.html "previous page")

previous

mlx.core.log1p

[](mlx.core.logcumsumexp.html "next page")

next

mlx.core.logcumsumexp

Contents

- [[`logaddexp()`]](#mlx.core.logaddexp)

By MLX Contributors

© Copyright 2023, Apple.\