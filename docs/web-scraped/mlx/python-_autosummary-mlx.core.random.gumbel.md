# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.gumbel.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.gumbel.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.gumbel

## Contents

- [[`gumbel()`]](#mlx.core.random.gumbel)

# mlx.core.random.gumbel[\#](#mlx-core-random-gumbel "Link to this heading")

[[gumbel]][(]*[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.gumbel "Link to this definition")

:   Sample from the standard Gumbel distribution.

    The values are sampled from a standard Gumbel distribution which CDF [`exp(-exp(-x))`].

    Parameters[:]

    :   - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The shape of the output.

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the output. Default: [`float32`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The [`array`] with shape [`shape`] and distributed according to the Gumbel distribution.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.categorical.html "previous page")

previous

mlx.core.random.categorical

[](mlx.core.random.key.html "next page")

next

mlx.core.random.key

Contents

- [[`gumbel()`]](#mlx.core.random.gumbel)

By MLX Contributors

© Copyright 2023, Apple.\