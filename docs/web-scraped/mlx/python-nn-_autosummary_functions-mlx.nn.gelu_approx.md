# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.gelu_approx.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.gelu_approx.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.gelu_approx

## Contents

- [[`gelu_approx`]](#mlx.nn.gelu_approx)

# mlx.nn.gelu_approx[\#](#mlx-nn-gelu-approx "Link to this heading")

*[class][ ]*[[gelu_approx]][(]*[[x]]*[)][\#](#mlx.nn.gelu_approx "Link to this definition")

:   An approximation to Gaussian Error Linear Unit.

    See [[`gelu()`]](mlx.nn.gelu.html#mlx.nn.gelu "mlx.nn.gelu") for the exact computation.

    This function approximates [`gelu`] with a maximum absolute error [\\(\< 0.0005\\)] in the range [\\(\[-6, 6\]\\)] using the following

    ::: 
    \\\[x = 0.5 \* x \* \\left(1 + \\text\\left((\\sqrt \* \\left(x + 0.044715 \* x\^3\\right)\\right)\\right)\\\]
    :::

[](mlx.nn.gelu.html "previous page")

previous

mlx.nn.gelu

[](mlx.nn.gelu_fast_approx.html "next page")

next

mlx.nn.gelu_fast_approx

Contents

- [[`gelu_approx`]](#mlx.nn.gelu_approx)

By MLX Contributors

© Copyright 2023, Apple.\