# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GroupNorm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.GroupNorm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.GroupNorm

## Contents

- [[`GroupNorm`]](#mlx.nn.GroupNorm)

# mlx.nn.GroupNorm[\#](#mlx-nn-groupnorm "Link to this heading")

*[class][ ]*[[GroupNorm]][(]*[[num_groups]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-05]]*, *[[affine]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[pytorch_compatible]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)][\#](#mlx.nn.GroupNorm "Link to this definition")

:   Applies Group Normalization \[1\] to the inputs.

    Computes the same normalization as layer norm, namely

    ::: 
    \\\[y = \\frac + \\epsilon} \\gamma + \\beta,\\\]
    :::

    where [\\(\\gamma\\)] and [\\(\\beta\\)] are learned per feature dimension parameters initialized at 1 and 0 respectively. However, the mean and variance are computed over the spatial dimensions and each group of features. In particular, the input is split into num_groups across the feature dimension.

    The feature dimension is assumed to be the last dimension and the dimensions that precede it (except the first) are considered the spatial dimensions.

    \[1\]: [https://arxiv.org/abs/1803.08494](https://arxiv.org/abs/1803.08494)

    Parameters[:]

    :   - **num_groups** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Number of groups to separate the features into

        - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The feature dimensions of the input to normalize over

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- A small additive constant for numerical stability

        - **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If True learn an affine transform to apply after the normalization.

        - **pytorch_compatible** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If True perform the group normalization in the same order/grouping as PyTorch.

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.GLU.html "previous page")

previous

mlx.nn.GLU

[](mlx.nn.GRU.html "next page")

next

mlx.nn.GRU

Contents

- [[`GroupNorm`]](#mlx.nn.GroupNorm)

By MLX Contributors

© Copyright 2023, Apple.\