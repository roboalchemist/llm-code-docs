# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.normal.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.normal.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.normal

## Contents

- [[`normal()`]](#mlx.core.random.normal)

# mlx.core.random.normal[\#](#mlx-core-random-normal "Link to this heading")

[[normal]][(]*[[shape]][[:]][ ][[Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[loc]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[scale]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.normal "Link to this definition")

:   Generate normally distributed random numbers.

    If [`loc`] and [`scale`] are not provided the "standard" normal distribution is used. That means \$x sim mathcal(0, 1)\$ for real numbers and \$text(x),text(x) sim mathcal(0, frac)\$ for complex numbers.

    Parameters[:]

    :   - **shape** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Shape of the output. Default: [`()`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Type of the output. Default: [`float32`].

        - **loc** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Mean of the distribution. Default: [`None`].

        - **scale** (*scalar* *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Standard deviation of the distribution. Default: [`None`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The output array of random values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.key.html "previous page")

previous

mlx.core.random.key

[](mlx.core.random.multivariate_normal.html "next page")

next

mlx.core.random.multivariate_normal

Contents

- [[`normal()`]](#mlx.core.random.normal)

By MLX Contributors

© Copyright 2023, Apple.\