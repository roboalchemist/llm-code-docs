# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.truncated_normal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.truncated_normal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.truncated_normal

## Contents

- [[`truncated_normal()`]](#mlx.core.random.truncated_normal)

# mlx.core.random.truncated_normal[\#](#mlx-core-random-truncated-normal "Link to this heading")

[[truncated_normal]][(]*[[lower]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[upper]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.truncated_normal "Link to this definition")

:   Generate values from a truncated normal distribution.

    The values are sampled from the truncated normal distribution on the domain [`(lower,`]` `[`upper)`]. The bounds [`lower`] and [`upper`] can be scalars or arrays and must be broadcastable to [`shape`].

    Parameters[:]

    :   - **lower** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Lower bound of the domain.

        - **upper** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Upper bound of the domain.

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The shape of the output. Default:[`()`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the output. Default: [`float32`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The output array of random values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.split.html "previous page")

previous

mlx.core.random.split

[](mlx.core.random.uniform.html "next page")

next

mlx.core.random.uniform

Contents

- [[`truncated_normal()`]](#mlx.core.random.truncated_normal)

By MLX Contributors

© Copyright 2023, Apple.\