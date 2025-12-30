# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv_general.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.conv_general.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.conv_general

## Contents

- [[`conv_general()`]](#mlx.core.conv_general)

# mlx.core.conv_general[\#](#mlx-core-conv-general "Link to this heading")

[[conv_general]][(]*[[input]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[weight]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][[,]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][[\]]]][ ][[=]][ ][[0]]*, *[[kernel_dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[1]]*, *[[input_dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[1]]*, *[[groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[flip]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.conv_general "Link to this definition")

:   General convolution over an input with several channels

    Parameters[:]

    :   - **input** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array of shape [`(N,`]` `[`...,`]` `[`C_in)`].

        - **weight** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Weight array of shape [`(C_out,`]` `[`...,`]` `[`C_in)`].

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") with kernel strides. All spatial dimensions get the same stride if only one number is specified. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*), or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)),* *optional*) -- [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") with input padding. All spatial dimensions get the same padding if only one number is specified. Default: [`0`].

        - **kernel_dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") with kernel dilation. All spatial dimensions get the same dilation if only one number is specified. Default: [`1`]

        - **input_dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") with input dilation. All spatial dimensions get the same dilation if only one number is specified. Default: [`1`]

        - **groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Input feature groups. Default: [`1`].

        - **flip** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Flip the order in which the spatial dimensions of the weights are processed. Performs the cross-correlation operator when [`flip`] is [`False`] and the convolution operator otherwise. Default: [`False`].

    Returns[:]

    :   The convolved array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.conv_transpose3d.html "previous page")

previous

mlx.core.conv_transpose3d

[](mlx.core.cos.html "next page")

next

mlx.core.cos

Contents

- [[`conv_general()`]](#mlx.core.conv_general)

By MLX Contributors

© Copyright 2023, Apple.\