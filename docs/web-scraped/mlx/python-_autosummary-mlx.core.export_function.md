# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.export_function.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.export_function.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.export_function

## Contents

- [[`export_function()`]](#mlx.core.export_function)

# mlx.core.export_function[\#](#mlx-core-export-function "Link to this heading")

[[export_function]][(]*[[arg0]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]*, *[[fun]][[:]][ ][[[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")]*, *[[\*]][[args]]*, *[[shapeless]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*, *[[\*\*]][[kwargs]]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#mlx.core.export_function "Link to this definition")

:   Export an MLX function.

    Example input arrays must be provided to export a function. The example inputs can be variable [`*args`] and [`**kwargs`] or a tuple of arrays and/or dictionary of string keys with array values.

    ::: 
    Warning

    This is part of an experimental API which is likely to change in future versions of MLX. Functions exported with older versions of MLX may not be compatible with future versions.
    :::

    Parameters[:]

    :   - **file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *or* *Callable*) -- Either a file path to export the function to or a callback.

        - **fun** (*Callable*) -- A function which takes as input zero or more [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns one or more [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **\*args** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Example array inputs to the function.

        - **shapeless** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether or not the function allows inputs with variable shapes. Default: [`False`].

        - **\*\*kwargs** ([*array*](mlx.core.array.html#mlx.core.array "mlx.core.array")) -- Additional example keyword array inputs to the function.

    Example

    :::: 
    ::: highlight
        def fun(x, y):
            return x + y

        x = mx.array(1)
        y = mx.array([1, 2, 3])
        mx.export_function("fun.mlxfn", fun, x, y=y)
    :::
    ::::

[](../export.html "previous page")

previous

Export Functions

[](mlx.core.import_function.html "next page")

next

mlx.core.import_function

Contents

- [[`export_function()`]](#mlx.core.export_function)

By MLX Contributors

© Copyright 2023, Apple.\