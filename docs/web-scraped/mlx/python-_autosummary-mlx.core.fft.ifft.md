# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.ifft.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.ifft.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.ifft

## Contents

- [[`ifft()`]](#mlx.core.fft.ifft)

# mlx.core.fft.ifft[\#](#mlx-core-fft-ifft "Link to this heading")

[[ifft]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[n]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.ifft "Link to this definition")

:   One dimensional inverse discrete Fourier Transform.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Size of the transformed axis. The corresponding axis in the input is truncated or padded with zeros to match [`n`]. The default value is [`a.shape[axis]`].

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis along which to perform the FFT. The default is [`-1`].

    Returns[:]

    :   The inverse DFT of the input along the given axis.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.fft.html "previous page")

previous

mlx.core.fft.fft

[](mlx.core.fft.fft2.html "next page")

next

mlx.core.fft.fft2

Contents

- [[`ifft()`]](#mlx.core.fft.ifft)

By MLX Contributors

© Copyright 2023, Apple.\