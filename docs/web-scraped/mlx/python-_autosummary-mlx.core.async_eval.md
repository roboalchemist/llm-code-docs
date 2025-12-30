# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.async_eval.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.async_eval.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.async_eval

## Contents

- [[`async_eval()`]](#mlx.core.async_eval)

# mlx.core.async_eval[\#](#mlx-core-async-eval "Link to this heading")

[[async_eval]][(]*[[\*]][[args]]*[)][\#](#mlx.core.async_eval "Link to this definition")

:   Asynchronously evaluate an [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or tree of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

    ::: 
    Note

    This is an experimental API and may change in future versions.
    :::

    Parameters[:]

    :   **\*args** (*arrays* *or* *trees* *of* *arrays*) -- Each argument can be a single array or a tree of arrays. If a tree is given the nodes can be a Python [[`list`]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), [[`tuple`]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") or [[`dict`]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)"). Leaves which are not arrays are ignored.

    Example

    :::: 
    ::: highlight
        >>> x = mx.array(1.0)
        >>> y = mx.exp(x)
        >>> mx.async_eval(y)
        >>> print(y)
        >>>
        >>> y = mx.exp(x)
        >>> mx.async_eval(y)
        >>> z = y + 3
        >>> mx.async_eval(z)
        >>> print(z)
    :::
    ::::

[](mlx.core.eval.html "previous page")

previous

mlx.core.eval

[](mlx.core.compile.html "next page")

next

mlx.core.compile

Contents

- [[`async_eval()`]](#mlx.core.async_eval)

By MLX Contributors

© Copyright 2023, Apple.\