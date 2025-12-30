# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.gelu_fast_approx.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.gelu_fast_approx.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.gelu_fast_approx

## Contents

- [[`gelu_fast_approx`]](#mlx.nn.gelu_fast_approx)

# mlx.nn.gelu_fast_approx[\#](#mlx-nn-gelu-fast-approx "Link to this heading")

*[class][ ]*[[gelu_fast_approx]][(]*[[x]]*[)][\#](#mlx.nn.gelu_fast_approx "Link to this definition")

:   A fast approximation to Gaussian Error Linear Unit.

    See [[`gelu()`]](mlx.nn.gelu.html#mlx.nn.gelu "mlx.nn.gelu") for the exact computation.

    This function approximates [`gelu`] with a maximum absolute error [\\(\< 0.015\\)] in the range [\\(\[-6, 6\]\\)] using the following

    ::: 
    \\\[x = x \\sigma\\left(1.702 x\\right)\\\]
    :::

    where [\\(\\sigma(\\cdot)\\)] is the logistic sigmoid.

    References: - [hendrycks/GELUs](https://github.com/hendrycks/GELUs) - [https://arxiv.org/abs/1606.08415](https://arxiv.org/abs/1606.08415)

[](mlx.nn.gelu_approx.html "previous page")

previous

mlx.nn.gelu_approx

[](mlx.nn.glu.html "next page")

next

mlx.nn.glu

Contents

- [[`gelu_fast_approx`]](#mlx.nn.gelu_fast_approx)

By MLX Contributors

© Copyright 2023, Apple.\