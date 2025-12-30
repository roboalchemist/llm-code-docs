# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.ELU.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.ELU.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.ELU

## Contents

- [[`ELU`]](#mlx.nn.ELU)

# mlx.nn.ELU[\#](#mlx-nn-elu "Link to this heading")

*[class][ ]*[[ELU]][(]*[[alpha]][[=]][[1.0]]*[)][\#](#mlx.nn.ELU "Link to this definition")

:   

    Applies the Exponential Linear Unit.

    :   Simply [`mx.where(x`]` `[`>`]` `[`0,`]` `[`x,`]` `[`alpha`]` `[`*`]` `[`(mx.exp(x)`]` `[`-`]` `[`1))`].

    See [[`elu()`]](../_autosummary_functions/mlx.nn.elu.html#mlx.nn.elu "mlx.nn.elu") for the functional equivalent.

    Parameters[:]

    :   **alpha** -- the [\\(\\alpha\\)] value for the ELU formulation. Default: [`1.0`]

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.Embedding.html "previous page")

previous

mlx.nn.Embedding

[](mlx.nn.GELU.html "next page")

next

mlx.nn.GELU

Contents

- [[`ELU`]](#mlx.nn.ELU)

By MLX Contributors

© Copyright 2023, Apple.\