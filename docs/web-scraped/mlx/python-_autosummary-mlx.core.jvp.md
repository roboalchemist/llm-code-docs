# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.jvp.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.jvp.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.jvp

## Contents

- [[`jvp()`]](#mlx.core.jvp)

# mlx.core.jvp[\#](#mlx-core-jvp "Link to this heading")

[[jvp]][(]*[[fun]][[:]][ ][[Callable]]*, *[[primals]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*, *[[tangents]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]]]*[)] [[→] [[[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[,]][ ][[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[array]](mlx.core.array.html#mlx.core.array "mlx.core.array")[[\]]][[\]]]]][\#](#mlx.core.jvp "Link to this definition")

:   Compute the Jacobian-vector product.

    This computes the product of the Jacobian of a function [`fun`] evaluated at [`primals`] with the [`tangents`].

    Parameters[:]

    :   - **fun** (*Callable*) -- A function which takes a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns a single [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **primals** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- A list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") at which to evaluate the Jacobian.

        - **tangents** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")*)*) -- A list of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") which are the "vector" in the Jacobian-vector product. The [`tangents`] should be the same in number, shape, and type as the inputs of [`fun`] (i.e. the [`primals`]).

    Returns[:]

    :   A tuple with the outputs of [`fun`] in the first position and the Jacobian-vector products in the second position.

    Return type[:]

    :   [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")), [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")))

    Example

    :::: 
    ::: highlight
        import mlx.core as mx

        outs, jvps = mx.jvp(mx.sin, (mx.array(1.0),), (mx.array(1.0),))
    :::
    ::::

[](mlx.core.value_and_grad.html "previous page")

previous

mlx.core.value_and_grad

[](mlx.core.vjp.html "next page")

next

mlx.core.vjp

Contents

- [[`jvp()`]](#mlx.core.jvp)

By MLX Contributors

© Copyright 2023, Apple.\