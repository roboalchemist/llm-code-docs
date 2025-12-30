# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.contiguous.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.contiguous.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.contiguous

## Contents

- [[`contiguous()`]](#mlx.core.contiguous)

# mlx.core.contiguous[\#](#mlx-core-contiguous "Link to this heading")

[[contiguous]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[/]]*, *[[allow_col_major]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.contiguous "Link to this definition")

:   Force an array to be row contiguous. Copy if necessary.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- The input to make contiguous

        - **allow_col_major** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) -- Consider column major as contiguous and don't copy

    Returns[:]

    :   The row or col contiguous output.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.concatenate.html "previous page")

previous

mlx.core.concatenate

[](mlx.core.conj.html "next page")

next

mlx.core.conj

Contents

- [[`contiguous()`]](#mlx.core.contiguous)

By MLX Contributors

© Copyright 2023, Apple.\