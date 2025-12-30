# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.grad.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.grad.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.grad

## Contents

- [[`grad()`]](#mlx.core.grad)

# mlx.core.grad[\#](#mlx-core-grad "Link to this heading")

[[grad]][(]*[[fun]][[:]][ ][[Callable]]*, *[[argnums]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")[[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[argnames]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][Sequence][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]][ ][[=]][ ][[\[\]]]*[)] [[→] [[Callable]]][\#](#mlx.core.grad "Link to this definition")

:   Returns a function which computes the gradient of [`fun`].

    Parameters[:]

    :   - **fun** (*Callable*) -- A function which takes a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or trees of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns a scalar output [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **argnums** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*),* *optional*) -- Specify the index (or indices) of the positional arguments of [`fun`] to compute the gradient with respect to. If neither [`argnums`] nor [`argnames`] are provided [`argnums`] defaults to [`0`] indicating [`fun`]'s first argument.

        - **argnames** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*(*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*),* *optional*) -- Specify keyword arguments of [`fun`] to compute gradients with respect to. It defaults to \[\] so no gradients for keyword arguments by default.

    Returns[:]

    :   A function which has the same input arguments as [`fun`] and returns the gradient(s).

    Return type[:]

    :   *Callable*

[](mlx.core.enable_compile.html "previous page")

previous

mlx.core.enable_compile

[](mlx.core.value_and_grad.html "next page")

next

mlx.core.value_and_grad

Contents

- [[`grad()`]](#mlx.core.grad)

By MLX Contributors

© Copyright 2023, Apple.\