# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.split.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.split.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.split

## Contents

- [[`split()`]](#mlx.core.random.split)

# mlx.core.random.split[\#](#mlx-core-random-split "Link to this heading")

[[split]][(]*[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[num]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[2]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.split "Link to this definition")

:   Split a PRNG key into sub keys.

    Parameters[:]

    :   - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input key to split.

        - **num** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Number of sub keys. Default: [`2`].

    Returns[:]

    :   The array of sub keys with [`num`] as its first dimension.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.seed.html "previous page")

previous

mlx.core.random.seed

[](mlx.core.random.truncated_normal.html "next page")

next

mlx.core.random.truncated_normal

Contents

- [[`split()`]](#mlx.core.random.split)

By MLX Contributors

© Copyright 2023, Apple.\