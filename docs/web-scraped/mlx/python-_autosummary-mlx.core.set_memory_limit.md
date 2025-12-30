# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_memory_limit.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.set_memory_limit.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.set_memory_limit

## Contents

- [[`set_memory_limit()`]](#mlx.core.set_memory_limit)

# mlx.core.set_memory_limit[\#](#mlx-core-set-memory-limit "Link to this heading")

[[set_memory_limit]][(]*[[limit]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][\#](#mlx.core.set_memory_limit "Link to this definition")

:   Set the memory limit.

    The memory limit is a guideline for the maximum amount of memory to use during graph evaluation. If the memory limit is exceeded and there is no more RAM (including swap when available) allocations will result in an exception.

    When metal is available the memory limit defaults to 1.5 times the maximum recommended working set size reported by the device.

    Parameters[:]

    :   **limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- Memory limit in bytes.

    Returns[:]

    :   The previous memory limit in bytes.

    Return type[:]

    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

[](mlx.core.get_cache_memory.html "previous page")

previous

mlx.core.get_cache_memory

[](mlx.core.set_cache_limit.html "next page")

next

mlx.core.set_cache_limit

Contents

- [[`set_memory_limit()`]](#mlx.core.set_memory_limit)

By MLX Contributors

© Copyright 2023, Apple.\