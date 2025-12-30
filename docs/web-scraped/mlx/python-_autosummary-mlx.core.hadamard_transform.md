# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.hadamard_transform.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.hadamard_transform.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.hadamard_transform

## Contents

- [[`hadamard_transform()`]](#mlx.core.hadamard_transform)

# mlx.core.hadamard_transform[\#](#mlx-core-hadamard-transform "Link to this heading")

[[hadamard_transform]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[scale]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.hadamard_transform "Link to this definition")

:   Perform the Walsh-Hadamard transform along the final axis.

    Equivalent to:

    :::: 
    ::: highlight
        from scipy.linalg import hadamard

        y = (hadamard(len(x)) @ x) * scale
    :::
    ::::

    Supports sizes [`n`]` `[`=`]` `[`m*2^k`] for [`m`] in [`(1,`]` `[`12,`]` `[`20,`]` `[`28)`] and [`2^k`]` `[`<=`]` `[`8192`] for float32 and [`2^k`]` `[`<=`]` `[`16384`] for float16/bfloat16.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **scale** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) -- Scale the output by this factor. Defaults to [`1/sqrt(a.shape[-1])`] so that the Hadamard matrix is orthonormal.

    Returns[:]

    :   The transformed array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.greater_equal.html "previous page")

previous

mlx.core.greater_equal

[](mlx.core.identity.html "next page")

next

mlx.core.identity

Contents

- [[`hadamard_transform()`]](#mlx.core.hadamard_transform)

By MLX Contributors

© Copyright 2023, Apple.\