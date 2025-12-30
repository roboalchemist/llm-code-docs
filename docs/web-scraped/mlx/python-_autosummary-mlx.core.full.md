# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.full.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.full.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.full

## Contents

- [[`full()`]](#mlx.core.full)

# mlx.core.full[\#](#mlx-core-full "Link to this heading")

[[full]][(]*[[shape]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[vals]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[dtype]][[:]][ ][[[Dtype]](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.full "Link to this definition")

:   Construct an array with the given value.

    Constructs an array of size [`shape`] filled with [`vals`]. If [`vals`] is an [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") it must be broadcastable to the given [`shape`].

    Parameters[:]

    :   - **shape** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The shape of the output array.

        - **vals** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") *or* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Values to fill the array with.

        - **dtype** ([*Dtype*](mlx.core.Dtype.html#mlx.core.Dtype "mlx.core.Dtype")*,* *optional*) -- Data type of the output array. If unspecified the output type is inferred from [`vals`].

    Returns[:]

    :   The output array with the specified shape and values.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.floor_divide.html "previous page")

previous

mlx.core.floor_divide

[](mlx.core.gather_mm.html "next page")

next

mlx.core.gather_mm

Contents

- [[`full()`]](#mlx.core.full)

By MLX Contributors

© Copyright 2023, Apple.\