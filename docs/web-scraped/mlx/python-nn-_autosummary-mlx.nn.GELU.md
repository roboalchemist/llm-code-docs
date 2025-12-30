# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GELU.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary/mlx.nn.GELU.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.GELU

## Contents

- [[`GELU`]](#mlx.nn.GELU)

# mlx.nn.GELU[\#](#mlx-nn-gelu "Link to this heading")

*[class][ ]*[[GELU]][(]*[[approx]][[=]][[\'none\']]*[)][\#](#mlx.nn.GELU "Link to this definition")

:   Applies the Gaussian Error Linear Units.

    ::: 
    \\\[\\textrm(x) = x \* \\Phi(x)\\\]
    :::

    where [\\(\\Phi(x)\\)] is the Gaussian CDF.

    However, if [`approx`] is set to 'precise' or 'fast' it applies

    ::: 
    \\\[\\begin\\textrm(x) &= 0.5 \* x \* \\left(1 + \\text\\left((\\sqrt \* \\left(x + 0.044715 \* x\^3\\right)\\right)\\right) \\\\ \\textrm(x) &= x \* \\sigma\\left(1.702 \* x\\right)\\end\\\]
    :::

    respectively.

    ::: 
    Note

    For compatibility with the PyTorch API, 'tanh' can be used as an alias for 'precise'.
    :::

    See [[`gelu()`]](../_autosummary_functions/mlx.nn.gelu.html#mlx.nn.gelu "mlx.nn.gelu"), [[`gelu_approx()`]](../_autosummary_functions/mlx.nn.gelu_approx.html#mlx.nn.gelu_approx "mlx.nn.gelu_approx") and [[`gelu_fast_approx()`]](../_autosummary_functions/mlx.nn.gelu_fast_approx.html#mlx.nn.gelu_fast_approx "mlx.nn.gelu_fast_approx") for the functional equivalents and information regarding error bounds.

    Parameters[:]

    :   **approx** (*\'none\'* *\|* *\'precise\'* *\|* *\'fast\'*) -- Which approximation to gelu to use if any.

    Methods

    ::: pst-scrollable-table-container
    :::

[](mlx.nn.ELU.html "previous page")

previous

mlx.nn.ELU

[](mlx.nn.GLU.html "next page")

next

mlx.nn.GLU

Contents

- [[`GELU`]](#mlx.nn.GELU)

By MLX Contributors

© Copyright 2023, Apple.\