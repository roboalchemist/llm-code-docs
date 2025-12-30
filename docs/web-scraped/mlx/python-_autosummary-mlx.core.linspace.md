# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linspace.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.linspace.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.linspace

## Contents

- [[`linspace()`]](#mlx.core.linspace)

# mlx.core.linspace[\#](#mlx-core-linspace "Link to this heading")

[[linspace]][(]*[[start]][[:]][ ][[scalar]]*, *[[stop]][[:]][ ][[scalar]]*, *[[num]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[50]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.linspace "Link to this definition")

:   Generate [`num`] evenly spaced numbers over interval [`[start,`]` `[`stop]`].

    Parameters[:]

    :   - **start** (*scalar*) -- Starting value.

        - **stop** (*scalar*) -- Stopping value.

        - **num** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Number of samples, defaults to [`50`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Specifies the data type of the output, default to [`float32`].

    Returns[:]

    :   The range of values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.less_equal.html "previous page")

previous

mlx.core.less_equal

[](mlx.core.load.html "next page")

next

mlx.core.load

Contents

- [[`linspace()`]](#mlx.core.linspace)

By MLX Contributors

© Copyright 2023, Apple.\