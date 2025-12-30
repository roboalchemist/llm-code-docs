# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.compile.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.compile.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.compile

## Contents

- [[`compile()`]](#mlx.core.compile)

# mlx.core.compile[\#](#mlx-core-compile "Link to this heading")

[[compile]][(]*[[fun]][[:]][ ][[Callable]]*, *[[inputs]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[outputs]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[shapeless]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[Callable]]][\#](#mlx.core.compile "Link to this definition")

:   Returns a compiled function which produces the same output as [`fun`].

    Parameters[:]

    :   - **fun** (*Callable*) -- A function which takes a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or trees of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or trees of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **inputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") *or* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*,* *optional*) -- These inputs will be captured during the function compilation along with the inputs to [`fun`]. The [`inputs`] can be a [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") or a [[`dict`]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") containing arbitrarily nested lists, dictionaries, or arrays. Leaf nodes that are not [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") are ignored. Default: [`None`]

        - **outputs** ([*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") *or* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*,* *optional*) -- These outputs will be captured and updated in a compiled function. The [`outputs`] can be a [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") or a [[`dict`]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") containing arbitrarily nested lists, dictionaries, or arrays. Leaf nodes that are not [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") are ignored. Default: [`None`]

        - **shapeless** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- A function compiled with the [`shapeless`] option enabled will not be recompiled when the input shape changes. Not all functions can be compiled with [`shapeless`] enabled. Attempting to compile such functions with shapeless enabled will throw. Note, changing the number of dimensions or type of any input will result in a recompilation even with [`shapeless`] set to [`True`]. Default: [`False`]

    Returns[:]

    :   A compiled function which has the same input arguments as [`fun`] and returns the the same output(s).

    Return type[:]

    :   *Callable*

[](mlx.core.async_eval.html "previous page")

previous

mlx.core.async_eval

[](mlx.core.custom_function.html "next page")

next

mlx.core.custom_function

Contents

- [[`compile()`]](#mlx.core.compile)

By MLX Contributors

© Copyright 2023, Apple.\