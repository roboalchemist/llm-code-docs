# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.randint.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.randint.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.randint

## Contents

- [[`randint()`]](#mlx.core.random.randint)

# mlx.core.random.randint[\#](#mlx-core-random-randint "Link to this heading")

[[randint]][(]*[[low]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[high]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[int32]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.randint "Link to this definition")

:   Generate random integers from the given interval.

    The values are sampled with equal probability from the integers in half-open interval [`[low,`]` `[`high)`]. The lower and upper bound can be scalars or arrays and must be broadcastable to [`shape`].

    Parameters[:]

    :   - **low** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Lower bound of the interval.

        - **high** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Upper bound of the interval.

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Shape of the output. Default: [`()`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Type of the output. Default: [`int32`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The array of random integers.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.multivariate_normal.html "previous page")

previous

mlx.core.random.multivariate_normal

[](mlx.core.random.seed.html "next page")

next

mlx.core.random.seed

Contents

- [[`randint()`]](#mlx.core.random.randint)

By MLX Contributors

© Copyright 2023, Apple.\