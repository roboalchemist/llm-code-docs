# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Linear.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Linear.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Linear

## Contents

- [[`Linear`]](#mlx.nn.Linear)

# mlx.nn.Linear[\#](#mlx-nn-linear "Link to this heading")

*[class][ ]*[[Linear]][(]*[[input_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[output_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.Linear "Link to this definition")

:   Applies an affine transformation to the input.

    Concretely:

    ::: 
    \\\[y = x W\^\\top + b\\\]
    :::

    where: where [\\(W\\)] has shape [`[output_dims,`]` `[`input_dims]`] and [\\(b\\)] has shape [`[output_dims]`].

    The values are initialized from the uniform distribution [\\(\\mathcal(-, )\\)], where [\\(k = \\frac}\\)] and [\\(D_i\\)] is equal to [`input_dims`].

    Parameters[:]

    :   - **input_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the input features

        - **output_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the output features

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`False`] then the layer will not use a bias. Default is [`True`].

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`to_quantized`](\[group_size, bits, mode\])   Return a [[`QuantizedLinear`]](mlx.nn.QuantizedLinear.html#mlx.nn.QuantizedLinear "mlx.nn.QuantizedLinear") layer that approximates this layer.
      ------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.nn.LeakyReLU.html "previous page")

previous

mlx.nn.LeakyReLU

[](mlx.nn.LogSigmoid.html "next page")

next

mlx.nn.LogSigmoid

Contents

- [[`Linear`]](#mlx.nn.Linear)

By MLX Contributors

© Copyright 2023, Apple.\