# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.divmod.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.divmod.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.divmod

## Contents

- [[`divmod()`]](#mlx.core.divmod)

# mlx.core.divmod[\#](#mlx-core-divmod "Link to this heading")

[[divmod]][(]*[[a]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[b]][[:]][ ][[scalar][ ][[\|]][ ][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]*, *[[stream]][[:]][ ][[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[ ][[\|]][ ][[Stream]](stream_class.html#mlx.core.Stream "mlx.core.Stream")[ ][[\|]][ ][[Device]](mlx.core.Device.html#mlx.core.Device "mlx.core.Device")][ ][[=]][ ][[None]]*[)] [[→] [[[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")]][\#](#mlx.core.divmod "Link to this definition")

:   Element-wise quotient and remainder.

    The fuction [`divmod(a,`]` `[`b)`] is equivalent to but faster than [`(a`]` `[`//`]` `[`b,`]` `[`a`]` `[`%`]` `[`b)`]. The function uses numpy-style broadcasting semantics. Either or both input arrays can also be scalars.

    Parameters[:]

    :   - **a** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

        - **b** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Input array or scalar.

    Returns[:]

    :   The quotient [`a`]` `[`//`]` `[`b`] and remainder [`a`]` `[`%`]` `[`b`].

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"), [*array*](mlx.core.array.html#mlx.core.array "mlx.core.array"))

[](mlx.core.divide.html "previous page")

previous

mlx.core.divide

[](mlx.core.einsum.html "next page")

next

mlx.core.einsum

Contents

- [[`divmod()`]](#mlx.core.divmod)

By MLX Contributors

© Copyright 2023, Apple.\