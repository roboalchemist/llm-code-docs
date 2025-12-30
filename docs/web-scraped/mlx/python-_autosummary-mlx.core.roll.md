# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.roll.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.roll.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.roll

## Contents

- [[`roll()`]](#mlx.core.roll)

# mlx.core.roll[\#](#mlx-core-roll "Link to this heading")

[[roll]][(]*[[a]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[shift]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]]*, *[[axis]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Tuple][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]]][ ][[=]][ ][[None]]*, *[[/]]*, *[[\*]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.roll "Link to this definition")

:   Roll array elements along a given axis.

    Elements that are rolled beyond the end of the array are introduced at the beggining and vice-versa.

    If the axis is not provided the array is flattened, rolled and then the shape is restored.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array

        - **shift** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*)*) -- The number of places by which elements are shifted. If positive the array is rolled to the right, if negative it is rolled to the left. If an int is provided but the axis is a tuple then the same value is used for all axes.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- The axis or axes along which to roll the elements.

[](mlx.core.right_shift.html "previous page")

previous

mlx.core.right_shift

[](mlx.core.round.html "next page")

next

mlx.core.round

Contents

- [[`roll()`]](#mlx.core.roll)

By MLX Contributors

© Copyright 2023, Apple.\