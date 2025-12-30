# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.permutation.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.random.permutation.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.random.permutation

## Contents

- [[`permutation()`]](#mlx.core.random.permutation)

# mlx.core.random.permutation[\#](#mlx-core-random-permutation "Link to this heading")

[[permutation]][(]*[[x]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[axis]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[key]][[:]][ ][[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.random.permutation "Link to this definition")

:   Generate a random permutation or permute the entries of an array.

    Parameters[:]

    :   - **x** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- If an integer is provided a random permtuation of [`mx.arange(x)`] is returned. Otherwise the entries of [`x`] along the given axis are randomly permuted.

        - **axis** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- The axis to permute along. Default: [`0`].

        - **key** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*,* *optional*) -- A PRNG key. Default: [`None`].

    Returns[:]

    :   The generated random permutation or randomly permuted input array.

    Return type[:]

    :   [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")

[](mlx.core.random.laplace.html "previous page")

previous

mlx.core.random.laplace

[](../transforms.html "next page")

next

Transforms

Contents

- [[`permutation()`]](#mlx.core.random.permutation)

By MLX Contributors

© Copyright 2023, Apple.\