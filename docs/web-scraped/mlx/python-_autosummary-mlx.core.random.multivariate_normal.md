# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.multivariate_normal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.multivariate_normal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.multivariate_normal

## Contents

- [[`multivariate_normal()`]](#mlx.core.random.multivariate_normal)

# mlx.core.random.multivariate_normal[\#](#mlx-core-random-multivariate-normal "Link to this heading")

[[multivariate_normal]][(]*[[mean]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[cov]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.multivariate_normal "Link to this definition")

:   Generate jointly-normal random samples given a mean and covariance.

    The matrix [`cov`] must be positive semi-definite. The behavior is undefined if it is not. The only supported [`dtype`] is [`float32`].

    Parameters[:]

    :   - **mean** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- array of shape [`(...,`]` `[`n)`], the mean of the distribution.

        - **cov** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- array of shape [`(...,`]` `[`n,`]` `[`n)`], the covariance matrix of the distribution. The batch shape [`...`] must be broadcast-compatible with that of [`mean`].

        - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The output shape must be broadcast-compatible with [`mean.shape[:-1]`] and [`cov.shape[:-2]`]. If empty, the result shape is determined by broadcasting the batch shapes of [`mean`] and [`cov`]. Default: [`[]`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The output type. Default: [`float32`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The output array of random values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.normal.html "previous page")

previous

mlx.core.random.normal

[](mlx.core.random.randint.html "next page")

next

mlx.core.random.randint

Contents

- [[`multivariate_normal()`]](#mlx.core.random.multivariate_normal)

By MLX Contributors

© Copyright 2023, Apple.\