# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.exponential_decay.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.exponential_decay.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.exponential_decay

## Contents

- [[`exponential_decay()`]](#mlx.optimizers.exponential_decay)

# mlx.optimizers.exponential_decay[\#](#mlx-optimizers-exponential-decay "Link to this heading")

[[exponential_decay]][(]*[[init]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[decay_rate]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]][\#](#mlx.optimizers.exponential_decay "Link to this definition")

:   Make an exponential decay scheduler.

    Parameters[:]

    :   - **init** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Initial value.

        - **decay_rate** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Multiplicative factor to decay by.

    Example

    :::: 
    ::: highlight
        >>> lr_schedule = optim.exponential_decay(1e-1, 0.9)
        >>> optimizer = optim.SGD(learning_rate=lr_schedule)
        >>> optimizer.learning_rate
        array(0.1, dtype=float32)
        >>>
        >>> for _ in range(5): optimizer.update(, )
        ...
        >>> optimizer.learning_rate
        array(0.06561, dtype=float32)
    :::
    ::::

[](mlx.optimizers.cosine_decay.html "previous page")

previous

mlx.optimizers.cosine_decay

[](mlx.optimizers.join_schedules.html "next page")

next

mlx.optimizers.join_schedules

Contents

- [[`exponential_decay()`]](#mlx.optimizers.exponential_decay)

By MLX Contributors

© Copyright 2023, Apple.\