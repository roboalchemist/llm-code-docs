# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QuantizedLinear.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.QuantizedLinear.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.QuantizedLinear

## Contents

- [[`QuantizedLinear`]](#mlx.nn.QuantizedLinear)

# mlx.nn.QuantizedLinear[\#](#mlx-nn-quantizedlinear "Link to this heading")

*[class][ ]*[[QuantizedLinear]][(]*[[input_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[output_dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[64]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[4]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*[)][\#](#mlx.nn.QuantizedLinear "Link to this definition")

:   Applies an affine transformation to the input using a quantized weight matrix.

    It is the quantized equivalent of [[`mlx.nn.Linear`]](mlx.nn.Linear.html#mlx.nn.Linear "mlx.nn.Linear"). For now its parameters are frozen and will not be included in any gradient computation but this will probably change in the future.

    [[`QuantizedLinear`]](#mlx.nn.QuantizedLinear "mlx.nn.QuantizedLinear") also provides a classmethod [`from_linear()`] to convert linear layers to [[`QuantizedLinear`]](#mlx.nn.QuantizedLinear "mlx.nn.QuantizedLinear") layers.

    Parameters[:]

    :   - **input_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the input features.

        - **output_dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the output features.

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`False`] then the layer will not use a bias. Default: [`True`].

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The group size to use for the quantized weight. See [[`quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"). Default: [`64`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The bit width to use for the quantized weight. See [[`quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"). Default: [`4`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The quantization method to use (see [[`mlx.core.quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize")). Default: [`"affine"`].

    Methods

    ::: pst-scrollable-table-container
      -------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`from_linear`](linear_layer\[, group_size, \...\])   Create a [[`QuantizedLinear`]](#mlx.nn.QuantizedLinear "mlx.nn.QuantizedLinear") layer from a [[`Linear`]](mlx.nn.Linear.html#mlx.nn.Linear "mlx.nn.Linear") layer.
      -------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.nn.QuantizedEmbedding.html "previous page")

previous

mlx.nn.QuantizedEmbedding

[](mlx.nn.RMSNorm.html "next page")

next

mlx.nn.RMSNorm

Contents

- [[`QuantizedLinear`]](#mlx.nn.QuantizedLinear)

By MLX Contributors

© Copyright 2023, Apple.\