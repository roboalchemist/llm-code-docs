# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GLU.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.GLU.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.GLU

## Contents

- [[`GLU`]](#mlx.nn.GLU)

# mlx.nn.GLU[\#](#mlx-nn-glu "Link to this heading")

*[class][ ]*[[GLU]][(]*[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*[)][\#](#mlx.nn.GLU "Link to this definition")

:   Applies the gated linear unit function.

    This function splits the [`axis`] dimension of the input into two halves ([\\(a\\)] and [\\(b\\)]) and applies [\\(a \* \\sigma(b)\\)].

    ::: 
    \\\[\\textrm(x) = a \* \\sigma(b)\\\]
    :::

    Parameters[:]

    :   **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimension to split along. Default: [`-1`]

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.GELU.html "previous page")

previous

mlx.nn.GELU

[](mlx.nn.GroupNorm.html "next page")

next

mlx.nn.GroupNorm

Contents

- [[`GLU`]](#mlx.nn.GLU)

By MLX Contributors

© Copyright 2023, Apple.\