# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.step_decay.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.step_decay.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.step_decay

## Contents

- [[`step_decay()`]](#mlx.optimizers.step_decay)

# mlx.optimizers.step_decay[\#](#mlx-optimizers-step-decay "Link to this heading")

[[step_decay]][(]*[[init]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[decay_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[step_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]][\#](#mlx.optimizers.step_decay "Link to this definition")

:   Make a step decay scheduler.

    Parameters[:]

    :   - **init** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Initial value.

        - **decay_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Multiplicative factor to decay by.

        - **step_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Decay every [`step_size`] steps.

    Example

    :::: 
    ::: highlight
        >>> lr_schedule = optim.step_decay(1e-1, 0.9, 10)
        >>> optimizer = optim.SGD(learning_rate=lr_schedule)
        >>> optimizer.learning_rate
        array(0.1, dtype=float32)
        >>>
        >>> for _ in range(21): optimizer.update(, )
        ...
        >>> optimizer.learning_rate
        array(0.081, dtype=float32)
    :::
    ::::

[](mlx.optimizers.linear_schedule.html "previous page")

previous

mlx.optimizers.linear_schedule

[](../../_autosummary/mlx.optimizers.clip_grad_norm.html "next page")

next

mlx.optimizers.clip_grad_norm

Contents

- [[`step_decay()`]](#mlx.optimizers.step_decay)

By MLX Contributors

© Copyright 2023, Apple.\