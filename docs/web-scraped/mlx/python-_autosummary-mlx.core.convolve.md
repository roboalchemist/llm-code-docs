# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.convolve.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.convolve.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.convolve

## Contents

- [[`convolve()`]](#mlx.core.convolve)

# mlx.core.convolve[\#](#mlx-core-convolve "Link to this heading")

[[convolve]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[v]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'full\']]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.convolve "Link to this definition")

:   The discrete convolution of 1D arrays.

    If [`v`] is longer than [`a`], then they are swapped. The conv filter is flipped following signal processing convention.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- 1D Input array.

        - **v** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- 1D Input array.

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- 

    Returns[:]

    :   The convolved array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.conjugate.html "previous page")

previous

mlx.core.conjugate

[](mlx.core.conv1d.html "next page")

next

mlx.core.conv1d

Contents

- [[`convolve()`]](#mlx.core.convolve)

By MLX Contributors

© Copyright 2023, Apple.\