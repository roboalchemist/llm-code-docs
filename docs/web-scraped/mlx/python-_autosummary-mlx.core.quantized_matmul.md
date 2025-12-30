# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.quantized_matmul.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.quantized_matmul.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.quantized_matmul

## Contents

- [[`quantized_matmul()`]](#mlx.core.quantized_matmul)

# mlx.core.quantized_matmul[\#](#mlx-core-quantized-matmul "Link to this heading")

[[quantized_matmul]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[w]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[scales]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[biases]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[transpose]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.quantized_matmul "Link to this definition")

:   Perform the matrix multiplication with the quantized matrix [`w`]. The quantization uses one floating point scale and bias per [`group_size`] of elements. Each element in [`w`] takes [`bits`] bits and is packed in an unsigned 32 bit integer.

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **w** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Quantized matrix packed in unsigned integers

        - **scales** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The scales to use per [`group_size`] elements of [`w`]

        - **biases** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- The biases to use per [`group_size`] elements of [`w`]. Default: [`None`].

        - **transpose** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Defines whether to multiply with the transposed [`w`] or not, namely whether we are performing [`x`]` `[`@`]` `[`w.T`] or [`x`]` `[`@`]` `[`w`]. Default: [`True`].

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The size of the group in [`w`] that shares a scale and bias. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of bits occupied by each element of [`w`] in the quantized array. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- The quantization mode. Default: [`"affine"`].

    Returns[:]

    :   The result of the multiplication of [`x`] with [`w`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.quantize.html "previous page")

previous

mlx.core.quantize

[](mlx.core.radians.html "next page")

next

mlx.core.radians

Contents

- [[`quantized_matmul()`]](#mlx.core.quantized_matmul)

By MLX Contributors

© Copyright 2023, Apple.\