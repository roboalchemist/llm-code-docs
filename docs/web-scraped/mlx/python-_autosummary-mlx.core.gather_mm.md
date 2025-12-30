# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.gather_mm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.gather_mm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.gather_mm

## Contents

- [[`gather_mm()`]](#mlx.core.gather_mm)

# mlx.core.gather_mm[\#](#mlx-core-gather-mm "Link to this heading")

[[gather_mm]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[lhs_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[rhs_indices]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[\*]]*, *[[sorted_indices]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.gather_mm "Link to this definition")

:   Matrix multiplication with matrix-level gather.

    Performs a gather of the operands with the given indices followed by a (possibly batched) matrix multiplication of two arrays. This operation is more efficient than explicitly applying a [[`take()`]](mlx.core.take.html#mlx.core.take "mlx.core.take") followed by a [[`matmul()`]](mlx.core.matmul.html#mlx.core.matmul "mlx.core.matmul").

    The indices [`lhs_indices`] and [`rhs_indices`] contain flat indices along the batch dimensions (i.e. all but the last two dimensions) of [`a`] and [`b`] respectively.

    For [`a`] with shape [`(A1,`]` `[`A2,`]` `[`...,`]` `[`AS,`]` `[`M,`]` `[`K)`], [`lhs_indices`] contains indices from the range [`[0,`]` `[`A1`]` `[`*`]` `[`A2`]` `[`*`]` `[`...`]` `[`*`]` `[`AS)`]

    For [`b`] with shape [`(B1,`]` `[`B2,`]` `[`...,`]` `[`BS,`]` `[`M,`]` `[`K)`], [`rhs_indices`] contains indices from the range [`[0,`]` `[`B1`]` `[`*`]` `[`B2`]` `[`*`]` `[`...`]` `[`*`]` `[`BS)`]

    If only one index is passed and it is sorted, the [`sorted_indices`] flag can be passed for a possible faster implementation.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array.

        - **lhs_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Integer indices for [`a`]. Default: [`None`]

        - **rhs_indices** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- Integer indices for [`b`]. Default: [`None`]

        - **sorted_indices** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- May allow a faster implementation if the passed indices are sorted. Default: [`False`].

    Returns[:]

    :   The output array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.full.html "previous page")

previous

mlx.core.full

[](mlx.core.gather_qmm.html "next page")

next

mlx.core.gather_qmm

Contents

- [[`gather_mm()`]](#mlx.core.gather_mm)

By MLX Contributors

© Copyright 2023, Apple.\