# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.glu.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.glu.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.glu

## Contents

- [[`glu`]](#mlx.nn.glu)

# mlx.nn.glu[\#](#mlx-nn-glu "Link to this heading")

*[class][ ]*[[glu]][(]*[[x]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*[)][\#](#mlx.nn.glu "Link to this definition")

:   Applies the gated linear unit function.

    This function splits the [`axis`] dimension of the input into two halves ([\\(a\\)] and [\\(b\\)]) and applies [\\(a \* \\sigma(b)\\)].

    ::: 
    \\\[\\textrm(x) = a \* \\sigma(b)\\\]
    :::

    Parameters[:]

    :   **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The dimension to split along. Default: [`-1`]

[](mlx.nn.gelu_fast_approx.html "previous page")

previous

mlx.nn.gelu_fast_approx

[](mlx.nn.hard_shrink.html "next page")

next

mlx.nn.hard_shrink

Contents

- [[`glu`]](#mlx.nn.glu)

By MLX Contributors

© Copyright 2023, Apple.\