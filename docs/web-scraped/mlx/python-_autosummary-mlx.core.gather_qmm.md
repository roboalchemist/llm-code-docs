# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.gather_qmm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.gather_qmm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.gather_qmm

## Contents

- [[`gather_qmm()`]](#mlx.core.gather_qmm)

# mlx.core.gather_qmm[\#](#mlx-core-gather-qmm "Link to this heading")

[[gather_qmm]][(]*[[x]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[w]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[scales]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[biases]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[lhs_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[rhs_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[transpose]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[True]]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*, *[[\*]]*, *[[sorted_indices]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.gather_qmm "Link to this definition")

:   Perform quantized matrix multiplication with matrix-level gather.

    This operation is the quantized equivalent to [[`gather_mm()`]](mlx.core.gather_mm.html#mlx.core.gather_mm "mlx.core.gather_mm"). Similar to [[`gather_mm()`]](mlx.core.gather_mm.html#mlx.core.gather_mm "mlx.core.gather_mm"), the indices [`lhs_indices`] and [`rhs_indices`] contain flat indices along the batch dimensions (i.e. all but the last two dimensions) of [`x`] and [`w`] respectively.

    Note that [`scales`] and [`biases`] must have the same batch dimensions as [`w`] since they represent the same quantized matrix.

    Parameters[:]

    :   - **x** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **w** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Quantized matrix packed in unsigned integers

        - **scales** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The scales to use per [`group_size`] elements of [`w`]

        - **biases** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- The biases to use per [`group_size`] elements of [`w`]. Default: [`None`].

        - **lhs_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Integer indices for [`x`]. Default: [`None`].

        - **rhs_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Integer indices for [`w`]. Default: [`None`].

        - **transpose** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Defines whether to multiply with the transposed [`w`] or not, namely whether we are performing [`x`]` `[`@`]` `[`w.T`] or [`x`]` `[`@`]` `[`w`]. Default: [`True`].

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The size of the group in [`w`] that shares a scale and bias. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of bits occupied by each element of [`w`] in the quantized array. See supported values and defaults in the [[table of quantization modes]](mlx.core.quantize.html#quantize-modes). Default: [`None`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- The quantization mode. Default: [`"affine"`].

        - **sorted_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- May allow a faster implementation if the passed indices are sorted. Default: [`False`].

    Returns[:]

    :   

        The result of the multiplication of [`x`] with [`w`]

        :   after gathering using [`lhs_indices`] and [`rhs_indices`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.gather_mm.html "previous page")

previous

mlx.core.gather_mm

[](mlx.core.greater.html "next page")

next

mlx.core.greater

Contents

- [[`gather_qmm()`]](#mlx.core.gather_qmm)

By MLX Contributors

© Copyright 2023, Apple.\