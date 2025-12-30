# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv_transpose2d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.conv_transpose2d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.conv_transpose2d

## Contents

- [[`conv_transpose2d()`]](#mlx.core.conv_transpose2d)

# mlx.core.conv_transpose2d[\#](#mlx-core-conv-transpose2d "Link to this heading")

[[conv_transpose2d]][(]*[[input]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weight]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[0]]*, *[[dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[1]]*, *[[output_padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[0]]*, *[[groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.conv_transpose2d "Link to this definition")

:   2D transposed convolution over an input with several channels

    Note: Only the default [`groups=1`] is currently supported.

    Parameters[:]

    :   - **input** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array of shape [`(N,`]` `[`H,`]` `[`W,`]` `[`C_in)`].

        - **weight** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Weight array of shape [`(C_out,`]` `[`KH,`]` `[`KW,`]` `[`C_in)`].

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of size 2 with kernel strides. All spatial dimensions get the same stride if only one number is specified. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of size 2 with symmetric input padding. All spatial dimensions get the same padding if only one number is specified. Default: [`0`].

        - **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of size 2 with kernel dilation. All spatial dimensions get the same dilation if only one number is specified. Default: [`1`]

        - **output_padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") of size 2 with output padding. All spatial dimensions get the same output padding if only one number is specified. Default: [`0`].

        - **groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- input feature groups. Default: [`1`].

    Returns[:]

    :   The convolved array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.conv_transpose1d.html "previous page")

previous

mlx.core.conv_transpose1d

[](mlx.core.conv_transpose3d.html "next page")

next

mlx.core.conv_transpose3d

Contents

- [[`conv_transpose2d()`]](#mlx.core.conv_transpose2d)

By MLX Contributors

© Copyright 2023, Apple.\