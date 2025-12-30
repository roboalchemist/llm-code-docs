# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.addmm.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.addmm.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.addmm

## Contents

- [[`addmm()`]](#mlx.core.addmm)

# mlx.core.addmm[\#](#mlx-core-addmm "Link to this heading")

[[addmm]][(]*[[c]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[alpha]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[beta]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[1.0]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.addmm "Link to this definition")

:   Matrix multiplication with addition and optional scaling.

    Perform the (possibly batched) matrix multiplication of two arrays and add to the result with optional scaling factors.

    Parameters[:]

    :   - **c** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **alpha** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Scaling factor for the matrix product of [`a`] and [`b`] (default: [`1`])

        - **beta** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Scaling factor for [`c`] (default: [`1`])

    Returns[:]

    :   [`alpha`]` `[`*`]` `[`(a`]` `[`@`]` `[`b)`]`  `[`+`]` `[`beta`]` `[`*`]` `[`c`]

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.add.html "previous page")

previous

mlx.core.add

[](mlx.core.all.html "next page")

next

mlx.core.all

Contents

- [[`addmm()`]](#mlx.core.addmm)

By MLX Contributors

© Copyright 2023, Apple.\