# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.vmap.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.vmap.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.vmap

## Contents

- [[`vmap()`]](#mlx.core.vmap)

# mlx.core.vmap[\#](#mlx-core-vmap "Link to this heading")

[[vmap]][(]*[[fun]][[:]][ ][[Callable]]*, *[[in_axes]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")][ ][[=]][ ][[0]]*, *[[out_axes]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")][ ][[=]][ ][[0]]*[)] [[→] [[Callable]]][\#](#mlx.core.vmap "Link to this definition")

:   Returns a vectorized version of [`fun`].

    Parameters[:]

    :   - **fun** (*Callable*) -- A function which takes a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or a tree of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") and returns a variable number of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array") or a tree of [[`array`]](mlx.core.array.html#mlx.core.array "mlx.core.array").

        - **in_axes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- An integer or a valid prefix tree of the inputs to [`fun`] where each node specifies the vmapped axis. If the value is [`None`] then the corresponding input(s) are not vmapped. Defaults to [`0`].

        - **out_axes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) -- An integer or a valid prefix tree of the outputs of [`fun`] where each node specifies the vmapped axis. If the value is [`None`] then the corresponding outputs(s) are not vmapped. Defaults to [`0`].

    Returns[:]

    :   The vectorized function.

    Return type[:]

    :   *Callable*

[](mlx.core.vjp.html "previous page")

previous

mlx.core.vjp

[](../fast.html "next page")

next

Fast

Contents

- [[`vmap()`]](#mlx.core.vmap)

By MLX Contributors

© Copyright 2023, Apple.\