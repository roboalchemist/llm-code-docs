# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.fftshift.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.fftshift.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.fftshift

## Contents

- [[`fftshift()`]](#mlx.core.fft.fftshift)

# mlx.core.fft.fftshift[\#](#mlx-core-fft-fftshift "Link to this heading")

[[fftshift]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axes]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.fftshift "Link to this definition")

:   Shift the zero-frequency component to the center of the spectrum.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **axes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Axes over which to perform the shift. If [`None`], shift all axes.

    Returns[:]

    :   The shifted array with the same shape as the input.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.irfftn.html "previous page")

previous

mlx.core.fft.irfftn

[](mlx.core.fft.ifftshift.html "next page")

next

mlx.core.fft.ifftshift

Contents

- [[`fftshift()`]](#mlx.core.fft.fftshift)

By MLX Contributors

© Copyright 2023, Apple.\