# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.rfft.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.rfft.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.rfft

## Contents

- [[`rfft()`]](#mlx.core.fft.rfft)

# mlx.core.fft.rfft[\#](#mlx-core-fft-rfft "Link to this heading")

[[rfft]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[n]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[-1]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.rfft "Link to this definition")

:   One dimensional discrete Fourier Transform on a real input.

    The output has the same shape as the input except along [`axis`] in which case it has size [`n`]` `[`//`]` `[`2`]` `[`+`]` `[`1`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array. If the array is complex it will be silently cast to a real type.

        - **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Size of the transformed axis. The corresponding axis in the input is truncated or padded with zeros to match [`n`]. The default value is [`a.shape[axis]`].

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- Axis along which to perform the FFT. The default is [`-1`].

    Returns[:]

    :   The DFT of the input along the given axis. The output data type will be complex.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.ifftn.html "previous page")

previous

mlx.core.fft.ifftn

[](mlx.core.fft.irfft.html "next page")

next

mlx.core.fft.irfft

Contents

- [[`rfft()`]](#mlx.core.fft.rfft)

By MLX Contributors

© Copyright 2023, Apple.\