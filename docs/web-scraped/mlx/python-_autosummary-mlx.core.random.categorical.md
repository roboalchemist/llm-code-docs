# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.categorical.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.categorical.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.categorical

## Contents

- [[`categorical()`]](#mlx.core.random.categorical)

# mlx.core.random.categorical[\#](#mlx-core-random-categorical "Link to this heading")

[[categorical]][(]*[[logits]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[num_samples]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.categorical "Link to this definition")

:   Sample from a categorical distribution.

    The values are sampled from the categorical distribution specified by the unnormalized values in [`logits`]. Note, at most one of [`shape`] or [`num_samples`] can be specified. If both are [`None`], the output has the same shape as [`logits`] with the [`axis`] dimension removed.

    Parameters[:]

    :   - **logits** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The *unnormalized* categorical distribution(s).

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The axis which specifies the distribution. Default: [`-1`].

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The shape of the output. This must be broadcast compatible with [`logits.shape`] with the [`axis`] dimension removed. Default: [`None`]

        - **num_samples** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of samples to draw from each of the categorical distributions in [`logits`]. The output will have [`num_samples`] in the last dimension. Default: [`None`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The [`shape`]-sized output array with type [`uint32`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.bernoulli.html "previous page")

previous

mlx.core.random.bernoulli

[](mlx.core.random.gumbel.html "next page")

next

mlx.core.random.gumbel

Contents

- [[`categorical()`]](#mlx.core.random.categorical)

By MLX Contributors

© Copyright 2023, Apple.\