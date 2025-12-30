# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RMSNorm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.RMSNorm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.RMSNorm

## Contents

- [[`RMSNorm`]](#mlx.nn.RMSNorm)

# mlx.nn.RMSNorm[\#](#mlx-nn-rmsnorm "Link to this heading")

*[class][ ]*[[RMSNorm]][(]*[[dims]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[eps]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1e-05]]*[)][\#](#mlx.nn.RMSNorm "Link to this definition")

:   Applies Root Mean Square normalization \[1\] to the inputs.

    Computes

    ::: 
    \\\[y = \\frac} \\gamma\\\]
    :::

    where [\\(\\gamma\\)] is a learned per feature dimension parameter initialized at 1.

    Note the accumulation for the mean is done in 32-bit precision.

    \[1\]: [https://arxiv.org/abs/1910.07467](https://arxiv.org/abs/1910.07467)

    Parameters[:]

    :   - **dims** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The feature dimension of the input to normalize over

        - **eps** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- A small additive constant for numerical stability

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.QuantizedLinear.html "previous page")

previous

mlx.nn.QuantizedLinear

[](mlx.nn.ReLU.html "next page")

next

mlx.nn.ReLU

Contents

- [[`RMSNorm`]](#mlx.nn.RMSNorm)

By MLX Contributors

© Copyright 2023, Apple.\