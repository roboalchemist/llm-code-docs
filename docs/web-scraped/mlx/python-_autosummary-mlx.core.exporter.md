# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.exporter.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.exporter.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.exporter

## Contents

- [[`exporter()`]](#mlx.core.exporter)

# mlx.core.exporter[\#](#mlx-core-exporter "Link to this heading")

[[exporter]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[fun]][[:]][ ][[[Callable]](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")]*, *[[\*]]*, *[[shapeless]][[:]][ ][[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")][ ][[=]][ ][[False]]*[)] [[→] [[mlx.core.FunctionExporter]]][\#](#mlx.core.exporter "Link to this definition")

:   Make a callable object to export multiple traces of a function to a file.

    ::: 
    Warning

    This is part of an experimental API which is likely to change in future versions of MLX. Functions exported with older versions of MLX may not be compatible with future versions.
    :::

    Parameters[:]

    :   - **file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- File path to export the function to.

        - **shapeless** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) -- Whether or not the function allows inputs with variable shapes. Default: [`False`].

    Example

    :::: 
    ::: highlight
        def fun(*args):
            return sum(args)

        with mx.exporter("fun.mlxfn", fun) as exporter:
            exporter(mx.array(1))
            exporter(mx.array(1), mx.array(2))
            exporter(mx.array(1), mx.array(2), mx.array(3))
    :::
    ::::

[](mlx.core.import_function.html "previous page")

previous

mlx.core.import_function

[](mlx.core.export_to_dot.html "next page")

next

mlx.core.export_to_dot

Contents

- [[`exporter()`]](#mlx.core.exporter)

By MLX Contributors

© Copyright 2023, Apple.\