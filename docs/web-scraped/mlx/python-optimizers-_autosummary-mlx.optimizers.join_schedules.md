# Source: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.join_schedules.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.join_schedules.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.optimizers.join_schedules

## Contents

- [[`join_schedules()`]](#mlx.optimizers.join_schedules)

# mlx.optimizers.join_schedules[\#](#mlx-optimizers-join-schedules "Link to this heading")

[[join_schedules]][(]*[[schedules]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")[[\]]]]*, *[[boundaries]][[:]][ ][[[List]](https://docs.python.org/3/library/typing.html#typing.List "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*[)] [[→] [[[Callable]](https://docs.python.org/3/library/typing.html#typing.Callable "(in Python v3.14)")]][\#](#mlx.optimizers.join_schedules "Link to this definition")

:   Join multiple schedules to create a new schedule.

    Parameters[:]

    :   - **schedules** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(Callable)*) -- A list of schedules. Schedule [\\(i+1\\)] receives a step count indicating the number of steps since the [\\(i\\)]-th boundary.

        - **boundaries** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- A list of integers of length [`len(schedules)`]` `[`-`]` `[`1`] that indicates when to transition between schedules.

    Example

    :::: 
    ::: highlight
        >>> linear = optim.linear_schedule(0, 1e-1, steps=10)
        >>> cosine = optim.cosine_decay(1e-1, 200)
        >>> lr_schedule = optim.join_schedules([linear, cosine], [10])
        >>> optimizer = optim.Adam(learning_rate=lr_schedule)
        >>> optimizer.learning_rate
        array(0.0, dtype=float32)
        >>> for _ in range(12): optimizer.update(, )
        ...
        >>> optimizer.learning_rate
        array(0.0999938, dtype=float32)
    :::
    ::::

[](mlx.optimizers.exponential_decay.html "previous page")

previous

mlx.optimizers.exponential_decay

[](mlx.optimizers.linear_schedule.html "next page")

next

mlx.optimizers.linear_schedule

Contents

- [[`join_schedules()`]](#mlx.optimizers.join_schedules)

By MLX Contributors

© Copyright 2023, Apple.\