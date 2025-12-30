# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.vjp.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.vjp.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.vjp

## Contents

- [[`vjp()`]](#mlx.core.vjp)

# mlx.core.vjp[\#](#mlx-core-vjp "Link to this heading")

[[vjp]][(]*[[fun]][[:]][ ][[Callable]]*, *[[primals]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[cotangents]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[\]]]]][\#](#mlx.core.vjp "Link to this definition")

:   Compute the vector-Jacobian product.

    Computes the product of the [`cotangents`] with the Jacobian of a function [`fun`] evaluated at [`primals`].

    Parameters[:]

    :   - **fun** (*Callable*) -- A function which takes a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns a single [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **primals** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- A list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") at which to evaluate the Jacobian.

        - **cotangents** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- A list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") which are the "vector" in the vector-Jacobian product. The [`cotangents`] should be the same in number, shape, and type as the outputs of [`fun`].

    Returns[:]

    :   A tuple with the outputs of [`fun`] in the first position and the vector-Jacobian products in the second position.

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")), [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")))

    Example

    :::: 
    ::: highlight
        import mlx.core as mx

        outs, vjps = mx.vjp(mx.sin, (mx.array(1.0),), (mx.array(1.0),))
    :::
    ::::

[](mlx.core.jvp.html "previous page")

previous

mlx.core.jvp

[](mlx.core.vmap.html "next page")

next

mlx.core.vmap

Contents

- [[`vjp()`]](#mlx.core.vjp)

By MLX Contributors

© Copyright 2023, Apple.\