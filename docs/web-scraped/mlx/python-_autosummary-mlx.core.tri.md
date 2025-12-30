# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.tri.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.tri.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.tri

## Contents

- [[`tri()`]](#mlx.core.tri)

# mlx.core.tri[\#](#mlx-core-tri "Link to this heading")

[[tri]][(]*[[n]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[m]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[k]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.tri "Link to this definition")

:   An array with ones at and below the given diagonal and zeros elsewhere.

    Parameters[:]

    :   - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of rows in the output.

        - **m** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of cols in the output. Defaults to [`None`].

        - **k** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The diagonal of the 2-D array. Defaults to [`0`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Data type of the output array. Defaults to [`float32`].

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to [`None`].

    Returns[:]

    :   Array with its lower triangle filled with ones and zeros elsewhere

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.transpose.html "previous page")

previous

mlx.core.transpose

[](mlx.core.tril.html "next page")

next

mlx.core.tril

Contents

- [[`tri()`]](#mlx.core.tri)

By MLX Contributors

© Copyright 2023, Apple.\