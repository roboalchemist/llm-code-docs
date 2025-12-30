# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.eye.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.eye.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.eye

## Contents

- [[`eye()`]](#mlx.core.eye)

# mlx.core.eye[\#](#mlx-core-eye "Link to this heading")

[[eye]][(]*[[n]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[m]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[k]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[float32]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.eye "Link to this definition")

:   Create an identity matrix or a general diagonal matrix.

    Parameters[:]

    :   - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The number of rows in the output.

        - **m** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of columns in the output. Defaults to n.

        - **k** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Index of the diagonal. Defaults to 0 (main diagonal).

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Data type of the output array. Defaults to float32.

        - **stream** ([*Stream*](stream_class.html#mlx.core.Stream "mlx.core.Stream")*,* *optional*) -- Stream or device. Defaults to None.

    Returns[:]

    :   An array where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.expand_dims.html "previous page")

previous

mlx.core.expand_dims

[](mlx.core.flatten.html "next page")

next

mlx.core.flatten

Contents

- [[`eye()`]](#mlx.core.eye)

By MLX Contributors

© Copyright 2023, Apple.\