# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.nan_to_num.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.nan_to_num.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.nan_to_num

## Contents

- [[`nan_to_num()`]](#mlx.core.nan_to_num)

# mlx.core.nan_to_num[\#](#mlx-core-nan-to-num "Link to this heading")

[[nan_to_num]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[nan]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[posinf]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[neginf]][[:]][ ][[[float]](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.nan_to_num "Link to this definition")

:   Replace NaN and Inf values with finite numbers.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **nan** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Value to replace NaN with. Default: [`0`].

        - **posinf** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Value to replace positive infinities with. If [`None`], defaults to largest finite value for the given data type. Default: [`None`].

        - **neginf** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) -- Value to replace negative infinities with. If [`None`], defaults to the negative of the largest finite value for the given data type. Default: [`None`].

    Returns[:]

    :   Output array with NaN and Inf replaced.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.multiply.html "previous page")

previous

mlx.core.multiply

[](mlx.core.negative.html "next page")

next

mlx.core.negative

Contents

- [[`nan_to_num()`]](#mlx.core.nan_to_num)

By MLX Contributors

© Copyright 2023, Apple.\