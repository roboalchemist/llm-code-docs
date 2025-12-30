# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.ConvTranspose3d.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.ConvTranspose3d.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.ConvTranspose3d

## Contents

- [[`ConvTranspose3d`]](#mlx.nn.ConvTranspose3d)

# mlx.nn.ConvTranspose3d[\#](#mlx-nn-convtranspose3d "Link to this heading")

*[class][ ]*[[ConvTranspose3d]][(]*[[in_channels]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[out_channels]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[kernel_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")]*, *[[stride]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[dilation]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][ ][[=]][ ][[1]]*, *[[output_padding]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.ConvTranspose3d "Link to this definition")

:   Applies a 3-dimensional transposed convolution over the multi-channel input image.

    The channels are expected to be last i.e. the input shape should be [`NDHWC`] where:

    - [`N`] is the batch dimension

    - [`D`] is the input image depth

    - [`H`] is the input image height

    - [`W`] is the input image width

    - [`C`] is the number of input channels

    Parameters[:]

    :   - **in_channels** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of input channels.

        - **out_channels** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of output channels.

        - **kernel_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")) -- The size of the convolution filters.

        - **stride** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*,* *optional*) -- The size of the stride when applying the filter. Default: [`1`].

        - **padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*,* *optional*) -- How many positions to 0-pad the input with. Default: [`0`].

        - **dilation** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*,* *optional*) -- The dilation of the convolution.

        - **output_padding** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*,* *optional*) -- Additional size added to one side of the output shape. Default: [`0`].

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If [`True`] add a learnable bias to the output. Default: [`True`]

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.ConvTranspose2d.html "previous page")

previous

mlx.nn.ConvTranspose2d

[](mlx.nn.Dropout.html "next page")

next

mlx.nn.Dropout

Contents

- [[`ConvTranspose3d`]](#mlx.nn.ConvTranspose3d)

By MLX Contributors

© Copyright 2023, Apple.\