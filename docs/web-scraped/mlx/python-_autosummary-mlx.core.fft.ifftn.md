# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.ifftn.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.ifftn.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.ifftn

## Contents

- [[`ifftn()`]](#mlx.core.fft.ifftn)

# mlx.core.fft.ifftn[\#](#mlx-core-fft-ifftn "Link to this heading")

[[ifftn]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[s]][[:]][ ][[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[\...]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axes]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.ifftn "Link to this definition")

:   n-dimensional inverse discrete Fourier Transform.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **s** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Sizes of the transformed axes. The corresponding axes in the input are truncated or padded with zeros to match the sizes in [`s`]. The default value is the sizes of [`a`] along [`axes`].

        - **axes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Axes along which to perform the FFT. The default is [`None`] in which case the FFT is over the last [`len(s)`] axes or all axes if [`s`] is also [`None`].

    Returns[:]

    :   The inverse DFT of the input along the given axes.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.fftn.html "previous page")

previous

mlx.core.fft.fftn

[](mlx.core.fft.rfft.html "next page")

next

mlx.core.fft.rfft

Contents

- [[`ifftn()`]](#mlx.core.fft.ifftn)

By MLX Contributors

© Copyright 2023, Apple.\