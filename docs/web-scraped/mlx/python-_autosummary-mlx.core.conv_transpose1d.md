# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv_transpose1d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.conv_transpose1d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.conv_transpose1d

## Contents

- [[`conv_transpose1d()`]](#mlx.core.conv_transpose1d)

# mlx.core.conv_transpose1d[\#](#mlx-core-conv-transpose1d "Link to this heading")

[[conv_transpose1d]][(]*[[input]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weight]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[output_padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.conv_transpose1d "Link to this definition")

:   1D transposed convolution over an input with several channels

    Parameters[:]

    :   - **input** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array of shape [`(N,`]` `[`L,`]` `[`C_in)`].

        - **weight** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Weight array of shape [`(C_out,`]` `[`K,`]` `[`C_in)`].

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Kernel stride. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Input padding. Default: [`0`].

        - **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Kernel dilation. Default: [`1`].

        - **output_padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Output padding. Default: [`0`].

        - **groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Input feature groups. Default: [`1`].

    Returns[:]

    :   The convolved array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.conv3d.html "previous page")

previous

mlx.core.conv3d

[](mlx.core.conv_transpose2d.html "next page")

next

mlx.core.conv_transpose2d

Contents

- [[`conv_transpose1d()`]](#mlx.core.conv_transpose1d)

By MLX Contributors

© Copyright 2023, Apple.\