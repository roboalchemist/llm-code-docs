# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_wired_limit.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.set_wired_limit.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.set_wired_limit

## Contents

- [[`set_wired_limit()`]](#mlx.core.set_wired_limit)

# mlx.core.set_wired_limit[\#](#mlx-core-set-wired-limit "Link to this heading")

[[set_wired_limit]][(]*[[limit]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]][\#](#mlx.core.set_wired_limit "Link to this definition")

:   Set the wired size limit.

    ::: 
    Note

    - This function is only useful on macOS 15.0 or higher.

    - The wired limit should remain strictly less than the total memory size.
    :::

    The wired limit is the total size in bytes of memory that will be kept resident. The default value is [`0`].

    Setting a wired limit larger than system wired limit is an error. You can increase the system wired limit with:

    :::: 
    ::: highlight
        sudo sysctl iogpu.wired_limit_mb=<size_in_megabytes>
    :::
    ::::

    Use [`device_info()`] to query the system wired limit ([`"max_recommended_working_set_size"`]) and the total memory size ([`"memory_size"`]).

    Parameters[:]

    :   **limit** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) -- The wired limit in bytes.

    Returns[:]

    :   The previous wired limit in bytes.

    Return type[:]

    :   [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

[](mlx.core.set_cache_limit.html "previous page")

previous

mlx.core.set_cache_limit

[](mlx.core.clear_cache.html "next page")

next

mlx.core.clear_cache

Contents

- [[`set_wired_limit()`]](#mlx.core.set_wired_limit)

By MLX Contributors

© Copyright 2023, Apple.\