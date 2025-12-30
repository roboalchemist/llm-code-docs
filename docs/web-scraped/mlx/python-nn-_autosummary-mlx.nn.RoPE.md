# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RoPE.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.RoPE.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.RoPE

## Contents

- [[`RoPE`]](#mlx.nn.RoPE)

# mlx.nn.RoPE[\#](#mlx-nn-rope "Link to this heading")

*[class][ ]*[[RoPE]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[traditional]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[base]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[10000]]*, *[[scale]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*[)][\#](#mlx.nn.RoPE "Link to this definition")

:   Implements the rotary positional encoding.

    The traditional implementation rotates consecutive pairs of elements in the feature dimension while the default implementation rotates pairs with stride half the feature dimensions for efficiency.

    For more details see [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864).

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The feature dimensions to be rotated. If the input feature is larger than dims then the rest is left unchanged.

        - **traditional** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- If set to [`True`] choose the traditional implementation which is slightly less efficient. Default: [`False`].

        - **base** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The base used to compute angular frequency for each dimension in the positional encodings. Default: [`10000`].

        - **scale** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- The scale used to scale the positions. Default: [`1.0`].

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.RNN.html "previous page")

previous

mlx.nn.RNN

[](mlx.nn.SELU.html "next page")

next

mlx.nn.SELU

Contents

- [[`RoPE`]](#mlx.nn.RoPE)

By MLX Contributors

© Copyright 2023, Apple.\