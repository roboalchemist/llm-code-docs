# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.matmul.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.matmul.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.matmul

## Contents

- [[`matmul()`]](#mlx.core.matmul)

# mlx.core.matmul[\#](#mlx-core-matmul "Link to this heading")

[[matmul]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.matmul "Link to this definition")

:   Matrix multiplication.

    Perform the (possibly batched) matrix multiplication of two arrays. This function supports broadcasting for arrays with more than two dimensions.

    - If the first array is 1-D then a 1 is prepended to its shape to make it a matrix. Similarly if the second array is 1-D then a 1 is appended to its shape to make it a matrix. In either case the singleton dimension is removed from the result.

    - A batched matrix multiplication is performed if the arrays have more than 2 dimensions. The matrix dimensions for the matrix product are the last two dimensions of each input.

    - All but the last two dimensions of each input are broadcast with one another using standard numpy-style broadcasting semantics.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

    Returns[:]

    :   The matrix product of [`a`] and [`b`].

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.logsumexp.html "previous page")

previous

mlx.core.logsumexp

[](mlx.core.max.html "next page")

next

mlx.core.max

Contents

- [[`matmul()`]](#mlx.core.matmul)

By MLX Contributors

© Copyright 2023, Apple.\