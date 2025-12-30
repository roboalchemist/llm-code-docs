# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.irfft.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.irfft.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.irfft

## Contents

- [[`irfft()`]](#mlx.core.fft.irfft)

# mlx.core.fft.irfft[\#](#mlx-core-fft-irfft "Link to this heading")

[[irfft]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[n]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.irfft "Link to this definition")

:   The inverse of [[`rfft()`]](mlx.core.fft.rfft.html#mlx.core.fft.rfft "mlx.core.fft.rfft").

    The output has the same shape as the input except along [`axis`] in which case it has size [`n`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Size of the transformed axis. The corresponding axis in the input is truncated or padded with zeros to match [`n`]` `[`//`]` `[`2`]` `[`+`]` `[`1`]. The default value is [`a.shape[axis]`]` `[`//`]` `[`2`]` `[`+`]` `[`1`].

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis along which to perform the FFT. The default is [`-1`].

    Returns[:]

    :   The real array containing the inverse of [[`rfft()`]](mlx.core.fft.rfft.html#mlx.core.fft.rfft "mlx.core.fft.rfft").

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.rfft.html "previous page")

previous

mlx.core.fft.rfft

[](mlx.core.fft.rfft2.html "next page")

next

mlx.core.fft.rfft2

Contents

- [[`irfft()`]](#mlx.core.fft.irfft)

By MLX Contributors

© Copyright 2023, Apple.\