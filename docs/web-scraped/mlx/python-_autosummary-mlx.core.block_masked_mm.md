# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.block_masked_mm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.block_masked_mm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.block_masked_mm

## Contents

- [[`block_masked_mm()`]](#mlx.core.block_masked_mm)

# mlx.core.block_masked_mm[\#](#mlx-core-block-masked-mm "Link to this heading")

[[block_masked_mm]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[block_size]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[64]]*, *[[mask_out]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mask_lhs]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[mask_rhs]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.block_masked_mm "Link to this definition")

:   Matrix multiplication with block masking.

    Perform the (possibly batched) matrix multiplication of two arrays and with blocks of size [`block_size`]` `[`x`]` `[`block_size`] optionally masked out.

    Assuming [`a`] with shape (..., M, K) and b with shape (..., K, N)

    - [`lhs_mask`] must have shape (..., [\\(\\lceil\\)] M / [`block_size`] [\\(\\rceil\\)], [\\(\\lceil\\)] K / [`block_size`] [\\(\\rceil\\)])

    - [`rhs_mask`] must have shape (..., [\\(\\lceil\\)] K / [`block_size`] [\\(\\rceil\\)], [\\(\\lceil\\)] N / [`block_size`] [\\(\\rceil\\)])

    - [`out_mask`] must have shape (..., [\\(\\lceil\\)] M / [`block_size`] [\\(\\rceil\\)], [\\(\\lceil\\)] N / [`block_size`] [\\(\\rceil\\)])

    Note: Only [`block_size=64`] and [`block_size=32`] are currently supported

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **block_size** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Size of blocks to be masked. Must be [`32`] or [`64`]. Default: [`64`].

        - **mask_out** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Mask for output. Default: [`None`].

        - **mask_lhs** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Mask for [`a`]. Default: [`None`].

        - **mask_rhs** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Mask for [`b`]. Default: [`None`].

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.bitwise_xor.html "previous page")

previous

mlx.core.bitwise_xor

[](mlx.core.broadcast_arrays.html "next page")

next

mlx.core.broadcast_arrays

Contents

- [[`block_masked_mm()`]](#mlx.core.block_masked_mm)

By MLX Contributors

© Copyright 2023, Apple.\