# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.layer_norm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fast.layer_norm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fast.layer_norm

## Contents

- [[`layer_norm()`]](#mlx.core.fast.layer_norm)

# mlx.core.fast.layer_norm[\#](#mlx-core-fast-layer-norm "Link to this heading")

[[layer_norm]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weight]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fast.layer_norm "Link to this definition")

:   Layer normalization.

    The normalization is with respect to the last axis of the input [`x`].

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **weight** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A multiplicative weight to scale the result by. The [`weight`] should be one-dimensional with the same size as the last axis of [`x`]. If set to [`None`] then no scaling happens.

        - **bias** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- An additive offset to be added to the result. The [`bias`] should be one-dimensional with the same size as the last axis of [`x`]. If set to [`None`] then no translation happens.

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- A small additive constant for numerical stability.

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fast.rms_norm.html "previous page")

previous

mlx.core.fast.rms_norm

[](mlx.core.fast.rope.html "next page")

next

mlx.core.fast.rope

Contents

- [[`layer_norm()`]](#mlx.core.fast.layer_norm)

By MLX Contributors

© Copyright 2023, Apple.\