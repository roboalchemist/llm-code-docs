# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.irfft2.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.fft.irfft2.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.fft.irfft2

## Contents

- [[`irfft2()`]](#mlx.core.fft.irfft2)

# mlx.core.fft.irfft2[\#](#mlx-core-fft-irfft2 "Link to this heading")

[[irfft2]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[s]][[:]][ ][[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[,]][ ][[\...]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[axes]][[:]][ ][[[Sequence]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[\[-2,] [-1\]]]*, *[[stream]][[:]][ ][[[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.fft.irfft2 "Link to this definition")

:   The inverse of [[`rfft2()`]](mlx.core.fft.rfft2.html#mlx.core.fft.rfft2 "mlx.core.fft.rfft2").

    Note the input is generally complex. The dimensions of the input specified in [`axes`] are padded or truncated to match the sizes from [`s`]. The last axis in [`axes`] is treated as the real axis and will have size [`s[-1]`]` `[`//`]` `[`2`]` `[`+`]` `[`1`].

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input array.

        - **s** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Sizes of the transformed axes. The corresponding axes in the input are truncated or padded with zeros to match the sizes in [`s`] except for the last axis which has size [`s[-1]`]` `[`//`]` `[`2`]` `[`+`]` `[`1`]. The default value is the sizes of [`a`] along [`axes`].

        - **axes** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Axes along which to perform the FFT. The default is [`[-2,`]` `[`-1]`].

    Returns[:]

    :   The real array containing the inverse of [[`rfft2()`]](mlx.core.fft.rfft2.html#mlx.core.fft.rfft2 "mlx.core.fft.rfft2").

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.fft.rfft2.html "previous page")

previous

mlx.core.fft.rfft2

[](mlx.core.fft.rfftn.html "next page")

next

mlx.core.fft.rfftn

Contents

- [[`irfft2()`]](#mlx.core.fft.irfft2)

By MLX Contributors

© Copyright 2023, Apple.\