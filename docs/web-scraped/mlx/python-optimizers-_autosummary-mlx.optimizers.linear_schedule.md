# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.linear_schedule.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.linear_schedule.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.linear_schedule

## Contents

- [[`linear_schedule()`]](#mlx.optimizers.linear_schedule)

# mlx.optimizers.linear_schedule[\#](#mlx-optimizers-linear-schedule "Link to this heading")

[[linear_schedule]][(]*[[init]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[end]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]*, *[[steps]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]][\#](#mlx.optimizers.linear_schedule "Link to this definition")

:   Make a linear scheduler.

    Parameters[:]

    :   - **init** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Initial value.

        - **end** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Final value.

        - **steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Number of steps to apply the schedule over. The value is [`end`] for any steps beyond [`steps`].

    Example

    :::: 
    ::: highlight
        >>> lr_schedule = optim.linear_schedule(0, 1e-1, 100)
        >>> optimizer = optim.Adam(learning_rate=lr_schedule)
        >>> optimizer.learning_rate
        array(0.0, dtype=float32)
        >>> for _ in range(101): optimizer.update(, )
        ...
        >>> optimizer.learning_rate
        array(0.1, dtype=float32)
    :::
    ::::

[](mlx.optimizers.join_schedules.html "previous page")

previous

mlx.optimizers.join_schedules

[](mlx.optimizers.step_decay.html "next page")

next

mlx.optimizers.step_decay

Contents

- [[`linear_schedule()`]](#mlx.optimizers.linear_schedule)

By MLX Contributors

© Copyright 2023, Apple.\