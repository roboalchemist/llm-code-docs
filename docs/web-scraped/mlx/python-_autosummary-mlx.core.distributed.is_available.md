# Source: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.is_available.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../../_sources/python/_autosummary/mlx.core.distributed.is_available.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# mlx.core.distributed.is_available

## Contents

- [[`is_available()`]](#mlx.core.distributed.is_available)

# mlx.core.distributed.is_available[\#](#mlx-core-distributed-is-available "Link to this heading")

[[is_available]][(]*[[backend]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")][ ][[=]][ ][[\'any\']]*[)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][\#](#mlx.core.distributed.is_available "Link to this definition")

:   Check if a communication backend is available.

    Note, this function returns whether MLX has the capability of instantiating that distributed backend not whether it is possible to create a communication group. For that purpose one should use [`init(strict=True)`].

    Parameters[:]

    :   **backend** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) -- The name of the backend to check for availability. It takes the same values as [[`init()`]](mlx.core.distributed.init.html#mlx.core.distributed.init "mlx.core.distributed.init"). Default: [`"any"`].

    Returns[:]

    :   Whether the distributed backend is available.

    Return type[:]

    :   [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

[](mlx.core.distributed.Group.html "previous page")

previous

mlx.core.distributed.Group

[](mlx.core.distributed.init.html "next page")

next

mlx.core.distributed.init

Contents

- [[`is_available()`]](#mlx.core.distributed.is_available)

By MLX Contributors

© Copyright 2023, Apple.\