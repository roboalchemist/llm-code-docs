# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.import_function.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.import_function.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.import_function

## Contents

- [[`import_function()`]](#mlx.core.import_function)

# mlx.core.import_function[\#](#mlx-core-import-function "Link to this heading")

[[import_function]][(]*[[file]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[Callable]]][\#](#mlx.core.import_function "Link to this definition")

:   Import a function from a file.

    The imported function can be called either with [`*args`] and [`**kwargs`] or with a tuple of arrays and/or dictionary of string keys with array values. Imported functions always return a tuple of arrays.

    ::: 
    Warning

    This is part of an experimental API which is likely to change in future versions of MLX. Functions exported with older versions of MLX may not be compatible with future versions.
    :::

    Parameters[:]

    :   **file** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) -- The file path to import the function from.

    Returns[:]

    :   The imported function.

    Return type[:]

    :   *Callable*

    Example

    :::: 
    ::: highlight
        >>> fn = mx.import_function("function.mlxfn")
        >>> out = fn(a, b, x=x, y=y)[0]
        >>>
        >>> out = fn((a, b), [0]
    :::
    ::::

[](mlx.core.export_function.html "previous page")

previous

mlx.core.export_function

[](mlx.core.exporter.html "next page")

next

mlx.core.exporter

Contents

- [[`import_function()`]](#mlx.core.import_function)

By MLX Contributors

© Copyright 2023, Apple.\