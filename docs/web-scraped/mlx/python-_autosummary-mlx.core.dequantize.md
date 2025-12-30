# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.dequantize.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.dequantize.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.dequantize

## Contents

- [[`dequantize()`]](#mlx.core.dequantize)

# mlx.core.dequantize[\#](#mlx-core-dequantize "Link to this heading")

[[dequantize]][(]*[[w]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[scales]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[biases]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.dequantize "Link to this definition")

:   Dequantize the matrix [`w`] using quantization parameters.

    Parameters[:]

    :   - **w** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Matrix to be dequantized

        - **scales** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The scales to use per [`group_size`] elements of [`w`].

        - **biases** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- The biases to use per [`group_size`] elements of [`w`]. Default: [`None`].

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The size of the group in [`w`] that shares a scale and bias. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of bits occupied by each element of [`w`] in the quantized array. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- The data type of the dequantized output. If [`None`] the return type is inferred from the scales and biases when possible and otherwise defaults to [`bfloat16`]. Default: [`None`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- The quantization mode. Default: [`"affine"`].

    Returns[:]

    :   The dequantized version of [`w`]

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

    Notes

    The currently supported quantization modes are [`"affine"`], [`"mxfp4`], [`"mxfp8"`], and [`"nvfp4"`].

    For [`affine`] quantization, given the notation in [[`quantize()`]](mlx.core.quantize.html#mlx.core.quantize "mlx.core.quantize"), we compute [\\(w_i\\)] from [\\(\\hat\\)] and corresponding [\\(s\\)] and [\\(\\beta\\)] as follows

    ::: 
    \\\[w_i = s \\hat + \\beta\\\]
    :::

[](mlx.core.degrees.html "previous page")

previous

mlx.core.degrees

[](mlx.core.diag.html "next page")

next

mlx.core.diag

Contents

- [[`dequantize()`]](#mlx.core.dequantize)

By MLX Contributors

© Copyright 2023, Apple.\