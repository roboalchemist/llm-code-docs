# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_cache_limit.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.set_cache_limit.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.set_cache_limit

## Contents

- [[`set_cache_limit()`]](#mlx.core.set_cache_limit)

# mlx.core.set_cache_limit[\#](#mlx-core-set-cache-limit "Link to this heading")

[[set_cache_limit]][(]*[[limit]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][\#](#mlx.core.set_cache_limit "Link to this definition")

:   Set the free cache limit.

    If using more than the given limit, free memory will be reclaimed from the cache on the next allocation. To disable the cache, set the limit to [`0`].

    The cache limit defaults to the memory limit. See [[`set_memory_limit()`]](mlx.core.set_memory_limit.html#mlx.core.set_memory_limit "mlx.core.set_memory_limit") for more details.

    Parameters[:]

    :   **limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The cache limit in bytes.

    Returns[:]

    :   The previous cache limit in bytes.

    Return type[:]

    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

[](mlx.core.set_memory_limit.html "previous page")

previous

mlx.core.set_memory_limit

[](mlx.core.set_wired_limit.html "next page")

next

mlx.core.set_wired_limit

Contents

- [[`set_cache_limit()`]](#mlx.core.set_cache_limit)

By MLX Contributors

© Copyright 2023, Apple.\