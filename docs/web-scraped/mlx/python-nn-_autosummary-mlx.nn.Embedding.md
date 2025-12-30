# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Embedding.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.Embedding.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.Embedding

## Contents

- [[`Embedding`]](#mlx.nn.Embedding)

# mlx.nn.Embedding[\#](#mlx-nn-embedding "Link to this heading")

*[class][ ]*[[Embedding]][(]*[[num_embeddings]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#mlx.nn.Embedding "Link to this definition")

:   Implements a simple lookup table that maps each input integer to a high-dimensional vector.

    Typically used to embed discrete tokens for processing by neural networks.

    Parameters[:]

    :   - **num_embeddings** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- How many possible discrete tokens can we embed. Usually called the vocabulary size.

        - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimensionality of the embeddings.

    Methods

    ::: pst-scrollable-table-container
      ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      [`as_linear`](x)                               Call the embedding layer as a linear layer.
      [`to_quantized`](\[group_size, bits, mode\])   Return a [[`QuantizedEmbedding`]](mlx.nn.QuantizedEmbedding.html#mlx.nn.QuantizedEmbedding "mlx.nn.QuantizedEmbedding") layer that approximates this embedding layer.
      ------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    :::

[](mlx.nn.Dropout3d.html "previous page")

previous

mlx.nn.Dropout3d

[](mlx.nn.ELU.html "next page")

next

mlx.nn.ELU

Contents

- [[`Embedding`]](#mlx.nn.Embedding)

By MLX Contributors

© Copyright 2023, Apple.\