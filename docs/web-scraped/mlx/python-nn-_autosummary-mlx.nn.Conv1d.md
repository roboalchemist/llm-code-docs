# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Conv1d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Conv1d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Conv1d

## Contents

- [[`Conv1d`]](#mlx.nn.Conv1d)

# mlx.nn.Conv1d[\#](#mlx-nn-conv1d "Link to this heading")

*[class][ ]*[[Conv1d]][(]*[[in_channels]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[out_channels]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[kernel_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.Conv1d "Link to this definition")

:   Applies a 1-dimensional convolution over the multi-channel input sequence.

    The channels are expected to be last i.e. the input shape should be [`NLC`] where:

    - [`N`] is the batch dimension

    - [`L`] is the sequence length

    - [`C`] is the number of input channels

    Parameters[:]

    :   - **in_channels** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of input channels

        - **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of output channels

        - **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The size of the convolution filters

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The stride when applying the filter. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- How many positions to 0-pad the input with. Default: [`0`].

        - **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The dilation of the convolution.

        - **groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of groups for the convolution. Default: [`1`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`] add a learnable bias to the output. Default: [`True`]

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.CELU.html "previous page")

previous

mlx.nn.CELU

[](mlx.nn.Conv2d.html "next page")

next

mlx.nn.Conv2d

Contents

- [[`Conv1d`]](#mlx.nn.Conv1d)

By MLX Contributors

© Copyright 2023, Apple.\