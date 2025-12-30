# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.uniform.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.uniform.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.uniform

## Contents

- [[`uniform()`]](#mlx.core.random.uniform)

# mlx.core.random.uniform[\#](#mlx-core-random-uniform "Link to this heading")

[[uniform]][(]*[[low]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")][ ][[=]][ ][[0]]*, *[[high]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")][ ][[=]][ ][[1]]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.uniform "Link to this definition")

:   Generate uniformly distributed random numbers.

    The values are sampled uniformly in the half-open interval [`[low,`]` `[`high)`]. The lower and upper bound can be scalars or arrays and must be broadcastable to [`shape`].

    Parameters[:]

    :   - **low** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Lower bound of the distribution. Default: [`0`].

        - **high** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Upper bound of the distribution. Default: [`1`].

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Shape of the output. Default:[`()`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Type of the output. Default: [`float32`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The output array random values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.truncated_normal.html "previous page")

previous

mlx.core.random.truncated_normal

[](mlx.core.random.laplace.html "next page")

next

mlx.core.random.laplace

Contents

- [[`uniform()`]](#mlx.core.random.uniform)

By MLX Contributors

© Copyright 2023, Apple.\