# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.quantize.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.quantize.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.quantize

## Contents

- [[`quantize()`]](#mlx.core.quantize)

# mlx.core.quantize[\#](#mlx-core-quantize "Link to this heading")

[[quantize]][(]*[[w]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[group_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[bits]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mode]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'affine\']]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[,]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]][\#](#mlx.core.quantize "Link to this definition")

:   Quantize the array [`w`].

    Note, every [`group_size`] elements in a row of [`w`] are quantized together. Hence, the last dimension of [`w`] should be divisible by [`group_size`].

    ::: 
    Warning

    [`quantize`] only supports inputs with two or more dimensions with the last dimension divisible by [`group_size`]
    :::

    The supported quantization modes are [`"affine"`], [`"mxfp4"`], [`"mxfp8"`], and [`"nvfp4"`]. They are described in more detail below.

    Parameters[:]

    :   - **w** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Array to be quantized

        - **group_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The size of the group in [`w`] that shares a scale and bias. See supported values and defaults in the [[table of quantization modes]](#quantize-modes). Default: [`None`].

        - **bits** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The number of bits occupied by each element of [`w`] in the quantized array. See supported values and defaults in the [[table of quantization modes]](#quantize-modes). Default: [`None`].

        - **mode** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- The quantization mode. Default: [`"affine"`].

    Returns[:]

    :   A tuple with either two or three elements containing:

        - w_q (array): The quantized version of [`w`]

        - scales (array): The quantization scales

        - biases (array): The quantization biases (returned for [`mode=="affine"`]).

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

    Notes

    ::: pst-scrollable-table-container
    []
      mode     group size        bits                   scale type      bias
      -------- ----------------- ---------------------- --------------- ------
      affine   32, 64^\*^, 128   2, 3, 4^\*^, 5, 6, 8   same as input   yes
      mxfp4    32^\*^            4^\*^                  e8m0            no
      mxfp8    32^\*^            4^\*^                  e8m0            no
      nvfp4    16^\*^            4^\*^                  e4m3            no

      : [Quantization modes][\#](#id1 "Link to this table") 
    :::

    ^\*^ indicates the default value when unspecified.

    The [`"affine"`] mode quantizes groups of [\\(g\\)] consecutive elements in a row of [`w`]. For each group the quantized representation of each element [\\(\\hat\\)] is computed as follows:

    ::: 
    \\\[\\begin\\begin \\alpha &= \\max_i w_i \\\\ \\beta &= \\min_i w_i \\\\ s &= \\frac \\\\ \\hat &= \\textrm\\left( \\frac\\right). \\end\\end\\\]
    :::

    After the above computation, [\\(\\hat\\)] fits in [\\(b\\)] bits and is packed in an unsigned 32-bit integer from the lower to upper bits. For instance, for 4-bit quantization we fit 8 elements in an unsigned 32 bit integer where the 1st element occupies the 4 least significant bits, the 2nd bits 4-7 etc.

    To dequantize the elements of [`w`], we also save [\\(s\\)] and [\\(\\beta\\)] which are the returned [`scales`] and [`biases`] respectively.

    The [`"mxfp4"`], [`"mxfp8"`], and [`"nvfp4"`] modes similarly quantize groups of [\\(g\\)] elements of [`w`]. For the [`"mx"`] modes, the group size must be [`32`]. For [`"nvfp4"`] the group size must be 16. The elements are quantized to 4-bit or 8-bit precision floating-point values: E2M1 for [`"fp4"`] and E4M3 for [`"fp8"`]. There is a shared 8-bit scale per group. The [`"mx"`] modes us an E8M0 scale and the [`"nv"`] mode uses an E4M3 scale. Unlike [`affine`] quantization, these modes does not have a bias value.

    More details on the [`"mx"`] formats can be found in the [specification](https://www.opencompute.org/documents/ocp-microscaling-formats-mx-v1-0-spec-final-pdf).

[](mlx.core.put_along_axis.html "previous page")

previous

mlx.core.put_along_axis

[](mlx.core.quantized_matmul.html "next page")

next

mlx.core.quantized_matmul

Contents

- [[`quantize()`]](#mlx.core.quantize)

By MLX Contributors

© Copyright 2023, Apple.\