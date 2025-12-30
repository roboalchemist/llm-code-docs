# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.value_and_grad.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.nn.value_and_grad.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.nn.value_and_grad

## Contents

- [[`value_and_grad()`]](#mlx.nn.value_and_grad)

# mlx.nn.value_and_grad[\#](#mlx-nn-value-and-grad "Link to this heading")

[[value_and_grad]][(]*[[model]][[:]][ ][[[Module]](../nn/module.html#mlx.nn.Module "mlx.nn.layers.base.Module")]*, *[[fn]][[:]][ ][[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]*[)][\#](#mlx.nn.value_and_grad "Link to this definition")

:   Transform the passed function [`fn`] to a function that computes the gradients of [`fn`] wrt the model's trainable parameters and also its value.

    Parameters[:]

    :   - **model** ([*Module*](../nn/module.html#mlx.nn.Module "mlx.nn.Module")) -- The model whose trainable parameters to compute gradients for

        - **fn** (*Callable*) -- The scalar function to compute gradients for

    Returns[:]

    :   A callable that returns the value of [`fn`] and the gradients wrt the trainable parameters of [`model`]

[](../nn.html "previous page")

previous

Neural Networks

[](mlx.nn.quantize.html "next page")

next

mlx.nn.quantize

Contents

- [[`value_and_grad()`]](#mlx.nn.value_and_grad)

By MLX Contributors

© Copyright 2023, Apple.\