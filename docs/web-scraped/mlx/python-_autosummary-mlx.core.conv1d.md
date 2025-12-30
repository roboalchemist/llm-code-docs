# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv1d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.conv1d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.conv1d

## Contents

- [[`conv1d()`]](#mlx.core.conv1d)

# mlx.core.conv1d[\#](#mlx-core-conv1d "Link to this heading")

[[conv1d]][(]*[[input]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weight]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.conv1d "Link to this definition")

:   1D convolution over an input with several channels

    Parameters[:]

    :   - **input** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array of shape [`(N,`]` `[`L,`]` `[`C_in)`].

        - **weight** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Weight array of shape [`(C_out,`]` `[`K,`]` `[`C_in)`].

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Kernel stride. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Input padding. Default: [`0`].

        - **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Kernel dilation. Default: [`1`].

        - **groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Input feature groups. Default: [`1`].

    Returns[:]

    :   The convolved array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.convolve.html "previous page")

previous

mlx.core.convolve

[](mlx.core.conv2d.html "next page")

next

mlx.core.conv2d

Contents

- [[`conv1d()`]](#mlx.core.conv1d)

By MLX Contributors

© Copyright 2023, Apple.\