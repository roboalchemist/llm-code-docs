# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.cosine_decay.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.cosine_decay.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.cosine_decay

## Contents

- [[`cosine_decay()`]](#mlx.optimizers.cosine_decay)

# mlx.optimizers.cosine_decay[\#](#mlx-optimizers-cosine-decay "Link to this heading")

[[cosine_decay]][(]*[[init]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[decay_steps]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[end]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0.0]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]][\#](#mlx.optimizers.cosine_decay "Link to this definition")

:   Make a cosine decay scheduler.

    Parameters[:]

    :   - **init** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Initial value.

        - **decay_steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Number of steps to decay over. The decayed value is constant for steps beyond [`decay_steps`].

        - **end** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Final value to decay to. Default: [`0`].

    Example

    :::: 
    ::: highlight
        >>> lr_schedule = optim.cosine_decay(1e-1, 1000)
        >>> optimizer = optim.SGD(learning_rate=lr_schedule)
        >>> optimizer.learning_rate
        array(0.1, dtype=float32)
        >>>
        >>> for _ in range(5): optimizer.update(, )
        ...
        >>> optimizer.learning_rate
        array(0.0999961, dtype=float32)
    :::
    ::::

[](../schedulers.html "previous page")

previous

Schedulers

[](mlx.optimizers.exponential_decay.html "next page")

next

mlx.optimizers.exponential_decay

Contents

- [[`cosine_decay()`]](#mlx.optimizers.cosine_decay)

By MLX Contributors

© Copyright 2023, Apple.\