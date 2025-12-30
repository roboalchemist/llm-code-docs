# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.bernoulli.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.bernoulli.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.bernoulli

## Contents

- [[`bernoulli()`]](#mlx.core.random.bernoulli)

# mlx.core.random.bernoulli[\#](#mlx-core-random-bernoulli "Link to this heading")

[[bernoulli]][(]*[[p]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")][ ][[=]][ ][[0.5]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.bernoulli "Link to this definition")

:   Generate Bernoulli random values.

    The values are sampled from the bernoulli distribution with parameter [`p`]. The parameter [`p`] can be a [[`float`]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") or [[`array`]](https://docs.python.org/3/library/array.html#module-array "(in Python v3.14)") and must be broadcastable to [`shape`].

    Parameters[:]

    :   - **p** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Parameter of the Bernoulli distribution. Default: [`0.5`].

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Shape of the output. Default: [`p.shape`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The array of random integers.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](../random.html "previous page")

previous

Random

[](mlx.core.random.categorical.html "next page")

next

mlx.core.random.categorical

Contents

- [[`bernoulli()`]](#mlx.core.random.bernoulli)

By MLX Contributors

© Copyright 2023, Apple.\