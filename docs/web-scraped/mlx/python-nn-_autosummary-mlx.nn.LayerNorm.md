# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.LayerNorm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.LayerNorm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.LayerNorm

## Contents

- [[`LayerNorm`]](#mlx.nn.LayerNorm)

# mlx.nn.LayerNorm[\#](#mlx-nn-layernorm "Link to this heading")

*[class][ ]*[[LayerNorm]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-05]]*, *[[affine]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[bias]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*[)][\#](#mlx.nn.LayerNorm "Link to this definition")

:   Applies layer normalization \[1\] on the inputs.

    Computes

    ::: 
    \\\[y = \\frac + \\epsilon} \\gamma + \\beta,\\\]
    :::

    where [\\(\\gamma\\)] and [\\(\\beta\\)] are learned per feature dimension parameters initialized at 1 and 0 respectively.

    \[1\]: [https://arxiv.org/abs/1607.06450](https://arxiv.org/abs/1607.06450)

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The feature dimension of the input to normalize over

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- A small additive constant for numerical stability

        - **affine** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If True learn an affine transform to apply after the normalization

        - **bias** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- If True include a translation to the affine transformation. If set to False the transformation is not really affine just scaling.

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.InstanceNorm.html "previous page")

previous

mlx.nn.InstanceNorm

[](mlx.nn.LeakyReLU.html "next page")

next

mlx.nn.LeakyReLU

Contents

- [[`LayerNorm`]](#mlx.nn.LayerNorm)

By MLX Contributors

© Copyright 2023, Apple.\