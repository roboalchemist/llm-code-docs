# Source: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.step.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/nn/_autosummary_functions/mlx.nn.step.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.step

## Contents

- [[`step`]](#mlx.nn.step)

# mlx.nn.step[\#](#mlx-nn-step "Link to this heading")

*[class][ ]*[[step]][(]*[[x]][[:]][ ][[[array]](../../_autosummary/mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[threshold]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*[)][\#](#mlx.nn.step "Link to this definition")

:   Applies the Step Activation Function.

    This function implements a binary step activation, where the output is set to 1 if the input is greater than a specified threshold, and 0 otherwise.

    ::: 
    \\\[\\begin\\text(x) = \\begin 0 & \\text x \< \\text \\\\ 1 & \\text x \\geq \\text \\end\\end\\\]
    :::

    Parameters[:]

    :   **threshold** -- The value to threshold at.

[](mlx.nn.softshrink.html "previous page")

previous

mlx.nn.softshrink

[](mlx.nn.tanh.html "next page")

next

mlx.nn.tanh

Contents

- [[`step`]](#mlx.nn.step)

By MLX Contributors

© Copyright 2023, Apple.\