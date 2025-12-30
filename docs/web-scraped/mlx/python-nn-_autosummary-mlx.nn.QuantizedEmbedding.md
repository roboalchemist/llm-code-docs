# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QuantizedEmbedding.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.QuantizedEmbedding.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.QuantizedEmbedding

## Contents

- [[`QuantizedEmbedding`]](#mlx.nn.QuantizedEmbedding)

# mlx.nn.QuantizedEmbedding[\#](#mlx-nn-quantizedembedding "Link to this heading")

*[class][ ]*[[QuantizedEmbedding]][(]*[[num_embeddings]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[64]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[4]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*[)][\#](#mlx.nn.QuantizedEmbedding "Link to this definition")

:   The same as [[`Embedding`]](mlx.nn.Embedding.html#mlx.nn.Embedding "mlx.nn.Embedding") but with a quantized weight matrix.

    [[`QuantizedEmbedding`]](#mlx.nn.QuantizedEmbedding "mlx.nn.QuantizedEmbedding") also provides a [`from_embedding()`] classmethod to convert embedding layers to [[`QuantizedEmbedding`]](#mlx.nn.QuantizedEmbedding "mlx.nn.QuantizedEmbedding") layers.

    Parameters[:]

    :   - **num_embeddings** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- How many possible discrete tokens can we embed. Usually called the vocabulary size.

        - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the embeddings.

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The group size to use for the quantized weight. See [[`quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"). Default: [`64`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The bit width to use for the quantized weight. See [[`quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"). Default: [`4`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The quantization method to use (see [[`mlx.core.quantize()`]](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize")). Default: [`"affine"`].

    Methods

    ::: pst-scrollable-table-container
      -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`as_linear`](x)                                Call the quantized embedding layer as a quantized linear layer.
      [`from_embedding`](embedding_layer\[, \...\])   Create a [[`QuantizedEmbedding`]](#mlx.nn.QuantizedEmbedding "mlx.nn.QuantizedEmbedding") layer from an [[`Embedding`]](mlx.nn.Embedding.html#mlx.nn.Embedding "mlx.nn.Embedding") layer.
      -------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.nn.PReLU.html "previous page")

previous

mlx.nn.PReLU

[](mlx.nn.QuantizedLinear.html "next page")

next

mlx.nn.QuantizedLinear

Contents

- [[`QuantizedEmbedding`]](#mlx.nn.QuantizedEmbedding)

By MLX Contributors

© Copyright 2023, Apple.\