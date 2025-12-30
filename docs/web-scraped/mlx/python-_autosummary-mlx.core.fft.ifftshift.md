# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.ifftshift.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.ifftshift.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.ifftshift

## Contents

- [[`ifftshift()`]](#mlx.core.fft.ifftshift)

# mlx.core.fft.ifftshift[\#](#mlx-core-fft-ifftshift "Link to this heading")

[[ifftshift]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axes]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.ifftshift "Link to this definition")

:   The inverse of [[`fftshift()`]](mlx.core.fft.fftshift.html#mlx.core.fft.fftshift "mlx.core.fft.fftshift"). While identical to [[`fftshift()`]](mlx.core.fft.fftshift.html#mlx.core.fft.fftshift "mlx.core.fft.fftshift") for even-length axes, the behavior differs for odd-length axes.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **axes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Axes over which to perform the inverse shift. If [`None`], shift all axes.

    Returns[:]

    :   The inverse-shifted array with the same shape as the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.fftshift.html "previous page")

previous

mlx.core.fft.fftshift

[](../linalg.html "next page")

next

Linear Algebra

Contents

- [[`ifftshift()`]](#mlx.core.fft.ifftshift)

By MLX Contributors

© Copyright 2023, Apple.\