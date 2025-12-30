# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.optimizers.clip_grad_norm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.optimizers.clip_grad_norm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.clip_grad_norm

## Contents

- [[`clip_grad_norm()`]](#mlx.optimizers.clip_grad_norm)

# mlx.optimizers.clip_grad_norm[\#](#mlx-optimizers-clip-grad-norm "Link to this heading")

[[clip_grad_norm]][(]*[[grads]]*, *[[max_norm]]*[)][\#](#mlx.optimizers.clip_grad_norm "Link to this definition")

:   Clips the global norm of the gradients.

    This function ensures that the global norm of the gradients does not exceed [`max_norm`]. It scales down the gradients proportionally if their norm is greater than [`max_norm`].

    Example

    :::: 
    ::: highlight
        >>> grads = 
        >>> clipped_grads, total_norm = clip_grad_norm(grads, max_norm=2.0)
        >>> print(clipped_grads)
        
    :::
    ::::

    Parameters[:]

    :   - **grads** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) -- A dictionary containing the gradient arrays.

        - **max_norm** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- The maximum allowed global norm of the gradients.

    Returns[:]

    :   The possibly rescaled gradients and the original gradient norm.

    Return type[:]

    :   ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"), [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"))

[](../optimizers/_autosummary/mlx.optimizers.step_decay.html "previous page")

previous

mlx.optimizers.step_decay

[](../distributed.html "next page")

next

Distributed Communication

Contents

- [[`clip_grad_norm()`]](#mlx.optimizers.clip_grad_norm)

By MLX Contributors

© Copyright 2023, Apple.\